from typing import Optional

from pydantic import BaseModel


class ImageExamRequest(BaseModel):
    """Schema for request body of image exam"""

    image_type_id: Optional[int] = None
    company_id: Optional[int] = None
    exam_name: str
    description: Optional[str] = None
    # status: int
    # created_by: int
    # updated_by: int


class ImageExamUpdateRequest(BaseModel):
    """Schema for update body of image exam"""

    image_type_id: Optional[int] = None
    company_id: Optional[int] = None
    exam_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    # updated_by: Optional[int] = None
