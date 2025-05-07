import pyotp
import pyperclip

secretKey = "[ENTER SECRET KEY]"

otp = pyotp.TOTP(secretKey)
otpCode = otp.now()

print(otpCode)
pyperclip.copy(otpCode)
