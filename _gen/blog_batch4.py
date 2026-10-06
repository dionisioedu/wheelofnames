#!/usr/bin/env python3
"""Blog batch 4 — Guides (how-to for each tool) + a product News post.

Guides teach the *use* of each tool; the News post announces recent changes.
Each article dict: slug, emoji, title, h1, desc, body, category.
"""
from blog_lib import cta, cta_wheel

ARTICLES = [
# ------------------------------------------------------------------ GUIDES
{
"slug": "how-to-use-a-wheel-spinner",
"category": "guides",
"emoji": "🎡",
"title": "How to Use a Wheel Spinner (Complete Guide) | Wheel Of List",
"h1": "How to Use a Wheel Spinner",
"desc": "Everything the wheel can do: adding names, images, weights, presets, sharing a wheel by link, and when to spin instead of deciding yourself.",
  "faqs": [
    ("Is the wheel of names truly random?",
     "Yes. Every segment has an equal chance on every spin, and the winner is whichever segment lands under the pointer when the wheel stops. Nothing is weighted toward earlier or later names."),
    ("How many names can I add to a wheel spinner?",
     "You can paste dozens of names or items. Up to about 12 segments stay readable; beyond that the labels shrink, so for very long lists use the Random Number Generator or Raffle Picker instead."),
    ("Can I save a wheel and reuse it later?",
     "Yes. Use \"Copy link\" to share the exact list as a URL, or save it under My Wheels so it loads again with one click next class or next event."),
  ],
"body": """
<p>A wheel spinner looks like a toy and works like a decision machine. You put options on it, spin, and physics picks one so nobody has to. This guide walks through every feature of the <a href="/">Wheel Of List spinner</a> — from your first spin to shared, weighted, image-based wheels — so you can use it for anything from picking a restaurant to running a live giveaway.</p>

<h2>1. Add your options</h2>
<p>Type names into the list on the left, one per line. Each line becomes a slice. You can also paste a whole column from a spreadsheet and the wheel rebuilds instantly. Hit <strong>Spin</strong> in the middle (or click the wheel) and it lands on one slice at random.</p>

<h2>2. Make the wheel recognisable (images)</h2>
<p>Paste an image URL next to a name and the slice shows the picture instead of text — logos for teams, photos for people, emoji for themes. This is what makes the wheel feel like a game rather than a form.</p>

<h2>3. Weight the odds (without rigging them)</h2>
<p>Sometimes a fair spin isn't what you want. Give an entry a bigger weight and it takes up a proportionally larger slice, so it wins more often. Weighting is the honest way to express "I want X twice as likely as Y" — everyone can see the slice sizes, so it's transparent, not a trick. Use it for: weighting giveaway entries by number of tickets, favouring a restaurant you all secretly want, or giving a beginner a bigger slice in a party game.</p>

<h2>4. Save presets you reuse</h2>
<p>Lunch options, a chore list, a class roster — if you spin the same list weekly, save it as a preset. Presets also generate clean shareable links, so the whole list travels with the URL: send <code>wheeloflist.com/?items=...</code> to a friend and they open your exact wheel.</p>

<h2>5. Share the wheel by link</h2>
<p>Click <strong>Copy link</strong> and the current list is encoded into the URL. This is the fastest way to run a remote giveaway or let a group add names: everyone opens the same wheel, nobody retypes anything. For Instagram or YouTube giveaways, paste your commenter list, spin once on camera, done.</p>

<h2>6. Sound, themes and editing in place</h2>
<p>The wheel ticks as each slice passes and plays a win sound on landing (mute it with the speaker button). Ten colour themes let you match the mood — from plain light mode to neon and retro arcade. Double-click a slice to rename it; drag to reorder.</p>

<h2>When to use a wheel (and when not to)</h2>
<p>Use a wheel when the decision is genuinely arbitrary, when you want consensus without negotiation, or when you need the choice to <em>look</em> random and unarguable (dish duty, seat order, who goes first). Don't use a wheel when real preferences exist — a wheel can't discover that half your group hates mushrooms. Decide the options honestly, then let the wheel pick.</p>

<h2>Common tasks</h2>
<table>
<tr><th>You want to…</th><th>Do this</th></tr>
<tr><td>Pick a random winner</td><td>Paste the entries, spin once. Use weights for extra tickets.</td></tr>
<tr><td>Let everyone see the same wheel</td><td>Copy link, share the URL.</td></tr>
<tr><td>Choose among unequal odds</td><td>Set the weight column, keep it visible.</td></tr>
<tr><td>Run a themed party game</td><td>Open a Wheel Template like Truth or Dare.</td></tr>
</table>
""" + cta_wheel("Try it now",
"Add your list and spin — no sign-up, works offline once loaded.",
["Pizza", "Sushi", "Burgers", "Tacos", "Salad"], "Spin the wheel →") + """
""",
},
{
"slug": "how-to-run-a-fair-giveaway",
"category": "guides",
"emoji": "🏆",
"title": "How to Run a Fair Raffle Online (Step by Step) | Wheel Of List",
"h1": "How to Run a Fair Raffle",
"desc": "Step-by-step: import entries, add ticket weighting, spin live and prove the draw was fair. Handles late entries, ties, and recording the winner.",
  "faqs": [
    ("How do I prove my raffle wasn't rigged?",
     "Record the draw on camera, state the number of entries aloud before spinning, and use a tool that picks live. Showing the full entry list and the spin in one unbroken clip is the simplest proof."),
    ("What is ticket weighting and when should I use it?",
     "Weighting gives some entries more chances than others - useful when people earn extra entries by sharing or referring. Add each person's name once per ticket so the odds stay transparent."),
    ("Can I run a raffle with more than one winner?",
     "Yes. The Raffle Picker draws multiple non-repeating winners in one run, with silver and bronze medals for 2nd and 3rd place."),
  ],
"body": """
<p>Running a giveaway looks easy until someone asks \"how do I know you didn't just pick your friend?\" This guide gives you a method that produces a provably random winner <em>on camera</em>, using the <a href="/raffle-picker/">Raffle Picker</a> and the <a href="/">wheel</a>. It takes about two minutes per giveaway.</p>

<h2>Step 1 — Collect entries in one list</h2>
<p>One entry per line. Copy them from your Instagram comments, a Google Sheet column, or a form export. Plain text only — no numbering, no formatting. If someone commented five times and the rules allow it, paste five lines.</p>

<h2>Step 2 — Do you need weighting?</h2>
<p>If entries are equal, skip this. If some people get more tickets (bought extra, are subscribers, etc.), use the weight column. Weighting by tickets is the difference between a fair raffle and a popularity contest — and because weights are visible, it's honest.</p>

<h2>Step 3 — Spin it live and record</h2>
<p>Screen-record the spin. The wheel's randomness comes from the browser's cryptographic random source, and the reduced-motion / tick-by-tick animation makes the spin verifiable: viewers watch the pointer cross every slice. Don't cut the clip between list and result.</p>

<h2>Step 4 — Prove the pool size</h2>
<p>Before spinning, scroll the list so the total count is visible, or state it: \"137 entries.\" After the spin, the winner is highlighted. A recorded spin over a visible pool is more credible than any RNG screenshot — the audience watched every entry exist and every slice get a chance.</p>

<h2>Step 5 — Announce and record the backup</h2>
<p>Spin twice: winner and a runner-up (in case the winner is ineligible or doesn't reply). Announce the winner, tell people how to reply, and set a deadline.</p>

<h2>Handling the awkward cases</h2>
<p><strong>Someone cheated entries.</strong> Remove them before the spin and say so. Better to correct the pool in public than to silently ignore it.</p>
<p><strong>Winner doesn't respond.</strong> That's what the runner-up spin is for. Say clearly how long you'll wait.</p>
<p><strong>You want the entry list reproducible.</strong> Copy link encodes the exact list into the URL — save that link in your post description or a pinned comment so anyone can re-open the identical pool.</p>

<h2>Facebook, Instagram and YouTube</h2>
<p>The flow is identical everywhere: export the entries, paste, spin on camera, show the count. Instagram favours a full screen-recording; YouTube lets you keep the whole thing as an unlisted video you link in the description. For a live stream, keep the wheel open in a browser tab and spin on cue.</p>

<h2>Fairness rules worth stating up front</h2>
<p>State: how to enter, whether multiple entries count, the entry deadline, the prize, and how the winner is chosen at random. Writing these down protects you from disputes later and makes the whole thing feel like a game rather than a favour.</p>
""" + cta("Ready to draw a winner?",
"Paste your entries, spin on camera, and copy the link so anyone can verify the pool.",
"/raffle-picker/", "Open the Raffle Picker →") + """
""",
},
{
"slug": "how-to-pick-random-teams",
"category": "guides",
"emoji": "👥",
"title": "How to Split People Into Random Teams (Fairly) | Wheel Of List",
"h1": "How to Split People Into Random Teams",
"desc": "Random team generation for sports, classrooms and game nights — how many teams, how to keep it fair, and how to avoid repeat pairings across weeks.",
  "faqs": [
    ("How do I split people into fair random teams?",
     "Paste all names, choose the number of teams (or players per team), and shuffle. The generator deals round-robin after a Fisher-Yates shuffle, so team sizes stay even and no one can influence the draw."),
    ("Should the number of teams or players per team come first?",
     "Pick whichever constraint is fixed. If you need exactly 4 teams, choose team count. If each team must have 2 players, choose players per team and the generator works out the team count."),
    ("Can I keep certain people together or apart?",
     "Not automatically. Keep it fully random for fairness, then swap one or two names manually if you need to separate a pair - note the swap so everyone sees it was transparent."),
  ],
"body": """
<p>Dividing a group into teams by hand is a minefield: the same cliques form, the same two people end up together, and someone always claims it's rigged. Random team generation fixes all three in a single click. This guide uses the <a href="/team-generator/">Team Generator</a>.</p>

<h2>Step 1 — Enter the players</h2>
<p>One name per line. You can add a skill level or handicap next to each name if you're balancing a game that cares (see below).</p>

<h2>Step 2 — Choose how many teams</h2>
<p>Pick a team count and the generator splits the roster as evenly as possible, randomly each time. For odd numbers it places the extra player sensibly rather than dumping two people on one team.</p>

<h2>Step 3 — Balancing by skill (optional)</h2>
<p>For recreational sports, pure random can produce a stacked team and a sad team. Assign each player a skill value and let the generator distribute them — you get random <em>and</em> balanced, which random alone can't guarantee.</p>

<h2>Step 4 — Avoid repeat pairings across weeks</h2>
<p>If you play weekly, pure randomness will repeat pairings and people notice. The trick: keep a note of last week's teams and reshuffle until the overlap is small, or simply rerun the generator and eyeball it — a reroll only takes a second. For serious leagues, track pairings in a sheet and treat today's draw as a constraint.</p>

<h2>Classroom use</h2>
<p>For group work, team generation removes the social sting of being picked last: nobody chose, the physics did. Announce the rules first (size, whether groups are fixed all term), then generate once and let students see the result. Rerolling to engineer a result undermines the whole point — spin once.</p>

<h2>Party games and sports</h2>
<table>
<tr><th>Situation</th><th>Recommended</th></tr>
<tr><td>Backyard football, mixed ability</td><td>Skill-balanced teams</td></tr>
<tr><td>Board game night, 8 people, 2 tables</td><td>Pure random, reroll if lopsided</td></tr>
<tr><td>Classroom group project</td><td>Pure random, fixed for the term</td></tr>
<tr><td>Trivia, rotating pairs</td><td>Random each round</td></tr>
</table>
""" + cta("Split your group now",
"Paste names, pick a team count, get balanced random teams in one click.",
"/team-generator/", "Generate teams →") + """
""",
},
{
"slug": "how-to-use-dice-roller",
"category": "guides",
"emoji": "🎲",
"title": "How to Use a Dice Roller (D&D, Board Games, Teaching) | Wheel Of List",
"h1": "How to Use a Dice Roller",
"desc": "Roll d4 to d100 online: why digital dice are as fair as physical ones, how to roll pools for tabletop RPGs, and how to use dice to teach probability.",
  "faqs": [
    ("What dice can I roll online?",
     "Standard polyhedrals: d4, d6, d8, d10, d12 and d20, plus multiple dice at once. Each result is independent, so rolling three d6 is the same as rolling one d6 three times."),
    ("Is an online dice roller fair for tabletop games?",
     "Yes. A digital roller uses the same uniform random source as a fair physical die - each face has an equal chance every roll, and it cannot be biased by a worn edge or a bad throw."),
    ("How do I roll with advantage or add modifiers?",
     "Roll two d20s and keep the higher (advantage) or lower (disadvantage), then add your modifier to the kept result. The roller shows every die so you can apply the rule yourself."),
  ],
"body": """
<p>A digital dice roller is the same maths as a physical die, minus the die that rolled under the sofa. This guide covers the <a href="/dice-roller/">Dice Roller</a> for tabletop games, board games and teaching — plus the one thing that actually matters: making sure the roll is fair.</p>

<h2>Rolling standard dice</h2>
<p>Choose a die size — d4, d6, d8, d10, d12, d20, d100 — and roll. A d6 gives 1–6 with equal probability, exactly like the plastic one in your hand. The generator uses the browser's cryptographic random source, so there's no bias toward neat-looking numbers.</p>

<h2>Tabletop RPGs: pools and modifiers</h2>
<p>For a d20 attack roll with a +5 modifier, roll the d20 and add five mentally — or roll a pool of dice at once for damage (2d6, 3d8, etc.) and read the total. Rolling several dice at once is much faster than tapping a single die repeatedly, and the history shows each individual result so you can verify a crit.</p>

<h2>Are digital dice as fair as real ones?</h2>
<p>For most dice, yes — arguably fairer. Physical dice have manufacturing bias (rounded corners, uneven density) that shows up in long statistical tests. A cryptographically-seeded software die has no manufacturing tolerance. The caveat is trust: you have to trust the software. On Wheel Of List the roll is client-side and the code is simple; you can watch the history accumulate and test the distribution yourself.</p>

<h2>Teaching probability with dice</h2>
<p>Dice are the cheapest probability lab there is. Have students roll a d6 fifty times and tally the results — the bars flatten toward equal as the count grows (that's the law of large numbers). Then roll 2d6 and tally the <em>sums</em>: 7 dominates because more combinations make it. This single exercise teaches uniform vs. triangular distributions better than any worksheet.</p>

<h2>Board games and quick decisions</h2>
<p>Lost the physical die? Roll a d6 on your phone. Need a random move in a homebrew game? d4. Need 1–100 for a loot table? d100. The roller replaces every die in the box, and it never gets knocked off the table mid-game.</p>
""" + cta("Roll some dice",
"Pick a die size and roll — single dice or pools, with a running history.",
"/dice-roller/", "Open the Dice Roller →") + """
""",
},
{
"slug": "how-to-use-random-number-generator",
"category": "guides",
"emoji": "🔢",
"title": "How to Use a Random Number Generator (Ranges, Seeds)",
"h1": "How to Use a Random Number Generator",
"desc": "Generate random integers or decimals in any range: how to set a min and max, when you need a whole number, and how to avoid the classic off-by-one mistake.",
  "faqs": [
    ("Is an online random number generator truly random?",
     "For practical purposes, yes. It draws from the browser's cryptographic random source, which is unguessable and evenly distributed - far more random than asking a person to pick a number."),
    ("Can I generate decimals or negative numbers?",
     "Yes. Set a minimum and maximum of any size, including negatives and decimals like -1.5 to 1.5, and the generator returns a value in that range with uniform probability."),
    ("Can I pick a number without repeats?",
     "For a single draw, run it once. For several unique numbers in a range - like a lottery - use the Raffle Picker, which removes each winner before drawing the next."),
  ],
"body": """
<p>A random number generator is the tool for when the options aren't names but numbers: a number between 1 and 100, a decimal test value, an index to pick from a list you keep elsewhere. This guide covers the <a href="/random-number/">Random Number Generator</a> and the mistakes people make with ranges.</p>

<h2>Setting a range</h2>
<p>Enter a minimum and a maximum, then generate. By default you get a whole number in that range, <em>inclusive</em> — min 1, max 10 can return a 1 or a 10, not just 2 through 9. That inclusiveness is the single most common point of confusion. If you need 1–10 without the endpoints, set 2–9.</p>

<h2>Whole numbers vs. decimals</h2>
<p>Use integers for counting (picking a numbered seat, a lottery number, a page in a book). Use decimals when you're generating test data, simulating a percentage, or need a value between 0 and 1. You can control how many decimal places you get.</p>

<h2>The off-by-one trap</h2>
<p>\"Pick a number from 1 to 6\" and \"roll a die\" should give the same answers — both inclusive of 1 and 6. If your generator treats the max as exclusive, your \"d6\" is really a d5 plus one and the distribution is wrong. Always check whether the max is included, and state the range out loud when it matters.</p>

<h2>Uniform means uniform</h2>
<p>A good generator gives every value in the range equal probability. That matters in tests: if you generate 1–100 a thousand times, each value should appear about ten times. Run it a few thousand times and check — that's how you demo the law of large numbers, and how you catch a bad generator.</p>

<h2>Practical uses</h2>
<table>
<tr><th>Task</th><th>Setup</th></tr>
<tr><td>Lottery / door prize number</td><td>Integers 1–N inclusive</td></tr>
<tr><td>Pick a page to read to</td><td>Integers 1–total pages</td></tr>
<tr><td>Test data</td><td>Decimals, several places</td></tr>
<tr><td>Random delay simulation</td><td>Decimals in seconds</td></tr>
<tr><td>Assign a number to each student</td><td>Integers 1–class size</td></tr>
</table>
<p>If your options have names instead of numbers, the <a href="/">wheel</a> is usually clearer — people can see the options. Use numbers when the list lives elsewhere or you genuinely just need a value.</p>
""" + cta("Generate a number",
"Set your min and max and generate — integers or decimals, inclusive ranges.",
"/random-number/", "Open the generator →") + """
""",
},
{
"slug": "how-to-decide-with-coin-flip",
"category": "guides",
"emoji": "🪙",
"title": "How to Use a Coin Flip to Decide (and When Not To) | Wheel Of List",
"h1": "How to Use a Coin Flip to Decide",
"desc": "A digital coin flip is the fastest two-way decision there is. How to use it, why it's fair, and the psychology trick that reveals what you actually wanted.",
  "faqs": [
    ("Is flipping a coin actually 50/50?",
     "For a fair coin, yes - heads and tails each have a 50% chance on every flip. Online flips use a uniform random source, so they are exactly 50/50 with no bias from a thumb or an uneven coin."),
    ("When is a coin flip a bad way to decide?",
     "When the outcomes are not equally desirable. If you'd be disappointed by one result, you already know your preference - flipping just adds delay. Coin flips suit genuinely balanced, low-stakes choices."),
    ("Can I flip many coins or track the streak?",
     "Yes. The Coin Flip tool keeps a running heads/tails count and current streak, which is a neat way to see that long streaks are normal, not a sign of a rigged coin."),
  ],
"body": """
<p>Heads or tails is the oldest randomiser in the book and still the fastest. The <a href="/coin-flip/">Coin Flip</a> gives you a fair 50/50 in one click — no coin, no thumb, no \"that was definitely tails.\" Here's how to use it well, and one trick that makes it more useful than you'd expect.</p>

<h2>Why a digital flip is fair</h2>
<p>A real coin flip is close to 50/50 but not exact — spin, catch and thumb all add bias, and studies have measured real flips landing on the starting side slightly more often. A software flip samples the browser's cryptographic random source with no physical bias at all. If you need a provably fair two-way choice in front of an audience, digital wins on trust.</p>

<h2>How to run it</h2>
<p>Open the tool, click Flip, read the result. Run it repeatedly for best-of-three or to generate a sequence. That's it — the value is in the speed, not the settings.</p>

<h2>Two-way decisions it's perfect for</h2>
<p>Who pays for coffee. Who drives. Which of two restaurants. Who takes the first turn. Any genuine 50/50 where neither option is better and arguing would take longer than deciding. The moment the decision is binary and arbitrary, a coin flip is the optimal tool.</p>

<h2>The trick that reveals your preference</h2>
<p>Here's the psychology bit: when a coin flip says an option you secretly dislike and you feel a flicker of disappointment, you've just learned your real preference. The flip didn't decide — it revealed. If you're happy, go with the coin. If you're disappointed, ignore the coin and do the other thing. Either way you stopped being stuck, which was the actual problem.</p>

<h2>When a coin flip is the wrong tool</h2>
<p>More than two options — use the <a href="/">wheel</a> or the <a href="/random-number/">number generator</a>. Weighted odds — use weights. A decision that actually matters and deserves thought — a coin flip will just postpone it. The tool is for arbitrary binaries, not for outsourcing judgement you should do yourself.</p>
""" + cta("Flip a coin",
"Heads or tails, fair and instant — run best-of-three if you're feeling competitive.",
"/coin-flip/", "Flip the coin →") + """
""",
},
{
"slug": "how-to-run-a-tournament-bracket",
"category": "guides",
"emoji": "🏟️",
"title": "How to Run a Tournament Bracket (Setup, Seeding, Tie-breaks)",
"h1": "How to Run a Tournament Bracket",
"desc": "Build a single-elimination bracket for any group size: seeding, byes, randomising the draw fairly, and what to do when a match ends tied.",
  "faqs": [
    ("How do I seed a tournament bracket?",
     "Either randomize the draw or place ranked players so top seeds meet later. The generator handles byes automatically when the player count is not a power of two, so nobody sits out unfairly."),
    ("What happens with an odd number of players?",
     "The bracket rounds up to the next power of two and gives the surplus players a first-round bye, assigned at random for fairness."),
    ("Can I change a result after the tournament starts?",
     "Yes. Changing a match result resets and re-propagates every later round, so downstream brackets update automatically instead of leaving stale winners."),
  ],
"body": """
<p>A bracket turns a pile of players into a champion. Doing it by hand means drawing lines, erasing names and getting the byes wrong. The <a href="/tournament/">Tournament Bracket</a> builds it for you, any size. This guide covers the setup decisions that actually matter.</p>

<h2>Step 1 — Choose the format</h2>
<p><strong>Single elimination</strong> is fastest: lose once and you're out. Perfect for a lunchtime FIFA tournament or a quick office Smash Bros. crown. <strong>Double elimination</strong> gives everyone a second life so one bad match doesn't end an early favourite, at the cost of roughly double the matches. For most casual events, single elimination with randomised seeding is right.</p>

<h2>Step 2 — Seed or randomise</h2>
<p>Seeding places the strongest players apart so the two best meet only in the final. It's fairer to the favourites but predictable and can feel elitist. Randomising the whole draw is simpler and more exciting: anyone can get a brutal first round. Either is defensible — just pick one and announce it <em>before</em> the draw so nobody accuses you of engineering easier matchups.</p>

<h2>Step 3 — Handle byes</h2>
<p>If your player count isn't a power of two (4, 8, 16, 32), some players get a first-round bye. The generator assigns byes automatically and distributes them so they're spread across the bracket rather than dumped on one side. Don't do this by hand — misassigned byes are the number-one way to make a bracket unfair.</p>

<h2>Step 4 — Run the matches</h2>
<p>Advance winners into the next round as results come in. The bracket updates visually, so everyone can see who's next. Post the link (copy it) so players check their own matches instead of asking you.</p>

<h2>Tie-breaks</h2>
<p>Every tournament needs a tie rule decided up front. For games with scores, use goal differential. For anything else, replay the deciding match, or highest seed advances, or — most cleanly — a single coin flip, decided in public. Pick one rule and apply it consistently; inconsistency in tie-breaks is what turns a fun bracket into an argument.</p>

<h2>Player counts</h2>
<table>
<tr><th>Players</th><th>First round</th><th>Byes</th></tr>
<tr><td>8</td><td>4 matches</td><td>0</td></tr>
<tr><td>12</td><td>4 matches</td><td>4</td></tr>
<tr><td>16</td><td>8 matches</td><td>0</td></tr>
<tr><td>20</td><td>4 matches</td><td>12</td></tr>
</table>
<p>Big gaps in bye counts are normal and fine — the goal is equal opportunity to win the <em>event</em>, not the same number of matches per person.</p>
""" + cta("Build your bracket",
"Enter players, pick single or double elimination, and run the draw.",
"/tournament/", "Open the Bracket Builder →") + """
""",
},
{
"slug": "how-to-get-out-of-a-decision-rut",
"category": "guides",
"emoji": "🧭",
"title": "Four Tools to Stop Being Stuck on a Decision | Wheel Of List",
"h1": "Four Tools to Stop Being Stuck on a Decision",
"desc": "A quick map of which Wheel Of List tool to reach for depending on the decision in front of you — two options, many options, weighted odds, or a whole group.",
  "faqs": [
    ("How does randomness help me decide?",
     "When options are close, deliberating longer rarely changes the answer - it just costs time. Letting chance pick breaks the tie and hands you the decision, and your reaction to the result often reveals what you actually wanted."),
    ("Which tool should I use for a decision?",
     "Two options: a coin flip for a straight binary choice, or a wheel with all the options written out for three or more."),
    ("What if I dislike the result?",
     "That reaction is the answer. If the pick disappoints you, the other option was the one you wanted - take it and move on. Chance is a mirror for your real preference, not a replacement for it."),
  ],
"body": """
<p>Most \"I can't decide\" problems aren't about the options — they're about the decider. Different decisions need different tools, and picking the right one is half the fix. Here's the map, in roughly increasing complexity.</p>

<h2>Two options, genuinely equal → Coin Flip</h2>
<p>Coffee or tea. Walk or bus. Today's plan or tomorrow's. When two choices are truly tied, a <a href="/coin-flip/">coin flip</a> ends it in one click, and any flicker of disappointment tells you your real preference (see the coin-flip guide).</p>

<h2>A short list of options → Wheel</h2>
<p>Three to twenty named options that everyone should <em>see</em>. Restaurants, movies, chores, who's next. The <a href="/">wheel</a> shows the options as slices so the group trusts the result, and it's the most fun of the four, which matters when the decision is social.</p>

<h2>Weighted or unequal odds → Wheel with weights</h2>
<p>When some options should win more often — more tickets, a favourite, a handicap — use the wheel's weight column. Everyone can see the slice sizes, so it's transparent rather than sneaky. This is also the honest way to run a raffle where entries differ.</p>

<h2>A number, not a name → Random Number Generator</h2>
<p>Picking a lottery number, a page, a seat, or generating test values. Use the <a href="/random-number/">number generator</a> and remember the range is inclusive of both ends.</p>

<h2>A whole group → Team Generator or Bracket</h2>
<p>Need to split people → <a href="/team-generator/">Team Generator</a>. Need to run a competition → <a href="/tournament/">Tournament Bracket</a>. Both remove the social friction of someone choosing, which is the entire point.</p>

<h2>The meta-rule</h2>
<p>Before reaching for any tool, ask: do I actually have a preference I'm avoiding? If yes, the tool can't help — decide. If no, the decision is genuinely arbitrary and any of these tools will do the job faster than agonising. The tool isn't there to think for you; it's there to stop a non-decision eating twenty minutes of your day.</p>
""" + cta("Pick your tool",
"Ten tools for ten kinds of decision — start with the wheel and branch out.",
"/tools/", "Browse all tools →") + """
""",
},
# ------------------------------------------------------------------ NEWS
{
"slug": "product-update-themes-sounds-templates",
"category": "news",
"emoji": "🆕",
"title": "What's New: Themes, Sounds and 16 Templates",
"h1": "What's New: Themes, Sounds and 16 Wheel Templates",
"desc": "A round of updates across the site: ten colour themes, sound on every game, double the wheel templates, and a fresh look for the favicon.",
  "faqs": [
    ("How many themes are there now?",
     "Ten, from Light and Night to Neon, Ocean, Sunset, Forest, Candy, Retro, Paper and Midnight. Your choice is saved in the browser and applies across every tool."),
    ("Where did the sounds go?",
     "Every game now has sound effects - spin ticks, dice rolls, coin flips and a winner chime - synthesised in the browser with no downloads. A mute button in the corner turns them off and remembers your choice."),
    ("How many wheel templates are available?",
     "Sixteen ready-made wheels, including Who Pays?, Prize Wheel, Random Movie, Party Games, Baby Names, Christmas Movies and Study Break - each loads instantly with its list already filled in."),
  ],
"body": """
<p>A batch of updates just shipped across Wheel Of List. Here's what changed and why, in plain terms.</p>

<h2>Ten colour themes</h2>
<p>The site used to be light or dark. Now there are ten themes — from a warm Paper and a plain Light through Forest, Sunset and Deep Ocean to Neon Cyberpunk, Retro Arcade and Midnight Blue. Pick one from the selector in the header; your choice is saved and carries across every page and tool. Prefer the system-style binary? Light and Night are still there.</p>

<h2>Sound on every game</h2>
<p>The wheel has always ticked as it spun and chimed on the win. Now every tool does: the coin rings as it flips, the dice rattle as they roll, the wheel ticks past each slice. Every sound is generated in the browser — no downloads, instant, and works offline. A speaker button in the corner mutes everything if you spin in a quiet room, and your mute choice is remembered.</p>

<h2>Sixteen Wheel Templates</h2>
<p>Ready-made wheels doubled from 8 to 16. New arrivals include <strong>Who Pays?</strong> (settle the bill with a spin), <strong>Prize Wheel</strong> (a classic carnival wheel for giveaways), <strong>Random Movie</strong>, <strong>First-Date Questions</strong>, <strong>Party Games</strong>, <strong>Baby Names</strong>, <strong>Christmas Movies</strong> and <strong>Study Break</strong>. Each opens pre-loaded — spin immediately or edit the list. Browse them all on the <a href="/wheels/">Templates page</a>.</p>

<h2>A Guides section on the blog</h2>
<p>The blog now separates <strong>Guides</strong> (how to use each tool) from <strong>Theory</strong> (game theory and probability) and <strong>News</strong> (this kind of post). Filter with the buttons at the top of the <a href="/blog/">blog index</a>. If you've ever wondered how to run a fair giveaway or split teams without a fight, the guides have you covered.</p>

<h2>A proper icon</h2>
<p>The old favicon is gone. The browser tab, the mobile home-screen icon and the installable app icon are now all the brand wheel mark, at every size. The site is also installable as an app — look for the install prompt after you've spun a few times.</p>

<h2>What's next</h2>
<p>More guides, a little more polish on the wheel editor, and continued work on making every tool fast on a phone. If there's a tool or template you'd find useful, the feedback buttons at the bottom of each page come straight to us.</p>
""" + cta("See the templates",
"Sixteen ready-made wheels — spin one immediately or edit the list to fit.",
"/wheels/", "Browse Wheel Templates →") + """
""",
},
]

if __name__ == "__main__":
    print("%d articles in batch 4" % len(ARTICLES))
