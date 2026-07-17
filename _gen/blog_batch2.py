#!/usr/bin/env python3
"""Blog batch 2 — probability cluster."""
from blog_lib import cta

ARTICLES = [
{
"slug": "dice-probability-guide",
"emoji": "🎲",
"title": "Dice Probability 101: Why 7 Rules the Table | Wheel Of List Blog",
"h1": "Dice Probability 101: Why 7 Rules the Table",
"desc": "One die is flat, two dice make a pyramid, and that pyramid quietly runs Catan, Craps and Monopoly. The essential numbers, no math degree required.",
"body": """
<p>A single die is probability at its most boring: every face, exactly 1 in 6, about 16.7%. No number is hot, none is due, and the die has no memory. The interesting things start happening the moment you add a second die — because sums don't inherit that flatness. They form a pyramid, and that pyramid secretly runs half the games in your closet.</p>

<h2>The two-dice pyramid</h2>
<p>Two dice produce 36 equally likely combinations, but only 11 different sums. The sums in the middle can be made more ways than the ones at the edges:</p>
<table>
<tr><th>Sum</th><th>Ways</th><th>Probability</th></tr>
<tr><td>2 or 12</td><td>1 each</td><td>2.8%</td></tr>
<tr><td>3 or 11</td><td>2 each</td><td>5.6%</td></tr>
<tr><td>4 or 10</td><td>3 each</td><td>8.3%</td></tr>
<tr><td>5 or 9</td><td>4 each</td><td>11.1%</td></tr>
<tr><td>6 or 8</td><td>5 each</td><td>13.9%</td></tr>
<tr><td><strong>7</strong></td><td><strong>6</strong></td><td><strong>16.7%</strong></td></tr>
</table>
<p>Seven can be built six ways (1+6, 2+5, 3+4, 4+3, 5+2, 6+1). Twelve can be built exactly one way. That's the whole secret: no magic, just counting.</p>

<h2>What the pyramid runs</h2>
<p><strong>Catan:</strong> tiles numbered 6 and 8 are gold, 2 and 12 are jokes, and the robber lives on 7 because 7 comes up more than any other roll. The little dots under each number token are literally the "ways to roll it" count from the table above.</p>
<p><strong>Craps:</strong> the entire casino game is engineered around 7's dominance — it makes you win on the come-out roll and lose everafter.</p>
<p><strong>Monopoly:</strong> you're most likely to travel 7 squares per turn, which is why the orange properties (6-9 squares after the busiest square on the board, Jail) are statistically the best purchase in the game.</p>

<h2>Streaks, hot dice and other lies</h2>
<p>Rolled three sixes in a row? The chance of a fourth is still 1 in 6. Dice have no memory — each roll is independent, and "hot dice" is a story our pattern-hungry brains tell about noise. The related trap, believing a number is "due" after a drought, has its own article (and its own name: the gambler's fallacy).</p>

<h2>Quick mental math for gamers</h2>
<ul>
<li><strong>At least one six in N rolls:</strong> 1 roll → 17%, 2 → 31%, 4 → 52%, 6 → 67%. It never hits 100%, no matter how many dice you throw.</li>
<li><strong>Doubles:</strong> 6 doubles out of 36 combos = 1 in 6 per roll. Three consecutive doubles in Monopoly (straight to jail): 1 in 216.</li>
<li><strong>Beating a specific number:</strong> to roll strictly higher than a 4 on one die, you need 5 or 6 — 1 in 3.</li>
</ul>
""" + cta("See the pyramid yourself",
"Roll two dice thirty times and tally the sums — the bell shape around 7 appears astonishingly fast.",
"/dice-roller/", "Open the dice roller →") + """
<h2>The takeaway</h2>
<p>Dice odds come down to one skill: counting the ways. Sums with more recipes come up more often. Master that single idea and Catan placements, Craps tables and Monopoly's orange monopoly all snap into focus — and you'll never again pay good sheep for a settlement on a 12.</p>
""",
},
{
"slug": "birthday-paradox",
"emoji": "🎂",
"title": "The Birthday Paradox: 23 People, Even Odds | Wheel Of List Blog",
"h1": "The Birthday Paradox: 23 People, Even Odds",
"desc": "In a room of just 23 people there's a 50% chance two share a birthday. It feels wrong, it's mathematically airtight, and it even breaks cryptography.",
"body": """
<p>How many people do you need in a room before it's more likely than not that two of them share a birthday? Intuition mumbles something like 180. The correct answer is <strong>23</strong>. With 50 people the probability hits 97%; with 70 it's 99.9%. This result is so reliably offensive to human intuition that it's been a classroom staple for a century — and the reason it offends is the most instructive part.</p>

<h2>Why intuition fails</h2>
<p>When you hear the question, your brain quietly substitutes an easier one: "what's the chance someone shares <em>my</em> birthday?" That is indeed small — about 6% in a room of 23. But the paradox asks about <em>any pair</em> matching, and pairs multiply brutally: 23 people form 253 distinct pairs. Each pair is a fresh lottery ticket for a match. You're not playing 23 tickets; you're playing 253.</p>

<h2>The actual math, gently</h2>
<p>Compute the probability of <em>no</em> match and subtract from 1. Person two must dodge 1 birthday (364/365), person three must dodge 2 (363/365), and so on. Multiply the chain out to person 23 and the "everyone dodges everyone" probability falls to about 0.493 — meaning a 50.7% chance of at least one match. No trick, just multiplication grinding intuition into dust.</p>

<h2>Try it at your next event</h2>
<p>Any gathering of 25+ people is a live demonstration waiting to happen. Classrooms are perfect: a teacher with 30 students has about a 70% chance of a birthday match — ask everyone to shout their birthday month by month and watch the collision land. Wedding tables, office all-hands, five-a-side leagues: the paradox performs almost anywhere people gather in double digits.</p>
""" + cta("Run a birthday-paradox lottery",
"Draw random numbers 1-365 and see how quickly you get a repeat — it rarely takes more than 25 draws.",
"/random-number/", "Try it with the generator →") + """
<h2>Where it gets serious: breaking codes</h2>
<p>Cryptographers know the paradox as the <strong>birthday attack</strong>. A digital signature scheme is safe only if nobody can find two different documents with the same fingerprint (hash). Naively, a 64-bit fingerprint offers 2⁶⁴ possibilities — but the birthday math means collisions appear after only about 2³² random attempts, the square root. The paradox halves the effective strength of every hash function, which is why modern systems use fingerprints so long that even the square root is astronomical.</p>

<h2>The general lesson</h2>
<p>Coincidences are cheap. The birthday paradox is the flagship example of a broad truth: with enough pairs, matches are inevitable — same lottery numbers twice in a year somewhere on Earth, two strangers with the same PIN in one office, déjà vu-grade flukes of every kind. The right question about a coincidence is never "what were the odds of this?" but "how many chances did it have to happen?" The second number is always, always bigger than it feels.</p>
""",
},
{
"slug": "gamblers-fallacy",
"emoji": "🎰",
"title": "The Gambler's Fallacy: Why Streaks Lie | Wheel Of List Blog",
"h1": "The Gambler's Fallacy: Why Streaks Lie",
"desc": "In 1913, black hit 26 times in a row at Monte Carlo and gamblers lost fortunes betting red was 'due'. The bug in their heads is still in yours.",
"body": """
<p>Monte Carlo casino, August 18, 1913. The roulette ball lands on black. Then again. By the tenth black, gamblers are piling money on red — surely it's <em>due</em>. By the twentieth black, people are betting everything they have. The streak ran to <strong>26 blacks in a row</strong>, and the casino made millions, delivered by a single bug in human cognition that now bears the night's name: the Monte Carlo fallacy, better known as the gambler's fallacy.</p>

<h2>The bug, precisely</h2>
<p>The wheel has no memory. After 25 blacks, the probability of red on spin 26 is exactly what it was on spin one. The gamblers were treating independent events as if the universe kept a ledger and owed them a correction. It doesn't. Chance balances out in the infinite long run not by <em>compensating</em> for streaks but by <em>diluting</em> them under an ocean of new trials.</p>

<h2>Why your brain insists otherwise</h2>
<p>Psychologists Tversky and Kahneman traced it to the <em>representativeness heuristic</em>: we expect small samples to look like the long-run average. HTHTTH "looks random"; HHHHHH looks broken. But in six fair flips both exact sequences have identical probability — 1 in 64. Our sense of what randomness "should look like" is far tidier than actual randomness, which produces streaks constantly. In 100 coin flips, a run of six or more of the same side is more likely than not.</p>

<h2>The fallacy's evil twin</h2>
<p>The same wrong ledger produces the opposite bet: the <strong>hot-hand belief</strong> — he's made five shots, he can't miss! One fallacy says streaks must break; the other says streaks must continue. Both project structure onto independent events. (Amusing footnote: modern re-analyses found a small genuine hot-hand effect in basketball — human performance isn't a coin. The fallacy is applying streak-logic to things that <em>are</em> coins.)</p>

<h2>Where it costs real money</h2>
<ul>
<li><strong>Lottery players</strong> avoiding last week's winning numbers — identical odds next week.</li>
<li><strong>Slot players</strong> feeding a machine that's "about to pay out." It isn't. It's a PRNG with a fixed payout rate.</li>
<li><strong>Parents of three girls</strong> "certain" the fourth is a boy — still ~51/49.</li>
<li><strong>Even judges and loan officers</strong>: studies show decision-makers are measurably less likely to approve after a run of approvals — punishing applicants for their place in the queue.</li>
</ul>
""" + cta("Watch real streaks happen",
"Flip 30 times and count the streaks — our tracker shows them live. Runs of 4+ appear far more often than intuition expects.",
"/coin-flip/", "Flip and see →") + """
<h2>The inoculation</h2>
<p>One sentence, applied ruthlessly: <strong>independent events owe you nothing.</strong> Before betting on "due," ask whether the process has memory. Cards dealt from a shrinking deck do (card counting is just accounting). Coins, dice, wheels and lottery balls don't. The universe keeps no ledger — the only ledger is the one in your head, and it's cooked.</p>
""",
},
{
"slug": "monty-hall-problem",
"emoji": "🚪",
"title": "The Monty Hall Problem: Always Switch | Wheel Of List Blog",
"h1": "The Monty Hall Problem: Always Switch",
"desc": "Three doors, one car, one opened goat — and the most argued-about probability puzzle ever. Switching doubles your odds, and here's the version that finally clicks.",
"body": """
<p>You're on a game show. Three doors: one hides a car, two hide goats. You pick door 1. The host — who knows where the car is — opens door 3, revealing a goat, and asks: "want to switch to door 2?" Most people shrug: two doors left, 50/50, switching changes nothing. Most people are wrong. <strong>Switching wins two times out of three</strong>, and this little puzzle once made a thousand PhDs write angry letters.</p>

<h2>The intuition that finally works</h2>
<p>Forget the opened door for a second. Your original pick captured the car with probability 1/3 — nothing the host does can retroactively change that. Which means the car is <em>somewhere in the other two doors</em> with probability 2/3. When the host (who never reveals the car) opens one of those two doors, he isn't generating new randomness — he's <em>funneling that entire 2/3 into the one remaining closed door</em>. Switching is simply collecting it.</p>
<p>Still itchy? Scale it up: 100 doors, you pick one, the host opens 98 goat doors and leaves door 47 conspicuously shut. Your first pick was right 1% of the time. Would you seriously stay?</p>

<h2>The detail everyone misses</h2>
<p>The answer depends entirely on the host's <em>rules</em>, not just his actions. Monty knows the car's location, always opens a goat door, and always offers the switch. If instead the host opened a random door that merely <em>happened</em> to show a goat, the odds genuinely would be 50/50. Same visible events, different information content — because a constrained choice reveals more than a lucky one. This is the puzzle's deepest lesson: <strong>how</strong> information was produced matters as much as the information itself.</p>

<h2>The great pile-on of 1990</h2>
<p>When Marilyn vos Savant published the correct answer in <em>Parade</em>, she received some ten thousand letters, roughly a thousand from people with doctorates, many dripping with condescension, nearly all wrong. Even the great Paul Erdős refused to accept it until shown a computer simulation. Take comfort: if this puzzle bends your brain, you're in Hall-of-Fame company.</p>
""" + cta("Simulate it yourself",
"Put 'Car, Goat, Goat' on the wheel and play host 20 times — switching wins about 13 of them. Simulation beats argument.",
"/", "Build the three-door wheel →") + """
<h2>Why it matters off-stage</h2>
<p>Monty Hall is the cleanest known demonstration that evidence depends on process. A medical test result, a survived company in a success study, a suspiciously specific alibi — each means something different depending on the rule that produced it. Survivorship bias, publication bias and selection effects are all Monty in disguise: someone opened the goat doors before you arrived. The master question, on the game show and off: <em>what could I have been shown instead, and why wasn't I?</em></p>
""",
},
{
"slug": "how-random-number-generators-work",
"emoji": "💻",
"title": "How Computers Fake Randomness (and Why It's Fine) | Wheel Of List Blog",
"h1": "How Computers Fake Randomness (and Why It's Fine)",
"desc": "Computers are deterministic machines, yet they shuffle playlists and run lotteries. PRNGs, seeds, entropy and the difference between fake-good and fake-dangerous.",
"body": """
<p>A computer is a machine built to do exactly what it's told, identically, every time. So how does it roll a die? The honest answer: <strong>it doesn't</strong>. It computes sequences that merely <em>look</em> random — and the story of how well that works, where it breaks, and when it matters is one of computing's quiet masterpieces.</p>

<h2>The pseudo in pseudorandom</h2>
<p>A pseudorandom number generator (PRNG) is a formula that turns a current state into a next state, over and over, spitting out numbers along the way. Start from the same <strong>seed</strong> and you get the identical sequence forever — John von Neumann, who built one of the first PRNGs in the 1940s, joked that anyone using arithmetic for random digits is "in a state of sin." Yet good modern formulas produce streams that pass every statistical test humanity has devised: uniform spread, no detectable cycles, no correlations. Deterministic underneath, indistinguishable from chance on top.</p>

<h2>A famous cautionary tale</h2>
<p>Badness here is subtle. IBM's RANDU generator, shipped through the 1960s, looked fine one number at a time — but plot its outputs as 3D points and they collapse onto just 15 flat planes. Every Monte Carlo simulation that relied on it inherited invisible structure. The lesson stuck: randomness can fail in dimensions you didn't think to check, which is why modern generators (like the Mersenne Twister, or the xorshift family powering most browsers' <code>Math.random()</code>) are battle-tested against entire batteries of statistical attacks.</p>

<h2>Where seeds come from</h2>
<p>If the seed determines everything, the seed is everything. Systems harvest <em>entropy</em> — unpredictable physical noise — from timing jitter between your keystrokes, disk and network interrupt timings, and dedicated hardware circuits that amplify thermal noise in silicon. Cloudflare famously seeds part of its infrastructure by pointing a camera at a wall of lava lamps. The physical world supplies the dice; the PRNG merely stretches one roll into billions.</p>

<h2>When fake is fine — and when it's fatal</h2>
<p>For games, shuffles, raffles and simulations, a quality PRNG is not a compromise; it's mathematically fairer than physical alternatives (real coins have a measured ~51% bias toward their starting face; real dice have drilled pips and worn corners). The stakes change with an adversary. If an attacker can predict your generator, they can forge session tokens or empty a poker site — as happened in 1999 when programmers reverse-engineered PlanetPoker's shuffle from its timestamp seed and could name every card in the deck. That's why cryptographic RNGs (like your browser's <code>crypto.getRandomValues</code>) mix continuous fresh entropy into constructions designed to be unpredictable even to someone who knows the algorithm.</p>
""" + cta("Fairness you can inspect",
"Every spin and roll on this site uses the browser's built-in generator — statistically uniform, no memory, no house edge.",
"/tools/", "Explore the tools →") + """
<h2>The philosophical kicker</h2>
<p>Is anything truly random, or just unpredictable from where we stand? A coin flip obeys Newton; a PRNG obeys arithmetic; even quantum randomness is an interpretation with asterisks. For every practical purpose, <em>random enough for the use case</em> is the only standard there is — and for picking tonight's restaurant, your browser clears the bar with room to spare.</p>
""",
},
]
