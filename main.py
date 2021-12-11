import random, string, json


# https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string
def generate_uuid(q=10) -> dict:
    ids = dict()
    for i in range(1, q):
        x = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(5))
        ids[x] = ""

    return ids


# RUN ONCE TO GENERATE IDS AND STORE IN JSON FILE
if __name__ == "__main__":
    FILENAME = "uuid-participants.json"
    uuids = generate_uuid(30)
    print(uuids)

    with open(FILENAME, 'w') as fp:
        json.dump(uuids, fp)
