from __future__ import annotations
import functools
from typing import List, Dict, Set
from dataclasses import dataclass
from Options import Toggle, OptionSet
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms


@dataclass
class FortniteArchipelagoOptions:
    pass


class FortniteGame(Game):
    name = "Fortnite"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]
    is_adult_only_or_unrated = False
    options_cls = FortniteArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return []

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Visit NAMED_LOCATION",
                data={"NAMED_LOCATION": (self.br_named_locations, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Kill a player in NAMED_LOCATION",
                data={"NAMED_LOCATION": (self.br_named_locations, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Open COUNT chests in NAMED_LOCATION",
                data={
                    "COUNT": (self.chest_count, 1),
                    "NAMED_LOCATION": (self.br_named_locations, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Play a MODE game", data={"MODE": (self.game_mode, 1)}
            ),
        ]

    def br_named_locations(self) -> List[str]:
        return BR_NAMED_LOCATIONS

    def chest_count(self) -> range:
        return range(1, 4)

    def game_mode(self):
        return MODES


MODES = ["Blitz", "OG", "Battle Royale", "Zero Build"]
BR_NAMED_LOCATIONS = [
    "HARMONY HILLS",
    "DREAMY DOMAIN",
    "CANYON CROSSING",
    "RESISTANCE BASE",
    "FIRST ORDER BASE",
    "O.X.R. HQ",
    "SHINING SPAN",
    "RANGER'S REST",
    "OUTPOST ENCLAVE",
    "FOXY FLOODGATE",
    "KAPPA KAPPA FACTORY",
    "Outlaw Oasis",
    "BUGSWATTER BEACH",
    "UTOPIA  CITY",
    "SHOGUN'S SOLITUDE",
    "SUPERNOVA ACADEMY",
    "Shiny Shafts",
]
