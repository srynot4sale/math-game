#!/usr/bin/python

import cmd2 as cmd
import readline
import random


class interpreter(cmd.Cmd):

    student = 'Childname'
    people = ['Mum', 'Dad', 'Nan']

    answer = 0
    count = 0

    current_people = []


    def init(self):
        print ""
        print ""
        print self.colorize("Hello %s! Here are some maths questions for you." % self.student, 'blue')
        print ""
        self.question()
        self.cmdloop()


    def question(self):
        x = random.randint(1, 9)
        y = 10
        while x + y > 10:
            y = random.randint(1, 9)

        self.answer = x + y
        print ''
        print '%d + %d' % (x,y)
        print ''


    def do_quit(self, data):
        print 'Done %d questions!' % self.count
        print 'Good bye %s' % self.student
        return True


    def default(self, data):

        if len(self.current_people) < 1:
            self.current_people = self.people

        print ''
        if int(data) == self.answer:
            self.count += 1

            if random.randint(1, 5) == 4:
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



i = interpreter()
i.init()
