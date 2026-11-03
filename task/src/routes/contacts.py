from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.services.auth import auth_service
from src.database.db import get_db
from src.database.models import User
from src.schemas import ContactModel, ContactUpdate, ContactResponse, ContactSearch
from src.repository import contacts as repository_contacts


router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def reads_contacts(skip:int=0,limit:int=100,db:Session=Depends(get_db),
                        current_user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.get_contacts(skip,limit,current_user,db)

@router.get("/search", response_model=List[ContactResponse])
async def search_contacts(body:ContactSearch=Depends(),db:Session=Depends(get_db),
                          current_user: User = Depends(auth_service.get_current_user)):
    contact=await repository_contacts.search_contact(body,current_user,db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.get("/birthdays", response_model=List[ContactResponse])
async def upcoming_birthdays(skip:int=0,limit:int=100,db:Session=Depends(get_db),
                             current_user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.birthday_contacts(skip,limit,current_user,db)

@router.get("/{id}", response_model=ContactResponse)
async def reads_contacts(id:int,db:Session=Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    contact=await repository_contacts.get_contact(id,current_user,db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact

@router.post("/", response_model=ContactResponse)
async def create_contact(body:ContactModel,db:Session=Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.create_contact(body, current_user,db)

@router.put("/{id}", response_model=ContactResponse)
async def update_contact(id:int, body:ContactUpdate, db:Session=Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    update_contact=await repository_contacts.update_contact(id,body,current_user,db)
    if update_contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return update_contact


@router.delete("/{id}",response_model=ContactResponse)
async def remove_contact(id:int, db:Session=Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    del_contact=await repository_contacts.remove_contact(id,current_user,db)
    if del_contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return del_contact

