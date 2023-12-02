#------------Ex1------------ 
# statt AVG() = SUM() / LEN()
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# def avg(list):
#     totel=sum(list)/len(list)
#     print(round(totel))
# avg(student_heights)

totelSum=0
totelLen=0
for item in student_heights:
    totelSum+=item
    totelLen+=1
print(round(totelSum/totelLen))


#------------Ex2------------ 
#stat max() or min()
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

maxNum=0
for item in student_scores:
    if maxNum < item:
        maxNum=item
print(f"The highest score in the class is: {maxNum}")

#------------Ex3------------ 
# range(1,11) : is for a value from 1 to 10 this shood
# be count the sum of even number in range()
#Write your code below this row 👇
sum=0
for item in range(1,101):
    if item % 2==0:
        sum+=item
print(sum)
## Nour 
