# WholeRootLab Digital Materia Medica v0.1

This folder contains the first MVP package for WholeRootLab: a Notion-ready Digital Materia Medica sample plus a generated PDF for sharing with herbal medicine students.

## Deliverables

- `notion/WholeRootLab_Digital_Materia_Medica_v0_1.md` - master Notion import page with introduction, disclaimer, reusable template, and three monographs.
- `notion/monographs/` - individual Markdown pages for Birch, Meadowsweet, and Stinging Nettle.
- `notion/Monograph_Database.csv` - seed database for a Notion table.
- `tools/build_pdf.py` - ReportLab script that generates the polished PDF sample.
- `output/pdf/whole_root_lab_digital_materia_medica_v0_1.pdf` - generated PDF output after running the build script.

## Build

Use the bundled Python runtime available in Codex:

```bash
/Users/otto/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 tools/build_pdf.py
```

## Product Position

WholeRootLab v0.1 is an educational evidence-synthesis sample. It is intentionally cautious:

- Educational use only.
- Not medical advice.
- No diagnosis, treatment, or dosing recommendations.
- Consult qualified professionals for clinical decisions.

