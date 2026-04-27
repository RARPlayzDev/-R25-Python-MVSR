import google.generativeai as genai
import pandas as pd
import json
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import pagesizes
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

min_price = int(input("Enter minimum price: "))
max_price = int(input("Enter maximum price: "))

response = {
  {
    "Brand": "Acer",
    "Model": "Aspire 7 A715-76G",
    "Price": 55000,
    "CPU": "Intel i5-12450H",
    "CPU_Generation": "12th Gen",
    "Cores_Threads": "8 Cores / 12 Threads",
    "GPU": "NVIDIA RTX 2050",
    "GPU_VRAM": "4GB",
    "RAM_Size": "8GB",
    "RAM_Type": "DDR4",
    "RAM_Speed": "3200MHz",
    "Storage_Size": "512GB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "144Hz",
    "Battery": "50Wh",
    "Weight": "2.1kg",
    "Upgrade_Options": "RAM up to 32GB, extra SSD slot",
    "Best_For": "Entry gaming and students",
    "Verdict": "Best budget RTX option."
  },
  {
    "Brand": "HP",
    "Model": "Victus 15-fa0666TX",
    "Price": 60000,
    "CPU": "Intel i5-12450H",
    "CPU_Generation": "12th Gen",
    "Cores_Threads": "8 Cores / 12 Threads",
    "GPU": "NVIDIA GTX 1650",
    "GPU_VRAM": "4GB",
    "RAM_Size": "8GB",
    "RAM_Type": "DDR4",
    "RAM_Speed": "3200MHz",
    "Storage_Size": "512GB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "144Hz",
    "Battery": "52Wh",
    "Weight": "2.3kg",
    "Upgrade_Options": "RAM & SSD expandable",
    "Best_For": "Casual gaming",
    "Verdict": "Solid beginner gaming laptop."
  },
  {
    "Brand": "Lenovo",
    "Model": "IdeaPad Gaming 3 15ACH6",
    "Price": 65000,
    "CPU": "Ryzen 5 5600H",
    "CPU_Generation": "5000 Series",
    "Cores_Threads": "6 Cores / 12 Threads",
    "GPU": "NVIDIA RTX 3050",
    "GPU_VRAM": "4GB",
    "RAM_Size": "8GB",
    "RAM_Type": "DDR4",
    "RAM_Speed": "3200MHz",
    "Storage_Size": "512GB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "120Hz",
    "Battery": "45Wh",
    "Weight": "2.25kg",
    "Upgrade_Options": "Dual RAM slots, SSD upgrade",
    "Best_For": "Budget AAA gaming",
    "Verdict": "Balanced performance choice."
  },
  {
    "Brand": "ASUS",
    "Model": "TUF Gaming F15 FX506HC",
    "Price": 70000,
    "CPU": "Intel i5-11400H",
    "CPU_Generation": "11th Gen",
    "Cores_Threads": "6 Cores / 12 Threads",
    "GPU": "NVIDIA RTX 3050",
    "GPU_VRAM": "4GB",
    "RAM_Size": "16GB",
    "RAM_Type": "DDR4",
    "RAM_Speed": "3200MHz",
    "Storage_Size": "512GB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "144Hz",
    "Battery": "48Wh",
    "Weight": "2.3kg",
    "Upgrade_Options": "RAM up to 32GB",
    "Best_For": "Competitive gaming",
    "Verdict": "High refresh esports pick."
  },
  {
    "Brand": "Dell",
    "Model": "G15 5520",
    "Price": 75000,
    "CPU": "Intel i5-12500H",
    "CPU_Generation": "12th Gen",
    "Cores_Threads": "12 Cores / 16 Threads",
    "GPU": "NVIDIA RTX 3050",
    "GPU_VRAM": "4GB",
    "RAM_Size": "16GB",
    "RAM_Type": "DDR4",
    "RAM_Speed": "3200MHz",
    "Storage_Size": "512GB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "120Hz",
    "Battery": "56Wh",
    "Weight": "2.6kg",
    "Upgrade_Options": "Dual SSD support",
    "Best_For": "Gaming and streaming",
    "Verdict": "Reliable midrange performer."
  },

  {
    "Brand": "MSI",
    "Model": "GF63 Thin 12UC",
    "Price": 80000,
    "CPU": "Intel i7-12650H",
    "CPU_Generation": "12th Gen",
    "Cores_Threads": "10 Cores / 16 Threads",
    "GPU": "NVIDIA RTX 3050",
    "GPU_VRAM": "4GB",
    "RAM_Size": "16GB",
    "RAM_Type": "DDR4",
    "RAM_Speed": "3200MHz",
    "Storage_Size": "1TB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "144Hz",
    "Battery": "51Wh",
    "Weight": "1.9kg",
    "Upgrade_Options": "RAM & SSD expandable",
    "Best_For": "Portable gaming",
    "Verdict": "Lightweight power machine."
  },

  {
    "Brand": "ASUS",
    "Model": "TUF A15 FA507RE",
    "Price": 90000,
    "CPU": "Ryzen 7 6800H",
    "CPU_Generation": "6000 Series",
    "Cores_Threads": "8 Cores / 16 Threads",
    "GPU": "NVIDIA RTX 3050 Ti",
    "GPU_VRAM": "4GB",
    "RAM_Size": "16GB",
    "RAM_Type": "DDR5",
    "RAM_Speed": "4800MHz",
    "Storage_Size": "1TB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "144Hz",
    "Battery": "90Wh",
    "Weight": "2.2kg",
    "Upgrade_Options": "RAM up to 32GB",
    "Best_For": "Serious gaming",
    "Verdict": "Excellent battery gaming laptop."
  },

  {
    "Brand": "Lenovo",
    "Model": "Legion 5 15ACH6H",
    "Price": 100000,
    "CPU": "Ryzen 7 5800H",
    "CPU_Generation": "5000 Series",
    "Cores_Threads": "8 Cores / 16 Threads",
    "GPU": "NVIDIA RTX 3060",
    "GPU_VRAM": "6GB",
    "RAM_Size": "16GB",
    "RAM_Type": "DDR4",
    "RAM_Speed": "3200MHz",
    "Storage_Size": "1TB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "165Hz",
    "Battery": "80Wh",
    "Weight": "2.4kg",
    "Upgrade_Options": "Dual RAM & SSD slots",
    "Best_For": "AAA ultra settings",
    "Verdict": "Best thermal performance."
  },

  {
    "Brand": "HP",
    "Model": "Omen 16-b0370TX",
    "Price": 115000,
    "CPU": "Intel i7-12700H",
    "CPU_Generation": "12th Gen",
    "Cores_Threads": "14 Cores / 20 Threads",
    "GPU": "NVIDIA RTX 3060",
    "GPU_VRAM": "6GB",
    "RAM_Size": "16GB",
    "RAM_Type": "DDR5",
    "RAM_Speed": "4800MHz",
    "Storage_Size": "1TB",
    "Storage_Type": "NVMe",
    "Display_Size": "16.1 inch",
    "Resolution": "Full HD",
    "Refresh_Rate": "144Hz",
    "Battery": "83Wh",
    "Weight": "2.35kg",
    "Upgrade_Options": "Expandable RAM & SSD",
    "Best_For": "Gaming and editing",
    "Verdict": "Premium performance laptop."
  },

  {
    "Brand": "Acer",
    "Model": "Predator Helios 300 PH315-55",
    "Price": 130000,
    "CPU": "Intel i7-12700H",
    "CPU_Generation": "12th Gen",
    "Cores_Threads": "14 Cores / 20 Threads",
    "GPU": "NVIDIA RTX 3060",
    "GPU_VRAM": "6GB",
    "RAM_Size": "16GB",
    "RAM_Type": "DDR5",
    "RAM_Speed": "4800MHz",
    "Storage_Size": "1TB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "QHD",
    "Refresh_Rate": "165Hz",
    "Battery": "90Wh",
    "Weight": "2.5kg",
    "Upgrade_Options": "Upgradable RAM & SSD",
    "Best_For": "High resolution gaming",
    "Verdict": "Powerful QHD gaming beast."
  },

  {
    "Brand": "ASUS",
    "Model": "ROG Strix G15 G513RM",
    "Price": 148000,
    "CPU": "Ryzen 9 6900HX",
    "CPU_Generation": "6000 Series",
    "Cores_Threads": "8 Cores / 16 Threads",
    "GPU": "NVIDIA RTX 3060",
    "GPU_VRAM": "6GB",
    "RAM_Size": "32GB",
    "RAM_Type": "DDR5",
    "RAM_Speed": "4800MHz",
    "Storage_Size": "1TB",
    "Storage_Type": "NVMe",
    "Display_Size": "15.6 inch",
    "Resolution": "QHD",
    "Refresh_Rate": "165Hz",
    "Battery": "90Wh",
    "Weight": "2.3kg",
    "Upgrade_Options": "Fully upgradeable",
    "Best_For": "Hardcore gaming",
    "Verdict": "Top tier gaming performance."
  }
  ,
{
  "Brand": "MSI",
  "Model": "Katana GF66 12UE",
  "Price": 82000,
  "CPU": "Intel i7-12650H",
  "CPU_Generation": "12th Gen",
  "Cores_Threads": "10 Cores / 16 Threads",
  "GPU": "NVIDIA RTX 3050 Ti",
  "GPU_VRAM": "4GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR4",
  "RAM_Speed": "3200MHz",
  "Storage_Size": "512GB",
  "Storage_Type": "NVMe",
  "Display_Size": "15.6 inch",
  "Resolution": "Full HD",
  "Refresh_Rate": "144Hz",
  "Battery": "53Wh",
  "Weight": "2.25kg",
  "Upgrade_Options": "RAM up to 64GB, extra SSD slot",
  "Best_For": "Midrange competitive gaming",
  "Verdict": "Strong CPU gaming option."
},
{
  "Brand": "Acer",
  "Model": "Nitro 5 AN515-58",
  "Price": 88000,
  "CPU": "Intel i5-12500H",
  "CPU_Generation": "12th Gen",
  "Cores_Threads": "12 Cores / 16 Threads",
  "GPU": "NVIDIA RTX 3060",
  "GPU_VRAM": "6GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR4",
  "RAM_Speed": "3200MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "15.6 inch",
  "Resolution": "Full HD",
  "Refresh_Rate": "144Hz",
  "Battery": "57Wh",
  "Weight": "2.4kg",
  "Upgrade_Options": "Dual RAM & SSD slots",
  "Best_For": "AAA gaming medium-high",
  "Verdict": "Great RTX 3060 value."
},
{
  "Brand": "Dell",
  "Model": "G15 5530",
  "Price": 95000,
  "CPU": "Intel i7-13650HX",
  "CPU_Generation": "13th Gen",
  "Cores_Threads": "14 Cores / 20 Threads",
  "GPU": "NVIDIA RTX 3050",
  "GPU_VRAM": "6GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR5",
  "RAM_Speed": "4800MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "15.6 inch",
  "Resolution": "Full HD",
  "Refresh_Rate": "165Hz",
  "Battery": "56Wh",
  "Weight": "2.6kg",
  "Upgrade_Options": "Expandable RAM & SSD",
  "Best_For": "Multitasking and gaming",
  "Verdict": "Powerful latest generation CPU."
},
{
  "Brand": "HP",
  "Model": "Victus 16-e0333AX",
  "Price": 105000,
  "CPU": "Ryzen 7 6800H",
  "CPU_Generation": "6000 Series",
  "Cores_Threads": "8 Cores / 16 Threads",
  "GPU": "NVIDIA RTX 3060",
  "GPU_VRAM": "6GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR5",
  "RAM_Speed": "4800MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "16.1 inch",
  "Resolution": "Full HD",
  "Refresh_Rate": "144Hz",
  "Battery": "70Wh",
  "Weight": "2.4kg",
  "Upgrade_Options": "RAM up to 32GB",
  "Best_For": "Smooth AAA gameplay",
  "Verdict": "Balanced power and cooling."
},
{
  "Brand": "Lenovo",
  "Model": "Legion 5i Pro 16IAH7",
  "Price": 120000,
  "CPU": "Intel i7-12700H",
  "CPU_Generation": "12th Gen",
  "Cores_Threads": "14 Cores / 20 Threads",
  "GPU": "NVIDIA RTX 3060",
  "GPU_VRAM": "6GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR5",
  "RAM_Speed": "4800MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "16 inch",
  "Resolution": "QHD",
  "Refresh_Rate": "165Hz",
  "Battery": "80Wh",
  "Weight": "2.5kg",
  "Upgrade_Options": "Dual SSD & RAM support",
  "Best_For": "High FPS QHD gaming",
  "Verdict": "Premium display quality."
},
{
  "Brand": "ASUS",
  "Model": "ROG Zephyrus G14 GA402RJ",
  "Price": 125000,
  "CPU": "Ryzen 7 6800HS",
  "CPU_Generation": "6000 Series",
  "Cores_Threads": "8 Cores / 16 Threads",
  "GPU": "NVIDIA RX 6700S",
  "GPU_VRAM": "8GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR5",
  "RAM_Speed": "4800MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "14 inch",
  "Resolution": "QHD",
  "Refresh_Rate": "120Hz",
  "Battery": "76Wh",
  "Weight": "1.7kg",
  "Upgrade_Options": "SSD upgradeable",
  "Best_For": "Portable high-end gaming",
  "Verdict": "Compact yet powerful."
},
{
  "Brand": "Acer",
  "Model": "Predator Helios Neo 16",
  "Price": 135000,
  "CPU": "Intel i7-13700HX",
  "CPU_Generation": "13th Gen",
  "Cores_Threads": "16 Cores / 24 Threads",
  "GPU": "NVIDIA RTX 4060",
  "GPU_VRAM": "8GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR5",
  "RAM_Speed": "4800MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "16 inch",
  "Resolution": "QHD",
  "Refresh_Rate": "165Hz",
  "Battery": "90Wh",
  "Weight": "2.6kg",
  "Upgrade_Options": "Fully upgradeable",
  "Best_For": "Next-gen AAA gaming",
  "Verdict": "Future-proof RTX 4060."
},
{
  "Brand": "MSI",
  "Model": "Pulse 15 B13VFK",
  "Price": 142000,
  "CPU": "Intel i7-13700H",
  "CPU_Generation": "13th Gen",
  "Cores_Threads": "14 Cores / 20 Threads",
  "GPU": "NVIDIA RTX 4060",
  "GPU_VRAM": "8GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR5",
  "RAM_Speed": "4800MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "15.6 inch",
  "Resolution": "QHD",
  "Refresh_Rate": "165Hz",
  "Battery": "90Wh",
  "Weight": "2.3kg",
  "Upgrade_Options": "RAM & SSD expandable",
  "Best_For": "High-end gaming",
  "Verdict": "Smooth QHD experience."
},
{
  "Brand": "ASUS",
  "Model": "ROG Strix G16 G614JV",
  "Price": 150000,
  "CPU": "Intel i7-13650HX",
  "CPU_Generation": "13th Gen",
  "Cores_Threads": "14 Cores / 20 Threads",
  "GPU": "NVIDIA RTX 4060",
  "GPU_VRAM": "8GB",
  "RAM_Size": "16GB",
  "RAM_Type": "DDR5",
  "RAM_Speed": "4800MHz",
  "Storage_Size": "1TB",
  "Storage_Type": "NVMe",
  "Display_Size": "16 inch",
  "Resolution": "QHD",
  "Refresh_Rate": "165Hz",
  "Battery": "90Wh",
  "Weight": "2.5kg",
  "Upgrade_Options": "Fully expandable",
  "Best_For": "Hardcore competitive gaming",
  "Verdict": "Flagship gaming performance."
}
}
text = response.text.strip()

if "```" in text:
    text = text.split("```")[1]
    if text.startswith("json"):
        text = text[4:]

data = json.loads(text)
df = pd.DataFrame(data)

df["ValueScore"] = df["RAM"].str.extract(r'(\d+)').astype(int) * 10
best_index = df["ValueScore"].idxmax()

file_name = "Gaming_Laptops_Catalog.pdf"
doc = SimpleDocTemplate(file_name, pagesize=pagesizes.letter)
elements = []

styles = getSampleStyleSheet()
elements.append(Paragraph(
    f"<b>Gaming Laptop Catalog (₹{min_price} - ₹{max_price})</b>",
    styles["Heading1"]
))
elements.append(Spacer(1, 15))

columns = [
    "Brand", "Model", "Price", "CPU", "GPU",
    "RAM", "Storage", "Display", "Refresh_Rate"
]

table_data = [columns]

for i, row in df.iterrows():
    table_row = [
        row["Brand"],
        row["Model"],
        f"₹{row['Price']}",
        row["CPU"],
        f"{row['GPU']} ({row['GPU_VRAM']})",
        f"{row['RAM']} {row['RAM_Type']}",
        f"{row['Storage']} {row['Storage_Type']}",
        row["Display"],
        row["Refresh_Rate"]
    ]
    table_data.append(table_row)

table = Table(table_data, repeatRows=1)

table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1),
     [colors.whitesmoke, colors.lightgrey]),
]))

table.setStyle(TableStyle([
    ('BACKGROUND', (0, best_index + 1),
     (-1, best_index + 1), colors.lightgreen)
]))

elements.append(table)

elements.append(Spacer(1, 20))
elements.append(Paragraph("<b>Best Value Pick</b>", styles["Heading2"]))
elements.append(Spacer(1, 5))

best = df.loc[best_index]

best_text = f"""
{best['Brand']} {best['Model']} offers {best['RAM']} {best['RAM_Type']}
and {best['GPU']} ({best['GPU_VRAM']}) at ₹{best['Price']}.
Verdict: {best['Verdict']}
"""

elements.append(Paragraph(best_text, styles["Normal"]))

elements.append(Spacer(1, 25))
elements.append(Paragraph("<b>Understanding Laptop Specifications</b>",
                          styles["Heading2"]))
elements.append(Spacer(1, 10))

explanation_text = """
RAM: Memory used for multitasking and gaming performance.

DDR4 vs DDR5: DDR5 is newer, faster and more power efficient.

GPU: Handles gaming graphics and video processing.

GPU VRAM: Dedicated memory for graphics. More VRAM = better high-resolution gaming.

NVMe SSD: Extremely fast storage compared to older SATA drives.

Refresh Rate (Hz): Higher refresh rate like 144Hz gives smoother gameplay.

CPU: The brain of the laptop. Higher generation = better performance.
"""

elements.append(Paragraph(explanation_text, styles["Normal"]))

doc.build(elements)

print("PDF Generated Successfully:", file_name)