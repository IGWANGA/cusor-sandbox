#!/usr/bin/env python3
"""Generate area-split BoQ CSVs (UTF-8 BOM) and formatted Excel workbooks (English)."""

from __future__ import annotations

import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path("/workspace/docs/procurement")

HEADERS = [
    "Item",
    "Area",
    "Trade",
    "Description",
    "Unit",
    "Qty",
    "Rate",
    "Amount",
    "Remarks",
]

LAB = "25F Laboratory"
OLD = "Existing Lab Modifications"
WH = "1F Warehouse"
ALL_AREAS = "Three packs total"
BOUNDARY = "Interface of three areas"

FONT_NAME = "Calibri"

BOQ_25F = [
    ("A", LAB, "Preliminaries", "Management, vertical transport, access and temporary works for the 25F laboratory only", "item", "1", "", "", "This area only"),
    ("A.1", LAB, "Preliminaries", "Protection of finishes, lifts and public corridors on this floor", "item", "1", "", "", ""),
    ("A.2", LAB, "Preliminaries", "Hoarding / dust screens at the office interface", "item", "1", "", "", ""),
    ("A.3", LAB, "Preliminaries", "Sorted construction waste removal (Level 25)", "item", "1", "", "", ""),
    ("B", LAB, "Partitions & doors", "Laboratory zoning partitions, vision panels, pass-throughs and lab doors", "item", "1", "", "", ""),
    ("B.1", LAB, "Partitions & doors", "Light-gauge steel stud partition, double-sided fire-rated plasterboard (incl. joints and corners)", "m2", "", "", "", "Measure from confirmed layout"),
    ("B.2", LAB, "Partitions & doors", "Laboratory door (vision panel, closer, seals)", "nr", "", "", "", ""),
    ("B.3", LAB, "Partitions & doors", "Fire door (lobby / electrical / gas bottle room, per fire review)", "nr", "", "", "", "If applicable"),
    ("B.4", LAB, "Partitions & doors", "Pass-through window (mechanical or electronic interlock)", "nr", "", "", "", "If shown on layout"),
    ("B.5", LAB, "Partitions & doors", "Internal vision panel / fixed glazed screen", "m2", "", "", "", ""),
    ("C", LAB, "Flooring", "Laboratory flooring (incl. substrate and skirting)", "item", "1", "", "", ""),
    ("C.1", LAB, "Flooring", "Clean existing floor, level, repair cracks", "m2", "", "", "", ""),
    ("C.2", LAB, "Flooring", "Laboratory epoxy floor (or equivalent PVC sheet — to be confirmed)", "m2", "", "", "", "Confirm finish"),
    ("C.3", LAB, "Flooring", "Anti-static flooring (equipment room, if required)", "m2", "", "", "", "Equipment room only"),
    ("C.4", LAB, "Flooring", "Chemical-resistant skirting", "m", "", "", "", ""),
    ("C.5", LAB, "Flooring", "Floor drain and falls (wet areas)", "nr", "", "", "", ""),
    ("D", LAB, "Walls & ceilings", "Laboratory wall finishes and ceiling", "item", "1", "", "", ""),
    ("D.1", LAB, "Walls & ceilings", "Chemical-resistant wall coating / laboratory wall panels", "m2", "", "", "", "Confirm paint or panels"),
    ("D.2", LAB, "Walls & ceilings", "Aluminium or clean-room ceiling (incl. grid and access panels)", "m2", "", "", "", ""),
    ("D.3", LAB, "Walls & ceilings", "Equipment hangers and fire-stopping at ceiling penetrations", "item", "1", "", "", ""),
    ("E", LAB, "Lab furniture", "Benches, reagent cabinets, glassware cabinets and installation", "item", "1", "", "", "Furniture supply scope TBC"),
    ("E.1", LAB, "Lab furniture", "Wall / island bench (worktop, frame, reagent shelf)", "m", "", "", "", "Per layout"),
    ("E.2", LAB, "Lab furniture", "Reagent cabinet / glassware cabinet / changing locker", "nr", "", "", "", ""),
    ("E.3", LAB, "Lab furniture", "Builder’s work for emergency shower / eyewash (opening and fixings)", "set", "", "", "", "Note if client-supplied"),
    ("F", LAB, "Fume hoods & extract", "Fume hoods and laboratory extract / make-up air", "item", "1", "", "", ""),
    ("F.1", LAB, "Fume hoods & extract", "Fume hood supply and install (incl. face-velocity commissioning)", "nr", "", "", "", "Qty per layout"),
    ("F.2", LAB, "Fume hoods & extract", "Extract ductwork (incl. supports and fire dampers)", "m", "", "", "", ""),
    ("F.3", LAB, "Fume hoods & extract", "Make-up / 100% fresh-air ductwork", "m", "", "", "", ""),
    ("F.4", LAB, "Fume hoods & extract", "Extract / roof fan (incl. vibration isolation and cowl)", "nr", "", "", "", "Location TBC"),
    ("F.5", LAB, "Fume hoods & extract", "Room pressure and air-volume balancing", "item", "1", "", "", ""),
    ("G", LAB, "HVAC", "Laboratory air-conditioning (comfort or process — TBC)", "item", "1", "", "", ""),
    ("G.1", LAB, "HVAC", "Indoor unit / terminal / grille", "nr", "", "", "", ""),
    ("G.2", LAB, "HVAC", "Refrigerant pipe / condensate drain", "m", "", "", "", ""),
    ("G.3", LAB, "HVAC", "Controls point", "nr", "", "", "", ""),
    ("H", LAB, "Electrical", "Laboratory power and lighting", "item", "1", "", "", ""),
    ("H.1", LAB, "Electrical", "Dedicated laboratory DB and breakers", "nr", "", "", "", ""),
    ("H.2", LAB, "Electrical", "Cables, tray and conduit", "m", "", "", "", ""),
    ("H.3", LAB, "Electrical", "Under-bench / wall sockets (weatherproof covers where needed)", "nr", "", "", "", ""),
    ("H.4", LAB, "Electrical", "Clean-room / panel luminaire", "set", "", "", "", ""),
    ("H.5", LAB, "Electrical", "Emergency lighting and exit signs", "set", "", "", "", ""),
    ("H.6", LAB, "Electrical", "Equipotential bonding and earthing", "item", "1", "", "", "Required for laboratory"),
    ("H.7", LAB, "Electrical", "Electrical testing and commissioning", "item", "1", "", "", ""),
    ("I", LAB, "Plumbing", "Lab water, purified-water points and waste", "item", "1", "", "", ""),
    ("I.1", LAB, "Plumbing", "Bench sink, tap and pipework", "set", "", "", "", ""),
    ("I.2", LAB, "Plumbing", "Purified / DI water point builder’s work", "nr", "", "", "", "Builder’s work only if system is client-supplied"),
    ("I.3", LAB, "Plumbing", "Chemical-resistant waste pipe", "m", "", "", "", ""),
    ("I.4", LAB, "Plumbing", "Waste collection / neutralisation (provisional)", "item", "1", "", "", "Optional — pending process"),
    ("I.5", LAB, "Plumbing", "Emergency shower water supply and drain", "set", "", "", "", ""),
    ("I.6", LAB, "Plumbing", "Pressure test and flush", "item", "1", "", "", ""),
    ("J", LAB, "Special gases", "Gas bottle room and pipework (if applicable)", "item", "1", "", "", "Delete whole trade if not required"),
    ("J.1", LAB, "Special gases", "Cylinder restraint and gas pipework", "m", "", "", "", ""),
    ("J.2", LAB, "Special gases", "Flammable / toxic gas detector", "nr", "", "", "", ""),
    ("K", LAB, "ELV", "Data, access control, CCTV and fire alarm", "item", "1", "", "", "Confirm if in this package"),
    ("K.1", LAB, "ELV", "Data outlet", "nr", "", "", "", ""),
    ("K.2", LAB, "ELV", "Access-control point", "nr", "", "", "", ""),
    ("K.3", LAB, "ELV", "CCTV point", "nr", "", "", "", ""),
    ("K.4", LAB, "ELV", "Fire detector / MCP / sounder", "nr", "", "", "", ""),
    ("L", LAB, "Fire & handover", "Fire-stopping, extinguishers and clean handover", "item", "1", "", "", ""),
    ("L.1", LAB, "Fire & handover", "Fire-stopping of sleeves and openings", "item", "1", "", "", ""),
    ("L.2", LAB, "Fire & handover", "Extinguisher cabinet and contents", "set", "", "", "", ""),
    ("L.3", LAB, "Fire & handover", "Final clean and removal of protection", "item", "1", "", "", ""),
    ("M", LAB, "Provisional", "Contingency for 25F laboratory (optional)", "item", "1", "", "", "Delete if not required"),
]

BOQ_OLD = [
    ("A", OLD, "Protection", "Protect retained equipment, services and adjacent rooms during works", "item", "1", "", "", ""),
    ("A.1", OLD, "Protection", "Wrap existing instruments and benches; rigid barriers", "item", "1", "", "", "Required at occupied interfaces"),
    ("A.2", OLD, "Protection", "Isolation, dust control and temporary access", "item", "1", "", "", ""),
    ("B", OLD, "Strip-out", "Strip partitions, ceilings, floors, benches and redundant services in the alteration zone", "item", "1", "", "", "Confirm retain list before strip-out"),
    ("B.1", OLD, "Strip-out", "Remove light partitions (incl. cart-away)", "m2", "", "", "", ""),
    ("B.2", OLD, "Strip-out", "Local ceiling strip-out", "m2", "", "", "", ""),
    ("B.3", OLD, "Strip-out", "Local floor-finish removal", "m2", "", "", "", ""),
    ("B.4", OLD, "Strip-out", "Remove or disconnect benches for relocation (no new furniture)", "item", "1", "", "", "Confirm relocate vs dispose"),
    ("B.5", OLD, "Strip-out", "Remove redundant electrical points and make good", "nr", "", "", "", ""),
    ("B.6", OLD, "Strip-out", "Remove redundant plumbing / extract duct", "m", "", "", "", ""),
    ("B.7", OLD, "Strip-out", "Construction waste removal", "item", "1", "", "", ""),
    ("C", OLD, "Builder’s work", "Partitions, doors, floors, walls and ceilings made good or new to the altered layout", "item", "1", "", "", ""),
    ("C.1", OLD, "Builder’s work", "New / modified light-gauge stud partition", "m2", "", "", "", ""),
    ("C.2", OLD, "Builder’s work", "Relocate, replace or block door openings", "nr", "", "", "", ""),
    ("C.3", OLD, "Builder’s work", "Floor patching and local epoxy / PVC matching", "m2", "", "", "", "Match retained floor colour"),
    ("C.4", OLD, "Builder’s work", "Wall repair and chemical-resistant recoating", "m2", "", "", "", ""),
    ("C.5", OLD, "Builder’s work", "Ceiling repair, level and replace damaged tiles", "m2", "", "", "", ""),
    ("D", OLD, "Bench alterations", "Relocate, join and patch retained lab furniture", "item", "1", "", "", ""),
    ("D.1", OLD, "Bench alterations", "Move benches, re-fix and level", "m", "", "", "", ""),
    ("D.2", OLD, "Bench alterations", "Cut worktops, edge and recut sink openings", "item", "1", "", "", ""),
    ("D.3", OLD, "Bench alterations", "Short run of new wall bench (gap infill only)", "m", "", "", "", "Large new runs belong on the 25F pack"),
    ("E", OLD, "Electrical alterations", "Relocate circuits, adjust DB and lighting points", "item", "1", "", "", ""),
    ("E.1", OLD, "Electrical alterations", "Relocate or add socket / circuit", "nr", "", "", "", ""),
    ("E.2", OLD, "Electrical alterations", "Relocate or replace luminaire", "set", "", "", "", ""),
    ("E.3", OLD, "Electrical alterations", "Adjust circuits in existing DB", "item", "1", "", "", "Keep existing board unless capacity is short"),
    ("E.4", OLD, "Electrical alterations", "Insulation and energisation tests after works", "item", "1", "", "", ""),
    ("F", OLD, "HVAC / extract alterations", "Reroute ductwork, relocate fume hoods and rebalance air", "item", "1", "", "", ""),
    ("F.1", OLD, "HVAC / extract alterations", "Relocate fume hood (incl. reconnect extract)", "nr", "", "", "", "Delete if hood is scrapped"),
    ("F.2", OLD, "HVAC / extract alterations", "Reroute extract / make-up duct", "m", "", "", "", ""),
    ("F.3", OLD, "HVAC / extract alterations", "Relocate indoor AC unit or adjust grilles", "nr", "", "", "", ""),
    ("F.4", OLD, "HVAC / extract alterations", "Recommission air volume and room pressure", "item", "1", "", "", ""),
    ("G", OLD, "Plumbing alterations", "Relocate sinks, taps and waste", "item", "1", "", "", ""),
    ("G.1", OLD, "Plumbing alterations", "Relocate hot/cold water point", "nr", "", "", "", ""),
    ("G.2", OLD, "Plumbing alterations", "Reroute chemical-resistant waste", "m", "", "", "", ""),
    ("G.3", OLD, "Plumbing alterations", "Relocate floor drain and make good falls", "nr", "", "", "", ""),
    ("G.4", OLD, "Plumbing alterations", "Pressure test and flush after works", "item", "1", "", "", ""),
    ("H", OLD, "ELV alterations", "Relocate data, access, CCTV and fire points with partitions", "item", "1", "", "", "Confirm if in this package"),
    ("H.1", OLD, "ELV alterations", "Relocate / reinstate data outlet", "nr", "", "", "", ""),
    ("H.2", OLD, "ELV alterations", "Relocate access / CCTV point", "nr", "", "", "", ""),
    ("H.3", OLD, "ELV alterations", "Relocate and reset fire detector", "nr", "", "", "", ""),
    ("I", OLD, "Make-good & clean", "Interface with retained areas, close openings, clean handover", "item", "1", "", "", ""),
    ("I.1", OLD, "Make-good & clean", "Fire-stop openings and decorative close-up", "item", "1", "", "", ""),
    ("I.2", OLD, "Make-good & clean", "Match finishes and floors to unaltered areas", "item", "1", "", "", "Avoid obvious colour mismatch"),
    ("I.3", OLD, "Make-good & clean", "Final clean, remove protection, assist equipment reset", "item", "1", "", "", ""),
    ("J", OLD, "Provisional", "Contingency for existing-lab alterations (optional; hidden services risk)", "item", "1", "", "", "Delete if not required"),
]

BOQ_WH = [
    ("A", WH, "Preliminaries", "Management, unloading access, hoarding and temporary works for the 1F warehouse only", "item", "1", "", "", "This area only"),
    ("A.1", WH, "Preliminaries", "Occupation of 1F loading door, temporary hoarding and traffic guidance", "item", "1", "", "", ""),
    ("A.2", WH, "Preliminaries", "Protection of columns, doorways and completed floors", "item", "1", "", "", ""),
    ("A.3", WH, "Preliminaries", "Construction waste removal (Level 1)", "item", "1", "", "", ""),
    ("B", WH, "Flooring", "Warehouse slab, levelling, finish and lining", "item", "1", "", "", ""),
    ("B.1", WH, "Flooring", "Clean existing slab, repair hollow spots, level", "m2", "", "", "", ""),
    ("B.2", WH, "Flooring", "Concrete make-up / hardener (if required)", "m2", "", "", "", "Confirm if structural slab already exists"),
    ("B.3", WH, "Flooring", "Epoxy floor (or wear-resistant finish — TBC)", "m2", "", "", "", ""),
    ("B.4", WH, "Flooring", "Bay / aisle lining and numbering", "m", "", "", "", ""),
    ("B.5", WH, "Flooring", "Column guards / corner protection", "nr", "", "", "", ""),
    ("C", WH, "Walls & doors", "Wall coatings, impact protection and doors", "item", "1", "", "", ""),
    ("C.1", WH, "Walls & doors", "Internal plaster repair and paint (incl. intumescent if required)", "m2", "", "", "", ""),
    ("C.2", WH, "Walls & doors", "Powered roller shutter (incl. guides, motor, controls)", "nr", "", "", "", "Loading door"),
    ("C.3", WH, "Walls & doors", "Pedestrian fire / escape door", "nr", "", "", "", ""),
    ("C.4", WH, "Walls & doors", "Lobby, canopy or loading-dock rain protection", "item", "1", "", "", "If present on site"),
    ("D", WH, "Racking builder’s work", "Racking bases, embeds and install attend (racking supply excluded unless confirmed)", "item", "1", "", "", "Confirm racking supply with procurement"),
    ("D.1", WH, "Racking builder’s work", "Embed / chemical-anchor racking base bolts", "nr", "", "", "", ""),
    ("D.2", WH, "Racking builder’s work", "Local thickened base or blinding", "m3", "", "", "", "Per racking supplier loads"),
    ("D.3", WH, "Racking builder’s work", "Racking supply and install (provisional, optional)", "item", "1", "", "", "Delete if not in this contract"),
    ("E", WH, "Power & lighting", "Warehouse power distribution and high-bay lighting", "item", "1", "", "", ""),
    ("E.1", WH, "Power & lighting", "Warehouse distribution board", "nr", "", "", "", ""),
    ("E.2", WH, "Power & lighting", "Cables, tray and conduit", "m", "", "", "", ""),
    ("E.3", WH, "Power & lighting", "High-bay / LED industrial luminaire", "set", "", "", "", ""),
    ("E.4", WH, "Power & lighting", "Emergency lighting and exit signs", "set", "", "", "", ""),
    ("E.5", WH, "Power & lighting", "Forklift / charging or power socket (if required)", "nr", "", "", "", ""),
    ("E.6", WH, "Power & lighting", "Electrical testing and commissioning", "item", "1", "", "", ""),
    ("F", WH, "Ventilation", "Warehouse ventilation (fans or duct, per height and stock)", "item", "1", "", "", "Delete if natural ventilation only"),
    ("F.1", WH, "Ventilation", "Extract fan / roof fan", "nr", "", "", "", ""),
    ("F.2", WH, "Ventilation", "Duct and grille (if any)", "m", "", "", "", ""),
    ("G", WH, "Fire", "Warehouse sprinklers, detection, extinguishers and fire-stopping", "item", "1", "", "", "Per fire review"),
    ("G.1", WH, "Fire", "Sprinkler pipe, heads and supports", "m", "", "", "", "Note if tying into existing system"),
    ("G.2", WH, "Fire", "Smoke / heat detector", "nr", "", "", "", ""),
    ("G.3", WH, "Fire", "Relocate or add hose-reel cabinet (if required)", "set", "", "", "", ""),
    ("G.4", WH, "Fire", "Extinguisher cabinet and contents", "set", "", "", "", ""),
    ("G.5", WH, "Fire", "Fire-stopping", "item", "1", "", "", ""),
    ("H", WH, "ELV", "CCTV, access and data (warehouse office corner, if any)", "item", "1", "", "", "Confirm if in this package"),
    ("H.1", WH, "ELV", "CCTV point", "nr", "", "", "", "Loading door and storage"),
    ("H.2", WH, "ELV", "Access-control point", "nr", "", "", "", ""),
    ("H.3", WH, "ELV", "Data outlet (duty / small office)", "nr", "", "", "", ""),
    ("I", WH, "Ancillary room (optional)", "Duty / small office partitions and simple fit-out inside the warehouse", "item", "1", "", "", "Delete whole trade if no ancillary room"),
    ("I.1", WH, "Ancillary room (optional)", "Light partitions and door", "m2", "", "", "", ""),
    ("I.2", WH, "Ancillary room (optional)", "Simple ceiling, floor and lights", "m2", "", "", "", ""),
    ("J", WH, "Signage & handover", "Signs and final clean", "item", "1", "", "", ""),
    ("J.1", WH, "Signage & handover", "Safety signs, height limit, no-storage and escape plan", "item", "1", "", "", ""),
    ("J.2", WH, "Signage & handover", "Final clean and removal of protection", "item", "1", "", "", ""),
    ("K", WH, "Provisional", "Contingency for 1F warehouse (optional)", "item", "1", "", "", "Delete if not required"),
]

SUMMARY = [
    ("A", LAB, "Area subtotal", "All additional works for the 25F laboratory (see itemised sheet)", "item", "1", "", "", "Amount from sheet “25F Laboratory”"),
    ("B", OLD, "Area subtotal", "All additional works for existing lab modifications (see itemised sheet)", "item", "1", "", "", "Amount from sheet “Existing Lab Mods”"),
    ("C", WH, "Area subtotal", "All additional works for the 1F warehouse (see itemised sheet)", "item", "1", "", "", "Amount from sheet “1F Warehouse”"),
    ("D", ALL_AREAS, "Total", "A + B + C above; additional / extra scope only", "item", "1", "", "", "Excludes original contract"),
]

DWG_25F = [
    ("A-L25-001", LAB, "25F laboratory — floor layout (draft)", "Architecture", "A", "2026-09-03", "Draft — for review", "drawings/25f-lab/", "Partitions, zoning, doors"),
    ("A-L25-002", LAB, "25F laboratory — bench and furniture layout", "Architecture", "A", "2026-09-03", "Draft / TBD", "drawings/25f-lab/", ""),
    ("A-L25-003", LAB, "25F laboratory — RCP / lighting", "Architecture", "A", "2026-09-03", "Not started / TBD", "drawings/25f-lab/", ""),
    ("E-L25-001", LAB, "25F laboratory — electrical layout", "MEP", "A", "2026-09-03", "Draft / TBD", "drawings/25f-lab/", "Sockets, lighting, DB"),
    ("M-L25-001", LAB, "25F laboratory — extract / HVAC layout", "MEP", "A", "2026-09-03", "Draft / TBD", "drawings/25f-lab/", "Fume hoods and extract"),
    ("P-L25-001", LAB, "25F laboratory — plumbing layout", "MEP", "A", "2026-09-03", "Draft / TBD", "drawings/25f-lab/", "Lab sinks, waste, shower"),
]
DWG_OLD = [
    ("A-OL-001", OLD, "Existing lab — as-built / strip-out", "Architecture", "A", "2026-09-03", "Draft — for review", "drawings/old-lab/", "Mark retain / strip-out"),
    ("A-OL-002", OLD, "Existing lab — altered layout", "Architecture", "A", "2026-09-03", "Draft — for review", "drawings/old-lab/", "Read against strip-out drawing"),
    ("A-OL-003", OLD, "Existing lab — bench and services relocation overlay", "Sketch", "A", "2026-09-03", "Draft / TBD", "drawings/old-lab/", "Avoid double-counting 25F new work"),
    ("E-OL-001", OLD, "Existing lab — electrical relocation", "MEP", "A", "2026-09-03", "Draft / TBD", "drawings/old-lab/", ""),
    ("M-OL-001", OLD, "Existing lab — extract / AC relocation", "MEP", "A", "2026-09-03", "Draft / TBD", "drawings/old-lab/", ""),
]
DWG_WH = [
    ("A-WH-001", WH, "1F warehouse — floor layout (draft)", "Architecture", "A", "2026-09-03", "Draft — for review", "drawings/1f-warehouse/", "Doors, storage, ancillary"),
    ("A-WH-002", WH, "1F warehouse — floor lining and racking", "Architecture", "A", "2026-09-03", "Draft / TBD", "drawings/1f-warehouse/", "Still needed if racking is client-supplied"),
    ("E-WH-001", WH, "1F warehouse — electrical / lighting", "MEP", "A", "2026-09-03", "Draft / TBD", "drawings/1f-warehouse/", "High-bay lighting, power"),
    ("F-WH-001", WH, "1F warehouse — fire layout", "MEP", "A", "2026-09-03", "Draft / TBD", "drawings/1f-warehouse/", "Sprinklers, detection, escape"),
]
DWG_SHARED = [
    ("SK-ALL-001", BOUNDARY, "Scope boundary / original-contract interface sketch", "Sketch", "A", "2026-09-03", "Draft — for review", "drawings/", "Avoid double-counting between packs or vs original contract"),
]
DRAWINGS = DWG_25F + DWG_OLD + DWG_WH + DWG_SHARED

DRAWING_HEADERS = [
    "Dwg no.",
    "Area",
    "Title",
    "Discipline",
    "Rev",
    "Date",
    "Status",
    "File / location",
    "Remarks",
]

SHEET_LAB = "25F Laboratory"
SHEET_OLD = "Existing Lab Mods"
SHEET_WH = "1F Warehouse"


def write_csv(path: Path, headers: list[str], rows: list[tuple]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)


AREA_FILLS = {
    LAB: PatternFill("solid", fgColor="D6EAF8"),
    OLD: PatternFill("solid", fgColor="FCF3CF"),
    WH: PatternFill("solid", fgColor="D5F5E3"),
    ALL_AREAS: PatternFill("solid", fgColor="FADBD8"),
    BOUNDARY: PatternFill("solid", fgColor="E8DAEF"),
}

HEADER_ROW_FILL = PatternFill("solid", fgColor="F2F3F4")
THIN = Border(
    left=Side(style="thin", color="D9D9D9"),
    right=Side(style="thin", color="D9D9D9"),
    top=Side(style="thin", color="D9D9D9"),
    bottom=Side(style="thin", color="D9D9D9"),
)
FONT = Font(name=FONT_NAME, size=10)
FONT_BOLD = Font(name=FONT_NAME, size=10, bold=True)
WRAP = Alignment(vertical="center", wrap_text=True)
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
NAVY = PatternFill("solid", fgColor="1F4E79")


def is_section_row(seq: str) -> bool:
    return seq and "." not in str(seq)


def write_boq_sheet(ws, title: str, rows: list[tuple]) -> int:
    ws.sheet_view.showGridLines = False
    ws["A1"] = title
    ws["A1"].font = Font(name=FONT_NAME, size=16, bold=True, color="1F4E79")
    ws.merge_cells("A1:I1")
    ws.row_dimensions[1].height = 28

    ws["A2"] = "Additional / extra scope · working draft · quantities to be measured · rates should match like trades on the original contract"
    ws["A2"].font = Font(name=FONT_NAME, size=9, italic=True, color="666666")
    ws.merge_cells("A2:I2")

    header_row = 4
    for c, h in enumerate(HEADERS, 1):
        cell = ws.cell(header_row, c, h)
        cell.fill = NAVY
        cell.font = Font(name=FONT_NAME, bold=True, color="FFFFFF", size=11)
        cell.alignment = CENTER
        cell.border = THIN
    ws.row_dimensions[header_row].height = 22
    ws.freeze_panes = "A5"

    for i, row in enumerate(rows):
        r = header_row + 1 + i
        seq, area, trade, desc, unit, qty, rate, amount, note = row
        values = [seq, area, trade, desc, unit, qty, rate, amount, note]
        section = is_section_row(seq)
        fill = AREA_FILLS.get(area)
        for c, val in enumerate(values, 1):
            cell = ws.cell(r, c, val if val != "" else None)
            cell.font = FONT_BOLD if section else FONT
            cell.alignment = CENTER if c in (1, 2, 5) else WRAP
            cell.border = THIN
            if section:
                cell.fill = HEADER_ROW_FILL
            elif fill and c == 2:
                cell.fill = fill
            if c in (6, 7, 8) and val not in ("", None):
                try:
                    cell.value = float(val)
                except ValueError:
                    pass
            if c in (6, 7, 8):
                cell.number_format = "#,##0.00"
                cell.alignment = CENTER
        ws.cell(r, 8).value = f'=IF(OR(F{r}="",G{r}=""),"",F{r}*G{r})'
        ws.cell(r, 8).number_format = "#,##0.00"
        ws.row_dimensions[r].height = 32 if section else 36

    last = header_row + len(rows)
    total_row = last + 1
    for c in range(1, 10):
        ws.cell(total_row, c).fill = NAVY
        ws.cell(total_row, c).font = Font(name=FONT_NAME, bold=True, color="FFFFFF")
        ws.cell(total_row, c).border = THIN
    ws.cell(total_row, 1, f"{title} — amount subtotal")
    ws.cell(total_row, 1).alignment = Alignment(horizontal="right", vertical="center")
    ws.merge_cells(start_row=total_row, start_column=1, end_row=total_row, end_column=7)
    ws.cell(total_row, 8, f"=SUM(H{header_row+1}:H{last})")
    ws.cell(total_row, 8).number_format = "#,##0.00"
    ws.cell(total_row, 8).font = Font(name=FONT_NAME, bold=True, color="FFFFFF")
    ws.cell(total_row, 9, "0 if rates are blank — not a free quote")
    ws.cell(total_row, 9).font = Font(name=FONT_NAME, size=9, color="FFFFFF")
    ws.row_dimensions[total_row].height = 22

    widths = {"A": 10, "B": 28, "C": 24, "D": 62, "E": 8, "F": 10, "G": 12, "H": 14, "I": 36}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    ws.auto_filter.ref = f"A{header_row}:I{last}"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.print_title_rows = f"{header_row}:{header_row}"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.oddHeader.left.text = "Additional quote · for internal confirmation only"
    ws.oddFooter.center.text = "&P / &N"
    return total_row


def write_summary_sheet(ws, total_cells: dict[str, str]) -> None:
    ws.sheet_view.showGridLines = False
    ws["A1"] = "Additional quotes and drawings — split into three packs by area"
    ws["A1"].font = Font(name=FONT_NAME, size=16, bold=True, color="1F4E79")
    ws.merge_cells("A1:G1")
    ws.row_dimensions[1].height = 28

    ws["A2"] = "Date: 3 September 2026    Purpose: procurement internal confirmation of extra scope    Quotes and drawings split by the same areas    Excludes original contract"
    ws["A2"].font = Font(name=FONT_NAME, size=9, italic=True, color="666666")
    ws.merge_cells("A2:G2")

    notes = [
        "A  25F Laboratory: quote + drawings (layout, benches, extract, lab plumbing). Standalone file: A-25F-laboratory-quote-and-drawings.xlsx",
        "B  Existing lab modifications: quote + drawings (strip-out, altered layout, services relocation). Standalone file: B-existing-lab-mods-quote-and-drawings.xlsx",
        "C  1F Warehouse: quote + drawings (layout, lining/racking, lighting, fire). Standalone file: C-1F-warehouse-quote-and-drawings.xlsx",
    ]
    for i, text in enumerate(notes):
        ws.cell(4 + i, 1, text)
        ws.merge_cells(start_row=4 + i, start_column=1, end_row=4 + i, end_column=7)
        ws.cell(4 + i, 1).font = FONT
        ws.cell(4 + i, 1).alignment = WRAP
        ws.row_dimensions[4 + i].height = 32

    headers = ["No.", "Area", "Sheet", "Scope summary", "Amount", "Status (procurement)", "Remarks"]
    hr = 8
    for c, h in enumerate(headers, 1):
        cell = ws.cell(hr, c, h)
        cell.fill = NAVY
        cell.font = Font(name=FONT_NAME, bold=True, color="FFFFFF")
        cell.alignment = CENTER
        cell.border = THIN
    ws.freeze_panes = "A9"

    data = [
        ("A", LAB, SHEET_LAB, "New lab fit-out, benches, fume hoods, lab MEP", total_cells[LAB], "Pending", f'See sheet "{SHEET_LAB}"'),
        ("B", OLD, SHEET_OLD, "Protect, strip-out, relocate, make good", total_cells[OLD], "Pending", f'See sheet "{SHEET_OLD}"'),
        ("C", WH, SHEET_WH, "Floor, doors, lighting, power, fire", total_cells[WH], "Pending", f'See sheet "{SHEET_WH}"'),
    ]
    for i, (code, area, sheet, summary, formula, status, note) in enumerate(data):
        r = hr + 1 + i
        vals = [code, area, sheet, summary, None, status, note]
        fill = AREA_FILLS[area]
        for c, val in enumerate(vals, 1):
            cell = ws.cell(r, c, val)
            cell.font = FONT_BOLD if c <= 2 else FONT
            cell.alignment = CENTER if c in (1, 2, 3, 6) else WRAP
            cell.border = THIN
            cell.fill = fill
        ws.cell(r, 5, formula)
        ws.cell(r, 5).number_format = "#,##0.00"
        ws.cell(r, 5).font = FONT_BOLD
        ws.row_dimensions[r].height = 28

    total_r = hr + 4
    ws.merge_cells(start_row=total_r, start_column=1, end_row=total_r, end_column=4)
    ws.cell(total_r, 1, "Three packs total (additional / extra scope)")
    ws.cell(total_r, 1).font = Font(name=FONT_NAME, bold=True, color="FFFFFF")
    ws.cell(total_r, 1).alignment = Alignment(horizontal="right", vertical="center")
    for c in range(1, 8):
        ws.cell(total_r, c).fill = NAVY
        ws.cell(total_r, c).border = THIN
        ws.cell(total_r, c).font = Font(name=FONT_NAME, bold=True, color="FFFFFF")
    ws.cell(total_r, 5, f"=SUM(E{hr+1}:E{hr+3})")
    ws.cell(total_r, 5).number_format = "#,##0.00"
    ws.cell(total_r, 6, "Pending")
    ws.cell(total_r, 7, "Total is 0 if rates are blank — not a zero quote")

    dv = DataValidation(type="list", formula1='"Pending,Confirmed,Revise,Not required"', allow_blank=True)
    dv.error = "Choose Pending / Confirmed / Revise / Not required"
    dv.errorTitle = "Status"
    dv.prompt = "Procurement to complete"
    dv.promptTitle = "Pack status"
    ws.add_data_validation(dv)
    dv.add(f"F{hr+1}:F{hr+3}")

    ws["A14"] = "How to fill"
    ws["A14"].font = Font(name=FONT_NAME, size=12, bold=True, color="1F4E79")
    steps = [
        "1. Open the area sheet, enter Qty from site measure; enter Rate only if procurement wants a priced BoQ. Amount calculates automatically.",
        "2. Delete rows that do not belong (no fume hoods on the warehouse pack; no existing-lab strip-out on the 25F pack).",
        "3. On this sheet, mark each pack Confirmed / Revise / Not required.",
        "4. Keep drawings with the same area: drawings/25f-lab, drawings/old-lab, drawings/1f-warehouse.",
        "5. Send procurement the three standalone files (A/B/C each has quote + drawing register). Do not send the old combined BoQ.",
        "6. Racking supply, waste neutralisation, special gases and ancillary rooms are optional — delete if not required.",
    ]
    for i, s in enumerate(steps):
        ws.cell(15 + i, 1, s)
        ws.merge_cells(start_row=15 + i, start_column=1, end_row=15 + i, end_column=7)
        ws.cell(15 + i, 1).font = FONT
        ws.row_dimensions[15 + i].height = 28

    widths = {"A": 10, "B": 28, "C": 20, "D": 48, "E": 14, "F": 20, "G": 32}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.page_setup.paperSize = ws.PAPERSIZE_A4


def write_drawing_sheet(ws, title: str, rows: list[tuple]) -> None:
    ws.sheet_view.showGridLines = False
    ws["A1"] = title
    ws["A1"].font = Font(name=FONT_NAME, size=16, bold=True, color="1F4E79")
    ws.merge_cells("A1:I1")
    ws["A2"] = "Do not attach unfinished drawings. Mark them Not started / TBD. Keep drawings in the same area pack as the quote."
    ws["A2"].font = Font(name=FONT_NAME, size=9, italic=True, color="666666")
    ws.merge_cells("A2:I2")

    hr = 4
    for c, h in enumerate(DRAWING_HEADERS, 1):
        cell = ws.cell(hr, c, h)
        cell.fill = NAVY
        cell.font = Font(name=FONT_NAME, bold=True, color="FFFFFF")
        cell.alignment = CENTER
        cell.border = THIN
    ws.freeze_panes = "A5"
    for i, row in enumerate(rows):
        r = hr + 1 + i
        area = row[1]
        fill = AREA_FILLS.get(area)
        for c, val in enumerate(row, 1):
            cell = ws.cell(r, c, val)
            cell.font = FONT
            cell.alignment = CENTER if c in (1, 2, 4, 5, 6) else WRAP
            cell.border = THIN
            if fill and c == 2:
                cell.fill = fill
        ws.row_dimensions[r].height = 32
    last = hr + len(rows)
    widths = {"A": 14, "B": 28, "C": 52, "D": 14, "E": 8, "F": 14, "G": 18, "H": 22, "I": 36}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w
    ws.auto_filter.ref = f"A{hr}:I{last}"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1


def write_area_pack(path: Path, title: str, boq_rows: list[tuple], dwg_rows: list[tuple]) -> None:
    wb = Workbook()
    ws_boq = wb.active
    ws_boq.title = "Quote"
    write_boq_sheet(ws_boq, title, boq_rows)
    ws_dwg = wb.create_sheet("Drawing register")
    write_drawing_sheet(ws_dwg, f"{title} — drawing register", dwg_rows)
    wb.save(path)
    print(f"wrote {path}")


def main() -> None:
    write_csv(ROOT / "02-boq-summary.csv", HEADERS, SUMMARY)
    write_csv(ROOT / "02a-boq-25f-lab.csv", HEADERS, BOQ_25F)
    write_csv(ROOT / "02b-boq-old-lab.csv", HEADERS, BOQ_OLD)
    write_csv(ROOT / "02c-boq-1f-warehouse.csv", HEADERS, BOQ_WH)
    write_csv(ROOT / "03a-drawings-25f-lab.csv", DRAWING_HEADERS, DWG_25F)
    write_csv(ROOT / "03b-drawings-old-lab.csv", DRAWING_HEADERS, DWG_OLD)
    write_csv(ROOT / "03c-drawings-1f-warehouse.csv", DRAWING_HEADERS, DWG_WH)
    write_csv(ROOT / "03-drawing-register.csv", DRAWING_HEADERS, DRAWINGS)

    write_area_pack(ROOT / "A-25F-laboratory-quote-and-drawings.xlsx", LAB, BOQ_25F, DWG_25F)
    write_area_pack(ROOT / "B-existing-lab-mods-quote-and-drawings.xlsx", OLD, BOQ_OLD, DWG_OLD)
    write_area_pack(ROOT / "C-1F-warehouse-quote-and-drawings.xlsx", WH, BOQ_WH, DWG_WH)

    wb = Workbook()
    ws_sum = wb.active
    ws_sum.title = "Overview"

    ws_lab = wb.create_sheet(SHEET_LAB)
    ws_old = wb.create_sheet(SHEET_OLD)
    ws_wh = wb.create_sheet(SHEET_WH)
    ws_dwg_lab = wb.create_sheet("25F Drawings")
    ws_dwg_old = wb.create_sheet("Existing Lab Drawings")
    ws_dwg_wh = wb.create_sheet("1F Warehouse Drawings")
    ws_dwg_all = wb.create_sheet("Drawing register")

    lab_total_row = write_boq_sheet(ws_lab, LAB, BOQ_25F)
    old_total_row = write_boq_sheet(ws_old, OLD, BOQ_OLD)
    wh_total_row = write_boq_sheet(ws_wh, WH, BOQ_WH)

    total_cells = {
        LAB: f"='{SHEET_LAB}'!H{lab_total_row}",
        OLD: f"='{SHEET_OLD}'!H{old_total_row}",
        WH: f"='{SHEET_WH}'!H{wh_total_row}",
    }
    write_summary_sheet(ws_sum, total_cells)
    write_drawing_sheet(ws_dwg_lab, "25F Laboratory — drawing register", DWG_25F)
    write_drawing_sheet(ws_dwg_old, "Existing lab modifications — drawing register", DWG_OLD)
    write_drawing_sheet(ws_dwg_wh, "1F Warehouse — drawing register", DWG_WH)
    write_drawing_sheet(ws_dwg_all, "Drawing register — three areas + interface", DRAWINGS)

    out = ROOT / "quotes-and-drawings-by-area.xlsx"
    wb.save(out)
    print(f"wrote {out}")
    print(f"25F rows={len(BOQ_25F)} old={len(BOQ_OLD)} wh={len(BOQ_WH)} dwg={len(DRAWINGS)}")


if __name__ == "__main__":
    main()
