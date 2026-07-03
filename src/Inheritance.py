class a:
    def printt(self):
        print("this is parent class")

class b(a):
    def class_name(self):
        print("this is b's class")

single_inheritance=b()
single_inheritance.printt()

class aa:
    def printt(self):
        print("this is parent class")

class bb(aa):
    def class_name(self):
        print("this is b's class")

class cc(bb):
    def class_work(self):
        print("this is c's work")


multilevel_inheritance=cc()
multilevel_inheritance.class_name()
