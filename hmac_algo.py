import hashlib
import hmac

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def check_data(data, original_hash):
    if hmac.compare_digest(generate_hash(data), original_hash):
        print("data is intact and verified")
    else:
        print("warning:data has been tampered with")

original_data = "this is a secret message"
h = generate_hash(original_data)

print("original hash:", h)

print("\nchecking original data:")
check_data(original_data, h)

print("\n checking tampered data")
check_data("this is a hacked message", h)

print("\n checking data with added space:")
check_data("this is a secret message", h)

print("\n checking data with missing character:")
check_data("this is a seet message", h)