# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Facade
@time: 30/05/2018 9:24 PM
"""


class AlarmSensor:
    def run(self):
        print "Alarm ring"


class WaterSprinker:
    def run(self):
        print "Spray Water"


class EmergencyDialer:
    def run(self):
        print "Dial 119"


class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinker = WaterSprinker()
        self.emergency_dialer = EmergencyDialer()

    def run_all(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()


"""
门面模式，也称外观模式。要求子系统的外部与内部的通信必须要通过一个统一的对象进行。
如本案例中所有类的启动都需要通过EmergencyFacade这个统一的对象实现。
有点：减少依赖。 提升安全（屏蔽内部细节，可以在门面进行灵活的控制）。
缺点：不符合开闭原则。一旦系统形成后需要变化，几乎只能重写门面代码。
"""
if __name__ == '__main__':
    emergency_facade = EmergencyFacade()
    emergency_facade.run_all()
