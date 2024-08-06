from dataclasses import dataclass

from our_favorite_space.rating.vo.comment import (
    RecreationRatingData,
    RestaurantRatingData,
)
from our_favorite_space.users.domain.user import User


@dataclass
class Rating:
    user: User
    data: RestaurantRatingData | RecreationRatingData
    comment: str
