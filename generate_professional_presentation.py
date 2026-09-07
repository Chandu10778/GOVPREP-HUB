from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from datetime import datetime

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Define color scheme matching academic template
HEADER_COLOR = RGBColor(25, 55, 130)  # Dark blue
ACCENT_COLOR = RGBColor(192, 0, 0)   # Red accent
TEXT_COLOR = RGBColor(0, 0, 0)
LIGHT_GRAY = RGBColor(240, 240, 240)

def add_header(slide, title_text):
    """Add header with title and institute info"""
    # Header background
    header = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(0.8))
    header.fill.solid()
    header.fill.fore_color.rgb = HEADER_COLOR
    header.line.color.rgb = HEADER_COLOR
    
    # Title in header
    title_frame = header.text_frame
    p = title_frame.paragraphs[0]
    p.text = title_text
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.alignment = PP_ALIGN.CENTER
    title_frame.margin_top = Inches(0.1)

def add_institute_footer(slide):
    """Add institute footer"""
    footer = slide.shapes.add_textbox(Inches(0.3), Inches(7), Inches(9.4), Inches(0.4))
    tf = footer.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Department of Computer Science and Engineering | IcfaiTech Faculty of Science & Technology"
    p.font.size = Pt(9)
    p.font.color.rgb = RGBColor(100, 100, 100)
    p.alignment = PP_ALIGN.CENTER

def add_content_slide(prs, title, sections_data):
    """Add content slide with title and sections"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # Add header
    add_header(slide, title)
    
    # Add content
    content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.2), Inches(9), Inches(5.6))
    tf = content_box.text_frame
    tf.word_wrap = True
    
    for idx, section in enumerate(sections_data):
        if idx > 0:
            p = tf.add_paragraph()
            p.text = ""
            p.space_after = Pt(6)
        
        # Section title
        p = tf.add_paragraph()
        p.text = section['title']
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT_COLOR
        p.space_before = Pt(12)
        p.space_after = Pt(8)
        p.level = 0
        
        # Section points
        for point in section['points']:
            p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(14)
            p.font.color.rgb = TEXT_COLOR
            p.space_after = Pt(6)
            p.level = 1
    
    add_institute_footer(slide)

# Slide 1: Title Slide
slide1 = prs.slides.add_slide(prs.slide_layouts[6])
background = slide1.background
fill = background.fill
fill.solid()
fill.fore_color.rgb = HEADER_COLOR

# Logo/Title area
logo_box = slide1.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(1.5))
logo_tf = logo_box.text_frame
logo_tf.word_wrap = True
p = logo_tf.paragraphs[0]
p.text = "AI-Powered Learning Platform"
p.font.size = Pt(48)
p.font.bold = True
p.font.color.rgb = RGBColor(255, 255, 255)
p.alignment = PP_ALIGN.CENTER

# Subtitle
subtitle_box = slide1.shapes.add_textbox(Inches(1), Inches(3.2), Inches(8), Inches(1))
subtitle_tf = subtitle_box.text_frame
subtitle_tf.word_wrap = True
p = subtitle_tf.paragraphs[0]
p.text = "Intelligent Tutoring System for Student Success"
p.font.size = Pt(28)
p.font.color.rgb = RGBColor(200, 200, 200)
p.alignment = PP_ALIGN.CENTER

# Project info
info_box = slide1.shapes.add_textbox(Inches(1), Inches(5), Inches(8), Inches(1.5))
info_tf = info_box.text_frame
info_tf.word_wrap = True
p = info_tf.paragraphs[0]
p.text = "Faculty of Science & Technology\nIcfaiTech"
p.font.size = Pt(18)
p.font.color.rgb = RGBColor(255, 255, 255)
p.alignment = PP_ALIGN.CENTER

# Date
date_box = slide1.shapes.add_textbox(Inches(1), Inches(6.7), Inches(8), Inches(0.5))
date_tf = date_box.text_frame
p = date_tf.paragraphs[0]
p.text = f"Date: {datetime.now().strftime('%d/%m/%Y')}"
p.font.size = Pt(12)
p.font.color.rgb = RGBColor(180, 180, 180)
p.alignment = PP_ALIGN.CENTER

# Slide 2: Introduction - Problem Statement & Objectives
introduction_sections = [
    {
        'title': 'Problem Statement',
        'points': [
            'Traditional education systems lack personalization and adaptive learning mechanisms',
            'Students struggle with information overload and unstructured learning resources',
            'Limited 24/7 access to expert guidance and tutoring support',
            'Difficulty in tracking progress and maintaining consistent learning engagement',
            'No real-time feedback mechanism for performance improvement'
        ]
    },
    {
        'title': 'Project Objectives',
        'points': [
            'Develop an intelligent platform that provides personalized AI-powered tutoring',
            'Create comprehensive, well-organized study material repository across multiple subjects',
            'Implement real-time chatbot assistance using advanced AI (Groq API)',
            'Build task and assignment management system with deadline tracking',
            'Design gamification features (streak system) to enhance user engagement',
            'Enable data-driven insights into student progress and learning patterns'
        ]
    }
]

add_content_slide(prs, "Introduction", introduction_sections)

# Slide 3: System Overview
system_sections = [
    {
        'title': 'System Architecture',
        'points': [
            'Frontend: React.js with responsive UI using Tailwind CSS',
            'Backend: Flask REST API for server-side logic and data management',
            'Database: SQLAlchemy ORM with relational database design',
            'AI Integration: Groq API for advanced language model capabilities'
        ]
    },
    {
        'title': 'Key Components',
        'points': [
            'User Authentication & Profile Management Module',
            'AI Chatbot Engine with context-aware conversations',
            'Study Materials Repository with categorization',
            'Task Management & Progress Tracking System',
            'Gamification Engine (Streaks & Achievements)'
        ]
    }
]

add_content_slide(prs, "System Overview", system_sections)

# Slide 4: Features & Functionalities
features_sections = [
    {
        'title': 'Core Features',
        'points': [
            'Real-time AI Chatbot: Context-aware tutoring with subject expertise',
            'Study Materials: Curated resources organized by topics and difficulty levels',
            'Dashboard Analytics: Visual progress tracking and performance metrics',
            'Task Management: Create, assign, and track assignments with deadlines',
            'Streak System: Daily engagement counter to promote consistent learning'
        ]
    },
    {
        'title': 'Additional Features',
        'points': [
            'Previous Year Questions (PYQ) section for exam preparation',
            'Current Affairs Integration for real-world context',
            'User Profile Customization and Learning Preferences',
            'Mobile-responsive design for accessibility across devices'
        ]
    }
]

add_content_slide(prs, "Features & Functionalities", features_sections)

# Slide 5: Technical Stack
tech_sections = [
    {
        'title': 'Frontend Technologies',
        'points': [
            'React.js - UI library for interactive components',
            'React Router - Client-side routing and navigation',
            'Tailwind CSS - Utility-first CSS framework for styling',
            'Lucide Icons - Modern SVG icon library'
        ]
    },
    {
        'title': 'Backend Technologies',
        'points': [
            'Python Flask - Lightweight web framework',
            'SQLAlchemy - ORM for database operations',
            'Flask-CORS - Cross-Origin Resource Sharing support',
            'Groq API - Large Language Model integration'
        ]
    }
]

add_content_slide(prs, "Technology Stack", tech_sections)

# Slide 6: Implementation & Deployment
impl_sections = [
    {
        'title': 'Development Methodology',
        'points': [
            'Modular architecture with separated concerns',
            'RESTful API design for frontend-backend communication',
            'Database normalization for data integrity',
            'Version control using Git for collaborative development'
        ]
    },
    {
        'title': 'Deployment Strategy',
        'points': [
            'Environment-based configuration management',
            'Database schema migration tools',
            'Seed scripts for initial data population',
            'Error handling and logging mechanisms',
            'API endpoint validation and authentication'
        ]
    }
]

add_content_slide(prs, "Implementation & Deployment", impl_sections)

# Slide 7: Benefits & Impact
benefits_sections = [
    {
        'title': 'Student Benefits',
        'points': [
            'Personalized learning experience tailored to individual needs',
            '24/7 access to AI tutoring without geographic limitations',
            'Improved engagement through gamification (streak system)',
            'Better organization with comprehensive task management',
            'Enhanced performance through real-time feedback'
        ]
    },
    {
        'title': 'Institutional Benefits',
        'points': [
            'Improved student retention and satisfaction rates',
            'Data-driven insights into learning patterns and outcomes',
            'Modern technological infrastructure',
            'Scalable solution for multiple cohorts and courses'
        ]
    }
]

add_content_slide(prs, "Benefits & Impact", benefits_sections)

# Slide 8: Future Roadmap
roadmap_sections = [
    {
        'title': 'Phase 2 Enhancements',
        'points': [
            'Mobile Application Development (iOS/Android)',
            'Advanced Analytics Dashboard with predictive insights',
            'Multi-language support for broader accessibility',
            'Peer-to-peer learning and collaboration features'
        ]
    },
    {
        'title': 'Long-term Vision',
        'points': [
            'Integration with institutional Learning Management Systems',
            'Advanced adaptive learning algorithms',
            'Video content integration and interactive labs',
            'Blockchain-based credential verification'
        ]
    }
]

add_content_slide(prs, "Future Roadmap", roadmap_sections)

# Slide 9: Conclusion
conclusion_slide = prs.slides.add_slide(prs.slide_layouts[6])
background = conclusion_slide.background
fill = background.fill
fill.solid()
fill.fore_color.rgb = HEADER_COLOR

# Main conclusion text
conclusion_box = conclusion_slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(2.5))
conclusion_tf = conclusion_box.text_frame
conclusion_tf.word_wrap = True

p = conclusion_tf.paragraphs[0]
p.text = "Transforming Education Through\nAI-Powered Intelligent Learning"
p.font.size = Pt(42)
p.font.bold = True
p.font.color.rgb = RGBColor(255, 255, 255)
p.alignment = PP_ALIGN.CENTER
p.space_after = Pt(20)

p = conclusion_tf.add_paragraph()
p.text = "Building a platform that empowers students, engages learners,\nand transforms educational outcomes through technology"
p.font.size = Pt(16)
p.font.color.rgb = RGBColor(200, 200, 200)
p.alignment = PP_ALIGN.CENTER

# Save presentation
output_path = r"c:\Users\chand\OneDrive\Desktop\project\AI_Learning_Platform_Professional.pptx"
prs.save(output_path)
print(f"[SUCCESS] Professional presentation created: {output_path}")
