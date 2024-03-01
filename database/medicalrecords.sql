--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5
-- Dumped by pg_dump version 15.2

-- Started on 2024-02-27 00:23:53 -05

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 4561 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16446)
-- Name: appointments; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.appointments (
    appointment_id integer NOT NULL,
    patient_id integer,
    doctor_id integer,
    insurance_id integer,
    establishment_id integer,
    appointment_date timestamp without time zone,
    duration_minutes integer,
    status smallint DEFAULT 1,
    notes text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.appointments OWNER TO medicalrappuser;

--
-- TOC entry 215 (class 1259 OID 16454)
-- Name: appointments_appointment_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.appointments_appointment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.appointments_appointment_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4562 (class 0 OID 0)
-- Dependencies: 215
-- Name: appointments_appointment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.appointments_appointment_id_seq OWNED BY public.appointments.appointment_id;


--
-- TOC entry 216 (class 1259 OID 16455)
-- Name: companies; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.companies (
    company_id integer NOT NULL,
    commercial_name character varying(100) NOT NULL,
    contact_person_id integer,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.companies OWNER TO medicalrappuser;

--
-- TOC entry 217 (class 1259 OID 16461)
-- Name: companies_company_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.companies_company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.companies_company_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4563 (class 0 OID 0)
-- Dependencies: 217
-- Name: companies_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.companies_company_id_seq OWNED BY public.companies.company_id;


--
-- TOC entry 218 (class 1259 OID 16462)
-- Name: disease_types; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.disease_types (
    disease_type_id integer NOT NULL,
    disease_name character varying(100) NOT NULL,
    description text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.disease_types OWNER TO medicalrappuser;

--
-- TOC entry 219 (class 1259 OID 16470)
-- Name: disease_types_disease_type_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.disease_types_disease_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.disease_types_disease_type_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4564 (class 0 OID 0)
-- Dependencies: 219
-- Name: disease_types_disease_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.disease_types_disease_type_id_seq OWNED BY public.disease_types.disease_type_id;


--
-- TOC entry 220 (class 1259 OID 16471)
-- Name: diseases; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.diseases (
    disease_id integer NOT NULL,
    disease_type_id integer,
    disease_code character varying(20),
    disease_name character varying(100) NOT NULL,
    description text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.diseases OWNER TO medicalrappuser;

--
-- TOC entry 221 (class 1259 OID 16479)
-- Name: diseases_disease_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.diseases_disease_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.diseases_disease_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4565 (class 0 OID 0)
-- Dependencies: 221
-- Name: diseases_disease_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.diseases_disease_id_seq OWNED BY public.diseases.disease_id;


--
-- TOC entry 222 (class 1259 OID 16480)
-- Name: doctors; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.doctors (
    doctor_id integer NOT NULL,
    person_id integer,
    specialty_id integer,
    license_number character varying(50),
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer,
    company_id integer
);


ALTER TABLE public.doctors OWNER TO medicalrappuser;

--
-- TOC entry 223 (class 1259 OID 16486)
-- Name: doctors_doctor_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.doctors_doctor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.doctors_doctor_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4566 (class 0 OID 0)
-- Dependencies: 223
-- Name: doctors_doctor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.doctors_doctor_id_seq OWNED BY public.doctors.doctor_id;


--
-- TOC entry 224 (class 1259 OID 16487)
-- Name: establishments; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.establishments (
    establishment_id integer NOT NULL,
    company_id integer,
    establishment_name character varying(100) NOT NULL,
    establishment_number character varying(20),
    address character varying(255),
    city character varying(100),
    country character varying(100),
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.establishments OWNER TO medicalrappuser;

--
-- TOC entry 225 (class 1259 OID 16495)
-- Name: establishments_establishment_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.establishments_establishment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.establishments_establishment_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4567 (class 0 OID 0)
-- Dependencies: 225
-- Name: establishments_establishment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.establishments_establishment_id_seq OWNED BY public.establishments.establishment_id;


--
-- TOC entry 226 (class 1259 OID 16496)
-- Name: exam_types; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.exam_types (
    exam_type_id integer NOT NULL,
    company_id integer,
    exam_name character varying(100) NOT NULL,
    description text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.exam_types OWNER TO medicalrappuser;

--
-- TOC entry 227 (class 1259 OID 16504)
-- Name: exam_types_exam_type_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.exam_types_exam_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exam_types_exam_type_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4568 (class 0 OID 0)
-- Dependencies: 227
-- Name: exam_types_exam_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.exam_types_exam_type_id_seq OWNED BY public.exam_types.exam_type_id;


--
-- TOC entry 228 (class 1259 OID 16505)
-- Name: exams; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.exams (
    exam_id integer NOT NULL,
    exam_type_id integer,
    company_id integer,
    exam_name character varying(100) NOT NULL,
    description text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.exams OWNER TO medicalrappuser;

--
-- TOC entry 229 (class 1259 OID 16513)
-- Name: exams_exam_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.exams_exam_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exams_exam_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4569 (class 0 OID 0)
-- Dependencies: 229
-- Name: exams_exam_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.exams_exam_id_seq OWNED BY public.exams.exam_id;


--
-- TOC entry 230 (class 1259 OID 16514)
-- Name: image_exams; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.image_exams (
    image_exam_id integer NOT NULL,
    image_type_id integer,
    company_id integer,
    exam_name character varying(100) NOT NULL,
    description text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.image_exams OWNER TO medicalrappuser;

--
-- TOC entry 231 (class 1259 OID 16522)
-- Name: image_exams_image_exam_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.image_exams_image_exam_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_exams_image_exam_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4570 (class 0 OID 0)
-- Dependencies: 231
-- Name: image_exams_image_exam_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.image_exams_image_exam_id_seq OWNED BY public.image_exams.image_exam_id;


--
-- TOC entry 232 (class 1259 OID 16523)
-- Name: image_types; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.image_types (
    image_type_id integer NOT NULL,
    company_id integer,
    image_type_name character varying(100) NOT NULL,
    description text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.image_types OWNER TO medicalrappuser;

--
-- TOC entry 233 (class 1259 OID 16531)
-- Name: image_types_image_type_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.image_types_image_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_types_image_type_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4571 (class 0 OID 0)
-- Dependencies: 233
-- Name: image_types_image_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.image_types_image_type_id_seq OWNED BY public.image_types.image_type_id;


--
-- TOC entry 234 (class 1259 OID 16532)
-- Name: insurances; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.insurances (
    insurance_id integer NOT NULL,
    person_id integer,
    insurance_name character varying(100) NOT NULL,
    policy_number character varying(50),
    coverage_details text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.insurances OWNER TO medicalrappuser;

--
-- TOC entry 235 (class 1259 OID 16540)
-- Name: insurances_insurance_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.insurances_insurance_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.insurances_insurance_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4572 (class 0 OID 0)
-- Dependencies: 235
-- Name: insurances_insurance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.insurances_insurance_id_seq OWNED BY public.insurances.insurance_id;


--
-- TOC entry 236 (class 1259 OID 16541)
-- Name: medical_attentions; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.medical_attentions (
    attention_id integer NOT NULL,
    appointment_id integer,
    establishment_id integer,
    doctor_id integer,
    service_id integer,
    insurance_id integer,
    company_id integer,
    attention_date timestamp without time zone,
    symptoms text,
    diagnosis text,
    treatment text,
    current_condition text,
    evolution text,
    next_appointment_date timestamp without time zone,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.medical_attentions OWNER TO medicalrappuser;

--
-- TOC entry 237 (class 1259 OID 16549)
-- Name: medical_attentions_attention_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.medical_attentions_attention_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medical_attentions_attention_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4573 (class 0 OID 0)
-- Dependencies: 237
-- Name: medical_attentions_attention_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.medical_attentions_attention_id_seq OWNED BY public.medical_attentions.attention_id;


--
-- TOC entry 238 (class 1259 OID 16550)
-- Name: medication_diets; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.medication_diets (
    med_diet_id integer NOT NULL,
    medication_type_id integer,
    company_id integer,
    medication_diet_name character varying(100) NOT NULL,
    generic_composition text,
    indications text,
    contraindications text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.medication_diets OWNER TO medicalrappuser;

--
-- TOC entry 239 (class 1259 OID 16558)
-- Name: medication_diets_med_diet_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.medication_diets_med_diet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medication_diets_med_diet_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4574 (class 0 OID 0)
-- Dependencies: 239
-- Name: medication_diets_med_diet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.medication_diets_med_diet_id_seq OWNED BY public.medication_diets.med_diet_id;


--
-- TOC entry 240 (class 1259 OID 16559)
-- Name: medication_types; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.medication_types (
    medication_type_id integer NOT NULL,
    company_id integer,
    medication_name character varying(100) NOT NULL,
    description text,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.medication_types OWNER TO medicalrappuser;

--
-- TOC entry 241 (class 1259 OID 16567)
-- Name: medication_types_medication_type_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.medication_types_medication_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medication_types_medication_type_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4575 (class 0 OID 0)
-- Dependencies: 241
-- Name: medication_types_medication_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.medication_types_medication_type_id_seq OWNED BY public.medication_types.medication_type_id;


--
-- TOC entry 242 (class 1259 OID 16568)
-- Name: patients; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.patients (
    patient_id integer NOT NULL,
    person_id integer,
    category character varying(20),
    occupation_ref character varying(50),
    income_date date,
    is_client boolean,
    insurance character varying(50),
    status character varying(20) DEFAULT 1,
    alert_1 character varying(255),
    alert_2 character varying(255),
    alert_3 character varying(255),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer,
    company_id integer
);


ALTER TABLE public.patients OWNER TO medicalrappuser;

--
-- TOC entry 243 (class 1259 OID 16576)
-- Name: patients_patient_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.patients_patient_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_patient_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4576 (class 0 OID 0)
-- Dependencies: 243
-- Name: patients_patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.patients_patient_id_seq OWNED BY public.patients.patient_id;


--
-- TOC entry 244 (class 1259 OID 16577)
-- Name: persons; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.persons (
    person_id integer NOT NULL,
    first_name character varying(50),
    last_name character varying(50),
    identification_type character varying(50),
    identification character varying(50),
    birthdate date,
    gender character varying(10),
    marital_status character varying(20),
    address character varying(255),
    phone_number character varying(15),
    email character varying(100),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer,
    company_id integer
);


ALTER TABLE public.persons OWNER TO medicalrappuser;

--
-- TOC entry 245 (class 1259 OID 16584)
-- Name: persons_person_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.persons_person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.persons_person_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4577 (class 0 OID 0)
-- Dependencies: 245
-- Name: persons_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.persons_person_id_seq OWNED BY public.persons.person_id;


--
-- TOC entry 246 (class 1259 OID 16585)
-- Name: services; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.services (
    service_id integer NOT NULL,
    service_name character varying(100) NOT NULL,
    description text,
    price numeric(10,2),
    iva_percentage numeric(5,2),
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer,
    company_id integer,
    specialty_id integer
);


ALTER TABLE public.services OWNER TO medicalrappuser;

--
-- TOC entry 247 (class 1259 OID 16593)
-- Name: services_service_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.services_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_service_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4578 (class 0 OID 0)
-- Dependencies: 247
-- Name: services_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.services_service_id_seq OWNED BY public.services.service_id;


--
-- TOC entry 248 (class 1259 OID 16594)
-- Name: specialties; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.specialties (
    specialty_id integer NOT NULL,
    company_id integer,
    specialty_name character varying(100) NOT NULL,
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.specialties OWNER TO medicalrappuser;

--
-- TOC entry 249 (class 1259 OID 16600)
-- Name: specialties_specialty_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.specialties_specialty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.specialties_specialty_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4579 (class 0 OID 0)
-- Dependencies: 249
-- Name: specialties_specialty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.specialties_specialty_id_seq OWNED BY public.specialties.specialty_id;


--
-- TOC entry 251 (class 1259 OID 16822)
-- Name: users; Type: TABLE; Schema: public; Owner: medicalrappuser
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(100) NOT NULL,
    password character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    full_name character varying(255) NOT NULL,
    role character varying(50) NOT NULL,
    access_token character varying(255),
    status smallint DEFAULT 1,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    created_by integer,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_by integer
);


ALTER TABLE public.users OWNER TO medicalrappuser;

--
-- TOC entry 250 (class 1259 OID 16821)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: medicalrappuser
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO medicalrappuser;

--
-- TOC entry 4580 (class 0 OID 0)
-- Dependencies: 250
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: medicalrappuser
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 4226 (class 2604 OID 16601)
-- Name: appointments appointment_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.appointments ALTER COLUMN appointment_id SET DEFAULT nextval('public.appointments_appointment_id_seq'::regclass);


--
-- TOC entry 4230 (class 2604 OID 16602)
-- Name: companies company_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.companies ALTER COLUMN company_id SET DEFAULT nextval('public.companies_company_id_seq'::regclass);


--
-- TOC entry 4234 (class 2604 OID 16603)
-- Name: disease_types disease_type_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.disease_types ALTER COLUMN disease_type_id SET DEFAULT nextval('public.disease_types_disease_type_id_seq'::regclass);


--
-- TOC entry 4238 (class 2604 OID 16604)
-- Name: diseases disease_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.diseases ALTER COLUMN disease_id SET DEFAULT nextval('public.diseases_disease_id_seq'::regclass);


--
-- TOC entry 4242 (class 2604 OID 16605)
-- Name: doctors doctor_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.doctors ALTER COLUMN doctor_id SET DEFAULT nextval('public.doctors_doctor_id_seq'::regclass);


--
-- TOC entry 4246 (class 2604 OID 16606)
-- Name: establishments establishment_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.establishments ALTER COLUMN establishment_id SET DEFAULT nextval('public.establishments_establishment_id_seq'::regclass);


--
-- TOC entry 4250 (class 2604 OID 16607)
-- Name: exam_types exam_type_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.exam_types ALTER COLUMN exam_type_id SET DEFAULT nextval('public.exam_types_exam_type_id_seq'::regclass);


--
-- TOC entry 4254 (class 2604 OID 16608)
-- Name: exams exam_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.exams ALTER COLUMN exam_id SET DEFAULT nextval('public.exams_exam_id_seq'::regclass);


--
-- TOC entry 4258 (class 2604 OID 16609)
-- Name: image_exams image_exam_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.image_exams ALTER COLUMN image_exam_id SET DEFAULT nextval('public.image_exams_image_exam_id_seq'::regclass);


--
-- TOC entry 4262 (class 2604 OID 16610)
-- Name: image_types image_type_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.image_types ALTER COLUMN image_type_id SET DEFAULT nextval('public.image_types_image_type_id_seq'::regclass);


--
-- TOC entry 4266 (class 2604 OID 16611)
-- Name: insurances insurance_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.insurances ALTER COLUMN insurance_id SET DEFAULT nextval('public.insurances_insurance_id_seq'::regclass);


--
-- TOC entry 4270 (class 2604 OID 16612)
-- Name: medical_attentions attention_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions ALTER COLUMN attention_id SET DEFAULT nextval('public.medical_attentions_attention_id_seq'::regclass);


--
-- TOC entry 4274 (class 2604 OID 16613)
-- Name: medication_diets med_diet_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medication_diets ALTER COLUMN med_diet_id SET DEFAULT nextval('public.medication_diets_med_diet_id_seq'::regclass);


--
-- TOC entry 4278 (class 2604 OID 16614)
-- Name: medication_types medication_type_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medication_types ALTER COLUMN medication_type_id SET DEFAULT nextval('public.medication_types_medication_type_id_seq'::regclass);


--
-- TOC entry 4282 (class 2604 OID 16615)
-- Name: patients patient_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.patients ALTER COLUMN patient_id SET DEFAULT nextval('public.patients_patient_id_seq'::regclass);


--
-- TOC entry 4286 (class 2604 OID 16616)
-- Name: persons person_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.persons ALTER COLUMN person_id SET DEFAULT nextval('public.persons_person_id_seq'::regclass);


--
-- TOC entry 4289 (class 2604 OID 16617)
-- Name: services service_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.services ALTER COLUMN service_id SET DEFAULT nextval('public.services_service_id_seq'::regclass);


--
-- TOC entry 4293 (class 2604 OID 16618)
-- Name: specialties specialty_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.specialties ALTER COLUMN specialty_id SET DEFAULT nextval('public.specialties_specialty_id_seq'::regclass);


--
-- TOC entry 4297 (class 2604 OID 16825)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 4518 (class 0 OID 16446)
-- Dependencies: 214
-- Data for Name: appointments; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.appointments (appointment_id, patient_id, doctor_id, insurance_id, establishment_id, appointment_date, duration_minutes, status, notes, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4520 (class 0 OID 16455)
-- Dependencies: 216
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.companies (company_id, commercial_name, contact_person_id, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4522 (class 0 OID 16462)
-- Dependencies: 218
-- Data for Name: disease_types; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.disease_types (disease_type_id, disease_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4524 (class 0 OID 16471)
-- Dependencies: 220
-- Data for Name: diseases; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.diseases (disease_id, disease_type_id, disease_code, disease_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4526 (class 0 OID 16480)
-- Dependencies: 222
-- Data for Name: doctors; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.doctors (doctor_id, person_id, specialty_id, license_number, status, created_at, created_by, updated_at, updated_by, company_id) FROM stdin;
\.


--
-- TOC entry 4528 (class 0 OID 16487)
-- Dependencies: 224
-- Data for Name: establishments; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.establishments (establishment_id, company_id, establishment_name, establishment_number, address, city, country, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4530 (class 0 OID 16496)
-- Dependencies: 226
-- Data for Name: exam_types; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.exam_types (exam_type_id, company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4532 (class 0 OID 16505)
-- Dependencies: 228
-- Data for Name: exams; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.exams (exam_id, exam_type_id, company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4534 (class 0 OID 16514)
-- Dependencies: 230
-- Data for Name: image_exams; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.image_exams (image_exam_id, image_type_id, company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4536 (class 0 OID 16523)
-- Dependencies: 232
-- Data for Name: image_types; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.image_types (image_type_id, company_id, image_type_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4538 (class 0 OID 16532)
-- Dependencies: 234
-- Data for Name: insurances; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.insurances (insurance_id, person_id, insurance_name, policy_number, coverage_details, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4540 (class 0 OID 16541)
-- Dependencies: 236
-- Data for Name: medical_attentions; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.medical_attentions (attention_id, appointment_id, establishment_id, doctor_id, service_id, insurance_id, company_id, attention_date, symptoms, diagnosis, treatment, current_condition, evolution, next_appointment_date, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4542 (class 0 OID 16550)
-- Dependencies: 238
-- Data for Name: medication_diets; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.medication_diets (med_diet_id, medication_type_id, company_id, medication_diet_name, generic_composition, indications, contraindications, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4544 (class 0 OID 16559)
-- Dependencies: 240
-- Data for Name: medication_types; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.medication_types (medication_type_id, company_id, medication_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4546 (class 0 OID 16568)
-- Dependencies: 242
-- Data for Name: patients; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.patients (patient_id, person_id, category, occupation_ref, income_date, is_client, insurance, status, alert_1, alert_2, alert_3, created_at, created_by, updated_at, updated_by, company_id) FROM stdin;
\.


--
-- TOC entry 4548 (class 0 OID 16577)
-- Dependencies: 244
-- Data for Name: persons; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.persons (person_id, first_name, last_name, identification_type, identification, birthdate, gender, marital_status, address, phone_number, email, created_at, created_by, updated_at, updated_by, company_id) FROM stdin;
\.


--
-- TOC entry 4550 (class 0 OID 16585)
-- Dependencies: 246
-- Data for Name: services; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.services (service_id, service_name, description, price, iva_percentage, status, created_at, created_by, updated_at, updated_by, company_id, specialty_id) FROM stdin;
\.


--
-- TOC entry 4552 (class 0 OID 16594)
-- Dependencies: 248
-- Data for Name: specialties; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.specialties (specialty_id, company_id, specialty_name, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4555 (class 0 OID 16822)
-- Dependencies: 251
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: medicalrappuser
--

COPY public.users (user_id, username, password, email, full_name, role, access_token, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 4581 (class 0 OID 0)
-- Dependencies: 215
-- Name: appointments_appointment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.appointments_appointment_id_seq', 1, false);


--
-- TOC entry 4582 (class 0 OID 0)
-- Dependencies: 217
-- Name: companies_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.companies_company_id_seq', 1, false);


--
-- TOC entry 4583 (class 0 OID 0)
-- Dependencies: 219
-- Name: disease_types_disease_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.disease_types_disease_type_id_seq', 1, false);


--
-- TOC entry 4584 (class 0 OID 0)
-- Dependencies: 221
-- Name: diseases_disease_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.diseases_disease_id_seq', 1, false);


--
-- TOC entry 4585 (class 0 OID 0)
-- Dependencies: 223
-- Name: doctors_doctor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.doctors_doctor_id_seq', 1, false);


--
-- TOC entry 4586 (class 0 OID 0)
-- Dependencies: 225
-- Name: establishments_establishment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.establishments_establishment_id_seq', 1, false);


--
-- TOC entry 4587 (class 0 OID 0)
-- Dependencies: 227
-- Name: exam_types_exam_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.exam_types_exam_type_id_seq', 1, false);


--
-- TOC entry 4588 (class 0 OID 0)
-- Dependencies: 229
-- Name: exams_exam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.exams_exam_id_seq', 1, false);


--
-- TOC entry 4589 (class 0 OID 0)
-- Dependencies: 231
-- Name: image_exams_image_exam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.image_exams_image_exam_id_seq', 1, false);


--
-- TOC entry 4590 (class 0 OID 0)
-- Dependencies: 233
-- Name: image_types_image_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.image_types_image_type_id_seq', 1, false);


--
-- TOC entry 4591 (class 0 OID 0)
-- Dependencies: 235
-- Name: insurances_insurance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.insurances_insurance_id_seq', 1, false);


--
-- TOC entry 4592 (class 0 OID 0)
-- Dependencies: 237
-- Name: medical_attentions_attention_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.medical_attentions_attention_id_seq', 1, false);


--
-- TOC entry 4593 (class 0 OID 0)
-- Dependencies: 239
-- Name: medication_diets_med_diet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.medication_diets_med_diet_id_seq', 1, false);


--
-- TOC entry 4594 (class 0 OID 0)
-- Dependencies: 241
-- Name: medication_types_medication_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.medication_types_medication_type_id_seq', 1, false);


--
-- TOC entry 4595 (class 0 OID 0)
-- Dependencies: 243
-- Name: patients_patient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.patients_patient_id_seq', 1, false);


--
-- TOC entry 4596 (class 0 OID 0)
-- Dependencies: 245
-- Name: persons_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.persons_person_id_seq', 1, false);


--
-- TOC entry 4597 (class 0 OID 0)
-- Dependencies: 247
-- Name: services_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.services_service_id_seq', 1, false);


--
-- TOC entry 4598 (class 0 OID 0)
-- Dependencies: 249
-- Name: specialties_specialty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.specialties_specialty_id_seq', 1, false);


--
-- TOC entry 4599 (class 0 OID 0)
-- Dependencies: 250
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: medicalrappuser
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, false);


--
-- TOC entry 4302 (class 2606 OID 16620)
-- Name: appointments appointments_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_pkey PRIMARY KEY (appointment_id);


--
-- TOC entry 4304 (class 2606 OID 16622)
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (company_id);


--
-- TOC entry 4306 (class 2606 OID 16624)
-- Name: disease_types disease_types_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.disease_types
    ADD CONSTRAINT disease_types_pkey PRIMARY KEY (disease_type_id);


--
-- TOC entry 4308 (class 2606 OID 16626)
-- Name: diseases diseases_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.diseases
    ADD CONSTRAINT diseases_pkey PRIMARY KEY (disease_id);


--
-- TOC entry 4310 (class 2606 OID 16628)
-- Name: doctors doctors_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (doctor_id);


--
-- TOC entry 4312 (class 2606 OID 16630)
-- Name: establishments establishments_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.establishments
    ADD CONSTRAINT establishments_pkey PRIMARY KEY (establishment_id);


--
-- TOC entry 4314 (class 2606 OID 16632)
-- Name: exam_types exam_types_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.exam_types
    ADD CONSTRAINT exam_types_pkey PRIMARY KEY (exam_type_id);


--
-- TOC entry 4316 (class 2606 OID 16634)
-- Name: exams exams_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_pkey PRIMARY KEY (exam_id);


--
-- TOC entry 4318 (class 2606 OID 16636)
-- Name: image_exams image_exams_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.image_exams
    ADD CONSTRAINT image_exams_pkey PRIMARY KEY (image_exam_id);


--
-- TOC entry 4320 (class 2606 OID 16638)
-- Name: image_types image_types_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.image_types
    ADD CONSTRAINT image_types_pkey PRIMARY KEY (image_type_id);


--
-- TOC entry 4322 (class 2606 OID 16640)
-- Name: insurances insurances_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.insurances
    ADD CONSTRAINT insurances_pkey PRIMARY KEY (insurance_id);


--
-- TOC entry 4324 (class 2606 OID 16642)
-- Name: medical_attentions medical_attentions_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_pkey PRIMARY KEY (attention_id);


--
-- TOC entry 4326 (class 2606 OID 16644)
-- Name: medication_diets medication_diets_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medication_diets
    ADD CONSTRAINT medication_diets_pkey PRIMARY KEY (med_diet_id);


--
-- TOC entry 4328 (class 2606 OID 16646)
-- Name: medication_types medication_types_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medication_types
    ADD CONSTRAINT medication_types_pkey PRIMARY KEY (medication_type_id);


--
-- TOC entry 4330 (class 2606 OID 16648)
-- Name: patients patients_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (patient_id);


--
-- TOC entry 4332 (class 2606 OID 16650)
-- Name: persons persons_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_pkey PRIMARY KEY (person_id);


--
-- TOC entry 4334 (class 2606 OID 16652)
-- Name: services services_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (service_id);


--
-- TOC entry 4336 (class 2606 OID 16654)
-- Name: specialties specialties_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.specialties
    ADD CONSTRAINT specialties_pkey PRIMARY KEY (specialty_id);


--
-- TOC entry 4338 (class 2606 OID 16836)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 4340 (class 2606 OID 16832)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 4342 (class 2606 OID 16834)
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- TOC entry 4343 (class 2606 OID 16655)
-- Name: appointments appointments_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctors(doctor_id);


--
-- TOC entry 4344 (class 2606 OID 16660)
-- Name: appointments appointments_establishment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_establishment_id_fkey FOREIGN KEY (establishment_id) REFERENCES public.establishments(establishment_id);


--
-- TOC entry 4345 (class 2606 OID 16665)
-- Name: appointments appointments_insurance_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_insurance_id_fkey FOREIGN KEY (insurance_id) REFERENCES public.insurances(insurance_id);


--
-- TOC entry 4346 (class 2606 OID 16670)
-- Name: appointments appointments_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(patient_id);


--
-- TOC entry 4347 (class 2606 OID 16675)
-- Name: companies companies_contact_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_contact_person_id_fkey FOREIGN KEY (contact_person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 4348 (class 2606 OID 16680)
-- Name: diseases diseases_disease_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.diseases
    ADD CONSTRAINT diseases_disease_type_id_fkey FOREIGN KEY (disease_type_id) REFERENCES public.disease_types(disease_type_id);


--
-- TOC entry 4349 (class 2606 OID 16685)
-- Name: doctors doctors_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4350 (class 2606 OID 16690)
-- Name: doctors doctors_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 4351 (class 2606 OID 16695)
-- Name: doctors doctors_specialties_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_specialties_id_fkey FOREIGN KEY (specialty_id) REFERENCES public.specialties(specialty_id);


--
-- TOC entry 4352 (class 2606 OID 16700)
-- Name: establishments establishments_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.establishments
    ADD CONSTRAINT establishments_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4353 (class 2606 OID 16705)
-- Name: exam_types exam_types_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.exam_types
    ADD CONSTRAINT exam_types_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4354 (class 2606 OID 16710)
-- Name: exams exams_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4355 (class 2606 OID 16715)
-- Name: exams exams_exam_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_exam_type_id_fkey FOREIGN KEY (exam_type_id) REFERENCES public.exam_types(exam_type_id);


--
-- TOC entry 4369 (class 2606 OID 16720)
-- Name: patients fk_person_id; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT fk_person_id FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 4356 (class 2606 OID 16725)
-- Name: image_exams image_exams_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.image_exams
    ADD CONSTRAINT image_exams_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4357 (class 2606 OID 16730)
-- Name: image_exams image_exams_image_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.image_exams
    ADD CONSTRAINT image_exams_image_type_id_fkey FOREIGN KEY (image_type_id) REFERENCES public.image_types(image_type_id);


--
-- TOC entry 4358 (class 2606 OID 16735)
-- Name: image_types image_types_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.image_types
    ADD CONSTRAINT image_types_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4359 (class 2606 OID 16740)
-- Name: insurances insurances_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.insurances
    ADD CONSTRAINT insurances_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 4360 (class 2606 OID 16745)
-- Name: medical_attentions medical_attentions_appointment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_appointment_id_fkey FOREIGN KEY (appointment_id) REFERENCES public.appointments(appointment_id);


--
-- TOC entry 4361 (class 2606 OID 16750)
-- Name: medical_attentions medical_attentions_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4362 (class 2606 OID 16755)
-- Name: medical_attentions medical_attentions_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctors(doctor_id);


--
-- TOC entry 4363 (class 2606 OID 16760)
-- Name: medical_attentions medical_attentions_establishment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_establishment_id_fkey FOREIGN KEY (establishment_id) REFERENCES public.establishments(establishment_id);


--
-- TOC entry 4364 (class 2606 OID 16765)
-- Name: medical_attentions medical_attentions_insurance_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_insurance_id_fkey FOREIGN KEY (insurance_id) REFERENCES public.insurances(insurance_id);


--
-- TOC entry 4365 (class 2606 OID 16770)
-- Name: medical_attentions medical_attentions_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.services(service_id);


--
-- TOC entry 4366 (class 2606 OID 16775)
-- Name: medication_diets medication_diets_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medication_diets
    ADD CONSTRAINT medication_diets_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4367 (class 2606 OID 16780)
-- Name: medication_diets medication_diets_medication_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medication_diets
    ADD CONSTRAINT medication_diets_medication_type_id_fkey FOREIGN KEY (medication_type_id) REFERENCES public.medication_types(medication_type_id);


--
-- TOC entry 4368 (class 2606 OID 16785)
-- Name: medication_types medication_types_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.medication_types
    ADD CONSTRAINT medication_types_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4370 (class 2606 OID 16790)
-- Name: patients patients_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4371 (class 2606 OID 16795)
-- Name: patients patients_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 4372 (class 2606 OID 16800)
-- Name: persons persons_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4373 (class 2606 OID 16805)
-- Name: services services_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 4374 (class 2606 OID 16810)
-- Name: services services_specialty_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_specialty_id_fkey FOREIGN KEY (specialty_id) REFERENCES public.specialties(specialty_id);


--
-- TOC entry 4375 (class 2606 OID 16815)
-- Name: specialties specialties_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: medicalrappuser
--

ALTER TABLE ONLY public.specialties
    ADD CONSTRAINT specialties_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


-- Completed on 2024-02-27 00:24:12 -05

--
-- PostgreSQL database dump complete
--

