def howMuth(n):
    tx = ""
    for i in range(n):
        tx=tx+"#"
    return tx+" "
fil = open("./text")
li = fil.read().split('\n')
fil.close()
n = 4
tx = howMuth(n)
for i in range(len(li)):
    li[i] = tx +li[i]
tx = "\n".join(li)
fil = open("out","w")
fil.write(tx)
fil.close()
print(tx)