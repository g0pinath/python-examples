# Use of String Formatting
float1 = 121212563.78453
print("{:5.2f}".format(float1))

# Use of String Interpolation
float2 = 121212563.78453
print("%5.2f" % float2)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.236))