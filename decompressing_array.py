from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self):
        m = []
        for period in self.dates:
            d1 = period[0]
            d2 = period[1]
            dates = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]
            m.extend(dates)
        return m


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)
