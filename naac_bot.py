import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ANSWERS = [
    (re.compile(r"full form|what is naac|meaning of naac", re.I),
     "NAAC stands for the National Assessment and Accreditation Council. The University Grants Commission says NAAC was established in 1994 to evaluate the performance of universities and colleges in India.",
     "Source: https://www.ugc.gov.in/Aboutus/NAAC"),
    (re.compile(r"purpose|why was naac|what does naac do|aim of naac", re.I),
     "NAAC evaluates higher education institutions through assessment and accreditation. The UGC describes the process as performance evaluation based on self-study and peer review using defined criteria.",
     "Source: https://www.ugc.gov.in/Aboutus/NAAC"),
    (re.compile(r"iqac|internal quality assurance", re.I),
     "IQAC means Internal Quality Assurance Cell. It supports an institution's ongoing quality assurance and improvement work, such as coordinating quality initiatives and keeping records organized.",
     "Applicable IQAC and reporting requirements can depend on institution type and current NAAC guidance."),
    (re.compile(r"ssr|self.?study report", re.I),
     "SSR means Self-Study Report. It is an institution's structured self-evaluation for an assessment process, prepared in the format applicable to its institution type and cycle.",
     "Use the current official manual or portal instructions for required sections and format."),
    (re.compile(r"aqar|annual quality assurance report", re.I),
     "AQAR means Annual Quality Assurance Report. Some NAAC guidance uses it for annual quality reporting by institutions; check whether it applies to your institution and current cycle.",
     "Use current NAAC guidance for the relevant institution category."),
    (re.compile(r"grade|score|cgpa|predict|rank|result", re.I),
     "I cannot predict or assign an NAAC grade or score. The official outcome depends on the applicable assessment process and verified institutional information.",
     "Check official NAAC communications for results; this demo is not an evaluator."),
    (re.compile(r"deadline|last date|schedule|due date|when is", re.I),
     "I cannot confirm current deadlines because this demo does not connect to live NAAC notices.",
     "Check the official NAAC portal for latest dates: https://assessmentonline-basic.naac.gov.in/"),
    (re.compile(r"eligib|eligible|eligibility", re.I),
     "Eligibility depends on the applicable rules and institution category. I cannot determine official eligibility from this demo.",
     "Confirm eligibility using the current official NAAC manual and portal."),
    (re.compile(r"visit|peer team|assessment team", re.I),
     "Prepare a shared evidence repository, assign a contact for each topic, and check that submitted information matches underlying records. Make sure relevant staff can explain how documented practices are carried out.",
     "Visit format and procedures can vary. Follow instructions for the current cycle."),
    (re.compile(r"data accuracy|verify data|check data|quantitative|numbers correct", re.I),
     "For each data point, record its source, reporting period, owner, and calculation method. Have a second person compare the submitted value with the source record and document corrections.",
     "Follow metric-specific definitions and evidence requirements in the current manual."),
    (re.compile(r"team|roles|responsibilit|who should", re.I),
     "Assign one coordinator and a responsible owner for each applicable criterion or metric. Include the departments that hold the source records, and set a review date before submission.",
     "Use your institution's governance process and current NAAC instructions to confirm responsibilities."),
    (re.compile(r"evidence|document|record|proof", re.I),
     "Create an evidence register with the requirement, source record, owner, date range, and verification status. Keep submitted information traceable to original institutional records.",
     "This is a preparation method, not an official exhaustive document list. Check the current NAAC manual."),
    (re.compile(r"benefit|advantage|why accreditation|value of accreditation", re.I),
     "Accreditation provides a structured way to review institutional quality and identify areas for improvement. It can also make an institution's quality processes more transparent to stakeholders.",
     "It does not guarantee a particular grade, funding, admission outcome, or other benefit."),
    (re.compile(r"plagiarism|ethic|original|copy|ai use", re.I),
     "Use the bot as a study and planning aid. Write the report in your own words, verify factual claims against official sources, and follow your course rules for acknowledging AI assistance.",
     "Do not submit generated text as original work if your instructor requires disclosure."),
    (re.compile(r"criteria|criterion|framework|metric|assessment", re.I),
     "Start by identifying the framework that applies to your institution and cycle. Then map each applicable criterion or metric to an owner and supporting records.",
     "Exact criteria and evidence rules depend on the current official manual for your institution category."),
    (re.compile(r"process|accreditation|cycle|steps", re.I),
     "A practical preparation path is to confirm the applicable framework, organize institutional data and evidence, complete required portal submissions, and follow the assessment steps for that cycle.",
     "This is a high-level outline. Verify current eligibility, process, and deadlines in official NAAC guidance."),
]


def get_answer(question):
    for pattern, answer, source_note in ANSWERS:
        if pattern.search(question):
            return f"{answer}\n\n{source_note}"
    return (
        "I can help with NAAC basics, IQAC, SSR, criteria, evidence, data checks, "
        "preparation, and accreditation steps. Tell me your institution type and "
        "specific question.\n\n"
        "For current rules or deadlines, check https://assessmentonline-basic.naac.gov.in/"
    )


def send_message(event=None):
    question = question_entry.get().strip()
    if not question:
        return
    chat_area.configure(state="normal")
    chat_area.insert(tk.END, f"You: {question}\n\n")
    chat_area.insert(tk.END, f"NAAC Bot: {get_answer(question)}\n\n")
    chat_area.configure(state="disabled")
    chat_area.see(tk.END)
    question_entry.delete(0, tk.END)


def clear_chat():
    chat_area.configure(state="normal")
    chat_area.delete("1.0", tk.END)
    chat_area.configure(state="disabled")


root = tk.Tk()
root.title("NAAC Information Bot")
root.geometry("760x560")
root.minsize(480, 380)
root.configure(bg="#f5f7f4")

tk.Label(root, text="NAAC Information Bot", font=("Arial", 20, "bold"),
         bg="#f5f7f4", fg="#176b50").pack(pady=(18, 4))
tk.Label(root, text="Ask about NAAC basics, IQAC, SSR, evidence, or preparation.",
         font=("Arial", 10), bg="#f5f7f4", fg="#526158").pack(pady=(0, 12))

chat_area = ScrolledText(root, wrap=tk.WORD, font=("Arial", 11), bg="white",
                         fg="#172620", padx=12, pady=12)
chat_area.pack(fill=tk.BOTH, expand=True, padx=18, pady=8)
chat_area.insert(tk.END, "NAAC Bot: Hello! Ask me about NAAC. Try 'What is IQAC?' or 'How do I organize evidence?'\n\n")
chat_area.configure(state="disabled")

input_frame = tk.Frame(root, bg="#f5f7f4")
input_frame.pack(fill=tk.X, padx=18, pady=(8, 18))
question_entry = tk.Entry(input_frame, font=("Arial", 12))
question_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
question_entry.bind("<Return>", send_message)

tk.Button(input_frame, text="Send", command=send_message, bg="#176b50", fg="white",
          font=("Arial", 11, "bold"), padx=18, relief=tk.FLAT).pack(
              side=tk.LEFT, padx=(8, 0), ipady=5)
tk.Button(root, text="New conversation", command=clear_chat, bg="#eaf4ee",
          fg="#176b50", font=("Arial", 10), relief=tk.FLAT).pack(pady=(0, 12))

root.mainloop()

