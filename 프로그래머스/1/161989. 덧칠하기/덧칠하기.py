def solution(n, m, section):
    answer = 0
    current = 0  # 현재 덮고 있는 위치

    for i in section:
        # 만약 현재 덮고 있는 위치가 현재 구간보다 작다면
        if current < i:
            answer += 1  # 새 작업이 필요하므로 카운트 증가
            current = i + m - 1  # 덮을 수 있는 범위 업데이트

    return answer
