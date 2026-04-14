class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a,b,c = sides
        if not (a+b>c and b+c>a and a+c>b):
            return []
        
        def safe_acos(x):
            return math.acos(max(-1,min(1,x))) # type: ignore

        A = safe_acos((b*b+c*c-a*a)/(2*b*c))
        B = safe_acos((a*a+c*c-b*b)/(2*a*c))
        C = safe_acos((b*b+a*a-c*c)/(2*b*a))

        ans = [math.degrees(A),math.degrees(B),math.degrees(C)] # type: ignore

        return sorted(ans)