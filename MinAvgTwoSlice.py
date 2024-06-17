# 시간복잡도에 의해 구글링으로 해답확인
# 참고 : https://datacodingschool.tistory.com/22

def solution(A):
    minA = (A[0]+A[1]) / 2
    result = 0

    for i in range(0, len(A)-1):
        tmp = (A[i] + A[i+1]) / 2
        if minA > tmp:
            minA = tmp
            result = i
            
# 그룹의 원소는 최소 2개 이상이므로 2개와 3개인 그룹만 비교
    for j in range(0, len(A)-2):
        tmp = (A[j] + A[j+1] + A[j+2]) / 3
        if minA > tmp:
            minA = tmp
            result = j

    return result