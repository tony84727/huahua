from typing import Dict, List
from PIL import Image, ImageDraw
import aiohttp
import re
import random
import io


class Chunk:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Plot:
    def __init__(self, name: str, owner: str, chunks: List):
        self.name = name
        self.owner = owner
        self.chunks = chunks

    def __repr__(self) -> str:
        return f"name: {self.name}, owner: {self.owner}, size: {self.size}"

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


class TerrainFetcher:
    def __init__(self, address: str) -> None:
        self.address = address

    async def fetch(self) -> bytes:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://{self.address}/Layers/TerrainLatest.gif') as r:
                return await r.content.read()


class PlotMapComposer:
    """Draw colorful overlays on the terrain to mark plots"""

    def __init__(self, terrain, plots: List[Plot]):
        self.terrain = terrain
        self.plots = plots

    def compose(self) -> Image:
        with Image.open(io.BytesIO(self.terrain)).convert('RGBA') as im:
            with Image.new('RGBA', im.size) as overlay:
                draw = ImageDraw.Draw(overlay)
                for p in self.plots:
                    color = (
                        random.randrange(0, 256),
                        random.randrange(0, 256),
                        random.randrange(0, 256),
                        200,
                    )
                    for c in p.chunks:
                        draw.rectangle(
                            (c.x - 10, c.y - 10, c.x + 10, c.y + 10),
                            fill=color,
                        )
                out = Image.alpha_composite(im, overlay)
                return out
