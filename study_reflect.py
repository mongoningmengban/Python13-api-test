# -*- coding:utf-8 _*-
"""
@author:mongo
@time: 2018/12/17
@email:3126972006@qq.com
@function： 反射
魔法一样
静态---运行前，如果要调用类的属性或者方法，我需要实例化它的对象
动态---运行时，我就获取类的属性或者方法，甚至更改它的属性或者方法
"""


class Girls:
    single = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def singe(self):
        print(self.name + "会唱歌")


if __name__ == '__main__':
    g = Girls('mongo', 18)
    print(g.name)
    g.singe()

    setattr(Girls, 'hub', 'swimming')  # 给类或者实例对象动态的去添加属性或者方法
    # print(g.hub)

    # g2 = Girls('lucy', 20)
    # print(g2.hub)
    # print(getattr(Girls, 'male'))  # 根据属性名获取类的属性,当属性不存在的时候，报AttributeError
    print(hasattr(Girls, 'male'))  # 判断当前这个类有没有这个属性,有就返回True，没有就返回False
    print(hasattr(Girls, 'single'))  # 判断类是否有这个类属性
    print(hasattr(g, 'name'))  # 判断对象是否有这个实例属性

    # delattr(g, 'name')  # 删除对象属性
    # print(g.name)

    delattr(Girls, 'single')  # 删除类属性
    print(getattr(Girls, 'single'))
