import colorama
import discord
from dataclasses import dataclass

@dataclass
class Version:
    major: int
    middle: int
    minor: int
    official: bool
    final: bool

class Colors:
    dt_color = colorama.Fore.BLUE
    source_color = colorama.Fore.MAGENTA
    reset = colorama.Fore.RESET

def to_dscolor(color: colorama.Fore):
    return color_map.get(color, discord.Color.green())

color_map = {
    colorama.Fore.RED: discord.Color.red(),
    colorama.Fore.GREEN: discord.Color.green(),
    colorama.Fore.YELLOW: discord.Color.gold(),
    colorama.Fore.BLUE: discord.Color.blue(),
    colorama.Fore.MAGENTA: discord.Color.purple(),
    colorama.Fore.CYAN: discord.Color.teal(),
    colorama.Fore.WHITE: discord.Color.from_rgb(255, 255, 255),
    colorama.Fore.BLACK: discord.Color.from_rgb(0, 0, 0),
}

verson = Version(0, 0, 1, True, False)
