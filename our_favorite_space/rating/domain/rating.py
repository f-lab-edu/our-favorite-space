from dataclasses import dataclass

from rating.vo.comment import RecreationRatingData, RestaurantRatingData
from space.domain.space import Space
from users.domain.user import User


@dataclass
class Rating:
    user: User
    space: Space
    data: RestaurantRatingData | RecreationRatingData
    comment: str
