import random as r
#ADFGVX 표 만들기
def set_adfgvx():
    adfgvx = []; li = ['A', 'D', 'F', 'G', 'V', 'X']
    context = ["A"]
    
    for i in range(7):
        adfgvx.append([None]*7)

    adfgvx[0][0] = ""

    #행ㅡ, 열ㅣ 설정
    for i in range(1, 7):
        adfgvx[i][0] = li[i-1]
        adfgvx[0][i] = li[i-1]

    #내용 집어넣기
    i = 65
    for j in range(1, 7):
        for k in range(1, 7):
            adfgvx[j][k] = chr(i)
            i += 1
            if i == 91: break

    for i in range(3,  7):
        adfgvx[5][i] = str(i - 3)

    for i in range(1, 7):
        adfgvx[6][i] = str(i + 3)
    """
    #테스트 출력
    print("ADFGVX표")
    for i in range(7):
        for j in range(7):
            print(adfgvx[i][j], end = "\t")
        print()
    """
    return adfgvx

def enc_ADFGVX(adfgvx, origin, enc_key):
    x = 0; y = 0; first_enc = ""

    #1단계 암호문 생성
    for i in origin:
        for k in range(1, 7):
            if not(i in adfgvx[k][1:]): pass
            else:
                y = k
                x = adfgvx[k][1:].index(i) + 1
                first_enc += adfgvx[0][y] + adfgvx[x][0]
                break

    #암호키 가공
    key = ""
    for i in enc_key:
        if i in key: pass
        else: key += i
    """
    #테스트 출력
    print(f"암호키 : {key}")
    print(f"1단계 암호문 : first_enc")
    """
    #암호문 표 생성
    enc_graph = []; li = []; le = 0

    #암호키의 원소 좌표값 찾기
    for i in key:
        li.append(i)
    le = len(li)
    enc_graph.append(li)

    #암호문 표 채우기
    li = []
    for i in first_enc:
        li.append(i)
        if len(li) == le:
            enc_graph.append(li)
            li = []

    #빈칸은 의미없는 문자로 채움(랜덤 문자로)
    if len(li) != le:
        while len(li) < le:
            rand = r.randint(65, 90)
            li.append(chr(rand))
        enc_graph.append(li)

    """
    #테스트 출력
    print("암호문 표")
    for i in range(len(enc_graph)):
        for j in range(len(enc_graph[0])):
            print(enc_graph[i][j], end = "\t")
        print()
    """

    #암호키 정렬
    encli = list(map(ord, enc_graph[0]))
    encli.sort()
    encli = list(map(chr, encli))

    #최종 암호문 표 생성
    enclist = []
    for i in range(len(enc_graph)):
        enclist.append([None] * len(enc_graph[0]))

    #암호문 표 채워넣기
    k = 0
    for i in encli:
        ind = enc_graph[0].index(i)
        for j in range(len(enclist)):
            enclist[j][k] = enc_graph[j][ind]
        k +=1

    #암호문 구하기
    cryptogram = ""
    for j in range(len(enclist[0])):
        for i in enclist[1:]:
            cryptogram += i[j]
        cryptogram += " "
    """
    #테스트 출력
    print("최종 암호문 표")
    for i in range(len(enclist)):
        for j in range(len(enclist[0])):
            print(enclist[i][j], end = "\t")
        print()

    print("최종 암호문")
    print(cryptogram)
    """
    return cryptogram

def adfgvx():
    origin = input("암호화 시킬 문장을 입력해주세요\n: ")
    origin.upper()

    enc_key = input("암호키를 입력해주세요\n: ")
    enc_key.upper()
    
    adfgvx = set_adfgvx()
    cryptogram = enc_ADFGVX(adfgvx, origin, enc_key)

    print(cryptogram)
adfgvx()
