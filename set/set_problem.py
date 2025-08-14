st1 = {10,20,10,20,30,40}

st2 = {20,30,30,10,50,60,40}

inters = st2.issuperset(st1)

print(inters)

seta = {12,20,30,40}
setb = {30,40,50,60}
symm = seta.symmetric_difference(setb)
print(symm)


sachin_friends = ["rahul","ganguly","yuvi","zaheer","raina","dhoni"]
dhoni_friends = ["rahul","ganguly","yuvi","raina","kohli","sachin"]
sachin_friends=set(sachin_friends)
dhoni_friends=set(dhoni_friends)
all = sachin_friends.union(dhoni_friends)
print(all)
