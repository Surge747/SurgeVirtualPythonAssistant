#MAGIC 8 BALL CODE
q=""
x=0
while q!="quit":
    a=0
    print("""This is the magic 8 ball ask a question or type quit to quit""")
    q=input("Enter Question here : ")
    x=len(q)
    while x>=14:
        x=x-13
    while a!=13:
        print("""Shaking the ball
░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░████████░░░░░░░
░░░░░██▒▒▒▒▒▒▒▒██░░░░░
░░░░█▒▒▒▒▒▒▒▒▒▒▒▒█░░░░
░░░█▒▒▒▒▒░░░░▒▒▒▒▒█░░░
░░█▒▒▒▒▒░░██░░▒▒▒▒▒█░░
░█▒▒▒▒▒░░█░░█░░▒▒▒▒▒█░
░█▒▒▒▒░░░░██░░░░▒▒▒▒█░
░█▒▒▒▒▒░░█░░█░░▒▒▒▒▒█░
░░█▒▒▒▒▒░░██░░▒▒▒▒▒█░░
░░░█▒▒▒▒▒░░░░▒▒▒▒▒█░░░
░░░░█▒▒▒▒▒▒▒▒▒▒▒▒█░░░░
░░░░░██▒▒▒▒▒▒▒▒██░░░░░
░░░░░░░████████░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░
""")
        a+=1
    if x==1:
        print("My sources say no.")
    elif x==2:
        print("Yes – definitely")
    elif x==3:
        print("Without a doubt.")
    elif x==4:
        print("It is decidedly so.")
    elif x==5:
        print("Signs point to yes.")
    elif x==6:
        print("Yes.")
    elif x==7:
        print("Most likely.")
    elif x==8:
        print("My reply is no.")
    elif x==9:
        print("Very doubtful.")
    elif x==10:
        print("Outlook good.")
    elif x==11:
        print("It is certain.")
    elif x==12:
        print("As I see it, yes.")
    elif x==13:
        print("Outlook not so good.")
        
