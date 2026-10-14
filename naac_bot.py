import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ANSWERS = [
    (re.compile(r"criteria|framework|assessment", re.I),
     "First identify the assessment framework that applies to your institution and accreditation cycle. Then map each applicable criterion or metric to an owner and supporting records.",
     "Exact requirements depend on the current NAAC manual for your institution type."),
    (re.compile(r"evidence|document|record", re.I),
     "Create an evidence register with the requirement, source record, owner, date range, and verification status. Keep submitted information traceable to source records.",
     "Check the current NAAC manual for the evidence required."),
    (re.compile(r"visit|peer|team", re.I),
     "Prepare a shared evidence repository, assign an owner for each topic, and check that submitted information matches the underlying records.",
     "Follow current NAAC instructions for visit procedures and schedules."),
    (re.compile(r"process|accreditation|cycle", re.I),
     "Confirm the applicable framework, organize institutional data and evidence, complete required portal submissions, and follow the assessment steps for your cycle.",
     "Verify eligibility, process, and deadlines using current official NAAC guidance."),
]


def get_answer(question):
    for pattern, answer, reminder in ANSWERS:
        if pattern.search(question):
            return f"{answer}\n\nReminder: {reminder}"
    return (
        "I can help with accreditation preparation, criteria, evidence, and visit readiness. "
        "Tell me your institution type and current stage for more specific guidance.\n\n"
        "Verify requirements in current official NAAC publications."
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
root.geometry("700x520")
root.minsize(450, 350)
root.configure(bg="#f5f7f4")

tk.Label(root, text="NAAC Information Bot", font=("Arial", 20, "bold"),
         bg="#f5f7f4", fg="#176b50").pack(pady=(18, 4))
tk.Label(root, text="Ask about accreditation, criteria, evidence, or visit preparation.",
         font=("Arial", 10), bg="#f5f7f4", fg="#526158").pack(pady=(0, 12))

chat_area = ScrolledText(root, wrap=tk.WORD, font=("Arial", 11), bg="white",
                         fg="#172620", padx=12, pady=12)
chat_area.pack(fill=tk.BOTH, expand=True, padx=18, pady=8)
chat_area.insert(tk.END, "NAAC Bot: Hello! Ask me a question about NAAC preparation.\n\n")
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

