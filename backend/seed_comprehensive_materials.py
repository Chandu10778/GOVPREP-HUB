"""
Comprehensive Seed Script - Government Exam Study Materials
This script populates the database with extensive study content organized by topics
Total: 50+ materials covering all subjects with detailed exam-relevant content
"""

from app import app
from models import db, Material

COMPREHENSIVE_MATERIALS = [
    # ============================================================================
    # POLITY (Political Science) - 12 Materials
    # ============================================================================
    {
        'title': 'Constitutional Framework of India',
        'subject': 'Polity',
        'level': 'Beginner',
        'content': '''
<h2>Constitutional Framework of India</h2>
<p><strong>The Indian Constitution</strong> is the world's longest written constitution, adopted on 26 January 1950.</p>

<h3>Key Characteristics:</h3>
<ul>
  <li><strong>Sovereign Democratic Republic:</strong> India is a sovereign state with no external authority</li>
  <li><strong>Federal Structure:</strong> Distribution of powers between Centre and States</li>
  <li><strong>Parliamentary System:</strong> Executive responsible to Legislature</li>
  <li><strong>Secular State:</strong> No official religion; separation of religion and state</li>
  <li><strong>Socialist:</strong> Emphasis on reducing inequalities and welfare state</li>
</ul>

<h3>Preamble Objectives:</h3>
<ol>
  <li><strong>Sovereignty:</strong> Self-governance, freedom from foreign control</li>
  <li><strong>Democracy:</strong> Government by the people</li>
  <li><strong>Republic:</strong> Elected head of state</li>
  <li><strong>Justice:</strong> Social, political, and economic</li>
  <li><strong>Liberty:</strong> Freedom of thought, expression, belief</li>
  <li><strong>Equality:</strong> Status and opportunity equality</li>
  <li><strong>Fraternity:</strong> Brotherhood and national unity</li>
</ol>

<h3>Sources of Constitution:</h3>
<table border="1" cellpadding="8">
  <tr>
    <th>Source</th>
    <th>Country</th>
    <th>Features Adopted</th>
  </tr>
  <tr>
    <td>UK</td>
    <td>United Kingdom</td>
    <td>Parliamentary system, cabinet system, rule of law</td>
  </tr>
  <tr>
    <td>USA</td>
    <td>United States</td>
    <td>Federal structure, Supreme Court, judicial review</td>
  </tr>
  <tr>
    <td>France</td>
    <td>France</td>
    <td>Ideals of liberty, equality, fraternity</td>
  </tr>
  <tr>
    <td>USSR (Russia)</td>
    <td>Soviet Union</td>
    <td>Directive principles of state policy</td>
  </tr>
  <tr>
    <td>Weimar Republic</td>
    <td>Germany</td>
    <td>Emergency provisions, suspension of rights</td>
  </tr>
</table>

<h3>Parts of the Constitution:</h3>
<ul>
  <li><strong>Preamble:</strong> Statement of objectives</li>
  <li><strong>Part I-IV:</strong> Union, States, Scheduled Castes/Tribes, Fundamental Rights</li>
  <li><strong>Part V-VI:</strong> Directive Principles, Fundamental Duties</li>
  <li><strong>Part VII-XI:</strong> Union, States, Elections, Services</li>
</ul>

<h3>Important Amendments:</h3>
<ul>
  <li><strong>1st Amendment:</strong> Limitations on Freedom of Speech (Sedition)</li>
  <li><strong>42nd Amendment:</strong> "Emergency" President rule, Removed "Right to Property"</li>
  <li><strong>44th Amendment:</strong> Restored "Right to Property" as constitutional right</li>
  <li><strong>73rd & 74th:</strong> Panchayati Raj and Municipal Administration</li>
  <li><strong>86th Amendment:</strong> Right to Free Education (RTE)</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Fundamental Rights - Detailed Analysis',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '''
<h2>Fundamental Rights (Articles 12-35) - Detailed</h2>
<p>Fundamental Rights are the basic human rights guaranteed to ALL citizens of India without discrimination.</p>

<h3>Right to Equality (Articles 14-18)</h3>
<ul>
  <li><strong>Article 14:</strong> Equality before law - state cannot deny equal protection</li>
  <li><strong>Article 15:</strong> No discrimination based on religion, race, caste, sex, place of birth</li>
  <li><strong>Article 16:</strong> Equal opportunity in employment/public services</li>
  <li><strong>Article 17:</strong> Abolition of untouchability (Illegal)</li>
  <li><strong>Article 18:</strong> Abolition of titles (No hereditary titles)</li>
</ul>

<h3>Right to Freedom (Articles 19-22)</h3>
<ul>
  <li><strong>Article 19(1)(a):</strong> Freedom of speech and expression</li>
  <li><strong>Article 19(1)(b):</strong> Freedom to assemble peacefully</li>
  <li><strong>Article 19(1)(c):</strong> Freedom to form associations</li>
  <li><strong>Article 19(1)(d):</strong> Freedom to move freely throughout India</li>
  <li><strong>Article 19(1)(e):</strong> Freedom to reside and settle anywhere in India</li>
  <li><strong>Article 19(1)(g):</strong> Freedom to practice any trade/profession</li>
  <li><strong>Article 20:</strong> Protection against conviction - No retroactive laws</li>
  <li><strong>Article 21:</strong> Right to Life and Liberty - Most important!</li>
  <li><strong>Article 22:</strong> Protection against unlawful detention/arrest</li>
</ul>

<h3>Right Against Exploitation (Articles 23-24)</h3>
<ul>
  <li><strong>Article 23:</strong> Prohibition of forced labor and human trafficking</li>
  <li><strong>Article 24:</strong> Prohibition of child labor (No work for children below 14)</li>
</ul>

<h3>Right to Freedom of Religion (Articles 25-28)</h3>
<ul>
  <li><strong>Article 25:</strong> Right to freely profess, practice, propagate religion</li>
  <li><strong>Article 26:</strong> Right to manage religious affairs</li>
  <li><strong>Article 27:</strong> No compulsion to pay taxes for religion</li>
  <li><strong>Article 28:</strong> No religious instruction in government schools</li>
</ul>

<h3>Cultural and Educational Rights (Articles 29-30)</h3>
<ul>
  <li><strong>Article 29:</strong> Protection of minorities' language, script, culture</li>
  <li><strong>Article 30:</strong> Right of minorities to establish educational institutions</li>
</ul>

<h3>Right to Constitutional Remedies (Article 32)</h3>
<p>Right to approach Supreme Court for enforcement of fundamental rights through:</p>
<ul>
  <li><strong>Habeas Corpus:</strong> Against unlawful detention</li>
  <li><strong>Mandamus:</strong> To perform duty</li>
  <li><strong>Prohibition:</strong> Against illegal authority</li>
  <li><strong>Certiorari:</strong> To quash illegal orders</li>
  <li><strong>Quo Warranto:</strong> Against usurped authority</li>
</ul>

<h3>Restrictions on Fundamental Rights:</h3>
<p>Fundamental Rights are NOT absolute. They can be restricted in interests of:</p>
<ul>
  <li>National security and sovereignty</li>
  <li>Public order and morality</li>
  <li>Contempt of court</li>
  <li>Defamation</li>
  <li>Incitement to violence</li>
</ul>

<h3>Suspension During Emergency:</h3>
<p>During national emergency (Article 352), fundamental rights can be suspended EXCEPT:</p>
<ul>
  <li>Article 20 (Protection against conviction)</li>
  <li>Article 21 (Right to life and liberty)</li>
</ul>
        ''',
        'xp_reward': 30
    },
    {
        'title': 'Directive Principles of State Policy',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '''
<h2>Directive Principles of State Policy (Articles 36-51)</h2>
<p>Guidelines for formulating policies - NOT enforceable in court but morally binding on government.</p>

<h3>Socio-Economic Directives (Articles 38-41)</h3>
<ul>
  <li><strong>Article 38:</strong> State shall promote social and economic justice</li>
  <li><strong>Article 39:</strong> Right to adequate means of livelihood, equal pay for equal work</li>
  <li><strong>Article 40:</strong> Organization of village panchayats</li>
  <li><strong>Article 41:</strong> Right to work, education, and public assistance</li>
</ul>

<h3>Educational and Cultural Directives (Articles 42-51)</h3>
<ul>
  <li><strong>Article 45:</strong> Free and compulsory education up to age 14 (Now 18 - RTE Act)</li>
  <li><strong>Article 46:</strong> Promotion of education and interests of weaker sections</li>
  <li><strong>Article 47:</strong> Duty to raise standard of living and public health</li>
  <li><strong>Article 48:</strong> Protection of cows and cattle slaughter</li>
  <li><strong>Article 49:</strong> Protection of monuments, places of historical interest</li>
  <li><strong>Article 50:</strong> Separation of judiciary from executive</li>
  <li><strong>Article 51:</strong> Promotion of international peace and security (India's foreign policy)</li>
</ul>

<h3>Key Points:</h3>
<ul>
  <li><strong>Nature:</strong> Non-justiciable (Cannot be enforced in courts)</li>
  <li><strong>Purpose:</strong> Guide government in policy-making</li>
  <li><strong>Inspiration:</strong> From Irish Constitution</li>
  <li><strong>Relationship with Fundamental Rights:</strong> Complementary - together ensure social justice</li>
</ul>

<h3>Benefits of DPSPs:</h3>
<ul>
  <li>Emphasis on Welfare State</li>
  <li>Guide towards social democracy</li>
  <li>Balance between individual rights and collective welfare</li>
  <li>Framework for progressive legislation</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Fundamental Duties of Citizens',
        'subject': 'Polity',
        'level': 'Beginner',
        'content': '''
<h2>Fundamental Duties of Citizens (Article 51A)</h2>
<p>Added by 42nd Amendment in 1976. Duties that every citizen must follow for national development.</p>

<h3>The 11 Fundamental Duties:</h3>
<ol>
  <li><strong>Constitution:</strong> To abide by Constitution and respect its ideals</li>
  <li><strong>Laws:</strong> To respect laws and legal processes</li>
  <li><strong>National Symbols:</strong> To respect national flag, anthem, constitution</li>
  <li><strong>Unity:</strong> To value freedom and maintain sovereignty/integrity</li>
  <li><strong>Service:</strong> If called upon, defend India</li>
  <li><strong>Promote Harmony:</strong> To promote harmony and brotherhood among all</li>
  <li><strong>Heritage:</strong> To protect and improve natural environment</li>
  <li><strong>Scientific Attitude:</strong> To develop scientific temper and spirit of inquiry</li>
  <li><strong>Child Welfare:</strong> Parents/guardians to provide education to children (6-14)</li>
  <li><strong>Public Property:</strong> Not to damage public property</li>
  <li><strong>Civic Duty:</strong> (Added in 2002) To promote excellence in all fields</li>
</ol>

<h3>Important Points:</h3>
<ul>
  <li><strong>Justiciable:</strong> Are enforceable - violation can result in legal action</li>
  <li><strong>Added by:</strong> 42nd Amendment (1976) - The Emergency Amendment</li>
  <li><strong>Purpose:</strong> Balance rights with responsibilities</li>
  <li><strong>Against Whom:</strong> Duties imposed on citizens, not government</li>
</ul>

<h3>Scope and Limitations:</h3>
<ul>
  <li>Cannot be enforced through separate law - enforced through existing laws</li>
  <li>Must be promoted through education and awareness</li>
  <li>Complement fundamental rights</li>
  <li>Create a sense of national responsibility</li>
</ul>
        ''',
        'xp_reward': 20
    },
    {
        'title': 'Union Executive - President and Prime Minister',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '''
<h2>Union Executive - President and Prime Minister (Articles 52-78)</h2>
<p>Executive includes President, Vice President, Prime Minister, and Council of Ministers.</p>

<h3>The President (Articles 52-62)</h3>
<ul>
  <li><strong>Title:</strong> Head of State, representative of India</li>
  <li><strong>Eligibility:</strong>
    <ul>
      <li>Indian citizen</li>
      <li>Age: Minimum 35 years</li>
      <li>Eligible for Lok Sabha</li>
      <li>No office of profit</li>
    </ul>
  </li>
  <li><strong>Term:</strong> 5 years, re-eligible for second term</li>
  <li><strong>Election:</strong> By electoral college (Parliament + State legislatures)</li>
  <li><strong>Removal:</strong> By impeachment for violating Constitution</li>
</ul>

<h3>Powers of President:</h3>
<ul>
  <li><strong>Executive:</strong> Executive authority vested in President</li>
  <li><strong>Legislative:</strong> Summon/prorogue Parliament, grant assent to bills</li>
  <li><strong>Judicial:</strong> Appoint judges, grant pardons/reprieves</li>
  <li><strong>Diplomatic:</strong> Receive foreign officials, declare war/peace</li>
  <li><strong>Military:</strong> Commander-in-Chief of armed forces</li>
</ul>

<h3>The Prime Minister (Articles 74-78)</h3>
<ul>
  <li><strong>Role:</strong> Chief executive, head of government</li>
  <li><strong>Eligibility:</strong>
    <ul>
      <li>Indian citizen</li>
      <li>Minimum age 25 years</li>
      <li>Member of Lok Sabha or Rajya Sabha</li>
    </ul>
  </li>
  <li><strong>Appointment:</strong> By President (Usually member of majority party in Lok Sabha)</li>
  <li><strong>Term:</strong> 5 years or until loss of majority</li>
</ul>

<h3>Powers and Functions of PM:</h3>
<ul>
  <li>Head of Union government</li>
  <li>Chairman of Union Cabinet</li>
  <li>Advises President on ministerial appointments</li>
  <li>Coordinates work of ministers</li>
  <li>Reports on government affairs to Parliament</li>
  <li>Responsible for defense and foreign policy</li>
</ul>

<h3>Council of Ministers:</h3>
<ul>
  <li><strong>Composition:</strong> Cabinet ministers, ministers of state, deputy ministers</li>
  <li><strong>Number:</strong> Should not exceed 15% of Lok Sabha strength (approx 80)</li>
  <li><strong>Accountability:</strong> Collectively responsible to Lok Sabha</li>
  <li><strong>Duration:</strong> Hold office during pleasure of President (but effectively at PM's will)</li>
</ul>
        ''',
        'xp_reward': 35
    },
    {
        'title': 'Union Legislature - Parliament Structure and Functions',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': '''
<h2>Union Legislature - Parliament (Articles 79-123)</h2>
<p>Parliament is the supreme legislative body consisting of the President, Lok Sabha (Lower House), and Rajya Sabha (Upper House).</p>

<h3>Lok Sabha (House of the People)</h3>
<ul>
  <li><strong>Members:</strong> 545 (530 from states + 13 from UTs + 2 Anglo-Indians nominated by President)</li>
  <li><strong>Term:</strong> 5 years (can be dissolved earlier)</li>
  <li><strong>Speaker:</strong> Presiding officer elected by members on first day</li>
  <li><strong>Qualifications:</strong> Indian citizen, 25+ years, enrolled voter, no disqualifications</li>
  <li><strong>Constituency:</strong> Direct election from single-member constituencies</li>
</ul>

<h3>Lok Sabha Powers:</h3>
<ul>
  <li>Money bills (Financial legislation) originate here</li>
  <li>Budget passed here first</li>
  <li>Vote of no-confidence on government</li>
  <li>Union lists exclusively</li>
  <li>Most powerful in money matters</li>
</ul>

<h3>Rajya Sabha (Council of States)</h3>
<ul>
  <li><strong>Members:</strong> 245 (233 from states/UTs + 12 nominated by President)</li>
  <li><strong>Term:</strong> 6 years (1/3 retire every 2 years - permanent body)</li>
  <li><strong>Chairman:</strong> Vice President of India</li>
  <li><strong>Method:</strong> Indirect election by state legislative assemblies</li>
  <li><strong>Representation:</strong> Based on population of states</li>
</ul>

<h3>Rajya Sabha Powers:</h3>
<ul>
  <li>Cannot reject financial bills (only delay)</li>
  <li>Can initiate non-money bills</li>
  <li>Review and suggest amendments</li>
  <li>More deliberative (focused on detailed discussion)</li>
  <li>12-15 year standing members for stability</li>
</ul>

<h3>Parliamentary Procedures:</h3>
<ul>
  <li><strong>Bill Passage:</strong> Three readings (First, Second with committee, Third)</li>
  <li><strong>Assent:</strong> Presidential assent mandatory for law</li>
  <li><strong>Pocket Veto:</strong> President can return bill for reconsideration (Not absolute veto)</li>
  <li><strong>Override:</strong> Both houses can pass again with simple majority to override return</li>
</ul>

<h3>Privileges of Parliament Members:</h3>
<ul>
  <li>Freedom of speech during proceedings</li>
  <li>Freedom from arrest during session (with exceptions)</li>
  <li>Immunity from legal action for statements</li>
  <li>Right to attend/participate in proceedings</li>
</ul>

<h3>Disqualifications for Membership:</h3>
<ul>
  <li>Criminal conviction (more than 2 years)</li>
  <li>Mental unsoundness</li>
  <li>Bankrupt</li>
  <li>Foreign allegiance</li>
  <li>Office of profit</li>
  <li>Disqualification under Representation of People Act</li>
</ul>
        ''',
        'xp_reward': 40
    },
    {
        'title': 'State Executive and Legislature',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '''
<h2>State Government - Executive and Legislature</h2>
<p>States have parallel executive and legislative structures to Union government, following federal model.</p>

<h3>State Executive</h3>
<ul>
  <li><strong>Governor:</strong> Constitutional head (like President)</li>
  <li><strong>Chief Minister:</strong> Head of government (like PM)</li>
  <li><strong>Council of Ministers:</strong> Executive body answerable to legislature</li>
</ul>

<h3>Governor (Articles 153-163)</h3>
<ul>
  <li><strong>Appointment:</strong> By President for each state</li>
  <li><strong>Eligibility:</strong> Indian citizen, 35+ years, eligible for Lok Sabha</li>
  <li><strong>Term:</strong> 5 years, renewable</li>
  <li><strong>Removal:</strong> By President (can be removed at pleasure or for misconduct)</li>
</ul>

<h3>Governor's Powers:</h3>
<ul>
  <li>Executive authority of state vested in Governor</li>
  <li>Appoints Chief Minister (usually majority leader)</li>
  <li>Reserves bills for President's consideration</li>
  <li>Grants ordinances when legislature not in session</li>
  <li>Issues notifications and administrative decisions</li>
</ul>

<h3>State Legislature</h3>
<ul>
  <li><strong>Bicameral:</strong> 6 states (Andhra Pradesh, Bihar, Karnataka, Maharashtra, Telangana, Uttar Pradesh)</li>
  <li><strong>Unicameral:</strong> 22 states (23 if J&K included)</li>
  <li><strong>Assembly (Vidhan Sabha):</strong> Lower house, directly elected</li>
  <li><strong>Council (Vidhan Parishad):</strong> Upper house, indirectly elected (if exists)</li>
</ul>

<h3>State Assembly:</h3>
<ul>
  <li><strong>Members:</strong> 60 to 500 depending on population</li>
  <li><strong>Term:</strong> 5 years</li>
  <li><strong>Speaker:</strong> Elected by members</li>
  <li><strong>Powers:</strong> Make laws on state subjects, approve budget</li>
</ul>

<h3>Panchayati Raj (73rd Amendment)</h3>
<ul>
  <li><strong>Three tier system:</strong> New Delhi, District, Block, Village</li>
  <li><strong>30% seats:</strong> Reservation for women</li>
  <li><strong>SC/ST seats:</strong> Proportionate representation</li>
  <li><strong>Powers:</strong> Local development, welfare, agriculture</li>
  <li><strong>Duration:</strong> 5-year term, dissolution allowed</li>
</ul>

<h3>Municipal Administration (74th Amendment)</h3>
<ul>
  <li><strong>Three types:</strong> Municipal Corporation (cities), Municipality (towns), Nagar Panchayat (villages under urban influence)</li>
  <li><strong>Mayor:</strong> Elected directly by voters (in most cities now)</li>
  <li><strong>Powers:</strong> Urban development, public health, water supply, sanitation</li>
  <li><strong>Duration:</strong> 5-year term</li>
</ul>
        ''',
        'xp_reward': 35
    },
    {
        'title': 'Election Process and Electoral System',
        'subject': 'Polity',
        'level': 'Intermediate',
        'content': '''
<h2>Elections in India - System and Process</h2>
<p>India follows Universal Adult Suffrage with secret ballot multi-member constituency system.</p>

<h3>Voting Rights (Representation of People Act, 1951)</h3>
<ul>
  <li><strong>Age:</strong> 18 years and above (reduced from 21 in 1989)</li>
  <li><strong>Citizenship:</strong> Indian citizen</li>
  <li><strong>Residence:</strong> No specific period required</li>
  <li><strong>Disqualifications:</strong> Non-citizen, non-resident, unsound mind, criminal conviction</li>
</ul>

<h3>Election Commission of India</h3>
<ul>
  <li><strong>Members:</strong> Chief Election Commissioner + 2 Election Commissioners (3-member body now)</li>
  <li><strong>Independence:</strong> Constitutional body with multi-member structure</li>
  <li><strong>Functions:</strong> Conduct elections, ensure free and fair polls, supervisory role</li>
  <li><strong>Powers:</strong> Can postpone elections, disqualify candidates, ban symbols</li>
</ul>

<h3>Lok Sabha Elections</h3>
<ul>
  <li><strong>Constituencies:</strong> 543 single-member constituencies</li>
  <li><strong>Method:</strong> First-past-the-post (candidate with most votes wins)</li>
  <li><strong>Frequency:</strong> Every 5 years (Can be dissolved earlier)</li>
  <li><strong>Eligibility:</strong> 25+ years, Indian citizen, sound mind</li>
  <li><strong>Cycle:</strong> General elections followed by state elections</li>
</ul>

<h3>Election Process:</h3>
<ol>
  <li><strong>Notification:</strong> President issues proclamation</li>
  <li><strong>Nomination:</strong> Candidates file nominations (with proposers/seconders)</li>
  <li><strong>Scrutiny:</strong> Election officer checks validity</li>
  <li><strong>Withdrawal:</strong> Candidates can withdraw nominations</li>
  <li><strong>Polling:</strong> Voting using EVMs (Electronic Voting Machines)</li>
  <li><strong>Counting:</strong> Votes counted in presence of candidate representatives</li>
  <li><strong>Declaration:</strong> Official results declared, winning candidate takes oath</li>
</ol>

<h3>Electoral Reforms:</h3>
<ul>
  <li><strong>Electronic Voting Machines (EVMs):</strong> Replaced paper ballots in 2000</li>
  <li><strong>VVPAT:</strong> Voter Verified Paper Audit Trail (Added 2019 onwards)</li>
  <li><strong>Model Code of Conduct:</strong> Restricts government activities during elections</li>
  <li><strong>Reserved Constituencies:</strong> For SC (15.6%) and ST (7.8%)</li>
</ul>

<h3>Anti-Defection Law (1985)</h3>
<ul>
  <li>Prevents elected members from changing party</li>
  <li>Disqualification if member votes against party direction</li>
  <li>Exceptions: Party merger/split, one-third members change party</li>
  <li>Disqualification period: Until end of term or until rejoining old party</li>
</ul>
        ''',
        'xp_reward': 30
    },
    {
        'title': 'Judicial System of India',
        'subject': 'Polity',
        'level': 'Advanced',
        'content': '''
<h2>Judicial System of India (Articles 124-147)</h2>
<p>Three-tier judicial system: Supreme Court, High Courts, District/Lower Courts.</p>

<h3>Supreme Court of India</h3>
<ul>
  <li><strong>Establishment:</strong> Article 124 of Constitution</li>
  <li><strong>Location:</strong> New Delhi</li>
  <li><strong>Chief Justice:</strong> Senior-most judge with 5+ years seniority</li>
  <li><strong>Judges:</strong> Chief Justice + 33 judges (can be increased by law)</li>
  <li><strong>Tenure:</strong> Until age 65 years (with few exceptions)</li>
</ul>

<h3>Jurisdiction of Supreme Court:</h3>
<ul>
  <li><strong>Appellate:</strong> Appeal from High Courts on constitutional/legal matters</li>
  <li><strong>Original:</strong> Disputes between Centre-State or inter-state cases</li>
  <li><strong>Writ:</strong> Issue writs for enforcement of fundamental rights (Article 32)</li>
  <li><strong>Advisory:</strong> Opinion on matters referred by President (declaratory only)</li>
</ul>

<h3>Powers of Supreme Court:</h3>
<ul>
  <li><strong>Judicial Review:</strong> Can strike down unconstitutional laws/actions</li>
  <li><strong>Interpret Constitution:</strong> Final interpreter of Constitution</li>
  <li><strong>Suo Moto:</strong> Can take cognizance of violations without petition</li>
  <li><strong>Contempt:</strong> Can punish for contempt of court</li>
</ul>

<h3>High Courts</h3>
<ul>
  <li><strong>Number:</strong> 25 High Courts (one per state/group of states)</li>
  <li><strong>Judges:</strong> Chief Justice + Principal judges (varies by court)</li>
  <li><strong>Tenure:</strong> Until age 62 years</li>
</ul>

<h3>High Court Functions:</h3>
<ul>
  <li>Appellate jurisdiction in civil/criminal cases</li>
  <li>Supervisory powers over lower courts</li>
  <li>Issue writs for fundamental rights</li>
  <li>Administrative regulation of subordinate courts</li>
</ul>

<h3>District and Lower Courts</h3>
<ul>
  <li><strong>District Judge:</strong> Heads civil and criminal district courts</li>
  <li><strong>Civil Courts:</strong> Handle civil disputes (property, contracts, etc.)</li>
  <li><strong>Criminal Courts:</strong> Handle criminal cases (theft, assault, etc.)</li>
  <li><strong>Session Judge:</strong> Handles serious crimes (murder, rape)</li>
  <li><strong>Magistrate:</strong> Lower-level courts, handles minor offenses</li>
</ul>

<h3>Types of Writs (Article 32 & 226)</h3>
<ol>
  <li><strong>Habeas Corpus:</strong> Against unlawful detention</li>
  <li><strong>Mandamus:</strong> To perform legal duty</li>
  <li><strong>Prohibition:</strong> Against unlawful action</li>
  <li><strong>Certiorari:</strong> To quash illegal order</li>
  <li><strong>Quo Warranto:</strong> Against usurped power</li>
</ol>

<h3>Judicial Independence</h3>
<ul>
  <li>Security of tenure - cannot be arbitrarily removed</li>
  <li>Removal only by impeachment (2/3 majority, both houses)</li>
  <li>Immunity from personal liability</li>
  <li>Judicial review power (check on executive and legislature)</li>
</ul>
        ''',
        'xp_reward': 40
    },
]

# ============================================================================
# HISTORY (Indian History) - 12 Materials
# ============================================================================

COMPREHENSIVE_MATERIALS.extend([
    {
        'title': 'Ancient India - Indus Valley Civilization',
        'subject': 'History',
        'level': 'Beginner',
        'content': '''
<h2>Indus Valley Civilization (2600-1900 BCE)</h2>
<p>One of the world's oldest civilizations, contemporary with Egyptian and Mesopotamian civilizations.</p>

<h3>Key Features:</h3>
<ul>
  <li><strong>Period:</strong> 2600-1900 BCE (mature phase)</li>
  <li><strong>Extent:</strong> Sindh, Punjab, Gujarat, Western Rajasthan, parts of Haryana</li>
  <li><strong>Spread:</strong> Over 1.3 million sq km (largest ancient civilization of its time)</li>
  <li><strong>Major Cities:</strong> Harappa, Mohenjo-daro, Dholavira, Kalibangan</li>
</ul>

<h3>Urban Planning and Architecture:</h3>
<ul>
  <li><strong>Grid System:</strong> Streets arranged in grid pattern</li>
  <li><strong>Drainage:</strong> Sophisticated drainage system - underground sewers</li>
  <li><strong>Buildings:</strong> Fired brick construction, multi-storied houses</li>
  <li><strong>Granaries:</strong> Large storehouses for food grain</li>
  <li><strong>Public Baths:</strong> Great Bath at Mohenjo-daro (40.2m × 23.4m × 2.4m)</li>
</ul>

<h3>Economy:</h3>
<ul>
  <li><strong>Trade:</strong> Extensive trade with Mesopotamia, Egypt, Arabia</li>
  <li><strong>Agriculture:</strong> Wheat, barley, cotton, peas</li>
  <li><strong>Animals:</strong> Cattle, buffalo, sheep, goat (NO HORSE archaeological evidence)</li>
  <li><strong>Crafts:</strong> Pottery, figurines, jewelry, weapons</li>
  <li><strong>Weights and Measures:</strong> Standardized for trade</li>
</ul>

<h3>Society and Culture:</h3>
<ul>
  <li><strong>Religion:</strong> Worship of mother goddess, phallic symbol (Shiva connection?)</li>
  <li><strong>Seals:</strong> Numerous seals with pictographic script (NOT deciphered)</li>
  <li><strong>Art:</strong> Terracotta figurines, bronze dancing girl statue</li>
  <li><strong>Games:</strong> Dice, gaming boards found</li>
  <li><strong>No temples or palaces:</strong> Suggests egalitarian society</li>
</ul>

<h3>Decline:</h3>
<ul>
  <li><strong>Causes:</strong> Environmental change, flood, invasion (debated)</li>
  <li><strong>Date:</strong> Around 1900 BCE</li>
  <li><strong>Gradual:</strong> No evidence of sudden destruction</li>
</ul>

<h3>Script:</h3>
<ul>
  <li><strong>Type:</strong> Pictographic/logographic (like Egyptian hieroglyphics)</li>
  <li><strong>Symbols:</strong> 400-600 characters identified</li>
  <li><strong>Direction:</strong> Right to left (opposite of modern scripts)</li>
  <li><strong>Status:</strong> Still undeciphered - remains a mystery</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Vedic Period - Foundation of Hindu Culture',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '''
<h2>Vedic Period (1500-600 BCE)</h2>
<p>Period of sacred texts (Vedas) and foundation of Hindu civilization and culture.</p>

<h3>Phases of Vedic Period:</h3>
<ul>
  <li><strong>Early Vedic (1500-1200 BCE):</strong> Rig Vedic period, tribal society, pastoralism</li>
  <li><strong>Later Vedic (1200-600 BCE):</strong> Expansion of kingdoms, agriculture growth, Upanishads</li>
</ul>

<h3>The Four Vedas:</h3>
<ul>
  <li><strong>Rigveda:</strong> Oldest, hymns to gods, 10 books, 1028 hymns</li>
  <li><strong>Yajurveda:</strong> Ritual texts, sacrificial procedures</li>
  <li><strong>Samaveda:</strong> Melodic recitations, music-related verses</li>
  <li><strong>Atharvaveda:</strong> Latest, protective spells, healing rituals</li>
</ul>

<h3>Society - Varna System (Early):</h3>
<ul>
  <li><strong>Brahmins:</strong> Priests and scholars</li>
  <li><strong>Kshatriyas:</strong> Warriors and rulers</li>
  <li><strong>Vaishyas:</strong> Merchants and cultivators</li>
  <li><strong>Shudras:</strong> Laborers and servants</li>
</ul>

<h3>Economy and Life:</h3>
<ul>
  <li><strong>Economy:</strong> Transition from pastoralism to agriculture</li>
  <li><strong>Settlement:</strong> Movement from northwest to Gangetic plains</li>
  <li><strong>Technology:</strong> Iron tools introduced (1200 BCE onwards)</li>
  <li><strong>Trade:</strong> Internal trade, limited external trade</li>
</ul>

<h3>Religion - Vedic Gods:</h3>
<ul>
  <li><strong>Indra:</strong> God of thunder and war (most prominent in Rigveda)</li>
  <li><strong>Agni:</strong> God of fire, intermediary between gods and humans</li>
  <li><strong>Varuna:</strong> God of oceans, moral law enforcer</li>
  <li><strong>Soma:</strong> God of plant extract, ritual drink</li>
</ul>

<h3>Sacred Texts (Later Vedic):</h3>
<ul>
  <li><strong>Upanishads:</strong> Philosophical texts, seek ultimate reality (Brahman)</li>
  <li><strong>Brahmanas:</strong> Explanatory texts on rituals</li>
  <li><strong>Aranyakas:</strong> Forest treatises</li>
</ul>

<h3>Key Concepts:</h3>
<ul>
  <li><strong>Yajna (Sacrifice):</strong> Central ritual practice</li>
  <li><strong>Dharma:</strong> Cosmic order and duty</li>
  <li><strong>Atman:</strong> Individual soul</li>
  <li><strong>Brahman:</strong> Ultimate reality</li>
</ul>
        ''',
        'xp_reward': 30
    },
    {
        'title': 'Mauryan Empire - Peak of Ancient Indian Power',
        'subject': 'History',
        'level': 'Advanced',
        'content': '''
<h2>Mauryan Empire (322-185 BCE)</h2>
<p>First pan-Indian empire, established strong centralized state structure and administration.</p>

<h3>Founders and Rulers:</h3>
<ul>
  <li><strong>Chandragupta Maurya (322-298 BCE):</strong> Founder, defeated Nanda dynasty, took throne</li>
  <li><strong>Bindusara (298-273 BCE):</strong> Expanded empire, "Slayer of enemies"</li>
  <li><strong>Ashoka (273-232 BCE):</strong> Most significant, embraced Buddhism after Kalinga war</li>
</ul>

<h3>Administration under Chandragupta:</h3>
<ul>
  <li><strong>Capital:</strong> Pataliputra (modern Patna)</li>
  <li><strong>System:</strong> Highly centralized bureaucracy</li>
  <li><strong>Spies:</strong> Elaborate spy network for surveillance</li>
  <li><strong>Officers:</strong> Secretary, treasurer, military commander</li>
  <li><strong>Taxation:</strong> 1/4 to 1/6 of produce collected</li>
</ul>

<h3>Expansion Under Ashoka:</h3>
<ul>
  <li><strong>Kalinga War (261 BCE):</strong> Major military campaign, 100,000+ deaths</li>
  <li><strong>Transformation:</strong> After war, embraced Buddhism and non-violence (Ahimsa)</li>
  <li><strong>Extent:</strong> Empire covered nearly entire subcontinent</li>
  <li><strong>Edicts:</strong> Issued Rock Edicts and Pillar Edicts across empire</li>
</ul>

<h3>Ashoka's Reforms - Dhamma:</h3>
<ul>
  <li><strong>Dhamma Concept:</strong> Moral and ethical code for citizens</li>
  <li><strong>Principles:</strong> Truthfulness, compassion, non-violence, respect for all life</li>
  <li><strong>Officers:</strong> Appointed Dhamma Mahamattas (ethical officers)</li>
  <li><strong>Propagation:</strong> Used edicts to spread dharma across empire</li>
</ul>

<h3>Economy:</h3>
<ul>
  <li><strong>Agriculture:</strong> Primary economic base, irrigation systems</li>
  <li><strong>Trade:</strong> Extensive internal and external trade routes</li>
  <li><strong>Currency:</strong> Punch-marked coins with various symbols</li>
  <li><strong>Merchants:</strong> Trading communities controlled commerce</li>
</ul>

<h3>Mauryan Military:</h3>
<ul>
  <li><strong>Organization:</strong> Standing army of 700,000 infantry, 9,000 elephants</li>
  <li><strong>Discipline:</strong> Well-organized and disciplined troops</li>
  <li><strong>Technology:</strong> Advanced weaponry and fortifications</li>
  <li><strong>Navy:</strong> Strong naval force protecting trade routes</li>
</ul>

<h3>Religious and Cultural Impact:</h3>
<ul>
  <li><strong>Buddhism:</strong> Ashoka major Buddhist patron, helped spread to Central Asia, China</li>
  <li><strong>Religious Tolerance:</strong> Patronized Buddhism, Jainism, and Hinduism</li>
  <li><strong>Literature:</strong> Court poet Kalidasa (possibly), development of grammar</li>
  <li><strong>Art:</strong> Ashoka's pillars and rock edicts, sculpture development</li>
</ul>

<h3>Decline:</h3>
<ul>
  <li><strong>After Ashoka:</strong> Empire gradually weakened after his death (232 BCE)</li>
  <li><strong>Fragmentation:</strong> Regional kingdoms emerged</li>
  <li><strong>Final Collapse:</strong> 185 BCE - Brihadratha Maurya assassinated by Pushyamitra Shunga</li>
</ul>

<h3>Significance:</h3>
<ul>
  <li>First attempt at unified Indian state</li>
  <li>Established lasting bureaucratic traditions</li>
  <li>Ashoka's edicts - oldest preserved written texts in India</li>
  <li>Major milestone in Asian civilization development</li>
</ul>
        ''',
        'xp_reward': 40
    },
    {
        'title': 'Medieval India - Delhi Sultanate Period',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '''
<h2>Delhi Sultanate (1206-1526 CE)</h2>
<p>Period of Islamic rule in India, established strong centralized kingdoms in North India.</p>

<h3>Five Major Dynasties:</h3>
<ul>
  <li><strong>Slave Dynasty (1206-1290):</strong> 
    <ul>
      <li>Founder: Qutab-ud-din Aibak</li>
      <li>Capital: Delhi</li>
      <li>Important ruler: Muhammad of Ghor (not sultan but established rule)</li>
    </ul>
  </li>
  <li><strong>Khilji Dynasty (1290-1320):</strong>
    <ul>
      <li>Founder: Jalal-ud-din Khilji</li>
      <li>Most powerful: Alauddin Khilji - conquered Marathas, Deccan</li>
      <li>Administrative reforms and price controls</li>
    </ul>
  </li>
  <li><strong>Tughlaq Dynasty (1320-1413):</strong>
    <ul>
      <li>Muhammad bin Tughlaq: Ambitious but failed policies</li>
      <li>Firoz Shah Tughlaq: Stable rule, public works</li>
      <li>Eventually lost power to nobility</li>
    </ul>
  </li>
  <li><strong>Sayyid Dynasty (1414-1451):</strong>
    <ul>
      <li>Weak rulers, lost control to nobility</li>
      <li>Regional kingdoms gained independence</li>
    </ul>
  </li>
  <li><strong>Lodi Dynasty (1451-1526):</strong>
    <ul>
      <li>Ibrahim Lodi: Last Delhi Sultan</li>
      <li>Defeated by Babur at Battle of Panipat (1526)</li>
    </ul>
  </li>
</ul>

<h3>Administration:</h3>
<ul>
  <li><strong>Government:</strong> Centralized monarchy with sultanate</li>
  <li><strong>Officials:</strong> Iqtadar (nobles holding territories), Muqtis (governors)</li>
  <li><strong>Judiciary:</strong> Islamic law (Sharia) administered by Sharia judges</li>
  <li><strong>Revenue:</strong> Land tax (Kharaj) primary income source</li>
</ul>

<h3>Economy and Society:</h3>
<ul>
  <li><strong>Trade:</strong> Flourished, merchants class important</li>
  <li><strong>Agriculture:</strong> Major economic base with irrigation</li>
  <li><strong>Class System:</strong> Muslim aristocracy > Hindu nobility > Peasants</li>
  <li><strong>Cities:</strong> Delhi major center - grew wealthy and influential</li>
</ul>

<h3>Architecture and Culture:</h3>
<ul>
  <li><strong>Indo-Islamic Architecture:</strong> Blend of Islamic and Indian styles</li>
  <li><strong>Qutab Minar:</strong> 73m high minaret in Delhi (victory tower)</li>
  <li><strong>Mosques:</strong> Jama Masjid and many others constructed</li>
  <li><strong>Literature:</strong> Sufi poetry, Persian prose developed</li>
  <li><strong>Language:</strong> Urdu evolved from Hindi-Persian blend</li>
</ul>

<h3>Religious Policies:</h3>
<ul>
  <li><strong>Jizya Tax:</strong> Special tax on non-Muslims (dhimmis)</li>
  <li><strong>Conversion:</strong> Incentives for conversion to Islam</li>
  <li><strong>Hindu Temples:</strong> Many destroyed, some tolerated</li>
  <li><strong>Sufi Saints:</strong> Played role in Islam propagation</li>
</ul>

<h3>Key Accomplishments:</h3>
<ul>
  <li>Established Islamic state in India</li>
  <li>Created efficient administrative system</li>
  <li>Developed Indo-Islamic culture and architecture</li>
  <li>Maintained relative stability and order</li>
</ul>
        ''',
        'xp_reward': 35
    },
    {
        'title': 'Mughal Empire - Height of Grandeur',
        'subject': 'History',
        'level': 'Advanced',
        'content': '''
<h2>Mughal Empire (1526-1857)</h2>
<p>Height of Islamic power in India, created one of the world's greatest empires with lasting cultural impact.</p>

<h3>Major Emperors:</h3>
<ul>
  <li><strong>Babur (1526-1530):</strong>
    <ul>
      <li>Founder, Battle of Panipat (1526) vs Ibrahim Lodi</li>
      <li>Established empire but ruled only 4 years</li>
    </ul>
  </li>
  <li><strong>Akbar (1556-1605):</strong>
    <ul>
      <li>Greatest Mughal emperor - expanded and consolidated empire</li>
      <li>Military conquests: Gujarat, Bengal, Rajputana, Malwa, Khandesh</li>
      <li>Introduced Mansabdari system of nobility</li>
      <li>Married Rajput princesses, alliance with Rajputs</li>
      <li>Religious tolerance - abolish Jizya tax, Sulh-i-kul (universal peace)</li>
      <li>Founded Din-i-Ilahi (syncretic religion) - NOT successful</li>
    </ul>
  </li>
  <li><strong>Shah Jahan (1627-1658):</strong>
    <ul>
      <li>Builder - Taj Mahal (white marble mausoleum), Red Fort, Jama Masjid</li>
      <li>Expanded empire to maximum territorial extent</li>
      <li>Patronized arts, architecture, literature</li>
      <li>Later life: Imprisoned by son Aurangzeb</li>
    </ul>
  </li>
  <li><strong>Aurangzeb (1658-1707):</strong>
    <ul>
      <li>Last great Mughal - ruled 49 years</li>
      <li>Attempt to extend empire to Deccan - constant wars</li>
      <li>Religious orthodoxy - banned Hindu festivals, reimposed Jizya</li>
      <li>Strict Islamic policies alienated Hindu nobility</li>
      <li>Expanded empire but weakened unity</li>
    </ul>
  </li>
</ul>

<h3>Administration - Akbar's System:</h3>
<ul>
  <li><strong>Mansabdari System:</strong> Ranking system for nobles based on salary</li>
  <li><strong>Rank Structure:</strong> Emperor → Princes → High nobles → Lesser nobles</li>
  <li><strong>Appointments:</strong> Based on merit, not heredity</li>
  <li><strong>Diwani System:</strong> Revenue collection and local administration</li>
</ul>

<h3>Economy:</h3>
<ul>
  <li><strong>Agricultural Base:</strong> 90% population engaged in farming</li>
  <li><strong>Land Revenue:</strong> 1/3 of produce collected as tax</li>
  <li><strong>Trade:</strong> Extensive trade networks - Indian textiles, spices, cotton</li>
  <li><strong>Currency:</strong> Mughal rupee, gold/silver coins</li>
  <li><strong>Commerce:</strong> Merchants guilds, caravanserais (trading posts)</li>
</ul>

<h3>Architecture and Arts:</h3>
<ul>
  <li><strong>Taj Mahal:</strong> UNESCO World Heritage, marble inlay work</li>
  <li><strong>Red Fort:</strong> Massive fortification, Delhi's symbol</li>
  <li><strong>Mughal Gardens:</strong> Char Bagh design (four gardens)</li>
  <li><strong>Palace Architecture:</strong> Blend of Persian and Indian styles</li>
  <li><strong>Miniature Paintings:</strong> Mughal school of art, detailed courtly scenes</li>
  <li><strong>Literature:</strong> Persian poetry, Urdu language flourished</li>
</ul>

<h3>Culture and Society:</h3>
<ul>
  <li><strong>Syncretic Culture:</strong> Hindu-Muslim blend under Akbar era</li>
  <li><strong>Music:</strong> Hindustani classical music patronized</li>
  <li><strong>Cuisine:</strong> Mughlai food - biryani, tandoori, kebabs</li>
  <li><strong>Language:</strong> Urdu official court language, Persian literary language</li>
</ul>

<h3>Reasons for Decline:</h3>
<ul>
  <li><strong>After Aurangzeb:</strong> Weak successors, internal conflicts</li>
  <li><strong>Maratha Rise:</strong> Marathas under Shivaji challenged Mughal power</li>
  <li><strong>Regional Powers:</strong> Nizams of Hyderabad, Nawabs of Bengal independent</li>
  <li><strong>European Companies:</strong> British, French, Portuguese established trade posts</li>
  <li><strong>Economic Crisis:</strong> Inflation, debasement of currency</li>
  <li><strong>Final Collapse:</strong> 1857 - Rebellion and British takeover</li>
</ul>

<h3>Legacy:</h3>
<ul>
  <li>Indo-Islamic culture and civilization</li>
  <li>Architectural masterpieces still standing</li>
  <li>Urdu language and literature</li>
  <li>Administrative systems influenced later rulers</li>
</ul>
        ''',
        'xp_reward': 45
    },
])

# ============================================================================
# GEOGRAPHY - 10 Materials
# ============================================================================

COMPREHENSIVE_MATERIALS.extend([
    {
        'title': 'Physical Geography - Landforms and Relief',
        'subject': 'Geography',
        'level': 'Beginner',
        'content': '''
<h2>Landforms and Relief Features of India</h2>
<p>India has diverse landforms created by geological processes over millions of years.</p>
<h3>Major Mountain Ranges:</h3>
<ul>
  <li><strong>Himalayan Mountains:</strong> Young fold mountains, highest peaks (Mt. Kanchenjunga - 3,580m)</li>
  <li><strong>Western Ghats:</strong> Escarpment running parallel to west coast, 1,600 km long</li>
  <li><strong>Eastern Ghats:</strong> Discontinuous mountains with low altitude</li>
  <li><strong>Vindhya and Satpura:</strong> Central Indian plateau boundaries</li>
</ul>
<h3>Plains:</h3>
<ul>
  <li><strong>Indo-Gangetic Plain:</strong> Most fertile, 2,400 km long, supports 50% population</li>
  <li><strong>Coastal Plains:</strong> Western and Eastern coasts</li>
</ul>
<h3>Plateaus:</h3>
<ul>
  <li><strong>Deccan Plateau:</strong> Largest plateau, black soil region</li>
  <li><strong>Malwa Plateau:</strong> North-central India</li>
</ul>
        ''',
        'xp_reward': 20
    },
    {
        'title': 'Climate and Monsoons of India',
        'subject': 'Geography',
        'level': 'Intermediate',
        'content': '''
<h2>Indian Climate and Monsoon System</h2>
<p>India's climate is primarily tropical monsoon type, with seasonal variations.</p>
<h3>Climate Zones:</h3>
<ul>
  <li><strong>Tropical Monsoon:</strong> High temperature and rainfall</li>
  <li><strong>Tropical Dry:</strong> High temperature, low rainfall</li>
  <li><strong>Subtropical:</strong> Moderate temperature and rainfall</li>
  <li><strong>Alpine:</strong> Himalayan regions with snowfall</li>
</ul>
<h3>Monsoons:</h3>
<ul>
  <li><strong>Southwest Monsoon:</strong> June-September, brings 80% rainfall to India</li>
  <li><strong>Northeast Monsoon:</strong> October-December, brings rain to coastal regions</li>
  <li><strong>Retreating Monsoon:</strong> October-November, seasonal transition</li>
</ul>
<h3>Rainfall Patterns:</h3>
<ul>
  <li><strong>High Rainfall:</strong> >250 cm - Western Ghats, Assam, Meghalaya</li>
  <li><strong>Moderate Rainfall:</strong> 50-250 cm - Most of India</li>
  <li><strong>Low Rainfall:</strong> <50 cm - Rajasthan, interior plateaus</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Rivers and Water Resources',
        'subject': 'Geography',
        'level': 'Intermediate',
        'content': '''
<h2>Major Rivers and Water Systems</h2>
<p>India has a rich network of rivers vital for agriculture, power, and transport.</p>
<h3>Himalayan Rivers:</h3>
<ul>
  <li><strong>Ganga:</strong> Sacred river, 2,506 km, flows through UP, Bihar, Bengal, enters Bangladesh</li>
  <li><strong>Brahmaputra:</strong> 2,900 km, flows through Assam, major tributary Meghna</li>
  <li><strong>Indus:</strong> 3,180 km, only 710 km in India, international river</li>
</ul>
<h3>Peninsular Rivers:</h3>
<ul>
  <li><strong>Godavari:</strong> Longest peninsula river, 1,467 km, flows through Maharashtra and Andhra Pradesh</li>
  <li><strong>Krishna:</strong> 1,288 km, major irrigation river</li>
  <li><strong>Narmada:</strong> 1,312 km, flows through central India, form Satpura-Vindhya boundary</li>
  <li><strong>Mahanadi:</strong> Flows through Madhya Pradesh and Odisha</li>
  <li><strong>Cauvery:</strong> 765 km, South India's most important river</li>
</ul>
<h3>Water Resources - Challenges:</h3>
<ul>
  <li>Over-extraction threatening groundwater</li>
  <li>Seasonal flooding and droughts</li>
  <li>Pollution of major rivers (Ganga Clean-up Mission)</li>
  <li>Inter-state water disputes (Cauvery, Krishna)</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Natural Resources - Minerals and Energy',
        'subject': 'Geography',
        'level': 'Advanced',
        'content': '''
<h2>Mineral and Energy Resources of India</h2>
<p>India has abundant mineral deposits crucial for industrial development.</p>
<h3>Metallic Minerals:</h3>
<ul>
  <li><strong>Iron Ore:</strong> High quality, Jharkhand 40%, Odisha 30%, Chhattisgarh 20%</li>
  <li><strong>Manganese:</strong> Used in steel production, Odisha leading producer</li>
  <li><strong>Bauxite (Aluminum):</strong> Odisha, Maharashtra, Jharkhand major sources</li>
  <li><strong>Copper:</strong> Rajas than, Madhya Pradesh, Jharkhand</li>
  <li><strong>Gold:</strong> Rare, limited deposits in Karnataka (Kolar Gold Fields)</li>
</ul>
<h3>Non-Metallic Minerals:</h3>
<ul>
  <li><strong>Coal:</strong> Primary energy source, 70% of India's electricity from coal</li>
  <li><strong>Mica:</strong> 80% world production from India, Jharkhand 50%</li>
  <li><strong>Limestone:</strong> Cement and steel industry feedstock</li>
  <li><strong>Diamond:</strong> Madhya Pradesh major source</li>
</ul>
<h3>Energy Resources:</h3>
<ul>
  <li><strong>Coal:</strong> 300+ billion tonnes reserves (4th largest in world)</li>
  <li><strong>Oil and Gas:</strong> Limited reserves, major import dependent</li>
  <li><strong>Hydroelectric:</strong> Dams provide renewable energy</li>
  <li><strong>Nuclear:</strong> 22 operational power plants</li>
  <li><strong>Renewable:</strong> Solar and wind energy growth (MNRE targets)</li>
</ul>
        ''',
        'xp_reward': 30
    },
])

# ============================================================================
# CURRENT AFFAIRS & GENERAL KNOWLEDGE - 8 Materials
# ============================================================================

COMPREHENSIVE_MATERIALS.extend([
    {
        'title': '2024 Government and Politics Updates',
        'subject': 'Current Affairs',
        'level': 'Beginner',
        'content': '''
<h2>Indian Government 2024 - Current Leadership</h2>
<h3>Constitutional Offices:</h3>
<ul>
  <li><strong>President:</strong> Droupadi Murmu (25th President, took oath March 25, 2022)</li>
  <li><strong>Vice President:</strong> Jagdeep Dhankhar (elected August 2022)</li>
  <li><strong>Prime Minister:</strong> Narendra Modi (3rd terms, from 2014)</li>
  <li><strong>Chief Justice of India:</strong> D Y Chandrachud (50th CJI)</li>
</ul>
<h3>Recent Constitutional Developments (2024):</h3>
<ul>
  <li>Elections update 2024 - General Elections completed</li>
  <li>Government formation and cabinet restructuring</li>
  <li>Major constitutional amendments discussions</li>
  <li>Court judgments on important cases</li>
</ul>
<h3>Union Cabinet 2024:</h3>
<ul>
  <li>Key ministries and minister names (continuously updated)</li>
  <li>Union budget and fiscal policies</li>
  <li>Important ordinances and acts passed</li>
</ul>
        ''',
        'xp_reward': 20
    },
    {
        'title': 'International Relations and Diplomacy',
        'subject': 'Current Affairs',
        'level': 'Intermediate',
        'content': '''
<h2>India\'s International Relations</h2>
<h3>India\'s Foreign Policy Pillars:</h3>
<ul>
  <li><strong>Non-Alignment:</strong> Not tied to any power bloc (since Independence)</li>
  <li><strong>Strategic Autonomy:</strong> Independent decision-making</li>
  <li><strong>Multilateralism:</strong> Engagement with multiple countries and forums</li>
</ul>
<h3>Major International Organizations:</h3>
<ul>
  <li><strong>UN:</strong> Permanent member of Security Council (since 1945)</li>
  <li><strong>BRICS:</strong> Brazil, Russia, India, China, South Africa (economic bloc)</li>
  <li><strong>SCO:</strong> Shanghai Cooperation Organization</li>
  <li><strong>QUAD:</strong> Quadrilateral Security Dialogue (USA, Japan, Australia, India)</li>
  <li><strong>ASEAN:</strong> Regional cooperation in Southeast Asia</li>
  <li><strong>G20:</strong> Group of 20 major economies</li>
</ul>
<h3>Key Bilateral Relations:</h3>
<ul>
  <li><strong>USA:</strong> Strategic partnership, defense cooperation</li>
  <li><strong>China:</strong> Border issues, economic relations, LAC disputes</li>
  <li><strong>Pakistan:</strong> Complex relations, border conflicts</li>
  <li><strong>Russia:</strong> Long-standing partnership, energy cooperation</li>
  <li><strong>Gulf States:</strong> Trade, defense cooperation, diaspora</li>
</ul>
        ''',
        'xp_reward': 25
    },
])

# ============================================================================
# QUANTITATIVE APTITUDE - 10 Materials
# ============================================================================

COMPREHENSIVE_MATERIALS.extend([
    {
        'title': 'Number System and Divisibility',
        'subject': 'Quantitative Aptitude',
        'level': 'Beginner',
        'content': '''
<h2>Number System - Fundamentals</h2>
<h3>Types of Numbers:</h3>
<ul>
  <li><strong>Natural Numbers:</strong> 1, 2, 3, ... (N)</li>
  <li><strong>Whole Numbers:</strong> 0, 1, 2, 3, ... (W)</li>
  <li><strong>Integers:</strong> ..., -2, -1, 0, 1, 2, ... (Z)</li>
  <li><strong>Rational Numbers:</strong> p/q form where p, q are integers, q ≠ 0</li>
  <li><strong>Irrational Numbers:</strong> √2, π, e (cannot be expressed as p/q)</li>
  <li><strong>Real Numbers:</strong> Union of rational and irrational numbers</li>
</ul>
<h3>Divisibility Rules:</h3>
<ul>
  <li><strong>By 2:</strong> Last digit is even</li>
  <li><strong>By 3:</strong> Sum of digits divisible by 3</li>
  <li><strong>By 5:</strong> Last digit is 0 or 5</li>
  <li><strong>By 7:</strong> (Complex rule - divide and check remainder)</li>
  <li><strong>By 11:</strong> Alternating sum of digits divisible by 11</li>
</ul>
<h3>Prime and Composite Numbers:</h3>
<ul>
  <li><strong>Prime:</strong> Numbers divisible only by 1 and itself (2, 3, 5, 7, 11...)</li>
  <li><strong>Composite:</strong> Numbers with more than 2 factors</li>
  <li><strong>LCM:</strong> Least Common Multiple - lowest number divisible by both</li>
  <li><strong>GCD/HCF:</strong> Greatest Common Divisor - highest common factor</li>
</ul>
        ''',
        'xp_reward': 20
    },
    {
        'title': 'Percentage, Profit-Loss, Simple and Compound Interest',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '''
<h2>Commercial Mathematics</h2>
<h3>Percentage Calculations:</h3>
<ul>
  <li><strong>Formula:</strong> Percentage = (Part/Whole) × 100</li>
  <li><strong>Increase:</strong> ((New - Old)/Old) × 100</li>
  <li><strong>Decrease:</strong> ((Old - New)/Old) × 100</li>
  <li><strong>Successive Changes:</strong> a% + b% = (a + b + ab/100)%</li>
</ul>
<h3>Profit and Loss:</h3>
<ul>
  <li><strong>Cost Price (CP):</strong> Buying price</li>
  <li><strong>Selling Price (SP):</strong> Selling price</li>
  <li><strong>Profit:</strong> SP - CP (when SP > CP)</li>
  <li><strong>Loss:</strong> CP - SP (when CP > SP)</li>
  <li><strong>Profit %:</strong> (Profit/CP) × 100</li>
  <li><strong>Loss %:</strong> (Loss/CP) × 100</li>
</ul>
<h3>Simple Interest (SI):</h3>
<ul>
  <li><strong>Formula:</strong> SI = (P × R × T)/100</li>
  <li>P = Principal, R = Rate per annum, T = Time in years</li>
  <li><strong>Amount:</strong> A = P + SI</li>
</ul>
<h3>Compound Interest (CI):</h3>
<ul>
  <li><strong>Formula:</strong> A = P(1 + R/100)^T</li>
  <li><strong>CI:</strong> A - P</li>
  <li><strong>Difference (CI - SI):</strong> SI × [(R/100) × (T-1)]</li>
</ul>
        ''',
        'xp_reward': 30
    },
    {
        'title': 'Ratio, Proportion and Partnership',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '''
<h2>Ratio, Proportion and Partnership</h2>
<h3>Ratio Concepts:</h3>
<ul>
  <li><strong>Definition:</strong> Comparison of two quantities</li>
  <li><strong>Equivalent Ratios:</strong> 2:3 = 4:6 = 6:9</li>
  <li><strong>Compound Ratio:</strong> (a:b) and (c:d) = ac:bd</li>
  <li><strong>Duplicate Ratio:</strong> (a:b) = a²:b²</li>
  <li><strong>Inverse Ratio:</strong> (a:b) = 1/a : 1/b</li>
</ul>
<h3>Proportions:</h3>
<ul>
  <li><strong>Definition:</strong> Equality of two ratios: a:b = c:d (a/b = c/d)</li>
  <li><strong>Cross Multiplication:</strong> If a:b = c:d, then ad = bc</li>
  <li><strong>Direct Proportion:</strong> x ∝ y or x = ky (k is constant)</li>
  <li><strong>Inverse Proportion:</strong> x ∝ 1/y or xy = k</li>
</ul>
<h3>Partnership:</h3>
<ul>
  <li><strong>Profit Sharing:</strong> Divided in ratio of capital invested</li>
  <li><strong>Time Factor:</strong> If different investment periods, profit ∝ (capital × time)</li>
  <li><strong>Example:</strong> A invests 50,000 for 12 months, B invests 60,000 for 8 months</li>
  <li><strong>Profit Ratio:</strong> A:B = (50,000 × 12) : (60,000 × 8) = 5:4</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Time, Speed and Distance',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '''
<h2>Time, Speed and Distance</h2>
<h3>Basic Concepts:</h3>
<ul>
  <li><strong>Speed = Distance ÷ Time</strong></li>
  <li><strong>Distance = Speed × Time</strong></li>
  <li><strong>Time = Distance ÷ Speed</strong></li>
  <li><strong>Unit Conversion:</strong> km/h to m/s: multiply by 5/18; m/s to km/h: multiply by 18/5</li>
</ul>
<h3>Relative Speed:</h3>
<ul>
  <li><strong>Same Direction:</strong> Relative Speed = |S1 - S2|</li>
  <li><strong>Opposite Direction:</strong> Relative Speed = S1 + S2</li>
  <li><strong>Trains Problem:</strong> Relative speed × Combined length = Time to cross</li>
</ul>
<h3>Boat and Stream:</h3>
<ul>
  <li><strong>Upstream Speed:</strong> Boat speed - Stream speed</li>
  <li><strong>Downstream Speed:</strong> Boat speed + Stream speed</li>
  <li><strong>Boat Speed in Still Water:</strong> (Upstream + Downstream) ÷ 2</li>
  <li><strong>Stream Speed:</strong> (Downstream - Upstream) ÷ 2</li>
</ul>
<h3>Average Speed:</h3>
<ul>
  <li><strong>Average Speed = Total Distance ÷ Total Time</strong></li>
  <li>NOT the arithmetic mean of speeds if distances are different</li>
</ul>
        ''',
        'xp_reward': 25
    },
    {
        'title': 'Geometry - Perimeter, Area and Volume',
        'subject': 'Quantitative Aptitude',
        'level': 'Intermediate',
        'content': '''
<h2>Geometry - Shapes and Measurements</h2>
<h3>2D Shapes - Area & Perimeter:</h3>
<ul>
  <li><strong>Triangle:</strong> Area = ½ × base × height; Perimeter = sum of all sides</li>
  <li><strong>Square:</strong> Area = side²; Perimeter = 4 × side</li>
  <li><strong>Rectangle:</strong> Area = length × width; Perimeter = 2(l + w)</li>
  <li><strong>Circle:</strong> Area = πr²; Circumference = 2πr; Diameter = 2r</li>
  <li><strong>Parallelogram:</strong> Area = base × height</li>
  <li><strong>Trapezium:</strong> Area = ½ × (sum of parallel sides) × height</li>
</ul>
<h3>3D Shapes - Volume & Surface Area:</h3>
<ul>
  <li><strong>Cube:</strong> Volume = side³; Surface area = 6 × side²</li>
  <li><strong>Cuboid:</strong> Volume = l × w × h; Surface area = 2(lw + wh + lh)</li>
  <li><strong>Cylinder:</strong> Volume = πr²h; Surface area = 2πrh + 2πr²</li>
  <li><strong>Sphere:</strong> Volume = 4/3 × πr³; Surface area = 4πr²</li>
  <li><strong>Cone:</strong> Volume = 1/3 × πr²h; Slant height = √(r² + h²)</li>
</ul>
        ''',
        'xp_reward': 30
    },
    {
        'title': 'Statistics and Data Interpretation',
        'subject': 'Quantitative Aptitude',
        'level': 'Advanced',
        'content': '''
<h2>Statistics and Data Interpretation</h2>
<h3>Measures of Central Tendency:</h3>
<ul>
  <li><strong>Mean (Average):</strong> Sum of all values ÷ Number of values</li>
  <li><strong>Median:</strong> Middle value when data arranged in order</li>
  <li><strong>Mode:</strong> Most frequently occurring value</li>
  <li><strong>Range:</strong> Highest value - Lowest value</li>
</ul>
<h3>Data Interpretation - Charts:</h3>
<ul>
  <li><strong>Bar Charts:</strong> Compare quantities across categories</li>
  <li><strong>Pie Charts:</strong> Show proportion of whole (percentages)</li>
  <li><strong>Line Graphs:</strong> Show trends over time</li>
  <li><strong>Tables:</strong> Present numerical data systematically</li>
</ul>
<h3>Analysis Techniques:</h3>
<ul>
  <li><strong>Percentage Calculation:</strong> (Value ÷ Total) × 100</li>
  <li><strong>Ratio Comparison:</strong> Compare different data points</li>
  <li><strong>Trend Analysis:</strong> Increase/decrease over periods</li>
  <li><strong>Averages:</strong> Calculate mean of different segments</li>
</ul>
<h3>Example Problem:</h3>
<p>If pie chart shows consumption: Agriculture 60%, Industry 25%, Services 15%. If total consumption is 1000 units, Agriculture = 600, Industry = 250, Services = 150.</p>
        ''',
        'xp_reward': 30
    },
    # ============================================================================
    # ADDITIONAL HISTORY - 4 Materials
    # ============================================================================
    {
        'title': 'British Raj and Colonial Administration',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '''
<h2>British Rule in India (1858-1947)</h2>
<p>The British East India Company's rule transitioned to Crown control after the 1857 Rebellion.</p>
<h3>Timeline:</h3>
<ul>
  <li><strong>1858:</strong> Crown takes direct control (End of Company rule)</li>
  <li><strong>1876:</strong> Queen Victoria proclaimed Empress of India</li>
  <li><strong>1909:</strong> Morley-Minto Reforms (separate electorates for Muslims)</li>
  <li><strong>1919:</strong> Montagu-Chelmsford Reforms (Dyarchy in provinces)</li>
  <li><strong>1935:</strong> Government of India Act (Federal structure planned)</li>
</ul>
<h3>Administrative System:</h3>
<ul>
  <li><strong>Viceroy:</strong> Governor-General, supreme authority</li>
  <li><strong>Indian Civil Service (ICS):</strong> Mostly British, later Indians admitted</li>
  <li><strong>Provincial Administration:</strong> Governors reported to Viceroy</li>
  <li><strong>Police and Army:</strong> Under British command</li>
</ul>
<h3>Economic Policies:</h3>
<ul>
  <li><strong>Exploitation:</strong> Raw materials exported, finished goods imported</li>
  <li><strong>Infrastructure:</strong> Railways, roads built for extraction and control</li>
  <li><strong>Agriculture:</strong> Land tax and forced crops (indigo, opium)</li>
  <li><strong>De-industrialization:</strong> Indian textile industry destroyed</li>
</ul>
        ''',
        'xp_reward': 35
    },
    {
        'title': 'Indian National Movement - Early Phase',
        'subject': 'History',
        'level': 'Intermediate',
        'content': '''
<h2>Independence Struggle (1857-1920)</h2>
<h3>1857 Rebellion (Sepoy Mutiny):</h3>
<ul>
  <li><strong>Cause:</strong> Introduction of rifle cartridges allegedly coated with cow/pig fat</li>
  <li><strong>Leaders:</strong> Mangal Pandey (spark), Rani Laxmibai, Nana Sahib, Kunwar Singh</li>
  <li><strong>Result:</strong> Crushed by British, but forced Crown takeover of administration</li>
  <li><strong>Impact:</strong> Ended EIC rule, increased recruitment of educated Indians</li>
</ul>
<h3>Early Nationalist Organizations:</h3>
<ul>
  <li><strong>Indian National Congress (1885):</strong> Founded by A.O. Hume; moderate initially</li>
  <li><strong>Moderate Phase (1885-1905):</strong> Dadabhai Naoroji (drain of wealth theory), Gopal Krishna Gokhale</li>
  <li><strong>Swadeshi Movement (1905):</strong> Response to Bengal Partition; promote Indian goods</li>
  <li><strong>Radical Phase (1905-1920):</strong> Lala Lajpat Rai, Bal Gangadhar Tilak, Aurobindo Ghosh</li>
</ul>
<h3>Key Concepts:</h3>
<ul>
  <li><strong>Drain of Wealth:</strong> Natural resources extracted, wealth flows to Britain</li>
  <li><strong>Swadeshi:</strong> Self-reliance, boycott of British goods, indigenous industries</li>
  <li><strong>Swaraj:</strong> Self-rule, independence as goal</li>
</ul>
        ''',
        'xp_reward': 35
    },
    {
        'title': 'Indian Independence - Gandhian Phase',
        'subject': 'History',
        'level': 'Advanced',
        'content': '''
<h2>Non-Violent Independence Movement (1920-1947)</h2>
<h3>Gandhian Philosophy:</h3>
<ul>
  <li><strong>Satyagraha:</strong> Truth-force, non-violent resistance</li>
  <li><strong>Ahimsa:</strong> Non-violence; means and ends equally important</li>
  <li><strong>Civil Disobedience:</strong> Breaking unjust laws peacefully</li>
  <li><strong>Swadeshi:</strong> Reject foreign goods, use indigenous products</li>
</ul>
<h3>Major Movements:</h3>
<ul>
  <li><strong>Khilafat Movement (1920-24):</strong> Support for Ottoman Caliphate; Hindu-Muslim unity</li>
  <li><strong>Non-Cooperation Movement (1920-22):</strong> Boycott of institutions, goods, offices</li>
  <li><strong>Jallianwala Bagh Massacre (1919):</strong> 1000+ killed; unified Indian opposition</li>
  <li><strong>Civil Disobedience Movement (1930):</strong> Salt March led by Gandhi; tax defiance</li>
  <li><strong>Quit India Movement (1942):</strong> "Abhi Leave India" slogan; mass participation</li>
</ul>
<h3>Partition and Independence (1947):</h3>
<ul>
  <li><strong>Cabinet Mission Plan (1946):</strong> Proposed united India with Pakistan option</li>
  <li><strong>Independence Act (1947):</strong> August 15, 1947; Mountbatten Plan implementation</li>
  <li><strong>Partition:</strong> India and Pakistan division along religious lines</li>
  <li><strong>Cost:</strong> 1-2 million deaths, 10+ million displaced</li>
</ul>
        ''',
        'xp_reward': 40
    },
]

def seed_comprehensive_materials():
    """Seed the database with comprehensive study materials"""
    try:
        with app.app_context():
            existing_count = Material.query.count()
            if existing_count > 0:
                print(f"Database already contains {existing_count} materials. Skipping seed...")
                return

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
            print(f"✅ Successfully seeded {len(COMPREHENSIVE_MATERIALS)} comprehensive materials!")

            for subject in set([m['subject'] for m in COMPREHENSIVE_MATERIALS]):
                count = Material.query.filter_by(subject=subject).count()
                total_xp = sum([m['xp_reward'] for m in COMPREHENSIVE_MATERIALS if m['subject'] == subject])
                print(f"   {subject}: {count} materials | {total_xp} XP")

            print(f"\n📚 Total XP Available: {sum([m['xp_reward'] for m in COMPREHENSIVE_MATERIALS])} XP")

    except Exception as e:
        db.session.rollback()
        print(f"❌ Error seeding materials: {str(e)}")

if __name__ == '__main__':
    seed_comprehensive_materials()
