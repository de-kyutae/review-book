import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data  # __init__에 주어진 인수를 인스턴스 변수 data에 대입, 실제 데이터가 Variable의 data에 보관

data = np.array(1.0)
x = Variable(data)  # x는 데이터를 담는 상자
print(x.data)

# class Function:
#   def __call__(self, input): # call 메소드의 input : Variable 인스턴스
#     x = input.data # 데이터를 꺼낸다
#     y = x ** 2 # 실제 계산
#     output = Variable(y)
#     return output


class Function:
    def __call__(self, input):  # call 메서드 두가지 작업 : 1) 'Variable에서 데이터 찾기'와 2)'계산 결과를 Variable에 포장하기'
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):  # 구체적인 계산을 하는 메소드
        raise NotImplementedError()


class Square(Function):  # __ call __ 메서드 그대로 계승
    def forward(self, x):
        return x ** 2
