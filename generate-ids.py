import random, string, json
from fpdf import FPDF


# https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string
def generate_uuid(q=10) -> dict:
    ids = dict()
    for i in range(0, q):
        x = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(5))
        ids[x] = ""

    return ids


def create_pdf(uuids: dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    # create a cell
    pdf.cell(200, 10, txt="HCI Experiment Participant IDs", ln=2, align='C')

    # add cells for each id
    for idx, i in enumerate(uuids.keys()):
        pdf.cell(200, 10, txt=i, ln=idx, align='C')

    # save the pdf with name .pdf
    pdf.output("ID_PRINT.pdf")


# RUN ONCE TO GENERATE IDS AND STORE IN JSON FILE
if __name__ == "__main__":
    FILENAME = "uuid-participants.json"
    uuids = generate_uuid(30)

    with open(FILENAME, 'w') as fp:
        json.dump(uuids, fp)

    create_pdf(uuids)
