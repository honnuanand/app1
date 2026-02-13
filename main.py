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
    <title>Sewa LEAD Detroit - Leadership, Education and Development</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a5e; line-height: 1.7; background: #fff; }
        img { max-width: 100%; display: block; }
        a { color: #1a1a5e; }

        /* ===== NAV ===== */
        nav { display: flex; justify-content: space-between; align-items: center; padding: 0 2rem; height: 64px; background: #1a1a5e; position: sticky; top: 0; z-index: 100; }
        nav .logo { font-size: 1.2rem; font-weight: 700; color: #fff; letter-spacing: 0.5px; }
        nav .logo span { color: #f0a500; }
        nav ul { list-style: none; display: flex; gap: 1.5rem; }
        nav a { text-decoration: none; color: rgba(255,255,255,0.8); font-weight: 500; font-size: 0.88rem; transition: color 0.2s; }
        nav a:hover { color: #f0a500; }

        /* ===== ANNOUNCEMENT BAR ===== */
        .announcement { background: #f0a500; color: #1a1a5e; text-align: center; padding: 0.6rem 2rem; font-size: 0.9rem; font-weight: 600; }
        .announcement a { color: #1a1a5e; text-decoration: underline; }

        /* ===== HERO ===== */
        .hero { position: relative; min-height: 520px; display: flex; align-items: center; background: linear-gradient(135deg, #1a1a5e 0%, #2d2d8a 50%, #1a1a5e 100%); overflow: hidden; }
        .hero-overlay { position: absolute; inset: 0; background: rgba(26,26,94,0.65); z-index: 1; }
        .hero-bg { position: absolute; inset: 0; background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 520"><rect fill="%231a1a5e" width="1440" height="520"/><circle cx="200" cy="400" r="300" fill="%23f0a500" opacity="0.05"/><circle cx="1200" cy="100" r="400" fill="%23f5c842" opacity="0.04"/></svg>') center/cover; }
        .hero-content { position: relative; z-index: 2; max-width: 700px; padding: 4rem 2rem 4rem 4rem; }
        .hero-content .chapter-badge { display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(240,165,0,0.2); border: 1px solid rgba(240,165,0,0.4); color: #f5c842; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 1.5rem; }
        .hero-content h1 { font-size: 3rem; color: #fff; line-height: 1.2; margin-bottom: 1rem; }
        .hero-content h1 .gold { color: #f0a500; }
        .hero-content p { font-size: 1.15rem; color: rgba(255,255,255,0.85); margin-bottom: 2rem; line-height: 1.8; }
        .hero-content .hero-actions { display: flex; gap: 1rem; flex-wrap: wrap; }
        .btn { display: inline-block; padding: 0.85rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 700; font-size: 0.95rem; transition: transform 0.2s, box-shadow 0.2s; border: none; cursor: pointer; }
        .btn-gold { background: #f0a500; color: #1a1a5e; }
        .btn-gold:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(240,165,0,0.4); }
        .btn-outline { background: transparent; color: #fff; border: 2px solid rgba(255,255,255,0.3); }
        .btn-outline:hover { border-color: #f0a500; color: #f0a500; }
        .hero-image { position: absolute; right: 0; top: 0; bottom: 0; width: 45%; z-index: 1; }
        .hero-image .placeholder { width: 100%; height: 100%; background: linear-gradient(135deg, rgba(240,165,0,0.15), rgba(26,26,94,0.3)); display: flex; align-items: center; justify-content: center; color: rgba(255,255,255,0.3); font-size: 0.9rem; text-align: center; padding: 2rem; }

        /* ===== SECTION UTILITIES ===== */
        section { padding: 5rem 2rem; }
        .container { max-width: 1100px; margin: 0 auto; }
        .section-header { margin-bottom: 3rem; }
        .section-header .label { display: inline-block; background: #f0a500; color: #1a1a5e; padding: 0.25rem 0.8rem; border-radius: 4px; font-size: 0.75rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 0.75rem; }
        .section-header h2 { font-size: 2.2rem; color: #1a1a5e; margin-bottom: 0.75rem; line-height: 1.3; }
        .section-header p { color: #475569; font-size: 1.05rem; max-width: 650px; line-height: 1.8; }
        .section-header.centered { text-align: center; }
        .section-header.centered p { margin-left: auto; margin-right: auto; }
        .divider { width: 60px; height: 4px; background: #f0a500; border-radius: 2px; margin: 1rem 0; }
        .section-header.centered .divider { margin: 1rem auto; }

        /* ===== ABOUT ===== */
        .about { background: #f8fafc; }
        .about-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
        .about-text h3 { font-size: 1.3rem; color: #1a1a5e; margin: 1.5rem 0 0.75rem; }
        .about-text h3:first-of-type { margin-top: 0; }
        .about-text p { color: #334155; font-size: 1rem; margin-bottom: 1rem; }
        .about-image { border-radius: 16px; overflow: hidden; background: linear-gradient(135deg, #e0e7ff, #dbeafe); aspect-ratio: 4/3; display: flex; align-items: center; justify-content: center; }
        .img-placeholder { width: 100%; height: 100%; min-height: 300px; background: linear-gradient(135deg, #eef2ff 0%, #dbeafe 100%); display: flex; flex-direction: column; align-items: center; justify-content: center; color: #94a3b8; font-size: 0.85rem; gap: 0.5rem; padding: 2rem; text-align: center; border: 2px dashed #cbd5e1; border-radius: 12px; }
        .img-placeholder .icon { font-size: 2rem; opacity: 0.5; }
        .about-stats-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-top: 3rem; }
        .stat-card { background: #fff; border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
        .stat-card .number { font-size: 2rem; font-weight: 800; color: #1a1a5e; }
        .stat-card .label { font-size: 0.8rem; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-top: 0.25rem; }

        /* ===== ANNOUNCEMENTS ===== */
        .announcements-list { display: flex; flex-direction: column; gap: 1.5rem; }
        .announcement-card { display: grid; grid-template-columns: 200px 1fr; gap: 2rem; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 12px rgba(0,0,0,0.06); transition: box-shadow 0.2s; }
        .announcement-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.1); }
        .announcement-card .card-image { background: linear-gradient(135deg, #eef2ff, #dbeafe); display: flex; align-items: center; justify-content: center; color: #94a3b8; font-size: 0.8rem; min-height: 160px; border: 2px dashed #cbd5e1; margin: 0.75rem; border-radius: 8px; text-align: center; padding: 1rem; }
        .announcement-card .card-body { padding: 1.5rem 1.5rem 1.5rem 0; }
        .announcement-card .date { font-size: 0.8rem; color: #f0a500; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; }
        .announcement-card h3 { font-size: 1.15rem; color: #1a1a5e; margin-bottom: 0.5rem; }
        .announcement-card p { color: #475569; font-size: 0.95rem; line-height: 1.7; }
        .announcement-card .read-more { display: inline-block; margin-top: 0.75rem; color: #1a1a5e; font-weight: 600; font-size: 0.9rem; text-decoration: none; }
        .announcement-card .read-more:hover { color: #f0a500; }

        /* ===== ACTIVITIES ===== */
        .activities { background: #f8fafc; }
        .activity-section { margin-bottom: 4rem; }
        .activity-section:last-child { margin-bottom: 0; }
        .activity-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; }
        .activity-layout.reverse { direction: rtl; }
        .activity-layout.reverse > * { direction: ltr; }
        .activity-text h3 { font-size: 1.5rem; color: #1a1a5e; margin-bottom: 0.75rem; }
        .activity-text p { color: #334155; font-size: 1rem; margin-bottom: 1rem; line-height: 1.8; }
        .activity-text ul { padding-left: 1.2rem; margin-bottom: 1rem; }
        .activity-text li { color: #334155; font-size: 0.95rem; margin-bottom: 0.4rem; }
        .activity-image { border-radius: 12px; overflow: hidden; aspect-ratio: 16/10; }

        /* ===== PROGRAM STRUCTURE ===== */
        .structure { background: #1a1a5e; color: #fff; }
        .structure .section-header h2 { color: #fff; }
        .structure .section-header p { color: rgba(255,255,255,0.7); }
        .structure .divider { background: #f0a500; }
        .pathway { max-width: 800px; margin: 0 auto; }
        .pathway-step { display: grid; grid-template-columns: 80px 1fr; gap: 1.5rem; margin-bottom: 2.5rem; position: relative; }
        .pathway-step::before { content: ''; position: absolute; left: 39px; top: 70px; bottom: -20px; width: 2px; background: rgba(255,255,255,0.15); }
        .pathway-step:last-child::before { display: none; }
        .step-badge { width: 80px; height: 80px; border-radius: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-weight: 800; flex-shrink: 0; }
        .step-badge .year { font-size: 0.65rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.8; }
        .step-badge .level { font-size: 1.5rem; }
        .badge-bronze { background: linear-gradient(135deg, #cd7f32, #a0622a); color: #fff; }
        .badge-silver { background: linear-gradient(135deg, #c0c0c0, #a8a8a8); color: #1a1a5e; }
        .badge-gold { background: linear-gradient(135deg, #f0a500, #d4920a); color: #1a1a5e; }
        .badge-platinum { background: linear-gradient(135deg, #e8e8e8, #fff); color: #1a1a5e; }
        .step-content h3 { font-size: 1.2rem; margin-bottom: 0.25rem; }
        .step-content .award-name { color: #f0a500; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.5rem; }
        .step-content p { color: rgba(255,255,255,0.75); font-size: 0.95rem; line-height: 1.7; }

        /* ===== GALLERY ===== */
        .gallery-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
        .gallery-grid .gallery-item { border-radius: 12px; overflow: hidden; aspect-ratio: 4/3; }
        .gallery-grid .gallery-item.tall { grid-row: span 2; aspect-ratio: auto; }

        /* ===== INVOLVEMENT ===== */
        .involvement { background: linear-gradient(135deg, #1a1a5e 0%, #2d2d8a 100%); color: #fff; }
        .involvement .section-header h2 { color: #fff; }
        .involvement .section-header p { color: rgba(255,255,255,0.7); }
        .involvement .divider { background: #f0a500; }
        .involve-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
        .involve-card { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 2.5rem 2rem; transition: background 0.2s, transform 0.2s; }
        .involve-card:hover { background: rgba(255,255,255,0.1); transform: translateY(-3px); }
        .involve-card .card-icon { font-size: 2.5rem; margin-bottom: 1.25rem; }
        .involve-card h3 { font-size: 1.15rem; margin-bottom: 0.75rem; }
        .involve-card p { color: rgba(255,255,255,0.7); font-size: 0.95rem; line-height: 1.7; }

        /* ===== DETAILS ===== */
        .details { background: #f8fafc; }
        .details-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
        .detail-block { background: #fff; border-radius: 12px; padding: 2rem; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
        .detail-block h3 { font-size: 1.1rem; color: #1a1a5e; margin-bottom: 1rem; padding-bottom: 0.75rem; border-bottom: 2px solid #f0a500; }
        .detail-block p { color: #334155; font-size: 0.95rem; margin-bottom: 0.75rem; line-height: 1.7; }
        .detail-block ul { padding-left: 1.2rem; }
        .detail-block li { color: #334155; font-size: 0.93rem; margin-bottom: 0.5rem; line-height: 1.6; }

        /* ===== CTA ===== */
        .cta-banner { background: #f0a500; padding: 4rem 2rem; text-align: center; }
        .cta-banner h2 { font-size: 2.2rem; color: #1a1a5e; margin-bottom: 1rem; }
        .cta-banner p { color: #1a1a5e; opacity: 0.8; max-width: 600px; margin: 0 auto 2rem; font-size: 1.05rem; line-height: 1.7; }
        .btn-dark { background: #1a1a5e; color: #fff; }
        .btn-dark:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(26,26,94,0.3); }

        /* ===== FOOTER ===== */
        footer { background: #0f0f3d; color: rgba(255,255,255,0.5); padding: 3rem 2rem; }
        .footer-grid { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 3rem; }
        .footer-grid h4 { color: #fff; font-size: 0.95rem; margin-bottom: 1rem; }
        .footer-grid p { font-size: 0.88rem; line-height: 1.7; }
        .footer-grid a { color: rgba(255,255,255,0.5); text-decoration: none; font-size: 0.88rem; }
        .footer-grid a:hover { color: #f0a500; }
        .footer-links { display: flex; flex-direction: column; gap: 0.6rem; }
        .footer-bottom { max-width: 1100px; margin: 2rem auto 0; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.8rem; text-align: center; }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 900px) {
            .about-layout, .activity-layout, .details-layout { grid-template-columns: 1fr; }
            .activity-layout.reverse { direction: ltr; }
            .hero-image { display: none; }
            .hero-content { padding: 3rem 2rem; max-width: 100%; }
            .hero h1 { font-size: 2.2rem; }
            .involve-grid { grid-template-columns: 1fr; }
            .gallery-grid { grid-template-columns: repeat(2, 1fr); }
            .gallery-grid .gallery-item.tall { grid-row: span 1; aspect-ratio: 4/3; }
            .about-stats-row { grid-template-columns: repeat(2, 1fr); }
            .footer-grid { grid-template-columns: 1fr; }
            .announcement-card { grid-template-columns: 1fr; }
            .announcement-card .card-image { margin: 0.75rem 0.75rem 0; min-height: 120px; }
            .announcement-card .card-body { padding: 1.25rem; }
            nav ul { display: none; }
        }
    </style>
</head>
<body>

    <!-- Nav -->
    <nav>
        <div class="logo">SEWA <span>LEAD</span> &middot; Detroit</div>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#news">News</a></li>
            <li><a href="#activities">Activities</a></li>
            <li><a href="#program">Program</a></li>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="#join">Get Involved</a></li>
        </ul>
    </nav>

    <!-- Announcement Bar -->
    <div class="announcement">
        Registration for 2025-2026 LEAD year is now open! Online courses start January 23rd. <a href="https://www.sewausa.org/Lead">Register here &rarr;</a>
    </div>

    <!-- Hero -->
    <div class="hero">
        <div class="hero-bg"></div>
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <div class="chapter-badge">Sewa International USA &middot; Detroit Chapter</div>
            <h1>Pathways to Serve Through <span class="gold">Leadership</span></h1>
            <p>Sewa LEAD is a youth development program for high school students. We empower the next generation to serve their communities, develop leadership skills, and become socially conscious citizens &mdash; right here in Metro Detroit.</p>
            <div class="hero-actions">
                <a href="https://www.sewausa.org/Lead" class="btn btn-gold" target="_blank">Register for LEAD</a>
                <a href="#activities" class="btn btn-outline">See What We Do</a>
            </div>
        </div>
        <div class="hero-image">
            <div class="placeholder">
                <div style="font-size:2rem;margin-bottom:0.5rem;">&#128247;</div>
                Chapter hero photo<br>
                <em style="font-size:0.8rem;">e.g., group photo of LEADs in yellow shirts at a service event</em>
            </div>
        </div>
    </div>

    <!-- About -->
    <section class="about" id="about">
        <div class="container">
            <div class="about-layout">
                <div class="about-text">
                    <div class="section-header">
                        <div class="label">About LEAD</div>
                        <h2>Leadership, Education<br>and Development</h2>
                        <div class="divider"></div>
                    </div>
                    <p>LEAD is Sewa International's flagship youth development program. It's a 4-year volunteer service-learning leadership graduation program designed for high school students in grades 8 through 12. The Detroit chapter brings together students from across Metro Detroit to learn, serve, and grow as leaders.</p>

                    <h3>Our Purpose</h3>
                    <p>We provide a platform for young people to serve the greater community and experience the joy of giving. Through hands-on service projects, structured online learning, and mentorship from dedicated parent volunteers, LEAD introduces socially conscious leadership to the next generation.</p>

                    <h3>How It Works</h3>
                    <p>The program is delivered in a hybrid format. Our Detroit chapter hosts monthly speaker series, chapter meetings, and community service projects throughout the year. Students also participate in nationally curated online courses through Sewa Academy from January through March, and attend the National Youth Conference each July.</p>
                </div>
                <div class="about-image">
                    <div class="img-placeholder">
                        <div class="icon">&#128247;</div>
                        Chapter photo<br>
                        <em>e.g., LEADs at a chapter meeting or service event</em>
                    </div>
                </div>
            </div>
            <div class="about-stats-row">
                <div class="stat-card">
                    <div class="number">4</div>
                    <div class="label">Year Program</div>
                </div>
                <div class="stat-card">
                    <div class="number">100+</div>
                    <div class="label">Service Hours / Year</div>
                </div>
                <div class="stat-card">
                    <div class="number">$150</div>
                    <div class="label">Annual Registration</div>
                </div>
                <div class="stat-card">
                    <div class="number">Oct-Aug</div>
                    <div class="label">Program Cycle</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Announcements -->
    <section id="news">
        <div class="container">
            <div class="section-header">
                <div class="label">Announcements</div>
                <h2>Latest News &amp; Updates</h2>
                <div class="divider"></div>
                <p>Stay informed about upcoming events, registration deadlines, and chapter activities.</p>
            </div>
            <div class="announcements-list">
                <div class="announcement-card">
                    <div class="card-image">
                        <div>&#128247;<br>Event photo</div>
                    </div>
                    <div class="card-body">
                        <div class="date">January 2026</div>
                        <h3>Online Learning Modules Begin January 23rd</h3>
                        <p>All LEAD online courses will kick off the weekend of January 23rd and run through March 14th. Courses are hosted on Zoom with live classes, and quizzes and homework are available on Sewa Academy (Zoho LMS). There will be a break during Presidents Day weekend. Mentors and students should ensure WhatsApp groups are set up for each team.</p>
                        <a href="#" class="read-more">Learn more &rarr;</a>
                    </div>
                </div>
                <div class="announcement-card">
                    <div class="card-image">
                        <div>&#128247;<br>Service event photo</div>
                    </div>
                    <div class="card-body">
                        <div class="date">Upcoming</div>
                        <h3>Forgotten Harvest Food Bank Service Day</h3>
                        <p>Join your fellow LEADs for our next Forgotten Harvest food bank volunteering session. We'll be sorting and packing food donations for families across Metro Detroit. Parents are welcome to join &mdash; remember, 20 hours of parent participation is part of the program commitment. Please RSVP through your team WhatsApp group.</p>
                        <a href="#" class="read-more">RSVP now &rarr;</a>
                    </div>
                </div>
                <div class="announcement-card">
                    <div class="card-image">
                        <div>&#128247;<br>Award ceremony photo</div>
                    </div>
                    <div class="card-body">
                        <div class="date">Registration Open</div>
                        <h3>2025-2026 LEAD Registration Now Open</h3>
                        <p>New and returning students can now register for the upcoming LEAD year. The program is open to all 8th through 12th graders regardless of citizenship status. Registration fee is $150 per year. Students must enter at Level 1 (Bronze) and progress through the levels each year. Visit sewausa.org/Lead to complete your registration.</p>
                        <a href="https://www.sewausa.org/Lead" class="read-more" target="_blank">Register &rarr;</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Service Activities -->
    <section class="activities" id="activities">
        <div class="container">
            <div class="section-header centered">
                <div class="label">What We Do</div>
                <h2>Service Activities &amp; Community Impact</h2>
                <div class="divider"></div>
                <p>Our Detroit chapter LEADs participate in a wide range of hands-on service projects throughout the year. Here's how we make a difference in our community.</p>
            </div>

            <!-- Activity 1 -->
            <div class="activity-section">
                <div class="activity-layout">
                    <div class="activity-text">
                        <h3>Community Service &amp; Environment</h3>
                        <p>Our LEADs roll up their sleeves to keep Metro Detroit clean and green. From highway and neighborhood cleanups to invasive plant removal at local parks, students learn the value of environmental stewardship through direct action.</p>
                        <ul>
                            <li><strong>Highway &amp; Neighborhood Cleanup</strong> &mdash; Regular cleanup drives along adopted highway stretches and local neighborhoods</li>
                            <li><strong>Walkathons &amp; Save Soil Initiatives</strong> &mdash; Organized awareness walks and soil conservation projects</li>
                            <li><strong>Invasive Plant Removal</strong> &mdash; Partnering with local parks to restore native habitats</li>
                            <li><strong>Community Garden Projects</strong> &mdash; Planting and maintaining gardens that benefit local families</li>
                        </ul>
                    </div>
                    <div class="activity-image">
                        <div class="img-placeholder">
                            <div class="icon">&#127795;</div>
                            Photo: LEADs doing cleanup or gardening<br>
                            <em>e.g., students in yellow shirts planting or cleaning up</em>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Activity 2 -->
            <div class="activity-section">
                <div class="activity-layout reverse">
                    <div class="activity-text">
                        <h3>Hunger Relief &amp; Basic Needs</h3>
                        <p>Fighting hunger is at the heart of our chapter's service work. Our students regularly volunteer at food banks, prepare and serve meals for those in need, and organize supply drives for local families facing hardship.</p>
                        <ul>
                            <li><strong>Food Service &amp; Meal Preparation</strong> &mdash; Preparing hundreds of meals including our signature Burrito Sewa sandwich-making drives</li>
                            <li><strong>Forgotten Harvest</strong> &mdash; Volunteering at Metro Detroit's leading food rescue organization</li>
                            <li><strong>Thrift Store Assistance</strong> &mdash; Helping sort, organize, and serve at local thrift stores</li>
                            <li><strong>Family Support Drives</strong> &mdash; Collecting and distributing food, clothing, and supplies to families in need</li>
                        </ul>
                    </div>
                    <div class="activity-image">
                        <div class="img-placeholder">
                            <div class="icon">&#127858;</div>
                            Photo: LEADs at food bank or meal prep<br>
                            <em>e.g., students making sandwiches or at Forgotten Harvest</em>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Activity 3 -->
            <div class="activity-section">
                <div class="activity-layout">
                    <div class="activity-text">
                        <h3>Health &amp; Wellness</h3>
                        <p>Our LEADs support community health through blood drives, wellness events, and senior care programs. These activities connect students with healthcare professionals and teach the importance of giving back to vulnerable populations.</p>
                        <ul>
                            <li><strong>Blood Drives</strong> &mdash; Organizing and supporting community blood donation events</li>
                            <li><strong>Doctors for Sewa</strong> &mdash; Assisting at free health camps and wellness screenings</li>
                            <li><strong>Senior Support</strong> &mdash; Visiting and assisting senior citizens in our community</li>
                            <li><strong>Health Awareness Campaigns</strong> &mdash; Educating the community on health and wellness topics</li>
                        </ul>
                    </div>
                    <div class="activity-image">
                        <div class="img-placeholder">
                            <div class="icon">&#129657;</div>
                            Photo: LEADs at a health event<br>
                            <em>e.g., blood drive or senior support activity</em>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Activity 4 -->
            <div class="activity-section">
                <div class="activity-layout reverse">
                    <div class="activity-text">
                        <h3>Education &amp; Youth Programs</h3>
                        <p>LEADs support education both as learners and as teachers. Through tutoring programs, hospital gift wrapping, and speaker series, students develop their own skills while lifting up others in the community.</p>
                        <ul>
                            <li><strong>ASPIRE Tutoring</strong> &mdash; Peer-to-peer and cross-age tutoring for underserved students in the community</li>
                            <li><strong>Gift Wrapping for Hospitals</strong> &mdash; Brightening the days of hospitalized children with gifts and cards</li>
                            <li><strong>Speaker Series</strong> &mdash; Monthly talks from community leaders, entrepreneurs, and professionals</li>
                            <li><strong>Sewa Academy Online Courses</strong> &mdash; Nationally curated leadership and service learning curriculum</li>
                        </ul>
                    </div>
                    <div class="activity-image">
                        <div class="img-placeholder">
                            <div class="icon">&#128218;</div>
                            Photo: LEADs tutoring or at a workshop<br>
                            <em>e.g., students at ASPIRE session or speaker event</em>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Activity 5 -->
            <div class="activity-section">
                <div class="activity-layout">
                    <div class="activity-text">
                        <h3>Social Causes &mdash; Local &amp; Global</h3>
                        <p>Beyond our regular service activities, LEADs engage with broader social issues. Whether it's providing aid during a crisis, raising funds for a cause, or running awareness campaigns, our students learn to think globally while acting locally.</p>
                        <ul>
                            <li><strong>Disaster Relief &amp; Crisis Aid</strong> &mdash; Mobilizing quickly to support communities in times of need</li>
                            <li><strong>Fundraising Campaigns</strong> &mdash; Organizing events and drives to raise funds for local and global causes</li>
                            <li><strong>Environmental Advocacy</strong> &mdash; Protecting natural resources through awareness and action</li>
                            <li><strong>Civic Engagement</strong> &mdash; Building bridges across communities through collaborative service</li>
                        </ul>
                    </div>
                    <div class="activity-image">
                        <div class="img-placeholder">
                            <div class="icon">&#127760;</div>
                            Photo: LEADs at a social cause event<br>
                            <em>e.g., walkathon, fundraiser, or awareness campaign</em>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Program Structure -->
    <section class="structure" id="program">
        <div class="container">
            <div class="section-header centered">
                <div class="label">Program</div>
                <h2>4-Year Graduation Pathway</h2>
                <div class="divider"></div>
                <p>LEAD is a progressive program. Students enter at Level 1 and advance each year by completing service hours, coursework, and community projects. Upon graduating Level 3, students receive the LEAD Graduation Certificate and Gold Medal.</p>
            </div>
            <div class="pathway">
                <div class="pathway-step">
                    <div class="step-badge badge-bronze"><span class="year">Year 1</span><span class="level">1</span></div>
                    <div class="step-content">
                        <h3>Bronze &mdash; Ready to LEAD</h3>
                        <div class="award-name">Volunteer Service Award &middot; Bronze Pin</div>
                        <p>Students begin with the Ready to LEAD (RTL) course, learning the foundations of service, community engagement, and Sewa values. They participate in chapter service projects, attend speaker series, and begin logging their 100+ service hours for the year. This is where every LEAD's journey starts.</p>
                    </div>
                </div>
                <div class="pathway-step">
                    <div class="step-badge badge-silver"><span class="year">Year 2</span><span class="level">2</span></div>
                    <div class="step-content">
                        <h3>Silver &mdash; Design to LEAD</h3>
                        <div class="award-name">Volunteer Service Learning Award &middot; Silver Pin</div>
                        <p>Students take the Design To LEAD (DTL) course, which deepens their service learning with a mandatory project completion. They design and execute their own community service project, applying leadership and planning skills. This is where LEADs transition from participants to project leaders.</p>
                    </div>
                </div>
                <div class="pathway-step">
                    <div class="step-badge badge-gold"><span class="year">Year 3</span><span class="level">3</span></div>
                    <div class="step-content">
                        <h3>Gold &mdash; VANI LEADership</h3>
                        <div class="award-name">Volunteer Service Learning Leadership Award &middot; Gold Medal &amp; Graduation Certificate</div>
                        <p>The pinnacle of the LEAD program. Students take VANI &mdash; The Sewa LEADership Course, serve as DTL mentors for Level 2 students, and lead teams. Upon completing this level with 100+ hours, LEADs receive their Graduation Certificate and Gold Medal recognizing three years of cumulative service and leadership.</p>
                    </div>
                </div>
                <div class="pathway-step">
                    <div class="step-badge badge-platinum"><span class="year">Year 4</span><span class="level">4</span></div>
                    <div class="step-content">
                        <h3>Platinum &mdash; National Leadership</h3>
                        <div class="award-name">National Service Leadership Excellence Award</div>
                        <p>LEAD graduates can continue into Year 4 and join the National Youth Council. At this level, students participate in national-level planning and execution, mentoring younger LEADs across chapters, and shaping the future direction of the LEAD program nationwide.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Photo Gallery -->
    <section id="gallery">
        <div class="container">
            <div class="section-header centered">
                <div class="label">Gallery</div>
                <h2>Our LEADs in Action</h2>
                <div class="divider"></div>
                <p>A glimpse into the service, learning, and camaraderie at Sewa LEAD Detroit.</p>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item">
                    <div class="img-placeholder" style="height:100%;">
                        <div class="icon">&#128247;</div>Group service event
                    </div>
                </div>
                <div class="gallery-item">
                    <div class="img-placeholder" style="height:100%;">
                        <div class="icon">&#128247;</div>Food bank volunteering
                    </div>
                </div>
                <div class="gallery-item tall">
                    <div class="img-placeholder" style="height:100%;">
                        <div class="icon">&#128247;</div>Chapter meeting or speaker event
                    </div>
                </div>
                <div class="gallery-item">
                    <div class="img-placeholder" style="height:100%;">
                        <div class="icon">&#128247;</div>Award ceremony
                    </div>
                </div>
                <div class="gallery-item">
                    <div class="img-placeholder" style="height:100%;">
                        <div class="icon">&#128247;</div>Cleanup drive
                    </div>
                </div>
                <div class="gallery-item">
                    <div class="img-placeholder" style="height:100%;">
                        <div class="icon">&#128247;</div>Team photo
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Get Involved -->
    <section class="involvement" id="join">
        <div class="container">
            <div class="section-header centered">
                <div class="label">Get Involved</div>
                <h2>How You Can Help</h2>
                <div class="divider"></div>
                <p>Whether you're a student, parent, or community member, there's a place for you in Sewa LEAD Detroit.</p>
            </div>
            <div class="involve-grid">
                <div class="involve-card">
                    <div class="card-icon">&#127891;</div>
                    <h3>Join as a Student</h3>
                    <p>Are you in grades 8-12? Join LEAD to earn service hours, develop leadership skills, build your college resume, and make lifelong friendships while making a real difference in Detroit. The program runs October through August with a $150 annual registration fee. All backgrounds are welcome.</p>
                </div>
                <div class="involve-card">
                    <div class="card-icon">&#128104;&#8205;&#128105;&#8205;&#128103;</div>
                    <h3>Become a Parent Mentor</h3>
                    <p>Parent mentors are the backbone of LEAD. You'll guide a team of 4-5 students through their online learning modules, facilitate breakout room discussions on Zoom, track progress, and help with project mentorship. The time commitment is approximately 3 hours per week from January through March, and flexible hours during the project phase.</p>
                </div>
                <div class="involve-card">
                    <div class="card-icon">&#129309;</div>
                    <h3>Volunteer &amp; Donate</h3>
                    <p>Support our chapter by volunteering at service events, hosting or sponsoring activities, or making a tax-deductible donation. Every contribution helps us expand our reach and serve more families in Metro Detroit. Your time, skills, and generosity make our programs possible.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Program Details -->
    <section class="details">
        <div class="container">
            <div class="section-header centered">
                <div class="label">Details</div>
                <h2>Program Information</h2>
                <div class="divider"></div>
            </div>
            <div class="details-layout">
                <div class="detail-block">
                    <h3>Eligibility &amp; Registration</h3>
                    <p>LEAD is open to all high school students in grades 8 through 12, regardless of citizenship, permanent residency, H1B, or any other immigration status. Sewa is a Hindu faith-based organization but provides equal opportunity to all racial, ethnic, religious, and gender backgrounds.</p>
                    <p>Students and parents must be sincerely committed to the program. A $150 flat registration fee is charged per year. All new students enter at Level 1, regardless of grade level.</p>
                </div>
                <div class="detail-block">
                    <h3>Hours &amp; Project Requirements</h3>
                    <ul>
                        <li>Minimum <strong>100 service hours per year</strong> to receive the Sewa National Presidential Award</li>
                        <li>Minimum <strong>75 hours</strong> required to pass and advance to the next level</li>
                        <li>Non-service hours are capped at <strong>20 hours</strong> for didactic sessions</li>
                        <li>Unlimited service hours can be logged during the implementation phase (April-May)</li>
                        <li>Project completion is <strong>mandatory for Level 2</strong>, optional for Levels 1 and 3</li>
                        <li><strong>20 hours minimum parent commitment</strong> is required</li>
                    </ul>
                </div>
                <div class="detail-block">
                    <h3>Program Calendar</h3>
                    <p><strong>October - December:</strong> Chapter onboarding, service projects, speaker series, and community engagement activities begin.</p>
                    <p><strong>January - March:</strong> Online learning modules through Sewa Academy on Zoho LMS. Live Zoom classes on weekends with team-based breakout sessions. Break during Presidents Day weekend.</p>
                    <p><strong>April - July:</strong> Self-paced project mentorship phase. Teams work on their service projects with mentor guidance.</p>
                    <p><strong>July - August:</strong> National Youth Conference, regional conferences, award ceremonies, and celebrations.</p>
                </div>
                <div class="detail-block">
                    <h3>Awards &amp; Recognition</h3>
                    <p><strong>Year 1 &mdash; Bronze Pin:</strong> Volunteer Service Award recognizing dedicated participation and community service contributions.</p>
                    <p><strong>Year 2 &mdash; Silver Pin:</strong> Volunteer Service Learning Award for exceptional commitment to service with reflection and learning.</p>
                    <p><strong>Year 3 &mdash; Gold Medal:</strong> Volunteer Service Learning Leadership Award and LEAD Graduation Certificate. The certificate reflects cumulative accomplishment across all three years.</p>
                    <p><strong>Year 4 &mdash; Platinum:</strong> National Service Leadership Excellence Award for graduates who join the National Youth Council.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <div class="cta-banner">
        <h2>Ready to Lead Through Service?</h2>
        <p>Join Sewa LEAD Detroit and become part of a community of young leaders who are making a real difference. Whether you're a student, parent, or community supporter, there's a place for you here.</p>
        <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
            <a href="https://www.sewausa.org/Lead" class="btn btn-dark" target="_blank">Register for LEAD</a>
            <a href="https://www.sewausa.org/Donate-for-Detroit-MI" class="btn btn-dark" target="_blank">Donate to Detroit Chapter</a>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-grid">
            <div>
                <h4>Sewa LEAD &middot; Detroit Chapter</h4>
                <p>Sewa International USA is a Hindu faith-inspired, non-profit service organization. LEAD (Leadership, Education and Development) is our flagship youth development program empowering high school students to serve communities and develop as leaders.</p>
                <p style="margin-top:1rem;">Together We Serve Better.</p>
            </div>
            <div>
                <h4>Quick Links</h4>
                <div class="footer-links">
                    <a href="https://www.sewausa.org/Lead" target="_blank">Register for LEAD</a>
                    <a href="https://www.sewausa.org" target="_blank">Sewa International USA</a>
                    <a href="https://www.sewausa.org/Donate-for-Detroit-MI" target="_blank">Donate to Detroit</a>
                    <a href="#about">About the Program</a>
                    <a href="#activities">Service Activities</a>
                </div>
            </div>
            <div>
                <h4>Contact Us</h4>
                <div class="footer-links">
                    <a href="mailto:Detroit@sewausa.org">Detroit@sewausa.org</a>
                    <a href="mailto:lead@sewausa.org">lead@sewausa.org</a>
                    <a href="tel:+17343956952">+1 (734) 395-6952</a>
                    <a>Anand Pappuri, Chapter Coordinator</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2026 Sewa International USA &middot; Detroit Chapter &middot; All donations are tax-deductible.
        </div>
    </footer>

</body>
</html>
"""
