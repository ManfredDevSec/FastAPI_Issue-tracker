import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueUpdate, IssueOut , IssueCreate,IssueStatus
from app.storage import load_data, save_data


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.get("/", response_model=list[IssueOut], status_code=status.HTTP_200_OK)
def get_issues():
    """Retrieve all issues."""
    issues = load_data()
    return issues

@router.post("/", response_model=IssueCreate, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create an Issue"""
    issues = load_data()
    new_issue = {
        "id":str(uuid.uuid4()),
        "title":payload.title,
        "description":payload.description,
        "priority":payload.priority,
        "status":IssueStatus.open
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

@router.get("/{issue_id}", response_model=IssueOut, status_code=status.HTTP_200_OK)
def get_issue(issue_id: str):
    """Retrieve an issue by ID."""
    issues = load_data()
    issue = next((issue for issue in issues if issue["id"] == issue_id), None)
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return issue

@router.put("/{issue_id}", response_model=IssueOut, status_code=status.HTTP_200_OK)
def update_issue(issue_id: str, payload: IssueUpdate):
    """Update an issue by ID."""
    issues = load_data()
    issue = next((issue for issue in issues if issue["id"] == issue_id), None)
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    issue.update(payload.model_dump())
    save_data(issues)
    return issue

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    """Delete an issue by ID."""
    issues = load_data()
    issue = next((issue for issue in issues if issue["id"] == issue_id), None)
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    issues.remove(issue)
    save_data(issues)
    return None