from pydantic import BaseModel, Field, AnyUrl, field_validator, model_validator, computed_field, EmailStr
from typing import Annotated, Literal, List, Optional
from uuid import UUID
from datetime import datetime

class daimensionModel(BaseModel):
    length_cm: Annotated[float, Field(gt=0, examples=[13.5], description="Length of the product in centimeters")]
    width_cm: Annotated[float, Field(gt=0, examples=[7.5], description="Width of the product in centimeters")]
    height_cm: Annotated[float, Field(gt=0, examples=[0.8], description="Height of the product in centimeters")]

    @property
    def volume_cm3(self) -> float:
        return round(self.length_cm * self.width_cm * self.height_cm, 2)

class Seller(BaseModel):
    id: UUID
    name: Annotated[
        str,
        Field(
            min_length=2,
            max_length=60,
            title="Seller Name",
            description="Name of the seller (2-60 chars).",
            examples=["Mi Store", "Apple Store India"],
        ),
    ]
    email: EmailStr 
    website: AnyUrl

    @field_validator("email", mode="after")
    @classmethod
    def validate_seller_email_domain(cls, value: EmailStr):
        allowed_domains = {
            "mistore.in",
            "realmeofficial.in",
            "samsungindia.in",
            "lenovostore.in",
            "hpworld.in",
            "applestoreindia.in",
            "dellexclusive.in",
            "sonycenter.in",
            "oneplusstore.in",
            "asusexclusive.in",
        }
        domain = str(value).split("@")[1]
        if domain not in allowed_domains:
            raise ValueError(f"Seller email domain not allowed: {domain}")
        return value





class product(BaseModel):
    id : UUID
    
    sku : Annotated[
        str, 
        Field(
            min_length=8, 
            max_length=20, 
            example="eg3g-1234-567", 
            description="Stock Keeping Unit - unique identifier for the product")
            ]
    name : Annotated[str,Field(min_length=1,  max_length=100, examples=["Realme C3"], description="Name of the product")]
    description : Annotated[
        str,    
        Field(
            min_length=1, 
            max_length=500, 
            example="Realme C3 is a budget smartphone with 6.5-inch display, MediaTek Helio G70 processor, and 5000mAh battery.", 
            description="Detailed description of the product")
        ]
    catogory : Annotated[
        str, 
        Field(
            min_length=1, 
            max_length=50, 
            example="Smartphones", 
            description="Category to which the product belongs")
            ]
    brand : Annotated[
        str,
        Field(
            min_length=1, 
            max_length=50, 
            example="Realme", 
            description="Brand of the product")
            ]
    price: Annotated[
        float,
        Field(
            gt=0, 
            example=9999.99, 
            description="Price of the product in USD")
            ]
    currency: Literal["INR"] = "INR"
    discount_percent: Annotated[
        float,
        Field(
            ge=0, 
            le=100, 
            example=10.5, 
            description="Discount percentage on the product")
            ]
    stock: Annotated[
        int,
        Field(
            ge=0, 
            examples=[100], 
            description="Number of items available in stock")
            ]
    is_active: bool = True
    rating: Annotated[
        float,
        Field(
            ge=0, 
            le=5, 
            example=4.5, 
            description="Average customer rating for the product")
            ]
    
    tag: Annotated[
        Optional[list[str]],
        Field(
            default=None, 
            example=["budget", "smartphone", "android"], 
            description="List of tags associated with the product")
            ]
    image_urls: Annotated[
        List[AnyUrl],
        Field(max_length=1, description="At least 1 image url"),
    ]
    dimensions_cm: daimensionModel
    seller : Seller

    created_at: datetime

    @field_validator("sku", mode="after")
    @classmethod
    def validate_sku_format(cls, value :str):
        if "-" not in value:
            raise ValueError("sku must have "-"")
        last = value.split("-")[-1]
        if not (len(last) == 3 and last.isdigit()): 
            raise ValueError(" sku must end with 3 digit number")
        
        return value
    
    @model_validator(mode="after")
    def velidate_business_rules(cls, model: "product"):
        if model.stock == 0 and model.is_active is True:
            raise ValueError("product cannot be active if stock is 0")
        
        if model.discount_percent > 0 and model.rating  == 0:
            raise ValueError("product cannot have discount if rating is 0")
        
        return model
    
    @computed_field
    @property
    def final_price(self) -> float:
        return round(self.price * (1- self.discount_percent / 100), 2)
    
    



# UPDATE PYDANTIC
class DimensionsCMUpdate(BaseModel):
    length: Optional[float] = Field(gt=0)
    width: Optional[float] = Field(gt=0)
    height: Optional[float] = Field(gt=0)


class SellerUpdate(BaseModel):
    name: Optional[str] = Field(min_length=2, max_length=60)
    email: Optional[EmailStr]
    website: Optional[AnyUrl]

    @field_validator("email", mode="after")
    @classmethod
    def validate_seller_email_domain(cls, value: EmailStr):
        allowed_domains = {
            "mistore.in",
            "realmeofficial.in",
            "samsungindia.in",
            "lenovostore.in",
            "hpworld.in",
            "applestoreindia.in",
            "dellexclusive.in",
            "sonycenter.in",
            "oneplusstore.in",
            "asusexclusive.in",
        }
        domain = str(value).split("@")[-1].lower()
        if domain not in allowed_domains:
            raise ValueError(f"Seller email domain not allowed: {domain}")
        return value


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(min_length=3, max_length=80)
    description: Optional[str] = Field(max_length=200)
    category: Optional[str]
    brand: Optional[str]

    price: Optional[float] = Field(gt=0)
    currency: Optional[Literal["INR"]]

    discount_percent: Optional[int] = Field(ge=0, le=90)
    stock: Optional[int] = Field(ge=0)
    is_active: Optional[bool]
    rating: Optional[float] = Field(ge=0, le=5)

    tags: Optional[List[str]] = Field(max_length=10)
    image_urls: Optional[List[AnyUrl]]

    dimensions_cm: Optional[DimensionsCMUpdate]
    seller: Optional[SellerUpdate]

    @model_validator(mode="after")
    @classmethod
    def validate_business_rules(cls, model: "product"):
        if model.stock == 0 and model.is_active is True:
            raise ValueError("If stock is 0, is_active must be false")

        if model.discount_percent > 0 and model.rating == 0:
            raise ValueError("Discounted product must have a rating (rating != 0)")

        return model

    @computed_field
    @property
    def final_price(self) -> float:
        return round(self.price * (1 - self.discount_percent / 100), 2)

    @computed_field
    @property
    def volume_cm3(self) -> float:
        d = self.dimensions_cm
        return round(d.length * d.width * d.height, 2)
