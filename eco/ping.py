import requests


class PingResult:
    def __init__(self, raw_json):
        self.raw = raw_json

    def total_players(self):
        return self.raw['TotalPlayers']

    def players(self):
        return self.raw['OnlinePlayersNames']

    def description(self):
        return self.raw['Description']

    def detailed_description(self):
        return self.raw['DetailedDescription']

    def version(self):
        return self.raw['Version']


class Pinger:
    def __init__(self, address):
        self.address = address

    def fetch(self) -> PingResult:
        r = requests.get('http://{}/info'.format(self.address))
        return PingResult(r.json())
