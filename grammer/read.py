#read.py
f = open("C:/python/새파일.txt" , 'r')
data = f.read()
print(data)
f.close()

# 파일 내용 전체를 문자열로 반환함
# 따라서 data는 파일 전체 내용임