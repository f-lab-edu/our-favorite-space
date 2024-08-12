from dataclasses import dataclass

from rating.vo.comment import RecreationRatingData, RestaurantRatingData
from users.domain.user import User


@dataclass
class Rating:
    user: User
    data: RestaurantRatingData | RecreationRatingData
    comment: str
