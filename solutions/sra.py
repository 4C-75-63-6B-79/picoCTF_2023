def findGCD(num1, num2):
    if(num1 % num2 == 0):
        return num2;
    return findGCD(num2, num1%num2);

def checkIfGCDOne(num1, num2):
    gcd = findGCD(num1, num2);
    if(gcd == 1):
        return True;
    else:
        return False;

def convertToBase10(num):
    arr = '';
    while(num // 256 > 0):
        arr = str(num % 256) + arr;
        num = num // 256
    return str(num) + arr;


plain_text = "TkOOWq9Zivyn7psX"
n = 68710609692670237571386690355447531294137474915252461168883218103929481784501
encrypted_text = 35477332725621769660212284883459684770715621433490853045499699354050733007634
d = 51434667453693473686843457011274553881519202482451574573594592145961209892037
e = 65537;


smallest_128_bit_number  = pow(2, 127);
start_n = smallest_128_bit_number * smallest_128_bit_number;

print(smallest_128_bit_number);

# while(True):
#     plain_number = pow(encrypted_text, d, start_n);
