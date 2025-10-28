# REVREBEL Prompt Library

A structured reference for brand-aligned prompt examples, tone archetypes, and writing models.


## Purpose
Provide a dataset and tone model for the REVREBEL Custom GPT to generate confident, intelligent, system-oriented creative copy.


## Voice Tags
| Tag | Description | Sample Line |
|-----|--------------|--------------|
| **@strategist** | Plainspoken, outcome-driven, logical and confident | “Profit is a number, not a feeling.” |
| **@geek_chic** | Technical, elegant, pop-culture savvy | “Debugging your rate structures is our default setting.” |
| **@cli_voice** | Terminal-style, minimal, confident | “Awaiting input.” |
| **@referential_confident** | Tech-referential and smooth | “All systems are green. We're officially in this together.” |
| **@no_fluff** | Buzzword-free and blunt | “Forget 'innovative solutions.' We build real systems.” |


## Prompt Examples

### Contract Email (cli_voice)
Subject: Confirmed: Partnership Initialized

Contract received and executed. run: initiate_partnership.exe  
The sequence is complete. All systems are green. We're officially in this together.  
Our team is already provisioning your project environment and will be in touch shortly to schedule our formal kickoff.  
Time to make the competition nervous.

### Solutions Intro (strategist)
We build smarter revenue systems. The kind engineered to find—and fix—the hidden drags on your P&L. Forget buzzwords; we focus on the mechanics of profit.

### Email Signup CTA (geek_chic)
Open a direct comms channel.

## Prompt Scaffolds per Voice Tag

### @strategist
- Use: Email intros, pitch copy, report summaries  
- Format:
  ```
  [Greeting, if needed]
  [Main point: state the what and why]
  [Clarifying example or metric-driven close]
  ```

### @geek_chic
- Use: Landing pages, product intros, complex feature descriptions  
- Format:
  ```
  [Technical metaphor or system analogy]
  [Breakdown of what it does]
  [Closing call to action with system/efficiency payoff]
  ```

### @cli_voice
- Use: Button labels, confirmations, alert banners  
- Format:
  ```
  [Short verb or terminal message]
  [Optional: system status or result]
  ```

### @referential_confident
- Use: Welcome messages, onboarding, partnership emails  
- Format:
  ```
  [Narrative or sci-fi framing intro]
  [Mission-ready confirmation]
  [Optional: Next steps with confidence]
  ```

### @no_fluff
- Use: Report headlines, feature comparisons, client briefings  
- Format:
  ```
  [Problem → Impact statement]
  [Solution offered directly]
  [Quantifiable gain if available]
  ```