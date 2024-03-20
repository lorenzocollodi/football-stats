import asyncio
import json

import aiohttp
import numpy as np
from understat import Understat
from matplotlib import pyplot as plt


async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        data = await understat.get_player_matches(7006)
        sorted_matches = sorted(data, key=lambda x: x["date"])[-50:]
        goals = np.array([int(match["goals"]) for match in sorted_matches])
        x_goals = np.array([float(match["xG"]) for match in sorted_matches])
        mean_goals = (goals[:-2] + goals[1:-1] + goals[2:]) / 3
        mean_x_goals = (x_goals[:-2] + x_goals[1:-1] + x_goals[2:]) / 3
        plt.plot(mean_goals, color="red")
        plt.plot(mean_x_goals, color="blue")
        plt.show()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
