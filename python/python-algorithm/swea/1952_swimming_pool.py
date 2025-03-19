def cost(daily, monthly, quarterly, yearly, plans):

    # dp = [0] * 13
    # dp[1] = min(plans[0] * daily, monthly)
    # dp[2] = min(dp[1] + plans[1] * daily, dp[1] + monthly)
    # dp[3] = min(dp[2] + plans[2] * daily, dp[2] + monthly, dp[2] + quarterly)
    # dp[4] = min(dp[3] + plans[3] * daily, dp[3] + monthly, dp[2] + quarterly)
    # dp[5] = min(dp[4] + plans[4] * daily, dp[4] + monthly, dp[2] + quarterly)
    # dp[6] = min(dp[5] + plans[5] * daily, dp[5] + monthly, dp[5] + quarterly)
    # dp[7] = min(dp[6] + plans[6] * daily, dp[6] + monthly, dp[5] + quarterly)
    # dp[8] = min(dp[7] + plans[7] * daily, dp[7] + monthly, dp[5] + quarterly)
    # dp[9] = min(dp[8] + plans[8] * daily, dp[8] + monthly, dp[8] + quarterly)
    # dp[10] = min(dp[9] + plans[9] * daily, dp[9] + monthly, dp[8] + quarterly)
    # dp[11] = min(dp[10] + plans[10] * daily, dp[10] + monthly, dp[8] + quarterly)
    # dp[12] = min(dp[11] + plans[11] * daily, dp[11] + monthly, dp[11] + quarterly, dp[0] + yearly)

    dp = [0] * 13

    for i in range(1, 13):

        # 일간 이용권 사용할경우
        dp[i] = dp[i-1] + plans[i-1] * daily

        # 월간 이용권 사용할경우
        dp[i] = min(dp[i], dp[i-1] + monthly)

        # 3개월 이용권 사용할경우
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + quarterly)

        # 연간 이용권 사용할경우
        if i == 12:
            dp[i] = min(dp[i], dp[0] + yearly)


    return dp[12]

T = int(input())
for test_case in range(1, T + 1):
    daily, monthly, quarterly, yearly = map(int, input().split())
    plans = list(map(int, input().split()))

    print(f"#{test_case} {cost(daily, monthly, quarterly, yearly, plans)}")