#!/usr/bin/env python3
"""Blog batch 5 — results-panel product news and focused SEO guides."""
from blog_lib import cta, cta_wheel


ARTICLES = [
{
"slug": "product-update-results-podium-ranking",
"category": "news",
"date": "2026-11-04",
"emoji": "🏆",
"title": "New Results Podium and Live Ranking",
"h1": "What's New: A Smarter Results Podium and Live Ranking",
"desc": "Wheel Of List now turns every spin into a clear live ranking, with trophy and medal highlights, ordered results, and a more polished animated interface.",
"faqs": [
    ("How is the Wheel Of List ranking ordered?",
     "Results stay in winning order from top to bottom. First place is always at the top, followed by second, third, and every later result."),
    ("What do the trophy and medals mean?",
     "The trophy marks first place, while silver and bronze medals identify second and third place. Later results use numbered positions for quick scanning."),
    ("Can I share the final ranking?",
     "Yes. The Share Results button creates a clean numbered list in the same top-to-bottom order shown on the results panel."),
],
"body": """
<p>The results area on <a href="/">Wheel Of List</a> has a new look and a clearer job: turn a sequence of spins into a ranking that anyone can understand at a glance. The refreshed panel is live now, with a podium-inspired design, better visual hierarchy and a result order that always runs from the highest position to the lowest.</p>

<h2>A podium you can read in one second</h2>
<p>First place now gets a trophy treatment, second place a silver medal, and third place a bronze medal. The colour, icon and position number work together, so the ranking remains easy to follow even when names are similar or the list grows during a live session.</p>
<p>From fourth place onward, each result keeps a strong numbered position without competing visually with the podium. This makes the panel useful for a single winner, a top three, or a longer finish order.</p>

<h2>Highest rank first, every time</h2>
<p>The ranking reads naturally from top to bottom: winner first, then runner-up, third place and the remaining results. New spins are added to the end of that order instead of pushing the current leader away from the top. It is a small behaviour change that makes a big difference when the wheel is displayed on a projector, shared in a meeting or used to run several rounds.</p>

<h2>A live result count</h2>
<p>The panel now shows how many results have been recorded. The same count appears on the Results tab, which makes it easy to switch between the wheel editor and the ranking without losing track of the session. An empty state explains what will happen before the first spin; after that, the list updates automatically.</p>

<h2>Cleaner result sharing</h2>
<p>The Share Results action now produces a simple numbered list that matches what is visible on screen. That is useful for pasting a final order into a group chat, classroom platform or event recap. The names are read from the visible ranking, so the shared version and the displayed version stay aligned.</p>

<h2>More depth without getting in the way</h2>
<p>The wider interface also received a visual pass. Layered gradients, subtle light and a slow background movement give the page more depth while keeping the wheel and result names as the focus. Glass-like surfaces separate the controls from the background, and the results panel uses stronger contrast for comfortable reading.</p>
<p>Motion respects the device's reduced-motion preference. When that preference is enabled, decorative animation is removed so the interface remains calm and accessible.</p>

<h2>Why we made this update</h2>
<p>A wheel spin is exciting, but the result is what people need to act on. The previous list recorded winners, yet it did not make the final order feel complete. The new podium closes that gap: it works as a lightweight scoreboard for games, presentations, workshops, classrooms, raffles and any activity with multiple picks.</p>

<h2>Try the new results panel</h2>
<p>Add a few names, spin more than once and open the Results tab. The first three positions receive podium styling automatically, and the rest of the ranking stays ordered underneath. No account or setup is required.</p>
""" + cta_wheel("See the new podium in action",
"Spin this sample list a few times, then open Results to watch the live ranking take shape.",
["Avery", "Jordan", "Morgan", "Riley", "Casey", "Taylor"], "Try the new results panel →") + """
""",
},
{
"slug": "random-name-picker-for-meetings",
"category": "guides",
"date": "2026-11-04",
"emoji": "🗣️",
"title": "Random Name Picker for Meetings and Workshops",
"h1": "How to Use a Random Name Picker in Meetings and Workshops",
"desc": "Use a random name picker to choose speakers, rotate facilitation, assign activities and make meetings more inclusive without putting people on the spot.",
"faqs": [
    ("How do I use a random name picker in a meeting?",
     "Add every participant once, explain what the draw will decide, and spin only after the group agrees to the rule. Remove each selected name when everyone should get one turn."),
    ("Is random selection fair for choosing speakers?",
     "It gives every listed participant the same chance, but fairness also requires consent and accessibility. Offer a pass option and never use a surprise draw for sensitive or high-stakes questions."),
    ("Can I use a name wheel in a remote meeting?",
     "Yes. Share your screen, keep the participant list visible before the spin, and post the final ranking or assignments in the meeting chat afterward."),
],
"body": """
<p>A random name picker can remove the awkward pause after “who wants to go first?” It can also distribute airtime, rotate small responsibilities and add energy to a workshop. The key is to use randomness as a transparent facilitation rule, not as a way to surprise or embarrass people. This guide shows how to use the <a href="/">Wheel Of List name picker</a> in in-person, hybrid and remote meetings.</p>

<h2>Good uses for a random name picker</h2>
<p>The tool works best when every outcome is acceptable and the task is low stakes. Useful examples include choosing the first speaker, rotating the daily stand-up order, assigning breakout-room reporters, selecting who reads the next prompt, choosing a retrospective activity or deciding which team presents first.</p>
<p>For anything sensitive — performance feedback, personal disclosures, conflict resolution — invite volunteers instead. Equal probability does not automatically make an activity psychologically safe.</p>

<h2>Step 1: define what the spin decides</h2>
<p>State the rule before adding names. “This spin chooses our presentation order” is clearer than “let's see who the wheel picks.” A specific rule helps participants understand the consequence, check that the list is correct and raise a concern before the result appears.</p>

<h2>Step 2: build a clean participant list</h2>
<p>Paste one name per line. Use the names people use in the meeting, remove duplicates and confirm that nobody is missing. For a large workshop, use team names instead of individuals when the activity belongs to a group. You can create a shareable wheel link in advance, but check attendance just before the session.</p>

<h2>Step 3: decide whether names can repeat</h2>
<p>For a speaking order, remove each person after selection so everyone gets exactly one turn. For repeated questions where every round should be independent, keep names on the wheel. Explain which mode you are using: repeated draws are mathematically fair over time, but a short meeting can still pick the same person twice.</p>

<h2>Step 4: give people a pass</h2>
<p>A fair meeting is not the same as a forced meeting. Let a selected participant say “pass” and spin again without needing to justify it. This keeps the playful energy while respecting accessibility needs, camera or audio problems, and moments when someone needs more preparation time.</p>

<h2>Step 5: show the draw</h2>
<p>In a room, project the wheel. In a remote call, share the browser tab and keep the full list visible before spinning. Watching the same animation creates a common reference point and makes the decision feel neutral. Avoid repeated rerolls after an inconvenient result; if a result is invalid, say why before spinning again.</p>

<h2>Meeting formats that work well</h2>
<table>
<tr><th>Meeting activity</th><th>Recommended setup</th></tr>
<tr><td>Daily stand-up order</td><td>One name each, remove after selection</td></tr>
<tr><td>Workshop presentations</td><td>Use team names, record the full ranking</td></tr>
<tr><td>Retrospective prompt</td><td>Put prompt names on the wheel instead of people</td></tr>
<tr><td>Breakout reporter</td><td>One representative per group, allow a pass</td></tr>
<tr><td>Facilitator rotation</td><td>Save the list and remove recent facilitators</td></tr>
</table>

<h2>Use the results panel as an agenda</h2>
<p>When the wheel creates an order, open the Results tab and use the ranking as the running agenda. First place appears at the top, followed by every later selection. Share the numbered result in the meeting chat so participants know when they are coming up and can prepare.</p>

<h2>Remote and hybrid meeting tips</h2>
<p>Increase browser zoom if names are small on a shared screen, mute the sound when it would interrupt conversation, and pause briefly after the result so everyone can read it. In hybrid rooms, have the facilitator control the wheel from the shared display rather than asking remote participants to open separate copies that could produce different draws.</p>

<h2>A simple facilitation script</h2>
<p>Try: “I have everyone on the wheel. We'll spin once for the presentation order, remove each team after it is picked, and anyone can ask for a pass. Does the list look right?” That twenty-second explanation establishes consent, transparency and the exact meaning of the draw.</p>
""" + cta_wheel("Start a meeting order",
"Replace these sample roles with participant names, share your screen and spin once for each position.",
["Facilitator", "Designer", "Developer", "Marketing", "Operations"], "Open a meeting wheel →") + """
""",
},
{
"slug": "how-to-create-a-quiz-wheel",
"category": "guides",
"date": "2026-11-04",
"emoji": "❓",
"title": "How to Create an Interactive Quiz Wheel",
"h1": "How to Create an Interactive Quiz Wheel",
"desc": "Build a quiz wheel for classrooms, training and game nights: choose question categories, set clear rules, avoid repeats and keep every round moving.",
"faqs": [
    ("How do I make a quiz wheel online?",
     "Add one question, topic or category per line, save the wheel, and spin to choose the next prompt. Remove a selected item if it should not appear twice."),
    ("Should a quiz wheel contain questions or categories?",
     "Use full questions for a short ready-to-play quiz. Use categories for a longer game where the host keeps several questions for each topic."),
    ("How can I make a classroom quiz wheel fair?",
     "Use equally sized entries, publish the scoring rules before the first spin, alternate teams consistently, and offer the same time limit for every question."),
],
"body": """
<p>A quiz wheel turns a list of questions into a game people can see and anticipate. Instead of moving through a worksheet in order, the wheel chooses the next topic, prompt or challenge. That small piece of randomness works well in classrooms, employee training, team socials and family game nights. You can build one in minutes with the <a href="/">Wheel Of List spinner</a>.</p>

<h2>Choose the right kind of quiz wheel</h2>
<p>There are three useful formats. A <strong>question wheel</strong> contains complete prompts, such as “What is the capital of Canada?” A <strong>category wheel</strong> contains broader topics like Geography, Science and Music, while the host keeps a separate question bank. A <strong>challenge wheel</strong> mixes tasks — answer, draw, act, explain or solve.</p>
<p>Full questions are fastest for a short review. Categories scale better because you can reuse the same wheel with new questions underneath each topic.</p>

<h2>Step 1: write balanced entries</h2>
<p>Add one entry per line. Keep labels short enough to read on a slice, and avoid putting clues in one category name that do not appear in the others. If one topic is much harder, mark its point value clearly or split the wheel into difficulty levels.</p>

<h2>Step 2: decide the game rules first</h2>
<p>Before spinning, define who answers, how long they have, how points work and whether another team can steal. A simple structure is: alternate teams, 30 seconds per question, one point for a correct answer, and one steal attempt after an incorrect answer. The wheel should choose the prompt; it should not be responsible for rules that change halfway through the game.</p>

<h2>Step 3: prevent or allow repeats</h2>
<p>Remove an entry after it is selected when every question should appear once. Keep entries when categories may repeat and you have multiple prompts per category. If repeats stay enabled, prepare at least three questions for every category so the second spin does not stall the game.</p>

<h2>Step 4: make difficulty visible</h2>
<p>For mixed-age groups or training cohorts, create separate Easy, Medium and Hard entries, or include point values in the labels. Another option is two wheels: the first chooses a category and the second chooses difficulty. Keep the scoring symmetric so both teams face the same range of possible outcomes.</p>

<h2>Step 5: host the round</h2>
<p>Show the wheel on a shared screen, read the selected entry aloud, then start the timer. Mark the score somewhere everyone can see. If a prompt is ambiguous, discard it openly and spin again; do not quietly substitute a different question after seeing which team will answer.</p>

<h2>Ready-made quiz wheel ideas</h2>
<table>
<tr><th>Audience</th><th>Wheel entries</th></tr>
<tr><td>Classroom review</td><td>Vocabulary, Key Dates, People, Concepts, Challenge</td></tr>
<tr><td>Employee training</td><td>Product, Process, Security, Customer, Scenario</td></tr>
<tr><td>Family game night</td><td>Movies, Music, Food, Places, Who Am I?</td></tr>
<tr><td>Language learning</td><td>Translate, Define, Spell, Use in a Sentence, Act It Out</td></tr>
</table>

<h2>Make the quiz accessible</h2>
<p>Read every prompt aloud as well as displaying it. Avoid relying on colour alone to communicate difficulty, allow extra response time when needed, and offer a non-timed mode. If spinning animation is distracting, participants with reduced-motion settings will receive a calmer experience automatically.</p>

<h2>Save and share the wheel</h2>
<p>Use a share link to prepare the categories before the session and open the same list on the presentation computer. The link carries the entries, which is useful for substitute teachers, co-facilitators and recurring training sessions. Keep the detailed answers in your own notes rather than in the wheel labels.</p>

<h2>After the final question</h2>
<p>Use the Results tab to review the order of selected categories, then run a final tie-breaker with one clearly labelled challenge entry or a separate <a href="/coin-flip/">coin flip</a> when the rules allow a 50/50 decision. Finish by asking which categories felt hardest; that feedback can guide the next lesson or training session.</p>
""" + cta_wheel("Try a ready-made quiz wheel",
"Use these five categories as-is or replace them with topics from your lesson, training or game night.",
["Science", "History", "Geography", "Movies", "Wildcard"], "Create a quiz wheel →") + """
""",
},
]


if __name__ == "__main__":
    print("%d articles in batch 5" % len(ARTICLES))
