

from app import app
from models import db, Material

SAMPLE_MATERIALS = [
    {
        'title': 'Overview of the Indian Constitution',
        'subject': 'Polity',
        'level': 'Beginner',
        'content': '''
<h2>Overview of the Indian Constitution</h2>
<p>The Constitution of India is the supreme law of the land. It establishes the framework of government, defines state structure, and ensures fundamental rights for citizens.</p>

<h3>Key Features:</h3>
<ul>
  <li><strong>Longest Written Constitution:</strong> Contains 448 articles, 12 schedules, and more than 100 amendments.</li>
  <li><strong>Adopted Date:</strong> January 26, 1950, celebrated as Republic Day.</li>
  <li><strong>Constituent Assembly:</strong> Drafted under the leadership of Dr. B.R. Ambedkar.</li>
  <li><strong>Hybrid Constitution:</strong> Combines features of federal and unitary systems.</li>
</ul>

<h3>Main Parts:</h3>
<ol>
  <li><strong>Preamble:</strong> States justice, liberty, equality, and fraternity as constitutional ideals.</li>
  <li><strong>Fundamental Rights:</strong> Articles 12-35 guarantee civil liberties.</li>
  <li><strong>Directive Principles of State Policy:</strong> Articles 36-51 provide social and economic goals.</li>
  <li><strong>Fundamental Duties:</strong> Article 51A outlines citizens' responsibilities.</li>
</ol>

<h3>Why It Matters:</h3>
<p>The Constitution balances individual freedom with social equity, protects democracy, and guides policy through Directive Principles.</p>

<blockquote>
"We, the people of India, having solemnly resolved to constitute India into a sovereign democratic republic..."
</blockquote>
        ''',
        'xp_reward': 20
    },
    {
        'title': 'Fundamental Rights, Directive Principles & Duties',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '''
<h2>Fundamental Rights, Directive Principles & Duties</h2>
<p>These three pillars help shape the relationship between citizens and the state.</p>

<h3>Fundamental Rights:</h3>
<p>Articles 12-35 offer six core freedoms.</p>
<ul>

  <li><strong>Right to Equality</strong> (Articles 14-18) – equality before law and prohibition of discrimination.</li>
  <li><strong>Right to Freedom</strong> (Articles 19-22) – includes expression, assembly, association, movement.</li>
  <li><strong>Right against Exploitation</strong> (Articles 23-24) – bans trafficking and child labour.</li>
  <li><strong>Right to Freedom of Religion</strong> (Articles 25-28) – guarantees religious freedom.</li>
  <li><strong>Cultural and Educational Rights</strong> (Articles 29-30) – protect minorities.</li>
  <li><strong>Right to Constitutional Remedies</strong> (Article 32) – allows petitioning the Supreme Court.</li>
</ul>

<h3>Directive Principles of State Policy:</h3>
<ul>
  <li>Not enforceable in courts, but essential for governance.</li>
  <li>Includes goals such as social justice, welfare state, and economic equality.</li>
  <li>Examples: free legal aid, uniform civil code, protection of environment.</li>
  
</ul>

<h3>Fundamental Duties:</h3>
<ul>
  <li>Added by the 42nd Amendment in 1976.</li>
  <li>Eleven duties include respecting the Constitution, promoting harmony, protecting the environment.</li>
</ul>

<h3>Important Notes:</h3>
<ul>
  <li>The 44th Amendment removed the Right to Property from Fundamental Rights.</li>
  <li>The 86th Amendment introduced the Right to Education.</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Structure of Government and Federalism',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': '''
<h2>Structure of Government and Federalism</h2>
<p>India follows a parliamentary system with a clear separation of powers among the legislature, executive, and judiciary.</p>

<h3>Legislature:</h3>
<ul>
  <li><strong>Parliament:</strong> Bicameral body consisting of Lok Sabha and Rajya Sabha.</li>
  <li><strong>Lok Sabha:</strong> Representatives elected directly by the people.</li>
  <li><strong>Rajya Sabha:</strong> Represents states and union territories.</li>
</ul>

<h3>Executive:</h3>
<ul>
  <li><strong>President:</strong> Head of state with ceremonial powers.</li>
  <li><strong>Prime Minister:</strong> Leader of government and head of the Council of Ministers.</li>
  <li><strong>Council of Ministers:</strong> Responsible for administering ministries and policies.</li>
</ul>

<h3>Judiciary:</h3>
<ul>
  <li><strong>Supreme Court:</strong> Apex court with power of judicial review.</li>
  <li><strong>High Courts:</strong> State-level courts.</li>
  <li><strong>Subordinate Courts:</strong> District and lower courts.</li>
</ul>

<h3>Federalism:</h3>
<ul>
  <li>India is a federal republic with a strong center.</li>
  <li>Powers are divided by the Union List, State List, and Concurrent List.</li>
  <li>Inter-state relations are managed through the Inter-State Council and Finance Commission.</li>
</ul>
        ''',
        'xp_reward': 30
    },
    {
        'title': 'Ancient India: Indus, Mauryas & Guptas',
        'subject': 'History',
        'level': 'Beginner',
        'content': '''
<h2>Ancient India: Indus Valley, Mauryan Empire and Gupta Golden Age</h2>
<p>This section covers the early foundations of Indian civilisation and the rise of classical empires.</p>

<h3>Indus Valley Civilization:</h3>
<ul>
  <li>Major cities: Harappa and Mohenjo-Daro.</li>
  <li>Urban planning: grid streets, drainage systems, standardized bricks.</li>
  <li>Economy: agriculture, trade, craft specialization.</li>
</ul>

<h3>Mauryan Empire:</h3>
<ul>
  <li><strong>Founder:</strong> Chandragupta Maurya.</li>
  <li><strong>Administration:</strong> Centralized state with a detailed bureaucracy described by Kautilya.</li>
  <li><strong>Emperor Ashoka:</strong> Spread Buddhism and promoted dhamma after Kalinga War.</li>
</ul>

<h3>Gupta Empire:</h3>
<ul>
  <li>Often called India’s Golden Age.</li>
  <li>Key rulers: Chandragupta I, Samudragupta, Chandragupta II.</li>
  <li>Achievements: mathematics, astronomy, literature, temple architecture.</li>
</ul>
        ''',
        'xp_reward': 20
    },
    {
        'title': 'Mughal Empire: Administration and Culture',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '''
<h2>Mughal Empire: Administration, Culture and Decline</h2>
<p>The Mughal Empire shaped Indian culture, administration, and architecture for centuries.</p>

<h3>Administrative System:</h3>
<ul>
  <li><strong>Central Administration:</strong> Emperor, nobles, and revenue officials.</li>
  <li><strong>Mansabdari System:</strong> Ranked officers were paid through jagirs.</li>
  <li><strong>Zamindars:</strong> Local landlords who collected revenue.</li>
</ul>

<h3>Cultural Contributions:</h3>
<ul>
  <li>Monumental architecture: Taj Mahal, Red Fort, Fatehpur Sikri.</li>
  <li>Art and painting: Mughal miniatures combining Persian and Indian styles.</li>
  <li>Language and literature: Persian and Urdu flourished.</li>
</ul>

<h3>Decline of the Empire:</h3>
<ul>
  <li>Weak successors after Aurangzeb.</li>
  <li>Internal revolts, fiscal strain, and regional powers.</li>
  <li>British East India Company gained control after the Battle of Plassey.</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Modern India: Freedom Movement and Independence',
        'subject': 'History',
        'level': 'Advanced',
        'content': '''
<h2>Modern India: Freedom Movement and Independence</h2>
<p>This section explores India's struggle for independence from British colonial rule.</p>

<h3>Early Resistance:</h3>
<ul>
  <li>1857 Revolt: First major uprising against British rule.</li>
  <li>Formation of Congress: Indian National Congress founded in 1885.</li>
</ul>

<h3>Major Movements:</h3>
<ul>
  <li>Non-Cooperation Movement (1920)</li>
  <li>Civil Disobedience Movement (1930)</li>
  <li>Quit India Movement (1942)</li>
</ul>

<h3>Key Leaders:</h3>
<ul>
  <li>Mahatma Gandhi: Leader of non-violence and civil disobedience.</li>
  <li>Jawaharlal Nehru: First Prime Minister of India.</li>
  <li>Sardar Patel: Architect of political integration.</li>
</ul>

<h3>Independence:</h3>
<p>India gained independence on August 15, 1947, after a long freedom struggle and national negotiations.</p>
        ''',
        'xp_reward': 30
    },
    {
        'title': 'Indian Monsoon and Climate Zones',
        'subject': 'Geography',
        'level': 'Intermediate',
        'content': '''
<h2>Indian Monsoon and Climate Zones</h2>
<p>India's climate is dominated by the monsoon system and its varied physical regions.</p>

<h3>Monsoon Mechanism:</h3>
<ul>
  <li>Southwest monsoon arrives in June and brings heavy rains.</li>
  <li>Northeast monsoon affects southeast India between October and December.</li>
  <li>Factors: differential heating, pressure gradients, and the Himalayas.</li>
</ul>

<h3>Climate Zones:</h3>
<ul>
  <li>Tropical wet: heavy rainfall along the western coast.</li>
  <li>Tropical dry: central India including the Deccan plateau.</li>
  <li>Subtropical humid: northern plains, with hot summers and cool winters.</li>
  <li>Mountain climate: Himalayan region with cold temperatures and snowfall.</li>
</ul>

<h3>Importance:</h3>
<p>The monsoon supports agriculture, water resources, and rural livelihoods in India.</p>
        ''',
        'xp_reward': 22
    },
    {
        'title': 'Economic Geography: Resources and Agriculture',
        'subject': 'Geography',
        'level': 'Advanced',
        'content': '''
<h2>Economic Geography: Natural Resources and Agriculture</h2>
<p>India's economy depends on its land, minerals, water, and climatic diversity.</p>

<h3>Natural Resources:</h3>
<ul>
  <li>Minerals: coal, iron ore, bauxite, copper.</li>
  <li>Energy: hydroelectric potential, thermal power zones.</li>
  <li>Forests: timber, biodiversity, and ecological balance.</li>
</ul>

<h3>Agricultural Zones:</h3>
<ul>
  <li>Rice-wheat zone: Northern plains and eastern India.</li>
  <li>Pulses and oilseeds: central India.</li>
  <li>Plantation crops: tea, coffee, rubber in the south and northeast.</li>
</ul>

<h3>Development Challenges:</h3>
<ul>
  <li>Inequality in land distribution.</li>
  <li>Water scarcity and irrigation stress.</li>
  <li>Urbanization pressures on agricultural land.</li>
</ul>
        ''',
        'xp_reward': 28
    },
    {
        'title': 'India Economy, Schemes & Policy Updates',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '''
<h2>India Economy, Schemes and Policy Updates</h2>
<p>This material surveys recent economic data, government schemes, and key policy updates.</p>

<h3>Economic Highlights:</h3>
<ul>
  <li>GDP growth trends, inflation, and fiscal policy.</li>
  <li>Focus on digital payments, manufacturing, and services.</li>
  <li>Priority sectors: agriculture, MSMEs, renewable energy.</li>
</ul>

<h3>Important Government Schemes:</h3>
<ul>
  <li><strong>PM-KISAN:</strong> Income support for farmers.</li>
  <li><strong>Ayushman Bharat:</strong> Health insurance for vulnerable families.</li>
  <li><strong>Digital India:</strong> Digital infrastructure and e-governance.</li>
</ul>

<h3>Policy Focus:</h3>
<ul>
  <li>Green energy transition and climate action.</li>
  <li>Public sector reforms and privatization.</li>
  <li>Education, skilling, and youth employment.</li>
</ul>
        ''',
        'xp_reward': 24
    },
    {
        'title': 'International Relations and Global Events 2024',
        'subject': 'Current Affairs',
        'level': 'Advanced',
        'content': '''
<h2>International Relations and Global Events 2024</h2>
<p>Understanding the latest global trends is essential for current affairs preparation.</p>

<h3>Key Diplomatic Themes:</h3>
<ul>
  <li>Geopolitical rivalries between major powers.</li>
  <li>Trade agreements and strategic partnerships.</li>
  <li>Climate diplomacy and global summits.</li>
</ul>

<h3>Important Developments:</h3>
<ul>
  <li>India's growing role in the Quad and Indo-Pacific.</li>
  <li>Russia-Ukraine conflict and its global economic effects.</li>
  <li>Climate summit commitments from major economies.</li>
</ul>

<h3>Exam Relevance:</h3>
<p>Connect international events to India's foreign policy, security strategy, and economic interests.</p>
        ''',
        'xp_reward': 26
    },
    {
        'title': 'Percentage, Profit-Loss and Discount',
        'subject': 'Quantitative Aptitude',
        'level': 'Beginner',
        'content': '''
<h2>Percentage, Profit-Loss and Discount</h2>
<p>Mastery of these basics is crucial for arithmetic problems in competitive exams.</p>

<h3>Percentage Basics:</h3>
<p>Percentage = (Part / Whole) × 100</p>

<h3>Profit and Loss:</h3>
<ul>
  <li>Profit = Selling Price - Cost Price</li>
  <li>Loss = Cost Price - Selling Price</li>
  <li>Profit % = (Profit / Cost Price) × 100</li>
  <li>Loss % = (Loss / Cost Price) × 100</li>
</ul>

<h3>Discount:</h3>
<ul>
  <li>Discount = Marked Price - Selling Price</li>
  <li>Discount % = (Discount / Marked Price) × 100</li>
</ul>

<h3>Example:</h3>
<p>If an item is marked at ₹500 and sold for ₹400, discount = ₹100, discount % = 20%.</p>
        ''',
        'xp_reward': 20
    },
    {
        'title': 'Time, Work and Speed-Distance',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '''
<h2>Time, Work and Speed-Distance</h2>
<p>These topics test your ability to reason through rates, efficiency, and motion.</p>

<h3>Time and Work:</h3>
<ul>
  <li>Work = Rate × Time</li>
  <li>If A can do a job in 10 days, A’s rate = 1/10 job per day.</li>
  <li>Combined work: Add individual rates.</li>
</ul>

<h3>Speed, Distance and Time:</h3>
<ul>
  <li>Speed = Distance / Time</li>
  <li>Time = Distance / Speed</li>
  <li>Distance = Speed × Time</li>
</ul>

<h3>Example:</h3>
<p>If a train travels 120 km in 2 hours, its speed is 60 km/h.</p>
        ''',
        'xp_reward': 22
    },
    {
        'title': 'Data Interpretation: Tables and Graphs',
        'subject': 'Quantitative Aptitude',
        'level': 'Advanced',
        'content': '''
<h2>Data Interpretation: Tables, Graphs and Caselets</h2>
<p>Data interpretation requires reading information from tables, charts, and solving related quantitative questions.</p>

<h3>Types of Data:</h3>
<ul>
  <li>Tabular data: Organized in rows and columns.</li>
  <li>Bar charts and line graphs: Compare values visually.</li>
  <li>Pie charts: Show shares of a whole.</li>
</ul>

<h3>Strategy:</h3>
<ul>
  <li>Read the question carefully first.</li>
  <li>Identify relevant data points and compute step by step.</li>
  <li>Use approximation when needed to speed up calculations.</li>
</ul>

<h3>Exam Tip:</h3>
<p>Practice interpreting data from different formats to improve accuracy and speed.</p>
        ''',
        'xp_reward': 28
    }
]

def seed_materials():
    """Add sample materials to the database"""
    try:
        with app.app_context():
            # Check if materials already exist
            existing_count = Material.query.count()
            if existing_count > 0:
                print(f"Database already contains {existing_count} materials. Skipping seed...")
                return
            
            for data in SAMPLE_MATERIALS:
                material = Material(
                    title=data['title'],
                    subject=data['subject'],
                    level=data['level'],
                    content=data['content'],
                    xp_reward=data['xp_reward']
                )
                db.session.add(material)
            
            db.session.commit()
            print(f"✅ Successfully seeded {len(SAMPLE_MATERIALS)} materials!")
            
            # Display summary
            for subject in ['Polity', 'History', 'Geography', 'Current Affairs', 'Quantitative Aptitude']:
                count = Material.query.filter_by(subject=subject).count()
                print(f"   {subject}: {count} materials")
    
    except Exception as e:
        db.session.rollback()
        print(f"❌ Error seeding materials: {str(e)}")

if __name__ == '__main__':
    seed_materials()
