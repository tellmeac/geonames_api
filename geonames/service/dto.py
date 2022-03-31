from pydantic import BaseModel


class CompareResponse(BaseModel):
    """
    Response dto object of comparing two geographical points.
    """
    north_name: str
    is_equal_timezone: bool
