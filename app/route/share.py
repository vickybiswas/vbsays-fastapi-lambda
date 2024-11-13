from fastapi import APIRouter
from app.model.share import Share
from app.utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException



router = APIRouter()

@router.get("/", response_model=Share)
async def read_read_share(share_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Share).filter(Share.id == share_id).all()

    if not db_item:
        
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

"""
@app.post("/", response_model=Share)
async def create_share(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
Step 9: API Endpoint to Read an Item by ID
Here we created a API endpoint which is for getting data from database using an item id as input. In simple term when user want to access some data of item from database, he/she will send that item id and in response he/she get all details of that item from databse. so we created Another API endpoint (/items/{item_id}) which is defined using the @app.get decorator for reading an item by its ID. It takes the item_id as a parameter, queries the database, and returns the item. If the item is not found, it raises an HTTP exception with a 404 status.


@router.post("/", response_model=Share)
async def create_share(
    document_in: DocumentCreate, 
    session: SessionDep, 
    current_user: CurrentUser,
    document_type_id: Optional[int] = Query(None, description="For Authorization only")
) -> Any:
    Create a new document.

    - **document_in**: The details of the document to create.

    Returns the created document record.
   if document_in.parent_doc_id:
        
        # Check parent document is exit or not
        parent = crud.read_document_by_id(session, document_id=document_in.parent_doc_id)
        if not parent:
            raise HTTPException(status_code=400, detail="Parent document not found.")
        
        # If document type is pickup then match from entity id is same as from entity id during allotment
        if document_in.document_type_id == DocumentTypeEnum.PICKUP.value:
            main_document = crud.get_main_doc_by_type(session, main_doc_id=parent.main_document_id, type_id=document_in.document_type_id)
            if not main_document or main_document.from_entity_id != document_in.from_entity_id:
                 raise HTTPException(status_code=400, detail="Incorrect from entity value.")

    # Call CRUD function to create the new document
    return crud.create_document(session=session, document_in=document_in, user_id=current_user.id)

"""

# End of File