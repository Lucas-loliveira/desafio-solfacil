CSV_DATA_EXAMPLE = [
    {
        "CNPJ": "16.470.954/0001-06",
        "Razão Social": "Sol Eterno",
        "Nome Fantasia": "Sol Eterno LTDA",
        "Telefone": "(21) 98207-9901",
        "Email": "atendimento@soleterno.com",
        " CEP": "22783-115",
    },
    {
        "CNPJ": "19.478.819/0001-97",
        "Razão Social": "Sol da Manhã",
        "Nome Fantasia": "Sol da Manhã LTDA",
        "Telefone": "(21) 98207-9902",
        "Email": "atendimentosoldamanha.com",
        " CEP": "69314-690",
    },
    {
        "CNPJ": "12.473.742/0001-13",
        "Razão Social": "Sol Forte",
        "Nome Fantasia": "Sol Forte LTDA",
        "Telefone": "21982079903",
        "Email": "atendimentosolforte.com",
        " CEP": "84043-150",
    },
    {
        "CNPJ": "214.004.920-92",
        "Razão Social": "Sol Brilhante",
        "Nome Fantasia": "",
        "Telefone": "(21) 8207-9902",
        "Email": "atendimento@soleterno.com",
        " CEP": "57071-186",
    },
    {
        "CNPJ": "22783-115",
        "Razão Social": "Sol Energia",
        "Nome Fantasia": "Sol Energia LTDA",
        "Telefone": "",
        "Email": "atendimento@solenergia.com",
        " CEP": "12900-303",
    },
]


VALID_CNPJ = "01360643000109"
INVALID_CNPJ = "11111111111111"
INVALID_DATA = {
    "cnpj": INVALID_CNPJ,
    "name": "Test Company",
    "trade_name": "Test Co",
    "phone": "1111111111",
    "email": "test@test.com",
    "zip_code": "11111-111",
}

VALID_DATA = {
    "cnpj": VALID_CNPJ,
    "name": "Test Company",
    "trade_name": "Test Co",
    "phone": "1111111111",
    "email": "test@test.com",
    "zip_code": "11111-111",
}
