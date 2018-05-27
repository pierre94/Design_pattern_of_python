# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Adapter
@time: 27/05/2018 7:20 PM
"""
class AStaff:
    name = ""
    id = ""
    phone = ""

    def __init__(self, id):
        self.id = id

    def getName(self):
        print "A protocol getName method ... id:%s" % self.id
        return self.name

    def getPhone(self):
        print "A protocol getPhone method ... id:%s" % self.id
        return self.phone

    def setName(self, xname):
        print "A protocol setName method ... id:%s" % self.id
        self.name = xname

    def setPhone(self, xphone):
        print "A protocol setPhone method ... id:%s" % self.id
        self.phone = xphone

class BStaff:
    name = ""
    id = ""
    telephone = ""

    def __init__(self, id):
        self.id = id

    def getName(self):
        print "B protocol getName method ... id:%s" % self.id
        return self.name

    def getTelephone(self):
        print "B protocol getTelephone method ... id:%s" % self.id
        return self.telephone

    def setName(self, xname):
        print "B protocol setName method ... id:%s" % self.id
        self.name = xname

    def setTelephone(self, xtelephone):
        print "B protocol setTelePhone method ... id:%s" % self.id
        self.telephone = xtelephone


class BStaffAdapter:
    b_cpn = ""

    def __init__(self, id):
        self.b_cpn = BStaff(id)

    def setPhone(self, xphone):
        self.b_cpn.setTelephone(xphone)

    def getPhone(self):
        return self.b_cpn.getTelephone()

    def setName(self, xname):
        self.b_cpn.setName(xname)

    def getName(self):
        return self.b_cpn.name

"""
A公司想用B公司的接口时，直接调用B公司的接口是个办法，但是会对现有的业务流程造成不确定的风险。为了减少耦合，使用适配器将B公司的接口进行封装，
从而对外接口实现与A公司的一致.
实际设计系统时，避免使用适配器模式
"""
if __name__ == '__main__':
    a_staff = AStaff("123")
    a_staff.setName("A-123")
    a_staff.setPhone("12345678")

    b_staff = BStaffAdapter("456")
    b_staff.setPhone("87654321")
    b_staff.setName("B-456")
    print "B's name is %s" % b_staff.getName()
    print "B's telephone is %s" % b_staff.getPhone()
