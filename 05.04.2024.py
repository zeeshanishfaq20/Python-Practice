def consec_val(n):
    if not 1 <= n <= 150:
        return "Write a number between 1 and 150"
    seq = ''
    for i in range(1, n+1):
        seq += str(i)
    return seq    
           
if __name__ == '__main__':
    n = int(input())
    print(consec_val(n))