--
-- PostgreSQL database dump
--

-- Dumped from database version 12.14
-- Dumped by pg_dump version 15.2

-- Started on 2024-02-17 11:35:05 -05

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
-- TOC entry 6 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 2147227)
-- Name: appointments; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.appointments OWNER TO datapluserp;

--
-- TOC entry 218 (class 1259 OID 2147225)
-- Name: appointments_appointment_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.appointments_appointment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.appointments_appointment_id_seq OWNER TO datapluserp;

--
-- TOC entry 3429 (class 0 OID 0)
-- Dependencies: 218
-- Name: appointments_appointment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.appointments_appointment_id_seq OWNED BY public.appointments.appointment_id;


--
-- TOC entry 207 (class 1259 OID 2147026)
-- Name: companies; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.companies OWNER TO datapluserp;

--
-- TOC entry 206 (class 1259 OID 2147024)
-- Name: companies_company_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.companies_company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.companies_company_id_seq OWNER TO datapluserp;

--
-- TOC entry 3430 (class 0 OID 0)
-- Dependencies: 206
-- Name: companies_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.companies_company_id_seq OWNED BY public.companies.company_id;


--
-- TOC entry 223 (class 1259 OID 2147365)
-- Name: disease_types; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.disease_types OWNER TO datapluserp;

--
-- TOC entry 222 (class 1259 OID 2147363)
-- Name: disease_types_disease_type_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.disease_types_disease_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.disease_types_disease_type_id_seq OWNER TO datapluserp;

--
-- TOC entry 3431 (class 0 OID 0)
-- Dependencies: 222
-- Name: disease_types_disease_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.disease_types_disease_type_id_seq OWNED BY public.disease_types.disease_type_id;


--
-- TOC entry 225 (class 1259 OID 2147379)
-- Name: diseases; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.diseases OWNER TO datapluserp;

--
-- TOC entry 224 (class 1259 OID 2147377)
-- Name: diseases_disease_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.diseases_disease_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.diseases_disease_id_seq OWNER TO datapluserp;

--
-- TOC entry 3432 (class 0 OID 0)
-- Dependencies: 224
-- Name: diseases_disease_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.diseases_disease_id_seq OWNED BY public.diseases.disease_id;


--
-- TOC entry 209 (class 1259 OID 2147089)
-- Name: doctors; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.doctors OWNER TO datapluserp;

--
-- TOC entry 208 (class 1259 OID 2147087)
-- Name: doctors_doctor_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.doctors_doctor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.doctors_doctor_id_seq OWNER TO datapluserp;

--
-- TOC entry 3433 (class 0 OID 0)
-- Dependencies: 208
-- Name: doctors_doctor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.doctors_doctor_id_seq OWNED BY public.doctors.doctor_id;


--
-- TOC entry 215 (class 1259 OID 2147160)
-- Name: establishments; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.establishments OWNER TO datapluserp;

--
-- TOC entry 214 (class 1259 OID 2147158)
-- Name: establishments_establishment_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.establishments_establishment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.establishments_establishment_id_seq OWNER TO datapluserp;

--
-- TOC entry 3434 (class 0 OID 0)
-- Dependencies: 214
-- Name: establishments_establishment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.establishments_establishment_id_seq OWNED BY public.establishments.establishment_id;


--
-- TOC entry 227 (class 1259 OID 2147400)
-- Name: exam_types; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.exam_types OWNER TO datapluserp;

--
-- TOC entry 226 (class 1259 OID 2147398)
-- Name: exam_types_exam_type_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.exam_types_exam_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exam_types_exam_type_id_seq OWNER TO datapluserp;

--
-- TOC entry 3435 (class 0 OID 0)
-- Dependencies: 226
-- Name: exam_types_exam_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.exam_types_exam_type_id_seq OWNED BY public.exam_types.exam_type_id;


--
-- TOC entry 233 (class 1259 OID 2147458)
-- Name: exams; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.exams OWNER TO datapluserp;

--
-- TOC entry 232 (class 1259 OID 2147456)
-- Name: exams_exam_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.exams_exam_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exams_exam_id_seq OWNER TO datapluserp;

--
-- TOC entry 3436 (class 0 OID 0)
-- Dependencies: 232
-- Name: exams_exam_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.exams_exam_id_seq OWNED BY public.exams.exam_id;


--
-- TOC entry 237 (class 1259 OID 2147506)
-- Name: image_exams; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.image_exams OWNER TO datapluserp;

--
-- TOC entry 236 (class 1259 OID 2147504)
-- Name: image_exams_image_exam_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.image_exams_image_exam_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_exams_image_exam_id_seq OWNER TO datapluserp;

--
-- TOC entry 3437 (class 0 OID 0)
-- Dependencies: 236
-- Name: image_exams_image_exam_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.image_exams_image_exam_id_seq OWNED BY public.image_exams.image_exam_id;


--
-- TOC entry 231 (class 1259 OID 2147439)
-- Name: image_types; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.image_types OWNER TO datapluserp;

--
-- TOC entry 230 (class 1259 OID 2147437)
-- Name: image_types_image_type_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.image_types_image_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_types_image_type_id_seq OWNER TO datapluserp;

--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 230
-- Name: image_types_image_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.image_types_image_type_id_seq OWNED BY public.image_types.image_type_id;


--
-- TOC entry 217 (class 1259 OID 2147179)
-- Name: insurances; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.insurances OWNER TO datapluserp;

--
-- TOC entry 216 (class 1259 OID 2147177)
-- Name: insurances_insurance_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.insurances_insurance_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.insurances_insurance_id_seq OWNER TO datapluserp;

--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 216
-- Name: insurances_insurance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.insurances_insurance_id_seq OWNED BY public.insurances.insurance_id;


--
-- TOC entry 221 (class 1259 OID 2147301)
-- Name: medical_attentions; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.medical_attentions OWNER TO datapluserp;

--
-- TOC entry 220 (class 1259 OID 2147299)
-- Name: medical_attentions_attention_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.medical_attentions_attention_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medical_attentions_attention_id_seq OWNER TO datapluserp;

--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 220
-- Name: medical_attentions_attention_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.medical_attentions_attention_id_seq OWNED BY public.medical_attentions.attention_id;


--
-- TOC entry 235 (class 1259 OID 2147482)
-- Name: medication_diets; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.medication_diets OWNER TO datapluserp;

--
-- TOC entry 234 (class 1259 OID 2147480)
-- Name: medication_diets_med_diet_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.medication_diets_med_diet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medication_diets_med_diet_id_seq OWNER TO datapluserp;

--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 234
-- Name: medication_diets_med_diet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.medication_diets_med_diet_id_seq OWNED BY public.medication_diets.med_diet_id;


--
-- TOC entry 229 (class 1259 OID 2147419)
-- Name: medication_types; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.medication_types OWNER TO datapluserp;

--
-- TOC entry 228 (class 1259 OID 2147417)
-- Name: medication_types_medication_type_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.medication_types_medication_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medication_types_medication_type_id_seq OWNER TO datapluserp;

--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 228
-- Name: medication_types_medication_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.medication_types_medication_type_id_seq OWNED BY public.medication_types.medication_type_id;


--
-- TOC entry 205 (class 1259 OID 2147004)
-- Name: patients; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.patients OWNER TO datapluserp;

--
-- TOC entry 204 (class 1259 OID 2147002)
-- Name: patients_patient_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.patients_patient_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_patient_id_seq OWNER TO datapluserp;

--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 204
-- Name: patients_patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.patients_patient_id_seq OWNED BY public.patients.patient_id;


--
-- TOC entry 203 (class 1259 OID 2146975)
-- Name: persons; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.persons OWNER TO datapluserp;

--
-- TOC entry 202 (class 1259 OID 2146973)
-- Name: persons_person_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.persons_person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.persons_person_id_seq OWNER TO datapluserp;

--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 202
-- Name: persons_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.persons_person_id_seq OWNED BY public.persons.person_id;


--
-- TOC entry 213 (class 1259 OID 2147131)
-- Name: services; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.services OWNER TO datapluserp;

--
-- TOC entry 212 (class 1259 OID 2147129)
-- Name: services_service_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.services_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.services_service_id_seq OWNER TO datapluserp;

--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 212
-- Name: services_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.services_service_id_seq OWNED BY public.services.service_id;


--
-- TOC entry 211 (class 1259 OID 2147115)
-- Name: specialties; Type: TABLE; Schema: public; Owner: datapluserp
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


ALTER TABLE public.specialties OWNER TO datapluserp;

--
-- TOC entry 210 (class 1259 OID 2147113)
-- Name: specialties_specialty_id_seq; Type: SEQUENCE; Schema: public; Owner: datapluserp
--

CREATE SEQUENCE public.specialties_specialty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.specialties_specialty_id_seq OWNER TO datapluserp;

--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 210
-- Name: specialties_specialty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: datapluserp
--

ALTER SEQUENCE public.specialties_specialty_id_seq OWNED BY public.specialties.specialty_id;


--
-- TOC entry 3152 (class 2604 OID 2147230)
-- Name: appointments appointment_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.appointments ALTER COLUMN appointment_id SET DEFAULT nextval('public.appointments_appointment_id_seq'::regclass);


--
-- TOC entry 3128 (class 2604 OID 2147029)
-- Name: companies company_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.companies ALTER COLUMN company_id SET DEFAULT nextval('public.companies_company_id_seq'::regclass);


--
-- TOC entry 3160 (class 2604 OID 2147368)
-- Name: disease_types disease_type_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.disease_types ALTER COLUMN disease_type_id SET DEFAULT nextval('public.disease_types_disease_type_id_seq'::regclass);


--
-- TOC entry 3164 (class 2604 OID 2147382)
-- Name: diseases disease_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.diseases ALTER COLUMN disease_id SET DEFAULT nextval('public.diseases_disease_id_seq'::regclass);


--
-- TOC entry 3132 (class 2604 OID 2147092)
-- Name: doctors doctor_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.doctors ALTER COLUMN doctor_id SET DEFAULT nextval('public.doctors_doctor_id_seq'::regclass);


--
-- TOC entry 3144 (class 2604 OID 2147163)
-- Name: establishments establishment_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.establishments ALTER COLUMN establishment_id SET DEFAULT nextval('public.establishments_establishment_id_seq'::regclass);


--
-- TOC entry 3168 (class 2604 OID 2147403)
-- Name: exam_types exam_type_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.exam_types ALTER COLUMN exam_type_id SET DEFAULT nextval('public.exam_types_exam_type_id_seq'::regclass);


--
-- TOC entry 3180 (class 2604 OID 2147461)
-- Name: exams exam_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.exams ALTER COLUMN exam_id SET DEFAULT nextval('public.exams_exam_id_seq'::regclass);


--
-- TOC entry 3188 (class 2604 OID 2147509)
-- Name: image_exams image_exam_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.image_exams ALTER COLUMN image_exam_id SET DEFAULT nextval('public.image_exams_image_exam_id_seq'::regclass);


--
-- TOC entry 3176 (class 2604 OID 2147442)
-- Name: image_types image_type_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.image_types ALTER COLUMN image_type_id SET DEFAULT nextval('public.image_types_image_type_id_seq'::regclass);


--
-- TOC entry 3148 (class 2604 OID 2147182)
-- Name: insurances insurance_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.insurances ALTER COLUMN insurance_id SET DEFAULT nextval('public.insurances_insurance_id_seq'::regclass);


--
-- TOC entry 3156 (class 2604 OID 2147304)
-- Name: medical_attentions attention_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions ALTER COLUMN attention_id SET DEFAULT nextval('public.medical_attentions_attention_id_seq'::regclass);


--
-- TOC entry 3184 (class 2604 OID 2147485)
-- Name: medication_diets med_diet_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medication_diets ALTER COLUMN med_diet_id SET DEFAULT nextval('public.medication_diets_med_diet_id_seq'::regclass);


--
-- TOC entry 3172 (class 2604 OID 2147422)
-- Name: medication_types medication_type_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medication_types ALTER COLUMN medication_type_id SET DEFAULT nextval('public.medication_types_medication_type_id_seq'::regclass);


--
-- TOC entry 3124 (class 2604 OID 2147007)
-- Name: patients patient_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.patients ALTER COLUMN patient_id SET DEFAULT nextval('public.patients_patient_id_seq'::regclass);


--
-- TOC entry 3121 (class 2604 OID 2146978)
-- Name: persons person_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.persons ALTER COLUMN person_id SET DEFAULT nextval('public.persons_person_id_seq'::regclass);


--
-- TOC entry 3140 (class 2604 OID 2147134)
-- Name: services service_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.services ALTER COLUMN service_id SET DEFAULT nextval('public.services_service_id_seq'::regclass);


--
-- TOC entry 3136 (class 2604 OID 2147118)
-- Name: specialties specialty_id; Type: DEFAULT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.specialties ALTER COLUMN specialty_id SET DEFAULT nextval('public.specialties_specialty_id_seq'::regclass);


--
-- TOC entry 3404 (class 0 OID 2147227)
-- Dependencies: 219
-- Data for Name: appointments; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.appointments (appointment_id, patient_id, doctor_id, insurance_id, establishment_id, appointment_date, duration_minutes, status, notes, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3392 (class 0 OID 2147026)
-- Dependencies: 207
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.companies (company_id, commercial_name, contact_person_id, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3408 (class 0 OID 2147365)
-- Dependencies: 223
-- Data for Name: disease_types; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.disease_types (disease_type_id, disease_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3410 (class 0 OID 2147379)
-- Dependencies: 225
-- Data for Name: diseases; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.diseases (disease_id, disease_type_id, disease_code, disease_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3394 (class 0 OID 2147089)
-- Dependencies: 209
-- Data for Name: doctors; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.doctors (doctor_id, person_id, specialty_id, license_number, status, created_at, created_by, updated_at, updated_by, company_id) FROM stdin;
\.


--
-- TOC entry 3400 (class 0 OID 2147160)
-- Dependencies: 215
-- Data for Name: establishments; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.establishments (establishment_id, company_id, establishment_name, establishment_number, address, city, country, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3412 (class 0 OID 2147400)
-- Dependencies: 227
-- Data for Name: exam_types; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.exam_types (exam_type_id, company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3418 (class 0 OID 2147458)
-- Dependencies: 233
-- Data for Name: exams; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.exams (exam_id, exam_type_id, company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3422 (class 0 OID 2147506)
-- Dependencies: 237
-- Data for Name: image_exams; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.image_exams (image_exam_id, image_type_id, company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3416 (class 0 OID 2147439)
-- Dependencies: 231
-- Data for Name: image_types; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.image_types (image_type_id, company_id, image_type_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3402 (class 0 OID 2147179)
-- Dependencies: 217
-- Data for Name: insurances; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.insurances (insurance_id, person_id, insurance_name, policy_number, coverage_details, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3406 (class 0 OID 2147301)
-- Dependencies: 221
-- Data for Name: medical_attentions; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.medical_attentions (attention_id, appointment_id, establishment_id, doctor_id, service_id, insurance_id, company_id, attention_date, symptoms, diagnosis, treatment, current_condition, evolution, next_appointment_date, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3420 (class 0 OID 2147482)
-- Dependencies: 235
-- Data for Name: medication_diets; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.medication_diets (med_diet_id, medication_type_id, company_id, medication_diet_name, generic_composition, indications, contraindications, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3414 (class 0 OID 2147419)
-- Dependencies: 229
-- Data for Name: medication_types; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.medication_types (medication_type_id, company_id, medication_name, description, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3390 (class 0 OID 2147004)
-- Dependencies: 205
-- Data for Name: patients; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.patients (patient_id, person_id, category, occupation_ref, income_date, is_client, insurance, status, alert_1, alert_2, alert_3, created_at, created_by, updated_at, updated_by, company_id) FROM stdin;
\.


--
-- TOC entry 3388 (class 0 OID 2146975)
-- Dependencies: 203
-- Data for Name: persons; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.persons (person_id, first_name, last_name, identification_type, identification, birthdate, gender, marital_status, address, phone_number, email, created_at, created_by, updated_at, updated_by, company_id) FROM stdin;
\.


--
-- TOC entry 3398 (class 0 OID 2147131)
-- Dependencies: 213
-- Data for Name: services; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.services (service_id, service_name, description, price, iva_percentage, status, created_at, created_by, updated_at, updated_by, company_id, specialty_id) FROM stdin;
\.


--
-- TOC entry 3396 (class 0 OID 2147115)
-- Dependencies: 211
-- Data for Name: specialties; Type: TABLE DATA; Schema: public; Owner: datapluserp
--

COPY public.specialties (specialty_id, company_id, specialty_name, status, created_at, created_by, updated_at, updated_by) FROM stdin;
\.


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 218
-- Name: appointments_appointment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.appointments_appointment_id_seq', 1, false);


--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 206
-- Name: companies_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.companies_company_id_seq', 1, false);


--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 222
-- Name: disease_types_disease_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.disease_types_disease_type_id_seq', 1, false);


--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 224
-- Name: diseases_disease_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.diseases_disease_id_seq', 1, false);


--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 208
-- Name: doctors_doctor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.doctors_doctor_id_seq', 1, false);


--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 214
-- Name: establishments_establishment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.establishments_establishment_id_seq', 1, false);


--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 226
-- Name: exam_types_exam_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.exam_types_exam_type_id_seq', 1, false);


--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 232
-- Name: exams_exam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.exams_exam_id_seq', 1, false);


--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 236
-- Name: image_exams_image_exam_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.image_exams_image_exam_id_seq', 1, false);


--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 230
-- Name: image_types_image_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.image_types_image_type_id_seq', 1, false);


--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 216
-- Name: insurances_insurance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.insurances_insurance_id_seq', 1, false);


--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 220
-- Name: medical_attentions_attention_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.medical_attentions_attention_id_seq', 1, false);


--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 234
-- Name: medication_diets_med_diet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.medication_diets_med_diet_id_seq', 1, false);


--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 228
-- Name: medication_types_medication_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.medication_types_medication_type_id_seq', 1, false);


--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 204
-- Name: patients_patient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.patients_patient_id_seq', 1, false);


--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 202
-- Name: persons_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.persons_person_id_seq', 1, false);


--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 212
-- Name: services_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.services_service_id_seq', 1, false);


--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 210
-- Name: specialties_specialty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: datapluserp
--

SELECT pg_catalog.setval('public.specialties_specialty_id_seq', 1, false);


--
-- TOC entry 3209 (class 2606 OID 2147238)
-- Name: appointments appointments_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_pkey PRIMARY KEY (appointment_id);


--
-- TOC entry 3197 (class 2606 OID 2147034)
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (company_id);


--
-- TOC entry 3213 (class 2606 OID 2147376)
-- Name: disease_types disease_types_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.disease_types
    ADD CONSTRAINT disease_types_pkey PRIMARY KEY (disease_type_id);


--
-- TOC entry 3215 (class 2606 OID 2147390)
-- Name: diseases diseases_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.diseases
    ADD CONSTRAINT diseases_pkey PRIMARY KEY (disease_id);


--
-- TOC entry 3199 (class 2606 OID 2147097)
-- Name: doctors doctors_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (doctor_id);


--
-- TOC entry 3205 (class 2606 OID 2147171)
-- Name: establishments establishments_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.establishments
    ADD CONSTRAINT establishments_pkey PRIMARY KEY (establishment_id);


--
-- TOC entry 3217 (class 2606 OID 2147411)
-- Name: exam_types exam_types_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.exam_types
    ADD CONSTRAINT exam_types_pkey PRIMARY KEY (exam_type_id);


--
-- TOC entry 3223 (class 2606 OID 2147469)
-- Name: exams exams_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_pkey PRIMARY KEY (exam_id);


--
-- TOC entry 3227 (class 2606 OID 2147517)
-- Name: image_exams image_exams_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.image_exams
    ADD CONSTRAINT image_exams_pkey PRIMARY KEY (image_exam_id);


--
-- TOC entry 3221 (class 2606 OID 2147450)
-- Name: image_types image_types_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.image_types
    ADD CONSTRAINT image_types_pkey PRIMARY KEY (image_type_id);


--
-- TOC entry 3207 (class 2606 OID 2147190)
-- Name: insurances insurances_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.insurances
    ADD CONSTRAINT insurances_pkey PRIMARY KEY (insurance_id);


--
-- TOC entry 3211 (class 2606 OID 2147312)
-- Name: medical_attentions medical_attentions_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_pkey PRIMARY KEY (attention_id);


--
-- TOC entry 3225 (class 2606 OID 2147493)
-- Name: medication_diets medication_diets_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medication_diets
    ADD CONSTRAINT medication_diets_pkey PRIMARY KEY (med_diet_id);


--
-- TOC entry 3219 (class 2606 OID 2147430)
-- Name: medication_types medication_types_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medication_types
    ADD CONSTRAINT medication_types_pkey PRIMARY KEY (medication_type_id);


--
-- TOC entry 3195 (class 2606 OID 2147012)
-- Name: patients patients_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (patient_id);


--
-- TOC entry 3193 (class 2606 OID 2146983)
-- Name: persons persons_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_pkey PRIMARY KEY (person_id);


--
-- TOC entry 3203 (class 2606 OID 2147142)
-- Name: services services_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (service_id);


--
-- TOC entry 3201 (class 2606 OID 2147123)
-- Name: specialties specialties_pkey; Type: CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.specialties
    ADD CONSTRAINT specialties_pkey PRIMARY KEY (specialty_id);


--
-- TOC entry 3241 (class 2606 OID 2147244)
-- Name: appointments appointments_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctors(doctor_id);


--
-- TOC entry 3242 (class 2606 OID 2147254)
-- Name: appointments appointments_establishment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_establishment_id_fkey FOREIGN KEY (establishment_id) REFERENCES public.establishments(establishment_id);


--
-- TOC entry 3243 (class 2606 OID 2147249)
-- Name: appointments appointments_insurance_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_insurance_id_fkey FOREIGN KEY (insurance_id) REFERENCES public.insurances(insurance_id);


--
-- TOC entry 3244 (class 2606 OID 2147239)
-- Name: appointments appointments_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.appointments
    ADD CONSTRAINT appointments_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(patient_id);


--
-- TOC entry 3232 (class 2606 OID 2147035)
-- Name: companies companies_contact_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_contact_person_id_fkey FOREIGN KEY (contact_person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 3251 (class 2606 OID 2147391)
-- Name: diseases diseases_disease_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.diseases
    ADD CONSTRAINT diseases_disease_type_id_fkey FOREIGN KEY (disease_type_id) REFERENCES public.disease_types(disease_type_id);


--
-- TOC entry 3233 (class 2606 OID 2147108)
-- Name: doctors doctors_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3234 (class 2606 OID 2147098)
-- Name: doctors doctors_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 3235 (class 2606 OID 2147153)
-- Name: doctors doctors_specialties_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_specialties_id_fkey FOREIGN KEY (specialty_id) REFERENCES public.specialties(specialty_id);


--
-- TOC entry 3239 (class 2606 OID 2147172)
-- Name: establishments establishments_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.establishments
    ADD CONSTRAINT establishments_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3252 (class 2606 OID 2147412)
-- Name: exam_types exam_types_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.exam_types
    ADD CONSTRAINT exam_types_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3255 (class 2606 OID 2147475)
-- Name: exams exams_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3256 (class 2606 OID 2147470)
-- Name: exams exams_exam_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.exams
    ADD CONSTRAINT exams_exam_type_id_fkey FOREIGN KEY (exam_type_id) REFERENCES public.exam_types(exam_type_id);


--
-- TOC entry 3229 (class 2606 OID 2147018)
-- Name: patients fk_person_id; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT fk_person_id FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 3259 (class 2606 OID 2147523)
-- Name: image_exams image_exams_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.image_exams
    ADD CONSTRAINT image_exams_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3260 (class 2606 OID 2147518)
-- Name: image_exams image_exams_image_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.image_exams
    ADD CONSTRAINT image_exams_image_type_id_fkey FOREIGN KEY (image_type_id) REFERENCES public.image_types(image_type_id);


--
-- TOC entry 3254 (class 2606 OID 2147451)
-- Name: image_types image_types_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.image_types
    ADD CONSTRAINT image_types_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3240 (class 2606 OID 2147191)
-- Name: insurances insurances_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.insurances
    ADD CONSTRAINT insurances_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 3245 (class 2606 OID 2147313)
-- Name: medical_attentions medical_attentions_appointment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_appointment_id_fkey FOREIGN KEY (appointment_id) REFERENCES public.appointments(appointment_id);


--
-- TOC entry 3246 (class 2606 OID 2147338)
-- Name: medical_attentions medical_attentions_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3247 (class 2606 OID 2147323)
-- Name: medical_attentions medical_attentions_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctors(doctor_id);


--
-- TOC entry 3248 (class 2606 OID 2147318)
-- Name: medical_attentions medical_attentions_establishment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_establishment_id_fkey FOREIGN KEY (establishment_id) REFERENCES public.establishments(establishment_id);


--
-- TOC entry 3249 (class 2606 OID 2147333)
-- Name: medical_attentions medical_attentions_insurance_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_insurance_id_fkey FOREIGN KEY (insurance_id) REFERENCES public.insurances(insurance_id);


--
-- TOC entry 3250 (class 2606 OID 2147328)
-- Name: medical_attentions medical_attentions_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medical_attentions
    ADD CONSTRAINT medical_attentions_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.services(service_id);


--
-- TOC entry 3257 (class 2606 OID 2147499)
-- Name: medication_diets medication_diets_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medication_diets
    ADD CONSTRAINT medication_diets_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3258 (class 2606 OID 2147494)
-- Name: medication_diets medication_diets_medication_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medication_diets
    ADD CONSTRAINT medication_diets_medication_type_id_fkey FOREIGN KEY (medication_type_id) REFERENCES public.medication_types(medication_type_id);


--
-- TOC entry 3253 (class 2606 OID 2147431)
-- Name: medication_types medication_types_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.medication_types
    ADD CONSTRAINT medication_types_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3230 (class 2606 OID 2147050)
-- Name: patients patients_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3231 (class 2606 OID 2147013)
-- Name: patients patients_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id);


--
-- TOC entry 3228 (class 2606 OID 2147045)
-- Name: persons persons_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3237 (class 2606 OID 2147143)
-- Name: services services_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3238 (class 2606 OID 2147148)
-- Name: services services_specialty_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_specialty_id_fkey FOREIGN KEY (specialty_id) REFERENCES public.specialties(specialty_id);


--
-- TOC entry 3236 (class 2606 OID 2147124)
-- Name: specialties specialties_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: datapluserp
--

ALTER TABLE ONLY public.specialties
    ADD CONSTRAINT specialties_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(company_id);


--
-- TOC entry 3428 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2024-02-17 11:35:06 -05

--
-- PostgreSQL database dump complete
--

