#!/usr/bin/python

import cmd2 as cmd
import readline
import random
import config


class interpreter(cmd.Cmd):

    student = config.student
    people = config.people

    # Next answer
    answer = 0

    # No of correct answers
    count = 0

    # No of incorrect answers
    incorrect = 0

    # No of correct answers in a row
    roll = -1

    # Remaining "people"
    current_people = []

    # "No fingers" ceiling
    no_fingers = 5

    # Answer prompt
    prompt = '= '


    def init(self):
        print ""
        print ""
        print self.colorize("Hello %s! Here are some maths questions for you." % self.student, 'blue')
        print ""
        self.question()
        self.cmdloop()


    def question(self):

        self.roll += 1

        # 75% change to do addition, or 100% chance if within 5
        # questions of an incorrect answer (or when first starting)
        if self.roll < 5 or random.randint(1, 4) > 1:
            op = '+'
            mx = 10

            # Grab minimum of two random first numbers, lowers
            # the amount of higher numbers
            x1 = random.randint(1, mx - 1)
            x2 = random.randint(1, mx - 1)
            x = min(x1, x2)

            y = mx

            # Keep grabbing random second numbers until the add
            # up to under the mx value
            # There is also logic so that the questions get
            # progessively harder up to the mx value after an
            # incorrect answer (or when first starting)
            while x + y > mx or (min(x, y) > (self.roll + 1)):
                y = random.randint(1, mx - 1)

            # Save answer
            self.answer = x + y

            note = ''
            if self.answer <= self.no_fingers:
                note = '(no fingers!)'

        # 25% change to ask subtraction call
        else:
            op = '-'
            x = random.randint(2, 5)
            y = 3
            while x - y < 1:
                y = random.randint(1, 3)

            self.answer = x - y
            note = ''

        print ''
        print '%d %s %d %s' % (x, op, y, note)
        print ''


    def do_quit(self, data):
        print 'Done %d questions!' % self.count
        print '%d were incorrect' % self.incorrect
        print 'Good bye %s' % self.student
        return True


    def default(self, data):

        if len(self.current_people) < 1:
            self.current_people = self.people

        print ''
        if int(data) == self.answer:
            self.count += 1

            if random.randint(1, 5) == 4:
                if len(self.current_people) == 1:
                    p = 0
                else:
                    p = random.randint(1, len(self.current_people)) - 1

                person = self.current_people[p]
                del self.current_people[p]
                text = self.colorize('%s says well done!' % person, 'green')
            else:
                text = self.colorize('Well done %s!' % self.student, 'green')

            text += self.colorize(' That\'s %d correct!' % self.count, 'green')
            print text

            self.question()
        else:
            print self.colorize('Good try, try again %s :-)' % self.student, 'red')
            print ''

            self.roll = -1
            self.incorrect += 1



i = interpreter()
i.init()
