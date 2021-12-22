def encoding (message) : #message는 이진수 리스트 형태로 입력받는다
    import random
    su_in = 1
    sum =0
    seq = [] #초월증가 수열인 2의 거듭제곱을 모아둔 리스트
    more_add = [] #초월증가 수열의 합보다 큰 수를 모아둔 리스트
    open_bag = [] #공개할 bag
    code=0
    for i in range(1, len(message)+1):
        su_in = su_in*2
        seq.append(su_in)

    for i in range(0,len(message)): #초월증가 수열의 합
        sum += seq[i]

    for i in range(sum+1,sum+500) : #초월증가 수열의 합보다 큰 수를 리스트에 추가
        more_add.append(i)

    key1 = rand.sample(more_add, 1) #임의로 하나를 추출하여 비밀키1로 설정

    for i in range(more_add[0],key1): #서로소인 수를 임의로 하나 골라서 두번째 비밀키로 설정
        if gcd(i,key1) == 1:
            key2 = i
            break

    for i in range(0,len(seq)):
        b = seq[i] * key2 %key1
        open_bag.append(b) #공개키 배열을 만든다

    for i in range(0, len(message)):
        if message[i] == 1:
            code = code + open_bag[i]
        else : pass

    return code #암호화한 값을 반환한다.

