term = int(input("Number of terms:"))

n = 1
pi_est = 4/n
for i in range(2,term+2):
    if i == 2:
        pi_est = 4/n
        n = n + 2
    else:
        if i % 2 == 0:
            pi_est = 4/n + pi_est
        else:
            pi_est = pi_est - 4/n
        n = n + 2
    
print("Estimate of pi:", pi_est)
    
