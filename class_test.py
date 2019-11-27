class ClassA:
    explanation = '这是我的ClassA'
    def NormalMethod(self, name):
        print(self.explanation)
        print('可以输出外部参数{}'.format(name))

    @classmethod
    def ClassMethod(cls, explanation):
        print(cls.explanation)
        print(explanation)

    @staticmethod
    def StaticMethod(explanation):
        print(explanation)


if __name__ == '__main__':
    classa = ClassA()
    # classa.NormalMethod('hello')
    ClassA.NormalMethod('hello1','name')

    # classa.ClassMethod('ClassMethod')
    ClassA.ClassMethod('ClassMethod')