def changecase(func):
  print("hello")
  def myinner():
      print(11)
      return func().upper()
  return myinner

def addgreeting(func):
  print(1)
  def myinner():
      print(2)
      return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())
