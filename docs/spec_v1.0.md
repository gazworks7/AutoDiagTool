# Auto Diagnostic Tool — v1.0 (MVP) Specification

## 1. Purpose
Provide a simple, guided way to analyze automotive diagnostic data exported from an Autel MD-808 Pro.  
It combines:
- **User Q&A intake** (symptoms, when the problem occurs),
- **CSV import and parsing** from the scan tool,
- **LLM (Codex/GPT) reasoning** for suggestions,
- and **organized project storage** (“Issues”) for each vehicle fault.

---

## 2. Core Workflow
1. **Create Issue** → name it (e.g., “ABS Wheel Sensor”).  
2. **Intake Form** → answer guided questions:
   - Symptom summary  
   - Intermittent or Hard-On  
   - When it occurs (cold/hot/wet)  
   - Any recent repairs or replacements  
3. **Import CSV** → app parses DTCs, Freeze-Frame, and Live Data.  
4. **LLM Assist** → model summarizes the case and suggests next checks.  
5. **Checklist Output** → printable step-by-step diagnostic plan.  
6. **Save Issue** → stored locally with all associated data.

---

## 3. Data Model (minimal)
| Entity          | Key Fields                                                 | Notes                |
| --------------- | ---------------------------------------------------------- | -------------------- |
| **Issue**       | id, title, created_on, vehicle_id, status                  | Each diagnostic case |
| **Vehicle**     | id, year, make, model, vin, odo                            | Optional details     |
| **File**        | id, issue_id, filename, imported_on, source                | Source = “Autel CSV” |
| **DTC**         | issue_id, module, code, description, first_seen_at, status | Parsed codes         |
| **FreezeFrame** | issue_id, dtc_code, timestamp, kv_pairs (JSON)             |                      |
| **LiveData**    | issue_id, timestamp, pid, value, unit                      | For plotting         |

---

## 4. Architecture Options
**A) Flutter + Python service**
- Flutter handles UI & storage.
- Python handles CSV parsing + LLM API.

**B) Python + PySide6**
- Single desktop app with local SQLite.
- Simple UI (tabs: Intake | Data | LLM | Checklist).

---

## 5. LLM Prompts (v1.0)
1. **SummarizeCase** — short plain-English summary.  
2. **NextChecks** — 5 ranked diagnostic actions.  
3. **Checklist** — 6–10 boxed steps with required tools.  
*(Always advisory — user confirms with actual tests.)*

---

## 6. CSV Parsing Rules
- Detect sections: *Read Codes*, *Freeze Frame*, *Live Data*.  
- Handle commas, semicolons, irregular headers.  
- Unknown or blank lines are ignored but logged.  
- Normalize numeric formats and units.

---

## 7. UI Outline
Left panel: Issues list  
Top tabs: Intake | Data | LLM | Checklist  
Main view: Tables + simple line chart for time-series data.

---

## 8. Privacy & Safety
- All VIN/owner data stays local.  
- No direct ECU commands; advisory output only.  
- LLM context trimmed to essential data fields.

---

## 9. Success Definition
- Import real Autel CSV, view parsed results.  
- Generate a concise checklist with reasoning.  
- Save multiple Issues per vehicle.

---

## 10. Next Steps
1. Decide on Tech Route (A or B).  
2. Prepare 1 sample CSV from MD-808 Pro.  
3. Build prototype parser and Intake UI.  
4. Hook up LLM API (Codex / GPT-5).  
5. Test end-to-end on a real fault case.