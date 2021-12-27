#수신자의 준비 단계
#e의 범위 : 1 이상 100 이하
#d: c//a 이상 euler 미만의 정수 (항상 이 범위안에 들어감)

import random as r
import math as m

#소수 판별 함수
def pme_ck(x):
    try:
        x = int(x)
    except:
        return -1
    if x < 2:
        return -1
    
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return -1
    return x

#매개변수보다 작고, 매개변수와 서로소인 자연수 찾기
def pme_fd(euler):    
    while True:
        e = r.randint(1, 100)
        if m.gcd(euler, e) == 1:
            return e

#유클리드 알고리즘
def euclid(e, euler):
    for i in range(euler//e, euler):
        if (e*i)//euler == 1:
            return i

#수신자의 준비
def prepare(p, q):
    #입력받은 2개의 큰 소수 조건 확인
    p = pme_ck(p); q = pme_ck(q)
    if p == -1 or q == -1:
        print("\nError:조건에 맞지 않는 입력값\n")
        return -1

    #n의 오일러함수 값(euler)과 서로 소인 수(e) 임의로 구하기
    n = p * q; euler = (p-1) * (q-1)
    e = pme_fd(euler)
    
    #ed=1(mod 오일러함수(n))인 d 구하기
    d = euclid(e, euler)

    return(n, e, p, q, d, euler)

#평문 조건판별(정수)
def or_ck(x):
    try:
        x = int(x)
    except:
        print("\nError:조건에 맞지 않는 입력값\n")
        return -1
    else:
        return x

#4자리식 블럭단위로 만들기
def sep(original):
    original = str(original)
    blocks = []
    le = len(original)

    end = 0
    for i in range(le//4):
        end = 4*i
        blocks.append(original[4*i:4*i+4])

    if le%4 != 0:
        blocks.append(original[end+4:])

    blocks = list(map(int, blocks))
    return blocks

#암호화하기
def enc(blocks, e, n):
    cryptogram = ""
    for i in blocks:
        m = str((i**e)%n)
        k = len(m)
        cryptogram += '0'*(4-k) + m
    return cryptogram

#RSA 시작
def RSA():
    while True:
        p = input("2이상의 소수를 입력해 주세요\n")
        q = input("\n2이상의 소수를 입력해 주세요\n")
        result = prepare(p, q)
        if result == -1:
            continue
        break
        
    while True:
        if result[4] == None:
            result = prepare(p,q)
        else:
            break
        
    n = result[0]; e = result[1]; p = result[2]; q = result[3]; d = result[4]; euler = result[5]

    original = input("\n평문을 십진수로 입력해 주세요\n")
    
    while or_ck(original) == -1:
        print("\nError:조건에 맞지 않는 입력값\n")
        original = input("\n평문을 십진수로 입력해 주세요\n")

    original = or_ck(original)
    org_bls = sep(original)
    cryptogram = enc(org_bls, e, n)
    
    print(f"\nn:{n}, euler:{euler}\ne:{e}\np:{p}\nq:{q}\nd:{d}")
    print(f"Cryptogram:{cryptogram}")
RSA()

