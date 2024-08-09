class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def decomposer(version):
            v=[]
            sv=""
            for char in version:
                sv+=char
                if char==".":
                    v.append(int(sv[:-1]))
                    sv=""
            v.append(int(sv))
            return v

        v1=decomposer(version1)
        v2=decomposer(version2)

        nv1=len(v1)
        nv2=len(v2)

        if nv1>nv2:
            v2.extend([0]*(nv1-nv2))
        elif nv2>nv1:
            v1.extend([0]*(nv2-nv1))

        if v1<v2:
            return -1
        elif v1>v2:
            return 1
        else:
            return 0