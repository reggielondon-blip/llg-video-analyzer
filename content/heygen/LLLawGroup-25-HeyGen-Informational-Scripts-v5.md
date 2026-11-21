# L & L Law Group — 25 Informational "Know Your Law" Scripts for HeyGen · v5 (Shareable / National)
### Corner Floating Head · Full-Frame Hyper-Animated B-Roll · Logo Top-Right All Video · Big Center Logo Outro
**Firm:** L and L Law Group, PLLC · Frisco, TX · landllawgroup.com
**Avatars:** Reggie London / Njeri London — assigned per script (used as trusted narrators, not salespeople)

**What v5 is (and how it's different from v3/v4):**
This series is **information-first, not marketing.** The goal is a video anyone in the country can watch, learn something real in 30 seconds, and hit **like / save / share** — not "call us." So:
- **No phone number, no CTA to reach out, no "we can help you" pitch.** Each script teaches a genuinely useful, generally-applicable legal concept.
- **National scope.** Topics are framed around U.S. constitutional rights, Supreme Court rulings, and how the system works broadly — with an explicit *"laws vary by state, this is general info"* posture baked into the wording. Where a rule differs by state, the VO says so.
- **Branding is a light touch, not the point:** the **firm logo sits pinned in the TOP-RIGHT corner for 100% of every video** (small, semi-transparent watermark), and the video **ends on a large, centered firm logo** instead of a sales card.
- **Same cinematic engine as v4** — timecoded beats, paste-ready b-roll prompts, HeyGen avatar settings, on-screen kinetic text, transition specs — but tuned toward **"realistic yet hyper-animated"** motion-graphics that pop and are inherently shareable.

---

## 🔒 LAYOUT — LOCKED SPEC (read once, apply to all 25)

**Logo — TOP-RIGHT, always on**
- The firm logo is a **persistent watermark pinned in the top-right corner for the entire runtime** (frame 1 → outro). Keep it **~14–18% of frame width**, **~70–80% opacity**, ~5% edge inset, with a soft shadow so it reads over any b-roll.
- Because the logo owns the top-right, the **floating head never uses the top-right corner.**

**Floating head — a corner, small, always on**
- Small **picture-in-picture** talking head, soft-edged **circle** with a thin **gold halo** + drop shadow, **~26–32% of frame width**, constant **3–5px parallax drift** (never frozen).
- **Allowed corners:** **top-left → bottom-left → bottom-center-low.** (Never top-right — that's the logo. Avoid the bottom-right TikTok UI zone and the bottom ~18% caption band.)
- Present **100% of the runtime.** Never scales up to fill the frame.

**B-roll — full-frame, edge-to-edge, always running, HYPER-ANIMATED-REALISTIC**
- Fills the entire **1080×1920** frame behind the head and logo, frame 1 → outro. One continuous move, **no hard cuts** — bridge with match-cuts, light-leaks, particle dissolves, rack-focus.
- **Visual style for v5:** *realistic yet hyper-animated* — think photoreal materials (glass, metal, paper, light) driven by punchy, physics-y, slightly-exaggerated motion-graphics energy. Numbers slam and settle, objects assemble from particles, light behaves cinematically. Motion never fully dies (drifting particles even on "freeze" beats).

**Captions**
- Burn word-by-word captions in the **center band** (below the head, above the bottom UI), biased toward the corner **opposite** the head so text and face never fight. Keep captions clear of the top-right logo.

**Outro — LARGE CENTER LOGO (last 2.5–3.5s)**
- End every video on the **full firm logo, centered and larger** (~55–65% frame width), resolving from the final b-roll via a clean particle-assemble or light-bloom. The small top-right watermark can crossfade into this center logo. Add the compliance footer line under it.
- **No phone number. No "call now."** Optionally a single **shareable takeaway line** above the logo (e.g., *"Save this. Share it."*).

---

## ⚙️ GLOBAL PRODUCTION SETTINGS

**Brand palette:** Deep Plum/Aubergine `#3B0A45` · Gold `#E7B24C` · Off-White `#F7F3EE` · Alert Red `#E23A3A` (emphasis only) · Cool Teal `#2BB7B3` (info/positive) · Logo Cyan `#19B5E6` (from the mark — use sparingly as an accent so graphics harmonize with the logo).
**Type:** Heavy condensed sans (Anton / Bebas-style) for hooks + big words; clean sans (Inter/Poppins) for body + citations.
**Kinetic type feel:** captions animate word-by-word with a soft scale-in + gentle overshoot, then micro-settle — text *arrives*. Big numbers ease in oversized and settle with a faint heartbeat pulse. Reserve a true "snap" for genuine emphasis.
**B-roll feel:** one continuous visual idea per video — one camera, one move. Everything on soft easing curves with gentle motion blur, fine film grain, plum shadows + gold/cyan highlights.
**Specs:** 9:16, 1080×1920, **22–40 sec**, hook in the **first 2 seconds**, burned-in captions, trending low-lyric audio.
**Default b-roll prompt suffix (append to every b-roll prompt):**
> `— 9:16 vertical 1080x1920, photoreal materials with hyper-animated motion-graphics energy, cinematic film look, slow deliberate camera move, shallow depth of field, volumetric light, fine film grain, deep plum + gold + cyan palette, gentle motion blur, no on-screen text, no watermark, no logo, no readable faces.`

**Compliance (light, national-safe):** because these are law-firm-published, keep a small persistent footer or a 2-sec end line — *"General legal information, not legal advice. Laws vary by state."* Never state a rule as absolute where it varies; use *generally / usually / in most states / may.*

---

## 🛠️ HEYGEN BUILD ORDER (per video)

1. **Avatar VO:** paste the "Full VO for HeyGen" block (keep `[pause]` / emphasis markers). Generate on green screen with a neutral dark background → mask to a soft gold-haloed **circle** at ~28% width, pin in the script's corner (never top-right), add parallax drift.
2. **B-roll:** generate each beat's **B-ROLL PROMPT** (append the default suffix) at 5–8s, or pull the **[Stock fallback]**. Stitch into one continuous move with dissolves / match-cuts / light-leaks / rack-focus. Never hard-cut, never a still.
3. **Logo watermark:** place the firm logo top-right, ~16% width, ~75% opacity, on screen the whole time.
4. **Graphics + captions:** layer the per-beat **ON-SCREEN** kinetic text; burn word-by-word captions in the center band opposite the head, clear of the logo.
5. **Outro:** resolve to the **large centered logo** (particle-assemble / light-bloom) with the shareable takeaway line + compliance footer. Add trending audio. Export 1080×1920.

---

# THE 25 SCRIPTS

---

## 1. "Cops Don't Have to Read You Your Rights" (Miranda Myth)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *myth-busting, insider, calm* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Core idea:** Miranda only applies to *custodial interrogation* — not every arrest. · **Tone:** Surprising, clarifying.

**Full VO for HeyGen:**
> "Movies lied to you. [pause] Police don't have to read you your rights the moment they arrest you. (beat) Miranda warnings are only required before they *question* you while you're in custody. So if they arrest you and never interrogate you? No Miranda needed — and the case doesn't just get thrown out. [pause] What Miranda actually protects is this: anything you say during a custodial interrogation *without* that warning may be kept out of court. Knowing the difference is the whole game."

### Shot-by-shot
- **[00:00–00:04] Hook.** VO: *"Movies lied to you."*
  - **B-ROLL:** "A cinematic TV screen glitching in a dark room, film countdown leader flickering, static resolving into a police-lights glow." **[Stock fallback]** "old tv static glitch dark cinematic"
  - **ON-SCREEN:** `THE MOVIES LIED` — Anton, slam-in, center band (head bottom-left, logo top-right).
  - **→** glitch dissolves into the scene.
- **[00:04–00:12] The myth.** VO: *"Police don't have to read you your rights the moment they arrest you."*
  - **B-ROLL:** "Hyper-animated handcuffs clicking shut in photoreal metal, then a speech-bubble icon labeled with a big red X assembling from particles above them." **[Stock fallback]** "handcuffs closing macro slow motion"
  - **ON-SCREEN:** `MIRANDA ≠ every arrest` — red X stamps over a rights-card icon.
  - **→** match-cut on the particles.
- **[00:12–00:22] The truth.** VO: *"Miranda warnings are only required before they question you while you're in custody. So if they arrest you and never interrogate you? No Miranda needed."*
  - **B-ROLL:** "A glowing equation assembling in mid-air from light particles: an interrogation-room icon PLUS a custody icon EQUALS a Miranda-card icon, hyper-clean motion-graphics." **[Stock fallback]** "glowing icons equation motion graphics dark"
  - **ON-SCREEN:** `CUSTODY + INTERROGATION = Miranda` (each term eases in, `=` pulses).
  - **→** light-leak wipe.
- **[00:22–00:30] Payoff + outro.** VO: *"What Miranda actually protects is this: anything you say during a custodial interrogation without that warning may be kept out of court. Knowing the difference is the whole game."*
  - **B-ROLL:** "Spoken words as glowing text get gently swept out of a courtroom evidence tray by a beam of light, then the frame blooms to warm gold."
  - **OUTRO:** particle-assemble to **large center logo**; line above: `Save this — it's not what the movies taught you.` Footer: *General legal information, not legal advice. Laws vary by state.*

**Caption:** Miranda isn't what you think 🎬⚖️ #knowyourrights #miranda #lawtok #legaltips #criminaljustice

---

## 2. "The One Question That Ends a Police Stop" (Am I Free to Go?)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *empowering, clear* · **Head corner:** Top-left · **Runtime:** ~29s
**Core idea:** "Am I being detained, or am I free to go?" forces the encounter into a legal category. · **Tone:** Practical, empowering.

**Full VO for HeyGen:**
> "There's one sentence that instantly changes a police encounter. [pause] *'Am I being detained, or am I free to go?'* (beat) Here's why it works: legally, an encounter is either *consensual* — meaning you can walk away — or a *detention*, which requires the officer to have a real, articulable reason. [pause] Asking that question makes them pick a lane. If you're free to go, you can calmly leave. If you're detained, now you know it's serious — and you know to stay quiet."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"There's one sentence that instantly changes a police encounter."*
  - **B-ROLL:** "First-person POV on a sidewalk at dusk, a police cruiser's light bar softly pulsing ahead, cinematic haze." **[Stock fallback]** "pov walking toward police lights dusk"
  - **ON-SCREEN:** `ONE SENTENCE` center band (head top-left, logo top-right).
  - **→** push forward.
- **[00:05–00:12] The line.** VO: *"'Am I being detained, or am I free to go?'"*
  - **B-ROLL:** "The sentence materializes as glowing gold text that splits into two diverging light-paths on the pavement ahead." **[Stock fallback]** "two glowing paths diverging ground"
  - **ON-SCREEN:** the quote types on, then forks into two labeled beams.
  - **→** camera glides between the forks.
- **[00:12–00:22] The mechanism.** VO: *"Legally, an encounter is either consensual — meaning you can walk away — or a detention, which requires the officer to have a real, articulable reason. Asking that question makes them pick a lane."*
  - **B-ROLL:** "Two photoreal doorways of light labeled by icons — a walking-figure door and a stop-hand door — hyper-animated, one warm, one cool." **[Stock fallback]** "two glowing doorways light choice"
  - **ON-SCREEN:** `CONSENSUAL → you can leave` / `DETENTION → they need a reason`.
  - **→** rack-focus.
- **[00:22–00:29] Payoff + outro.** VO: *"If you're free to go, you can calmly leave. If you're detained, now you know it's serious — and you know to stay quiet."*
  - **B-ROLL:** "The warm 'walk away' path brightens and opens into daylight."
  - **OUTRO:** light-bloom to **large center logo**; line: `Memorize this sentence.` Footer disclaimer.

**Caption:** The question that makes them pick a lane 🚶‍♀️ #knowyourrights #policestop #lawtok #legaltips #detained

---

## 3. "Police Are Legally Allowed to Lie to You" (Interrogation Tactics)
**Avatar:** Reggie · **Voice:** speed 0.97×, tone *conspiratorial, eye-opening* · **Head corner:** Bottom-left · **Runtime:** ~31s
**Core idea:** During interrogation, police can lie about evidence — and courts allow it. · **Tone:** Shocking-but-true.

**Full VO for HeyGen:**
> "This one shocks people: [pause] during an interrogation, police are *allowed to lie to you.* (beat) They can say they have your fingerprints. That a witness saw you. That your friend already confessed and blamed you. None of it has to be true. The Supreme Court has said these deceptions are generally legal. [pause] Why does it matter? Because false evidence makes innocent people confess to things they didn't do. That's not paranoia — it's one of the leading causes of wrongful convictions."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"This one shocks people: during an interrogation, police are allowed to lie to you."*
  - **B-ROLL:** "A stark interrogation room, a single hanging lamp swinging slightly, photoreal, a two-way mirror reflecting distortion." **[Stock fallback]** "interrogation room single lamp dark"
  - **ON-SCREEN:** `THEY CAN LEGALLY LIE` — red, slam-in.
  - **→** push toward the table.
- **[00:05–00:16] The lies.** VO: *"They can say they have your fingerprints. That a witness saw you. That your friend already confessed and blamed you. None of it has to be true."*
  - **B-ROLL:** "Photoreal case-file folders sliding onto the table, each stamped with an official-looking label that then dissolves into smoke revealing it was empty — hyper-animated reveal, three times." **[Stock fallback]** "case files sliding table smoke dissolve"
  - **ON-SCREEN:** `"we have your prints" · "a witness saw you" · "your friend confessed"` each fades in then cracks/greys.
  - **→** match-cut on the smoke.
- **[00:16–00:24] The authority.** VO: *"The Supreme Court has said these deceptions are generally legal."*
  - **B-ROLL:** "A marble courthouse pillar with light raking across it, a subtle gavel-echo ripple in the light." **[Stock fallback]** "marble courthouse pillar light rake"
  - **ON-SCREEN:** `generally legal` in gold; small note `U.S. courts, broadly`.
  - **→** light-leak.
- **[00:24–00:31] Payoff + outro.** VO: *"False evidence makes innocent people confess to things they didn't do. That's one of the leading causes of wrongful convictions."*
  - **B-ROLL:** "The room dissolves into drifting particles that reassemble into warm light."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Now you know the game.` Footer disclaimer.

**Caption:** Wait… that's legal?? 🤯 #interrogation #knowyourrights #wrongfulconviction #lawtok #truecrime

---

## 4. "Silence Only Works If You Say It Out Loud" (Invoking the Right)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *counterintuitive, careful* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** Staying quiet isn't enough — you must clearly invoke the right to remain silent. · **Tone:** Surprising, useful.

**Full VO for HeyGen:**
> "Here's a twist most people miss: [pause] just *being* silent doesn't fully protect you. (beat) The Supreme Court has said that to use your right to remain silent, you generally have to *invoke* it — out loud. Sitting there quietly can actually be used against you. [pause] The fix is simple. You say, clearly: *'I'm invoking my right to remain silent, and I want a lawyer.'* Then you stop talking. That one sentence flips the switch the Constitution gives you."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Here's a twist most people miss: just being silent doesn't fully protect you."*
  - **B-ROLL:** "A photoreal light switch on a dark wall, off, a faint glow behind it waiting." **[Stock fallback]** "light switch dark wall macro"
  - **ON-SCREEN:** `SILENCE ISN'T ENOUGH` center band.
  - **→** camera drifts toward the switch.
- **[00:05–00:14] The rule.** VO: *"To use your right to remain silent, you generally have to invoke it — out loud. Sitting there quietly can actually be used against you."*
  - **B-ROLL:** "A mouth-zipper icon and a 'silent = still on record' meter, hyper-animated; a recording waveform keeps scrolling even during silence." **[Stock fallback]** "audio waveform scrolling dark"
  - **ON-SCREEN:** `quiet ≠ protected` in red; a waveform keeps recording.
  - **→** rack-focus to the switch.
- **[00:14–00:24] The fix.** VO: *"You say, clearly: 'I'm invoking my right to remain silent, and I want a lawyer.' Then you stop talking."*
  - **B-ROLL:** "The words form as glowing gold text; as the last word lands, the light switch flips UP and a warm protective glow floods the wall — hyper-animated satisfying click." **[Stock fallback]** "light switch flipping on glow"
  - **ON-SCREEN:** `"I'm invoking my right to remain silent — and I want a lawyer."` types on; switch flips.
  - **→** glow expands.
- **[00:24–00:30] Payoff + outro.** VO: *"That one sentence flips the switch the Constitution gives you."*
  - **B-ROLL:** "Warm light fills the frame."
  - **OUTRO:** light-bloom to **large center logo**; line: `Say the words. Then go quiet.` Footer disclaimer.

**Caption:** Silence has a password 🔒 #knowyourrights #righttoremainsilent #lawtok #legaltips #5thamendment

---

## 5. "You Can Say No to a Search" (Consent)
**Avatar:** Reggie · **Voice:** speed 1.0×, tone *empowering, matter-of-fact* · **Head corner:** Bottom-left · **Runtime:** ~29s
**Core idea:** You can refuse consent to a search, and refusal isn't evidence of guilt. · **Tone:** Empowering.

**Full VO for HeyGen:**
> "*'Mind if I take a look?'* [pause] That's a request — which means you're allowed to say no. (beat) If police don't have a warrant or probable cause, they often ask for *consent*, because consent lets them skip both. [pause] You can calmly say: *'I don't consent to any searches.'* That's not an admission of guilt — the courts have made clear that refusing a search can't, by itself, be used to prove you did something wrong. Being polite and being firm are not opposites."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"'Mind if I take a look?' That's a request — which means you're allowed to say no."*
  - **B-ROLL:** "A flashlight beam sweeping into an open car trunk / a bag at night, photoreal, dust in the beam." **[Stock fallback]** "flashlight beam searching bag night"
  - **ON-SCREEN:** `"MIND IF I LOOK?" = a request` center band.
  - **→** beam sweeps across.
- **[00:05–00:14] Why they ask.** VO: *"If police don't have a warrant or probable cause, they often ask for consent, because consent lets them skip both."*
  - **B-ROLL:** "A hyper-animated flowchart of light: a locked padlock (warrant) and a scale (probable cause) both greyed out, an arrow routing around them through a glowing 'CONSENT' gate." **[Stock fallback]** "glowing flowchart gates motion graphics"
  - **ON-SCREEN:** `no warrant? no probable cause? → they ask YOU`.
  - **→** the consent gate pulses.
- **[00:14–00:24] The line.** VO: *"You can calmly say: 'I don't consent to any searches.' Refusing a search can't, by itself, be used to prove you did something wrong."*
  - **B-ROLL:** "The words form as a gold shield of light that closes the 'CONSENT' gate; the flashlight beam gently retreats." **[Stock fallback]** "glowing shield closing gate light"
  - **ON-SCREEN:** `"I don't consent to any searches."` types on; `refusal ≠ guilt`.
  - **→** light-leak.
- **[00:24–00:29] Payoff + outro.** VO: *"Being polite and being firm are not opposites."*
  - **B-ROLL:** "Warm calm light fills the frame."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Polite and firm. Both.` Footer disclaimer.

**Caption:** "No" is a complete sentence 🚫🔦 #knowyourrights #4thamendment #consent #lawtok #legaltips

---

## 6. "Yes, You Can Record the Police" (First Amendment)
**Avatar:** Njeri · **Voice:** speed 0.99×, tone *confident, rights-forward* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** Recording police performing their duties in public is generally protected. · **Tone:** Empowering, timely.

**Full VO for HeyGen:**
> "Can you legally record the police? [pause] In public, doing their job — generally, yes. (beat) Courts across the country have recognized that recording officers is protected by the First Amendment. It's how accountability works. [pause] A few common-sense limits: don't physically interfere, don't trespass, and follow lawful orders about *where* you stand. But you don't have to stop filming just because you're told to. Keep your distance, keep it steady, and keep it rolling."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Can you legally record the police? In public, doing their job — generally, yes."*
  - **B-ROLL:** "A photoreal phone held up, its screen framing a soft-focus street scene with police lights, a red REC dot pulsing." **[Stock fallback]** "phone recording street scene pov"
  - **ON-SCREEN:** `YOU CAN RECORD` — with a pulsing REC dot; center band.
  - **→** push into the phone screen.
- **[00:05–00:14] The right.** VO: *"Courts across the country have recognized that recording officers is protected by the First Amendment. It's how accountability works."*
  - **B-ROLL:** "The phone screen expands to fill the frame; a hyper-animated '1st' badge assembles from light, a Constitution-scroll motif shimmering behind." **[Stock fallback]** "first amendment text glowing scroll"
  - **ON-SCREEN:** `1ST AMENDMENT` badge; `protected in public`.
  - **→** match-cut on the badge glow.
- **[00:14–00:25] The limits.** VO: *"Don't physically interfere, don't trespass, and follow lawful orders about where you stand. But you don't have to stop filming just because you're told to."*
  - **B-ROLL:** "Three clean icon-chips animating in — a hands-off icon, a boundary line, a 'step back' arrow — hyper-clean, then a steady tripod-glow around the phone." **[Stock fallback]** "icons animating rules motion graphics"
  - **ON-SCREEN:** `don't interfere · don't trespass · keep distance`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"Keep your distance, keep it steady, and keep it rolling."*
  - **B-ROLL:** "The REC dot glows warm gold, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `Accountability is a right.` Footer disclaimer.

**Caption:** Keep it rolling 🎥 #firstamendment #knowyourrights #recordthepolice #lawtok #accountability

---

## 7. "Reasonable Suspicion vs. Probable Cause" (The Two Thresholds)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *teacherly, clarifying* · **Head corner:** Bottom-left · **Runtime:** ~31s
**Core idea:** Two different legal bars — one lets them stop you, the other lets them arrest/search. · **Tone:** "Finally makes sense."

**Full VO for HeyGen:**
> "Police need different levels of proof for different things — and mixing them up costs people their rights. [pause] Level one: *reasonable suspicion.* A specific, articulable hunch that something's up. It lets an officer briefly *stop* you. (beat) Level two: *probable cause.* A fair likelihood that a crime occurred. That's the bar to *arrest* you or *search* — and it's much higher. [pause] So a stop isn't an arrest, and a hunch isn't proof. When officers blur that line, that's exactly where cases get challenged."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Police need different levels of proof for different things — and mixing them up costs people their rights."*
  - **B-ROLL:** "A photoreal vertical 'proof meter' — a glowing gauge on a dark background — empty, waiting to fill." **[Stock fallback]** "vertical gauge meter glowing dark"
  - **ON-SCREEN:** `TWO THRESHOLDS` center band.
  - **→** the meter begins to fill.
- **[00:05–00:15] Level one.** VO: *"Reasonable suspicion. A specific, articulable hunch that something's up. It lets an officer briefly stop you."*
  - **B-ROLL:** "The meter fills to a lower mark glowing cyan; a 'STOP' hand-icon assembles from particles beside it." **[Stock fallback]** "meter filling low cyan glow"
  - **ON-SCREEN:** `REASONABLE SUSPICION → brief stop` (lower rung lights).
  - **→** the meter keeps climbing.
- **[00:15–00:25] Level two.** VO: *"Probable cause. A fair likelihood that a crime occurred. That's the bar to arrest you or search — and it's much higher."*
  - **B-ROLL:** "The meter climbs much higher to gold; heavier icons — handcuffs, a search-magnifier — assemble at the top rung, hyper-animated weight." **[Stock fallback]** "meter filling high gold glow"
  - **ON-SCREEN:** `PROBABLE CAUSE → arrest / search` (top rung lights, higher).
  - **→** rack-focus down the meter.
- **[00:25–00:31] Payoff + outro.** VO: *"A stop isn't an arrest, and a hunch isn't proof. When officers blur that line, that's where cases get challenged."*
  - **B-ROLL:** "The two rungs pulse side by side, then bloom to warm light."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Two bars. Know both.` Footer disclaimer.

**Caption:** Stop ≠ arrest. Hunch ≠ proof. 📊 #knowyourrights #4thamendment #lawtok #legaltips #criminaljustice

---

## 8. "Can Police Search Your Car?" (The Automobile Exception)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *clarifying, practical* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** Cars get less protection than homes, but a stop alone isn't a blank check. · **Tone:** Useful, surprising.

**Full VO for HeyGen:**
> "Your car doesn't get the same privacy as your home. [pause] There's something called the *automobile exception*: if police have probable cause to believe there's evidence of a crime inside, they can generally search it — no warrant required. (beat) *But* — being pulled over for a broken taillight isn't automatically probable cause to tear your car apart. [pause] And you're still allowed to say you don't consent. Consent and probable cause are different doors, and knowing which one they're using matters."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Your car doesn't get the same privacy as your home."*
  - **B-ROLL:** "A photoreal car and a house side by side under a night sky, a glowing 'privacy shield' bubble strong around the house, thinner around the car." **[Stock fallback]** "car and house night comparison cinematic"
  - **ON-SCREEN:** `CAR ≠ HOME (for privacy)` center band.
  - **→** push toward the car.
- **[00:05–00:15] The exception.** VO: *"The automobile exception: if police have probable cause to believe there's evidence of a crime inside, they can generally search it — no warrant required."*
  - **B-ROLL:** "A hyper-animated padlock (warrant) fades out as a glowing 'PROBABLE CAUSE' key unlocks the car's shield directly." **[Stock fallback]** "glowing key unlocking light motion graphics"
  - **ON-SCREEN:** `probable cause → search, no warrant`.
  - **→** match-cut on the unlock.
- **[00:15–00:25] The limit.** VO: *"Being pulled over for a broken taillight isn't automatically probable cause to tear your car apart. And you're still allowed to say you don't consent."*
  - **B-ROLL:** "A tiny taillight-out icon tries to unlock the whole car shield and bounces off; then a gold 'I don't consent' shield reinforces the bubble." **[Stock fallback]** "car taillight glow night macro"
  - **ON-SCREEN:** `a ticket ≠ a full search` red; `"I don't consent."`
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"Consent and probable cause are different doors, and knowing which one they're using matters."*
  - **B-ROLL:** "The car's shield glows steady, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `Know which door they're using.` Footer disclaimer.

**Caption:** A ticket isn't a search warrant 🚗🔒 #knowyourrights #4thamendment #carsearch #lawtok #legaltips

---

## 9. "The Supreme Court Protects Your Phone" (Riley v. California)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *authoritative, reassuring* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Core idea:** Police generally need a warrant to search the phone in your pocket. · **Tone:** Empowering, modern.

**Full VO for HeyGen:**
> "The phone in your pocket holds your whole life — and the Supreme Court noticed. [pause] In a case called *Riley v. California*, the Court ruled that police generally need a *warrant* to search your phone, even after an arrest. (beat) Why? Because a smartphone isn't like a wallet — it's your messages, photos, location history, everything. The justices called it a window into your entire private world. [pause] There are narrow emergencies, but the default is clear: get a warrant. Your digital life has constitutional walls."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"The phone in your pocket holds your whole life — and the Supreme Court noticed."*
  - **B-ROLL:** "A photoreal phone glowing, and streams of light (photos, messages, maps) pouring out of it like a data-galaxy, hyper-animated." **[Stock fallback]** "phone data streams glowing galaxy"
  - **ON-SCREEN:** `YOUR WHOLE LIFE` center band.
  - **→** the data-streams swirl.
- **[00:05–00:15] The ruling.** VO: *"In a case called Riley v. California, the Court ruled that police generally need a warrant to search your phone, even after an arrest."*
  - **B-ROLL:** "A translucent gold shield assembles around the phone from particles; a case-cite ribbon unrolls beneath like fabric." **[Stock fallback]** "glowing shield forming around phone"
  - **ON-SCREEN:** `RILEY v. CALIFORNIA · 2014`; `WARRANT REQUIRED` with a key-turn.
  - **→** match-cut on the ribbon.
- **[00:15–00:25] The why.** VO: *"A smartphone isn't like a wallet — it's your messages, photos, location history, everything. The justices called it a window into your entire private world."*
  - **B-ROLL:** "The phone's screen becomes a photoreal window pane, warm light behind it, gently protected by the shield." **[Stock fallback]** "window pane light warm behind glass"
  - **ON-SCREEN:** small chips `messages · photos · location · everything`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"Your digital life has constitutional walls."*
  - **B-ROLL:** "The shield glows and the frame blooms warm."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Your data has walls.` Footer disclaimer.

**Caption:** SCOTUS built a wall around your phone 📱🧱 #4thamendment #riley #knowyourrights #lawtok #privacy

---

## 10. "When Police Can Enter Your Home Without a Warrant" (Exigent Circumstances)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *serious, clarifying* · **Head corner:** Top-left · **Runtime:** ~31s
**Core idea:** Home has the strongest protection, but a few exceptions let police in without a warrant. · **Tone:** Important, precise.

**Full VO for HeyGen:**
> "Your home has the strongest privacy protection in the Constitution. [pause] Generally, police need a *warrant* to come inside. But there are exceptions — and they're worth knowing. (beat) One: you let them in — that's consent. Two: they're chasing someone in *hot pursuit.* Three: a true emergency — *exigent circumstances* — like someone screaming for help or evidence being destroyed right then. [pause] Outside those, 'we'd like to come in' is a request. And at your own front door, you're allowed to say no."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Your home has the strongest privacy protection in the Constitution."*
  - **B-ROLL:** "A photoreal front door glowing with a warm force-field aura, night, protective and solid." **[Stock fallback]** "front door glowing aura night cinematic"
  - **ON-SCREEN:** `YOUR HOME = MAX PROTECTION` center band.
  - **→** push toward the door.
- **[00:05–00:13] The rule.** VO: *"Generally, police need a warrant to come inside. But there are exceptions — and they're worth knowing."*
  - **B-ROLL:** "A glowing padlock forms on the door; then three cracks of light appear as 'exception' seams, hyper-animated." **[Stock fallback]** "padlock forming on door light"
  - **ON-SCREEN:** `WARRANT — usually`; `3 exceptions →`.
  - **→** each seam lights in turn.
- **[00:13–00:25] The three.** VO: *"One: you let them in — that's consent. Two: they're chasing someone in hot pursuit. Three: a true emergency — exigent circumstances — like someone screaming for help or evidence being destroyed right then."*
  - **B-ROLL:** "Three photoreal icon-vignettes assemble in sequence: an open hand (consent), a running figure (hot pursuit), a flame/alarm (emergency) — hyper-animated, each glowing its own accent." **[Stock fallback]** "three icons sequence motion graphics glow"
  - **ON-SCREEN:** `1 consent · 2 hot pursuit · 3 emergency`.
  - **→** rack-focus back to the door.
- **[00:25–00:31] Payoff + outro.** VO: *"Outside those, 'we'd like to come in' is a request. And at your own front door, you're allowed to say no."*
  - **B-ROLL:** "The door's aura glows steady and warm, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `Your door, your call.` Footer disclaimer.

**Caption:** 3 ways they can come in — and every other way they can't 🚪 #4thamendment #knowyourrights #lawtok #legaltips

---

## 11. "Misdemeanor vs. Felony — The Real Difference" (Charge Levels)
**Avatar:** Reggie · **Voice:** speed 0.99×, tone *clear, explainer* · **Head corner:** Bottom-left · **Runtime:** ~29s
**Core idea:** The dividing line is usually the potential punishment — and the ripple effects differ hugely. · **Tone:** Foundational.

**Full VO for HeyGen:**
> "Misdemeanor or felony — what actually separates them? [pause] The simplest rule of thumb: it's about the *maximum punishment.* Generally, if a crime can be punished by more than a year of incarceration, it's a felony. Less than that, usually a misdemeanor. (beat) But the real difference is what comes *after.* [pause] A felony can affect voting, gun rights, jobs, and housing for years. Same act, different label — and the label can echo for a lifetime."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Misdemeanor or felony — what actually separates them?"*
  - **B-ROLL:** "A photoreal balance beam with two glowing platforms, one labeled area lower, one higher, waiting." **[Stock fallback]** "balance scale two platforms glow dark"
  - **ON-SCREEN:** `MISDEMEANOR vs FELONY` center band.
  - **→** a glowing '1 YEAR' line draws across.
- **[00:05–00:14] The line.** VO: *"The simplest rule of thumb: it's about the maximum punishment. Generally, more than a year of incarceration, it's a felony. Less than that, usually a misdemeanor."*
  - **B-ROLL:** "A hyper-animated horizontal threshold line labeled '1 YEAR' glows; below it a cyan zone, above it a red zone, objects sorting into each." **[Stock fallback]** "threshold line dividing zones motion graphics"
  - **ON-SCREEN:** `> 1 year → FELONY` / `< 1 year → MISDEMEANOR`.
  - **→** camera tilts up into the red zone.
- **[00:14–00:24] The ripple.** VO: *"The real difference is what comes after. A felony can affect voting, gun rights, jobs, and housing for years."*
  - **B-ROLL:** "Four photoreal icons — a ballot, a key, a briefcase, a house — dimming one by one as a red ripple passes over them, hyper-animated." **[Stock fallback]** "icons dimming ripple effect dark"
  - **ON-SCREEN:** `voting · firearms · jobs · housing`.
  - **→** rack-focus.
- **[00:24–00:29] Payoff + outro.** VO: *"Same act, different label — and the label can echo for a lifetime."*
  - **B-ROLL:** "The icons relight warm, frame blooms."
  - **OUTRO:** particle-assemble to **large center logo**; line: `The label outlives the case.` Footer disclaimer.

**Caption:** One year is the magic line ⚖️ #knowyourrights #felony #misdemeanor #lawtok #criminaljustice

---

## 12. "What 'Beyond a Reasonable Doubt' Really Means" (The Highest Standard)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *thoughtful, illuminating* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** It's the highest burden in law — not "beyond all doubt," but close to certainty. · **Tone:** Mind-opening.

**Full VO for HeyGen:**
> "In a criminal trial, the government has to prove guilt *beyond a reasonable doubt.* [pause] But what does that actually mean? (beat) It doesn't mean beyond *all* doubt — nothing human is that certain. It means the proof has to be so strong that a reasonable person would have no real doubt about it. [pause] It's the highest standard in our entire legal system — far higher than the 'more likely than not' used in civil cases. The reason? It's built to protect the innocent. Better to make the State work than to convict someone who might be innocent."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"In a criminal trial, the government has to prove guilt beyond a reasonable doubt."*
  - **B-ROLL:** "A photoreal glass being filled with glowing liquid-light toward a very high line marked near the top, cinematic." **[Stock fallback]** "glass filling glowing liquid light"
  - **ON-SCREEN:** `BEYOND A REASONABLE DOUBT` center band.
  - **→** the fill rises.
- **[00:05–00:15] The misconception.** VO: *"It doesn't mean beyond all doubt — nothing human is that certain. It means the proof has to be so strong that a reasonable person would have no real doubt."*
  - **B-ROLL:** "The glow rises to just below the very top rim, a tiny gap left; a hyper-animated label 'not 100%, but nearly' shimmers at the gap." **[Stock fallback]** "meter near full small gap glow"
  - **ON-SCREEN:** `NOT beyond ALL doubt` / `near-certainty`.
  - **→** rack-focus up the glass.
- **[00:15–00:25] The comparison.** VO: *"It's the highest standard in our entire legal system — far higher than the 'more likely than not' used in civil cases."*
  - **B-ROLL:** "Split comparison: a civil glass filled just past halfway (51%) beside the criminal glass filled near the top, hyper-clean." **[Stock fallback]** "two meters comparison low high"
  - **ON-SCREEN:** `civil: 51%` vs `criminal: near-certain`.
  - **→** light-leak.
- **[00:25–00:30] Payoff + outro.** VO: *"It's built to protect the innocent. Better to make the State work than to convict someone who might be innocent."*
  - **B-ROLL:** "Both glasses glow warm, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `Built to protect the innocent.` Footer disclaimer.

**Caption:** The highest bar in all of law 🥃⚖️ #knowyourrights #reasonabledoubt #lawtok #jurorduty #criminaljustice

---

## 13. "Arrested, Charged, Convicted — Three Different Things" (The Stages)
**Avatar:** Reggie · **Voice:** speed 0.99×, tone *clarifying, steadying* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Core idea:** These three words mean completely different things — and mixing them up ruins reputations. · **Tone:** Foundational, fairness-minded.

**Full VO for HeyGen:**
> "Arrested. Charged. Convicted. [pause] People treat these like the same word — they're not even close. (beat) *Arrested* means police detained you on suspicion. *Charged* means a prosecutor formally accused you. *Convicted* means a judge or jury found you guilty. [pause] Only the last one means the system decided you actually did it. Everything before that is still a presumption of *innocence.* That's not a technicality — it's the entire foundation. An arrest is an accusation, not a verdict."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Arrested. Charged. Convicted. People treat these like the same word — they're not even close."*
  - **B-ROLL:** "Three photoreal glowing stepping-stones emerging across a dark reflective surface, spaced apart, waiting to light." **[Stock fallback]** "glowing stepping stones dark water"
  - **ON-SCREEN:** `3 DIFFERENT WORDS` center band.
  - **→** camera glides to the first stone.
- **[00:05–00:16] The three.** VO: *"Arrested means police detained you on suspicion. Charged means a prosecutor formally accused you. Convicted means a judge or jury found you guilty."*
  - **B-ROLL:** "Each stepping-stone lights in sequence as the camera crosses — handcuffs icon, document icon, gavel icon assembling on each, hyper-animated." **[Stock fallback]** "path icons lighting sequence motion graphics"
  - **ON-SCREEN:** `ARRESTED → CHARGED → CONVICTED` (each lights on beat).
  - **→** match-cut stone to stone.
- **[00:16–00:25] The point.** VO: *"Only the last one means the system decided you actually did it. Everything before that is still a presumption of innocence."*
  - **B-ROLL:** "The first two stones glow softer cyan; only the third, the gavel stone, glows solid gold; a 'PRESUMED INNOCENT' banner shimmers over the first two." **[Stock fallback]** "final stone glowing gold path"
  - **ON-SCREEN:** `presumed INNOCENT until the last step`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"An arrest is an accusation, not a verdict."*
  - **B-ROLL:** "All three stones glow warm, frame blooms."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Accusation ≠ verdict.` Footer disclaimer.

**Caption:** Arrested ≠ guilty. Say it louder. 👏 #knowyourrights #presumedinnocent #lawtok #criminaljustice #dueprocess

---

## 14. "Bail vs. Bond — What's the Difference?" (Getting Out)
**Avatar:** Njeri · **Voice:** speed 0.99×, tone *practical, demystifying* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** Bail is the amount set; a bond is how it's paid. And it's about return, not guilt. · **Tone:** Useful, clarifying.

**Full VO for HeyGen:**
> "Bail and bond get used like the same thing — but they're two different pieces. [pause] *Bail* is the amount a court sets to let someone out while their case is pending. (beat) A *bond* is a way to cover that amount — often through a bail bond company that posts it for a fee. [pause] And here's the part people miss: bail isn't punishment. It's meant to make sure you come back to court — not to decide guilt. Which is exactly why, when it's set too high to pay, it can be challenged."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Bail and bond get used like the same thing — but they're two different pieces."*
  - **B-ROLL:** "Two photoreal puzzle pieces of light drifting toward each other over a dark surface, not yet joined." **[Stock fallback]** "puzzle pieces glowing joining dark"
  - **ON-SCREEN:** `BAIL vs BOND` center band.
  - **→** the pieces approach.
- **[00:05–00:14] Bail.** VO: *"Bail is the amount a court sets to let someone out while their case is pending."*
  - **B-ROLL:** "A gavel taps and a glowing number materializes above a courthouse — the 'amount set' — hyper-animated slam-and-settle." **[Stock fallback]** "glowing number gavel courthouse"
  - **ON-SCREEN:** `BAIL = the amount set`.
  - **→** the number floats toward the second piece.
- **[00:14–00:23] Bond.** VO: *"A bond is a way to cover that amount — often through a bail bond company that posts it for a fee."*
  - **B-ROLL:** "The second puzzle piece becomes a photoreal receipt/handshake of light paying the number, the two pieces locking together with a satisfying click." **[Stock fallback]** "handshake payment glowing light"
  - **ON-SCREEN:** `BOND = how it's paid` (pieces lock).
  - **→** rack-focus.
- **[00:23–00:30] Payoff + outro.** VO: *"Bail isn't punishment. It's meant to make sure you come back to court — not to decide guilt. When it's set too high to pay, it can be challenged."*
  - **B-ROLL:** "The joined pieces glow warm and steady, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `Not punishment — a promise to return.` Footer disclaimer.

**Caption:** Bail = the number. Bond = how it's paid. 🧩 #knowyourrights #bail #bond #lawtok #legaltips

---

## 15. "What Actually Happens at an Arraignment" (First Court Date)
**Avatar:** Reggie · **Voice:** speed 0.99×, tone *reassuring, guide* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Core idea:** The first court appearance is mostly formal — charges read, rights explained, plea entered. · **Tone:** Demystifying, calming.

**Full VO for HeyGen:**
> "The first court date after an arrest is called an *arraignment* — and it's less dramatic than TV makes it look. [pause] Here's what usually happens. (beat) The court formally tells you the charges. You're advised of your rights, including the right to an attorney. And you enter a plea — usually 'not guilty' at this early stage, which keeps every option open. [pause] The judge may also address bail. That's mostly it. It's not the trial. It's the system officially saying: here's what you're accused of — now the process begins."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"The first court date after an arrest is called an arraignment — and it's less dramatic than TV makes it look."*
  - **B-ROLL:** "A photoreal empty courtroom softly lighting up, a single podium glowing, calm and orderly." **[Stock fallback]** "empty courtroom lighting up calm"
  - **ON-SCREEN:** `THE ARRAIGNMENT` center band.
  - **→** glide toward the podium.
- **[00:05–00:16] The steps.** VO: *"The court formally tells you the charges. You're advised of your rights, including the right to an attorney. And you enter a plea — usually 'not guilty' at this early stage."*
  - **B-ROLL:** "Three glowing checklist cards assemble in the air over the podium — a document (charges), a rights-scroll, a plea-card — hyper-animated stamp-and-settle." **[Stock fallback]** "checklist cards assembling motion graphics"
  - **ON-SCREEN:** `1 charges read · 2 rights explained · 3 plea entered`.
  - **→** each card locks on beat.
- **[00:16–00:25] Bail note.** VO: *"The judge may also address bail. That's mostly it. It's not the trial."*
  - **B-ROLL:** "A small gavel-and-number motif appears and gently settles beside the cards; the courtroom glow warms." **[Stock fallback]** "gavel number glow courtroom"
  - **ON-SCREEN:** `+ bail may be set` / `NOT the trial`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"Here's what you're accused of — now the process begins."*
  - **B-ROLL:** "The courtroom blooms to warm gold."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Step one, not the verdict.` Footer disclaimer.

**Caption:** Your first court date, explained 🏛️ #knowyourrights #arraignment #lawtok #legaltips #criminaljustice

---

## 16. "Every Crime Has a Clock" (Statute of Limitations)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *intriguing, "did you know"* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** Most crimes have a deadline for filing charges — but the most serious often don't. · **Tone:** Fascinating.

**Full VO for HeyGen:**
> "Most crimes come with a hidden countdown clock. [pause] It's called the *statute of limitations* — a deadline for the government to actually file charges. (beat) If they miss it, they generally lose the ability to prosecute, no matter what. The idea is fairness: evidence fades, memories blur, and people shouldn't live under a threat forever. [pause] But here's the twist — the most serious crimes, like murder, often have *no* time limit at all. And the clock can pause if someone flees. Time is a bigger player in the law than most people realize."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Most crimes come with a hidden countdown clock."*
  - **B-ROLL:** "A photoreal hourglass with glowing sand, or a clock face dissolving into falling particles, cinematic dark." **[Stock fallback]** "hourglass glowing sand falling dark"
  - **ON-SCREEN:** `A HIDDEN CLOCK` center band.
  - **→** sand keeps falling.
- **[00:05–00:15] The rule.** VO: *"The statute of limitations — a deadline for the government to actually file charges. If they miss it, they generally lose the ability to prosecute."*
  - **B-ROLL:** "The hourglass empties and a glowing 'CLOSED' gate materializes over a courthouse door, hyper-animated." **[Stock fallback]** "gate closing glow courthouse"
  - **ON-SCREEN:** `miss the deadline → generally no charges`.
  - **→** match-cut on the gate.
- **[00:15–00:25] The twist.** VO: *"The most serious crimes, like murder, often have no time limit at all. And the clock can pause if someone flees."*
  - **B-ROLL:** "A special hourglass with sand that never falls — frozen mid-air, glowing red — beside a running-figure icon that pauses a second clock." **[Stock fallback]** "frozen hourglass sand suspended glow"
  - **ON-SCREEN:** `murder = often NO limit` red; `fleeing can PAUSE the clock`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"Time is a bigger player in the law than most people realize."*
  - **B-ROLL:** "The hourglasses glow warm, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `Time runs the law.` Footer disclaimer.

**Caption:** Every case has a countdown ⏳ #knowyourrights #statuteoflimitations #lawtok #legaltips #didyouknow

---

## 17. "The Rule That Can Delete Evidence" (Exclusionary Rule)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *dramatic, revealing* · **Head corner:** Bottom-left · **Runtime:** ~31s
**Core idea:** Evidence obtained by violating your rights can be thrown out — even if it proves guilt. · **Tone:** Powerful.

**Full VO for HeyGen:**
> "There's a rule that can make even real evidence *disappear* from a case. [pause] It's called the *exclusionary rule.* (beat) If police get evidence by violating your constitutional rights — an illegal search, an illegal stop — a court can refuse to let the government use it. [pause] And it goes further: anything they *found because* of that violation can be tossed too. Lawyers call it 'fruit of the poisonous tree.' [pause] Why let guilty-looking evidence vanish? Because it's the main thing that makes the government follow the rules in the first place."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"There's a rule that can make even real evidence disappear from a case."*
  - **B-ROLL:** "A photoreal evidence bag on a table beginning to dissolve into glowing particles, cinematic dark." **[Stock fallback]** "evidence bag dissolving particles dark"
  - **ON-SCREEN:** `EVIDENCE CAN VANISH` center band.
  - **→** particles drift.
- **[00:05–00:15] The rule.** VO: *"The exclusionary rule. If police get evidence by violating your constitutional rights — an illegal search, an illegal stop — a court can refuse to let the government use it."*
  - **B-ROLL:** "A glowing 'ILLEGAL SEARCH' stamp hits the evidence and it greys out, then a courtroom door slams a light-barrier in front of it, hyper-animated." **[Stock fallback]** "stamp hitting object grey out motion graphics"
  - **ON-SCREEN:** `rights violated → evidence excluded`.
  - **→** match-cut on the barrier.
- **[00:15–00:25] Fruit of the tree.** VO: *"Anything they found because of that violation can be tossed too. Lawyers call it 'fruit of the poisonous tree.'"*
  - **B-ROLL:** "A hyper-animated glowing tree with tainted red roots; the fruit on its branches greys and drops one by one." **[Stock fallback]** "glowing tree roots fruit falling motion graphics"
  - **ON-SCREEN:** `FRUIT OF THE POISONOUS TREE`.
  - **→** rack-focus.
- **[00:25–00:31] Payoff + outro.** VO: *"It's the main thing that makes the government follow the rules in the first place."*
  - **B-ROLL:** "The scene blooms to warm gold."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Rules exist because of this.` Footer disclaimer.

**Caption:** The rule that deletes evidence 🌳⚖️ #knowyourrights #exclusionaryrule #4thamendment #lawtok #criminaljustice

---

## 18. "Almost No One Actually Goes to Trial" (The Plea System)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *eye-opening, sobering* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** The vast majority of criminal cases end in plea deals, not trials. · **Tone:** Surprising, systemic.

**Full VO for HeyGen:**
> "Picture a criminal case and you probably imagine a dramatic trial. [pause] Reality? The overwhelming majority of convictions — often around ninety-five percent — come from *plea deals,* not trials. (beat) A plea deal is an agreement: you plead guilty, usually to a lesser charge or a lighter sentence, and skip the trial. [pause] It keeps the system moving — but it also means most people never get their day in court. That's why understanding a plea *before* accepting it matters so much. The fast path and the fair path aren't always the same."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Picture a criminal case and you probably imagine a dramatic trial."*
  - **B-ROLL:** "A photoreal grand courtroom, cinematic — then it begins to empty out, chairs fading, hyper-animated." **[Stock fallback]** "empty courtroom dramatic light"
  - **ON-SCREEN:** `THE TRIAL YOU IMAGINE…` center band.
  - **→** the room empties.
- **[00:05–00:15] The number.** VO: *"The overwhelming majority of convictions — often around ninety-five percent — come from plea deals, not trials."*
  - **B-ROLL:** "A hyper-animated bar/pie filling to ~95% in gold, a tiny sliver left for 'trials', big number slamming in." **[Stock fallback]** "percentage chart filling 95 motion graphics"
  - **ON-SCREEN:** `~95% = PLEA DEALS` (number slams, heartbeat pulse).
  - **→** match-cut on the chart.
- **[00:15–00:25] What it is.** VO: *"A plea deal is an agreement: you plead guilty, usually to a lesser charge or a lighter sentence, and skip the trial. It keeps the system moving — but most people never get their day in court."*
  - **B-ROLL:** "Two documents merge into one glowing 'AGREEMENT' with a handshake of light, a courthouse fading behind it." **[Stock fallback]** "documents merging agreement glow"
  - **ON-SCREEN:** `plead guilty → lesser charge / lighter sentence`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"The fast path and the fair path aren't always the same."*
  - **B-ROLL:** "Warm bloom."
  - **OUTRO:** light-bloom to **large center logo**; line: `Fast isn't always fair.` Footer disclaimer.

**Caption:** 95% never see a trial 😳 #knowyourrights #pleadeal #lawtok #criminaljustice #legaltips

---

## 19. "You Have a Right to a Lawyer — Even If You Can't Pay" (Gideon)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *inspiring, foundational* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Core idea:** If you can't afford a lawyer in a criminal case, one must be provided. · **Tone:** Empowering, historic.

**Full VO for HeyGen:**
> "One of the most important rights you have costs nothing to use. [pause] If you're facing criminal charges and can't afford a lawyer, one must be provided for you. (beat) It comes from a case called *Gideon v. Wainwright* — a man who was too poor to hire an attorney, convicted, and the Supreme Court said: that's not justice. [pause] So today, that's the public defender's job. Fair warning — they're often overworked. But the *right* itself is bedrock: no one should face the power of the government alone just because of their bank account."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"One of the most important rights you have costs nothing to use."*
  - **B-ROLL:** "A photoreal empty defense chair at a courtroom table glowing with a warm halo, waiting." **[Stock fallback]** "empty chair courtroom warm light"
  - **ON-SCREEN:** `A FREE RIGHT` center band.
  - **→** push toward the chair.
- **[00:05–00:14] The right.** VO: *"If you're facing criminal charges and can't afford a lawyer, one must be provided for you."*
  - **B-ROLL:** "A glowing figure of light materializes into the empty chair beside a defendant silhouette, hyper-animated 'you're not alone' assembly." **[Stock fallback]** "figure forming light beside silhouette"
  - **ON-SCREEN:** `can't afford one? → one is provided`.
  - **→** match-cut on the light.
- **[00:14–00:24] The history.** VO: *"It comes from a case called Gideon v. Wainwright — a man too poor to hire an attorney, and the Supreme Court said: that's not justice. Today, that's the public defender's job."*
  - **B-ROLL:** "A vintage case-file and a marble Supreme Court motif, a handwritten-letter glow (Gideon famously wrote his own appeal), hyper-real texture." **[Stock fallback]** "old letter document glow historic"
  - **ON-SCREEN:** `GIDEON v. WAINWRIGHT · 1963`.
  - **→** rack-focus.
- **[00:24–00:30] Payoff + outro.** VO: *"No one should face the power of the government alone just because of their bank account."*
  - **B-ROLL:** "The chair's halo blooms warm and gold."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Justice isn't for sale.` Footer disclaimer.

**Caption:** This right costs nothing 🤝 #knowyourrights #gideon #6thamendment #lawtok #righttocounsel

---

## 20. "Double Jeopardy — And Its Sneaky Loophole" (Tried Twice?)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *intriguing, twisty* · **Head corner:** Top-left · **Runtime:** ~31s
**Core idea:** You can't be tried twice for the same offense — but "separate sovereigns" is a real exception. · **Tone:** "Wait, what?"

**Full VO for HeyGen:**
> "You've heard of *double jeopardy* — but there's a loophole that surprises everyone. [pause] The rule: the government generally can't try you twice for the *same offense* after an acquittal. Once a jury says not guilty, that door is closed. (beat) But here's the catch. The federal government and a state government are considered *separate sovereigns.* [pause] So in some cases, being acquitted in state court doesn't automatically block a *federal* prosecution for related conduct. Same act, two different governments. The protection is real — but it has an edge most people never learn."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"You've heard of double jeopardy — but there's a loophole that surprises everyone."*
  - **B-ROLL:** "A photoreal door slamming shut with a glowing 'CLOSED' seal, cinematic." **[Stock fallback]** "door slamming shut glow seal"
  - **ON-SCREEN:** `DOUBLE JEOPARDY` center band.
  - **→** the seal sets.
- **[00:05–00:15] The rule.** VO: *"The government generally can't try you twice for the same offense after an acquittal. Once a jury says not guilty, that door is closed."*
  - **B-ROLL:** "A glowing 'NOT GUILTY' verdict locks a courtroom door with a hyper-animated bolt of light." **[Stock fallback]** "lock bolting door light motion graphics"
  - **ON-SCREEN:** `acquitted → can't retry (same offense)`.
  - **→** camera pans to a second door.
- **[00:15–00:26] The loophole.** VO: *"The federal government and a state government are considered separate sovereigns. So being acquitted in state court doesn't automatically block a federal prosecution for related conduct."*
  - **B-ROLL:** "Two distinct photoreal seals/flags of light — one 'STATE', one 'FEDERAL' — and a second door beside the locked one quietly glows open, hyper-animated reveal." **[Stock fallback]** "two seals emblems glowing separate"
  - **ON-SCREEN:** `SEPARATE SOVEREIGNS` / `state ≠ federal`.
  - **→** rack-focus between the two doors.
- **[00:26–00:31] Payoff + outro.** VO: *"The protection is real — but it has an edge most people never learn."*
  - **B-ROLL:** "Both doors glow warm, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `One act. Two sovereigns.` Footer disclaimer.

**Caption:** The double jeopardy loophole 😮 #knowyourrights #doublejeopardy #lawtok #legaltips #didyouknow

---

## 21. "What Makes a Search Warrant Actually Valid" (The Fine Print)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *precise, insider* · **Head corner:** Bottom-left · **Runtime:** ~31s
**Core idea:** A valid warrant needs probable cause, a neutral judge, and specific particularity. · **Tone:** Detail-that-matters.

**Full VO for HeyGen:**
> "A search warrant isn't magic paper — it has strict requirements, and each one can be challenged. [pause] Three big ones. (beat) First: *probable cause* — real facts, not a hunch. Second: a *neutral judge* has to approve it — not the officers investigating you. Third: *particularity* — it has to describe the specific place to search and things to seize. [pause] A warrant for your garage isn't a warrant for your bedroom. When any of those pieces is missing or overbroad, the search behind it can fall apart. The details aren't technicalities — they're the whole protection."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"A search warrant isn't magic paper — it has strict requirements, and each one can be challenged."*
  - **B-ROLL:** "A photoreal official warrant document glowing on a desk, wax-seal motif, cinematic light." **[Stock fallback]** "official document wax seal glow desk"
  - **ON-SCREEN:** `WHAT MAKES A WARRANT VALID` center band.
  - **→** three glowing requirement-slots draw onto the document.
- **[00:05–00:16] The three.** VO: *"Probable cause — real facts, not a hunch. A neutral judge has to approve it — not the officers investigating you. Particularity — it has to describe the specific place and things."*
  - **B-ROLL:** "Three hyper-animated seals stamp onto the document in sequence — a scale (probable cause), a balanced-judge figure (neutral), a magnifier-on-map (particularity)." **[Stock fallback]** "three seals stamping document motion graphics"
  - **ON-SCREEN:** `1 probable cause · 2 neutral judge · 3 particularity`.
  - **→** each seal glows on beat.
- **[00:16–00:25] The example.** VO: *"A warrant for your garage isn't a warrant for your bedroom. When any of those pieces is missing or overbroad, the search behind it can fall apart."*
  - **B-ROLL:** "A photoreal house floorplan of light; a warrant beam illuminates only the garage while the bedroom stays dark and shielded, hyper-animated." **[Stock fallback]** "floorplan glowing rooms highlight light"
  - **ON-SCREEN:** `garage ≠ bedroom` in red.
  - **→** rack-focus.
- **[00:25–00:31] Payoff + outro.** VO: *"The details aren't technicalities — they're the whole protection."*
  - **B-ROLL:** "The document glows warm, frame blooms."
  - **OUTRO:** particle-assemble to **large center logo**; line: `The fine print is the point.` Footer disclaimer.

**Caption:** Warrants have fine print for a reason 📜🔍 #knowyourrights #4thamendment #searchwarrant #lawtok #legaltips

---

## 22. "Why Driving Means You Already 'Consented'" (Implied Consent)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *informative, real-talk* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** Getting a license generally means agreeing to chemical testing under certain conditions — with consequences for refusal. · **Tone:** Useful, surprising.

**Full VO for HeyGen:**
> "Here's something buried in the fine print of your driver's license: [pause] in most states, getting one means you *already agreed* to chemical testing if you're lawfully arrested for impaired driving. (beat) It's called *implied consent.* Refusing a breath or blood test can carry its own penalty — like an automatic license suspension — separate from any criminal case. [pause] The rules vary a lot by state, and courts have added nuance about warrants for blood draws. The point isn't fear — it's that a big decision at the roadside is one you technically signed up for long before."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Here's something buried in the fine print of your driver's license."*
  - **B-ROLL:** "A photoreal driver's license rotating in light, tiny glowing fine-print lines animating along its edge." **[Stock fallback]** "driver license rotating light macro"
  - **ON-SCREEN:** `THE FINE PRINT` center band.
  - **→** push into the fine print.
- **[00:05–00:15] The rule.** VO: *"In most states, getting one means you already agreed to chemical testing if you're lawfully arrested for impaired driving. It's called implied consent."*
  - **B-ROLL:** "A glowing 'I AGREE' checkbox auto-checks itself as the license is issued, hyper-animated; a breath-test device icon assembles." **[Stock fallback]** "checkbox checking glow motion graphics"
  - **ON-SCREEN:** `license = IMPLIED CONSENT` (box auto-checks).
  - **→** match-cut on the check.
- **[00:15–00:25] The consequence.** VO: *"Refusing a breath or blood test can carry its own penalty — like an automatic license suspension — separate from any criminal case. Rules vary a lot by state."*
  - **B-ROLL:** "A license icon splitting into two glowing paths — 'test' and 'refuse' — the refuse path showing a suspended-license stamp, hyper-clean." **[Stock fallback]** "two paths diverging license suspended"
  - **ON-SCREEN:** `refuse → possible auto-suspension`; small `varies by state`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"A big decision at the roadside is one you technically signed up for long before."*
  - **B-ROLL:** "The license glows warm, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `You signed up years ago.` Footer disclaimer.

**Caption:** You already agreed (and didn't know it) 🚗📄 #knowyourrights #impliedconsent #dwi #lawtok #legaltips

---

## 23. "How 12 Strangers Decide Everything" (The Jury)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *civic, fascinating* · **Head corner:** Bottom-left · **Runtime:** ~31s
**Core idea:** A criminal jury must generally reach a unanimous verdict — and one holdout can hang it. · **Tone:** Awe-of-the-system.

**Full VO for HeyGen:**
> "In a criminal trial, your fate can rest on twelve strangers who've never met you. [pause] And here's the striking part: to convict, they generally have to agree *unanimously.* Every single one. (beat) If even one juror isn't convinced beyond a reasonable doubt, they can't be forced to change their vote — and the result can be a 'hung jury.' [pause] That's not a flaw. It's designed that way. It takes the full weight of a community to take someone's freedom. Twelve people, one voice required. That's a lot of protection built into a single room."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"In a criminal trial, your fate can rest on twelve strangers who've never met you."*
  - **B-ROLL:** "Twelve photoreal empty jury chairs in a warm-lit box, glowing softly one by one, cinematic." **[Stock fallback]** "empty jury box chairs warm light"
  - **ON-SCREEN:** `12 STRANGERS` center band.
  - **→** the chairs light in sequence.
- **[00:05–00:16] Unanimity.** VO: *"To convict, they generally have to agree unanimously. Every single one."*
  - **B-ROLL:** "Twelve glowing orbs of light rising above the chairs and merging into a single unified beam, hyper-animated 'all as one'." **[Stock fallback]** "twelve orbs merging beam light"
  - **ON-SCREEN:** `UNANIMOUS to convict` (12 dots → 1).
  - **→** match-cut on the beam.
- **[00:16–00:26] The holdout.** VO: *"If even one juror isn't convinced beyond a reasonable doubt, they can't be forced to change their vote — and the result can be a 'hung jury.'"*
  - **B-ROLL:** "Eleven orbs glow gold, one stays cyan and separate; the unified beam flickers and can't complete — hyper-animated tension." **[Stock fallback]** "one different orb standing out glow"
  - **ON-SCREEN:** `1 holdout = HUNG JURY`.
  - **→** rack-focus to the single orb.
- **[00:26–00:31] Payoff + outro.** VO: *"Twelve people, one voice required. That's a lot of protection built into a single room."*
  - **B-ROLL:** "All orbs glow warm together, frame blooms."
  - **OUTRO:** particle-assemble to **large center logo**; line: `One room. Twelve voices.` Footer disclaimer.

**Caption:** One juror can change everything 👥⚖️ #knowyourrights #jury #lawtok #criminaljustice #civics

---

## 24. "You Have a Right to a Speedy Trial" (The Clock on the Government)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *empowering, foundational* · **Head corner:** Top-left · **Runtime:** ~30s
**Core idea:** The government can't leave charges hanging over you indefinitely. · **Tone:** Reassuring, rights-forward.

**Full VO for HeyGen:**
> "Once you're charged, the government doesn't get unlimited time to bring you to trial. [pause] You have a constitutional right to a *speedy trial.* (beat) The idea is fairness: no one should sit under a cloud of charges forever — losing jobs, freedom, and peace of mind — while the case just… drifts. [pause] What counts as 'too long' depends on the reasons for the delay and whether it actually harmed the defense. It's not a stopwatch with an exact number. But it's a powerful principle: the clock runs on *them,* too."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Once you're charged, the government doesn't get unlimited time to bring you to trial."*
  - **B-ROLL:** "A photoreal large clock looming over a small figure, the hands glowing — but the pressure is on the clock, not the person, cinematic." **[Stock fallback]** "large clock looming figure dramatic"
  - **ON-SCREEN:** `THE CLOCK RUNS ON THEM` center band.
  - **→** the hands begin to move.
- **[00:05–00:15] The right.** VO: *"You have a constitutional right to a speedy trial. No one should sit under a cloud of charges forever."*
  - **B-ROLL:** "A dark storm-cloud of light hovering over a figure slowly clears as a glowing '6th' badge assembles, hyper-animated relief." **[Stock fallback]** "storm cloud clearing light figure"
  - **ON-SCREEN:** `SPEEDY TRIAL · 6th Amendment`.
  - **→** match-cut on the clearing.
- **[00:15–00:25] The nuance.** VO: *"What counts as 'too long' depends on the reasons for the delay and whether it actually harmed the defense. It's not a stopwatch with an exact number."*
  - **B-ROLL:** "A hyper-animated balance weighing 'reason for delay' vs 'harm to defense', glowing factors sliding onto each pan." **[Stock fallback]** "balance scale factors weighing motion graphics"
  - **ON-SCREEN:** `reason for delay ⚖ harm to defense`.
  - **→** rack-focus.
- **[00:25–00:30] Payoff + outro.** VO: *"The clock runs on them, too."*
  - **B-ROLL:** "The clock and figure glow warm, frame blooms."
  - **OUTRO:** light-bloom to **large center logo**; line: `Justice delayed is limited.` Footer disclaimer.

**Caption:** The government has a deadline too ⏱️ #knowyourrights #speedytrial #6thamendment #lawtok #legaltips

---

## 25. "A Record Isn't Always Forever" (Expungement & Sealing)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *hopeful, second-chance* · **Head corner:** Bottom-left · **Runtime:** ~31s
**Core idea:** Many places offer legal ways to clear or seal certain records. · **Tone:** Uplifting, empowering.

**Full VO for HeyGen:**
> "A criminal record can feel like a permanent shadow — but in many cases, it doesn't have to be. [pause] Depending on where you live and what happened, there may be a legal path to *expunge* — erase — or *seal* certain records. (beat) Expungement generally wipes it like it never happened. Sealing hides it from the public while keeping it visible to law enforcement. [pause] Eligibility varies enormously by state and by charge — dismissals and certain older offenses are the most common candidates. The takeaway: a past mistake isn't automatically a life sentence. Second chances can be built into the law itself."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"A criminal record can feel like a permanent shadow — but in many cases, it doesn't have to be."*
  - **B-ROLL:** "A photoreal document casting a long dark shadow that slowly begins to recede as warm light grows, cinematic." **[Stock fallback]** "document long shadow receding light"
  - **ON-SCREEN:** `NOT ALWAYS FOREVER` center band.
  - **→** the shadow pulls back.
- **[00:05–00:16] The two paths.** VO: *"There may be a legal path to expunge — erase — or seal certain records. Expungement generally wipes it like it never happened. Sealing hides it from the public while keeping it visible to law enforcement."*
  - **B-ROLL:** "The document splits into two glowing outcomes: one erased to blank glowing paper, one lowered into a vault sealing with a warm seam — hyper-animated." **[Stock fallback]** "paper erasing" + "vault sealing glow"
  - **ON-SCREEN:** `EXPUNGE = erased` / `SEAL = hidden from public`.
  - **→** the two outcomes settle side by side.
- **[00:16–00:26] The reality.** VO: *"Eligibility varies enormously by state and by charge — dismissals and certain older offenses are the most common candidates."*
  - **B-ROLL:** "A hyper-animated map-of-light with different states glowing different colors, a 'varies by state' shimmer, warm tones." **[Stock fallback]** "us map glowing states motion graphics"
  - **ON-SCREEN:** `varies by state + charge`; chips `dismissals · older offenses`.
  - **→** rack-focus.
- **[00:26–00:31] Payoff + outro.** VO: *"A past mistake isn't automatically a life sentence. Second chances can be built into the law itself."*
  - **B-ROLL:** "The document glows clean and warm, frame blooms."
  - **OUTRO:** particle-assemble to **large center logo**; line: `Second chances exist in the law.` Footer disclaimer.

**Caption:** Your record might not be forever 🔓✨ #knowyourrights #expungement #secondchance #lawtok #legaltips

---

# 🎬 PRODUCTION CHEAT SHEET (pin this in HeyGen)

**Per-video build order (v5)**
1. **Avatar VO:** paste the "Full VO for HeyGen" block (keep `[pause]` / emphasis markers). Generate on green screen, mask to a gold-haloed **circle** at ~28% width, pin in the script's corner (**never top-right — that's the logo**), add parallax drift.
2. **B-roll:** generate each beat's **B-ROLL PROMPT** (append the default suffix) at 5–8s, or pull the **[Stock fallback]**. Stitch into one continuous, full-frame, hyper-animated-realistic move — dissolves / match-cuts / light-leaks / rack-focus. Never hard-cut, never a still.
3. **Logo watermark:** firm logo top-right, ~16% width, ~75% opacity, on screen the **entire** video.
4. **Graphics + captions:** layer the per-beat **ON-SCREEN** kinetic text; burn word-by-word captions in the center band opposite the head, clear of the top-right logo.
5. **Outro:** resolve to the **large centered logo** (particle-assemble / light-bloom), shareable takeaway line above it, compliance footer below. Add trending audio. Export 1080×1920.

**The v5 rule set:**
- **Information first.** Every video teaches something true and generally useful. No phone number, no "call us," no client-acquisition pitch.
- **National + safe.** Frame rules as *general / usually / in most states / may.* When a rule varies by state, say so on screen and in VO.
- **Logo discipline.** Small top-right watermark the whole time; large centered logo only at the very end.
- **Shareability.** The hook is the first line, oversized in second 1, opposite the head. End on a saveable takeaway line so people screenshot and share.

**Avatar rotation (informational narrators):** alternate Reggie and Njeri roughly evenly for variety; both are neutral, trustworthy explainers here rather than pitchmen.

**Series tags (use on all):** `#knowyourrights #lawtok #legaltips #criminaljustice #didyouknow`
**Posting cadence:** 3–5×/week; lead with a "shock" myth-buster (1, 3, 18, 20), close with an uplifting one (12, 19, 23, 25).

**Compliance footer (every single video):**
> *General legal information, not legal advice. Laws vary by state. L and L Law Group, PLLC — Frisco, TX.*
