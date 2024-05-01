from typing import Optional

from pydantic import BaseModel


class ImageTypeRequest(BaseModel):
    """Schema for request body of image type"""

    company_id: Optional[int] = None
    image_type_name: str
    description: Optional[str] = None
    # status: int
    # created_by: int
    # updated_by: int


class ImageTypeUpdateRequest(BaseModel):
    """Schema for update body of image type"""

    company_id: Optional[int] = None
    image_type_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    # updated_by: Optional[int] = None
