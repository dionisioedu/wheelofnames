#!/usr/bin/env python3
"""Blog batch 1 — game theory cluster."""
from blog_lib import cta

ARTICLES = [
{
"slug": "prisoners-dilemma-party-games",
"emoji": "⛓️",
"title": "The Prisoner's Dilemma at Your Game Night | Wheel Of List Blog",
"h1": "The Prisoner's Dilemma at Your Game Night",
"desc": "The most famous problem in game theory isn't locked in a textbook — it's at your table every time someone decides whether to betray an alliance.",
"body": """
<p>Two suspects are arrested. The police separate them and offer each the same deal: betray your partner and walk free while they serve three years — but if you both betray each other, you both serve two. If you both stay silent, you each serve one. That's the prisoner's dilemma, the most famous thought experiment in game theory, and you don't need a police station to see it play out. You need a game night.</p>

<h2>Why betrayal is "rational"</h2>
<p>Look at the deal from one prisoner's perspective. If your partner stays silent, betraying them gets you zero years instead of one — better. If your partner betrays you, betraying them back gets you two years instead of three — also better. Betrayal wins in <em>both</em> scenarios, so a purely self-interested player always betrays. The trap: when both players follow this bulletproof logic, they both end up worse off than if they'd trusted each other. Individually rational, collectively terrible.</p>

<h2>Where you've already played this</h2>
<p><strong>Monopoly alliances.</strong> Two players agree not to build hotels on adjacent streets. Each turn, both quietly calculate whether breaking the pact first is worth it. It usually is — which is why Monopoly alliances have the shelf life of a banana.</p>
<p><strong>Risk truces.</strong> "You don't attack from Ukraine, I won't touch Alaska." Both players honor it right up until the exact moment one of them can win by not honoring it.</p>
<p><strong>Splitting the bill.</strong> Ten friends agree to split evenly. Each individually reasons that ordering the expensive steak costs them only one-tenth of its price. When everyone reasons this way, the bill explodes. Economists literally call this the "diner's dilemma."</p>

<h2>The twist: repetition changes everything</h2>
<p>Here's where it gets hopeful. In 1980, political scientist Robert Axelrod ran a tournament where computer programs played the prisoner's dilemma against each other hundreds of times. The winner wasn't a ruthless betrayer or a saintly cooperator. It was <strong>Tit for Tat</strong> — a four-line strategy: cooperate first, then copy whatever your opponent did last round.</p>
<p>Tit for Tat wins because repeated games have memory. Betray someone at game night and you gain one game — and lose the next ten, because nobody allies with you again. Your reputation is the mechanism that makes cooperation rational. This is why the dilemma feels different with strangers than with friends: with friends, you're never playing just once.</p>

<h2>Using the dilemma on purpose</h2>
<p>Want to feel the tension directly? Play "Split or Steal" at your next party: two players each secretly choose to split or steal a pot of points (or candy). Split/split shares it, steal/split takes it all, steal/steal gets nothing. Run ten rounds with rotating pairs and watch alliances, grudges and reputations form in real time. It's the entire field of game theory in a bowl of M&amp;Ms.</p>
""" + cta("Need to pair up players?",
"Random pairings keep the dilemma honest — nobody chooses their partner or their enemy.",
"/team-generator/", "Split players randomly →") + """
<h2>The takeaway</h2>
<p>The prisoner's dilemma explains why one-shot interactions tend toward selfishness and repeated ones toward cooperation. Game night is a repeated game. So is your office, your friend group and your marriage. Play accordingly — and if you must betray someone in Risk, at least accept that the next three games are going to be personal.</p>
""",
},
{
"slug": "nash-equilibrium-everyday-games",
"emoji": "⚖️",
"title": "Nash Equilibrium, Explained with Party Games | Wheel Of List Blog",
"h1": "Nash Equilibrium, Explained with Party Games",
"desc": "A Nash equilibrium is when no player gains by changing strategy alone. Sounds abstract — until you notice it deciding who does the dishes.",
"body": """
<p>John Nash won a Nobel Prize for an idea you can explain at a barbecue: a situation is in <strong>equilibrium</strong> when nobody can do better by changing their strategy <em>alone</em>. Not "everyone is happy." Not "the outcome is fair." Just: given what everyone else is doing, no single person benefits from switching. Once you learn to see Nash equilibria, you find them everywhere — especially in games and households.</p>

<h2>The intersection standoff</h2>
<p>Two cars reach a four-way stop. If both go, they crash. If both wait, nothing happens. The two equilibria: A goes while B waits, or B goes while A waits. In either one, neither driver gains by unilaterally switching — pulling out while the other is moving means a crash; waiting when the other waits means you're both stuck. Traffic rules exist to <em>pick one equilibrium for us</em> so we don't negotiate with headlights every morning.</p>

<h2>Party game equilibria</h2>
<p><strong>Hide and seek.</strong> If the seeker always checks the closet first, hiders stop using the closet. If hiders never use the closet, the seeker should stop checking it — which makes the closet safe again. There's no stable pure strategy; the equilibrium is <em>mixed</em>: everyone randomizes. Game theory proves that in games like this, the optimal strategy is literally to be unpredictable.</p>
<p><strong>Charades teams.</strong> Ever noticed teams settle into "the good actor always acts, the fast guesser always guesses"? That's an equilibrium: any one person switching roles makes their team worse. Nobody switches — even when everyone's bored. Equilibrium explains why the arrangement is <em>stable</em>, not why it's <em>fun</em>. Sometimes you need an outside force to shake things up.</p>
<p><strong>The last slice of pizza.</strong> Everyone wants it; nobody wants to be seen taking it. The equilibrium: it sits there until someone's willingness to be judged exceeds their politeness. (There is a better mechanism. It involves a wheel. We'll get to it.)</p>

<h2>Chores: the dark equilibrium</h2>
<p>Household chores often settle into a bad equilibrium: one person does most of the work because the other has learned that waiting long enough makes the problem disappear. Each is playing a best response to the other — the waiter gains nothing by starting to clean (it'll get done anyway), and the cleaner gains nothing by stopping (the house becomes a swamp). It's stable and miserable, the Nash equilibrium special.</p>
<p>Breaking a bad equilibrium requires changing the game itself: new rules, new payoffs, or an external randomizer that reassigns roles without negotiation.</p>
""" + cta("Change the game",
"A random chore assignment resets the equilibrium — nobody negotiates, nobody free-rides, physics decides.",
"/wheels/chore-wheel/", "Spin the chore wheel →") + """
<h2>Why this matters beyond games</h2>
<p>Nash's insight is that stability and quality are different things. Traffic patterns, pricing wars, standing ovations, what time parties actually start — all equilibria, none of them designed. The question worth asking about any stuck situation isn't "whose fault is this?" but "what game are we playing, and can we change its rules?" Change the payoffs and the behavior follows. That's cheaper than changing people.</p>
""",
},
{
"slug": "rock-paper-scissors-strategy",
"emoji": "✊",
"title": "How to Win Rock-Paper-Scissors (More Often) | Wheel Of List Blog",
"h1": "How to Win Rock-Paper-Scissors (More Often)",
"desc": "RPS is a fair game only if both players are random — and humans are terrible at random. The stats, the tells, and the counter-strategies.",
"body": """
<p>Rock-paper-scissors is the world's purest mixed-strategy game: three options, perfect symmetry, and a mathematical proof that the optimal strategy is to choose each throw with exactly one-third probability. Play truly randomly and nobody can beat you long-term — but nobody can lose to you either. The game only becomes winnable because of one glorious fact: <strong>humans cannot do random</strong>.</p>

<h2>The statistics of human throws</h2>
<p>Large tournament datasets and lab studies agree on the big patterns:</p>
<ul>
<li><strong>Rock is overplayed</strong> — roughly 35% of opening throws, especially by men and especially under pressure. Rock feels strong. Fists are primal.</li>
<li><strong>Winners repeat.</strong> Players who just won a round tend to throw the same thing again ("win-stay").</li>
<li><strong>Losers cycle forward.</strong> Players who just lost tend to switch to the throw that would have beaten their opponent's last throw — moving R→P→S in sequence ("lose-shift"). A study of 360 players at Zhejiang University documented exactly this pattern.</li>
<li><strong>Triples are rare.</strong> After throwing the same thing twice, most players feel an almost physical need to switch.</li>
</ul>

<h2>The exploits</h2>
<p><strong>Round one:</strong> against a typical opponent, open with paper. It beats the most common throw (rock) and rock-lovers are everywhere.</p>
<p><strong>After they win:</strong> expect a repeat. If their rock just beat your scissors, don't throw scissors again — throw paper to beat the rock that's coming.</p>
<p><strong>After they lose:</strong> expect the forward cycle. If their scissors just lost to your rock, they'll likely jump to paper (which would have beaten your rock). Throw scissors.</p>
<p><strong>Against announced throws:</strong> if someone says "here comes rock," they're probably lying — but at amateur level, surprisingly often they're not. Gladiatorial double-bluffing is a pro sport.</p>

<h2>The defense: be a robot</h2>
<p>Every exploit above works only against humans leaking patterns. The counter is to remove the human: pre-commit your throws using an external random source. A die works perfectly — 1-2 rock, 3-4 paper, 5-6 scissors. Now you're playing the Nash equilibrium and your opponent's psychology degree is useless. You won't win more than a third, but in a "loser does the dishes" negotiation, guaranteed unexploitability is exactly what you want.</p>
""" + cta("Randomize your throws",
"Generate 1-6 before each round: 1-2 rock, 3-4 paper, 5-6 scissors. Perfectly unexploitable.",
"/random-number/", "Open the number generator →") + """
<h2>Sicilian reasoning and its limits</h2>
<p>"He knows that I know that he overplays rock, so he expects paper, so he'll throw scissors, so I should throw rock…" — this recursion has no floor. Game theory's answer is elegant: when the levels of second-guessing become unbounded, the only strategy that can't be out-thought is randomness. Deep wisdom for a playground game: sometimes the smartest move is to stop being smart on purpose.</p>
""",
},
{
"slug": "fair-division-i-cut-you-choose",
"emoji": "🍰",
"title": "I Cut, You Choose: The Game Theory of Sharing Fairly | Wheel Of List Blog",
"h1": "I Cut, You Choose: The Game Theory of Sharing Fairly",
"desc": "The oldest fairness algorithm in the world needs no referee, no trust and no math degree — and it generalizes to inheritances, chores and roommates.",
"body": """
<p>Two kids, one piece of cake, guaranteed war. Except there's a 4,000-year-old protocol that solves it without a referee: <strong>one cuts, the other chooses</strong>. The cutter, knowing they'll receive the leftover piece, has every incentive to cut as evenly as humanly possible. The chooser can't complain — they picked. Nobody needs to trust anybody; the mechanism converts selfishness into fairness. Economists call this <em>envy-free division</em>, and it's the entry point to a genuinely deep field.</p>

<h2>Why it works</h2>
<p>The magic is that each player's greed protects the other. The cutter who cuts 60/40 hands the 60 to their opponent. The chooser who dawdles gains nothing. Each side's best strategy produces an outcome both consider acceptable — that's mechanism design in its purest form: don't ask people to be fair, <em>make fairness the winning move</em>.</p>

<h2>Beyond two people</h2>
<p>Three or more sharers make things dramatically harder. The Selfridge–Conway procedure guarantees envy-freeness for three people but can require trimming pieces and a second round of division. For <em>n</em> people, a general bounded envy-free protocol wasn't found until 2016 — it's so complex it's purely theoretical. There's a humbling lesson in that: fairness among two is a trick; fairness among many is one of the hardest problems mathematicians have ever formalized.</p>

<h2>Practical fair division at home</h2>
<p><strong>Divide-and-choose for chores:</strong> one roommate splits all chores into two bundles, the other picks a bundle. Works beautifully — the splitter balances "clean the bathroom" against "do all dishes for a week" with the precision of a Swiss watchmaker, because they'll be living with the leftovers.</p>
<p><strong>Sealed bids for shared stuff:</strong> when roommates split up, have everyone write secret valuations for each contested item; highest bid takes it and compensates the others in cash (the Knaster procedure). Sounds cold; prevents decade-long grudges over a couch.</p>
<p><strong>Turn-taking with a random start:</strong> for things that can't be cut — choosing bedrooms, draft picks, weekend shifts — alternate picks in A-B-B-A order to offset first-pick advantage, and let chance decide who starts.</p>
""" + cta("Who picks first?",
"Every fair division scheme needs an unbiased opening move. Let the wheel make it.",
"/", "Spin for first pick →") + """
<h2>When randomness IS the fair division</h2>
<p>Some things are indivisible and priceless — the last concert ticket, the window seat, naming the dog. For these, the fairest mechanism isn't clever cutting; it's an honest lottery. A visible, verifiable random draw gives everyone identical expected value, which is the only equality available when the good itself can't be shared. The ancient Athenians staffed their government by lottery for exactly this reason. Your household can settle the window seat the same way.</p>

<h2>The takeaway</h2>
<p>Fair division is the art of designing procedures where honesty and self-interest point the same direction. Cut-and-choose for the divisible, structured turns for the draftable, lotteries for the indivisible. The common thread: agree on the mechanism <em>before</em> you know which side of it you'll be on. That veil of ignorance is what makes everyone suddenly, sincerely interested in fairness.</p>
""",
},
{
"slug": "who-goes-first-game-theory",
"emoji": "🥇",
"title": "Who Goes First? A Surprisingly Deep Question | Wheel Of List Blog",
"h1": "Who Goes First? A Surprisingly Deep Question",
"desc": "First-move advantage is real, measured and bigger than you think — in chess, Monopoly, Catan and even rock-paper-scissors. Here's what to do about it.",
"body": """
<p>Every game night begins with a small ritual of injustice: someone gets to go first. We wave it off — "it's just a game" — but first-move advantage is real, measurable, and in some games enormous. Taking it seriously is the difference between a fair evening and a quietly rigged one.</p>

<h2>How big is the edge?</h2>
<ul>
<li><strong>Chess:</strong> White scores about 54-56% across millions of master games — a persistent edge from a single extra tempo.</li>
<li><strong>Monopoly:</strong> the first player buys from a fully stocked board. In a four-player game, simulations put player one's win rate several points above player four's.</li>
<li><strong>Connect Four:</strong> solved in 1988 — the first player wins with perfect play, full stop.</li>
<li><strong>Catan:</strong> first placement picks the best settlement spot on the whole board. The snake draft (1-2-3-4-4-3-2-1) exists precisely to soften this.</li>
<li><strong>Tic-tac-toe:</strong> first player can't lose with correct play, which is why the game dies the moment children solve it.</li>
</ul>
<p>Some games invert it: in bidding games and Uno-style shedding games, moving later means more information. Either way, turn order is rarely neutral.</p>

<h2>Bad solutions humans love</h2>
<p>"Youngest goes first" taxes the oldest sibling forever. "Whoever won last time goes last" sounds fair but creates rubber-band dynamics that punish winning. "Roll a die, highest starts" is decent but degenerates into re-roll arguments over ties. And "I'll just let you go first" is a favor — meaning it creates a debt, meaning it's not free. The common failure: every deterministic rule encodes somebody's advantage, and everybody at the table knows it.</p>

<h2>Good solutions from game design</h2>
<p><strong>Random selection, visibly performed.</strong> The gold standard. No memory, no bias, no debt. The key word is <em>visibly</em> — fairness that can't be seen doesn't reduce arguments.</p>
<p><strong>Snake drafts</strong> for anything with sequential picks: 1-2-3-4 then 4-3-2-1. First pick is offset by last pick in the next round.</p>
<p><strong>Auction the advantage:</strong> in heavier board games, players bid victory points for turn order — the edge goes to whoever values it most and they pay market price for it.</p>
<p><strong>Rotate deterministically after a random start:</strong> randomize game one, then pass the starting player left each game. One roll of fairness, then zero overhead forever.</p>
""" + cta("Settle it in five seconds",
"Names on the wheel, one spin, no arguments — and winners get removed so everyone starts once before anyone starts twice.",
"/", "Spin for turn order →") + """
<h2>The deeper point</h2>
<p>Kids argue about going first because they intuit what game theorists later proved: order is value. The mature response isn't to pretend otherwise — it's to price the advantage and distribute it fairly. Randomize the start, rotate thereafter, snake the drafts. Ninety seconds of mechanism design buys you a whole evening without the phrase "that's not fair." Cheap at twice the price.</p>
""",
},
]
