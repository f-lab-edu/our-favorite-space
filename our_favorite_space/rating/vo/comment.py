from dataclasses import dataclass

from pydantic import conint

MIN_SCORE = 0
MAX_SCORE = 5


@dataclass
class RestaurantRatingData:
    taste: conint(ge=MIN_SCORE, le=MAX_SCORE)
    service: conint(ge=MIN_SCORE, le=MAX_SCORE)
    condition: conint(ge=MIN_SCORE, le=MAX_SCORE)
    price: conint(ge=MIN_SCORE, le=MAX_SCORE)


@dataclass
class RecreationRatingData:
    convenience: conint(ge=MIN_SCORE, le=MAX_SCORE)
    service: conint(ge=MIN_SCORE, le=MAX_SCORE)
    condition: conint(ge=MIN_SCORE, le=MAX_SCORE)
    price: conint(ge=MIN_SCORE, le=MAX_SCORE)
