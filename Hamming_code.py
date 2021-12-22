def encoding(original): 
    number = len(original)
    p=1
    for i in range(0,number):
        if 2**i >= number + i + 1:
            p=i #검사숫자 개수를 구한다
            break
    r=[]
    for i  in range(p):
        r.append(pow(2,i)) #패리티 비트 위치 목록을 생성
    hamming=[0]*(number+p+1)#원래 비트와 패리티 비트+1한 값을 반환(0번째는 안 쓸 거임)
    hamming[0]='x'
    j=0
    for i in range(1, number+p+1): #데이터 위치에 데이터 삽입
        if i not in r:
            hamming[i]=original[j]
            j=j+1
    for h in r:
        add=0
        start=h
        while start <= len(hamming):
            for i in range(start,start+h):
                if i>=len(hamming):
                    break
                add= add + hamming[i]
            start = start + h + h
        if add%2==0:
            hamming[h]=0 
        else: hamming[h]=1
        
    return(hamming[1:])

