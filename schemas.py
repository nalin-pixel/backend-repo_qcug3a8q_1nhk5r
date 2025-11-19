"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (you can keep or remove if not needed)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Taludos lead/contact schema
class Lead(BaseModel):
    """
    Leads collection schema for contact form submissions.
    Collection name: "lead"
    """
    name: str = Field(..., description="Nome do cliente")
    email: EmailStr = Field(..., description="Email do cliente")
    phone: Optional[str] = Field(None, description="Telefone de contacto")
    company: Optional[str] = Field(None, description="Empresa (opcional)")
    message: str = Field(..., description="Mensagem enviada pelo cliente")
    service: Optional[str] = Field(None, description="Tipo de serviço de interesse: montagem, manutenção, inspeção, outros")
