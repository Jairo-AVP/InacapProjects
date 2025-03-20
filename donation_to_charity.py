"""
Donation to charity: The following if/elif/else statements will display a “thank you” message after someone donates to a charity; 
there will be a curated message based on how much was donated.

"""

donation = 1000

print("Thank you for you donation!")

if donation >= 1000:
    print("You've achieved platinum donor status.")
elif donation >= 500:
    print("You've achieved gold donor status.")
elif donation >= 100:
    print("You've achieved silver donor status.")
else:
    print("You've achieved bronze donor status.")