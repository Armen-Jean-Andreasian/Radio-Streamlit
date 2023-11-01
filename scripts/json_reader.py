import json


def reader(json_filepath) -> dict:
    with open(json_filepath) as f:
        radio_stations: dict = json.load(f)
    return radio_stations


if __name__ == '__main__':
    reader(json_filepath='radio.json')
