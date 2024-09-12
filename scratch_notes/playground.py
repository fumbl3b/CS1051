print('how many terms would you like to approximate?')
terms = int(input())

def leibniz_series(terms):
    pi_over_4 = 0
    for n in range(terms):
        # Each term is alternately positive and negative, starting with positive
        pi_over_4 += (-1)**n / (2*n + 1)
        print(f"current estimation of pi is: {pi_over_4 * 4}")
    # Multiply the sum by 4 to get the approximation of pi
    return pi_over_4 * 4

approx_pi = leibniz_series(terms)
print(f"Approximation of pi using {terms} terms: {approx_pi}")
