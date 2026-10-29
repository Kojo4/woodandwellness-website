"""Builds the four site pages from shared parts. Run: python3 tools/build_pages.py
Photos are free Unsplash images (Unsplash licence), loaded from images.unsplash.com.
They are illustrative stock photos, not photos of Wood and Wellness learners."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def u(pid, w=900, h=None):
    q = f"https://images.unsplash.com/{pid}?auto=format&fit=crop&w={w}&q=72"
    return q + (f"&h={h}" if h else "")


P = {
    "smile_bench": "photo-1687422810663-c316494f725a",
    "phone_shop": "photo-1687422811062-a966b55cb217",
    "weave": "photo-1688240817677-d28b8e232dd4",
    "bench_work": "photo-1733186718279-0936826f09a0",
    "machine_hands": "photo-1726912005253-7ff8a31428e9",
    "ground_work": "photo-1698768196149-bb0d8990ab78",
    "branch_smile": "photo-1615829949748-dbece8ce2e5c",
    "curly_lean": "photo-1754774674824-1530f7e46176",
    "plane_wood": "photo-1721508490082-2c32c0abf8dd",
    "studio_man": "photo-1612299065617-f883adb67bd1",
    "studio_woman": "photo-1612300330496-9616c05e06aa",
    "chisel_hands": "photo-1679797850019-3d0d8659a695",
    "chisel_close": "photo-1497219055242-93359eeed651",
    "vest_hat": "photo-1729843823577-40db41a5e8c9",
    "hardhat_wall": "photo-1621905252507-b35492cc74b4",
    "hardhat_hold": "photo-1621905252472-943afaa20e20",
    "trowel": "photo-1704005445445-2747074be8ac",
    "bricks_cement": "photo-1701850009190-2859ba2aeea6",
    "blocks_yellow": "photo-1617720356637-6264c1c0b4bb",
    "printers_row": "photo-1611117775350-ac3950990985",
    "printer_orange": "photo-1758435170505-e9b2772348c1",
    "woman_smile": "photo-1669752348267-367cc9f34138",
    "workshop_table": "photo-1590880795696-20c7dfadacde",
}

FONTS = (
    '<link rel="preconnect" href="https://api.fontshare.com">\n'
    '<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=switzer@400,500,600&display=swap">\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&display=swap">\n'
)

NAV = [("index.html", "Home"), ("schools.html", "Schools"), ("community.html", "Community"), ("store.html", "Store")]


def head(title, desc, page):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://woodandwellness.org/assets/og.png">
<meta property="og:type" content="website">
<meta name="theme-color" content="#F1EEE9">
<link rel="icon" href="assets/og.png">
{FONTS}<link rel="stylesheet" href="assets/css/noho.css">
</head>
<body data-page="{page}">
<a class="sr" href="#main">Skip to content</a>
<header class="top gut">
  <a class="mark" href="index.html" aria-label="Wood and Wellness home"><b>wood</b><i>&amp;</i><b>wellness</b></a>
  <button class="menu-btn" type="button" id="menu-open" aria-controls="drawer" aria-expanded="false" aria-label="Open menu">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
  </button>
</header>
<div class="drawer gut" id="drawer" hidden>
  <div class="drawer-head">
    <a class="mark" href="index.html"><b>wood</b><i>&amp;</i><b>wellness</b></a>
    <button class="menu-btn" type="button" id="menu-close" aria-label="Close menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <nav aria-label="Main">
{''.join(f'    <a href="{h}"' + (' aria-current="page"' if h.startswith(page) else '') + f'>{n}</a>{chr(10)}' for h, n in NAV)}  </nav>
  <div class="drawer-foot small"><span>info@woodandwellness.org</span><a href="https://www.instagram.com/wood_n_wellness/" rel="noopener">Instagram</a><a href="index.html#contact">Get in touch</a></div>
</div>
<main id="main">
"""


FOOT = """</main>
<footer class="foot">
  <div class="foot-grid gut">
    <div>
      <h4>Get in touch</h4>
      <p class="h-md" style="max-width:16ch">Bring the workshop to your learners.</p>
      <p class="small soft" style="margin-top:14px">info@woodandwellness.org</p>
    </div>
    <div><h4>Explore</h4><ul><li><a href="schools.html">Schools and SEND</a></li><li><a href="community.html">Community and youth justice</a></li><li><a href="store.html">The Store</a></li></ul></div>
    <div><h4>About</h4><ul><li><a href="index.html#standards">Safety and standards</a></li><li><a href="index.html#about">Who we are</a></li><li><a href="index.html#faq">FAQ</a></li></ul></div>
    <div><h4>Follow</h4><ul><li><a href="https://www.instagram.com/wood_n_wellness/" rel="noopener">Instagram</a></li></ul></div>
  </div>
  <div class="gut"><div class="foot-legal"><p>Wood and Wellness Limited, company number 17403376, 124 City Road, London EC1V 2NX.</p><p>Funded and community programmes are delivered by Wood and Wellness CIC.</p></div></div>
  <div class="foot-word gut" aria-hidden="true">wood&amp;wellness</div>
</footer>
<script>
(function(){
  var d=document.getElementById('drawer'),o=document.getElementById('menu-open'),c=document.getElementById('menu-close');
  function set(v){d.hidden=!v;o.setAttribute('aria-expanded',v);document.body.style.overflow=v?'hidden':'';if(v)c.focus();else o.focus();}
  o.addEventListener('click',function(){set(true)});c.addEventListener('click',function(){set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!d.hidden)set(false)});
  var f=document.getElementById('enquiry');if(!f)return;
  f.addEventListener('submit',function(e){e.preventDefault();
    var g=function(n){return (f.elements[n]&&f.elements[n].value)||''};
    var body='Name: '+g('name')+'\\nOrganisation: '+g('organisation')+'\\nEmail: '+g('email')+'\\nEnquiry: '+g('type')+'\\n\\n'+g('message');
    window.location.href='mailto:info@woodandwellness.org?subject='+encodeURIComponent('Website enquiry: '+g('type'))+'&body='+encodeURIComponent(body);
    document.getElementById('formnote').textContent='Your email app should open with your message ready. If it does not, email info@woodandwellness.org.';});
  var b=document.getElementById('copy-email');if(b)b.addEventListener('click',function(){
    var t='info@woodandwellness.org';var done=function(){b.textContent='Copied'};
    if(navigator.clipboard)navigator.clipboard.writeText(t).then(done,function(){});});
})();
</script>
</body>
</html>
"""


def tile(key, colour, alt, w=420):
    return f'<div class="tile t-{colour}"><img src="{u(P[key], w, int(w*1.25))}" alt="{alt}" loading="eager"></div>'


def chip(key, alt):
    return f'<span class="chip"><img src="{u(P[key], 160, 110)}" alt="{alt}"></span>'


CONTACT = """
<section class="contact" id="contact">
  <div class="contact-grid gut">
    <div>
      <h2 class="h-lg">Bring the workshop to your learners</h2>
      <p class="soft" style="margin-top:20px;max-width:40ch;font-size:17px">Tell us about your setting and we will come back within two working days with a suggested programme.</p>
      <div class="copyline"><code>info@woodandwellness.org</code><button class="btn btn-light" type="button" id="copy-email">Copy email</button></div>
    </div>
    <form class="form" id="enquiry" novalidate>
      <label for="f-name">Your name<input id="f-name" name="name" required autocomplete="name"></label>
      <label for="f-org">Organisation<input id="f-org" name="organisation" autocomplete="organization"></label>
      <label class="full" for="f-email">Email<input id="f-email" name="email" type="email" required autocomplete="email"></label>
      <label class="full" for="f-type">I am enquiring about<select id="f-type" name="type"><option>School or SEND setting</option><option>Youth justice</option><option>Adult or community</option><option>Partnership or sponsorship</option><option>The Store</option><option>Something else</option></select></label>
      <label class="full" for="f-msg">Message<textarea id="f-msg" name="message" rows="4"></textarea></label>
      <div class="full"><button class="btn btn-dark" type="submit">Send enquiry</button><p id="formnote" class="small soft" style="margin-top:10px">Pressing send opens your email app with your message ready to go.</p></div>
    </form>
  </div>
</section>
"""

# ---------------------------------------------------------------- HOME
HOME = head("Wood and Wellness", "Hands on construction and product design programmes for schools, SEND settings, youth justice and adult learners across London. Traditional craft, modern tools, measured outcomes.", "index") + f"""
<section class="hero">
  <div class="hero-copy gut">
    <div>
      <h1 class="h-xl">We teach traditional craft with modern tools, so learners make real progress</h1>
      <p class="lead">Accredited carpentry, bricklaying, plumbing, electrical and digital making for schools, SEND settings, youth justice and adult learners across London.</p>
      <div class="hero-actions"><a class="btn btn-dark" href="#contact">Book a call</a><a class="btn btn-light" href="#programmes">See programmes</a></div>
    </div>
    <p class="small">Construction and product design education, London</p>
  </div>
  <div class="hero-media">
    <div class="mosaic">
      {tile('smile_bench','mustard','Woodworker smiling at his bench')}
      {tile('hardhat_hold','clay','Builder holding a yellow hard hat')}
      <div class="gap"></div><div class="gap"></div>
      <div class="gap"></div>
      {tile('woman_smile','lilac','Maker smiling in a workshop')}
      {tile('branch_smile','olive','Young man smiling with a length of timber')}
      {tile('curly_lean','mustard','Woman leaning on a workbench, laughing')}
      {tile('hardhat_wall','sage','Builder in a hard hat beside a brick wall')}
      {tile('bench_work','sky','Craftsman working wood on a bench')}
    </div>
  </div>
</section>

<section class="statement gut">
  <p>Learners cut every joint by hand {chip('chisel_close','Chisel cutting into timber')} then again with handheld CNC {chip('machine_hands','Hands guiding wood through a machine')} and 3D printed jigs {chip('printer_orange','A 3D printer on a workbench')}, and decide which a real workshop should use</p>
</section>

<section class="panels" id="programmes">
  <article class="panel a gut">
    <p class="panel-tag">For schools and SEND settings</p>
    <div class="panel-img"><img src="{u(P['bricks_cement'], 900, 1125)}" alt="Hands laying a brick on fresh mortar"></div>
    <div class="panel-bar">
      <div><p class="small soft">Six week accredited blocks</p><h2 class="h-md">Your construction department, ready to run</h2></div>
      <div class="btns"><a class="btn btn-light" href="schools.html">Learn more</a><a class="btn btn-dark" href="#contact">Book</a></div>
    </div>
  </article>
  <article class="panel b gut">
    <p class="panel-tag">For youth justice and communities</p>
    <div class="panel-img"><img src="{u(P['ground_work'], 900, 1125)}" alt="Maker shaping a piece of wood"></div>
    <div class="panel-bar">
      <div><p class="small soft">Small groups, real products</p><h2 class="h-md">Making as wellbeing, and a way into work</h2></div>
      <div class="btns"><a class="btn btn-light" href="community.html">Learn more</a><a class="btn btn-dark" href="#contact">Partner</a></div>
    </div>
  </article>
</section>

<section class="sec gut" id="standards">
  <div class="sec-head"><h2 class="h-lg">Safe to say yes to</h2><p>Schools, councils and funders need to know practical work is properly managed. This sits behind every session.</p></div>
  <div class="rows">
    <div class="row"><span class="k">Insurance</span><span class="v">£5m public liability</span><span class="d">Plus £10m employer's liability.</span></div>
    <div class="row"><span class="k">People</span><span class="v">Enhanced DBS for every tutor</span><span class="d">With child and adult safeguarding training.</span></div>
    <div class="row"><span class="k">Planning</span><span class="v">Risk assessed, tool by tool</span><span class="d">Written for each trade, each tool and each venue before work begins.</span></div>
    <div class="row"><span class="k">Recognition</span><span class="v">ASDAN and AQA Unit Awards</span><span class="d">Every learner can gain credit for what they make.</span></div>
  </div>
  <p class="small soft" style="margin-top:20px">Safeguarding policy, insurance certificates and risk assessments are available on request.</p>
</section>

<section class="sec gut" style="padding-top:0">
  <div class="sec-head"><h2 class="h-lg">Six weeks, start to finish</h2><p>Every block runs ready to go, with tutors, materials, safety and accreditation handled by us.</p></div>
  <ol class="steps">
    <li class="step"><span class="n">Week 0</span><img src="{u(P['studio_woman'], 700, 467)}" alt="Planning at a workshop table"><h3 class="h-sm">Plan</h3><p>We review EHCPs with our occupational therapist and set each learner's goals.</p></li>
    <li class="step"><span class="n">Weeks 1 to 5</span><img src="{u(P['chisel_hands'], 700, 467)}" alt="Hands cutting a joint"><h3 class="h-sm">Build</h3><p>Weekly sessions with a specialist tutor, all tools, materials and PPE supplied.</p></li>
    <li class="step"><span class="n">Site day</span><img src="{u(P['blocks_yellow'], 700, 467)}" alt="Builder laying blocks on site"><h3 class="h-sm">Visit</h3><p>A day on a live building site to see the trade at full scale.</p></li>
    <li class="step"><span class="n">Week 6</span><img src="{u(P['studio_man'], 700, 467)}" alt="Maker smiling in a studio"><h3 class="h-sm">Show</h3><p>A showcase for families and staff, certificates, and a report for every learner.</p></li>
  </ol>
</section>

<section class="sec gut" style="padding-top:0">
  <div class="sec-head"><h2 class="h-lg">Evidence, not just a nice afternoon</h2><p>An occupational therapist assesses every learner at the start and end of each block. Schools get progress reports mapped to EHCP outcomes, ready for annual reviews.</p></div>
  <ul class="cards">
    <li class="card"><p class="small soft">Measured</p><h3 class="h-sm">Fine motor skills</h3><p>Grip, precision and tool control.</p></li>
    <li class="card"><p class="small soft">Measured</p><h3 class="h-sm">Gross motor skills</h3><p>Lifting, posture and coordination.</p></li>
    <li class="card"><p class="small soft">Measured</p><h3 class="h-sm">Motor planning</h3><p>Sequencing a task from start to finish.</p></li>
    <li class="card"><p class="small soft">Measured</p><h3 class="h-sm">Bilateral coordination</h3><p>Using both hands together on a tool.</p></li>
    <li class="card"><p class="small soft">Measured</p><h3 class="h-sm">Sensory regulation</h3><p>Noise, texture and focus in a working space.</p></li>
    <li class="card"><p class="small soft">Measured</p><h3 class="h-sm">Confidence and teamwork</h3><p>Roles, reflection and pride in work.</p></li>
  </ul>
</section>

<section class="about" id="about">
  <div class="gut">
    <div class="about-top"><img src="{u(P['workshop_table'], 300, 300)}" alt="Tools laid out on a workshop table"><p><b>Kojo Sarpong</b><br>Founder and Director</p><p>Wood and Wellness began with a simple idea: making things with your hands is good for you. It started as peer support for fathers and grew into accredited programmes across London.</p></div>
    <p class="h-md">Making as wellbeing, and as a way into work</p>
  </div>
  <div class="gut">
    <div class="about-top"><img src="{u(P['plane_wood'], 300, 300)}" alt="Hands working a piece of timber"><p><b>Two organisations</b><br>One team</p><p>Wood and Wellness CIC runs funded and community programmes. Wood and Wellness Limited holds our contracts with schools.</p></div>
    <p class="h-md">Real trade skills without building a department from scratch</p>
  </div>
</section>

<section class="sec gut">
  <h2 class="h-lg" style="margin-bottom:clamp(36px,5vw,64px)">Track record</h2>
  <div class="biglist">
    <div class="grp"><h3>Delivery</h3><ul><li><span>Enfield Council Summer University</span><span>2 summers</span></li><li><span>Young people aged 11 to 25 reached</span><span>100+</span></li><li><span>Impact reports delivered to the council</span><span>2</span></li></ul></div>
    <div class="grp"><h3>Accreditation</h3><ul><li><span>ASDAN short courses</span><span>Mapped</span></li><li><span>AQA Unit Award Scheme</span><span>Mapped</span></li><li><span>Pearson BTEC units under a school's approval</span><span>Available</span></li></ul></div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <h2 class="h-lg gut" style="margin-bottom:clamp(36px,5vw,64px)">The trades</h2>
  <div class="stack gut">
    <a class="story" href="schools.html#trades" style="text-decoration:none"><h3 class="h-md">Carpentry and joinery</h3><p>Measuring, marking and cutting joints by hand, then with 3D printed jigs and handheld CNC.</p><img src="{u(P['chisel_close'], 800, 450)}" alt="Chisel cutting timber"><div class="meta"><span>Six weeks</span><span>Learn more</span></div></a>
    <a class="story" href="schools.html#trades" style="text-decoration:none"><h3 class="h-md">Bricklaying</h3><p>Setting out, mixing and laying to a line, checked with spirit levels and laser lines.</p><img src="{u(P['trowel'], 800, 450)}" alt="Trowel on a brick wall"><div class="meta"><span>Six weeks</span><span>Learn more</span></div></a>
    <a class="story" href="schools.html#trades" style="text-decoration:none"><h3 class="h-md">Plumbing</h3><p>Cutting, bending and joining pipe, compression and push fit fittings, and leak testing on practice rigs.</p><div class="meta" style="margin-top:auto"><span>Six weeks</span><span>Learn more</span></div></a>
    <a class="story" href="schools.html#trades" style="text-decoration:none"><h3 class="h-md">Electrical</h3><p>Circuits, switches and safe wiring practice on low voltage training boards.</p><div class="meta" style="margin-top:auto"><span>Six weeks</span><span>Learn more</span></div></a>
    <a class="story" href="schools.html#trades" style="text-decoration:none"><h3 class="h-md">3D printing and digital making</h3><p>Designing in Tinkercad and combining printed parts with timber to make lamps and coat stands.</p><img src="{u(P['printers_row'], 800, 450)}" alt="A row of 3D printers"><div class="meta"><span>Six weeks</span><span>Learn more</span></div></a>
  </div>
</section>

<section class="sec gut" id="faq" style="padding-top:0">
  <div class="faq">
    <h2 class="h-lg">FAQ</h2>
    <div>
      <details><summary>How big are the groups?</summary><p>Small, so every learner gets time on the tools. We agree numbers with you based on your learners' needs and the space.</p></details>
      <details><summary>Who delivers the sessions?</summary><p>A specialist tutor for each trade, supported by our occupational therapist. Everyone holds an enhanced DBS check and has child and adult safeguarding training.</p></details>
      <details><summary>Is it safe for learners with complex needs?</summary><p>Yes. Every tool and task has a written risk assessment, sessions are planned around each EHCP, and electrical work uses low voltage boards.</p></details>
      <details><summary>How much does a block cost?</summary><p>Every setting is different, so we quote for your learners and the trades you choose. Get in touch and we will send a suggested programme within two working days.</p></details>
    </div>
  </div>
</section>
""" + CONTACT + FOOT

# ---------------------------------------------------------------- SCHOOLS
SCHOOLS = head("Schools and SEND | Wood and Wellness", "Construction blocks for independent and specialist schools: carpentry, bricklaying, plumbing, electrical and digital making, built around each EHCP and measured by an occupational therapist.", "schools") + f"""
<section class="intro gut">
  <h1 class="h-xl" style="max-width:14ch">Your construction department, ready to run</h1>
  <p>We plan, staff, equip and accredit practical trade blocks for independent and specialist schools, so your learners get real construction skills without you recruiting a tutor for every trade.</p>
  <ul class="tags"><li>14 to 19 and post 16</li><li>Built around each EHCP</li><li>OT measured progress</li><li>Accredited units</li></ul>
</section>
<img class="wide-img" src="{u(P['hardhat_wall'], 1800, 770)}" alt="Builder in a hard hat beside a brick wall">

<section class="sec" id="trades">
  <div class="sec-head gut"><h2 class="h-lg">Five blocks, one provider</h2><p>Each trade runs as its own six week block. Book one to start, or build a full year of construction with us. Most schools start with carpentry and add a trade each half term.</p></div>
  <div class="stack gut">
    <div class="story"><h3 class="h-md">Carpentry and joinery</h3><p>Measuring, marking and cutting joints by hand, then with 3D printed jigs and handheld CNC. Learners leave with a finished piece they designed.</p><img src="{u(P['chisel_hands'], 800, 450)}" alt="Hands cutting a joint"></div>
    <div class="story"><h3 class="h-md">Bricklaying</h3><p>Setting out, mixing and laying to a line, checked with spirit levels and laser lines. Brick bays can be built on site as a joinery project.</p><img src="{u(P['bricks_cement'], 800, 450)}" alt="Laying bricks on mortar"></div>
    <div class="story"><h3 class="h-md">Plumbing</h3><p>Cutting, bending and joining pipe, compression and push fit fittings, and testing for leaks on practice rigs.</p></div>
    <div class="story"><h3 class="h-md">Electrical</h3><p>Circuits, switches and safe wiring practice on low voltage training boards, with every finished item inspected and tested by a competent adult.</p></div>
    <div class="story"><h3 class="h-md">3D printing and digital making</h3><p>Designing in Tinkercad, printing parts and combining them with timber to make real products, such as lamps and coat stands.</p><img src="{u(P['printer_orange'], 800, 450)}" alt="A 3D printer on a workbench"></div>
  </div>
</section>

<section class="sec gut" id="ehcp" style="padding-top:0">
  <div class="sec-head"><h2 class="h-lg">Progress your SENCO can use</h2><p>An occupational therapist works alongside our tutors. Every learner is assessed at the start and end of the block, so you see measured change, not just attendance.</p></div>
  <ol class="steps" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
    <li class="step"><span class="n">Before week one</span><h3 class="h-sm">We read the EHCPs</h3><p>The OT reviews each plan with your team and sets practical goals for every learner.</p></li>
    <li class="step"><span class="n">Every session</span><h3 class="h-sm">We measure in the workshop</h3><p>Fine and gross motor skills, motor planning, coordination, sensory regulation, confidence and teamwork.</p></li>
    <li class="step"><span class="n">End of block</span><h3 class="h-sm">You get a report per learner</h3><p>Progress mapped to EHCP outcomes and ready for annual reviews, plus portfolio evidence for accreditation.</p></li>
  </ol>
</section>

<section class="panels">
  <article class="panel a gut">
    <p class="panel-tag">What is included</p>
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding-block:32px">
      <h2 class="h-lg" style="max-width:12ch;margin-bottom:28px">One booking covers it all</h2>
      <ul class="inc"><li>Specialist tutor for every session</li><li>Occupational therapist assessment and reports</li><li>All tools, materials and PPE</li><li>Risk assessments for every trade and tool</li><li>Session plans and portfolio evidence</li><li>A day on a live building site</li><li>Showcase for families and staff</li><li>Certificates for every learner</li></ul>
    </div>
  </article>
  <article class="panel b gut">
    <p class="panel-tag">Starting from scratch</p>
    <div class="panel-img"><img src="{u(P['workshop_table'], 900, 1125)}" alt="A workshop table with tools"></div>
    <div class="panel-bar"><div><p class="small soft">No workshop yet?</p><h2 class="h-md">We can build the space as well as teach in it</h2></div><div class="btns"><a class="btn btn-dark" href="#contact">Talk it through</a></div></div>
  </article>
</section>

<section class="sec gut">
  <h2 class="h-lg" style="margin-bottom:clamp(36px,5vw,64px)">Accreditation</h2>
  <div class="biglist">
    <div class="grp"><h3>Recognised achievement</h3><ul><li><span>ASDAN short courses</span><span>Mapped</span></li><li><span>AQA Unit Award Scheme</span><span>Mapped</span></li><li><span>Pearson BTEC construction units, under your centre's approval</span><span>Available</span></li></ul></div>
  </div>
</section>

<section class="sec gut" style="padding-top:0">
  <div class="faq">
    <h2 class="h-lg">What schools ask us</h2>
    <div>
      <details><summary>How big are the groups?</summary><p>Small, so every learner gets time on the tools. We agree numbers with you based on your learners' needs and the space.</p></details>
      <details><summary>Who delivers the sessions?</summary><p>A specialist tutor for each trade, supported by our occupational therapist. Everyone holds an enhanced DBS check and has child and adult safeguarding training.</p></details>
      <details><summary>Is it safe for learners with complex needs?</summary><p>Yes. Every tool and task has a written risk assessment, sessions are planned around each EHCP, and electrical work uses low voltage boards. Nothing is plugged in until it has been inspected and tested.</p></details>
      <details><summary>How much does a block cost?</summary><p>Every school is different, so we quote for your setting, your learners and the trades you choose. Get in touch and we will send a suggested programme within two working days.</p></details>
    </div>
  </div>
</section>
""" + CONTACT + FOOT

# ---------------------------------------------------------------- COMMUNITY
COMMUNITY = head("Community and youth justice | Wood and Wellness", "Wood and Wellness CIC runs making programmes for young people, youth justice services and adult learners across London.", "community") + f"""
<section class="hero">
  <div class="hero-copy gut">
    <div>
      <h1 class="h-xl">People arrive unsure. They leave having made something.</h1>
      <p class="lead">Our community interest company runs making programmes for young people, youth justice services and adult learners across London, and helps the people who want to keep going turn a skill into work.</p>
      <div class="hero-actions"><a class="btn btn-dark" href="#contact">Partner with us</a><a class="btn btn-light" href="#track">Our track record</a></div>
    </div>
    <p class="small">Wood and Wellness CIC</p>
  </div>
  <div class="hero-media">
    <div class="mosaic">
      {tile('weave','olive','Hands weaving a frame')}
      {tile('phone_shop','mustard','Woodworker smiling in his shop')}
      <div class="gap"></div><div class="gap"></div>
      <div class="gap"></div>
      {tile('curly_lean','clay','Woman laughing at a workbench')}
      {tile('ground_work','sky','Maker shaping wood')}
      {tile('woman_smile','sage','Maker smiling')}
    </div>
  </div>
</section>

<section class="sec gut" id="track">
  <div class="sec-head"><h2 class="h-lg">Enfield Council Summer University</h2><p>For two summers back to back, we delivered making workshops for more than 100 young people aged 11 to 25, including young people with special educational needs. Each year ended with documented outcomes and an impact report for the council.</p></div>
  <div class="rows">
    <div class="row"><span class="k">Young people</span><span class="v">100+</span><span class="d">Aged 11 to 25.</span></div>
    <div class="row"><span class="k">Years running</span><span class="v">2</span><span class="d">Back to back summers.</span></div>
    <div class="row"><span class="k">Impact reports</span><span class="v">2</span><span class="d">Delivered to Enfield Council.</span></div>
  </div>
</section>

<section class="panels">
  <article class="panel a gut" id="youth-justice">
    <p class="panel-tag">Youth justice</p>
    <div class="panel-img"><img src="{u(P['branch_smile'], 900, 1125)}" alt="Young man smiling with timber"></div>
    <div class="panel-bar"><div><p class="small soft">Small groups, accredited units, a route on</p><h2 class="h-md">Focus, skills and something real to show</h2></div><div class="btns"><a class="btn btn-dark" href="#contact">Talk to us</a></div></div>
  </article>
  <article class="panel b gut" id="adult">
    <p class="panel-tag">Adult and community</p>
    <div class="panel-img"><img src="{u(P['bench_work'], 900, 1125)}" alt="Craftsman working at a bench"></div>
    <div class="panel-bar"><div><p class="small soft">Beginner friendly, mobile kit, a finished product</p><h2 class="h-md">Learn a skill, feel the difference</h2></div><div class="btns"><a class="btn btn-dark" href="#contact">Book a course</a></div></div>
  </article>
</section>

<section class="sec gut">
  <div class="sec-head"><h2 class="h-lg">From learner to maker</h2><p>Making is good for wellbeing. It can also be a first step into work. Our pathway takes people from their first session to selling what they make.</p></div>
  <ol class="steps">
    <li class="step"><span class="n">Stage 1</span><h3 class="h-sm">Learn</h3><p>Practical sessions with traditional and modern tools.</p></li>
    <li class="step"><span class="n">Stage 2</span><h3 class="h-sm">Make</h3><p>Design and build finished products worth keeping.</p></li>
    <li class="step"><span class="n">Stage 3</span><h3 class="h-sm">Sell</h3><p>Selected pieces go on sale in the Wood and Wellness Store.</p></li>
    <li class="step"><span class="n">Stage 4</span><h3 class="h-sm">Grow</h3><p>Social media marketing and selling skills to build a maker business.</p></li>
  </ol>
</section>

<section class="sec gut" style="padding-top:0">
  <h2 class="h-lg" style="margin-bottom:clamp(36px,5vw,64px)">Work with us</h2>
  <div class="biglist">
    <div class="grp"><h3>Commissioners</h3><ul><li><span>Councils, youth justice services and alternative provision teams who need accredited provision with evidence of impact</span><span></span></li></ul></div>
    <div class="grp"><h3>Funders</h3><ul><li><span>Trusts and foundations backing skills, wellbeing and routes into work, with measured outcomes in every report</span><span></span></li></ul></div>
    <div class="grp"><h3>Tool partners</h3><ul><li><span>Makers of modern tools who want young people learning on their kit, with case studies from real sessions</span><span></span></li></ul></div>
  </div>
</section>
""" + CONTACT + FOOT

# ---------------------------------------------------------------- STORE
LAMP_SVG = """<svg viewBox="0 0 500 560" style="width:min(80%,420px)" aria-hidden="true">
  <defs><radialGradient id="glow" cx="50%" cy="44%" r="52%"><stop offset="0" stop-color="#FFF4DD" stop-opacity=".95"/><stop offset=".5" stop-color="#F1DDB5" stop-opacity=".4"/><stop offset="1" stop-color="#C8B8A4" stop-opacity="0"/></radialGradient>
  <linearGradient id="shell" x1="0" x2="1"><stop offset="0" stop-color="#F3E9D8"/><stop offset=".5" stop-color="#FFFBF3"/><stop offset="1" stop-color="#EADCC4"/></linearGradient></defs>
  <circle cx="250" cy="250" r="240" fill="url(#glow)"/>
  <path d="M250 70c70 0 112 70 112 150 0 92-50 170-112 170S138 312 138 220c0-80 42-150 112-150z" fill="url(#shell)"/>
  <g stroke="#D9C49E" stroke-width="1.4" fill="none" opacity=".8"><path d="M150 140c60 18 140 18 200 0"/><path d="M140 175c70 20 150 20 220 0"/><path d="M138 210c70 20 154 20 224 0"/><path d="M139 245c70 20 152 20 222 0"/><path d="M143 280c66 20 148 20 214 0"/><path d="M152 315c60 18 136 18 196 0"/><path d="M168 348c50 14 114 14 164 0"/></g>
  <rect x="200" y="388" width="100" height="22" rx="4" fill="#8A7A66"/><rect x="160" y="410" width="180" height="14" rx="4" fill="#6E6152"/>
</svg>"""

STORE = head("The Store | Wood and Wellness", "Pieces designed and made in our London workshop. Every sale helps fund making programmes for young people and adults.", "store") + f"""
<section class="intro gut">
  <p class="small soft" style="font-size:13px">The Wood and Wellness Store, opening soon</p>
  <h1 class="h-xl" style="max-width:13ch">Made in our workshop. Funding the next maker.</h1>
  <p>Pieces designed and made in our London workshop, and in time by makers from our programmes. Every sale helps fund making programmes for young people and adults across London.</p>
</section>

<section class="feature">
  <div class="feature-media">{LAMP_SVG}</div>
  <div class="feature-copy gut">
    <p class="small soft">Studio Collection</p>
    <h2 class="h-lg">The Cocoon Lamp</h2>
    <p class="h-md">£49.90</p>
    <p class="soft" style="max-width:44ch;font-size:17px">A lamp about becoming. A silkworm spins almost a kilometre of silk around itself, and quietly, out of sight, everything changes. We sketched that shape again and again, then printed it layer by layer in plant based PLA. Switched on, it glows the way a cocoon does: soft, warm and protective.</p>
    <dl class="specs"><div><dt>Size</dt><dd>180 × 180 × 230 mm</dd></div><div><dt>Material</dt><dd>PLA, textured matt white</dd></div><div><dt>Light</dt><dd>LED base, USB powered</dd></div><div><dt>Made</dt><dd>Dispatched within 3 working days</dd></div></dl>
    <div class="hero-actions"><a class="btn btn-dark" href="index.html#contact">Tell me when it launches</a><a class="btn btn-light" href="https://www.instagram.com/wood_n_wellness/" rel="noopener">See it on Instagram</a></div>
  </div>
</section>

<section class="sec gut">
  <div class="sec-head"><h2 class="h-lg">Every piece has a purpose</h2><p>Buying for a school, an office or a gift? Ask us about larger orders and commissions.</p></div>
  <ul class="cards">
    <li class="card"><p class="small soft">Impact</p><h3 class="h-sm">Funds programmes</h3><p>Money from every sale goes back into making programmes for young people and adults.</p></li>
    <li class="card"><p class="small soft">Pathway</p><h3 class="h-sm">Showcases makers</h3><p>As our learners grow, the Store becomes a place to sell what they design and make.</p></li>
    <li class="card"><p class="small soft">Origin</p><h3 class="h-sm">Made in London</h3><p>Designed, printed and finished in our London workshop, with traditional craft and modern tools.</p></li>
  </ul>
</section>
""" + CONTACT + FOOT

for name, html in [("index.html", HOME), ("schools.html", SCHOOLS), ("community.html", COMMUNITY), ("store.html", STORE)]:
    (ROOT / name).write_text(html)
    print("wrote", name, len(html))
