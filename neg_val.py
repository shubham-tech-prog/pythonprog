s = "INSTAGRAM"  # Define a string

print(s[6:9][::-1])     # [::-1] = reverse 'RAM' → 'MAR'


print(len(s))    # Prints the length of the string → 9

print(s[0:len(s)][::-1])   # Reversed = 'MARGATSNI'


print(s[0:9:2][::-1])  # Reversed = 'MRASI' 

print(s[::2][::-1])    # Reversed = 'MRASI'    

print(s[3:6:-1][::-1])     

print(s[9:0:-1][::-1])   # Reversed = 'NSTAGRAM'

print(s[::-1][::-1])     # Full reverse of the string, then reverse again → original string = 'INSTAGRAM'   

print(s[::-2][::-1])      # Then reversed = 'ISARM' 

print(s[-1:-9:-1][::-1])  # Reversed = 'ISTAGRAM' 

