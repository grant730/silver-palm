import numpy

def pi_func(n=10):
    #numpy.random.seed()
    randlist = numpy.random.rand(n, 2)
    # print(randlist)
    sqrlist = randlist ** 2
    # print(sqrlist)
    sumlist = sqrlist.sum(axis=1)
    #print("sum is", sumlist)
    points_in_arc = sum(1 for x in sumlist if x <= 1.00)
    pi = 4.0 * (points_in_arc / n)
    print("points under arc:", points_in_arc, "  total points:", n, "pi:", pi)
    return (pi)

nlist = list(range(1,1001))
pilist = list(map(pi_func, nlist))
