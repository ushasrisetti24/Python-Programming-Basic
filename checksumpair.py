def chkPair(A, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                print(f"Pair with a given sum {x} is ({A[i]},{A[j]})")
 
                return 1
    return 0
 
if __name__ == "__main__":
    A = [0, -1, 2, -3, 1]
    x = -2
    size = len(A)
 
    if (chkPair(A, size, x)):
        print("Valid pair exists")
 
    else:
        print(f"No valid pair exists for {x}")
