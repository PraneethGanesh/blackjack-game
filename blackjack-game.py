import random
def card_generator(card_num):
 card_list=["a","1","2","3","4","5","6","7","8","9","j","q","k"]
 value_list=[1,2,3,4,5,6,7,8,9,10,10,10,10]
 n=random.randint(0,12)
 print(f"card{card_num}:{card_list[n]}")
 return value_list[n]
print("lets play blackjack!\n\n")
print("user card are:")
u_sum=0
u_sum+=card_generator(1)
u_sum+=card_generator(2)
choice=input("do you want card 3?").lower()
if choice=="yes":
 u_sum+=card_generator(3)
print(f"sum of your caard is {u_sum}")
print("\n\n")
print("computer card are:")
c_sum=0
c_sum+=card_generator(1)
c_sum+=card_generator(2)
print(f"sum of computer cards is {c_sum}")
if u_sum==c_sum:
 print("tie")
elif u_sum==21:
 print("you won")
elif u_sum>21:
 print("computer won")
elif u_sum>c_sum:
 print("you won")
else:
 print("computer won")  
