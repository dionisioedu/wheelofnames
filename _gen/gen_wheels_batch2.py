#!/usr/bin/env python3
"""One-off generator for the 8 new wheel template pages (batch 2)."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://wheeloflist.com"

PAGES = [
    dict(
        slug="random-movie",
        name="Random Movie Picker",
        title="Random Movie Picker — Spin to Decide What to Watch | Wheel Of List",
        desc="Can't agree on a film? Spin the random movie picker and let it choose from action, comedy, horror, romance and more. Free, instant, argument-proof.",
        icon="🎬",
        subtitle="Stop scrolling the streaming apps and start watching",
        h1="Random Movie Picker",
        intro="You've spent forty minutes scrolling and the snacks are getting cold. This random movie picker hands the decision to the wheel: spin once, watch whatever it lands on, and reclaim your evening. Twelve genres and moods cover most nights — from a no-brainer action flick to a slow-burn drama.",
        whatson="Action, Comedy, Horror, Romance, Sci-Fi, Thriller, Animation, Documentary, Fantasy, Classic, Indie and Family. A deliberate spread so there's always something for the mood you're actually in, not the one you claimed you were in.",
        howto=[
            ("Spin and commit", "The rule that makes it work: whatever comes up is what you watch. No vetoes, no \"best of three\" unless everyone genuinely agrees beforehand."),
            ("Match your mood", "If it lands on Horror and it's a Tuesday night, hit reset and spin again — just be honest that you're filtering by mood, not rejecting the wheel."),
            ("Set up a marathon", "Turn on <em>Remove winner after spin</em> and keep going to build a whole weekend watchlist with no repeats."),
            ("Customize the list", "Have a shortlist of films in mind? Replace the genres with actual titles in the editor and treat it as your personal movie roulette."),
        ],
        entries=["Action", "Comedy", "Horror", "Romance", "Sci-Fi", "Thriller", "Drama", "Animation", "Documentary", "Fantasy", "Classic", "Family"],
        faqs=[
            ("Can I pick from actual movie titles instead of genres?",
             "Yes — click \u201cCustomize this wheel\u201d and swap the genres for your own shortlist of films. It becomes a true movie roulette with your exact collection."),
            ("Is the pick really random?",
             "Every genre sits on an equal segment, so each one has the same chance of being chosen. The result is only decided when the wheel stops."),
            ("What if we've seen the movie it picks?",
             "Turn on \u201cRemove winner after spin\u201d and spin again — the seen one drops off the wheel so you won't land on it twice."),
            ("Does it work for picking a TV episode too?",
             "Absolutely. Customize the entries to seasons, episodes or shows and it works exactly the same way."),
        ],
        related=[("what-to-watch", "🍿", "What to Watch Wheel", "Stop scrolling, start watching"), ("chore-wheel", "🧹", "Chore Wheel", "The referee your household needed"), ("what-to-do", "🎈", "What to Do Wheel", "Boredom ends where the wheel stops")],
    ),
    dict(
        slug="first-date-questions",
        name="First Date Questions",
        title="First Date Questions Wheel — Conversation Starters | Wheel Of List",
        desc="Nervous about silences? Spin the first date questions wheel for easy, interesting conversation starters. Keep the chat flowing and actually get to know each other.",
        icon="💬",
        subtitle="Never run out of things to talk about",
        h1="First Date Questions",
        intro="First dates have two enemies: awkward silence and talking about the weather. This wheel puts a dozen real questions on the table so the conversation moves itself. Spin, answer, and let the answers branch into new threads — it's a low-pressure way to learn what someone's actually like.",
        whatson="Questions about travel, childhood, dreams, music, food, fears, hidden talents and more. Light enough to keep the mood easy, but personal enough that the answers tell you something real.",
        howto=[
            ("Take turns spinning", "Person A spins and answers first, then hand over the wheel. You both end up answering, so it never feels like an interview."),
            ("Follow the thread", "Don't rush back to the wheel — if an answer sparks a story, follow it. The questions are springs, not a checklist."),
            ("Skip the hard ones", "If a question feels too much too soon, spin again. There's no scoring, and no obligation to answer anything."),
            ("Customize the set", "Use \u201cCustomize this wheel\u201d to add your own questions, or delete the ones you'd rather save for a second date."),
        ],
        entries=["Where's the best place you've ever travelled?", "What did you want to be when you were a kid?", "What's your guilty pleasure TV show?", "What's a skill you've always wanted to learn?", "What's the last thing that made you laugh out loud?", "If you could live anywhere, where would it be?", "What's your go-to comfort meal?", "What's a small thing that instantly improves your day?", "What song is on your repeat right now?", "What's the bravest thing you've ever done?", "What do you nerd out about?", "What's on your bucket list this year?"],
        faqs=[
            ("Are these questions too intense for a first date?",
             "No — they're deliberately on the light side. They invite stories rather than deep confessions, so the mood stays easy and there's no pressure to overshare."),
            ("How many questions should we get through?",
             "There's no target. Some nights you'll answer three and then talk for an hour; that's the point. The wheel breaks the ice, it doesn't set the pace."),
            ("Can we use it with a group instead of a couple?",
             "Definitely — it doubles as a party icebreaker. Everyone spins and answers in turn, which works far better than the usual \u201cso what's your job?\u201d loop."),
            ("Can I add my own questions?",
             "Yes. Open \u201cCustomize this wheel\u201d, replace or add entries, and share the link so you both see the same set."),
        ],
        related=[("icebreaker-questions", "🧊", "Icebreaker Question Wheel", "Ten questions, zero awkward silences"), ("date-night", "💘", "Date Night Wheel", "Because \u201cI don't know, you pick\u201d isn't a date"), ("what-to-do", "🎈", "What to Do Wheel", "Boredom ends where the wheel stops")],
    ),
    dict(
        slug="party-games",
        name="Party Games",
        title="Party Games Wheel — Spin to Pick the Next Game | Wheel Of List",
        desc="End the \u201cwhat should we play?\u201d debate. Spin the party games wheel to pick the next game — charades, trivia, karaoke and more. Free, fast and always fair.",
        icon="🎉",
        subtitle="Pick the next game without a group vote",
        h1="Party Games Wheel",
        intro="There's always one moment at every gathering where nobody can agree on what to play, and the energy starts to fizzle. This wheel kills that moment. Spin it, play whatever it lands on, and when the round's over spin again. A dozen proven crowd-pleasers mean there's always a next game.",
        whatson="Charades, Trivia, Truth or Dare, Karaoke, Pictionary, Would You Rather, Two Truths and a Lie, Never Have I Ever, Dance-off, Cards, Board Games and Karaoke encore. Classics that work with almost any group, plus a couple of wildcards to keep it lively.",
        howto=[
            ("Spin between rounds", "There's no agreeing on the next game — the wheel decides. It keeps the party moving and stops one loud voice from picking everything."),
            ("Rotate the chooser", "Let whoever won the last round spin the next one. Tiny bit of stakes, tiny bit of ceremony."),
            ("Match the crowd", "If your group skews shy, swap out the louder games for calmer ones using \u201cCustomize this wheel\u201d."),
            ("Remove completed games", "Turn on <em>Remove winner after spin</em> and you'll work through every game once without ever repeating."),
        ],
        entries=["Charades", "Trivia", "Truth or Dare", "Karaoke", "Pictionary", "Would You Rather", "Two Truths and a Lie", "Never Have I Ever", "Dance-off", "Card Games", "Board Games", "Free Choice"],
        faqs=[
            ("What if the group doesn't like the game it picks?",
             "Then you've learned something — customize the wheel to remove it. The whole point is to decide quickly, so try to play what comes up at least once before vetoing."),
            ("Do we need any equipment?",
             "Most of these need nothing at all. A few, like Pictionary or card games, need basic supplies, but there's always an equipment-free option on the wheel."),
            ("How many players does it work for?",
             "It suits anything from three people to a big party. For very large groups, split into teams and have one person spin for everyone."),
            ("Can I use it for a kids' party?",
             "Yes. Open the editor and swap in age-appropriate games — the wheel itself works exactly the same for any age group."),
        ],
        related=[("truth-or-dare", "🎭", "Truth or Dare Wheel", "The party classic, minus the arguing"), ("icebreaker-questions", "🧊", "Icebreaker Question Wheel", "Ten questions, zero awkward silences"), ("what-to-do", "🎈", "What to Do Wheel", "Boredom ends where the wheel stops")],
    ),
    dict(
        slug="baby-names",
        name="Baby Name Picker",
        title="Baby Name Picker Wheel — Spin to Choose a Name | Wheel Of List",
        desc="Stuck between two names? Spin the baby name picker wheel to shortlist and choose a name together. Fun for parents, baby showers and name games.",
        icon="👶",
        subtitle="Let the wheel settle the great name debate",
        h1="Baby Name Picker",
        intro="Every couple has a shortlist that never quite resolves. One of you loves it, the other has a cousin with the same name. The baby name picker won't replace your shortlist, but it will break the deadlock: load your favourites, spin, and see which one makes you both smile. It's also a brilliant baby-shower game for guests to play.",
        whatson="A mix of classic, modern, nature and vintage-inspired names to get you started — perfect as a party game or as a nudge when your own list is stuck at two. Swap them for your real shortlist before the big spin.",
        howto=[
            ("Shortlist first", "Get your real contenders down to a manageable set of eight to fourteen, then put them on the wheel. A shorter list makes every spin meaningful."),
            ("Use the gut-check", "Spin and watch your reaction. If the winner makes you wince, that name's off the list — and if it makes you both grin, you've probably found it."),
            ("Play it at a baby shower", "Guests spin for their prediction and you tally the results — a genuinely fun party game that doesn't require anyone to guess the bump size."),
            ("Customize completely", "Use \u201cCustomize this wheel\u201d to load your own names, add middle names, or run a two-round shortlist."),
        ],
        entries=["Olivia", "Liam", "Amelia", "Noah", "Sophia", "Ethan", "Isla", "Mason", "Ava", "Lucas", "Mia", "Leo"],
        faqs=[
            ("Should we really let a wheel name our baby?",
             "Think of it as a tie-breaker, not the decision-maker. It's best for choosing between names you already both like, or as a fun reveal at a shower."),
            ("Can I enter my own list of names?",
             "Yes — \u201cCustomize this wheel\u201d opens the editor so you can add your real shortlist, remove the defaults entirely, and share the wheel with your partner."),
            ("Is it a good baby shower game?",
             "It's one of the most popular uses. Guests spin to predict the name, or you run a knockout tournament to whittle a long list down to a favourite."),
            ("What if we get a name we don't like?",
             "Just spin again — or delete that entry from the wheel. The goal is to help you decide, not to trap you with a random pick."),
        ],
        related=[("party-games", "🎉", "Party Games Wheel", "Pick the next game without a group vote"), ("icebreaker-questions", "🧊", "Icebreaker Question Wheel", "Ten questions, zero awkward silences"), ("chore-wheel", "🧹", "Chore Wheel", "The referee your household needed")],
    ),
    dict(
        slug="christmas-movies",
        name="Christmas Movies",
        title="Christmas Movies Wheel — Spin for a Festive Film | Wheel Of List",
        desc="Spin the Christmas movies wheel to pick tonight's festive film — classics, rom-coms, animations and family favourites. Free, quick and full of holiday cheer.",
        icon="🎄",
        subtitle="Festive film night, decided in one spin",
        h1="Christmas Movies Wheel",
        intro="It's December, the tree's up, and everyone wants to watch a Christmas film — just not the same one. Rather than a twenty-minute negotiation over hot chocolate, let the wheel settle it. Spin, grab a blanket, and let the holiday movie marathon begin.",
        whatson="A festive spread of Christmas classics, animated family favourites, romantic comedies, and a couple of modern picks. Enough variety to suit a cosy solo night, a family gathering or a movie marathon with friends.",
        howto=[
            ("Spin for the first film", "Whoever's hosting spins, and the result starts the marathon. No rewinds, no \u201cbut we watched that last year\u201d."),
            ("Build a marathon", "Turn on <em>Remove winner after spin</em> and keep spinning to line up a whole evening of films with no repeats."),
            ("Match the audience", "Watching with kids? Customize the wheel to leave in only the family-friendly picks. Adult night? Keep the rom-coms and classics."),
            ("Save your favourites", "Use \u201cCustomize this wheel\u201d to load your actual shelf of festive films and share the link with the group."),
        ],
        entries=["Home Alone", "Elf", "The Polar Express", "Die Hard", "Love Actually", "The Grinch", "Miracle on 34th Street", "It's a Wonderful Life", "A Christmas Carol", "Frozen", "The Holiday", "National Lampoon's Christmas Vacation"],
        faqs=[
            ("Is Die Hard really a Christmas movie?",
             "That debate is exactly why it's on the wheel, and exactly why the wheel settles it. If your group disagrees, spin — the wheel's ruling is final."),
            ("Can I add my own Christmas films?",
             "Yes — \u201cCustomize this wheel\u201d opens the editor so you can swap in your family's must-watch list, then share the link so everyone sees the same films."),
            ("Can I use it for a whole month of films?",
             "Turn on \u201cRemove winner after spin\u201d and you'll work through the entire list once, giving you a December viewing calendar with no repeats."),
            ("Does it work for other holidays?",
             "Of course — the wheel is just a list. Open the editor and rename the entries for Halloween, Thanksgiving or any other seasonal marathon."),
        ],
        related=[("random-movie", "🎬", "Random Movie Picker", "Let the wheel choose tonight's film"), ("what-to-watch", "🍿", "What to Watch Wheel", "Stop scrolling, start watching"), ("party-games", "🎉", "Party Games Wheel", "Pick the next game without a group vote")],
    ),
    dict(
        slug="study-break",
        name="Study Break",
        title="Study Break Wheel — Spin for a Quick Break Activity | Wheel Of List",
        desc="Studying hard? Spin the study break wheel for a quick, restorative break activity — stretch, hydrate, walk or breathe. Free and instant, so you get back to work.",
        icon="📚",
        subtitle="Smart breaks that actually recharge you",
        h1="Study Break Wheel",
        intro="The trick to long study sessions isn't willpower, it's breaks that actually restore focus. This wheel picks a short, purposeful break for you so you don't lose twenty minutes deciding what to do — or worse, fall down a phone rabbit hole. Spin, take the break, come back sharper.",
        whatson="Twelve quick restorative activities: stretch, drink water, take a short walk, breathe, grab a snack and more. Most take under ten minutes and get you off the screen, which is the point.",
        howto=[
            ("Set a study timer", "Study for 25–50 minutes, then spin the wheel and take whatever break it gives you. The predictable rhythm beats vague \u201cI'll take a break soon\u201d plans."),
            ("Keep breaks short", "Aim for five to ten minutes. Long enough to reset your focus, short enough that you don't lose the thread of what you were doing."),
            ("Don't negotiate", "The wheel's job is to stop you deliberating. Whatever comes up is the break — even if it's the one you wouldn't have chosen."),
            ("Customize your list", "Add your own go-to resets, or remove the ones that tempt you into a doomscroll, using \u201cCustomize this wheel\u201d."),
        ],
        entries=["Stretch for 5 minutes", "Drink a glass of water", "Take a 10-minute walk", "Do 20 jumping jacks", "Breathe deeply for 2 minutes", "Grab a healthy snack", "Step outside for fresh air", "Tidy your desk", "Listen to one song", "Rest your eyes for 5 minutes", "Make a cup of tea", "Doodle for 5 minutes"],
        faqs=[
            ("How long should a study break be?",
             "Five to ten minutes for a quick reset, or up to twenty after a long focused block. The key is deciding in advance so the break doesn't stretch into an hour."),
            ("Is it bad to take breaks while studying?",
             "No — the opposite. Regular short breaks protect your focus and memory. The problem is only when breaks become unstructured screen time, which is what the wheel prevents."),
            ("Can I use it for work instead of study?",
             "Yes, it works exactly the same way. Swap in your own break ideas and use it on a Pomodoro-style work rhythm."),
            ("What if I don't like the break it picks?",
             "Take it anyway once, then customize it out. The point is to stop over-thinking your breaks — a small compromise is worth not losing your momentum."),
        ],
        related=[("workout", "💪", "Workout Wheel", "Your randomized no-equipment circuit"), ("chore-wheel", "🧹", "Chore Wheel", "The referee your household needed"), ("what-to-do", "🎈", "What to Do Wheel", "Boredom ends where the wheel stops")],
    ),
]


def build(p):
    url = f"{DOMAIN}/wheels/{p['slug']}/"
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faqs"]
        ],
    }
    webapp_ld = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": p["name"],
        "applicationCategory": "EntertainmentApplication",
        "operatingSystem": "Web",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "description": p["desc"],
        "url": url,
    }
    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": "Wheel Templates", "item": f"{DOMAIN}/wheels/"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": url},
        ],
    }
    howto_html = "\n".join(
        f"      <li><strong>{t}:</strong> {d}</li>" for t, d in p["howto"]
    )
    faq_html = "\n".join(
        f"    <p><strong>{q}</strong><br>{a}</p>" for q, a in p["faqs"]
    )
    related_cards = "\n".join(
        f'''        <a class="tool-card" href="/wheels/{slug}/">
          <div class="tool-card-icon">{icon}</div>
          <h4>{title}</h4>
          <p>{desc}</p>
          <div class="tool-card-arrow">→</div>
        </a>'''
        for slug, icon, title, desc in p["related"]
    )
    extra_card = '''        <a class="tool-card" href="/wheels/">
          <div class="tool-card-icon">🎯</div>
          <h4>All Wheel Templates</h4>
          <p>Browse every ready-made wheel in the gallery</p>
          <div class="tool-card-arrow">→</div>
        </a>'''
    entries_json = json.dumps(p["entries"])
    faq_ld_json = json.dumps(faq_ld, ensure_ascii=False, indent=2)
    webapp_ld_json = json.dumps(webapp_ld, ensure_ascii=False, indent=2)
    breadcrumb_ld_json = json.dumps(breadcrumb_ld, ensure_ascii=False, indent=2)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{p['title']}</title>
  <meta name="description" content="{p['desc']}">
  <meta name="robots" content="index, follow">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#6858e8">
  <link rel="icon" href="/favicon.ico">
  <meta property="og:title" content="{p['name']} — Wheel Of List">
  <meta property="og:description" content="{p['desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Wheel Of List">
  <meta property="og:image" content="{DOMAIN}/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:creator" content="@DionisioDev">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Quicksand&display=swap" rel="stylesheet">
  <link href="/styles.css" rel="stylesheet">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XV614N2RLR"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XV614N2RLR');
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
  <script type="application/ld+json">
{webapp_ld_json}
  </script>
  <script type="application/ld+json">
{breadcrumb_ld_json}
  </script>
  <script type="application/ld+json">
{faq_ld_json}
  </script>
  <style>
    .ww-wrap {{ position: relative; width: min(420px, 88vw); margin: 0 auto; }}
    #wwCanvas {{ width: 100%; height: auto; display: block; border-radius: 50%; box-shadow: 0 4px 12px rgba(0,0,0,0.3); cursor: pointer; background: #fff; }}
    .ww-pointer {{ position: absolute; top: -12px; left: 50%; transform: translateX(-50%) rotate(180deg); width: 40px; height: 34px; clip-path: polygon(50% 0%, 0% 100%, 100% 100%); background: #1E90FF; filter: drop-shadow(0 3px 5px rgba(0,0,0,0.4)); z-index: 5; }}
    .ww-result {{ font-size: 2rem; font-weight: 900; text-align: center; min-height: 2.8rem; margin: 18px 0 6px; }}
    .ww-controls {{ display: flex; gap: 14px; justify-content: center; align-items: center; flex-wrap: wrap; margin-top: 14px; }}
    .ww-entries {{ columns: 2; column-gap: 30px; }}
    @media (max-width: 600px) {{ .ww-entries {{ columns: 1; }} }}
  </style>
</head>
<body>
  <script>try{{if(localStorage.getItem('wheeloflist_theme')==='dark')document.body.classList.add('dark-theme');}}catch(e){{}}</script>

  <nav class="navbar navbar-expand-lg navbar-light navbar-custom">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">🎡 Wheel Of List</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarContent">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="toolsDropdown" role="button" data-bs-toggle="dropdown">Tools</a>
            <ul class="dropdown-menu" aria-labelledby="toolsDropdown">
              <li><a class="dropdown-item" href="/">🎡 Wheel Spinner</a></li>
              <li><a class="dropdown-item" href="/coin-flip/">🪙 Coin Flip</a></li>
              <li><a class="dropdown-item" href="/random-number/">🎲 Random Number Generator</a></li>
              <li><a class="dropdown-item" href="/dice-roller/">🎰 Dice Roller</a></li>
              <li><a class="dropdown-item" href="/yes-no-wheel/">❓ Yes or No Wheel</a></li>
              <li><a class="dropdown-item" href="/team-generator/">👥 Team Generator</a></li>
              <li><a class="dropdown-item" href="/random-letter/">🔤 Random Letter</a></li>
              <li><a class="dropdown-item" href="/raffle-picker/">🏆 Raffle Picker</a></li>
              <li><a class="dropdown-item" href="/tournament/">🏟️ Tournament Bracket</a></li>
              <li><a class="dropdown-item" href="/wheels/">🎯 Wheel Templates</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="/tools/">🧰 All Tools</a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="/#about">About</a></li>
          <li class="nav-item"><a class="nav-link" href="mailto:dionisiosoftware@gmail.com?subject=Wheel%20of%20List">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <div id="tools-container" style="display:block">
    <div class="tools-section">
      <div class="tools-header">
        <h2>{p['icon']} {p['name']}</h2>
        <p class="tools-subtitle">{p['subtitle']}</p>
      </div>
      <div class="tools-content">
        <div id="wheel-widget"></div>
      </div>
    </div>
  </div>

  <main class="container" style="max-width: 900px; padding: 40px 20px;">
    <h1 style="font-size:1.9rem;">{p['h1']}</h1>
    <p>{p['intro']}</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>{p['whatson']}</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">How to use this wheel</h2>
    <ul>
{howto_html}
    </ul>

    <h2 style="font-size:1.4rem; margin-top:2rem;">Make it yours</h2>
    <p>Want to add, remove or reword the options? Hit <strong>“Customize this wheel”</strong> under the spinner — it opens this exact list in the <a href="/">full wheel editor</a>, where you can edit entries, change the theme, and share your version with a link. You can also toggle <em>Remove winner after spin</em> to run through every option without repeats.</p>

    <h2 style="font-size:1.4rem; margin-top:2rem;">FAQ</h2>
{faq_html}

    <section class="quick-tools-section" style="margin-top:3rem;">
      <h3 class="quick-tools-title">More Wheels</h3>
      <div class="tools-grid">
{related_cards}
{extra_card}
      </div>
    </section>
  </main>

  <footer class="bg-light text-center mt-3 p-4">
    <div class="mb-2">
      <a href="/" class="text-decoration-none mx-2">Wheel Spinner</a>
      <a href="/coin-flip/" class="text-decoration-none mx-2">Coin Flip</a>
      <a href="/random-number/" class="text-decoration-none mx-2">Random Number</a>
      <a href="/dice-roller/" class="text-decoration-none mx-2">Dice Roller</a>
      <a href="/yes-no-wheel/" class="text-decoration-none mx-2">Yes or No Wheel</a>
      <a href="/team-generator/" class="text-decoration-none mx-2">Team Generator</a>
      <a href="/random-letter/" class="text-decoration-none mx-2">Random Letter</a>
      <a href="/raffle-picker/" class="text-decoration-none mx-2">Raffle Picker</a>
      <a href="/tournament/" class="text-decoration-none mx-2">Tournament Bracket</a>
      <a href="/wheels/" class="text-decoration-none mx-2">Wheel Templates</a>
      <a href="/tools/" class="text-decoration-none mx-2">All Tools</a>
    </div>
    <div class="mb-2">
      <a href="/privacy-policy/" class="text-decoration-none mx-2">Privacy Policy</a>
      <a href="/terms/" class="text-decoration-none mx-2">Terms of Use</a>
      <a href="mailto:dionisiosoftware@gmail.com?subject=Wheel%20of%20List" class="text-decoration-none mx-2">Contact</a>
    </div>
    <a href="https://dionisio.dev" class="text-decoration-none">Copyright © Dionisio Software</a>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script>window.WHEEL_DATA = {{"entries": {entries_json}, "removeDefault": false}};</script>
  <script src="/wheels/wheel-widget.js"></script>
  <script src="/engagement.js" defer></script>
  <script src="/consent.js" defer></script>
</body>
</html>
'''


for p in PAGES:
    outdir = os.path.join(ROOT, "wheels", p["slug"])
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.htm"), "w", encoding="utf-8") as fh:
        fh.write(build(p))
    print("wrote", p["slug"])
