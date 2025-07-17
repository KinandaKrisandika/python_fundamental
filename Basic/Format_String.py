# We can use concantenate for adding other variable to the string
# Apart from that we can use F string for adding variable into the string

Addition = [2,4,6,8]
Total = sum(Addition) / len(Addition)
Multiple = Total * 1000000


print(f"It is Average of Addition : {int(Total)}")
print(f"And it is how to create comma in thousand numbers : {Multiple:,} ")