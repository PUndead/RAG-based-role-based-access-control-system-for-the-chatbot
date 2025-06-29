import os
import pandas as pd
from rag_engine import add_documents_to_collection
from textwrap import wrap

# Folder containing the role-based files
data_dir = "data"

# Mapping of roles to their corresponding files
role_files = {
    "finance": ["financial_summary.md", "quarterly_financial_report.md"],
    "marketing": [
        "marketing_report_2024.md", 
        "marketing_report_q1_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q4_2024.md"
    ],
    "hr_collection": ["hr_data.csv"],
    "engineering": ["engineering_master_doc.md"],
    "employee": ["employee_handbook.md"]
}

# Process and ingest each role's documents
for role, files in role_files.items():
    all_docs = []
    all_metadatas = []

    for filename in files:
        filepath = os.path.join(data_dir, filename)
        data_type = role.replace("_collection", "").lower()

        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            continue

        if filename.endswith(".md"):
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
                chunks = wrap(text, width=1000)
                print(f"📄 Ingesting: {filename}")
                print(f"🔸 Total chunks: {len(chunks)}")
                all_docs.extend(chunks)
                all_metadatas.extend([{"source": filename, "data_type": data_type}] * len(chunks))

        elif filename.endswith(".csv"):
            df = pd.read_csv(filepath)
            docs = df.apply(lambda row: " | ".join(map(str, row)), axis=1).tolist()
            all_docs.extend(docs)
            all_metadatas.extend([{"source": filename, "data_type": data_type}] * len(docs))

    if all_docs:
        print(f"✅ Adding {len(all_docs)} documents to role: {data_type}")
        add_documents_to_collection(all_docs, all_metadatas)

# Persist to disk
import os
import pandas as pd
from rag_engine import add_documents_to_collection
from textwrap import wrap

# Folder containing the role-based files
data_dir = "data"

# Mapping of roles to their corresponding files
role_files = {
    "finance": ["financial_summary.md", "quarterly_financial_report.md"],
    "marketing": [
        "marketing_report_2024.md", 
        "marketing_report_q1_2024.md",
        "marketing_report_q2_2024.md",
        "marketing_report_q3_2024.md",
        "marketing_report_q4_2024.md"
    ],
    "hr_collection": ["hr_data.csv"],
    "engineering": ["engineering_master_doc.md"],
    "employee": ["employee_handbook.md"]
}

# Process and ingest each role's documents
for role, files in role_files.items():
    all_docs = []
    all_metadatas = []

    for filename in files:
        filepath = os.path.join(data_dir, filename)
        data_type = role.replace("_collection", "").lower()

        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            continue

        if filename.endswith(".md"):
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
                chunks = wrap(text, width=1000)
                print(f"📄 Ingesting: {filename}")
                print(f"🔸 Total chunks: {len(chunks)}")
                all_docs.extend(chunks)
                all_metadatas.extend([{"source": filename, "data_type": data_type}] * len(chunks))

        elif filename.endswith(".csv"):
            df = pd.read_csv(filepath)
            docs = df.apply(lambda row: " | ".join(map(str, row)), axis=1).tolist()
            all_docs.extend(docs)
            all_metadatas.extend([{"source": filename, "data_type": data_type}] * len(docs))

    if all_docs:
        print(f"✅ Adding {len(all_docs)} documents to role: {data_type}")
        add_documents_to_collection(all_docs, all_metadatas)

