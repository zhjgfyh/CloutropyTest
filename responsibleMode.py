# -*-coding:utf-8-*-

# Date: 2018.12.27
# ToDo: Learn designing mode - responsible mode

class Person:
    '''请假人'''
    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def getName(self):
        return self.__name

    def getDayoff(self):
        return self.__dayoff

    def getReason(self):
        return self.__reason

    def setLeader(self, leader):
        self.__leader = leader

    def request(self):
        print('{} 申请请假{}天，请假理由：{}'.format(self.__name, self.__dayoff, self.getReason()))

        if self.__leader is not None:
            self.__leader.handleRequest(self)

class Manager:
    '''公司管理人员'''
    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self.__nextHandler = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def setNextHandler(self, nextHandler):
        self.__nextHandler = nextHandler

    def getNextHandler(self):
        return self.__nextHandler

    def handleRequest(self, person):
        pass

class TeamLeader(Manager):
    '''小组长'''
    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if person.getDayoff() <= 2:
            print('同意{}请假。签字人：{}({})'.format(person.getName(), self.getName(), self.getTitle()))
        nexthander = self.getNextHandler()
        if nexthander is not None:
            nexthander.handleRequest(person)

class DeptManager(Manager):
    '''部门经理'''
    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if 2 < person.getDayoff() <= 10:
            print('同意{}请假。签字人：{}({})'.format(person.getName(), self.getName(), self.getTitle()))

        nexthander = self.getNextHandler()
        if nexthander is not None:
            nexthander.handleRequest(person)

class Director(Manager):
    '''老板'''
    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if person.getDayoff() > 10:
            print('同意{}请假。签字人：{}({})'.format(person.getName(), self.getName(), self.getTitle()))

        nexthander = self.getNextHandler()
        if nexthander is not None:
            nexthander.handleRequest(person)

class HR(Manager):
    '''行政人员'''
    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        print('{}的请假申请已经审核，情况属实！已备案处理。处理人{}'.format(person.getName(), self.getName()))

        nextHander = self.getNextHandler()

if __name__ == '__main__':
    teamLeader = TeamLeader('Eric', '小组长')
    manager = DeptManager('Leo', '研发经理')
    director = Director('老王', '公司老板')
    hr = HR('Tina', '行政总监')

    teamLeader.setNextHandler(manager)
    manager.setNextHandler(director)
    director.setNextHandler(hr)

    peter = Person('Peter', 2, '参加Google大会')
    peter.setLeader(teamLeader)
    peter.request()
    print('_' * 50)

    susan = Person('Susan', 10, '去欧洲旅游')
    susan.setLeader(teamLeader)
    susan.request()
    print('_' * 50)

    sam = Person('Sam', 22, '生病休息')
    sam.setLeader(teamLeader)
    sam.request()

