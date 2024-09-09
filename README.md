<small>
<center> Inflection AI </center>

## <center> Takeout file format for Pi user history </center>

Inflection AI's takeout file format for Pi user history is described below. The takeout file includes a digital signature block to ensure data integrity.

### Format Overview

The user's data is extracted into a JSON object which is then compressed, digitally signed, and made available in a JSON file with the following sections:

1. `user_data`: Contains the user's data and messages exchanged between the user and Pi in human-readable text format.
1. `base64encoded_compressed_user_data`: Contains a compressed and Base64-encoded version of `user_data`.
1. `signatures_of_compressed_user_data`: Contains four digital signatures of the compressed data, generated using Inflection AI's private keys. The public key for one of these private keys will be available at this GitHub repository, while the other three public keys will be held in reserve. 
1. `signature_verification_code`: Contains the location of this repository.

The signature should be considered **successfully validated**, if the public key available at this GitHub repository verifies **any** of the signatures in the takeout file.

An example exported JSON file:

```json
{
    "user_data": {
        "details": {
            "created_at": "2024-08-05T16:00:28.238Z",
            "entry_channel": "WEB",
            "first_name": "Alpha",
            "identifiers": [
                {
                    "identifier": "101010101010101010101",
                    "type": "GOOGLE_OAUTH_ID"
                },
                {
                    "identifier": "AlphaTheUser@example.com",
                    "type": "EMAIL"
                }
            ]
        },
        "messages": [
            {
                "channel": "WEB",
                "sent_at": "2024-08-05T16:00:28.278Z",
                "text": "Hey there, great to meet you. I’m Pi, your personal AI.\n\nMy goal is to be useful, friendly and fun. Ask me for advice, for answers, or let’s talk about whatever’s on your mind.\n\nHow's your day going?",
                "sender": "AI"
            },
            {
                "channel": "WEB",
                "sent_at": "2024-08-05T22:22:43.374Z",
                "text": "In python, how do I convert escaped unicode characters in a string to the unicode character. Eg I want to convert \\ud83d\\ude14 to 😔",
                "sender": "HUMAN"
            },
            {
                "channel": "WEB",
                "sent_at": "2024-08-05T22:22:43.388Z",
                "text": "To convert escaped Unicode characters in a string to their corresponding Unicode characters in Python, you can use the `unicode_escape` decoding method. Here's an example code snippet that demonstrates this:\n```python\n# Given string with escaped Unicode characters\ns = r\"\\ud83d\\ude14\"\n\n# Decode the string using 'unicode_escape'\ndecoded_s = s.encode(\"ascii\", \"backslashreplace\").decode(\"unicode_escape\")\n\n# Print the decoded string\nprint(decoded_s)\n```\nThis will output:\n```\n😔\n```\nIn the above code snippet, we first encode the string `s` using ASCII encoding and the `backslashreplace` error handler to replace any non-ASCII characters with their escaped Unicode representation. We then decode the encoded string using `unicode_escape` decoding to convert the escaped Unicode characters back to their Unicode representation.",
                "sender": "AI"
            }
        ]
    },
    "base64encoded_compressed_user_data": "eJy1VeFu2zYQ/p+nOGg/0gKK4DjpahgYNm8NYgHNEqAOCrQqbEY8W0Sko0BScY2gwB5iP7Zffbc9wR5hR0pNrDQOOmCzDVvk8e6+++47+nYP+BVJdEKVNhrDbdgIm7lB4VDOheP9aDgYHh8MRgeDF7PD78eDwXg4SoZHo3dRfO+B5MxmnheCCEvv9Pbk5237Uhnr5iQq9MZJWRdi26wkB1BLhcYjeX9n8K/b3urBcR/tcPDIeyv6nZvb1CH96fn56euT+fnkcjadp6+i3slP8b/LHmqZFXhp0fyEH0VVl5jkunoKwMnZJH39IO3d6sPeFoyoQmvFCvu09EFFO2kPVston+rky14nW5z4MZyf4gZcgQZjWHlJgNNQITrY6CaB9K/f/qzgQsV+aaDm5mkSJUzSJKOMzjaw0rxU1rtdITQWl00Zw9IoJFluQJCEZUMJTOw1x4WlNiDkjco5X3gmu+agMfBziY7TcShRXoO40o2DdcEivUET9jW1KCpFMqSf6vW+bfek8FAUrX58hBvZtTG978eWBP4DpofDMX+Oj5Kjl8c7mU4J6o0rNMVQ6DVIDSnkmrg6B2hzUaOEhlSuJQKDMCJ3zAwoAgHWGa7Nk8y9+vpUAicrjrYWFPr3JWqWNXJ0JP0PHh57y9+f//h9N0HTy7PJr/8/R6Pdapzpryi5/BZKlGE/Y9DWmqTfftzrouOfJQO5IC/XQOiiY3TeJl2ARF76OBWyh0xgyhPCWmOfbv4hhLek6pqHxbFO2anSxLBYsiziQtlxRovFom16Rt/BqbpB+gJ8rVzxRJEZWfgBTBb1m8jrEOoVhvMefBevsf57v1/JfkahFL7ofTibIPnVsywSNlcqi2LIoiuRX9tS2MJgXYocs+h50nrxuX48NrX5LzinC+m7+B2MjGpveXaX9XngIKMZ88E1lyXwXNeNG3f7XpHdIw+ID8iTf9OnN4Y13xz+7wVa/Nt1L+yiq33y5pc0bU/4pb96QnMf1rcANIbvGxaxLNF4CXUW9tkAaTpoQ22JJ3SrFdrDnrEvC481L5zSfNO9DfCoIyZAaFHLfqt2i25rhIP37knwpd2PwA5E33gjhqcPe5/+AaI2dSs=",
    "signatures_of_compressed_user_data": [
        "MIGIAkIBq9UuEvLx549MJWX3XLcX8j8I69mQPLUfrU1sUjaCHGmKuXrBdzVTYxR/HrkmbuEUeBxr0+5p7aDDQQz6PdbGkqQCQgGJUKxGGfo+lNFReSWrehurDg2aPmL81LFu377wwKxcxW4TUvqtCEg3HiyIi20djkCS1ylIOnuf0v4aeZcQbEjtHg==",
        "MIGIAkIBED4qLZB/RGTB4evlAI4rUgxtg533eRS2sU0LC2g8Tc2P1Ag5RlMonvRiGtHqit2rFzJ2gQEAcSSVAKCZXTbR0AcCQgFYDjwo/RHHY7MXPjVVBT93xhVZbN0dgdrHA2MKG8WfwWi0g0lzlqOW3mP9yBT9pnxiZAl1knyq3vwuB7JqKsRGqw==",
        "MIGGAkE6mnT7qR/spsOShFIJO3vsrXJIbbcfCbCR0KukmB/s17cU+6LHI0qSjc5qHx8DWLPWdKUOYnImSu8rnVrw7k1hDQJBRm1XQ3KmR97E0ZcggSg42XCQgc7dtDMnlrjENs4P4I5hiL2LYtQ4EkxWifR/6yxtncD0cl81HsE9KY5oalaGa/c=",
        "MIGIAkIBHRB+oQPvlPbt5gsRIlLigFGSZP39DOqTzkMY3Kh+hpbJd9bwdgbJMVkYfZnQWf5fC5A1Nsz2A64UxiLJhLNfJdsCQgGVREwVYvdRVF0xFXTpxVvUPpW2JnIkgpUZSHi07YyMhQ+SCbr/sCXIbPGYuEC4eZzLGU5jgZq44QyAhHp+Lqik1A=="
    ],
    "signature_verification_code": "https://github.com/InflectionAI/Signature-Verification"
}
```
---
### Signature Verification

To validate the signature in a takeout JSON file, run the following command:
```sh
$ python pi-verifier.py --input_file <SIGNED_TAKEOUT_JSON_FILE>
```