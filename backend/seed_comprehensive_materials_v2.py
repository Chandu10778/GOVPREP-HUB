"""
Comprehensive Seed Script - Government Exam Study Materials (v2 - Fixed)
Total: 62 comprehensive materials covering all subjects
"""

from app import app
from models import db, Material

COMPREHENSIVE_MATERIALS = [
    # ============================================================================
    # POLITY (Political Science) - 15 Materials
    # ============================================================================
    {
        'title': 'Constitutional Framework of India',
        'subject': 'Polity',
        'level': 'Beginner',
        'content': """
<h2>Constitutional Framework</h2>
<p>The Constitution of India was adopted by the Constituent Assembly on 26 November 1949 and came into force on 26 January 1950. It is the world's longest written constitution and establishes India as a sovereign, socialist, secular, democratic republic.</p>

<h3>Key Features</h3>
<ul>
  <li><strong>Federal structure:</strong> Division of powers between the Union and the States.</li>
  <li><strong>Parliamentary system:</strong> Executive responsible to the legislature.</li>
  <li><strong>Fundamental rights:</strong> Enforceable rights guaranteed to citizens.</li>
  <li><strong>Directive principles:</strong> Guidelines for state policy to establish social and economic justice.</li>
  <li><strong>Independent judiciary:</strong> Guardian of the Constitution, empowered with judicial review.</li>
</ul>

<h3>Preamble Objectives</h3>
<ul>
  <li>Justice – social, economic, and political</li>
  <li>Liberty – of thought, expression, belief, faith, and worship</li>
  <li>Equality – of status and opportunity</li>
  <li>Fraternity – assuring dignity and unity of the nation</li>
</ul>

<h3>Sources and Inspiration</h3>
<p>The Constitution borrowed features from many sources: the parliamentary system from the UK, fundamental rights from the USA, directive principles from Ireland, the emergency provisions from Germany, and judicial review from the USA.</p>
""",
        'xp_reward': 25
    },
    {
        'title': 'Fundamental Rights and Duties',
        'subject': 'Polity',
        'level': 'Beginner',
        'content': """
<h2>Fundamental Rights and Duties</h2>
<p>Fundamental rights are guaranteed by the Constitution under Articles 12-35. They are enforceable by courts and form the core of individual liberty and equality in India.</p>

<h3>Six Categories of Fundamental Rights</h3>
<ol>
  <li><strong>Right to Equality:</strong> Equality before law, prohibition of discrimination, equality of opportunity in public employment.</li>
  <li><strong>Right to Freedom:</strong> Freedom of speech and expression, assembly, association, movement, residence, and profession.</li>
  <li><strong>Right against Exploitation:</strong> Prohibition of human trafficking, forced labour, and child labour.</li>
  <li><strong>Right to Freedom of Religion:</strong> Freedom of conscience and religious practice, protection of religious institutions.</li>
  <li><strong>Cultural and Educational Rights:</strong> Rights of minorities to conserve their culture, language, and establish educational institutions.</li>
  <li><strong>Right to Constitutional Remedies:</strong> Right to move courts for enforcement of fundamental rights.</li>
</ol>

<h3>Fundamental Duties</h3>
<p>Added by the 42nd Amendment in 1976, Article 51A lists eleven duties for citizens, including respecting the Constitution, promoting harmony, protecting national heritage, and safeguarding public property.</p>

<h3>Important Points</h3>
<ul>
  <li>Fundamental rights may be subject to reasonable restrictions in the interest of sovereignty, security, public order, decency, morality, or public health.</li>
  <li>Article 32 allows individuals to approach the Supreme Court directly for protection of their rights.</li>
  <li>Article 31C gives priority to directive principles over certain fundamental rights in case of conflict.</li>
</ul>
""",
        'xp_reward': 25
    },
    {
        'title': 'Parliament and Legislature',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': """
<h2>Parliament and Legislature</h2>
<p>The Parliament of India is the supreme legislative body and consists of the President, Lok Sabha, and Rajya Sabha.</p>

<h3>Lok Sabha</h3>
<ul>
  <li>Lower house of Parliament.</li>
  <li>Members are directly elected by the people from single-member constituencies.</li>
  <li>Maximum strength of 545 members, including representation from Union Territories.</li>
  <li>Holds more power over money bills and can dismiss the government through a no-confidence motion.</li>
</ul>

<h3>Rajya Sabha</h3>
<ul>
  <li>Upper house, also called the Council of States.</li>
  <li>Members are elected by state legislatures and nominated by the President.</li>
  <li>Maximum strength of 245 members; one-third retire every two years.</li>
  <li>Serves as a forum for representing states and reviewing legislation.</li>
</ul>

<h3>Legislative Process</h3>
<p>Ordinary bills can be introduced in either house, but money bills must originate in Lok Sabha. After passage by both houses, bills are sent to the President for assent. In case of disagreement, a joint sitting may be called.</p>
""",
        'xp_reward': 30
    },
    {
        'title': 'President and Executive',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': """
<h2>President and Executive</h2>
<p>The President of India is the constitutional head of state, while the real executive authority rests with the Council of Ministers led by the Prime Minister.</p>

<h3>President</h3>
<ul>
  <li>Elected by an Electoral College consisting of elected members of both houses of Parliament and state legislative assemblies.</li>
  <li>Serves a five-year term and may be re-elected.</li>
  <li>Holds powers to appoint the Prime Minister, judges of the Supreme Court and High Courts, governors, and other key officials.</li>
  <li>Can promulgate ordinances when Parliament is not in session (Article 123).</li>
</ul>

<h3>Executive Authority</h3>
<p>The Council of Ministers, headed by the Prime Minister, is responsible to the Lok Sabha. The President acts on the advice of the Prime Minister and the Council of Ministers in most matters.</p>

<h3>Emergency Powers</h3>
<ul>
  <li>National Emergency (Article 352)</li>
  <li>President's Rule in states (Article 356)</li>
  <li>Financial Emergency (Article 360)</li>
</ul>

<h3>Special Functions</h3>
<p>The President also has the power to grant pardons, reprieves, and suspend sentences in certain cases.</p>
""",
        'xp_reward': 30
    },
    {
        'title': 'Judiciary and Constitutional Courts',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': """
<h2>Judiciary and Constitutional Courts</h2>
<p>Indian judiciary is a three-tier system with the Supreme Court at the top, followed by High Courts and subordinate courts.</p>

<h3>Supreme Court</h3>
<ul>
  <li>Apex court of the land.</li>
  <li>Has original jurisdiction in disputes between the Centre and states.</li>
  <li>Has appellate jurisdiction over High Court decisions.</li>
  <li>Exercises judicial review to strike down laws inconsistent with the Constitution.</li>
  <li>Enforces fundamental rights through writ jurisdiction under Article 32.</li>
</ul>

<h3>High Courts and Lower Courts</h3>
<p>High Courts are the highest courts at the state level and supervise subordinate courts. District Courts and Magistrate Courts form the lower judiciary for civil and criminal cases.</p>

<h3>Judicial Independence</h3>
<p>The Constitution provides security of tenure, separation of powers, and appointment safeguards to preserve the independence of judges.</p>
""",
        'xp_reward': 35
    },
    {
        'title': 'State Government and Federalism',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': """
<h2>State Government and Federalism</h2>
<p>India follows a quasi-federal structure with a strong central government and autonomous state governments.</p>

<h3>Division of Powers</h3>
<ul>
  <li><strong>Union List:</strong> Subjects reserved for the Centre.</li>
  <li><strong>State List:</strong> Subjects reserved for states.</li>
  <li><strong>Concurrent List:</strong> Subjects where both can legislate.</li>
  <li><strong>Residuary powers:</strong> Held by the Union.</li>
</ul>

<h3>State Leadership</h3>
<ul>
  <li>Governor is the constitutional head of a state.</li>
  <li>Chief Minister is the leader of the elected state government.</li>
  <li>State legislatures may be unicameral or bicameral.</li>
</ul>

<h3>Local Governance</h3>
<p>Panchayati Raj institutions were created by the 73rd Amendment and municipal bodies by the 74th Amendment to strengthen local self-government.</p>
""",
        'xp_reward': 30
    },
    {
        'title': 'Election System and Electoral Commission',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': """
<h2>Election System and Electoral Commission</h2>
<p>The Election Commission of India is an independent constitutional body responsible for conducting free and fair elections in the country.</p>

<h3>Election Commission</h3>
<ul>
  <li>Constitutionally established by Article 324.</li>
  <li>Consists of the Chief Election Commissioner and Election Commissioners.</li>
  <li>Supervises elections to Parliament, state legislatures, and the offices of President and Vice-President.</li>
</ul>

<h3>Electoral System</h3>
<ul>
  <li>Universal adult suffrage for citizens aged 18 and above.</li>
  <li>First-Past-The-Post (FPTP) voting system for Lok Sabha and state assemblies.</li>
  <li>Model Code of Conduct regulates political parties and candidates during elections.</li>
</ul>

<h3>Key Features</h3>
<p>Election laws are governed by the Representation of the People Act, 1951, and the Election Commission uses voter rolls, secret ballots, and Electronic Voting Machines (EVMs).</p>
""",
        'xp_reward': 30
    },
    {
        'title': 'Constitutional Amendments and Doctrine',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': """
<h2>Constitutional Amendments and Doctrine</h2>
<p>Article 368 empowers Parliament to amend the Constitution. Most amendments require a special majority in both houses, and certain changes also require ratification by state legislatures.</p>

<h3>Amendment Procedure</h3>
<ul>
  <li>Simple majority for provisions concerning procedure or rules.</li>
  <li>Two-thirds majority of members present and voting in both houses for most constitutional amendments.</li>
  <li>Ratification by at least half of the state legislatures for changes affecting federal provisions.</li>
</ul>

<h3>Basic Structure Doctrine</h3>
<p>The Supreme Court ruled in Kesavananda Bharati v. State of Kerala (1973) that Parliament cannot alter the Constitution's basic structure, including the supremacy of the Constitution, secularism, democracy, federalism, and judicial review.</p>

<h3>Important Amendments</h3>
<ul>
  <li>42nd Amendment: Strengthened state power and added fundamental duties.</li>
  <li>44th Amendment: Restricted emergency powers and restored civil liberties.</li>
  <li>74th Amendment: Strengthened urban local bodies.</li>
</ul>
""",
        'xp_reward': 35
    },
    {
        'title': 'Rights, Freedoms and Social Justice',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': """
<h2>Rights, Freedoms and Social Justice</h2>
<p>The Indian Constitution seeks to create an inclusive society by protecting individual freedoms and promoting social justice.</p>

<h3>Equality and Non-Discrimination</h3>
<p>Articles 14-18 guarantee equality before law, prohibit discrimination on grounds of religion, race, caste, sex, or place of birth, and abolish untouchability.</p>

<h3>Social Justice Measures</h3>
<ul>
  <li>Reservation in education and public employment for Scheduled Castes, Scheduled Tribes, and Other Backward Classes.</li>
  <li>Protection for minorities, women, children, and disadvantaged groups.</li>
  <li>Directive principles emphasize welfare, health, education, and labour rights.</li>
</ul>

<h3>Cultural Rights</h3>
<p>Minorities have the right to conserve their language, script, and culture and to establish educational institutions of their choice.</p>

<h3>Fraternity and National Unity</h3>
<p>The Constitution promotes fraternity to maintain the dignity of the individual and the unity and integrity of the nation.</p>
""",
        'xp_reward': 35
    },
    {
        'title': 'Centre-State Relations and Intergovernmental Institutions',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': '<h2>Centre-State Relations</h2><p>Indian federalism has a strong Centre with a division of subjects in the Union, State and Concurrent Lists. Intergovernmental institutions such as the Inter-State Council, Finance Commission and National Development Council help resolve disputes and coordinate policy. Fiscal federalism works through tax devolution, grants, and planning commission recommendations.</p>',
        'xp_reward': 35
    },
    {
        'title': 'Accountability, Transparency and RTI',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '<h2>Accountability and Transparency</h2><p>The Right to Information Act 2005 empowers citizens to seek information from public authorities, promoting transparency. The Lokpal and Lokayuktas are anti-corruption bodies, while the CAG audits government expenditure and the PAC reviews those reports. Ethical governance and citizen participation strengthen democratic accountability.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Emergency Provisions and Constitutional Amendments',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': '<h2>Emergency Provisions</h2><p>Articles 352, 356, and 360 provide for National Emergency, President\'s Rule, and Financial Emergency respectively. These provisions allow temporary suspension of fundamental rights and federal structure during crises. The 42nd and 44th Amendments modified these powers to prevent misuse.</p>',
        'xp_reward': 35
    },
    {
        'title': 'Constitutional Bodies and Commissions',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '<h2>Constitutional Bodies</h2><p>The Election Commission, Union Public Service Commission, Comptroller and Auditor General, and Attorney General are constitutional bodies. They ensure free elections, merit-based recruitment, financial accountability, and legal advice to the government respectively.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Local Self-Government and Panchayati Raj',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '<h2>Local Governance</h2><p>The 73rd and 74th Constitutional Amendments established Panchayati Raj institutions and municipal bodies. These provide for elected local governments with powers over local administration, planning, and development. The Finance Commission recommends resource sharing between Centre, states, and local bodies.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Union Territories and Special Status Areas',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': '<h2>Special Areas</h2><p>Union Territories are directly administered by the Centre, with Delhi having a special status. Article 370 granted special autonomy to Jammu and Kashmir, while Article 371 provides special provisions for states like Maharashtra, Gujarat, Nagaland, Assam, Manipur, Andhra Pradesh, Sikkim, Mizoram, Arunachal Pradesh, and Goa.</p>',
        'xp_reward': 35
    },

    # ============================================================================
    # HISTORY - 15 Materials
    # ============================================================================
    {
        'title': 'Indus Valley and Vedic Civilizations',
        'subject': 'History',
        'level': 'Beginner',
        'content': '<h2>Early Indian Civilizations</h2><p>Indus Valley (2300-1750 BCE): Harappa, Mohenjo-daro, urban planning, undeciphered script, trade. Vedic Age (1500-600 BCE): Aryan migration, Four Vedas, Varna system, transition to agriculture, Upanishadic philosophy introduced.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Mauryan and Post-Mauryan Period',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>Mauryan Empire (322-185 BCE)</h2><p>Founder: Chandragupta Maurya. Greatest ruler: Ashoka - ruled after Kalinga War (260 BCE). Adopted Buddhism, Ashoka Pillars with edicts, advanced administration, capital Pataliputra. Decline after Ashoka led to fragmentation.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Medieval Period - Delhi Sultanate',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>Delhi Sultanate (1206-1526 CE)</h2><p>Five dynasties: Slave (Qutbuddin Aibak - Qutub Minar), Khilji, Tughlaq, Sayyid, Lodi. Introduced Persian culture, Indo-Islamic architecture, Arabic administration. Alauddin Khilji: military reforms. Muhammad bin Tughlaq: ambitious but unpopular. Ended by Babur\'s victory 1526.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Mughal Empire - Rise and Peak',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>Mughal Era (1526-1857)</h2><p>Founder: Babur (defeated Ibrahim Lodi, 1526). Greatest: Akbar - religious tolerance, administrative genius, Mughal art peak. Jahangir: cultural patron. Shah Jahan: Taj Mahal (1632-1653). Built Indo-Islamic architecture, introduced Persian culture, centralized administration.</p>',
        'xp_reward': 35
    },
    {
        'title': 'British Raj and Colonial Administration',
        'subject': 'History',
        'level': 'Advanced',
        'content': '<h2>British Rule (1858-1947)</h2><p>Company rule ended after 1857 Rebellion, Crown took control. Victoria declared Empress (1876). Viceroy as supreme authority, ICS (Indian Civil Service) established. Economic exploitation: raw materials exported, finished goods imported. Infrastructure built to extract resources and maintain control.</p>',
        'xp_reward': 35
    },
    {
        'title': 'Independence Movement - Moderate Phase',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>Early Nationalist Movement (1857-1920)</h2><p>1857 Rebellion led by Mangal Pandey, Rani Laxmibai. Indian National Congress founded 1885 (A.O. Hume). Moderate phase: Dadabhai Naoroji (drain of wealth), Gopal Krishna Gokhale. Bengal Partition (1905) sparked Swadeshi movement. Radical phase: Tilak, Lala Lajpat Rai demanded Swaraj.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Gandhian Independence Struggle',
        'subject': 'History',
        'level': 'Advanced',
        'content': '<h2>Non-Violent Movement (1920-1947)</h2><p>Gandhi\'s Satyagraha (truth-force), Ahimsa (non-violence). Key movements: Khilafat (1920-24), Non-Cooperation (1920-22), Civil Disobedience (1930 Salt March), Quit India (1942). Jallianwala Bagh Massacre (1919) unified resistance. Independence via Mountbatten Plan, Partition (1947), 1-2 million deaths.</p>',
        'xp_reward': 35
    },
    {
        'title': 'Republic and Constitution Framing',
        'subject': 'History',
        'level': 'Advanced',
        'content': '<h2>Framing Constitution (1946-1950)</h2><p>Constituent Assembly headed by Dr. Rajendra Prasad. Dr. B.R. Ambedkar, Vallabhbhai Patel, Jawaharlal Nehru, Sardar Vallabhbhai Patel key figures. Constitution drafted to create secular, democratic, socialist republic. Adopted 26 January 1950. Universal adult suffrage unprecedented for that time.</p>',
        'xp_reward': 35
    },
    {
        'title': 'South Indian Kingdoms and Regional Empires',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>South Indian Kingdoms</h2><p>The Cholas, Cheras, and Pandyas dominated southern India, known for maritime trade, temple architecture, and advanced administration. The Vijayanagara Empire protected the south from northern invasions and promoted Telugu and Kannada culture. The Deccan Sultanates and Nayaka kingdoms shaped regional politics and heritage.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Revolutionary Movement and Nationalist Leaders',
        'subject': 'History',
        'level': 'Advanced',
        'content': '<h2>Revolutionary Movement</h2><p>Revolutionaries like Bhagat Singh, Chandrashekhar Azad, Subhas Chandra Bose, and the Ghadar Party used armed struggle alongside non-violent resistance. Important events include the Kakori Train Robbery, Chauri Chaura incident, and formation of the Indian National Army. Their sacrifices energized the freedom struggle.</p>',
        'xp_reward': 35
    },
    {
        'title': 'Partition, Nation-Building and Post-Independence India',
        'subject': 'History',
        'level': 'Advanced',
        'content': '<h2>Partition and Post-Independence Era</h2><p>The Partition of India in 1947 led to large-scale migration, communal violence, and the creation of India and Pakistan. Post-independence nation-building focused on integration of princely states, economic planning, land reforms, non-alignment policy, linguistic reorganization of states, and the development of democratic institutions.</p>',
        'xp_reward': 35
    },
    {
        'title': 'Ancient Indian Kingdoms and Empires',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>Ancient Indian Kingdoms</h2><p>The Mauryan Empire (321-185 BCE) under Ashoka spread Buddhism across Asia. The Gupta Golden Age (320-550 CE) excelled in mathematics, astronomy, and Sanskrit literature. The Kushan Empire facilitated Silk Road trade. Ancient India pioneered decimal system, zero concept, and medical science (Charaka, Sushruta).</p>',
        'xp_reward': 30
    },
    {
        'title': 'Medieval Kingdoms and Islamic Invasions',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>Medieval Period</h2><p>Delhi Sultanate (1206-1526) established by Qutb-ud-din Aibak. Mughal Empire (1526-1857) under Akbar, Jahangir, Shah Jahan, Aurangzeb. Rajput kingdoms resisted invasions. Vijayanagara Empire in south. Bhakti movement (Kabir, Tulsidas) and Sikhism emerged. Cultural synthesis of Hindu-Muslim traditions.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Colonial Reforms and Administrative Changes',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '<h2>Colonial Administration</h2><p>British East India Company rule (1757-1858), Crown rule (1858-1947). Administrative reforms: Cornwallis Code (1793), Charter Acts (1813, 1833, 1853). Economic policies: Permanent Settlement (1793), Ryotwari, Mahalwari systems. Social reforms: Abolition of Sati (1829), Widow Remarriage Act (1856), education policies.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Later Freedom Struggle and Mass Movements',
        'subject': 'History',
        'level': 'Advanced',
        'content': '<h2>Later Freedom Struggle</h2><p>Post-1857: Formation of INC (1885), Home Rule League (1916). Montagu-Chelmsford Reforms (1919), Government of India Act (1935). All India Muslim League (1906), Two-Nation Theory. Cripps Mission (1942), Cabinet Mission (1946). Wavell Plan, Mountbatten Plan leading to independence and partition.</p>',
        'xp_reward': 35
    },

    # ============================================================================
    # GEOGRAPHY - 10 Materials
    # ============================================================================
    {
        'title': 'Landforms, Rivers and Water Resources',
        'subject': 'Geography',
        'level': 'Beginner',
        'content': '<h2>Landforms and Rivers</h2><p>Himalayan mountains, Western/Eastern Ghats, Indo-Gangetic Plain, Deccan Plateau. Major rivers: Ganga (2506 km, holy), Brahmaputra (2900 km), Indus (3180 km), Godavari, Krishna, Narmada, Cauvery. Rivers crucial for irrigation, hydropower, transport. Inter-state disputes (Cauvery, Krishna).</p>',
        'xp_reward': 25
    },
    {
        'title': 'Indian Climate and Monsoons',
        'subject': 'Geography',
        'level': 'Intermediate',
        'content': '<h2>Monsoon System</h2><p>Southwest Monsoon (June-Sept) brings 80% rainfall. Caused by pressure differences. Northeast Monsoon (Oct-Dec) for southern regions. Tropical monsoon climate with regional variations. High rainfall Western Ghats >250cm, dry Rajasthan <50cm. Monsoon failure causes drought, excess causes floods.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Natural Resources and Minerals',
        'subject': 'Geography',
        'level': 'Advanced',
        'content': '<h2>Mineral and Energy Resources</h2><p>Iron Ore: Jharkhand 40%, Odisha 30%. Coal: 70% electricity generation, 4th largest reserves globally. Bauxite, Manganese, Mica (80% world production). Oil and gas limited. Nuclear power: 22 plants. Renewable energy: Solar, wind growing. Strategic minerals essential for industrialization.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Human Geography and Regions',
        'subject': 'Geography',
        'level': 'Advanced',
        'content': '<h2>Regional Geography</h2><p>Northern Plains: Indo-Gangetic, agricultural hub, 50% population. Southern Plateau: Deccan, black soil. Coastal regions: Trade, fishing. Northeast: High rainfall, diverse culture. Western coast: Mountains, ports. Eastern coast: Deltaic rivers. Urban-rural divide, migration patterns, population density variations affect development.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Indian Soils, Vegetation and Agriculture',
        'subject': 'Geography',
        'level': 'Intermediate',
        'content': '<h2>Soils and Agriculture</h2><p>India has diverse soils including alluvial, black, red, laterite, desert, and forest soils. Soil type influences cropping patterns: rice in alluvial plains, cotton on black soil, tea in laterite regions. Agricultural practices include multiple cropping, irrigation canals, wells, and modern Green Revolution techniques.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Environment, Biodiversity and Conservation',
        'subject': 'Geography',
        'level': 'Advanced',
        'content': '<h2>Environment and Biodiversity</h2><p>India is a megadiverse country with Himalayan, Western Ghats, Indo-Gangetic, and desert ecosystems. Protected areas include national parks, wildlife sanctuaries, and biosphere reserves. Key conservation laws are the Wildlife Protection Act, Forest Conservation Act, and Biodiversity Act.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Population Geography and Demographics',
        'subject': 'Geography',
        'level': 'Intermediate',
        'content': '<h2>Population Geography</h2><p>India\'s population: 1.4 billion (17% world total), 2nd largest country. Density: 464/sq km, highest in Kerala (859), lowest in Arunachal Pradesh (17). Age structure: 65% working age, demographic dividend. Urbanization: 34% urban, growing megacities (Delhi, Mumbai, Kolkata, Chennai). Migration patterns: Rural-urban, interstate.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Agriculture Systems and Food Security',
        'subject': 'Geography',
        'level': 'Advanced',
        'content': '<h2>Agriculture Systems</h2><p>India\'s agriculture: 16% GDP, 50% employment. Major crops: Rice (Punjab, West Bengal), Wheat (UP, Punjab), Cotton (Maharashtra, Gujarat), Sugarcane (UP, Maharashtra). Irrigation: Canals, wells, tube wells. Green Revolution increased yields. Food security: PDS, MSP, buffer stocks. Challenges: Climate change, water scarcity, soil degradation.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Transport Networks and Infrastructure',
        'subject': 'Geography',
        'level': 'Intermediate',
        'content': '<h2>Transport Networks</h2><p>Roads: 6.1 million km, Golden Quadrilateral connects metros. Railways: 68,000 km, 4th largest network. Ports: 13 major ports, 200 minor ports. Airports: 125 airports, international hubs (Delhi, Mumbai). Inland waterways: Ganga, Brahmaputra. Transport connectivity crucial for economic development and regional integration.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Disaster Management and Climate Change',
        'subject': 'Geography',
        'level': 'Advanced',
        'content': '<h2>Disaster Management</h2><p>India prone to earthquakes (Himalayan belt), cyclones (Bay of Bengal), floods (monsoon), droughts (arid regions). National Disaster Management Authority (NDMA) coordinates response. Climate change: Rising temperatures, melting glaciers, sea-level rise. Mitigation: Renewable energy, afforestation, sustainable development. Paris Agreement commitments.</p>',
        'xp_reward': 30
    },

    # ============================================================================
    # CURRENT AFFAIRS - 10 Materials
    # ============================================================================
    {
        'title': '2024 Government and Political Updates',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '<h2>Current Government 2024</h2><p>President: Droupadi Murmu (25th). Vice President: Jagdeep Dhankhar. PM: Narendra Modi. CJI: D Y Chandrachud. Focus: Digital India, Make in India, Atmanirbhar Bharat (self-reliance), Infrastructure development, Employment, Climate commitments, Economic growth targeting 7%+.</p>',
        'xp_reward': 25
    },
    {
        'title': 'International Relations and Diplomacy',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '<h2>India\'s Foreign Policy</h2><p>Strategic Autonomy principle - not aligned with any bloc. Key partnerships: QUAD (USA, Japan, Australia counter to China), BRICS (Russia, China, Brazil, South Africa - multipolar world). China border issues (LAC disputes Ladakh). Russia: defense/energy cooperation. Gulf: oil trade, diaspora. ASEAN: regional stability.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Economic Policies and Development',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '<h2>Economic Updates</h2><p>India 5th largest economy, IT services strong, manufacturing growth, agriculture baseline. GST (2017) unified taxation. RBI targets inflation control (4% target). Pradhan Mantri Jan Dhan Yojana for financial inclusion. FDI attraction. Export promotion. Stock market SENSEX performance. Employment generation challenges.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Social and Environmental Policies',
        'subject': 'Current Affairs',
        'level': 'Advanced',
        'content': '<h2>Development and Sustainability</h2><p>SDG alignment, climate commitments (Net Zero 2070), renewable energy targets, Ganga Cleanup Mission (water pollution), pollution control, plastic ban, women empowerment programs, education initiatives (NEP 2020), healthcare (Ayushman Bharat), poverty reduction schemes.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Science, Technology and Innovation',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '<h2>Science and Technology</h2><p>Recent advances include space missions like Chandrayaan, digital public infrastructure such as Aadhaar and UPI, and innovation in AI, biotechnology, and clean energy. Government initiatives including Atal Innovation Mission and Startup India support entrepreneurship and research.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Sports, Culture and Society',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '<h2>Sports and Culture</h2><p>India is promoting sports through Khelo India and hosting major events. Cultural diplomacy includes festivals, cinema, and arts. Social trends include youth employment, digital inclusion, gender equality programs, and challenges from rapid urbanization.</p>',
        'xp_reward': 25
    },
    {
        'title': 'International Organizations and Diplomacy',
        'subject': 'Current Affairs',
        'level': 'Advanced',
        'content': '<h2>International Relations</h2><p>India\'s role in UN, G20, BRICS, SCO, QUAD. Recent summits and agreements. Border disputes resolution, neighborhood policy (Act East, Look West). Climate diplomacy, trade agreements (RCEP, FTA negotiations). India\'s permanent seat bid in UNSC, NSG membership. Multilateral engagements and soft power projection.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Defense Policies and Security Issues',
        'subject': 'Current Affairs',
        'level': 'Advanced',
        'content': '<h2>Defense and Security</h2><p>Make in India for defense, Atmanirbhar Bharat initiatives. Border infrastructure development, military modernization. Cybersecurity threats, internal security challenges. Recent military exercises, defense acquisitions. Nuclear doctrine, missile programs. Coast Guard expansion, maritime security in Indian Ocean Region.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Economic Reforms and Fiscal Policies',
        'subject': 'Current Affairs',
        'level': 'Advanced',
        'content': '<h2>Economic Policies</h2><p>Recent reforms: GST 2.0, Direct Tax Code, labor codes. Fiscal consolidation, inflation targeting. RBI monetary policy, interest rate decisions. Budget 2024 highlights, infrastructure spending. Digital economy initiatives, fintech growth. Employment generation schemes, skill development programs. Economic recovery post-pandemic.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Social Programs and Welfare Schemes',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '<h2>Social Welfare</h2><p>PM Awas Yojana (housing for all), Swachh Bharat Mission (sanitation), Jal Jeevan Mission (water). Education: Mid-day meal, Beti Bachao Beti Padhao. Health: Ayushman Bharat, COVID vaccination drive. Employment: MGNREGA, PM Kisan. Women empowerment: Ujjwala Yojana, Sukanya Samriddhi. Tribal development, minority welfare programs.</p>',
        'xp_reward': 25
    },

    # ============================================================================
    # QUANTITATIVE APTITUDE - 12 Materials
    # ============================================================================
    {
        'title': 'Number System and Basic Arithmetic',
        'subject': 'Quantitative Aptitude',
        'level': 'Beginner',
        'content': '<h2>Number System Basics</h2><p>Natural, Whole, Integer, Rational, Irrational, Real numbers. Divisibility rules (2:even, 3:sum of digits, 5:0/5, 11:alternating sum). Prime (2,3,5,7...), Composite, LCM, GCD/HCF. Percentages, decimals, fractions conversion. Basic arithmetic operations with integers and decimals.</p>',
        'xp_reward': 20
    },
    {
        'title': 'Profit, Loss and Interest',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '<h2>Commercial Math</h2><p>Profit = SP - CP, Profit% = (Profit/CP)×100. Simple Interest SI = (P×R×T)/100. Compound Interest A = P(1+R/100)^T. Percentages: increase/decrease formulas. Discounts on marked price. Multiple profit/loss scenarios. Real-world banking and business calculations.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Ratio, Proportion and Partnership',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '<h2>Ratios and Proportions</h2><p>Ratio = comparison of quantities. Equivalent ratios (2:3 = 4:6). Compound ratio, duplicate ratio, inverse ratio. Proportion a:b = c:d, cross multiplication. Direct (x∝y) and inverse (x∝1/y) proportions. Partnership profit sharing based on capital×time invested.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Time, Speed and Distance',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '<h2>Motion Problems</h2><p>Speed = Distance÷Time. Unit conversion km/h to m/s (×5/18). Relative speed (same direction: |S1-S2|, opposite: S1+S2). Trains crossing problems. Boat and stream (upstream = boat-stream, downstream = boat+stream). Average speed = total distance ÷ total time, not arithmetic mean of speeds.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Geometry and Mensuration',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '<h2>Shapes and Measures</h2><p>2D: Triangle (½×base×height), Square (side²), Rectangle (l×w), Circle (πr²), Perimeter formulas. 3D: Cube (side³), Cuboid (l×w×h), Cylinder (πr²h), Sphere (4/3πr³), Volume and surface area calculations. Applications in real-world problems.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Time, Work and Pipes',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '<h2>Work and Time</h2><p>Work problems involve efficiency, time, and workforce. If A can do a job in x days and B in y days, together they finish in xy/(x+y) days. Pipes and cisterns problems use filling and emptying rates, with net rate equal to sum of individual rates.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Algebra, Equations and Progressions',
        'subject': 'Quantitative Aptitude',
        'level': 'Advanced',
        'content': '<h2>Algebra and Sequences</h2><p>Linear equations, simultaneous equations, quadratic equations, and arithmetic and geometric progressions are essential. Sum of first n natural numbers and formulas for series help solve work, age, mixture, and investment problems.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Permutations, Combinations and Probability',
        'subject': 'Quantitative Aptitude',
        'level': 'Advanced',
        'content': '<h2>Combinatorics and Probability</h2><p>Permutations cover arrangements, combinations cover selections. Probability is the ratio of favourable outcomes to total possible outcomes. Useful for exam questions on selection, order, and chance. Basic formulas include nPr, nCr, and probability of independent and mutually exclusive events.</p>',
        'xp_reward': 30
    },    {
        'title': 'Data Sufficiency and Logical Reasoning',
        'subject': 'Quantitative Aptitude',
        'level': 'Advanced',
        'content': '<h2>Data Sufficiency</h2><p>Questions provide statements and ask if they contain enough information to answer. Common in banking exams. Learn to identify when data is sufficient, insufficient, or contradictory. Practice determining what additional information is needed to solve problems involving ratios, percentages, averages, and geometry.</p>',
        'xp_reward': 30
    },
    {
        'title': 'Time and Work Variations',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '<h2>Time and Work Problems</h2><p>Advanced concepts: Pipes and cisterns, work efficiency variations, leave and join scenarios. Formula: Work = Rate × Time. For multiple workers: 1/Work = 1/A + 1/B + 1/C. Practice problems involving overtime, different efficiency rates, and complex scenarios where workers join or leave during the task.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Mixtures and Alligations',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '<h2>Mixtures and Alligations</h2><p>Alligation rule for mixing solutions of different concentrations. Formula: (Quantity of cheaper)/(Quantity of dearer) = (Price of dearer - Mean price)/(Mean price - Price of cheaper). Applications in profit-loss, mixtures of milk-water, alloys, and chemical solutions. Useful for problems involving repeated replacements and final concentrations.</p>',
        'xp_reward': 25
    },
    {
        'title': 'Coordinate Geometry and Mensuration',
        'subject': 'Quantitative Aptitude',
        'level': 'Advanced',
        'content': '<h2>Coordinate Geometry</h2><p>Distance formula: sqrt((x₂-x₁)² + (y₂-y₁)²). Section formula divides line in ratio m:n. Area of triangle: (1/2)|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|. Circle equations, tangents, chords. Combined with mensuration for complex 2D/3D geometry problems involving coordinates and measurements.</p>',
        'xp_reward': 30
    },]

def seed_comprehensive_materials():
    """Seed the database with comprehensive study materials"""
    with app.app_context():
        try:
            # Clear old data
            from models import MaterialProgress
            MaterialProgress.query.delete()
            Material.query.delete()
            db.session.commit()
            print("Cleared old materials and progress data")

            # Add new materials
            for data in COMPREHENSIVE_MATERIALS:
                material = Material(
                    title=data['title'],
                    subject=data['subject'],
                    level=data['level'],
                    content=data['content'],
                    xp_reward=data['xp_reward']
                )
                db.session.add(material)

            db.session.commit()
            print(f"Successfully seeded {len(COMPREHENSIVE_MATERIALS)} comprehensive materials!")
            print(f"📊 Breakdown by subject:")

            for subject in sorted(set([m['subject'] for m in COMPREHENSIVE_MATERIALS])):
                materials = [m for m in COMPREHENSIVE_MATERIALS if m['subject'] == subject]
                count = len(materials)
                total_xp = sum([m['xp_reward'] for m in materials])
                print(f"   {subject}: {count} materials | {total_xp} XP")

            total_xp = sum([m['xp_reward'] for m in COMPREHENSIVE_MATERIALS])
            print(f"Total XP Available: {total_xp} XP")

        except Exception as e:
            db.session.rollback()
            print(f"Error: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    seed_comprehensive_materials()
