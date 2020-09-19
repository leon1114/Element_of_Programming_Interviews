from typing import List, Dict

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    # 동전 교환 문제임. play scores 에 있는 숫자들을 중복 사용하여 final_score 만들 수 있는 경우의 수 구하기
    # dp[i] -> final score i 를 만들 수 있는 전체 경우의 수 라고 정의하자.
    # 위의 방식은 중복을 피할 수가 없음
    # dp[i][j] -> i 번째 요소까지만 사용해서 j 원을 만들 수 있는 총 가지수
    dp = [[0] * (final_score+1) for _ in range(len(individual_play_scores))]
    for i in range(len(individual_play_scores)):
        dp[i][0] = 1

    for i in range(len(individual_play_scores)):
        cur_score = individual_play_scores[i]
        for score in range(1, final_score+1):
            dp[i][score] = (dp[i-1][score] if i-1 >= 0 else 0) + (dp[i][score-cur_score] if score-cur_score >= 0 else 0)

    return dp[len(individual_play_scores)-1][final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
