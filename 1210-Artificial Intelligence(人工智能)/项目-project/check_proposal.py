# -*- coding: utf-8 -*-
"""Open proposal docx in WPS/Word, report page count, export PDF for visual check."""
import os

DOCX = r"C:\Users\admin\Desktop\港城莞AI课程\1210-Artificial Intelligence(人工智能)\项目-project\proposal_topic2.docx"
PDF = DOCX[:-5] + ".pdf"

import win32com.client

app = None
for progid in ("KWPS.Application", "Word.Application"):
    try:
        app = win32com.client.DispatchEx(progid)
        print("using", progid)
        break
    except Exception as e:
        print(progid, "unavailable:", e)
if app is None:
    raise SystemExit("no word processor COM available")

app.Visible = False
doc = app.Documents.Open(DOCX, ReadOnly=False)
doc.Repaginate()
pages = doc.ComputeStatistics(2)  # wdStatisticPages
words = doc.ComputeStatistics(0)  # wdStatisticWords
print("pages:", pages, "words:", words)
try:
    doc.ExportAsFixedFormat(PDF, 17)  # wdExportFormatPDF
    print("pdf exported:", os.path.exists(PDF))
except Exception as e:
    print("export failed:", e)
doc.Close(False)
app.Quit()
