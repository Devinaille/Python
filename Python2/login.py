db = {}

def newuser():
  prompt = 'login desired:'
  while True:
    name = raw_input(prompt)
    if name in db:
      prompt = 'name taken, try another:'
      continue
    else:
      pwd = raw_input('passwd:')
      db[name] = pwd
      break
    

def olduser():
  name = raw_input('login:')
  pwd = raw_input('passwd:')
  passwd = db.get(name)
  if passwd == pwd:
    print 'Welcome'
  else:
    print 'login error'

def view():
  print db

def quit1():
  print 'bye!'
  quit()


def showmenu():
  prompt = '''
(N)ew User login
(E)xisting User login
(V)iew
(Q)uit
Enter choice:'''
  
  done = False
  while not done:
    chosen = False
    while not chosen:
      try:
        choice = raw_input(prompt).strip()[0].lower()
      except (EOFError, KeyboardInterrupt):
        choice = 'q'
        done   = True
      print '\nYou picked: [%s]' % choice
      if choice not in CMDs:
        print 'invalid option'
      else:
        CMDs[choice]()
        chosen = True
        
        

if __name__ == '__main__':
  CMDs = {'n': newuser, 'e': olduser, 'v': view, 'q': quit1}
  showmenu()
