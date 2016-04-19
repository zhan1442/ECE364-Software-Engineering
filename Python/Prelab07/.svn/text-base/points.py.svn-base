class PointND:
    def __init__(self, *args):
        for item in args:
            if type(item) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.t = args
        self.n = len(args)

    def __str__(self):
        s = map('{:.2f}'.format, self.t)
        return '('+', '.join(s)+')'

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        tot = 0
        for i in range(self.n):
            tot += (self.t[i] - other.t[i])**2
        return tot ** (1/2)

    def nearestPoint(self, points):
        if not points:
            raise ValueError("Input cannot be empty.")
        nearest = points[0]
        min_dis = self.distanceFrom(points[0])
        for i in range(len(points)):
            if self.distanceFrom(points[i]) < min_dis:
                min_dis = self.distanceFrom(points[i])
                nearest = points[i]
        return nearest

    def clone(self):
        return PointND(*self.t)

    def __add__(self, other):
        if isinstance(other, PointND):
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            l = []
            for i in range(self.n):
                l.append(self.t[i] + other.t[i])
            return PointND(*tuple(l))
        if isinstance(other, float):
            l = []
            for i in range(self.n):
                l.append(self.t[i] + other)
            return PointND(*tuple(l))

    def __radd__(self, other):
        if isinstance(other, float):
            l = []
            for i in range(self.n):
                l.append(self.t[i] + other)
            return PointND(*tuple(l))

    def __sub__(self, other):
        if isinstance(other, PointND):
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            l = []
            for i in range(self.n):
                l.append(self.t[i] - other.t[i])
            return PointND(*tuple(l))
        if isinstance(other, float):
            l = []
            for i in range(self.n):
                l.append(self.t[i] - other)
            return PointND(*tuple(l))

    def __mul__(self, other):
        if isinstance(other, PointND):
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            l = []
            for i in range(self.n):
                l.append(self.t[i] * other.t[i])
            return PointND(*tuple(l))
        if isinstance(other, float):
            l = []
            for i in range(self.n):
                l.append(self.t[i] * other)
            return PointND(*tuple(l))

    def __rmul__(self, other):
        if isinstance(other, float):
            l = []
            for i in range(self.n):
                l.append(self.t[i] * other)
            return PointND(*tuple(l))

    def __truediv__(self, other):
        if isinstance(other, PointND):
            if self.n != other.n:
                raise ValueError("Cannot operate on points with different cardinalities.")
            l = []
            for i in range(self.n):
                l.append(self.t[i] / other.t[i])
            return PointND(*tuple(l))
        if isinstance(other, float):
            l = []
            for i in range(self.n):
                l.append(self.t[i] / other)
            return PointND(*tuple(l))

    def __neg__(self):
        l = []
        for i in range(self.n):
            l.append(-self.t[i])
        return PointND(*tuple(l))

    def __getitem__(self, i):
        return self.t[i]

    def __eq__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        for i in range(self.n):
            if self.t[i] != other.t[i]:
                return False
        return True

    def __ne__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        for i in range(self.n):
            if self.t[i] == other.t[i]:
                return False
        return True

    def __gt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        l = []
        for i in range(self.n):
            l.append(0.0)
        p = PointND(*tuple(l))
        if self.distanceFrom(p) > other.distanceFrom(p):
            return True
        return False

    def __ge__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        l = []
        for i in range(self.n):
            l.append(0.0)
        p = PointND(*tuple(l))
        if self.distanceFrom(p) >= other.distanceFrom(p):
            return True
        return False

    def __lt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        l = []
        for i in range(self.n):
            l.append(0.0)
        p = PointND(*tuple(l))
        if self.distanceFrom(p) < other.distanceFrom(p):
            return True
        return False

    def __le__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot operate on points with different cardinalities.")
        l = []
        for i in range(self.n):
            l.append(0.0)
        p = PointND(*tuple(l))
        if self.distanceFrom(p) <= other.distanceFrom(p):
            return True
        return False


class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z


class PointSet:
    def __init__(self, **kwargs):
        if 'pointList' not in kwargs.keys():
            raise KeyError("'pointList' input parameter not found.")
        if not kwargs['pointList'] or len(kwargs) > 1:
            raise ValueError("'pointList' input parameter cannot be empty.")
        self.points = set(kwargs['pointList'])
        self.n = kwargs['pointList'][0].n
        for p in self.points:
            if p.n != self.n:
                raise ValueError("Expecting a point with cardinality {0}.".format(self.n))

    def addPoint(self, p):
        if p.n != self.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        self.points.add(p)

    def count(self):
        return len(self.points)

    def computeBoundingHyperCube(self):
        min_cube = []
        max_cube = []
        for i in range(self.n):
            min_cube.append(list(self.points)[0][i])
            max_cube.append(list(self.points)[0][i])
        for p in self.points:
            for i in range(self.n):
                if p[i] > max_cube[i]:
                    max_cube[i] = p[i]
                elif p[i] < min_cube[i]:
                    min_cube[i] = p[i]
        return PointND(*tuple(min_cube)), PointND(*tuple(max_cube))

    def computeNearestNeighbors(self, otherPointSet):
        nearest_l = []
        for p in self.points:
            nearest = p.nearestPoint(list(otherPointSet.points))
            nearest_l.append((p, nearest))
        return nearest_l

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError("Expecting a point with cardinality {0}.".format(self.n))
        self.points.add(other)
        return self

    def __sub__(self, other):
        if other in self.points:
            self.points.remove(other)
        return self

    def __contains__(self, item):
        if item in self.points:
            return True
        return False












