class Point:
    def __init__ (self, x,y,a,b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 +a *x +b:
            raise ValueError('({}, {}) is not on the curve'.format(x,y))
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b 
    
    def __add__(self,other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}. {} are not on the same curve'.format
                            (self, other))
        if self.x is None:
            return other
        
        if other.x is None:
            return self
        #역원 덧셈: 한점에 그의 역원을 더하는 경우
        if self.x == other.x and self.y == - other.y:
            return Point(None, None, self.a, self.b)
    

    def __str__(self):
        if self.x is None:
            return 'Point(infinity)'
        else:
            return f'Point({self.x}, {self.y})_curve({self.a}, {self.b})'
        
    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        else:
            return f'Point({self.x}, {self.y})_curve({self.a}, {self.b})'