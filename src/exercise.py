from operator import itemgetter
d={1:2,3:4,4:3,2:1,0:0}
d=sorted(d.items(),key=itemgetter(1))
print(d)
map()