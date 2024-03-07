"""Constantes de la aplicación"""

COMPANIES_ROW = ['company_id', 'commercial_name', 'contact_person_id', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']
PERSONS_ROW = ['person_id', 'first_name', 'last_name', 'identification_type', 'identification', 'birthdate', 'gender', 'marital_status', 'address', 'phone_number', 'email', 'created_at', 'created_by', 'updated_at', 'updated_by', 'company_id']
DISEASE_TYPES_ROW = ['disease_type_id', 'disease_name', 'description', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']
EXAM_TYPES_ROW = ['exam_type_id', 'company_id', 'exam_name', 'description', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']
EXAMS_ROW = ['exam_id', 'exam_type_id', 'company_id', 'exam_name', 'description', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']
IMAGE_EXAMS_ROW = ['image_exam_id', 'image_type_id', 'company_id', 'exam_name', 'description', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']
IMAGE_TYPES_ROW = ['image_type_id', 'company_id', 'image_type_name', 'description', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']
SERVICE_ROW = ['service_id','service_name', 'description', 'price', 'iva_percentage', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by', 'company_id', 'specialty_id']
DISEASES_ROW = ['disease_id', 'disease_type_id', 'disease_code', 'disease_name', 'description', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']
ESTABLISHMENTS_ROW = ['establishment_id', 'company_id', 'establishment_name', 'establishment_number', 'address', 'city', 'country', 'status', 'created_at', 'created_by', 'updated_at', 'updated_by']