# last30days Research Prompt Pack

Five copy-paste research prompts for **last30days**, the open-source (MIT) skill by Matt Van Horn that lets your AI agent search what real people posted in the last 30 days (Reddit, Hacker News, Polymarket, GitHub and more) and write one brief.
Project: https://github.com/mvanhorn/last30days-skill · Licence: MIT · The skill and its base sources are free, no keys. Some extra sources need your own keys or accounts, and some of those are paid (see "Honest notes").

## Who it is for
Creators who need video ideas, founders and marketers who need to know what people really say about a tool or a competitor, and students who want to understand a topic fast from what people are discussing right now.

## What you need
- An AI agent that supports skills: Claude Code (recommended) or another Agent Skills host.
- Per the README, Reddit, HN, Polymarket and GitHub work immediately with zero configuration.
- Optional: your own keys or accounts for more sources (X, TikTok and others). The skill's setup wizard walks you through it.

## Install (from the project's README)
In Claude Code:
```text
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```
Other Agent Skills hosts (Codex, Cursor, Gemini CLI and more):
```text
npx skills add mvanhorn/last30days-skill -g
```
Then use it like this: `/last30days <topic>`

## Prompt 1: Video ideas in my niche
**Use it when:** you need your next video topics and want them to come from real questions and complaints, not from guessing.
```text
/last30days <NICHE, e.g. "home espresso" or "AI video tools">

Using only what you found in the last 30 days:
1. List the 10 questions people ask most and the 5 things they complain about most. Say which source each one came from.
2. Rank them by how much engagement they got (upvotes, comments, points).
3. For the top 5, write 5 video title angles each (curiosity, how-to, comparison, mistake, story). Keep every title honest: it must be answerable from the threads you found.
4. Link the thread behind every idea so I can open it.
```
**What you get back:** a ranked list of real audience questions and complaints with links, plus 25 title angles you can pick from.

## Prompt 2: Product reality check before buying
**Use it when:** you are about to pay for a tool or gadget and want what real users say, not the sales page.
```text
/last30days <PRODUCT NAME> reviews and problems

I am thinking of buying <PRODUCT NAME> for <MY USE CASE>.
Using only what people said in the last 30 days, give me:
- The 5 most repeated complaints (with the thread links)
- The 5 most repeated things people praise
- 3 alternatives people actually recommend instead, and why
- Anyone who says it does NOT fit a use case like mine
Finish with "Buy / wait / skip" and the 2 facts behind that call. Mark clearly what is one person's opinion and what many people repeat.
```
**What you get back:** a balanced complaints / praise / alternatives summary with links and a clear lean.

## Prompt 3: Competitor check
**Use it when:** you want to know how users compare you (or a tool you care about) with a competitor this month.
```text
/last30days <COMPETITOR X> vs <COMPETITOR Y>

For the last 30 days, compare what users say about <COMPETITOR X> and <COMPETITOR Y>:
- A side-by-side table: what people like, what they hate, price complaints, who they say it is best for
- Any switching stories ("I moved from X to Y" or the opposite) with links
- One thing <COMPETITOR X> users ask for that nobody is delivering yet
Quote short phrases from real posts and name where each one came from.
```
**What you get back:** a side-by-side comparison, switching stories and one open gap, all with sources.

## Prompt 4: Prepare for a meeting
**Use it when:** you meet a person or company tomorrow and a Google search only gives you old pages.
```text
/last30days <PERSON OR COMPANY NAME>

I have a meeting with <PERSON OR COMPANY NAME> on <DAY> about <TOPIC>.
Using only what happened in the last 30 days, give me:
- What they are working on or shipping right now
- What people are saying about them (good and bad)
- 3 smart questions I can ask that show I did my homework
- 2 things I should NOT bring up, and why
Mark anything you are unsure about, and link the source for each point.
```
**What you get back:** a one-page briefing with current activity, public sentiment and three good questions.

## Prompt 5: Is this trend real or hype?
**Use it when:** everyone is talking about something and you want to know if it is real before you spend time or money on it.
```text
/last30days <TREND OR TECHNOLOGY>

Is <TREND OR TECHNOLOGY> real or hype? Use the last 30 days only.
- What do developers say on Hacker News and GitHub (stars, issues, real projects built with it)?
- Is there a Polymarket market about it? If yes, give the odds and how much they moved. If no, say there is none.
- What do the skeptics say, and what do the believers say? Give each side's best argument.
Finish with a verdict: "real", "early", or "hype", plus what would change your mind. Do not hide weak evidence.
```
**What you get back:** a verdict with evidence from both sides, market odds if a market exists, and links.

## Honest notes
- Base sources (Reddit, HN, Polymarket, GitHub) need no keys. X, TikTok, Instagram, Perplexity and similar sources need your own keys or accounts, and some are paid or limited per the project's README. Do not assume they are free; check each one's pricing yourself.
- Results are only as good as what people posted in the last 30 days. A quiet topic gives a thin report.
- Always open the linked threads before you quote a number or a quote in a video or a post.
- Keep your own keys private; never paste them into a prompt or share them.

## Licences
last30days: MIT, Copyright (c) 2026 Matt Van Horn. This prompt pack: free, MIT, made by Mohamed (https://heeexy.app). Not affiliated with the last30days project.
