

nos = int(input('how many student do you have'))

grads = dict()

for i in range(nos) :
  sn = input('write student name')
  sg = int(input(f' write {sn} grade'))
  grads[sn]= sg 
print (grads)

for key, value in grads.items(): 
    print(key, ":", value)
    if value >=90 :
      print('excellent')
    elif value  >= 75 :
      print('good ')
    else :
      print('needs improvement')
