
def varargs(arg1, *args):
    print "args is of " + str(type(args))
    print args[0]+args[2]
    print len(args)
varargs("one",1,2,3)
