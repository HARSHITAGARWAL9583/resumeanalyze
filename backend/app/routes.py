from fastapi import APIRouter, UploadFile, File
import uuid, shutil, os
from app.services import process_job, get_job_status, get_job_result

router = APIRouter()

UPLOAD_DIR = "uploaded_jobs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
def upload_files(csv: UploadFile = File(...), jd: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    job_path = os.path.join(UPLOAD_DIR, job_id)
    os.makedirs(job_path)

    csv_path = os.path.join(job_path, "resumes.csv")
    jd_path = os.path.join(job_path, "jd.txt")

    with open(csv_path, "wb") as f: shutil.copyfileobj(csv.file, f)
    with open(jd_path, "wb") as f: shutil.copyfileobj(jd.file, f)

    process_job.delay(job_id, csv_path, jd_path)
    return {"job_id": job_id}

@router.get("/job/{job_id}/status")
def job_status(job_id: str):
    return get_job_status(job_id)

@router.get("/job/{job_id}/result")
def job_result(job_id: str):
    return get_job_result(job_id)