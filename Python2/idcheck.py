import string

alphas = string.letters + '_'
nums   = string.digits

print 'BEGIN!'
myinput = raw_input('pls input:\n')

if len(myinput) > 1:
  if myinput[0] not in alphas:
    print 'error1'
  else:
    for otherChar in myinput[1:]:
      if otherChar not in alphas + nums:
        print 'error2'
        break
      print otherChar
    print 'OK'