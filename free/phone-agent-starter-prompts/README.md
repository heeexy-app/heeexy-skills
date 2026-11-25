# Phone Agent Starter Prompts

Copy-paste prompts to let **Claude Code, Codex or any coding agent** use your own phone with **phone-harness**, the open-source (MIT) CLI by Shawn Pana.
Project: https://github.com/phone-harness/phone-harness · Licence: MIT · The CLI with YOUR OWN phone is free. The hosted "Phone Harness Cloud" phones are paid (see https://phone-harness.com/pricing).

## Who it is for
Anyone with a coding agent who wants it to do small jobs on a real phone: test an app, check something in an app that has no API, automate a boring tap-tap-tap routine.

## What you need (from the project's README)
| phone | needs |
|---|---|
| iPhone | a Mac with macOS 15+, iPhone Mirroring paired to an iOS 18+ iPhone, Accessibility + Screen Recording permission |
| Android | adb + USB debugging, on macOS, Linux or Windows |
Connecting the phone is always your job; the agent walks you through it.

## Step 1: the setup prompt (the project's own prompt, MIT)
Paste this into your agent:
```text
Install or upgrade phone-harness to the latest stable version with uv using Python 3.12, register the skill from `phone-harness skill`, then read https://github.com/phone-harness/phone-harness/blob/main/onboarding.md and walk me through it. Follow https://github.com/phone-harness/phone-harness/blob/main/install.md if setup or connection fails.
```
Then run `phone-harness doctor` to check the setup.

## Step 2: the safety prompt (paste it once, before any task)
```text
You are controlling my real phone with phone-harness. Rules for this whole session:
1. Before anything that spends money, sends a message, posts, deletes, or changes a setting, STOP and ask me with the exact details (amount, recipient, text). Wait for my "yes".
2. Never open banking, wallet, password-manager or email apps unless I name the app in this chat.
3. Take a screenshot and tell me what you see before your first tap in every new app.
4. If a button has no text label, take a screenshot and describe it to me instead of guessing.
5. When the task is done, go back to the home screen and summarise every action you took.
```

## Step 3: starter tasks (safe ones to try first)
1. `Open the Weather app and tell me tomorrow's high and low for my city.`
2. `Open Settings and tell me how much storage is free. Do not change anything.`
3. `Open Notes, create a new note titled "Agent test" and type: hello from my agent.`
4. `Open the Calendar and list my events for tomorrow (titles and times only).`
5. `Open the Photos app and tell me how many photos I took today. Do not share or delete anything.`
6. `Open [app name] and find the setting for [X]. Show me the path you took, step by step.`
7. (app testers) `Open my app [name], sign up with a test account, and report every screen where a button was hard to find.`

## Known limits (from the README)
- It reads text on the screen (OCR / accessibility tree), not icons: unlabeled buttons need a screenshot and a vision-capable model.
- No multi-touch, no camera or Face ID flows; DRM video shows black.
- Unlocking the iPhone pauses mirroring; a PIN-locked Android needs you.

## Tip
Start with a spare or test phone. Treat the agent like a new assistant: small tasks first, payments always confirmed by you.

## Licences
phone-harness: MIT (c) 2026 shawn pana. This prompt pack: free, MIT.
