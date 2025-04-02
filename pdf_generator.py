from fpdf import FPDF
from flask import Flask, request, send_file
import os

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(200, 10, "CareerBypass - Personalized Career Guide", ln=True, align='C')
        self.ln(10)
    
    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True, align='L')
        self.ln(5)
    
    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 7, body)
        self.ln(5)

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    data = request.json  # Expecting JSON input from frontend
    
    pdf = PDF()
    pdf.add_page()
    
    pdf.chapter_title("Personalized Career Guide")
    pdf.chapter_body(f"Hello {data['name']}, here is your career guide based on your input.")
    pdf.chapter_body(f"Current Industry: {data['industry']}\nDesired Industry: {data['desired_industry']}")
    pdf.chapter_body(f"Current Designation: {data['current_designation']}\nDesired Designation: {data['desired_designation']}")
    pdf.chapter_body(f"Current Salary: ₹{data['current_salary']}\nDesired Salary: ₹{data['desired_salary']}")
    
    pdf.chapter_title("Step-by-Step Action Plan")
    pdf.chapter_body("1. Identify skill gaps and enroll in relevant courses.\n2. Network with industry professionals.\n3. Work on practical projects to enhance experience.\n4. Update resume and apply for roles strategically.")
    
    file_path = "career_guide.pdf"
    pdf.output(file_path)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
