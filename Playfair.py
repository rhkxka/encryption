import random as r

#5x5
def set_playfair(key):
    #암호키 가공
    enc_key = ""
    for i in key:
        k = 0
        if i == "I" or i == "J": k += 1
        if i != " ":
            if k <= 1 and not(i in enc_key):
                enc_key += i

    playfair = []
    for i in range(5):
        playfair.append([None]*5)
    
    #내용 집어넣기
    m = 0; i = 65; jp = 0; kp = 0; error = 0
    #가공한 암호키 집어넣기
    for j in range(5):
        for k in range(5):
            try:
                l = enc_key[j*5+k]
                if l == "I" or l == "J":
                    playfair[j][k] = ["I", "J"]
                    m = 1
                    continue
                playfair[j][k] = l
            except:
                jp = j; kp =k; error = 1
                break
        if error == 1: break

    #그 외의 알파벳 집어넣기
    for j in range(jp, 5):
        if j == jp:
            for k in range(kp, 5):
                while chr(i) in enc_key:
                    i += 1
                    if i == 73 or i == 74:
                        if m == 1:
                            i = 75
                        else:
                            playfair[j][k] = [chr(i), chr(i+1)]
                            i += 2

                playfair[j][k] = chr(i)
                i += 1
                if i == 73 or i == 74:
                    if m == 1:
                        i = 75
                    else:
                        playfair[j][k] = [chr(i), chr(i+1)]
                        i += 2

        else:
            for k in range(0, 5):
                while chr(i) in enc_key:
                    i += 1
                    if i == 73 or i == 74:
                        if m == 1:
                            i = 75
                        else:
                            playfair[j][k] = [chr(i), chr(i+1)]
                            i += 2

                playfair[j][k] = chr(i)
                i += 1
                if i == 73 or i == 74:
                    if m == 1:
                        i = 75
                    else:
                        playfair[j][k] = [chr(i), chr(i+1)]
                        i += 2
    """                
    #테스트 출력
    print("Playfair 표")
    for i in range(5):
        for j in range(5):
            print(playfair[i][j], end = "\t")
        print()
    """
    return playfair

#평문 가공하기
def manuorigin(origin):
    ori = ""; originm = ""
    for i in origin:
        if i == " ": continue
        else: originm += i
        
    if len(originm) % 2 == 0:
        for i in range(0, len(originm), 2):
            ori += originm[i]
            if ori[i] != originm[i+1] and not(ord(ori[i]) == 73 and originm[i+1] == 74) and not(ord(ori[i]) == 74 and originm[i+1] == 73):
                ori += originm[i+1]
            else: ori += "X" + orginm[i+1]
    else:
        for i in range(0, len(originm)-1, 2):
            ori += originm[i]
            if ori[i] != originm[i+1] and not(ord(ori[i]) == 73 and originm[i+1] == 74) and not(ord(ori[i]) == 74 and originm[i+1] == 73):
                ori += originm[i+1]
            else:
                ori += "X" + originm[i+1]
        ori += originm[-1]

    if len(ori) % 2 != 0: ori += "X"
    return ori

#암호화
def enc_playfair(ori, playfair):
    enc = ""
    
    for i in range(0, len(ori), 2):
        one = ori[i]; two = ori[i+1]
        onexy = [0, 0]; twoxy = [0, 0]
        
        #가공한 평문의 좌표값 찾기
        if one in ["I", "J"]:
            for i in range(len(playfair)):
                if ["I", "J"] in playfair[i]:
                    onexy = [playfair[i].index(["I", "J"]), i]
                    break
        else:
            for i in range(len(playfair)):
                if one in playfair[i]:
                    onexy = [playfair[i].index(one), i]
                    break
        
        if two in ["I", "J"]:
            for i in range(len(playfair)):
                if ["I", "J"] in playfair[i]:
                    twoxy = [playfair[i].index(["I", "J"]), i]
                    break
        else:
            for i in range(len(playfair)):
                if two in playfair[i]:
                    twoxy = [playfair[i].index(two), i]
                    break

        #1. 행렬 모두 일치 X
        if onexy[0] != twoxy[0] and onexy[1] != twoxy[1]:
            try:
                enc += playfair[twoxy[1]][onexy[0]]
            except:
                enc += r.choice(["I", "J"])

            try:
                enc += playfair[onexy[1]][twoxy[0]]
            except:
                enc += r.choice(["I", "J"])
        
        #2. 행ㅡ만 일치
        elif onexy[1] == twoxy[1]:
            onex = onexy[0] + 1; twox = twoxy[0] + 1
            if onex >= 5: onex = 0
            if twox >= 5: twox = 0
            try:
                enc += playfair[onexy[1]][onex]
            except:
                enc += r.choice(["I", "J"])

            try:
                enc += playfair[onexy[1]][twox]
            except:
                enc += r.choice(["I", "J"])
                
        #3. 열ㅣ만 일치
        else:
            oney = onexy[1] + 1; twoy = twoxy[1] + 1
            if oney >= 5: oney = 0
            if twoy >= 5: twoy = 0
            try:
                enc += playfair[oney][onexy[0]]
            except:
                enc += r.choice(["I", "J"])

            try:
                enc += playfair[twoy][onexy[0]]
            except:
                enc += r.choice(["I", "J"])
                
    return enc
        
#playfair
def playfair(key, origin):
    playfair = set_playfair(key)
    ori = manuorigin(origin)
    enc = enc_playfair(ori, playfair)
    print(f"평문 : {origin}")
    print(f"가공한 평문 : {ori}")
    print("\t             Playfair 표")
    for i in range(5):
        for j in range(5):
            print(playfair[i][j], end = "\t")
        print()
    print(f"암호문 : {enc}")
    return enc
            
playfair("GENGHIS KHAN WAS A GREAT KING AND WARRIOR", "WOMAN SCHOOL")

