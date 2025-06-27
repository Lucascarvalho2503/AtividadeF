import xml.etree.ElementTree as ET
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Função para ler output.xml e extrair resumo dos testes
def parse_robot_output(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    total = int(root.attrib.get('total', 0))
    passed = int(root.attrib.get('passed', 0))
    failed = int(root.attrib.get('failed', 0))
    
    # Se não encontrar no root, tenta no elemento 'statistics'
    if total == 0 and root.find('statistics') is not None:
        stats = root.find('statistics')
        total = 0
        passed = 0
        failed = 0
        for stat in stats.findall('.//stat'):
            total += int(stat.attrib.get('total', 0))
            passed += int(stat.attrib.get('pass', 0))
            failed += int(stat.attrib.get('fail', 0))
    
    return total, passed, failed

# Função para criar o PPT com o resumo
def create_ppt(total, passed, failed, output_path='test_report.pptx'):
    prs = Presentation()
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # layout em branco

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(8), Inches(1))
    title_frame = title_box.text_frame
    title_frame.text = "Resumo dos Testes Robot Framework"
    title_frame.paragraphs[0].font.size = Pt(32)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

    content_box = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(6), Inches(3))
    content_tf = content_box.text_frame
    content_tf.word_wrap = True

    p1 = content_tf.add_paragraph()
    p1.text = f"Total de testes: {total}"
    p1.font.size = Pt(24)
    p1.font.color.rgb = RGBColor(0, 0, 0)

    p2 = content_tf.add_paragraph()
    p2.text = f"Testes aprovados: {passed}"
    p2.font.size = Pt(24)
    p2.font.color.rgb = RGBColor(0, 128, 0)  # verde

    p3 = content_tf.add_paragraph()
    p3.text = f"Testes falhados: {failed}"
    p3.font.size = Pt(24)
    p3.font.color.rgb = RGBColor(255, 0, 0)  # vermelho

    prs.save(output_path)
    print(f"PPT salvo em: {output_path}")

if __name__ == "__main__":
    total, passed, failed = parse_robot_output('output.xml')
    create_ppt(total, passed, failed)
