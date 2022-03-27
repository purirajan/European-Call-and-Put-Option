def call_payoff(S, K):
    return max(S-K, 0)
def put_payoff(S, K):
    return max(K-S, 0)
