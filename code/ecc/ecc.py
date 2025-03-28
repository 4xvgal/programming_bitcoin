#ecc

class FieldElement:
    def __init__(self, num, prime): # 객체 초기화, num과 prime을 인수로 받은 후 num 값이 경곗값을 포함하여 0과 prime-1 값 사이에 있는지확인
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self): # 객체를 문자열로 변환 
        return 'FieldElement_{}({})'.format(self.prime, self.num)
    def __eq__(self, other): # FieldElement 클래스의 구 개체가 같은지 검사. 같으면 True, 다르면 False 반환
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self, other):
        return not (self == other) # __eq__의 반대 결과를 반환