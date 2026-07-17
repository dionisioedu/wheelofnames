#!/usr/bin/env python3
"""Generate /wheels/ template pages + gallery for wheeloflist.com."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = '''  <nav class="navbar navbar-expand-lg navbar-light navbar-custom">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">🎡 Wheel Of List</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
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
  </nav>'''

FOOTER = '''  <footer class="bg-light text-center mt-3 p-4">
    <div class="mb-2">
      <a href="/" class="text-decoration-none mx-2">Wheel Spinner</a>
      <a href="/coin-flip/" class="text-decoration-none mx-2">Coin Flip</a>
      <a href="/random-number/" class="text-decoration-none mx-2">Random Number</a>
      <a href="/dice-roller/" class="text-decoration-none mx-2">Dice Roller</a>
      <a href="/yes-no-wheel/" class="text-decoration-none mx-2">Yes or No Wheel</a>
      <a href="/team-generator/" class="text-decoration-none mx-2">Team Generator</a>
      <a href="/random-letter/" class="text-decoration-none mx-2">Random Letter</a>
      <a href="/raffle-picker/" class="text-decoration-none mx-2">Raffle Picker</a>
      <a href="/wheels/" class="text-decoration-none mx-2">Wheel Templates</a>
      <a href="/tools/" class="text-decoration-none mx-2">All Tools</a>
    </div>
    <div class="mb-2">
      <a href="/privacy-policy/" class="text-decoration-none mx-2">Privacy Policy</a>
      <a href="/terms/" class="text-decoration-none mx-2">Terms of Use</a>
      <a href="mailto:dionisiosoftware@gmail.com?subject=Wheel%20of%20List" class="text-decoration-none mx-2">Contact</a>
    </div>
    <a href="https://dionisio.dev" class="text-decoration-none">Copyright © Dionisio Software</a>
  </footer>'''

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>@@TITLE@@</title>
  <meta name="description" content="@@DESC@@">
  <meta name="robots" content="index, follow">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="https://wheeloflist.com/wheels/@@SLUG@@/">
  <meta name="theme-color" content="#3369e8">
  <link rel="icon" href="/favicon.ico">
  <meta property="og:title" content="@@OG_TITLE@@">
  <meta property="og:description" content="@@DESC@@">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://wheeloflist.com/wheels/@@SLUG@@/">
  <meta property="og:site_name" content="Wheel Of List">
  <meta property="og:image" content="https://wheeloflist.com/og.jpg">
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
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XV614N2RLR');
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
  <script type="application/ld+json">
@@APP_JSON@@
  </script>
  <script type="application/ld+json">
@@BREADCRUMB_JSON@@
  </script>
  <script type="application/ld+json">
@@FAQ_JSON@@
  </script>
  <style>
    .ww-wrap { position: relative; width: min(420px, 88vw); margin: 0 auto; }
    #wwCanvas { width: 100%; height: auto; display: block; border-radius: 50%; box-shadow: 0 4px 12px rgba(0,0,0,0.3); cursor: pointer; background: #fff; }
    .ww-pointer { position: absolute; top: -12px; left: 50%; transform: translateX(-50%) rotate(180deg); width: 40px; height: 34px; clip-path: polygon(50% 0%, 0% 100%, 100% 100%); background: #1E90FF; filter: drop-shadow(0 3px 5px rgba(0,0,0,0.4)); z-index: 5; }
    .ww-result { font-size: 2rem; font-weight: 900; text-align: center; min-height: 2.8rem; margin: 18px 0 6px; }
    .ww-controls { display: flex; gap: 14px; justify-content: center; align-items: center; flex-wrap: wrap; margin-top: 14px; }
    .ww-entries { columns: 2; column-gap: 30px; }
    @media (max-width: 600px) { .ww-entries { columns: 1; } }
  </style>
</head>
<body>
  <script>try{if(localStorage.getItem('wheeloflist_theme')==='dark')document.body.classList.add('dark-theme');}catch(e){}</script>

@@NAV@@

  <div id="tools-container" style="display:block">
    <div class="tools-section">
      <div class="tools-header">
        <h2>@@EMOJI@@ @@NAME@@</h2>
        <p class="tools-subtitle">@@SUBTITLE@@</p>
      </div>
      <div class="tools-content">
        <div id="wheel-widget"></div>
      </div>
    </div>
  </div>

  <main class="container" style="max-width: 900px; padding: 40px 20px;">
@@BODY@@

    <h2 style="font-size:1.4rem; margin-top:2rem;">Make it yours</h2>
    <p>Want to add, remove or reword the options? Hit <strong>“Customize this wheel”</strong> under the spinner — it opens this exact list in the <a href="/">full wheel editor</a>, where you can edit entries, change the theme, and share your version with a link. You can also toggle <em>Remove winner after spin</em> to run through every option without repeats.</p>

    <h2 style="font-size:1.4rem; margin-top:2rem;">FAQ</h2>
@@FAQ_HTML@@

    <section class="quick-tools-section" style="margin-top:3rem;">
      <h3 class="quick-tools-title">More Wheels</h3>
      <div class="tools-grid">
@@RELATED@@
      </div>
    </section>
  </main>

@@FOOTER@@

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script>window.WHEEL_DATA = @@WHEEL_DATA@@;</script>
  <script src="/wheels/wheel-widget.js"></script>
  <script src="/consent.js" defer></script>
</body>
</html>
'''

PAGES = [
  {
    "slug": "what-to-eat",
    "name": "What to Eat Wheel",
    "emoji": "🍕",
    "title": "What to Eat Wheel — Spin to Decide Your Next Meal | Wheel Of List",
    "og_title": "What to Eat Wheel — Spin to Decide Your Next Meal",
    "desc": "Can't decide what to eat? Spin the food wheel and let it pick dinner: pizza, sushi, tacos, pasta and more. Free, instant and argument-proof.",
    "subtitle": "Dinner indecision, solved in one spin",
    "remove_default": False,
    "entries": ["Pizza", "Sushi", "Burgers", "Tacos", "Pasta", "Thai", "Indian", "Chinese", "BBQ", "Salad", "Ramen", "Sandwiches"],
    "body": '''    <h1 style="font-size:1.9rem;">What to Eat Wheel</h1>
    <p>It's 7pm, everyone's hungry, and the conversation has been stuck on "I don't know, what do <em>you</em> want?" for twenty minutes. End it. Spin the wheel and dinner is decided — no vetoes, no debates, no scrolling through delivery apps until midnight. The wheel holds twelve crowd-pleasing options covering takeout classics and cook-at-home staples.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>Pizza, Sushi, Burgers, Tacos, Pasta, Thai, Indian, Chinese, BBQ, Salad, Ramen and Sandwiches. A deliberate mix: comfort food, healthy-ish options, and cuisines that reheat well. If your city has a great Ethiopian place or your fridge disagrees with half the list, customize it — your version is one click away.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">Pro tips for the hungry and indecisive</h2>
    <ul>
      <li><strong>The two-spin rule:</strong> if the result makes you go "ugh", you actually wanted something else — spin once more and notice which option you're rooting for.</li>
      <li><strong>Group dinners:</strong> agree <em>before</em> the spin that the wheel's word is final. This is the entire point of the wheel.</li>
      <li><strong>Weekly meal planning:</strong> turn on <em>Remove winner after spin</em> and spin seven times — that's your week, planned in under a minute.</li>
    </ul>''',
    "faq": [
      ("Can I add my own food options?",
       "Yes — click “Customize this wheel” to open the list in the full editor, where you can add, remove or edit any option and share your version."),
      ("How does the wheel decide?",
       "Each spin lands on a uniformly random position, so every food option has an equal chance. Twelve options means 1-in-12 odds for each."),
      ("Can I plan a whole week of meals?",
       "Yes — enable “Remove winner after spin” and keep spinning. Each result is removed, giving you a repeat-free meal plan."),
    ],
  },
  {
    "slug": "truth-or-dare",
    "name": "Truth or Dare Wheel",
    "emoji": "🎭",
    "title": "Truth or Dare Wheel — Spin to Play | Wheel Of List",
    "og_title": "Truth or Dare Wheel — Spin to Play",
    "desc": "Spin the Truth or Dare wheel and let chance run your party game. Fair 50/50 spins plus starter questions and dares for every group.",
    "subtitle": "The party classic, minus the arguing",
    "remove_default": False,
    "entries": ["Truth", "Dare", "Truth", "Dare", "Truth", "Dare", "Truth", "Dare"],
    "body": '''    <h1 style="font-size:1.9rem;">Truth or Dare Wheel</h1>
    <p>The oldest party game in the world has one weak point: the "you always pick truth!" argument. The wheel fixes it. Each player spins on their turn — the wheel decides truth or dare, chance takes the blame, and the game keeps moving. Four Truth and four Dare segments guarantee a fair 50/50 on every spin.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">How to play</h2>
    <ol>
      <li>Sit in a circle (or on a video call — it works great remotely).</li>
      <li>On your turn, spin the wheel. No re-spins — that's the rule that makes it fun.</li>
      <li>Truth: answer honestly. Dare: do the thing. The group decides if you delivered.</li>
      <li>Chickening out costs a forfeit — the group picks it (keep it kind).</li>
    </ol>
    <h2 style="font-size:1.4rem; margin-top:2rem;">Starter questions and dares</h2>
    <p><strong>Truths:</strong> What's the most embarrassing song you secretly love? What's a lie you told that you still feel bad about? Who in this room would you trade lives with for a day? What's your most irrational fear? What's the worst gift you ever gave someone?</p>
    <p><strong>Dares:</strong> Talk in an accent until your next turn. Let the group post a (harmless) status from your phone. Do your best impression of another player. Eat a spoonful of a condiment chosen by the group. Show everyone your most-used emoji list.</p>
    <p>Playing with kids or coworkers? Keep a "family mode" rule: all truths and dares must pass the grandma test. Need turn order too? Put everyone's name on the <a href="/">main wheel</a> and spin for who goes next.</p>''',
    "faq": [
      ("Is the wheel really 50/50 between truth and dare?",
       "Yes — the wheel has four Truth and four Dare segments, and every spin lands uniformly at random, so both outcomes always have equal odds."),
      ("Can I make a wheel with actual questions on it?",
       "Yes — click “Customize this wheel” and replace the segments with your own truths and dares, then share the link with your group."),
      ("Can we play remotely?",
       "Absolutely. Share your screen on the call, or send the wheel link so everyone spins the same wheel on their turn."),
    ],
  },
  {
    "slug": "what-to-watch",
    "name": "What to Watch Wheel",
    "emoji": "🍿",
    "title": "What to Watch Wheel — Spin for a Movie Genre | Wheel Of List",
    "og_title": "What to Watch Wheel — Spin for a Movie Genre",
    "desc": "Endless scrolling, zero movies watched? Spin the what-to-watch wheel and get a genre: comedy, horror, sci-fi and more. Decide in seconds, watch in minutes.",
    "subtitle": "Stop scrolling, start watching",
    "remove_default": False,
    "entries": ["Action", "Comedy", "Horror", "Sci-Fi", "Romance", "Thriller", "Animation", "Documentary", "Fantasy", "Drama"],
    "body": '''    <h1 style="font-size:1.9rem;">What to Watch Wheel</h1>
    <p>The average couple spends more time choosing a movie than watching the first act. Streaming menus are designed for browsing, not deciding — so decide somewhere else. Spin the wheel, get a genre, then pick the first title in that genre that catches your eye. Total decision time: about forty seconds.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>Ten genres: Action, Comedy, Horror, Sci-Fi, Romance, Thriller, Animation, Documentary, Fantasy and Drama. Broad on purpose — the wheel narrows the ocean to a lake, and picking a title from one genre is easy.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">House rules that actually work</h2>
    <ul>
      <li><strong>The first-scroll rule:</strong> after the spin, you must pick from the first row of results in that genre. No infinite scrolling allowed.</li>
      <li><strong>Movie night roulette:</strong> spin with <em>Remove winner after spin</em> on across a month of Fridays — you'll finally watch genres you always skip.</li>
      <li><strong>Custom catalogs:</strong> replace genres with your actual watchlist titles via “Customize this wheel” — then the wheel picks the exact movie.</li>
    </ul>
    <p>Arguing about who holds the remote? Settle it with a <a href="/coin-flip/">coin flip</a> first.</p>''',
    "faq": [
      ("Can I put specific movies on the wheel instead of genres?",
       "Yes — hit “Customize this wheel” and swap the genres for your own watchlist titles, then spin for the exact movie."),
      ("How do we choose the actual movie after the genre spin?",
       "Use the first-scroll rule: open your streaming app's row for that genre and pick from the first visible titles. It keeps the decision under a minute."),
      ("What if we hate the genre it lands on?",
       "One re-spin is allowed per night — but only one. Otherwise you're back to endless scrolling, and the wheel can't help you there."),
    ],
  },
  {
    "slug": "what-to-do",
    "name": "What to Do Wheel",
    "emoji": "🎈",
    "title": "What to Do Wheel — Beat Boredom with a Spin | Wheel Of List",
    "og_title": "What to Do Wheel — Beat Boredom with a Spin",
    "desc": "Bored? Spin the what-to-do wheel and get an instant activity: walk, cook, game, read, create. Twelve boredom-busting options, zero excuses.",
    "subtitle": "Boredom ends where the wheel stops",
    "remove_default": False,
    "entries": ["Go for a walk", "Call a friend", "Read a book", "Watch a movie", "Cook something new", "Play a game", "Do a workout", "Learn something", "Tidy one room", "Take a nap", "Write or journal", "Listen to a podcast"],
    "body": '''    <h1 style="font-size:1.9rem;">What to Do Wheel</h1>
    <p>Boredom is rarely a lack of options — it's having so many that none of them wins. That's a decision problem, and decision problems are what wheels are for. Spin once, do what it says for at least ten minutes. If you're still bored after ten minutes, spin again. You won't be.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>Twelve activities balanced across mind and body: go for a walk, call a friend, read a book, watch a movie, cook something new, play a game, do a workout, learn something, tidy one room, take a nap, write or journal, and listen to a podcast. Nothing requires buying anything or leaving your neighborhood.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">The ten-minute contract</h2>
    <p>The trick that makes this wheel work: commit to just ten minutes of whatever it picks. Starting is the hard part — a walk becomes a real walk, one tidy shelf becomes a clean room, one podcast minute becomes an episode. Psychologists call it the Zeigarnik effect; you'll call it finally getting off the couch.</p>
    <ul>
      <li><strong>For kids:</strong> customize it with age-appropriate activities and let them spin — chores disguised as a game work suspiciously well (see the <a href="/wheels/chore-wheel/">Chore Wheel</a>).</li>
      <li><strong>For rainy weekends:</strong> turn on <em>Remove winner after spin</em> and work through the whole wheel.</li>
    </ul>''',
    "faq": [
      ("What if the wheel picks something I can't do right now?",
       "Customize the wheel to match your situation — indoor-only days, kid-friendly lists, or office break versions all work. Or apply the one re-spin rule."),
      ("Why does spinning work better than just choosing?",
       "Choice overload is real: with twelve equal options, your brain stalls comparing them. The wheel removes the comparison step, and starting any activity beats optimizing which one."),
      ("Can I make a version for my kids?",
       "Yes — “Customize this wheel” lets you build a kid-specific list and share it. Their spins feel like a game, not an instruction."),
    ],
  },
  {
    "slug": "workout",
    "name": "Workout Wheel",
    "emoji": "💪",
    "title": "Workout Wheel — Spin for Your Next Exercise | Wheel Of List",
    "og_title": "Workout Wheel — Spin for Your Next Exercise",
    "desc": "Spin the workout wheel for your next exercise: push-ups, squats, plank, burpees and more. Turn any workout into a game — no equipment needed.",
    "subtitle": "Your randomized no-equipment circuit",
    "remove_default": False,
    "entries": ["15 Push-ups", "20 Squats", "60s Plank", "30 Jumping jacks", "12 Lunges each leg", "10 Burpees", "30 Mountain climbers", "20 Sit-ups", "45s Wall sit", "30s High knees"],
    "body": '''    <h1 style="font-size:1.9rem;">Workout Wheel</h1>
    <p>The hardest rep of any workout is deciding to start it. The wheel removes the decision: spin, do what it says, rest, spin again. Ten no-equipment exercises with set reps — a full-body circuit that assembles itself differently every session, which is exactly why it doesn't get boring.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>15 push-ups, 20 squats, a 60-second plank, 30 jumping jacks, 12 lunges per leg, 10 burpees, 30 mountain climbers, 20 sit-ups, a 45-second wall sit and 30 seconds of high knees. Push, legs, core and cardio — all bases covered, zero equipment, doable in a living room.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">Ways to play</h2>
    <ul>
      <li><strong>Classic circuit:</strong> 6–8 spins with 30–45 seconds rest between. Done in under 20 minutes.</li>
      <li><strong>Full sweep:</strong> turn on <em>Remove winner after spin</em> and complete all ten — the wheel guarantees no doubles.</li>
      <li><strong>Group mode:</strong> everyone does whatever the wheel picks, together. Complaining is allowed; skipping is not.</li>
      <li><strong>Leveling:</strong> customize reps to your level — beginners halve them, masochists double them.</li>
    </ul>
    <p><em>As with any exercise: warm up first, keep your form honest, and adapt the list to your body. The wheel is a game, not a personal trainer.</em></p>''',
    "faq": [
      ("Do I need any equipment?",
       "No — all ten exercises are bodyweight-only and fit in a small room. Push-ups, squats, planks and friends."),
      ("How many spins make a full workout?",
       "Six to eight spins with short rests is a solid 15–20 minute session. Or enable “Remove winner after spin” and complete the entire wheel once."),
      ("Can I change the exercises or reps?",
       "Yes — “Customize this wheel” opens the list in the editor. Adjust reps to your level or swap in your favorite movements."),
    ],
  },
  {
    "slug": "date-night",
    "name": "Date Night Wheel",
    "emoji": "💘",
    "title": "Date Night Wheel — Spin for Your Next Date Idea | Wheel Of List",
    "og_title": "Date Night Wheel — Spin for Your Next Date Idea",
    "desc": "Out of date ideas? Spin the date night wheel: cook together, stargaze, game night, picnic and more. Twelve ideas from free to fancy.",
    "subtitle": "Because “I don't know, you pick” isn't a date",
    "remove_default": False,
    "entries": ["Cook together", "Movie night", "Board games", "Picnic", "Stargazing", "New restaurant", "Mini golf", "Museum visit", "Karaoke", "Sunset walk", "Home wine tasting", "Living room dance"],
    "body": '''    <h1 style="font-size:1.9rem;">Date Night Wheel</h1>
    <p>Every couple has the same conversation: "What do you want to do?" — "I don't mind, you choose." Nobody chooses, and you end up watching whatever's on. The wheel is the third party that actually decides. Twelve date ideas, from completely free to slightly fancy, spun without mercy.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>Cook together, movie night, board games, picnic, stargazing, try a new restaurant, mini golf, museum visit, karaoke, sunset walk, home wine tasting, and a living room dance session. Half of them cost nothing — romance is mostly logistics plus intention.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">Rules of engagement</h2>
    <ul>
      <li><strong>The wheel is final.</strong> Land on karaoke? You're singing. That's the game, and honestly, that's the fun.</li>
      <li><strong>Alternate who spins.</strong> One spin per date night; the spinner handles the planning.</li>
      <li><strong>Monthly challenge:</strong> with <em>Remove winner after spin</em> on, work through all twelve over a year — a built-in anti-rut program.</li>
      <li><strong>Personalize it:</strong> swap in your city's specifics — that taco place, the lake trail, the arcade bar. Share the custom link with your partner.</li>
    </ul>''',
    "faq": [
      ("Are these ideas expensive?",
       "Half the wheel is free: stargazing, sunset walks, cooking what's already in the fridge, living room dancing. The other half ranges from cheap (mini golf) to a modest restaurant bill."),
      ("Can we make our own couples wheel?",
       "Yes — “Customize this wheel” lets you build a private version with your favorite spots and inside jokes, then share the link with your partner."),
      ("What if the wheel picks something we did last week?",
       "Turn on “Remove winner after spin” — every date idea comes up exactly once until you reset the wheel."),
    ],
  },
  {
    "slug": "chore-wheel",
    "name": "Chore Wheel",
    "emoji": "🧹",
    "title": "Chore Wheel — Spin to Assign Chores Fairly | Wheel Of List",
    "og_title": "Chore Wheel — Spin to Assign Chores Fairly",
    "desc": "End the chore wars. Spin the chore wheel to randomly assign dishes, laundry, vacuuming and more — fair for roommates, families and couples.",
    "subtitle": "The referee your household needed",
    "remove_default": True,
    "entries": ["Dishes", "Vacuum", "Laundry", "Clean bathroom", "Take out trash", "Mop floors", "Dust shelves", "Water plants", "Clean kitchen", "Wash windows"],
    "body": '''    <h1 style="font-size:1.9rem;">Chore Wheel</h1>
    <p>Every household has one person who "always ends up doing the dishes" and another who has been "about to vacuum" since March. The chore wheel is the neutral referee: chores get assigned by chance, everyone watches the spin, and nobody can argue with physics. <em>Remove winner after spin</em> is on by default — each chore leaves the wheel once it's claimed, so spin until the wheel is empty and the house is covered.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>Dishes, vacuum, laundry, clean bathroom, take out trash, mop floors, dust shelves, water plants, clean kitchen and wash windows. Ten chores that cover a standard week. Got a pet, a yard or a roommate who exclusively generates laundry? Customize the list to match your actual home.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">Three ways to run it</h2>
    <ul>
      <li><strong>Round-robin:</strong> take turns spinning until the wheel is empty. Whatever you land on is yours this week.</li>
      <li><strong>Weekly lottery:</strong> one person spins for everyone on Sunday night; results go on the fridge. The wheel's word is law.</li>
      <li><strong>Kids edition:</strong> customize with age-appropriate chores and small rewards between them — spinning turns "go clean your room" into a game they volunteer for.</li>
    </ul>
    <p>Need to decide who spins first? That's a job for the <a href="/">name wheel</a> — or a quick <a href="/coin-flip/">coin flip</a>.</p>''',
    "faq": [
      ("Why is “Remove winner after spin” on by default here?",
       "Because chores should be assigned exactly once per round. Each spin claims a chore and removes it, so the wheel empties as the week gets covered."),
      ("How do we handle chores nobody wants, like the bathroom?",
       "That's the beauty of the wheel — it doesn't care. Everyone accepts the same risk on every spin, which is the definition of fair."),
      ("Can I adapt it for my family or flat?",
       "Yes — “Customize this wheel” opens the list in the editor. Add pet duties, yard work or split big chores into smaller ones, then share the link with the household."),
    ],
  },
  {
    "slug": "icebreaker-questions",
    "name": "Icebreaker Question Wheel",
    "emoji": "🧊",
    "title": "Icebreaker Question Wheel — Spin to Break the Ice | Wheel Of List",
    "og_title": "Icebreaker Question Wheel — Spin to Break the Ice",
    "desc": "Spin the icebreaker wheel for instant conversation starters. Ten crowd-tested questions for teams, classrooms and meetups — no awkward silences.",
    "subtitle": "Ten questions, zero awkward silences",
    "remove_default": True,
    "entries": ["Your hidden talent?", "Dream vacation spot?", "Best meal you ever had?", "A skill you wish you had?", "Your first job story?", "Favorite childhood show?", "One item on your bucket list?", "Weirdest food you like?", "Your go-to karaoke song?", "Best advice you ever got?"],
    "body": '''    <h1 style="font-size:1.9rem;">Icebreaker Question Wheel</h1>
    <p>"Let's go around and introduce ourselves" is where energy goes to die. Spinning a wheel, though? Suddenly everyone's watching. The wheel picks the question, the randomness makes it feel like a game, and the answers actually get interesting. Built for team meetings, first days of class, workshops and any room full of strangers who need to become people to each other.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">What's on the wheel</h2>
    <p>Ten crowd-tested questions: your hidden talent, dream vacation spot, best meal ever, a skill you wish you had, your first job story, favorite childhood show, one bucket list item, weirdest food you like, go-to karaoke song, and the best advice you ever got. Specific enough to spark stories, safe enough for any workplace.</p>
    <h2 style="font-size:1.4rem; margin-top:2rem;">Formats that work</h2>
    <ul>
      <li><strong>Hot seat:</strong> one person spins, answers, then picks the next victim... volunteer. Questions vanish as they're used (removal is on by default).</li>
      <li><strong>Whole room:</strong> spin once and everyone answers the same question in one sentence. Fastest way to warm up 20+ people.</li>
      <li><strong>Remote standups:</strong> start the Monday call with one spin. Thirty seconds of humanity before the Jira board.</li>
      <li><strong>Your own deck:</strong> customize with team-specific or classroom-appropriate questions and share the link with co-facilitators.</li>
    </ul>
    <p>Need to pick <em>who</em> answers? Put the names on the <a href="/">name wheel</a> and spin both.</p>''',
    "faq": [
      ("Are these questions safe for work?",
       "Yes — all ten avoid politics, religion, relationships and anything HR-adjacent. They invite stories, not confessions."),
      ("Why do questions disappear after each spin?",
       "“Remove winner after spin” is on by default so the same question never comes up twice in one session. Hit Reset wheel to restore the full set."),
      ("Can I use my own questions?",
       "Absolutely — “Customize this wheel” opens the editor where you can write your own deck and share it with a link."),
    ],
  },
]

def schema_json(page):
    app = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": page["name"],
        "applicationCategory": "EntertainmentApplication",
        "operatingSystem": "Web",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "description": page["desc"],
        "url": "https://wheeloflist.com/wheels/%s/" % page["slug"],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://wheeloflist.com/"},
            {"@type": "ListItem", "position": 2, "name": "Wheel Templates", "item": "https://wheeloflist.com/wheels/"},
            {"@type": "ListItem", "position": 3, "name": page["name"], "item": "https://wheeloflist.com/wheels/%s/" % page["slug"]},
        ],
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in page["faq"]
        ],
    }
    return (json.dumps(app, indent=2, ensure_ascii=False),
            json.dumps(breadcrumb, indent=2, ensure_ascii=False),
            json.dumps(faq, indent=2, ensure_ascii=False))

def related_cards(page):
    others = [p for p in PAGES if p["slug"] != page["slug"]]
    idx = [p["slug"] for p in PAGES].index(page["slug"])
    picks = [others[i % len(others)] for i in range(idx, idx + 3)]
    cards = []
    for p in picks:
        cards.append(
            '        <a class="tool-card" href="/wheels/%s/">\n'
            '          <div class="tool-card-icon">%s</div>\n'
            '          <h4>%s</h4>\n'
            '          <p>%s</p>\n'
            '          <div class="tool-card-arrow">→</div>\n'
            '        </a>' % (p["slug"], p["emoji"], p["name"], p["subtitle"]))
    cards.append(
        '        <a class="tool-card" href="/wheels/">\n'
        '          <div class="tool-card-icon">🎯</div>\n'
        '          <h4>All Wheel Templates</h4>\n'
        '          <p>Browse every ready-made wheel in the gallery</p>\n'
        '          <div class="tool-card-arrow">→</div>\n'
        '        </a>')
    return '\n'.join(cards)

def faq_html(page):
    parts = []
    for q, a in page["faq"]:
        parts.append('    <p><strong>%s</strong><br>%s</p>' % (q, a))
    return '\n'.join(parts)

def build_page(page):
    app_j, bc_j, faq_j = schema_json(page)
    wheel_data = json.dumps({"entries": page["entries"], "removeDefault": page["remove_default"]}, ensure_ascii=False)
    html = (TEMPLATE
            .replace('@@TITLE@@', page["title"])
            .replace('@@OG_TITLE@@', page["og_title"])
            .replace('@@DESC@@', page["desc"])
            .replace('@@SLUG@@', page["slug"])
            .replace('@@NAME@@', page["name"])
            .replace('@@EMOJI@@', page["emoji"])
            .replace('@@SUBTITLE@@', page["subtitle"])
            .replace('@@APP_JSON@@', app_j)
            .replace('@@BREADCRUMB_JSON@@', bc_j)
            .replace('@@FAQ_JSON@@', faq_j)
            .replace('@@BODY@@', page["body"])
            .replace('@@FAQ_HTML@@', faq_html(page))
            .replace('@@RELATED@@', related_cards(page))
            .replace('@@WHEEL_DATA@@', wheel_data)
            .replace('@@NAV@@', NAV)
            .replace('@@FOOTER@@', FOOTER))
    out_dir = os.path.join(ROOT, 'wheels', page["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.htm'), 'w', encoding='utf-8') as f:
        f.write(html)
    return page["slug"]

GALLERY_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Wheel Templates — Ready-Made Decision Wheels | Wheel Of List</title>
  <meta name="description" content="Ready-made decision wheels you can spin right now: what to eat, truth or dare, what to watch, workouts, chores and more. Free, no sign-up.">
  <meta name="robots" content="index, follow">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="https://wheeloflist.com/wheels/">
  <meta name="theme-color" content="#3369e8">
  <link rel="icon" href="/favicon.ico">
  <meta property="og:title" content="Wheel Templates — Ready-Made Decision Wheels">
  <meta property="og:description" content="Spin ready-made wheels: what to eat, truth or dare, what to watch, workouts, chores and more.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://wheeloflist.com/wheels/">
  <meta property="og:site_name" content="Wheel Of List">
  <meta property="og:image" content="https://wheeloflist.com/og.jpg">
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
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XV614N2RLR');
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
  <script type="application/ld+json">
@@BREADCRUMB_JSON@@
  </script>
  <script type="application/ld+json">
@@ITEMLIST_JSON@@
  </script>
</head>
<body>
  <script>try{if(localStorage.getItem('wheeloflist_theme')==='dark')document.body.classList.add('dark-theme');}catch(e){}</script>

@@NAV@@

  <main class="container" style="max-width: 1000px; padding: 40px 20px;">
    <h1 style="font-size:2rem; text-align:center;">Wheel Templates</h1>
    <p style="text-align:center; max-width:680px; margin: 0 auto 2rem;">Ready-made wheels for life's recurring dilemmas. Every template spins right on its page — no setup, no sign-up — and every one can be customized in the <a href="/">full editor</a> and shared with a link.</p>

    <section class="quick-tools-section">
      <div class="tools-grid">
@@CARDS@@
      </div>
    </section>

    <h2 style="font-size:1.4rem; margin-top:3rem;">Build your own wheel</h2>
    <p>These templates are starting points. Open any of them and hit <strong>“Customize this wheel”</strong> to edit the options in the full <a href="/">Wheel of List editor</a> — or start from scratch: type your own list, spin, and share your wheel with anyone using the share link. Teachers build vocabulary wheels, streamers build challenge wheels, families build weekend wheels. Whatever you're deciding, there's a wheel for it — and if there isn't, you can make it in under a minute.</p>

    <h2 style="font-size:1.4rem; margin-top:2rem;">More decision tools</h2>
    <p>Binary choice? Try the <a href="/coin-flip/">Coin Flip</a> or the <a href="/yes-no-wheel/">Yes or No Wheel</a>. Splitting people instead of choosing options? The <a href="/team-generator/">Team Generator</a> handles groups, and the <a href="/raffle-picker/">Raffle Picker</a> draws winners from any list.</p>
  </main>

@@FOOTER@@

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script src="/consent.js" defer></script>
</body>
</html>
'''

def build_gallery():
    cards = []
    for p in PAGES:
        cards.append(
            '        <a class="tool-card" href="/wheels/%s/">\n'
            '          <div class="tool-card-icon">%s</div>\n'
            '          <h4>%s</h4>\n'
            '          <p>%s</p>\n'
            '          <div class="tool-card-arrow">→</div>\n'
            '        </a>' % (p["slug"], p["emoji"], p["name"], p["subtitle"]))
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://wheeloflist.com/"},
            {"@type": "ListItem", "position": 2, "name": "Wheel Templates", "item": "https://wheeloflist.com/wheels/"},
        ],
    }
    itemlist = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Wheel Templates",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": p["name"],
             "url": "https://wheeloflist.com/wheels/%s/" % p["slug"]}
            for i, p in enumerate(PAGES)
        ],
    }
    html = (GALLERY_TEMPLATE
            .replace('@@CARDS@@', '\n'.join(cards))
            .replace('@@BREADCRUMB_JSON@@', json.dumps(breadcrumb, indent=2, ensure_ascii=False))
            .replace('@@ITEMLIST_JSON@@', json.dumps(itemlist, indent=2, ensure_ascii=False))
            .replace('@@NAV@@', NAV)
            .replace('@@FOOTER@@', FOOTER))
    with open(os.path.join(ROOT, 'wheels', 'index.htm'), 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    for page in PAGES:
        print('built /wheels/%s/' % build_page(page))
    build_gallery()
    print('built /wheels/ gallery')
    print('%d template pages + gallery' % len(PAGES))
