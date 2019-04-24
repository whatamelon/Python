#adddata.py
f = open("C:/python/새파일.txt" , 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# 새파일이 갖고 있던 바로 다음값 부터 저장함