from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.farm import Farm
from app.schemas.farm import FarmCreate, FarmOut

router = APIRouter(prefix="/farms", tags=["farms"])

@router.post("", response_model=FarmOut, status_code=201)
def create_farm(payload: FarmCreate, db: Session = Depends(get_db)):
    farm = Farm(**payload.model_dump())
    db.add(farm)
    db.commit()
    db.refresh(farm)
    return farm

@router.get("", response_model=list[FarmOut])
def list_farms(city: str | None = None, db: Session = Depends(get_db)):
    q = select(Farm).where(Farm.is_active.is_(True))
    if city:
        q = q.where(Farm.city == city)
    return db.scalars(q).all()

@router.get("/{farm_id}", response_model=FarmOut)
def get_farm(farm_id: int, db: Session = Depends(get_db)):
    farm = db.get(Farm, farm_id)
    if not farm:
        raise HTTPException(404, "Farm not found")
    return farm