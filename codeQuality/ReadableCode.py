#  bad
x = 10

# good
user_age = 10

#  clever but confusing
result = [x*x for x in range(10) if x%2==0]

# readable
result = []
for num in range(10):
    if num % 2 == 0:
        result.append(num * num)



# Calculate final price after discount
final_price = price - discount


#add comments where needed