OTP = "1008"
n=0
t = 1
while n==0:
  user_otp = input("Enter OTP")
  if user_otp == OTP:
    name = input("Enter your name")
    city = input("Enter your city")
    print(f"Your name is:{name} and your city is: {city}")
    n =1
  elif user_otp != OTP and t <3:
    print("Wrong OTP")
    t += 1
  elif t == 3:
    print("One last trial left")
    t += 1
    continue
  elif t>3:
    print("You've exhausted the number of attempts. Please contact admin to recover password.")
    break

    