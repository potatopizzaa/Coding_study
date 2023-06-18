# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

word = str(input())

word = word.upper()

word_list = list(set(word))

cnt = []
for i in range(len(word_list)):
    cnt.append(word.count(word_list[i]))
Max = max(cnt)

if cnt.count(Max) != 1:
    print("?")
else:
    print(word_list[cnt.index(Max)])