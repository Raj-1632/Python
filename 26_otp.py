import otp
size = int(input("Enter the size of OTP you want to generate: "))
if size <= 0:
    print("Size must be a positive integer.")
else:
    otp = otp.generate_otp(size)
    print("Generated OTP:", otp)
    print("Size of OTP:", len(otp))