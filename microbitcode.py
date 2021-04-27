def add_thread():
  lineno=0
  thread_no=input("What is the thread number?\n>")
  r = csv.reader(open('threads.txt'))
  lines = list(r)
  for i in range (0,len(lines)):
    if lines[i][0]==thread_no:
      lineno=i
      print(lines[i]) 
  new_comment=input("What would you like to add?\n>")
  lines[i].append(new_comment)
  print(lines[i]) 
  writer = csv.writer(open('threads.txt', 'w'))
  writer.writerows(lines)