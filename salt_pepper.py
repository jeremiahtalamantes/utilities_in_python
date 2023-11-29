import hashlib
import os

#
# Salt and Pepper Functions
#

def generate_salt(length=32):
    """Generate a random salt."""
    return os.urandom(length)

def hash_password(password, salt, pepper):
    """Hash a password using SHA-256 with salt and pepper."""
    # Combine password, salt, and pepper
    combined = salt + password.encode('utf-8') + pepper.encode('utf-8')
    # Create SHA-256 hash
    return hashlib.sha256(combined).hexdigest()

# Example usage
password = "YourPasswordHere"
salt = generate_salt()
pepper = "YourPepperHere"  # This should be stored and retrieved securely from a key vault

hashed_password = hash_password(password, salt, pepper)

print(f"Salt: {salt.hex()}")
print(f"Hashed Password: {hashed_password}")
