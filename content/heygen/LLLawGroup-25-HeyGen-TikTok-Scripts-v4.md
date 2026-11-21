# L & L Law Group — 25 Viral TikTok Scripts for HeyGen · v4 (Production-Ready Shot Sheets)
### Small Floating Head Pinned in a Corner · Full-Frame B-Roll Running the Entire Video
**Firm:** L and L Law Group, PLLC · Frisco, TX · (972) 370-5060 (24/7) · landllawgroup.com
**Avatars:** Reggie London (former Dallas County ADA) / Njeri London (Co-Founding Partner) — assigned per script

**What changed in v4 (this version):** Every script is now a **shot-by-shot build sheet** an editor can run start-to-finish without guessing. Each one adds:
- **Timecoded beats** — the VO is chopped into 2–5 second beats with in/out times so the b-roll, captions, and lip-sync all line up.
- **Paste-ready b-roll prompts** — each beat has a text-to-video prompt (Runway / Kling / Sora / Luma / HeyGen AI B-roll) written to generate the exact shot, plus a stock-footage fallback search term.
- **HeyGen avatar settings** — voice preset, speaking speed, emotion/tone, and inline `[pause]` / emphasis markers baked into the VO so delivery lands.
- **On-screen text with timing** — the exact words, when they animate in, and where they sit relative to the head corner.
- **Transition spec between beats** — the specific bridge (match-cut, light-leak wipe, particle dissolve, rack-focus) so there is never a hard cut.
- **End-card layout** — where the phone number, CTA line, and compliance footer resolve in the last 3 seconds.

Scripts, VO wording, tone, CTAs, hashtags, and compliance language are **unchanged** from v3 — only the production detail around them is deeper. The floating-head spec and global settings from v3 are preserved verbatim below.

---

## 🔒 FLOATING HEAD — LOCKED SPEC (read once, apply to all 25)

**Placement — a corner, not the lower-third, not the center**
- The avatar head is a **picture-in-picture element pinned in ONE corner** of the frame. It floats *on top of* the b-roll — it is never the scene itself.
- **Size:** the head occupies roughly **28–34% of the frame width** (about a quarter of the screen). Big enough to read expression and lip-sync; small enough that the b-roll owns the frame.
- **Shape & lift:** soft-edged **circle** (or rounded square), a thin **gold halo ring**, and a subtle drop shadow so it separates cleanly from whatever moves behind it.
- **Motion:** constant micro-drift / parallax (~3–5px) plus natural speaking motion. The head is **never frozen**, even during a b-roll freeze-beat.
- **Safe-zone insets:** hold the head ~5–8% off the edges so the halo never clips. **Avoid the bottom-right** (TikTok's like/share/comment icons) and the **bottom ~20%** (UI + burned-in captions). Default corners in priority order: **top-left → top-right → bottom-left.** Use bottom-right only if you relocate captions.
- **Always on screen:** the head is present for **100% of the runtime** — hook, body, and end card. It never cuts away and never scales up to fill the frame.

**B-ROLL — full-frame, edge-to-edge, always running**
- B-roll fills the **entire 1080×1920 frame** behind the head, from frame 1 to the end card. The head floats over it the whole time.
- It **never stops and never shrinks to share the frame.** Intentional story "freezes" (e.g., Script 1's held moment) still keep drifting particles / light so motion never truly dies.
- Mental model: **a full-screen motion background with a small talking head in the corner** — like a streamer's cam, but cinematic.

**Captions & CTA placement**
- Burn captions in the **center band** (between the head corner and the bottom UI zone), or biased toward the corner **opposite** the head so text and face never fight.
- End card (last 3 sec): head stays in its corner; phone number + "Free consult — talk to a real attorney" resolves in the open space.

---

## ⚙️ GLOBAL PRODUCTION SETTINGS (unchanged)

**Brand palette:** Deep Plum/Aubergine `#3B0A45` · Gold `#E7B24C` · Off-White `#F7F3EE` · Alert Red `#E23A3A` (urgency only) · Cool Teal `#2BB7B3` (info/positive).
**Type:** Heavy condensed sans (Anton / Bebas-style) for hooks; clean sans (Inter/Poppins) for body.
**Kinetic type feel:** captions animate word-by-word with a soft scale-in + gentle overshoot, then a micro-settle — text *arrives*, it doesn't pop. Big numbers ease in large and settle with a faint heartbeat pulse. Transitions between graphics: cross-dissolve, draw-on (handwriting), or assemble-from-particles. Reserve a true "snap" for genuine urgency only.
**B-roll feel:** one continuous visual idea per video — one camera, one move, no hard cuts. Bridge beats with match-cuts on motion, light-leak wipes, particle dissolves, and rack-focus. Everything on soft easing curves with gentle motion blur.
**Specs:** 9:16, 1080×1920, **22–42 sec**, hook in the **first 2 seconds**, burned-in captions, trending low-lyric audio.
**Compliance (Texas Bar §7.04):** persistent small footer or 2-sec end frame — *"Attorney Advertising. General info, not legal advice. Past results don't guarantee future outcomes."* Never imply a guaranteed outcome; use *may / often / can*.

---

## 🛠️ HEYGEN BUILD SYSTEM (new in v4 — read before you build any script)

**The 6-layer stack (bottom to top), identical on every video:**
1. **B-roll base layer** — one continuous full-frame clip (or 3–5 generated clips crossfaded into one continuous move). This is Layer 0, edge-to-edge, always moving.
2. **Color/grade pass** — push toward the brand palette (plum shadows, gold highlights). Keep it filmic, slight grain, gentle motion blur.
3. **Graphics layer** — the kinetic on-screen text, case-cites, big numbers, icons listed per beat.
4. **Avatar PiP** — the HeyGen talking head, masked to a soft gold-haloed circle at ~30% width, pinned in the script's corner with 3–5px parallax drift.
5. **Captions layer** — burned-in word-by-word captions in the center band / opposite corner.
6. **End card + compliance footer** — resolves in the last 3s; footer can persist small the whole video.

**How to read each script's shot sheet:**
- **`[HH:MM]` beats** are `mm:ss` in/out. Total runtime is listed up top. Times are targets — HeyGen VO length will vary ±1–2s by voice; nudge b-roll clip lengths to match, never trim the VO.
- **`VO (say this)`** is the exact text to paste into HeyGen's avatar script box. Inline markers: `[pause]` = short breath beat; `**word**` = vocal emphasis (in HeyGen, isolate on its own line or add a comma to force the stress); `(beat)` = a ~0.4s hold.
- **`B-ROLL PROMPT`** is written to paste directly into a text-to-video generator. Always request: `9:16 vertical, 1080x1920, cinematic, slow camera move, shallow depth of field, no text, no watermark, no logos, no people talking to camera`. A **[Stock fallback]** search term is given if you'd rather pull licensed footage.
- **`ON-SCREEN`** is the kinetic text for that beat, with its animation.
- **`→ TRANSITION`** is the bridge into the next beat.

**HeyGen-specific tips baked into these sheets:**
- Generate the avatar VO **once, on green screen**, then key it out and mask to the circle — do not use HeyGen's built-in rectangular frame.
- Keep the avatar's **background prompt neutral** in HeyGen (solid green or dark plum) so the key is clean.
- Feed HeyGen the **whole script per video in one take** for consistent energy; cut b-roll to the VO afterward.
- Use HeyGen's **caption/subtitle export**, but restyle to the brand type (Anton hook, Inter body) in the editor for the kinetic feel.
- For the b-roll: generate at **5–8s per clip**, then stitch with cross-dissolves so the "one continuous move" rule holds. If a generator drifts off-brief, regenerate rather than hard-cutting.

**Default b-roll prompt suffix (append to every b-roll prompt below):**
> `— 9:16 vertical 1080x1920, cinematic film look, slow deliberate camera move, shallow depth of field, volumetric light, fine film grain, deep plum and gold color palette, gentle motion blur, no on-screen text, no watermark, no logo, no readable faces.`

---

# THE 25 SCRIPTS

---

## 1. "The 15-Day Clock Nobody Tells You About" (DWI / ALR)
**Avatar:** Reggie · **Voice:** Reggie preset, speed 0.98×, tone *urgent-protective, low and steady* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Marketing message:** DWI = a license deadline most people miss → call us in week one. · **Tone:** Urgent, ticking-clock, protective.

**Full VO for HeyGen (paste as one block):**
> "If you got a DWI in Texas, there's a clock running you don't even know about. (beat) It's not the criminal case — it's your license. You have **fifteen days** from your arrest to demand a hearing. [pause] Miss it… and on day forty-one your license is suspended automatically. No trial. No judge. Just gone. Most people find out on day sixteen. [pause] Call us *before* the clock beats you."

### Shot-by-shot
- **[00:00–00:03] Hook.** VO: *"If you got a DWI in Texas, there's a clock running you don't even know about."*
  - **B-ROLL PROMPT:** "Slow push-in through a dim room toward a large wall clock, second hand sweeping in extreme slow motion, dust motes drifting in a single shaft of light." **[Stock fallback]** "slow motion clock second hand dark cinematic"
  - **ON-SCREEN:** `A CLOCK IS ALREADY RUNNING` — Anton, scale-in word-by-word, top-center (opposite the bottom-left head).
  - **→ TRANSITION:** continuous push, no cut.
- **[00:03–00:09] Turn.** VO: *"It's not the criminal case — it's your license. You have fifteen days from your arrest to demand a hearing."*
  - **B-ROLL PROMPT:** "Calendar leaves peeling off one by one and drifting down like falling ash, revealing behind them a driver's license slowly being pulled toward the metal teeth of a paper shredder." **[Stock fallback]** "calendar pages falling slow motion" + "paper shredder close up"
  - **ON-SCREEN:** `15 DAYS` eases in oversized, gold, settles with a faint heartbeat pulse; small subhead `to demand a hearing`.
  - **→ TRANSITION:** match-cut on the drifting leaves into the shredder pull.
- **[00:09–00:16] The freeze.** VO: *"Miss it… and on day forty-one your license is suspended automatically. No trial. No judge. Just gone."*
  - **B-ROLL PROMPT:** "The license hangs by a thread at the shredder's mouth, the whole scene freezing mid-pull while particles and light continue to drift; the license slowly desaturates from color to grey." **[Stock fallback]** "id card shredder macro slow motion"
  - **ON-SCREEN:** `DAY 41 — SUSPENDED` *bleeds up* in Alert Red as the license greys out.
  - **→ TRANSITION:** hold on the frozen license, particles keep moving.
- **[00:16–00:23] Twist.** VO: *"Most people find out on day sixteen."*
  - **B-ROLL PROMPT:** "The frozen license drops fully into the shredder in slow motion as a single calendar leaf reading a blurred '16' drifts past the lens." **[Stock fallback]** "shredder destroying card slow motion"
  - **ON-SCREEN:** `most find out on DAY 16` — Inter, red, small draw-on underline.
  - **→ TRANSITION:** light-leak wipe to the end card.
- **[00:23–00:30] CTA end card.** VO: *"Call us before the clock beats you."*
  - **B-ROLL PROMPT:** "The dim room lifts into warm gold light, the clock softening out of focus, open dark space opening on the right." 
  - **ON-SCREEN / END CARD:** `Day of arrest? Call now` + **(972) 370-5060 · 24/7** resolves in the open space; head stays bottom-left. Compliance footer visible.

**CTA overlay:** "Day of arrest? Call now → (972) 370-5060 · 24/7"
**Caption:** The DWI deadline nobody warns you about ⏳ #dwi #texaslaw #dwilawyer #dallas #frisco #knowyourrights

---

## 2. "Do You Know Why I Pulled You Over?" (The One Question)
**Avatar:** Reggie · **Voice:** speed 0.97×, tone *insider, low, conspiratorial — almost a whisper on the hook* · **Head corner:** Top-right · **Runtime:** ~29s
**Marketing message:** Don't talk yourself into a charge — we defend what you *didn't* have to say. · **Tone:** Insider, conspiratorial.

**Full VO for HeyGen:**
> "When an officer leans in and asks, *'Do you know why I pulled you over?'* — that is not small talk. [pause] It's the first question on a test you didn't sign up for. Whatever you say next can become the evidence. (beat) You're allowed to be polite *and* say: *'Officer, I'd rather not answer questions.'* [pause] That's not guilt. That's the Fifth Amendment doing its job."

### Shot-by-shot
- **[00:00–00:04] Hook.** VO: *"When an officer leans in and asks, 'Do you know why I pulled you over?' — that is not small talk."*
  - **B-ROLL PROMPT:** "First-person POV slowly gliding toward a rolled-down car window at night, red and blue police light washing across the dashboard in a steady rhythmic tide." **[Stock fallback]** "police lights on dashboard night pov"
  - **ON-SCREEN:** `"Do you know why I pulled you over?"` — appears as kinetic caption that brightens on each light pass, center band under the top-right head.
  - **→ TRANSITION:** continuous glide, light keeps washing.
- **[00:04–00:12] Warning.** VO: *"It's the first question on a test you didn't sign up for. Whatever you say next can become the evidence."*
  - **B-ROLL PROMPT:** "A translucent speech bubble drifts up from the window and fills with floating glowing words that gather and link together." **[Stock fallback]** "abstract glowing particles forming shapes dark"
  - **ON-SCREEN:** `ADMISSION` warms slowly from white to red, letters locking like a latch.
  - **→ TRANSITION:** the words curl and morph on motion.
- **[00:12–00:20] The image.** VO: *"You're allowed to be polite and say: 'Officer, I'd rather not answer questions.'"*
  - **B-ROLL PROMPT:** "In soft focus, floating words slowly curl and reshape into the silhouette of a handcuff that eases shut, hypnotic slow drift." **[Stock fallback]** "handcuffs closing slow motion silhouette"
  - **ON-SCREEN:** `"I'd rather not answer questions."` types on calmly in Off-White, quote-style.
  - **→ TRANSITION:** rack-focus from the handcuff to open space.
- **[00:20–00:29] Close + CTA.** VO: *"That's not guilt. That's the Fifth Amendment doing its job."*
  - **B-ROLL PROMPT:** "The red and blue light softens to a calm warm glow, dashboard easing out of focus, dark open space opening lower-left."
  - **ON-SCREEN / END CARD:** `DON'T ANSWER` fades up as a calm watermark, then `Said too much? It's not over.` + **(972) 370-5060**. Head top-right; footer visible.

**CTA overlay:** "Said too much? It's not over. → (972) 370-5060"
**Caption:** The question that's actually a trap 👀 #policestop #knowyourrights #criminaldefense #texas #fifthamendment

---

## 3. "Your Warrant Is Not Going to Expire" (Outstanding Warrants)
**Avatar:** Njeri · **Voice:** speed 0.96×, tone *calm authority, unhurried, reassuring* · **Head corner:** Top-left · **Runtime:** ~31s
**Marketing message:** Warrants sit forever — resolve it on *your* terms before an arrest happens. · **Tone:** Calm authority.

**Full VO for HeyGen:**
> "Here's the myth that gets people arrested: *'If I just wait, the warrant will go away.'* [pause] It won't. A Texas warrant stays active **indefinitely.** No expiration. (beat) It's a trip wire on every traffic stop, every airport, every background check. [pause] The good news? You can resolve it *before* the cuffs — verify it, pre-arrange the bond, walk in on your schedule. That's the whole difference."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Here's the myth that gets people arrested: 'If I just wait, the warrant will go away.'"*
  - **B-ROLL PROMPT:** "A closed manila file resting on a wooden desk, time-lapse light cycling day-to-night sliding across its surface, dust settling in the beams." **[Stock fallback]** "time lapse light across desk day to night"
  - **ON-SCREEN:** `"It'll just go away." — a myth` center band; `myth` in red.
  - **→ TRANSITION:** continuous time-lapse.
- **[00:05–00:12] The truth.** VO: *"It won't. A Texas warrant stays active indefinitely. No expiration."*
  - **B-ROLL PROMPT:** "Faint ghostly numerals '2023 → 2026' dissolving in the corner of the frame as years pass over the unchanging file, camera drifting slowly upward off the desk." **[Stock fallback]** "abstract years passing numbers dissolve"
  - **ON-SCREEN:** `WARRANTS DON'T EXPIRE` draws itself on in gold, slow, like a signature.
  - **→ TRANSITION:** camera drifts up and out of the file into the next scene seamlessly.
- **[00:12–00:20] The trip wire.** VO: *"It's a trip wire on every traffic stop, every airport, every background check."*
  - **B-ROLL PROMPT:** "Seamless drift from the file into a nighttime traffic stop, then an airport security lane, the same glowing red file icon present in each scene." **[Stock fallback]** "airport security lane" + "traffic stop at night"
  - **ON-SCREEN:** `any traffic stop · any airport · any background check` types on in soft typewriter rhythm, gently scrolls.
  - **→ TRANSITION:** light-leak wipe between locations, file icon carries through.
- **[00:20–00:31] Resolution + CTA.** VO: *"The good news? You can resolve it before the cuffs — verify it, pre-arrange the bond, walk in on your schedule. That's the whole difference."*
  - **B-ROLL PROMPT:** "The red file icon turns calm gold as a figure walks into a courthouse in warm daylight, unhurried, open space to the right."
  - **ON-SCREEN / END CARD:** `verify · pre-arrange bond · walk in on your terms` then `Think you have a warrant?` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Think you have a warrant? → (972) 370-5060"
**Caption:** Waiting it out is the worst move 🚨 #warrant #texas #criminaldefense #dallaslawyer #legaltips

---

## 4. "Cuffed at Work… or Walk In on Your Terms?" (Walk-Through Surrender)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *reassuring, dignity-protecting, steady* · **Head corner:** Top-center, small · **Runtime:** ~27s
**Marketing message:** A controlled, attorney-coordinated surrender beats getting grabbed in public. · **Tone:** Reassuring, dignity-protecting.

**Full VO for HeyGen:**
> "Two ways this goes. [pause] Option one: they show up at your job, in front of everyone, no warning. (beat) Option two: your attorney confirms the warrant, arranges the bond *first*, and you walk in, get processed, and walk back out — same day. [pause] Same charge. Completely different day. We coordinate option two."

### Shot-by-shot
- **[00:00–00:04] Hook.** VO: *"Two ways this goes."*
  - **B-ROLL PROMPT:** "A vertical split-screen wipe opening from the center of a dark frame, the dividing line softly breathing with light." **[Stock fallback]** "split screen light divider vertical abstract"
  - **ON-SCREEN:** `TWO WAYS THIS GOES` — Anton, center, held high so it clears the top-center head; captions nudged low-center.
  - **→ TRANSITION:** split opens.
- **[00:04–00:12] Option one.** VO: *"Option one: they show up at your job, in front of everyone, no warning."*
  - **B-ROLL PROMPT (left panel):** "Desaturated, slightly slow-motion office scene: a person handcuffed at a desk as coworkers turn to look, cold blue-grey grade." **[Stock fallback]** "arrest at office desk dramatic"
  - **ON-SCREEN:** left label `CUFFED AT WORK` glides up from the lower edge, cold grey.
  - **→ TRANSITION:** the divider breathes toward the right panel.
- **[00:12–00:21] Option two.** VO: *"Option two: your attorney confirms the warrant, arranges the bond first, and you walk in, get processed, and walk back out — same day."*
  - **B-ROLL PROMPT (right panel):** "Warm gold-graded scene: the same person walking calmly into a building with paperwork handled, then back out into daylight, confident and unhurried." **[Stock fallback]** "person walking into courthouse confident daylight"
  - **ON-SCREEN:** right label `WALK IN ON YOUR TERMS`; green checkmarks stitch in one by one down the right side like a seam being sewn.
  - **→ TRANSITION:** left panel drains of color, right panel blooms brighter — the screen takes a side.
- **[00:21–00:27] Close + CTA.** VO: *"Same charge. Completely different day. We coordinate option two."*
  - **B-ROLL PROMPT:** "The right, warm panel expands to fill the whole frame, open daylight, calm."
  - **ON-SCREEN / END CARD:** `Surrender the smart way` + **(972) 370-5060**. Head top-center; footer visible.

**CTA overlay:** "Surrender the smart way → (972) 370-5060"
**Caption:** Don't let them pick the time and place 🤝 #warrant #criminaldefense #frisco #dallas #knowyourrights

---

## 5. "Field Sobriety Tests Are Voluntary" (DWI Roadside)
**Avatar:** Reggie · **Voice:** speed 1.0×, tone *myth-busting, empowering, a little punchy* · **Head corner:** Bottom-left · **Runtime:** ~28s
**Marketing message:** You have more rights at the roadside than you think — we challenge bad stops. · **Tone:** Myth-busting, empowering.

**Full VO for HeyGen:**
> "The roadside balance tests? Walking the line, following the pen, standing on one leg? [pause] In Texas, those are **voluntary.** You can decline. (beat) And even when people do them, these tests have to follow the NHTSA manual *exactly* — the instructions, the scoring, the medical questions. [pause] When officers cut corners, we pull their training records and put the whole 'evidence' on trial."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"The roadside balance tests? Walking the line, following the pen, standing on one leg?"*
  - **B-ROLL PROMPT:** "Three minimalist white line-art icons — walk-the-line, follow-the-pen, one-leg-stand — each drawing itself then dissolving fluidly into the next like a single pen never lifting, dark plum background." **[Stock fallback]** "animated line icons draw on dark background"
  - **ON-SCREEN:** the three icon names label each as it draws, upper/center; head clears bottom-left.
  - **→ TRANSITION:** each icon dissolves into the next.
- **[00:06–00:13] The reveal.** VO: *"In Texas, those are voluntary. You can decline."*
  - **B-ROLL PROMPT:** "Behind the icons, a clipboard labeled with a blurred agency manual flips its pages in soft focus, shallow depth of field breathing in and out." **[Stock fallback]** "clipboard pages flipping macro shallow focus"
  - **ON-SCREEN:** `VOLUNTARY` eases onto each icon with a gentle stamp-and-settle, gold.
  - **→ TRANSITION:** rack-focus from icons to clipboard.
- **[00:13–00:22] The mechanism.** VO: *"And even when people do them, these tests have to follow the NHTSA manual exactly — the instructions, the scoring, the medical questions."*
  - **B-ROLL PROMPT:** "Close-up of a manual's pages, precise printed lines and a scoring grid coming into sharp focus, a fine pointer tracing down a checklist." **[Stock fallback]** "checklist scoring sheet macro pointer"
  - **ON-SCREEN:** proof-points `HGN · 18-clue scoring` float up like subtitles, hold, drift off.
  - **→ TRANSITION:** light-leak wipe.
- **[00:22–00:28] Close + CTA.** VO: *"When officers cut corners, we pull their training records and put the whole 'evidence' on trial."*
  - **B-ROLL PROMPT:** "The manual closes and warm gold light spreads across the frame, open dark space right."
  - **ON-SCREEN / END CARD:** `You can say no.` then `Charged after a roadside test?` + **(972) 370-5060**. Head bottom-left; footer visible.

**CTA overlay:** "Charged after a roadside test? → (972) 370-5060"
**Caption:** You can say no to these 🚫 #dwi #fieldsobriety #knowyourrights #texas #dwilawyer

---

## 6. "Can Police Search Your Phone?" (Riley v. California)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *sharp, authoritative, precise* · **Head corner:** Top-left · **Runtime:** ~29s
**Marketing message:** We know the Fourth Amendment cold — illegal searches get suppressed. · **Tone:** Sharp, authoritative.

**Full VO for HeyGen:**
> "They arrested you — can they go through your phone? [pause] As a general rule: **no.** (beat) The Supreme Court said it in *Riley v. California* — searching your phone without a warrant violates the Fourth Amendment. [pause] There are narrow exceptions, but the default is they need a warrant, with probable cause, and specifics. If they searched anyway, that evidence may not survive a motion to suppress."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"They arrested you — can they go through your phone?"*
  - **B-ROLL PROMPT:** "A smartphone resting face-up in a single pool of light on a dark surface, lock-screen glowing, a hand slowly entering frame from the right reaching toward it." **[Stock fallback]** "smartphone in spotlight dark hand reaching"
  - **ON-SCREEN:** `CAN THEY SEARCH YOUR PHONE?` center band, clear of top-left head.
  - **→ TRANSITION:** continuous slow reach.
- **[00:05–00:12] The answer.** VO: *"As a general rule: no."*
  - **B-ROLL PROMPT:** "A translucent glowing shield assembles from drifting light particles between the hand and the phone, the hand slowing to a gentle stop just short of the glass." **[Stock fallback]** "glowing shield particles form protective barrier"
  - **ON-SCREEN:** `NO — as a general rule` big, gold, heartbeat settle.
  - **→ TRANSITION:** particles settle into a banner.
- **[00:12–00:20] The authority.** VO: *"The Supreme Court said it in Riley v. California — searching your phone without a warrant violates the Fourth Amendment."*
  - **B-ROLL PROMPT:** "Beneath the phone a case-citation ribbon unrolls smoothly like fabric settling, warm gold on dark." **[Stock fallback]** "unrolling ribbon banner gold cinematic"
  - **ON-SCREEN:** `RILEY v. CALIFORNIA · 2014` unfurls like a banner catching air.
  - **→ TRANSITION:** rack-focus to the ribbon's final word.
- **[00:20–00:29] Close + CTA.** VO: *"There are narrow exceptions, but the default is they need a warrant, with probable cause, and specifics. If they searched anyway, that evidence may not survive a motion to suppress."*
  - **B-ROLL PROMPT:** "The shield glows brighter with a soft key-turn motion, warm light expanding, open space lower-right."
  - **ON-SCREEN / END CARD:** `WARRANT REQUIRED` resolves in gold with a key-turn on the final word, then `Phone searched after arrest?` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Phone searched after arrest? → (972) 370-5060"
**Caption:** The Supreme Court already ruled on this 📱⚖️ #4thamendment #knowyourrights #criminaldefense #riley #texas

---

## 7. "A DWI Is Two Cases, Not One" (Parallel Tracks)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *clarifying, teacherly, confident* · **Head corner:** Top-left · **Runtime:** ~30s
**Marketing message:** Most people only fight one track and lose the other — we run both. · **Tone:** Clarifying.

**Full VO for HeyGen:**
> "One arrest. *Two* completely separate battles. [pause] Track one is the criminal case — that's guilt or innocence. (beat) Track two is your license, run by DPS, on its own fifteen-day clock. [pause] People pour everything into the courtroom and let the license suspension happen by default. We fight **both** tracks from day one — because keeping you driving matters just as much."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"One arrest. Two completely separate battles."*
  - **B-ROLL PROMPT:** "Overhead view gliding forward alongside a single glowing rail line on a dark surface, cinematic, slow dolly." **[Stock fallback]** "glowing rail line top down abstract move"
  - **ON-SCREEN:** `ONE ARREST · TWO CASES` center band, head clears top-left.
  - **→ TRANSITION:** the rail begins to split.
- **[00:05–00:14] The split.** VO: *"Track one is the criminal case — that's guilt or innocence. Track two is your license, run by DPS, on its own fifteen-day clock."*
  - **B-ROLL PROMPT:** "The single glowing rail smoothly splits into a Y, two rails pulling apart on an easing curve; one rail carries a small courthouse icon, the other a license icon, each with a softly ticking clock; the license rail tinted faint warning red." **[Stock fallback]** "railroad track splitting Y aerial"
  - **ON-SCREEN:** lane labels `CRIMINAL` and `ALR` slide in along their rails; `15 DAYS` hovers over the ALR lane with a slow pulse.
  - **→ TRANSITION:** camera keeps gliding between the diverging rails.
- **[00:14–00:23] The mistake.** VO: *"People pour everything into the courtroom and let the license suspension happen by default."*
  - **B-ROLL PROMPT:** "Camera drifts down the courthouse rail, brightly lit and busy, while the license rail dims and its red clock keeps ticking, neglected." **[Stock fallback]** "two diverging paths one dim one lit"
  - **ON-SCREEN:** the ALR lane visibly dims; `by default = you lose track 2` small red.
  - **→ TRANSITION:** camera pulls back to show both rails again.
- **[00:23–00:30] Close + CTA.** VO: *"We fight both tracks from day one — because keeping you driving matters just as much."*
  - **B-ROLL PROMPT:** "Both rails glow equally bright gold and run parallel forward into warm light, open space right."
  - **ON-SCREEN / END CARD:** `WE FIGHT BOTH` then `Two cases. One call.` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Two cases. One call. → (972) 370-5060"
**Caption:** Nobody tells you it's TWO cases 🚆 #dwi #alr #texas #dwilawyer #knowyourrights

---

## 8. "I Used to Be the Prosecutor" (Founder Story / Trust)
**Avatar:** Reggie · **Voice:** speed 0.96×, tone *personal, confident, first-person and warm — this is his story* · **Head corner:** Top-right · **Runtime:** ~30s
**Marketing message:** A former Dallas County ADA now reads the State's playbook *for you*. · **Tone:** Personal, confident.

**Full VO for HeyGen:**
> "I used to be on the other side of this. [pause] A Dallas County prosecutor — building the cases the State now wants to use on *you.* (beat) So when I read your file, I'm not guessing what they'll do next. I've *done* it. [pause] That two-sided view is the edge: I know where their case is weak, where the deadlines are, and which moves actually change the outcome."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"I used to be on the other side of this."*
  - **B-ROLL PROMPT:** "Slow lateral dolly across an empty, grand courtroom, low light raking over the wooden benches, dust in the beams, reverent and quiet." **[Stock fallback]** "empty courtroom slow dolly cinematic light"
  - **ON-SCREEN:** `I WAS ON THE OTHER SIDE` center band, head clears top-right.
  - **→ TRANSITION:** dolly continues toward a nameplate.
- **[00:05–00:13] The transform.** VO: *"A Dallas County prosecutor — building the cases the State now wants to use on you."*
  - **B-ROLL PROMPT:** "Close-up of an engraved desk nameplate reading 'PROSECUTION' catching raking light; in a seamless match-dissolve the engraved letters reshape into 'DEFENSE' on the same plate." **[Stock fallback]** "engraved nameplate close up light"
  - **ON-SCREEN:** `FORMER DALLAS COUNTY ADA` resolves in gold with a confident fade-up.
  - **→ TRANSITION:** cut on motion (the light sweep) into the chessboard.
- **[00:13–00:22] The edge.** VO: *"So when I read your file, I'm not guessing what they'll do next. I've done it."*
  - **B-ROLL PROMPT:** "A dark wooden chessboard, a single piece gliding forward, camera racking focus onto it as it lands with a soft click, cinematic shallow depth." **[Stock fallback]** "chess piece move macro shallow focus dark"
  - **ON-SCREEN:** `I know their next 3 moves` writes on like handwriting, the `3` briefly swelling before it settles.
  - **→ TRANSITION:** rack-focus pulls to open space.
- **[00:22–00:30] Close + CTA.** VO: *"That two-sided view is the edge: I know where their case is weak, where the deadlines are, and which moves actually change the outcome."*
  - **B-ROLL PROMPT:** "The chessboard softens into warm gold light, open space lower-left."
  - **ON-SCREEN / END CARD:** `Get the prosecutor's playbook on your side` + **(972) 370-5060**. Head top-right; footer visible.

**CTA overlay:** "Get the prosecutor's playbook on your side → (972) 370-5060"
**Caption:** I prosecuted these cases. Now I defend them. ♟️ #criminaldefense #formerprosecutor #dallas #frisco #lawyer

---

## 9. "Expunction vs. Non-Disclosure" (Clean Slate Explainer)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *hopeful, second-chance, warm* · **Head corner:** Top-center, small · **Runtime:** ~32s
**Marketing message:** There may be a legal path to erase or seal your record — let's check. · **Tone:** Hopeful, second-chance.

**Full VO for HeyGen:**
> "Two ways to clean up a Texas record — and they're not the same. [pause] **Expunction** wipes the arrest from the public databases like it never happened — usually for dismissals, acquittals, certain deferred outcomes. (beat) **Non-disclosure** *seals* it from the public but keeps it visible to law enforcement. [pause] Expunction is the bigger win; non-disclosure is the fallback. Which one you qualify for depends on your facts — and that's a five-minute conversation."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"Two ways to clean up a Texas record — and they're not the same."*
  - **B-ROLL PROMPT:** "Slow lateral glide across a desk in cold grey light, a printed criminal record sheet lying under a single lamp." **[Stock fallback]** "document on desk lamp light slow pan"
  - **ON-SCREEN:** `ERASED vs. SEALED` center band low, head held high center.
  - **→ TRANSITION:** camera settles over the left of the sheet.
- **[00:05–00:14] Expunction.** VO: *"Expunction wipes the arrest from the public databases like it never happened — usually for dismissals, acquittals, certain deferred outcomes."*
  - **B-ROLL PROMPT:** "A record sheet being erased line by line from left to right until the paper is clean and softly glowing white, magical eraser sweep." **[Stock fallback]** "text erasing off paper animation"
  - **ON-SCREEN:** card `EXPUNCTION = ERASED · CCP Ch. 55` rises with a soft eraser-sweep.
  - **→ TRANSITION:** camera slides right along the desk.
- **[00:14–00:24] Non-disclosure.** VO: *"Non-disclosure seals it from the public but keeps it visible to law enforcement."*
  - **B-ROLL PROMPT:** "The same sheet lowering into a heavy vault whose door eases shut, a seam of light sealing along the edge, background warming from cold grey to gold." **[Stock fallback]** "vault door closing seal light"
  - **ON-SCREEN:** card `NON-DISCLOSURE = SEALED · Gov't Code Ch. 411` rises with a gentle lock-turn.
  - **→ TRANSITION:** the two cards settle side by side mid-move.
- **[00:24–00:32] Close + CTA.** VO: *"Expunction is the bigger win; non-disclosure is the fallback. Which one you qualify for depends on your facts — and that's a five-minute conversation."*
  - **B-ROLL PROMPT:** "Both cards glow warm gold side by side, background fully warm, open space right."
  - **ON-SCREEN / END CARD:** `Check your record eligibility` + **(972) 370-5060**. Head top-center; footer visible.

**CTA overlay:** "Check your record eligibility → (972) 370-5060"
**Caption:** Erased vs. sealed — know the difference 🔓 #expunction #cleanslate #texas #secondchance #criminaldefense

---

## 10. "Weaving in Your Own Lane Isn't a Crime" (Bad Stops)
**Avatar:** Reggie · **Voice:** speed 1.0×, tone *provocative, challenging, a little edge* · **Head corner:** Bottom-left · **Runtime:** ~29s
**Marketing message:** A weak stop can sink the whole case — we attack the *reason* they pulled you over. · **Tone:** Provocative.

**Full VO for HeyGen:**
> "An officer says you were 'weaving' and lights you up. [pause] But here's the thing — drifting *within* your own lane is not, by itself, a legal reason to stop you in Texas. (beat) The courts said so. A hunch isn't enough. [pause] If the stop was bad, everything after it — the tests, the breath sample, the arrest — can come *out.* We start the defense at the very first second: *why did they stop you at all?*"

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"An officer says you were 'weaving' and lights you up."*
  - **B-ROLL PROMPT:** "Clean top-down animated view of a single car easing gently side to side within its lane lines on a dark highway, never touching the lines, road scrolling smoothly beneath, red-blue light appearing behind it." **[Stock fallback]** "top down car driving highway night aerial"
  - **ON-SCREEN:** `"WEAVING"?` in quotes, center band, head clears bottom-left.
  - **→ TRANSITION:** continuous scroll.
- **[00:06–00:14] The claim vs. reality.** VO: *"But here's the thing — drifting within your own lane is not, by itself, a legal reason to stop you in Texas."*
  - **B-ROLL PROMPT:** "A magnifying glass glides across the frame; inside the lens the dashcam-style image sharpens into focus, isolating the car staying within its lines." **[Stock fallback]** "magnifying glass over screen focus reveal"
  - **ON-SCREEN:** `within your lane ≠ a crime` fades up.
  - **→ TRANSITION:** rack-focus through the lens.
- **[00:14–00:22] The authority.** VO: *"The courts said so. A hunch isn't enough."*
  - **B-ROLL PROMPT:** "A case-citation ribbon slides up from the bottom to anchor beneath the magnified car, gold on dark." **[Stock fallback]** "legal document ribbon slide gold"
  - **ON-SCREEN:** `STATE v. CORTEZ · 2018` banners in; `a hunch ≠ a legal stop` fades up in red and draws its own underline left-to-right.
  - **→ TRANSITION:** light-leak wipe.
- **[00:22–00:29] Close + CTA.** VO: *"If the stop was bad, everything after it — the tests, the breath sample, the arrest — can come out. We start the defense at the very first second: why did they stop you at all?"*
  - **B-ROLL PROMPT:** "The dashcam image dissolves into warm gold light, open space right."
  - **ON-SCREEN / END CARD:** `Was your stop even legal?` + **(972) 370-5060**. Head bottom-left; footer visible.

**CTA overlay:** "Was your stop even legal? → (972) 370-5060"
**Caption:** "Weaving" isn't always a crime 🚗 #dwi #knowyourrights #texaslaw #criminaldefense #motiontosuppress

---

## 11. "Your First DWI — Here's What Actually Happens" (First-Offense Roadmap)
**Avatar:** Njeri · **Voice:** speed 0.97×, tone *steady, hand-on-shoulder, calming* · **Head corner:** Top-right · **Runtime:** ~31s
**Marketing message:** We demystify the process so fear doesn't make your decisions. · **Tone:** Steady, hand-on-shoulder.

**Full VO for HeyGen:**
> "First DWI? Your brain is screaming worst-case. [pause] Here's the *real* sequence. (beat) You're booked and released on bond. You have fifteen days to protect your license. The criminal charge usually gets filed thirty to sixty days later. Then comes your first court setting. [pause] None of it is the end of your life — but the early moves matter most. The earlier we start, the more options you keep."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"First DWI? Your brain is screaming worst-case."*
  - **B-ROLL PROMPT:** "A single glowing horizontal timeline stretching left to right on a dark plum background, the camera beginning a smooth horizontal travel along it." **[Stock fallback]** "glowing timeline horizontal abstract move"
  - **ON-SCREEN:** `WHAT ACTUALLY HAPPENS` center band low, head held high right so the lane stays readable.
  - **→ TRANSITION:** camera glides to the first node.
- **[00:05–00:13] Nodes 1–2.** VO: *"Here's the real sequence. You're booked and released on bond. You have fifteen days to protect your license."*
  - **B-ROLL PROMPT:** "Camera gliding node to node along the timeline; each node warms to gold as reached, a soft connecting line drawing itself forward beneath the camera." **[Stock fallback]** "connecting the dots line draw animation"
  - **ON-SCREEN:** node labels rise as reached: `Arrest → Booking → 15-Day ALR`; `15 DAYS` pulses gold.
  - **→ TRANSITION:** connecting line draws forward.
- **[00:13–00:23] Nodes 3–4.** VO: *"The criminal charge usually gets filed thirty to sixty days later. Then comes your first court setting."*
  - **B-ROLL PROMPT:** "The timeline continues building forward, two more nodes lighting to gold as the camera reaches them, warm trail behind." **[Stock fallback]** "timeline milestones lighting up sequence"
  - **ON-SCREEN:** `Charge Filed (30–60 days) → First Setting`.
  - **→ TRANSITION:** camera eases to the end of the line.
- **[00:23–00:31] Close + CTA.** VO: *"None of it is the end of your life — but the early moves matter most. The earlier we start, the more options you keep."*
  - **B-ROLL PROMPT:** "The full glowing timeline resolves and softens into warm gold light, open space lower-left."
  - **ON-SCREEN / END CARD:** `breathe. then act.` settles (words land a half-beat apart), then `First offense? Start here` + **(972) 370-5060**. Head top-right; footer visible.

**CTA overlay:** "First offense? Start here → (972) 370-5060"
**Caption:** What *actually* happens after a first DWI 🧭 #firstoffense #dwi #texas #dwilawyer #knowyourrights

---

## 12. "You'll Reach an Attorney. Not a Call Center." (Firm Differentiator)
**Avatar:** Reggie or Njeri (alternate) · **Voice:** speed 0.98×, tone *warm, human, welcoming* · **Head corner:** Top-left · **Runtime:** ~30s
**Marketing message:** Direct-to-attorney, flat fee in writing, no pressure. · **Tone:** Warm, human.

**Full VO for HeyGen:**
> "Call most firms after an arrest and you get a menu, a screener, a 'someone will call you back.' [pause] Call us — and an actual licensed attorney picks up. (beat) We'll ask what happened, read the report right there on the phone, and before we hang up you'll know your realistic punishment range, the first three moves we'd make, and a flat fee in writing. [pause] No pressure. Sleep on it. That's how it should work."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"Call most firms after an arrest and you get a menu, a screener, a 'someone will call you back.'"*
  - **B-ROLL PROMPT:** "A phone ringing in soft focus in the dark; cold blue holographic IVR menu buttons materialize floating in the air, flickering and glitching." **[Stock fallback]** "holographic UI buttons blue glitch dark"
  - **ON-SCREEN:** three chips `call center · paralegal triage · chatbot`, cold blue, top/center; head clears top-left.
  - **→ TRANSITION:** the cold buttons begin to dissolve.
- **[00:06–00:14] The shift.** VO: *"Call us — and an actual licensed attorney picks up."*
  - **B-ROLL PROMPT:** "The cold blue holographic buttons dissolve into scattering particles; through the clearing haze a warm human presence fades up answering the line, cold blue giving way to warm gold." **[Stock fallback]** "particles dissolve reveal warm light transition"
  - **ON-SCREEN:** the three chips cross out and glide off-frame in sequence.
  - **→ TRANSITION:** seamless cold-to-warm color shift.
- **[00:14–00:24] The promise.** VO: *"We'll ask what happened, read the report right there on the phone, and before we hang up you'll know your realistic punishment range, the first three moves we'd make, and a flat fee in writing."*
  - **B-ROLL PROMPT:** "Warm gold-lit desk, a document and phone in soft focus, a hand calmly turning a page, reassuring and unhurried." **[Stock fallback]** "hand turning document page warm desk"
  - **ON-SCREEN:** a single gold checkmark `a licensed attorney answers` settles in with a gentle bounce; small chips `punishment range · first 3 moves · flat fee in writing`.
  - **→ TRANSITION:** rack-focus to open space.
- **[00:24–00:30] Close + CTA.** VO: *"No pressure. Sleep on it. That's how it should work."*
  - **B-ROLL PROMPT:** "Warm gold light fills the frame, calm, open space right."
  - **ON-SCREEN / END CARD:** `Talk to a real attorney, free` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Talk to a real attorney, free → (972) 370-5060"
**Caption:** A human answers. Imagine that ☎️ #criminaldefense #lawyer #frisco #dallas #freeconsultation

---

## 13. "It's Not 'Just' Possession" (Drug Crimes / Penalty Groups)
**Avatar:** Njeri · **Voice:** speed 0.97×, tone *sobering, serious, measured* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Marketing message:** Texas drug law is brutal and tier-based — early defense changes everything. · **Tone:** Sobering.

**Full VO for HeyGen:**
> "In Texas, 'just possession' can still be a felony. [pause] The state sorts substances into penalty groups, and the charge scales with the group *and* the weight — and they count the whole mixture, not just the drug. (beat) Possession, delivery, even alleged intent — each is a different fight. [pause] Don't assume it's minor because the amount feels small. The label on the charge is where we start cutting."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"In Texas, 'just possession' can still be a felony."*
  - **B-ROLL PROMPT:** "An elegant brass balance scale on a dark surface tipping slowly under a tiny amount on one pan, single dramatic light, shallow depth." **[Stock fallback]** "brass balance scale tipping slow motion dark"
  - **ON-SCREEN:** `"JUST POSSESSION"?` center band, head clears bottom-left.
  - **→ TRANSITION:** camera pulls to reveal cards behind the scale.
- **[00:06–00:15] The tiers.** VO: *"The state sorts substances into penalty groups, and the charge scales with the group and the weight — and they count the whole mixture, not just the drug."*
  - **B-ROLL PROMPT:** "Behind the scale, cards labeled 'Penalty Group 1 / 2 / 3' stack and shuffle like a slow-dealing deck, each sliding into place." **[Stock fallback]** "cards dealing stacking slow motion macro"
  - **ON-SCREEN:** `HSC Ch. 481` ribbon slides in and anchors; `they count the whole mixture` small red.
  - **→ TRANSITION:** a stamp descends from top of frame.
- **[00:15–00:23] The stakes.** VO: *"Possession, delivery, even alleged intent — each is a different fight."*
  - **B-ROLL PROMPT:** "A large felony stamp hovering above the scene, slowly lowering and casting a softening shadow across the scale a beat before it touches down." **[Stock fallback]** "rubber stamp lowering shadow macro"
  - **ON-SCREEN:** `possession · delivery · manufacture` cross-fade in rotation; `FELONY?` rises in red, holds with a faint slow pulse.
  - **→ TRANSITION:** the stamp's shadow wipes to the close.
- **[00:23–00:30] Close + CTA.** VO: *"Don't assume it's minor because the amount feels small. The label on the charge is where we start cutting."*
  - **B-ROLL PROMPT:** "The scale rebalances toward level as warm gold light returns, open space right."
  - **ON-SCREEN / END CARD:** `Drug charge in DFW?` + **(972) 370-5060**. Head bottom-left; footer visible.

**CTA overlay:** "Drug charge in DFW? → (972) 370-5060"
**Caption:** "Just possession" is rarely just possession ⚖️ #drugcharges #texas #criminaldefense #penaltygroup #dallaslawyer

---

## 14. "Why Family Violence Charges Hit Harder" (Assault / Family Violence)
**Avatar:** Njeri · **Voice:** speed 0.96×, tone *serious, protective, grave* · **Head corner:** Top-right · **Runtime:** ~30s
**Marketing message:** The collateral consequences are lifelong — we fight the label, not just the case. · **Tone:** Serious, protective.

**Full VO for HeyGen:**
> "An assault–family-violence charge is more than the case in front of you. [pause] That label can follow you into your gun rights, your job, your housing, future enhancements — even after the case is 'over.' (beat) The bond conditions alone can lock you out of your own home. [pause] This is exactly the kind of charge where the *finding* matters as much as the outcome. We fight both."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"An assault–family-violence charge is more than the case in front of you."*
  - **B-ROLL PROMPT:** "A single document stamped with a bold label lying in one pool of light on a dark desk, long shadow beginning to stretch from it." **[Stock fallback]** "stamped document dramatic light long shadow"
  - **ON-SCREEN:** `IT'S MORE THAN THE CASE` center band, head clears top-right.
  - **→ TRANSITION:** the shadow begins to crawl.
- **[00:06–00:16] The shadow crawl.** VO: *"That label can follow you into your gun rights, your job, your housing, future enhancements — even after the case is 'over.'"*
  - **B-ROLL PROMPT:** "The document's shadow stretches and travels slowly across three softly lit icons in a row — a firearm, a house key, a briefcase — and as the shadow passes over each, that icon quietly dims." **[Stock fallback]** "shadow moving across objects slow reveal"
  - **ON-SCREEN:** `an affirmative finding follows you` types on quietly; as each icon dims, a small `✕ affected` tag fades in beside it.
  - **→ TRANSITION:** shadow continues to the last icon.
- **[00:16–00:24] The home.** VO: *"The bond conditions alone can lock you out of your own home."*
  - **B-ROLL PROMPT:** "The house-key icon dims fully and a faint locked-door outline appears, cold light, the shadow settling heavily over it." **[Stock fallback]** "locked door silhouette cold light"
  - **ON-SCREEN:** `locked out of your own home` small red.
  - **→ TRANSITION:** light-leak wipe to the close.
- **[00:24–00:30] Close + CTA.** VO: *"This is exactly the kind of charge where the finding matters as much as the outcome. We fight both."*
  - **B-ROLL PROMPT:** "The three icons relight to warm gold as the shadow recedes, open space lower-left."
  - **ON-SCREEN / END CARD:** `We fight the label, not just the case.` then `Accused of family violence?` + **(972) 370-5060**. Head top-right; footer visible.

**CTA overlay:** "Accused of family violence? → (972) 370-5060"
**Caption:** It's the label that follows you 🏠 #familyviolence #assault #texas #criminaldefense #knowyourrights

---

## 15. "Don't Let a Mistake Define a Kid's Future" (Juvenile Defense)
**Avatar:** Njeri · **Voice:** speed 0.97×, tone *compassionate, parent-to-parent, warm* · **Head corner:** Top-left · **Runtime:** ~31s
**Marketing message:** Juvenile records can be sealed — protect the opportunities ahead. · **Tone:** Compassionate, parent-to-parent.

**Full VO for HeyGen:**
> "When it's your child, every instinct says panic. [pause] Take a breath. (beat) In Texas, juvenile cases run on different rules — and many records can be sealed so a teenage mistake doesn't shadow college applications, jobs, or scholarships. [pause] The goal isn't just this case. It's protecting every door that's supposed to open later. That's the whole point of doing this right, early."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"When it's your child, every instinct says panic. Take a breath."*
  - **B-ROLL PROMPT:** "A young silhouette walking forward toward a bright horizon — a distant campus and office buildings — in slow hopeful forward motion, warm dawn light, camera trailing gently behind." **[Stock fallback]** "silhouette walking toward horizon hopeful dawn"
  - **ON-SCREEN:** `TAKE A BREATH` center band, head clears top-left.
  - **→ TRANSITION:** camera trails the walking figure.
- **[00:06–00:16] The rules.** VO: *"In Texas, juvenile cases run on different rules — and many records can be sealed so a teenage mistake doesn't shadow college applications, jobs, or scholarships."*
  - **B-ROLL PROMPT:** "Over the figure's shoulder, a paper labeled 'RECORD' lifts off and lowers gently into a vault that seals with a soft warm glow, leaving the path ahead clear and bright." **[Stock fallback]** "document into vault sealing glow"
  - **ON-SCREEN:** `Family Code Ch. 58 — sealing` banners in gently; small chips `college · jobs · scholarships`.
  - **→ TRANSITION:** the light builds as the figure keeps walking.
- **[00:16–00:24] The goal.** VO: *"The goal isn't just this case. It's protecting every door that's supposed to open later."*
  - **B-ROLL PROMPT:** "The horizon brightens; distant building doorways glow softly gold one by one as the figure approaches, warm and hopeful." **[Stock fallback]** "doorways glowing light hopeful path"
  - **ON-SCREEN:** the word `future` briefly warms brighter than the rest.
  - **→ TRANSITION:** soft light bloom to the close.
- **[00:24–00:31] Close + CTA.** VO: *"That's the whole point of doing this right, early."*
  - **B-ROLL PROMPT:** "Full warm gold light on the clear path ahead, open space right."
  - **ON-SCREEN / END CARD:** `one mistake ≠ a life sentence` then `Protect your child's record` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Protect your child's record → (972) 370-5060"
**Caption:** A teenage mistake shouldn't cost the future 🎓 #juveniledefense #texas #parenting #criminaldefense #secondchance

---

## 16. "You Don't Have to Sit in Jail" (Bond Reduction)
**Avatar:** Reggie · **Voice:** speed 1.0×, tone *action-oriented, urgent-but-calm* · **Head corner:** Bottom-right (relocate captions to upper-center) · **Runtime:** ~29s
**Marketing message:** High bond isn't final — we move fast to get people out. · **Tone:** Action-oriented, urgent-but-calm.

**Full VO for HeyGen:**
> "Bond set too high to pay? [pause] That number is not carved in stone. (beat) We can request a bond reduction hearing and argue the things that actually move a judge — ties to the community, no flight risk, the real facts of the case. [pause] Every day someone sits in jail is a day they can't help their own defense. So we move fast. The clock matters here too."

### Shot-by-shot
> **Caption note:** because the head is bottom-right this video, burn all captions in the **upper-center** band.
- **[00:00–00:05] Hook.** VO: *"Bond set too high to pay?"*
  - **B-ROLL PROMPT:** "A large glowing red number labeled 'BOND' hovering in the dark, heavy and immovable, a judge's gavel resting below it in soft focus." **[Stock fallback]** "glowing red number dark" + "gavel close up dark"
  - **ON-SCREEN:** `TOO HIGH TO PAY?` upper-center (head bottom-right).
  - **→ TRANSITION:** the gavel begins to tap.
- **[00:05–00:14] The mechanism.** VO: *"That number is not carved in stone. We can request a bond reduction hearing and argue the things that actually move a judge — ties to the community, no flight risk, the real facts of the case."*
  - **B-ROLL PROMPT:** "With each slow gavel tap the red number eases downward trailing a soft motion-blur, counting down; behind it jail bars gradually thin and lose opacity." **[Stock fallback]** "number countdown motion blur" + "jail bars dissolving light"
  - **ON-SCREEN:** the figure counts down smoothly (each lower number settling before the next tap); chips `community ties · no flight risk · real facts`.
  - **→ TRANSITION:** bars keep dissolving into daylight shafts.
- **[00:14–00:22] The urgency.** VO: *"Every day someone sits in jail is a day they can't help their own defense."*
  - **B-ROLL PROMPT:** "The jail bars dissolve fully into vertical shafts of warm daylight, confinement becoming open air, camera easing forward into the light." **[Stock fallback]** "prison bars to daylight transition hopeful"
  - **ON-SCREEN:** `motion for bond reduction` resolves with a calm stamp-and-settle.
  - **→ TRANSITION:** light bloom to the close.
- **[00:22–00:29] Close + CTA.** VO: *"So we move fast. The clock matters here too."*
  - **B-ROLL PROMPT:** "Open daylight fills the frame, calm and free, open space upper-left."
  - **ON-SCREEN / END CARD:** `That bond number can come down` + **(972) 370-5060** (kept upper-center/left, clear of head). Footer visible.

**CTA overlay:** "Loved one stuck on high bond? → (972) 370-5060"
**Caption:** That bond number can come down ⬇️ #bondreduction #jail #texas #criminaldefense #dallas

---

## 17. "Free Tools Before You Even Hire Us" (Calculators / Value)
**Avatar:** Reggie · **Voice:** speed 1.0×, tone *generous, upbeat, "try it yourself"* · **Head corner:** Top-left · **Runtime:** ~30s
**Marketing message:** We give value first — six free calculators, no signup. · **Tone:** Generous, "try it yourself."

**Full VO for HeyGen:**
> "Before you ever call a lawyer, you deserve to know what you're facing. [pause] So we built it free. (beat) Six calculators on our site — punishment ranges for any Texas charge, DWI bond estimates, even an expunction eligibility checker. [pause] No signup. No email wall. Plug in your situation and see the real range. Then, if you want a human to make sense of it, we're one call away."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"Before you ever call a lawyer, you deserve to know what you're facing."*
  - **B-ROLL PROMPT:** "A clean modern phone UI gliding into frame on a dark plum background, camera floating just above the glowing screen, generic slider controls visible (no readable brand text)." **[Stock fallback]** "phone screen ui sliders close up floating"
  - **ON-SCREEN:** `KNOW WHAT YOU'RE FACING` center band, head clears top-left.
  - **→ TRANSITION:** fingers reach for a slider.
- **[00:06–00:15] The tools.** VO: *"So we built it free. Six calculators on our site — punishment ranges for any Texas charge, DWI bond estimates, even an expunction eligibility checker."*
  - **B-ROLL PROMPT:** "Fingers easing sliders labeled generically (BAC, priors, charge level) and a results bar filling fluidly with warm gold, satisfying and smooth." **[Stock fallback]** "finger sliding UI slider result bar fill"
  - **ON-SCREEN:** `6 FREE TOOLS` resolves in gold; tool-name cards `Punishment Range · DWI Bond · Expunction Checker`.
  - **→ TRANSITION:** the view flips between tool cards like pages turning in soft 3-D.
- **[00:15–00:24] The reassurance.** VO: *"No signup. No email wall. Plug in your situation and see the real range."*
  - **B-ROLL PROMPT:** "Three tool cards flipping in sequence in soft 3-D, each settling face-up before the next begins, warm gold accents." **[Stock fallback]** "3d cards flipping sequence ui"
  - **ON-SCREEN:** `no signup` fades up as a small teal reassuring tag.
  - **→ TRANSITION:** last card settles, light-leak to close.
- **[00:24–00:30] Close + CTA.** VO: *"Then, if you want a human to make sense of it, we're one call away."*
  - **B-ROLL PROMPT:** "The phone screen softens into warm gold light, open space right."
  - **ON-SCREEN / END CARD:** `Free tools at landllawgroup.com` + `Questions? (972) 370-5060`. Head top-left; footer visible.

**CTA overlay:** "Free tools at landllawgroup.com · Questions? (972) 370-5060"
**Caption:** Free legal calculators, zero signup 🧮 #legaltools #texas #dwi #expunction #criminaldefense

---

## 18. "Should I Just Explain My Side to the Police?" (Right to Remain Silent)
**Avatar:** Reggie · **Voice:** speed 0.98×, tone *direct, protective, level* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Marketing message:** Cooperation ≠ confession — talk to us *before* you talk to them. · **Tone:** Direct, protective.

**Full VO for HeyGen:**
> "The most dangerous sentence after an arrest: *'I'll just explain my side and clear this up.'* [pause] I get the instinct. (beat) But that conversation isn't a clarification — it's evidence collection. [pause] You can be respectful and *still* say, *'I want a lawyer, and I'm not answering questions.'* That's not suspicious. It's smart. Let us explain your side — in the place where it actually helps you."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"The most dangerous sentence after an arrest: 'I'll just explain my side and clear this up.'"*
  - **B-ROLL PROMPT:** "A warm, inviting interview room, soft lamp light, camera drifting slowly inward toward a table with two chairs, comfortable and disarming." **[Stock fallback]** "interview room warm light slow push in"
  - **ON-SCREEN:** `"I'll just explain my side…"` rises center band, head clears bottom-left.
  - **→ TRANSITION:** continuous push-in.
- **[00:06–00:15] The reframe.** VO: *"I get the instinct. But that conversation isn't a clarification — it's evidence collection."*
  - **B-ROLL PROMPT:** "As the camera pushes in, a small red recording light blooms to life in the upper corner of the room, quietly recontextualizing the warmth into caution." **[Stock fallback]** "red recording light blinking dark corner"
  - **ON-SCREEN:** the earlier line `"I just wanted to explain…"` warms to red as the recording light blooms; `everything is evidence` fades up beneath, calm and final.
  - **→ TRANSITION:** a speech bubble lifts off the table.
- **[00:15–00:23] The image.** VO: *"You can be respectful and still say, 'I want a lawyer, and I'm not answering questions.'"*
  - **B-ROLL PROMPT:** "A translucent speech bubble lifts gently off the table and is filed away into a folder labeled generically that slides shut, smooth and deliberate." **[Stock fallback]** "file folder closing document macro"
  - **ON-SCREEN:** `"I want a lawyer."` types on in Off-White, quote-style.
  - **→ TRANSITION:** rack-focus to open space.
- **[00:23–00:30] Close + CTA.** VO: *"That's not suspicious. It's smart. Let us explain your side — in the place where it actually helps you."*
  - **B-ROLL PROMPT:** "The recording light fades and warm calm light returns, open space right."
  - **ON-SCREEN / END CARD:** `Before you talk to police, call us` + **(972) 370-5060**. Head bottom-left; footer visible.

**CTA overlay:** "Before you talk to police, call us → (972) 370-5060"
**Caption:** "Explaining your side" is a trap 🤐 #knowyourrights #remainsilent #criminaldefense #texas #lawyer

---

## 19. "What Refusing the Breath Test Really Costs" (DWI Refusal)
**Avatar:** Reggie · **Voice:** speed 0.99×, tone *real-talk, honest, no scare-mongering* · **Head corner:** Top-left · **Runtime:** ~31s
**Marketing message:** Refusal has consequences *and* defenses — don't navigate it blind. · **Tone:** Real-talk, no scare-mongering.

**Full VO for HeyGen:**
> "Refused the breath or blood test? Here's the honest version. [pause] A refusal can trigger a longer license suspension — and a failed test triggers its own. (beat) *But* — that suspension isn't automatic if you fight the ALR hearing in time. [pause] At that hearing we can challenge the stop, the request for a sample, the whole basis. Refusing isn't the end of the story. Missing the deadline is."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"Refused the breath or blood test? Here's the honest version."*
  - **B-ROLL PROMPT:** "A breathalyzer device glowing in the dark with a prompt reading 'REFUSE?', single cold light, shallow depth of field." **[Stock fallback]** "breathalyzer device glowing dark macro"
  - **ON-SCREEN:** `WHAT REFUSAL REALLY COSTS` center band, head clears top-left.
  - **→ TRANSITION:** two lines of light branch from the device.
- **[00:06–00:16] The branches.** VO: *"A refusal can trigger a longer license suspension — and a failed test triggers its own."*
  - **B-ROLL PROMPT:** "From the breathalyzer, two softly lit timelines branch and travel forward on a dark plane — one labeled with a longer span, one shorter — small license icons along each dimming in sequence." **[Stock fallback]** "two diverging glowing paths timeline abstract"
  - **ON-SCREEN:** branch labels ride their lines: `refuse → up to 180-day` and `.08+ → 90-day` resolve as the lines extend.
  - **→ TRANSITION:** a third path begins to light between them.
- **[00:16–00:24] The hope.** VO: *"But — that suspension isn't automatic if you fight the ALR hearing in time."*
  - **B-ROLL PROMPT:** "A third brighter path lights up between the two dim timelines, warmer gold, pulling the eye forward toward hope." **[Stock fallback]** "bright path emerging between dim paths"
  - **ON-SCREEN:** middle path labeled `ALR — winnable`, brighter than the rest.
  - **→ TRANSITION:** camera follows the bright path forward.
- **[00:24–00:31] Close + CTA.** VO: *"At that hearing we can challenge the stop, the request for a sample, the whole basis. Refusing isn't the end of the story. Missing the deadline is."*
  - **B-ROLL PROMPT:** "The bright middle path resolves into warm gold light, open space right."
  - **ON-SCREEN / END CARD:** `but the deadline is the real enemy` settles in gold, then `Refused the test? 15-day clock is running` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Refused the test? 15-day clock is running → (972) 370-5060"
**Caption:** What refusal actually costs (and how to fight it) 💨 #dwi #breathtest #alr #texas #knowyourrights

---

## 20. "Surviving the Ignition Interlock" (IID Guide)
**Avatar:** Njeri · **Voice:** speed 0.99×, tone *practical, matter-of-fact, helpful* · **Head corner:** Top-right · **Runtime:** ~32s
**Marketing message:** One interlock mistake can revoke your bond — we keep you driving and compliant. · **Tone:** Practical.

**Full VO for HeyGen:**
> "If a judge orders an ignition interlock, the rules are strict and the traps are real. [pause] You usually have thirty days to install it. (beat) It's mandatory for repeat offenses, a high BAC, or an accident with injury. [pause] And a single technical violation — even a false reading — can land you back in front of the judge. If your license is suspended, we can also pursue an occupational license so you keep getting to work. Compliance *and* mobility — both matter."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"If a judge orders an ignition interlock, the rules are strict and the traps are real."*
  - **B-ROLL PROMPT:** "Close-up of a dashboard-mounted ignition interlock device in a dim car interior, a green 'PASS' indicator glowing softly." **[Stock fallback]** "ignition interlock device dashboard close up"
  - **ON-SCREEN:** `THE INTERLOCK TRAPS` center band, head clears top-right.
  - **→ TRANSITION:** a wall calendar comes into focus behind the device.
- **[00:06–00:15] The clock.** VO: *"You usually have thirty days to install it."*
  - **B-ROLL PROMPT:** "Behind the device, a wall calendar with a single leaf peeling away in slow motion, warm-to-cold light, shallow focus breathing." **[Stock fallback]** "calendar page peeling slow motion"
  - **ON-SCREEN:** `30 DAYS TO INSTALL`; `Art. 17.40 bond condition` ribbon eases in.
  - **→ TRANSITION:** rack-focus back to the device.
- **[00:15–00:24] The traps.** VO: *"It's mandatory for repeat offenses, a high BAC, or an accident with injury. And a single technical violation — even a false reading — can land you back in front of the judge."*
  - **B-ROLL PROMPT:** "The device's green 'PASS' flickers to a red 'FAIL', the camera tightening a touch to mirror the gut-drop, tense cold light." **[Stock fallback]** "device screen pass to fail red flicker"
  - **ON-SCREEN:** trigger chips `repeat · BAC .15+ · injury` fade up in sequence.
  - **→ TRANSITION:** the red fades toward a calmer light.
- **[00:24–00:32] Close + CTA.** VO: *"If your license is suspended, we can also pursue an occupational license so you keep getting to work. Compliance and mobility — both matter."*
  - **B-ROLL PROMPT:** "The car pulls out into calm warm daylight, the road open ahead, reassuring, open space lower-left." **[Stock fallback]** "car driving into daylight open road pov"
  - **ON-SCREEN / END CARD:** `ODL = keep driving` resolves in teal, then `Interlock or license questions?` + **(972) 370-5060**. Head top-right; footer visible.

**CTA overlay:** "Interlock or license questions? → (972) 370-5060"
**Caption:** Don't let the interlock revoke your bond 🚙 #dwi #ignitioninterlock #texas #occupationallicense #knowyourrights

---

## 21. "Federal Charges Are a Different Animal" (Federal Defense)
**Avatar:** Reggie · **Voice:** speed 0.95×, tone *gravely serious, weighty, deliberate* · **Head corner:** Top-left · **Runtime:** ~31s
**Marketing message:** TXND/TXED federal work demands different firepower — we're admitted and ready. · **Tone:** Gravely serious.

**Full VO for HeyGen:**
> "If your case went *federal*, throw out the state playbook. [pause] Different court, different prosecutors, different math — federal sentencing runs on guidelines, and the government usually shows up prepared and patient. (beat) This is where mitigation, early strategy, and someone admitted in the Northern and Eastern Districts of Texas actually matters. [pause] The stakes are higher, so the defense has to start sharper, sooner."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"If your case went federal, throw out the state playbook."*
  - **B-ROLL PROMPT:** "A slow reverent push toward a monumental federal courthouse façade at dusk, low light raking across engraved stone letters reading 'U.S. DISTRICT COURT', imposing and quiet." **[Stock fallback]** "federal courthouse facade dramatic dusk push in"
  - **ON-SCREEN:** `FEDERAL ≠ STATE` center band, head clears top-left.
  - **→ TRANSITION:** the façade begins to dissolve into a grid.
- **[00:06–00:16] The math.** VO: *"Different court, different prosecutors, different math — federal sentencing runs on guidelines, and the government usually shows up prepared and patient."*
  - **B-ROLL PROMPT:** "The stone façade dissolves seamlessly into a glowing sentencing-guidelines grid that builds itself cell by cell as the camera continues forward, cold precise light." **[Stock fallback]** "glowing data grid building cells forward move"
  - **ON-SCREEN:** `guidelines ≠ state ranges` resolves in red, holding steady; badges `TXND · TXED · 5th Circuit` settle in sequence.
  - **→ TRANSITION:** from the grid lines a word assembles.
- **[00:16–00:24] The answer.** VO: *"This is where mitigation, early strategy, and someone admitted in the Northern and Eastern Districts of Texas actually matters."*
  - **B-ROLL PROMPT:** "From the grid lines, the word 'MITIGATION' assembles from the glowing cells — order emerging from the machinery, warming from cold to gold." **[Stock fallback]** "word assembling from particles gold"
  - **ON-SCREEN:** `MITIGATION` assembles in gold.
  - **→ TRANSITION:** light-leak to close.
- **[00:24–00:31] Close + CTA.** VO: *"The stakes are higher, so the defense has to start sharper, sooner."*
  - **B-ROLL PROMPT:** "The grid resolves into steady warm gold light, imposing but hopeful, open space right."
  - **ON-SCREEN / END CARD:** `Federal investigation or charge?` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Federal investigation or charge? → (972) 370-5060"
**Caption:** Federal ≠ state. Don't bring a knife. 🏛️ #federalcrime #txnd #txed #criminaldefense #texas

---

## 22. "The First Three Moves We Make" (Process / Credibility)
**Avatar:** Reggie · **Voice:** speed 1.0×, tone *confident, brisk, momentum-driven* · **Head corner:** Top-center, small · **Runtime:** ~29s
**Marketing message:** We don't wait — discovery, theory, and the first motion all in week one. · **Tone:** Confident.

**Full VO for HeyGen:**
> "People think hiring a lawyer means 'now we wait.' [pause] Not here. (beat) Week one: we request discovery and get the State's evidence on the table. We build the defense theory — what actually happened versus what they claim. And we outline the first motion. [pause] By the time most people are still panicking, your file is already *moving.* Momentum is a strategy."

### Shot-by-shot
- **[00:00–00:05] Hook.** VO: *"People think hiring a lawyer means 'now we wait.' Not here."*
  - **B-ROLL PROMPT:** "Three frosted-glass panels on a dark plum background beginning to slide in from the right, depth and reflection on the glass, cinematic." **[Stock fallback]** "frosted glass panels sliding 3d dark"
  - **ON-SCREEN:** `NOW WE WAIT? NO.` held high center so it doesn't cover the top-center head.
  - **→ TRANSITION:** first panel locks into place.
- **[00:05–00:13] Move 1.** VO: *"Week one: we request discovery and get the State's evidence on the table."*
  - **B-ROLL PROMPT:** "The first frosted-glass panel locks edge-to-edge like a domino settling, camera gliding past it, warm gold edge-light." **[Stock fallback]** "glass panel snapping into place reflection"
  - **ON-SCREEN:** panel `PULL DISCOVERY`; `WEEK ONE.` stamp eases in large; chip `1` with soft overshoot.
  - **→ TRANSITION:** camera glides to the second panel.
- **[00:13–00:21] Moves 2 & 3.** VO: *"We build the defense theory — what actually happened versus what they claim. And we outline the first motion."*
  - **B-ROLL PROMPT:** "Two more frosted-glass panels slide in and lock edge-to-edge like dominoes, the camera gliding past each as it clicks into place." **[Stock fallback]** "panels aligning sequence dominoes glass"
  - **ON-SCREEN:** panels `BUILD THE THEORY` and `FILE THE FIRST MOTION`; chips count `2 → 3`, each landing as its panel locks.
  - **→ TRANSITION:** camera pulls back to reveal all three.
- **[00:21–00:29] Close + CTA.** VO: *"By the time most people are still panicking, your file is already moving. Momentum is a strategy."*
  - **B-ROLL PROMPT:** "The three locked glass panels glow warm gold together, camera easing back into open light, open space lower area."
  - **ON-SCREEN / END CARD:** `Get your case moving` + **(972) 370-5060**. Head top-center; footer visible.

**CTA overlay:** "Get your case moving → (972) 370-5060"
**Caption:** What we do in the FIRST week ⚡ #criminaldefense #lawyer #texas #legalstrategy #dallas

---

## 23. "Theft Charges Scale With the Price Tag" (Theft Defense)
**Avatar:** Njeri · **Voice:** speed 0.98×, tone *clarifying, measured, informative* · **Head corner:** Bottom-left · **Runtime:** ~30s
**Marketing message:** The dollar value sets the tier — and the tier sets your future. We fight both. · **Tone:** Clarifying.

**Full VO for HeyGen:**
> "Texas theft law has a dial — and it's the dollar value. [pause] A low amount might be a ticket-level offense; cross the thresholds and you're staring at a felony, for the *same kind* of act. (beat) And theft is a 'crime of moral turpitude' — it can haunt job and license applications for years. [pause] So we fight on two fronts: the facts of the case *and* the value tier they're trying to pin on you."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"Texas theft law has a dial — and it's the dollar value."*
  - **B-ROLL PROMPT:** "A price tag spinning its numbers upward in soft motion-blur on a dark surface, single dramatic light, shallow depth." **[Stock fallback]** "price tag numbers spinning up macro"
  - **ON-SCREEN:** `IT'S A DIAL` center band, head clears bottom-left.
  - **→ TRANSITION:** a vertical meter appears beside the tag.
- **[00:06–00:16] The climb.** VO: *"A low amount might be a ticket-level offense; cross the thresholds and you're staring at a felony, for the same kind of act."*
  - **B-ROLL PROMPT:** "A vertical meter on the right climbing smoothly from a low mark to a high mark as the price tag rises, the lighting cooling from warm to cold as it climbs, stakes hardening." **[Stock fallback]** "vertical meter rising gauge fill cold"
  - **ON-SCREEN:** `value = charge level` ribbon; the tier ladder illuminates rung by rung `Class C → 1st-Degree Felony` as the meter passes each.
  - **→ TRANSITION:** a faint 'RECORD' stamp looms in the deep background gaining definition.
- **[00:16–00:24] The shadow.** VO: *"And theft is a 'crime of moral turpitude' — it can haunt job and license applications for years."*
  - **B-ROLL PROMPT:** "A faint stamp reading 'RECORD' slowly gains definition in the cold, deep background behind the meter, ominous." **[Stock fallback]** "faint stamp emerging background cold light"
  - **ON-SCREEN:** `follows you for years` fades up at the top of the meter.
  - **→ TRANSITION:** light-leak wipe to close.
- **[00:24–00:30] Close + CTA.** VO: *"So we fight on two fronts: the facts of the case and the value tier they're trying to pin on you."*
  - **B-ROLL PROMPT:** "The meter and tag warm back to gold, balanced, open space right."
  - **ON-SCREEN / END CARD:** `Theft or shoplifting charge?` + **(972) 370-5060**. Head bottom-left; footer visible.

**CTA overlay:** "Theft or shoplifting charge? → (972) 370-5060"
**Caption:** The price tag decides your charge 🏷️ #theft #shoplifting #texas #criminaldefense #knowyourrights

---

## 24. "Arrested Tonight? Do This." (24/7 Jail-Release)
**Avatar:** Reggie or Njeri (alternate) · **Voice:** speed 0.98×, tone *calm command, midnight-emergency, steady and reassuring* · **Head corner:** Top-right · **Runtime:** ~30s
**Marketing message:** Our line is 24/7 because arrests don't keep office hours. · **Tone:** Calm command, midnight-emergency.

**Full VO for HeyGen:**
> "It's the middle of the night, someone you love just got arrested, and you don't know what to do. [pause] Three things. (beat) One — they should stay silent; no statements, no 'explaining.' Two — don't consent to searches. Three — call us. [pause] Our line is answered twenty-four-seven by an actual attorney, because nobody schedules an arrest for business hours. We'll talk bond and the next move tonight."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"It's the middle of the night, someone you love just got arrested, and you don't know what to do."*
  - **B-ROLL PROMPT:** "A phone glowing alone in a dark room, screen reading '2:47 AM', shallow depth of field, quiet and tense." **[Stock fallback]** "phone glowing dark room night close up"
  - **ON-SCREEN:** `2:47 AM` sets quietly; head clears top-right.
  - **→ TRANSITION:** the call connects, warm light begins to spread.
- **[00:06–00:20] The three steps.** VO: *"Three things. One — they should stay silent; no statements, no 'explaining.' Two — don't consent to searches. Three — call us."*
  - **B-ROLL PROMPT:** "A calm wash of warm gold light spreading outward from the glowing phone, pushing back the dark, as a checklist writes itself in line by line as if by a steady hand." **[Stock fallback]** "warm light spreading from phone dark to warm"
  - **ON-SCREEN:** steps write on in rhythm with the VO, each landing as spoken: `1. stay silent · 2. don't consent · 3. call us`.
  - **→ TRANSITION:** the checklist completes, light fully warm.
- **[00:20–00:30] Close + CTA.** VO: *"Our line is answered twenty-four-seven by an actual attorney, because nobody schedules an arrest for business hours. We'll talk bond and the next move tonight."*
  - **B-ROLL PROMPT:** "The warm light settles into a calm reassuring glow around the phone, panic resolved into plan, open space lower-left."
  - **ON-SCREEN / END CARD:** `Arrested right now?` + **(972) 370-5060 · 24/7**. Head top-right; footer visible.

**CTA overlay:** "Arrested right now? → (972) 370-5060 · 24/7"
**Caption:** Save this before you need it 🌙 #arrested #knowyourrights #jailrelease #texas #criminaldefense

---

## 25. "'I'll Just Plead Guilty to Get It Over With'" (The Quiet-Plea Trap)
**Avatar:** Njeri · **Voice:** speed 0.97×, tone *wise, gently corrective, warm but firm* · **Head corner:** Top-left · **Runtime:** ~31s
**Marketing message:** The fast plea is often the expensive one — let us look first. · **Tone:** Wise, gently corrective.

**Full VO for HeyGen:**
> "I hear it constantly: *'I just want this gone — I'll plead guilty and move on.'* [pause] I understand the exhaustion. (beat) But a quick plea can carry consequences nobody warned you about — a permanent record, license issues, future enhancements, doors that quietly close years later. [pause] Pleading guilty is a *right* — but it should be a decision, not a reflex. Let an attorney look first. It's free, and it might change everything."

### Shot-by-shot
- **[00:00–00:06] Hook.** VO: *"I hear it constantly: 'I just want this gone — I'll plead guilty and move on.'"*
  - **B-ROLL PROMPT:** "A hand drifting slowly toward a document bearing a 'PLEAD GUILTY' stamp on a dark desk, single dramatic light, tension in the slow approach." **[Stock fallback]** "hand reaching to stamp document slow macro"
  - **ON-SCREEN:** `"I'll just plead guilty."` center band, head clears top-left.
  - **→ TRANSITION:** the hand's motion eases toward a freeze.
- **[00:06–00:15] The pause.** VO: *"I understand the exhaustion. But a quick plea can carry consequences nobody warned you about…"*
  - **B-ROLL PROMPT:** "Just before the hand lands, the motion eases to a freeze and a magnifying glass glides into frame over the document, particles drifting so motion never fully dies." **[Stock fallback]** "magnifying glass over document freeze macro"
  - **ON-SCREEN:** `fast ≠ free` fades up in red.
  - **→ TRANSITION:** the lens reveals what's hidden beneath.
- **[00:15–00:24] The reveal.** VO: *"…a permanent record, license issues, future enhancements, doors that quietly close years later."*
  - **B-ROLL PROMPT:** "Through the magnifying lens, hidden cost-icons surface from beneath the paper like watermarks slowly rising — a record, a license, a career, an immigration stamp — gentle and gradual, which makes it land harder." **[Stock fallback]** "watermark icons rising from paper reveal"
  - **ON-SCREEN:** hidden-cost icons `RECORD · LICENSE · CAREER · ENHANCEMENTS` surface one at a time with a soft watermark-style reveal.
  - **→ TRANSITION:** light-leak wipe to close.
- **[00:24–00:31] Close + CTA.** VO: *"Pleading guilty is a right — but it should be a decision, not a reflex. Let an attorney look first. It's free, and it might change everything."*
  - **B-ROLL PROMPT:** "The document softens into warm gold light, the hand withdrawing calmly, open space right."
  - **ON-SCREEN / END CARD:** `Before you plead, talk to us — free` + **(972) 370-5060**. Head top-left; footer visible.

**CTA overlay:** "Before you plead, talk to us — free → (972) 370-5060"
**Caption:** The fastest option is rarely the cheapest 🛑 #criminaldefense #plea #knowyourrights #texas #lawyer

---

# 🎬 PRODUCTION CHEAT SHEET (pin this in HeyGen)

**Per-video build order (v4)**
1. **Avatar VO:** paste the "Full VO for HeyGen" block into the avatar script box (keep the `[pause]` / emphasis markers). Generate on green screen with a neutral dark/green background prompt → mask to a **soft circle with a gold halo**, scale to **~28–34% width**, pin it in the corner on that script's header line. Add the constant 3–5px parallax drift.
2. **B-roll:** generate each timecoded beat's **B-ROLL PROMPT** (append the default suffix) at 5–8s in your text-to-video tool, OR pull the **[Stock fallback]** clip. Stitch beats with cross-dissolves / match-cuts / light-leaks / rack-focus into **one continuous, full-frame move** — **never** a hard cut, **never** a still, **never** shrink the b-roll to share the frame.
3. **Graphics + captions:** layer the per-beat **ON-SCREEN** kinetic text (draw-on, cross-dissolve, assemble-from-particles) in the center band or opposite the head corner; burn word-by-word captions.
4. **End card:** keep the head in its corner through the last 3 sec; the phone number + CTA line resolves in the open space listed per script.
5. Add trending low-lyric audio, keep the compliance footer visible, export 1080×1920.

**The v3/v4 layout rule:** full-screen motion background + a small corner talking head, on screen 100% of the time. If the head ever covers the b-roll's focal action, move it to the opposite corner — that's exactly what the per-script "Head corner" cue prevents.

**Hook discipline:** the first line of every script *is* the hook — oversized on screen in second 1, placed opposite the head corner. Earn the watch, then brand.

**Timing discipline (new in v4):** the beat timecodes are targets. HeyGen VO length varies ±1–2s by voice and speed — match the b-roll clip lengths to the *actual* generated VO, and never trim the VO to hit a timecode. Total runtime should land inside **22–42 sec**.

**Avatar rotation:** Reggie for "prosecutor's-edge / courtroom" angles (1,2,4,5,7,8,10,12,16,17,18,19,21,22,24); Njeri for "protective / second-chance / family" angles (3,6,9,11,13,14,15,20,23,25).

**Series tags (use on all):** `#criminaldefense #texas #frisco #dallas #knowyourrights #dwilawyer`
**Posting cadence:** 3–5×/week; lead the week with an urgency topic (1, 3, 19, 24), close it with a hope topic (9, 13, 15, 25).

**Compliance footer (every single video):**
> *Attorney Advertising. L and L Law Group, PLLC — Njeri London & Reggie London, Frisco, TX. General information, not legal advice. Past results do not guarantee future outcomes.*
