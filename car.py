class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印汽车的总里程"""
        print(f"This car has {self.odometer_reading} miles on it.")

class ElectricCar(Car):
    """电动车的独到之处"""

    def __init__(self,make,model,year):
        """
        初始化父类属性
        再初始化电动汽车的特有属性
        """

        super().__init__(make,model,year)
        self.battery_size=75

    def descriptive_battery(self):
        """打印一条描述电瓶容量的信息"""

        print(f"This car has a {self.battery_size}-KWH battery.")

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.descriptive_battery()  