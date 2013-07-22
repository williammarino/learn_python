from sys import argv

#set arguments for sys in
script, filename = argv

txt = open(filename)

print "here's your file %r:" % filename
print txt.read()
txt.close()


print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()