import json
import zlib
import base64
import argparse
import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

# Location of one of InflectionAI's public keys
inflectionAI_keys = "https://raw.githubusercontent.com/InflectionAI/Signature-Verification/main/InflectionAI.keys"

def fetch_public_keys(keys_url):
    response = requests.get(keys_url)
    response.raise_for_status()
    return [
        serialization.load_ssh_public_key(key.encode(), backend=default_backend())
        for key in response.text.splitlines()
    ]

def verify_signature(public_keys, compressed_data, signatures, expected_data):
    for public_key in public_keys:
        for signature_b64 in signatures:
            signature = base64.b64decode(signature_b64)
            try:
                public_key.verify(signature, compressed_data, ec.ECDSA(hashes.SHA256()))
                decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
                if json.loads(decompressed_data) == expected_data:
                    return "SUCCESS: Signature VERIFIED and decompressed data MATCHED user_data."
                else:
                    return "WARNING: Signature VERIFIED but decompressed data DOES NOT MATCH user_data."
            except Exception:
                continue
    return "FAILED: Signature COULD NOT BE VERIFIED"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Verify INPUT_FILE was digitally signed with an InflectionAI's key"
    )
    parser.add_argument("--input_file", required=True, help="Path to file to verify")
    args = parser.parse_args()

    public_keys = fetch_public_keys(inflectionAI_keys)
    with open(args.input_file, 'r', encoding='utf-8') as f:
        signed_takeout = json.load(f)

    user_data = signed_takeout["user_data"]
    base64encoded_compressed_user_data = signed_takeout["base64encoded_compressed_user_data"]
    signatures_of_compressed_user_data = signed_takeout["signatures_of_compressed_user_data"]
    compressed_user_data = base64.b64decode(base64encoded_compressed_user_data)

    print(verify_signature(public_keys, compressed_user_data, signatures_of_compressed_user_data, user_data))

