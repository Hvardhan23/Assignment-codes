
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

pi_digits = "314159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211"
largest_prime = 1

#checking pair of 5consecuive digits 
for i in range(len(pi_digits) - 4): #5digits starting number {last-4, last}
    number = int(pi_digits[i:i+5]) #taking int of 5 digits
    if is_prime(number):
        largest_prime = max(largest_prime, number)
print("The largest 5-digit prime number in the first 100 digits of Pi is:", largest_prime)
