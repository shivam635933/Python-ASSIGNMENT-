# Python Program to Find the Largest Number in a List.

number = [20,50,90,100,10]
#sort() function sorts the list in the ascending order as you tell us int the session
number.sort()
#Now the largest number will be the last number in the list
print("Largest Number in the list is: ",number[-1])


# Python Program to Find the Second Largest Number in a List.

number = [20,50,90,100,10]
#sort() function sorts the list in the ascending order as you tell us int the session
number.sort()
#Now the second largest number will be the last number in the list
print("Second Largest Number in the list is: ",number[-2])


#Python Program to Merge Two List and Sort it

number1 =[30,20,40,90]
number2 =[20,80,100,90]
# I use + operator to merge both the List 
newnumber = number1+number2
print("Merged List is: ",newnumber)
#now using the sort() function I sort the merged list
newnumber.sort()
print("Merged List and Sort List is: ",newnumber)


#Pthyon Program to Swap the First and Last Value of a List

number = [20,30,50,100,90]

print("without swap the List is: ",number)
#now assiging the value of first to last and last to first
number[0],number[-1] = number[-1],number[0]
print("Swap list will be: ",number)
