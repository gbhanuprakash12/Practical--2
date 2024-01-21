fh = open('Prac-2.txt','w')
length = 5
width = 4
area = length * width
perimeter = 2 * (length + width)
fh.write('Area Of Rectangle: '+str(area)+'\n')
fh.write('Perimeter Of Rectangle: '+str(perimeter)+'\n')
fh.close()