from typing import Dict, List
import aiohttp
import re


class Chunk:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Plot:
    def __init__(self, name: str, owner: str, chunks: List):
        self.name = name
        self.owner = owner
        self.chunks = chunks

    @property
    def size(self):
        return len(self.chunks)


class MapInfo:
    def __init__(self, plots: List[Plot]) -> None:
        self.plots = plots


class PlotNameOwnerParser:
    """Extract plot owner and name from the eco server response"""

    def __init__(self):
        self.pattern = re.compile('(.*), Owner: (.*)')

    def parse(self, text: str):
        """Parse

            Returns:
                Optional[(str,str)]: Tuple of (Name, Owner), if not match, returns None
        """
        matches = self.pattern.search(text)
        if matches is None:
            return None
        return (matches[1], matches[2])


def parse_map_info(raw_json: Dict):
    plot_name_parser = PlotNameOwnerParser()
    plots = []
    for (name, info) in raw_json['Plots'].items():
        name_owner = plot_name_parser.parse(name)
        if name_owner is None:
            continue
        (name, owner) = name_owner
        chunks = [Chunk(c['x'], c['y']) for c in info]
        plots.append(Plot(name, owner, chunks))
    return MapInfo(plots)


class MapInfoFetcher:
    def __init__(self, address: str) -> None:
        self.address = address

    async def fetch(self) -> List[MapInfo]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://{self.address}/api/v1/map/map.json') as r:
                return parse_map_info(await r.json())
