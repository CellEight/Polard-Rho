class polardRho():
    def __init__(self):
        return

    def f(self, x):
        return (x**2+1)%self._N

    def gcd(self, x, y):
        a,b = x,y
        if a == 0 or b == 0:
            return 0
        r = a%b
        while r!=0:
            a, b = b, r
            r = a%b
        return b

    def factor(self, N, t0=2, h0=2):
        self._N = N
        t, h = t0, h0
        d = self.gcd(N,h-t)
        while not (1<d<N and  d!=0):
            t = self.f(t)
            h = self.f(self.f(h))
            print(t,h)
            d = self.gcd(N,abs(h-t))
            print(d)
        if d==0:
            if t0==N:
                print("Method Failed, Try differnt (t0, h0) or f")
                return
            else:
                return factor(N,t0+1,h0+1)
        else:
            return d
