from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sewa LEAD - Leadership, Education and Development</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a5e; line-height: 1.7; }

        /* Nav */
        nav { display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 2rem; background: #1a1a5e; position: sticky; top: 0; z-index: 100; }
        nav .logo { font-size: 1.3rem; font-weight: 700; color: #fff; letter-spacing: 1px; }
        nav .logo span { color: #f0a500; }
        nav ul { list-style: none; display: flex; gap: 1.5rem; }
        nav a { text-decoration: none; color: rgba(255,255,255,0.85); font-weight: 500; font-size: 0.9rem; transition: color 0.2s; }
        nav a:hover { color: #f0a500; }
        .nav-toggle { display: none; background: none; border: none; color: #fff; font-size: 1.5rem; cursor: pointer; }

        /* Hero */
        .hero { background: linear-gradient(135deg, #1a1a5e 0%, #2d2d8a 100%); color: #fff; text-align: center; padding: 5rem 2rem 4rem; position: relative; overflow: hidden; }
        .hero::after { content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 6px; background: linear-gradient(90deg, #f0a500, #f5c842, #f0a500); }
        .hero .badge { display: inline-block; background: rgba(240,165,0,0.15); border: 1px solid rgba(240,165,0,0.4); color: #f5c842; padding: 0.4rem 1.2rem; border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem; letter-spacing: 1px; }
        .hero h1 { font-size: 3.2rem; margin-bottom: 0.5rem; }
        .hero h1 .highlight { color: #f0a500; }
        .hero .subtitle { font-size: 1.4rem; font-weight: 300; opacity: 0.9; margin-bottom: 0.5rem; }
        .hero .tagline { font-size: 1.1rem; opacity: 0.7; margin-bottom: 2.5rem; max-width: 650px; margin-left: auto; margin-right: auto; }
        .hero .cta-group { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
        .btn-primary { display: inline-block; padding: 0.8rem 2rem; background: #f0a500; color: #1a1a5e; border-radius: 8px; text-decoration: none; font-weight: 700; transition: transform 0.2s, box-shadow 0.2s; }
        .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(240,165,0,0.4); }
        .btn-secondary { display: inline-block; padding: 0.8rem 2rem; background: transparent; color: #fff; border: 2px solid rgba(255,255,255,0.4); border-radius: 8px; text-decoration: none; font-weight: 600; transition: border-color 0.2s; }
        .btn-secondary:hover { border-color: #f0a500; color: #f0a500; }

        /* Section base */
        section { padding: 4.5rem 2rem; }
        .container { max-width: 1100px; margin: 0 auto; }
        .section-label { display: inline-block; background: #f0a500; color: #1a1a5e; padding: 0.3rem 1rem; border-radius: 4px; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 1rem; }
        .section-title { font-size: 2.2rem; margin-bottom: 1rem; color: #1a1a5e; }
        .section-subtitle { color: #475569; font-size: 1.05rem; max-width: 700px; margin-bottom: 3rem; }
        .text-center { text-align: center; }
        .text-center .section-subtitle { margin-left: auto; margin-right: auto; }

        /* About */
        .about { background: #f0f6ff; }
        .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; }
        .about-text p { color: #334155; margin-bottom: 1rem; font-size: 1.05rem; }
        .about-stats { display: flex; gap: 2rem; margin-top: 2rem; }
        .stat { text-align: center; }
        .stat .num { font-size: 2rem; font-weight: 800; color: #1a1a5e; }
        .stat .label { font-size: 0.8rem; color: #64748b; text-transform: uppercase; letter-spacing: 1px; }
        .about-visual { background: linear-gradient(135deg, #e8f0fe, #dbeafe); border-radius: 16px; padding: 3rem 2rem; text-align: center; }
        .about-visual .lead-icon { font-size: 1.2rem; letter-spacing: 8px; font-weight: 800; color: #1a1a5e; margin-bottom: 1rem; }
        .about-visual .lead-icon span { color: #f0a500; }
        .about-visual .lead-meaning { display: flex; flex-direction: column; gap: 0.75rem; text-align: left; padding-left: 1rem; }
        .about-visual .lead-meaning div { display: flex; align-items: center; gap: 0.75rem; font-size: 1.05rem; font-weight: 600; color: #1a1a5e; }
        .about-visual .lead-meaning .letter { width: 36px; height: 36px; background: #1a1a5e; color: #f0a500; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; font-weight: 800; flex-shrink: 0; }

        /* Purpose */
        .purpose-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
        .purpose-card { background: #fff; border-radius: 12px; padding: 2rem; border-left: 4px solid #f0a500; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }
        .purpose-card .icon { font-size: 2rem; margin-bottom: 1rem; }
        .purpose-card h3 { font-size: 1.15rem; margin-bottom: 0.5rem; color: #1a1a5e; }
        .purpose-card p { color: #475569; font-size: 0.95rem; }

        /* Program Structure */
        .structure { background: #1a1a5e; color: #fff; }
        .structure .section-label { background: #f0a500; color: #1a1a5e; }
        .structure .section-title { color: #fff; }
        .structure .section-subtitle { color: rgba(255,255,255,0.7); }
        .levels { display: flex; flex-direction: column; gap: 0; max-width: 800px; margin: 0 auto; }
        .level { display: flex; align-items: stretch; position: relative; }
        .level-marker { width: 60px; display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }
        .level-dot { width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.9rem; flex-shrink: 0; }
        .level-line { flex: 1; width: 3px; background: rgba(255,255,255,0.2); }
        .level-content { flex: 1; padding: 0.5rem 0 2rem 1.5rem; }
        .level-content h3 { font-size: 1.1rem; margin-bottom: 0.3rem; }
        .level-content .award { font-size: 0.85rem; opacity: 0.7; margin-bottom: 0.4rem; }
        .level-content p { font-size: 0.9rem; opacity: 0.8; }
        .level-bronze .level-dot { background: #cd7f32; color: #fff; }
        .level-silver .level-dot { background: #c0c0c0; color: #1a1a5e; }
        .level-gold .level-dot { background: #f0a500; color: #1a1a5e; }
        .level-platinum .level-dot { background: linear-gradient(135deg, #e5e4e2, #fff); color: #1a1a5e; }

        /* Benefits */
        .benefits { background: #f8fafc; }
        .benefits-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; }
        .benefit { background: #fff; border-radius: 10px; padding: 1.5rem; text-align: center; transition: box-shadow 0.2s, transform 0.2s; border: 1px solid #e2e8f0; }
        .benefit:hover { box-shadow: 0 8px 24px rgba(26,26,94,0.1); transform: translateY(-3px); }
        .benefit .icon { width: 48px; height: 48px; background: #eef2ff; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin: 0 auto 1rem; }
        .benefit h3 { font-size: 0.95rem; margin-bottom: 0.4rem; color: #1a1a5e; }
        .benefit p { color: #64748b; font-size: 0.85rem; }

        /* Program Details */
        .details-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; }
        .detail-card { background: #fff; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
        .detail-card h3 { font-size: 1rem; color: #1a1a5e; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem; }
        .detail-card p, .detail-card li { color: #475569; font-size: 0.9rem; }
        .detail-card ul { padding-left: 1.2rem; }
        .detail-card li { margin-bottom: 0.3rem; }

        /* Awards */
        .awards { background: linear-gradient(180deg, #f0f6ff, #fff); }
        .awards-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
        .award-card { text-align: center; padding: 2rem 1.5rem; border-radius: 12px; background: #fff; border: 2px solid #e2e8f0; transition: border-color 0.2s; }
        .award-card:hover { border-color: #f0a500; }
        .award-card .medal { font-size: 3rem; margin-bottom: 1rem; }
        .award-card h3 { font-size: 1.1rem; color: #1a1a5e; margin-bottom: 0.3rem; }
        .award-card .year { font-size: 0.85rem; color: #f0a500; font-weight: 700; margin-bottom: 0.5rem; }
        .award-card p { color: #64748b; font-size: 0.85rem; }

        /* Chapters */
        .chapters { background: #1a1a5e; color: #fff; }
        .chapters .section-label { background: #f0a500; color: #1a1a5e; }
        .chapters .section-title { color: #fff; }
        .chapters .section-subtitle { color: rgba(255,255,255,0.7); }
        .chapters-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }
        .chapter { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12); border-radius: 10px; padding: 1.25rem; text-align: center; transition: background 0.2s, transform 0.2s; cursor: default; }
        .chapter:hover { background: rgba(240,165,0,0.12); transform: translateY(-2px); }
        .chapter .region { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #f0a500; margin-bottom: 0.3rem; }
        .chapter h3 { font-size: 1rem; color: #fff; }

        /* Timeline */
        .timeline-bar { display: flex; gap: 0; border-radius: 12px; overflow: hidden; margin-top: 2rem; }
        .timeline-phase { flex: 1; padding: 1.5rem 1rem; text-align: center; }
        .timeline-phase h4 { font-size: 0.9rem; margin-bottom: 0.3rem; }
        .timeline-phase p { font-size: 0.8rem; opacity: 0.85; }
        .phase-1 { background: #1a1a5e; color: #fff; }
        .phase-2 { background: #2d2d8a; color: #fff; }
        .phase-3 { background: #f0a500; color: #1a1a5e; }
        .phase-4 { background: #f5c842; color: #1a1a5e; }

        /* Activities */
        .activities { background: #fff8ee; }
        .activities-categories { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
        .activity-category { background: #fff; border-radius: 12px; padding: 1.75rem; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }
        .activity-category .cat-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.25rem; padding-bottom: 0.75rem; border-bottom: 3px solid #f0a500; }
        .activity-category .cat-icon { width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; flex-shrink: 0; }
        .activity-category h3 { font-size: 1.05rem; color: #1a1a5e; }
        .activity-list { list-style: none; display: flex; flex-direction: column; gap: 0.6rem; }
        .activity-list li { display: flex; align-items: center; gap: 0.6rem; color: #334155; font-size: 0.92rem; }
        .activity-list li::before { content: ''; width: 8px; height: 8px; background: #f0a500; border-radius: 50%; flex-shrink: 0; }
        .cat-green { background: #ecfdf5; }
        .cat-red { background: #fef2f2; }
        .cat-orange { background: #fff7ed; }
        .cat-blue { background: #eff6ff; }
        .cat-purple { background: #f5f3ff; }

        /* How to Help */
        .help-cards { display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap; margin-top: 2rem; }
        .help-card { background: #fff; border-radius: 12px; padding: 2rem 1.5rem; text-align: center; width: 240px; border: 2px solid #e2e8f0; transition: border-color 0.2s, transform 0.2s; }
        .help-card:hover { border-color: #f0a500; transform: translateY(-3px); }
        .help-card .help-icon { font-size: 2.5rem; margin-bottom: 0.75rem; }
        .help-card h3 { font-size: 1rem; color: #1a1a5e; margin-bottom: 0.4rem; }
        .help-card p { color: #64748b; font-size: 0.85rem; }

        /* CTA */
        .cta-section { background: linear-gradient(135deg, #f0a500, #f5c842); text-align: center; padding: 4rem 2rem; }
        .cta-section h2 { font-size: 2rem; color: #1a1a5e; margin-bottom: 1rem; }
        .cta-section p { color: #1a1a5e; opacity: 0.8; max-width: 600px; margin: 0 auto 2rem; font-size: 1.05rem; }
        .btn-dark { display: inline-block; padding: 0.8rem 2.5rem; background: #1a1a5e; color: #fff; border-radius: 8px; text-decoration: none; font-weight: 700; transition: transform 0.2s; }
        .btn-dark:hover { transform: translateY(-2px); }

        /* Footer */
        footer { background: #0f0f3d; color: rgba(255,255,255,0.6); padding: 2.5rem 2rem; }
        .footer-content { max-width: 1100px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
        .footer-links { display: flex; gap: 1.5rem; }
        .footer-links a { color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.9rem; }
        .footer-links a:hover { color: #f0a500; }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2rem; }
            .hero .subtitle { font-size: 1.1rem; }
            .about-grid { grid-template-columns: 1fr; }
            .awards-grid { grid-template-columns: 1fr; }
            nav ul { display: none; }
            .nav-toggle { display: block; }
            .about-stats { flex-wrap: wrap; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="logo">SEWA <span>LEAD</span></div>
        <button class="nav-toggle" aria-label="Menu">&#9776;</button>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#structure">Program</a></li>
            <li><a href="#benefits">Benefits</a></li>
            <li><a href="#activities">Activities</a></li>
            <li><a href="#awards">Awards</a></li>
            <li><a href="#chapters">Chapters</a></li>
            <li><a href="#join">Join</a></li>
        </ul>
    </nav>

    <!-- Hero -->
    <div class="hero">
        <div class="badge">SEWA INTERNATIONAL USA</div>
        <h1>Sewa <span class="highlight">LEAD</span> Program</h1>
        <div class="subtitle">Leadership, Education and Development</div>
        <p class="tagline">A youth development program empowering high school students to serve their communities, build leadership skills, and experience the joy of giving.</p>
        <div class="cta-group">
            <a href="#join" class="btn-primary">Join LEAD</a>
            <a href="#structure" class="btn-secondary">Explore the Program</a>
        </div>
    </div>

    <!-- About LEAD -->
    <section class="about" id="about">
        <div class="container">
            <div class="about-grid">
                <div class="about-text">
                    <div class="section-label">About</div>
                    <h2 class="section-title">What is Sewa LEAD?</h2>
                    <p>LEAD is Sewa International's Youth Development Program for high school students. It provides a platform for participants to serve the greater community and experience the joy of selfless service.</p>
                    <p>The program introduces socially conscious leadership in young people, combining impactful in-person experiences with structured online learning through local Sewa chapters.</p>
                    <p>Delivered in a hybrid format, local chapters host speaker series, chapter meetings, and hands-on service projects, while nationally curated online courses run through Sewa Academy and the National Youth Conference.</p>
                    <div class="about-stats">
                        <div class="stat"><div class="num">4</div><div class="label">Year Program</div></div>
                        <div class="stat"><div class="num">100+</div><div class="label">Hours / Year</div></div>
                        <div class="stat"><div class="num">4</div><div class="label">Award Levels</div></div>
                    </div>
                </div>
                <div class="about-visual">
                    <div class="lead-icon">L<span>E</span>AD</div>
                    <div class="lead-meaning">
                        <div><span class="letter">L</span> Leadership</div>
                        <div><span class="letter" style="background:#f0a500;color:#1a1a5e;">E</span> Education</div>
                        <div><span class="letter">A</span> And</div>
                        <div><span class="letter">D</span> Development</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Purpose -->
    <section id="purpose">
        <div class="container">
            <div class="text-center">
                <div class="section-label">Purpose</div>
                <h2 class="section-title">Why Sewa LEAD?</h2>
                <p class="section-subtitle">Building the next generation of service-minded leaders through community engagement, mentorship, and hands-on experience.</p>
            </div>
            <div class="purpose-grid">
                <div class="purpose-card">
                    <div class="icon">&#129309;</div>
                    <h3>Serve the Community</h3>
                    <p>Provides a platform for participants to serve the greater community and experience the joy of giving through hands-on service projects.</p>
                </div>
                <div class="purpose-card">
                    <div class="icon">&#127891;</div>
                    <h3>Socially Conscious Leadership</h3>
                    <p>Introduces socially conscious leadership in youngsters, cultivating civic awareness and a service-oriented mindset.</p>
                </div>
                <div class="purpose-card">
                    <div class="icon">&#128218;</div>
                    <h3>Hybrid Learning</h3>
                    <p>Combines in-person chapter experiences with nationally curated online courses through Sewa Academy on the Zoho LMS platform.</p>
                </div>
                <div class="purpose-card">
                    <div class="icon">&#129504;</div>
                    <h3>College-Ready Skills</h3>
                    <p>Develops critical thinking, responsibility, time management, public speaking, and planning skills valuable for college and beyond.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Program Structure -->
    <section class="structure" id="structure">
        <div class="container">
            <div class="text-center">
                <div class="section-label">Program Structure</div>
                <h2 class="section-title">4-Year Graduation Pathway</h2>
                <p class="section-subtitle">Students progress through four levels, each building on the last. Entry starts at Level 1. Minimum 100 hours per year for the Sewa National Presidential Award. Pass score requires minimum 75 hours.</p>
            </div>
            <div class="levels">
                <div class="level level-bronze">
                    <div class="level-marker"><div class="level-dot">1</div><div class="level-line"></div></div>
                    <div class="level-content">
                        <h3>Level 1: Bronze</h3>
                        <div class="award">Volunteer Service Award &middot; Bronze Pin</div>
                        <p>Ready to LEAD (RTL) Course &mdash; Introduction to service, community engagement fundamentals, and Sewa values.</p>
                    </div>
                </div>
                <div class="level level-silver">
                    <div class="level-marker"><div class="level-dot">2</div><div class="level-line"></div></div>
                    <div class="level-content">
                        <h3>Level 2: Silver</h3>
                        <div class="award">Volunteer Service Learning Award &middot; Silver Pin</div>
                        <p>Design To LEAD (DTL) Course &mdash; Service learning with mandatory project completion. Deeper engagement with community initiatives.</p>
                    </div>
                </div>
                <div class="level level-gold">
                    <div class="level-marker"><div class="level-dot">3</div><div class="level-line"></div></div>
                    <div class="level-content">
                        <h3>Level 3: Gold</h3>
                        <div class="award">Volunteer Service Learning Leadership Award &middot; Gold Medal</div>
                        <p>VANI &mdash; The Sewa LEADership Course. LEAD Graduation, DTL Mentor, Team Leader. Certificate is cumulative accomplishment of three years.</p>
                    </div>
                </div>
                <div class="level level-platinum">
                    <div class="level-marker"><div class="level-dot">4</div><div class="level-line"></div></div>
                    <div class="level-content">
                        <h3>Level 4: Platinum</h3>
                        <div class="award">National Service Leadership Excellence Award</div>
                        <p>National Youth Council membership. National-level planning and execution. Graduates become part of national leadership.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Benefits -->
    <section class="benefits" id="benefits">
        <div class="container">
            <div class="text-center">
                <div class="section-label">Benefits</div>
                <h2 class="section-title">What Participants Gain</h2>
                <p class="section-subtitle">LEAD develops well-rounded leaders through service, learning, and community engagement.</p>
            </div>
            <div class="benefits-grid">
                <div class="benefit">
                    <div class="icon">&#127793;</div>
                    <h3>Personal Growth</h3>
                    <p>Well-rounded development through service and reflection</p>
                </div>
                <div class="benefit">
                    <div class="icon">&#128101;</div>
                    <h3>Community Leaders</h3>
                    <p>Engage with socially responsible community leaders</p>
                </div>
                <div class="benefit">
                    <div class="icon">&#128149;</div>
                    <h3>Self Upliftment</h3>
                    <p>Self upliftment through selfless service to others</p>
                </div>
                <div class="benefit">
                    <div class="icon">&#127908;</div>
                    <h3>New Competencies</h3>
                    <p>Public speaking, time management, planning, fundraising</p>
                </div>
                <div class="benefit">
                    <div class="icon">&#128161;</div>
                    <h3>Innovation</h3>
                    <p>Innovation and problem solving through real-world projects</p>
                </div>
                <div class="benefit">
                    <div class="icon">&#129309;</div>
                    <h3>Peer Relationships</h3>
                    <p>Strengthening peer relationships and building networks</p>
                </div>
                <div class="benefit">
                    <div class="icon">&#127760;</div>
                    <h3>Community Impact</h3>
                    <p>Contribute to community initiatives and Sewa projects</p>
                </div>
                <div class="benefit">
                    <div class="icon">&#127942;</div>
                    <h3>Service Recognition</h3>
                    <p>Service hours recognition with awards and certificates</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Awards -->
    <section class="awards" id="awards">
        <div class="container">
            <div class="text-center">
                <div class="section-label">Recognition</div>
                <h2 class="section-title">Awards &amp; Certificates</h2>
                <p class="section-subtitle">Sewa Pins and Certificates are awarded upon completing 100 service hours each fiscal year. Minimum 75 hours required to remain eligible for the next level.</p>
            </div>
            <div class="awards-grid">
                <div class="award-card">
                    <div class="medal" style="color:#cd7f32;">&#127941;</div>
                    <div class="year">Year 1</div>
                    <h3>Bronze Pin</h3>
                    <p>Volunteer Service Award for dedicated participation and community service.</p>
                </div>
                <div class="award-card">
                    <div class="medal" style="color:#c0c0c0;">&#127941;</div>
                    <div class="year">Year 2</div>
                    <h3>Silver Pin</h3>
                    <p>Volunteer Service Learning Award for service with reflection and learning.</p>
                </div>
                <div class="award-card">
                    <div class="medal" style="color:#f0a500;">&#127942;</div>
                    <div class="year">Year 3</div>
                    <h3>Gold Medal</h3>
                    <p>Volunteer Service Learning Leadership Award. LEAD Graduation Certificate for cumulative accomplishment.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Program Details -->
    <section id="details">
        <div class="container">
            <div class="text-center">
                <div class="section-label">Details</div>
                <h2 class="section-title">Program Guidelines</h2>
                <p class="section-subtitle">Everything you need to know about eligibility, timeline, and enrollment.</p>
            </div>
            <div class="details-grid">
                <div class="detail-card">
                    <h3>&#9989; Eligibility</h3>
                    <ul>
                        <li>Current 8th, 9th, 10th, 11th, and 12th graders</li>
                        <li>All statuses welcome (Citizenship, PR, H1B, etc.)</li>
                        <li>Equal opportunity for all racial, ethnic, religious, and gender backgrounds</li>
                        <li>Must enter from Level 1</li>
                    </ul>
                </div>
                <div class="detail-card">
                    <h3>&#128197; Timeline</h3>
                    <ul>
                        <li>Program runs October 1 to August 31 (school year cycle)</li>
                        <li>Online courses: January 23 through March 14</li>
                        <li>Self-paced project phase: April - July</li>
                        <li>National Youth Conference in July</li>
                    </ul>
                </div>
                <div class="detail-card">
                    <h3>&#128176; Registration</h3>
                    <ul>
                        <li>$150 flat registration fee per year</li>
                        <li>Centralized enrollment for all chapters</li>
                        <li>Students and parents must commit to program rules</li>
                        <li>20 minimum hours of parent commitment required</li>
                    </ul>
                </div>
                <div class="detail-card">
                    <h3>&#9200; Hours Requirements</h3>
                    <ul>
                        <li>100 hours minimum for Sewa National Presidential Award</li>
                        <li>75 hours minimum to pass and advance</li>
                        <li>Non-service hours capped at 20 for didactic sessions</li>
                        <li>Unlimited service hours during implementation phase</li>
                    </ul>
                </div>
                <div class="detail-card">
                    <h3>&#128104;&#8205;&#127891; Mentorship</h3>
                    <ul>
                        <li>Teams of 4-5 students, each with an adult mentor</li>
                        <li>Weekly live Zoom classes on weekends</li>
                        <li>Mentor guides learning through breakout rooms</li>
                        <li>Project mentorship during self-paced phase</li>
                    </ul>
                </div>
                <div class="detail-card">
                    <h3>&#127891; Graduation</h3>
                    <ul>
                        <li>3-year progressive program to graduate</li>
                        <li>Achieve criteria at each level to advance</li>
                        <li>LEAD Graduation Certificate and Gold Medal at Level 3</li>
                        <li>Graduates can join Level 4 national leadership</li>
                    </ul>
                </div>
            </div>

            <!-- Timeline visual -->
            <div class="timeline-bar">
                <div class="timeline-phase phase-1">
                    <h4>Oct - Dec</h4>
                    <p>Chapter Onboarding &amp; Service</p>
                </div>
                <div class="timeline-phase phase-2">
                    <h4>Jan - Mar</h4>
                    <p>Online Learning Modules</p>
                </div>
                <div class="timeline-phase phase-3">
                    <h4>Apr - Jul</h4>
                    <p>Project &amp; Implementation</p>
                </div>
                <div class="timeline-phase phase-4">
                    <h4>Jul - Aug</h4>
                    <p>Conference &amp; Awards</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Service Activities -->
    <section class="activities" id="activities">
        <div class="container">
            <div class="text-center">
                <div class="section-label">Service Activities</div>
                <h2 class="section-title">What LEADs Do at Chapters</h2>
                <p class="section-subtitle">Each Sewa chapter organizes hands-on service projects across these focus areas. Here's a glimpse of the activities LEADs participate in.</p>
            </div>
            <div class="activities-categories">
                <div class="activity-category">
                    <div class="cat-header">
                        <div class="cat-icon cat-green">&#127795;</div>
                        <h3>Community Service &amp; Environment</h3>
                    </div>
                    <ul class="activity-list">
                        <li>Highway &amp; Neighborhood Cleanup</li>
                        <li>Walkathons &amp; Save Soil Initiatives</li>
                        <li>Invasive Plant Removal</li>
                        <li>Park Restoration &amp; Tree Planting</li>
                        <li>Community Garden Projects</li>
                    </ul>
                </div>
                <div class="activity-category">
                    <div class="cat-header">
                        <div class="cat-icon cat-orange">&#127858;</div>
                        <h3>Hunger Relief &amp; Basic Needs</h3>
                    </div>
                    <ul class="activity-list">
                        <li>Food Service &amp; Meal Preparation</li>
                        <li>Food Bank Volunteering (Forgotten Harvest)</li>
                        <li>Thrift Store Assistance</li>
                        <li>Burrito Sewa &amp; Sandwich Making Drives</li>
                        <li>Providing Food &amp; Supplies to Families</li>
                    </ul>
                </div>
                <div class="activity-category">
                    <div class="cat-header">
                        <div class="cat-icon cat-red">&#129657;</div>
                        <h3>Health &amp; Wellness</h3>
                    </div>
                    <ul class="activity-list">
                        <li>Blood Drives</li>
                        <li>Doctors for Sewa</li>
                        <li>Senior Support &amp; Elder Care</li>
                        <li>Health Camps &amp; Awareness</li>
                        <li>Mental Health &amp; Wellness Workshops</li>
                    </ul>
                </div>
                <div class="activity-category">
                    <div class="cat-header">
                        <div class="cat-icon cat-blue">&#128218;</div>
                        <h3>Education &amp; Youth Programs</h3>
                    </div>
                    <ul class="activity-list">
                        <li>ASPIRE Tutoring for Underserved Students</li>
                        <li>Gift Wrapping for Hospitals</li>
                        <li>Speaker Series &amp; Workshop Hosting</li>
                        <li>Sewa Academy Online Courses</li>
                        <li>National Youth Conference</li>
                    </ul>
                </div>
                <div class="activity-category">
                    <div class="cat-header">
                        <div class="cat-icon cat-purple">&#127760;</div>
                        <h3>Social Causes &mdash; Local &amp; Global</h3>
                    </div>
                    <ul class="activity-list">
                        <li>Aid in Times of Crisis &amp; Disaster Relief</li>
                        <li>Empower Students Through Education</li>
                        <li>Protect the Environment</li>
                        <li>Fundraising &amp; Awareness Campaigns</li>
                        <li>Civic Engagement &amp; Community Building</li>
                    </ul>
                </div>
                <div class="activity-category">
                    <div class="cat-header">
                        <div class="cat-icon" style="background:#fef3c7;">&#129309;</div>
                        <h3>How You Can Help</h3>
                    </div>
                    <ul class="activity-list">
                        <li>Volunteer your time at chapter events</li>
                        <li>Become a parent mentor (4-5 student team)</li>
                        <li>Make a tax-deductible donation</li>
                        <li>Spread the word in your community</li>
                        <li>Host or sponsor a service event</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Chapters -->
    <section class="chapters" id="chapters">
        <div class="container">
            <div class="text-center">
                <div class="section-label">Chapters</div>
                <h2 class="section-title">Find Your Local Chapter</h2>
                <p class="section-subtitle">LEAD operates through local Sewa chapters across the country. Each chapter hosts speaker series, meetings, and hands-on service projects.</p>
            </div>
            <div class="chapters-grid">
                <div class="chapter"><div class="region">Northeast</div><h3>New Jersey</h3></div>
                <div class="chapter"><div class="region">Northeast</div><h3>New York</h3></div>
                <div class="chapter"><div class="region">Northeast</div><h3>Connecticut</h3></div>
                <div class="chapter"><div class="region">Southeast</div><h3>Atlanta</h3></div>
                <div class="chapter"><div class="region">Southeast</div><h3>Charlotte</h3></div>
                <div class="chapter"><div class="region">Southeast</div><h3>Tampa</h3></div>
                <div class="chapter"><div class="region">South</div><h3>Dallas</h3></div>
                <div class="chapter"><div class="region">South</div><h3>Houston</h3></div>
                <div class="chapter"><div class="region">South</div><h3>Austin</h3></div>
                <div class="chapter"><div class="region">Midwest</div><h3>Chicago</h3></div>
                <div class="chapter"><div class="region">Midwest</div><h3>Detroit</h3></div>
                <div class="chapter"><div class="region">Midwest</div><h3>Columbus</h3></div>
                <div class="chapter"><div class="region">West</div><h3>Bay Area</h3></div>
                <div class="chapter"><div class="region">West</div><h3>Los Angeles</h3></div>
                <div class="chapter"><div class="region">West</div><h3>Seattle</h3></div>
                <div class="chapter"><div class="region">West</div><h3>Phoenix</h3></div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="cta-section" id="join">
        <h2>Ready to Lead Through Service?</h2>
        <p>Join thousands of high school students across America who are building leadership skills, serving their communities, and making a difference through Sewa LEAD.</p>
        <a href="https://www.sewausa.org/Lead" class="btn-dark" target="_blank">Register Now</a>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div>Sewa LEAD &middot; Sewa International USA &middot; Pathways to Serve Through Leadership</div>
            <div class="footer-links">
                <a href="https://www.sewausa.org/Lead" target="_blank">sewausa.org/Lead</a>
                <a href="mailto:lead@sewausa.org">lead@sewausa.org</a>
            </div>
        </div>
    </footer>

</body>
</html>
"""
