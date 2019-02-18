#readline_all.py
f = open("C:/python/새파일.txt" , 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 무한루프안에서 계속 한 줄씩 읽고 더 읽을 라인이 없으면 break 수행
