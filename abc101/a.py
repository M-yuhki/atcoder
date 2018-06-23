s = input()
if(s == "++++"):
    print(4)
elif(s == "----"):
    print(-4)
elif(s == "+++-" or s == "++-+" or s == "+-++" or s == "-+++"):
    print(2)
elif(s == "---+" or s == "--+-" or s == "-+--" or s == "+---"):
    print(-2)
else:
    print(0)
