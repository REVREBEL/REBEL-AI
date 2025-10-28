# Database: Structural & Definitions Guide
# `persona_revrebel`

This document serves as the foundational architecture and operational guide for building and maintaining a vector database that encapsulates a brand's entire identity—from strategic core to tactical application. The goal is to enable AI-powered asset generation that is always on-brand.

**Purpose:**

This index is dedicated to storing REVREBEL's brand personality traits, voice scaffolds, tone examples, and writing techniques. It enables modular injection of stylistic guidance into GPT responses — separate from factual knowledge or recommendation content.

**Use Cases:** 

Style-aware GPT completions - Personality preloading in multi-step prompt chains - Experimental testing of tone or voice shifts (e.g., witty vs dry) - Modular swap-ins for future persona updates (persona_version: v2)

<br>
---
<br>

## CLASSIFICATION OVERVIEW
<br>

Before defining modules, the system needs a universal way to determine how incoming content should be classified — whether it belongs as a Canonical Principle, a Matrix rule, or a standalone asset. This logic applies across all modules.

<br>

### High-Level Rules

* **Canonical Principle** → Use when content describes strategy, philosophy, or conceptual tone (the *why* and *how* behind the brand's behavior).
* **Matrix Entry** → Use when content contains actionable guidance, lists, rules, or contrasting examples (e.g., Do/Don't, If/Then logic).
* **Dual Classification** → When both narrative guidance and rules coexist, create both a Canonical record (for context) and Matrix entries (for executional application).

<br>

### Application Across Modules

| Example                           | Module                         | Classification                                                   |
| --------------------------------- | ------------------------------ | ---------------------------------------------------------------- |
| Brand Emulators (Example 4)       | Brand Comparison & Inspiration | Canonical (conceptual) + optional Matrix for reference metaphors |
| Writing Do's & Don'ts (Example 7) | Brand Voice & Style            | Matrix (rules) + Canonical overview of writing intent            |
| Voice Principles (Example 6)      | Brand Voice & Style            | Canonical (tone philosophy) + optional Matrix (behavioral rules) |
| Psychographics (Example 5)        | Audience Insight               | Canonical (motivational narrative)                               |
| Brand Personality (Example 8)     | Brand Core                     | Canonical (descriptive personality narrative)                    |

<br>

## Appling the Logic

When processing brand input related to voice, tone, or communication rules, the system first determines whether the content should be stored as a **Canonical Principle**, a **Voice Matrix**, or both.

<br>

**Initial Check Logic:**

* If the input contains **strategic or philosophical explanations** about *how the brand communicates* (e.g., tone, intent, emotional character) → classify as **Canonical Principle**.
* If the input contains **actionable instructions, do/don't phrasing, or behavior-based rules** → classify as **Voice Matrix**.
* If both exist → store **both record types**: a narrative *principle* and modular *matrix* entries for enforcement.

<br>

## Decision Breakdown & Insert Examples

### Scenario A: Input only contains Canonical Principle-style content

**Example:** "Our brand voice balances confident authority with human approachability..."

**Action:** Create one vector entry under **Brand Voice & Style → Voice Principles.**

```json
{
  "id": "voice-authority-approachability",
  "text": "Our brand voice balances confident authority with human approachability. We communicate with precision, using direct and jargon-free language to make complex ideas simple. Messaging is structured, research-informed, and focused on education — all while maintaining warmth through conversational tone, empathy, and subtle humor. This duality positions us as a trusted expert who helps businesses grow without intimidation.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Principles",
    "use_case": "Tone calibration",
    "tone": "Confident, Approachable, Educational",
    "audience": "Writers, Marketers, Designers, AI Systems",
    "language": "English",
    "channel": "All",
    "funnel_stage": "Awareness → Retention"
  }
}
```

<br>

#### Scenario B: Input contains actionable rules or both narrative + behavior guidance

**Example:** "Do: Draw from recent data. Don't: Use unverified statements."

**Action:** Create multiple atomic entries under **Brand Voice & Style → Voice Matrix.** Each captures one attribute and its do/don't behavior.

```json
{
  "id": "vm-transparent-trustworthy-do",
  "text": "Transparent & Trustworthy — Do: Provide sources and data; avoid unsubstantiated claims.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Matrix",
    "attribute": "Transparent & Trustworthy",
    "rule_type": "do",
    "severity": "must",
    "example_good": "Source: STR Weekly Report, Sept 2025.",
    "example_bad": "Everyone knows this works.",
    "channel": "All",
    "weight": 0.85,
    "language": "English"
  }
}
```

```json
{
  "id": "vm-transparent-trustworthy-dont",
  "text": "Transparent & Trustworthy — Don't: Make unsubstantiated or vague claims.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Matrix",
    "attribute": "Transparent & Trustworthy",
    "rule_type": "dont",
    "severity": "must",
    "example_good": "Provide citations for any performance metrics.",
    "example_bad": "We guarantee immediate results!",
    "channel": "All",
    "weight": 0.85,
    "language": "English"
  }
}
```
<br>

### Why This Is Useful / Ideal

This two-tiered method allows the vector database to store **context-rich strategy** and **atomic executional rules** side by side. It gives AI systems both **philosophical guidance** and **practical enforcement parameters**.

#### Benefits:

* **Precision + Context:** Narrative entries train AI to understand tone; matrix rules provide exact language constraints.
* **Granular Retrieval:** Enables querying tone attributes, rule types, or severity to tailor brand content.
* **AI Alignment:** Models can use Canonical Principles for context-building, and Voice Matrix rules for copy validation or generation.
* **Scalable Governance:** Allows future automation (linting, QA, tone scoring) without losing the brand's creative nuance.
* **Cross-Functional Utility:** Useful for brand teams, copywriters, and AI systems alike — linking strategy to real-world application.
* **Consistency:** Shared decision logic ensures uniform data modeling across modules.
* **Efficiency:** Prevents duplication and clarifies which format to use during vector insertion.
* **Scalability:** Supports automated ingestion workflows by predefining rule triggers (e.g., detect 'Do/Don't' → Matrix).
* **Retrieval Precision:** Enables filtered queries that combine context (Canonical) with application (Matrix) for better AI output.

#### Later Use:

* **During Prompting:** Fetch *Voice Principles* + *Tone by Channel* + *Voice Matrix* (must + should rules).
* **During Validation:** Compare generated text against *don't* rules for quality assurance.
* **During Training:** Use Canonical Principles as embedding context to maintain emotional fidelity.

<br>
---
<br>

## STRUCTURE OVERVIEW

The brand vector database is composed of **7 key modules**, each containing multiple semantic submodules. Each element within these modules is stored as a vectorized object with metadata for filtering and context-based retrieval.

<br>

### CHANNEL-SPECIFIC TONE MANAGEMENT

To handle tone differences across channels such as social (more lively) versus blog (more instructional), create a submodule under **Brand Voice & Style** named *Tone by Channel*. Each channel entry should include:

* Channel-specific tone descriptors (e.g., lively, conversational, instructional, authoritative).
* Example phrasing and sentence structure guidance.
* Associated metadata fields such as:

  * `module`: Brand Voice & Style
  * `submodule`: Tone by Channel
  * `channel`: Social, Blog, Email, etc.
  * `tone`: Descriptive tone words per channel (e.g., playful, professional)
    This approach maintains brand consistency while allowing nuanced tone and phrasing adaptations per platform.

<br>

### EXPANDED: Tone-Channel Matrix

For granular control over platform-specific voice, expand the Tone by Channel submodule with detailed constraints:

```json
{
  "id": "tone-linkedin-professional",
  "text": "LinkedIn tone balances professional authority with approachability. Use data-driven insights, industry terminology, and thought leadership framing. Maintain conversational professionalism without corporate stiffness.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Tone by Channel",
    "channel": "social",
    "platform": "linkedin",
    "tone": "professional-approachable",
    "constraints": {
      "max_length": 3000,
      "emoji_allowed": false,
      "hashtag_style": "minimal (1-3 strategic tags)",
      "sentence_length": "medium (15-25 words)",
      "formality": "business-casual"
    },
    "example_phrases": [
      "Here's what the data tells us:",
      "Three insights worth considering:",
      "Industry leaders are shifting toward..."
    ],
    "avoid_phrases": [
      "Hey folks!",
      "This is AMAZING!!! 🚀",
      "You won't believe..."
    ],
    "persona_version": "v2.0",
    "status": "active"
  }
}
```

**Recommended Channels to Define:**
- LinkedIn (professional)
- Twitter/X (punchy, conversational)
- Instagram (visual, aspirational)
- Blog (instructional, comprehensive)
- Email (direct, value-driven)
- Product UI (helpful, concise)
- Documentation (clear, technical)

<br>
---
<br>

## MODULE 1: Brand Core
**Definition**: Captures the strategic essence and foundational beliefs of the brand.

| Submodule | Definition | Example Use Cases | Placement Rules |
|----------|-------------|--------------------|-----------------|
| Mission & Vision | The brand's purpose and long-term aspiration | AI generates 'About Us' page or founder pitch | Use when request includes "why we exist" or "what we aim to become" |
| Brand Values | Ethical, cultural, or strategic principles | Tone/voice alignment, internal culture guides | Insert if prompt includes "principles" or "values-driven" keywords |
| Brand Purpose | The brand's reason for being in the market | Campaign messaging, brand storytelling | Use for top-level narratives or strategic intros |
| Brand Personality | Traits that describe brand as a human | AI content voice, tone simulation | Insert if user mentions "brand feels like..." or lists traits (e.g., bold, smart) |
| Brand Archetype | Narrative framework that defines brand's role | Messaging tone, emotional hook writing | Include when archetype words (Hero, Sage, etc.) are used |

<br>
<br>

## MODULE 2: Audience Insight
**Definition**: Describes who the brand is talking to and how to emotionally resonate with them.

| Submodule | Definition | Example Use Cases | Placement Rules |
|----------|-------------|--------------------|-----------------|
| Demographics | Age, gender, income, role, region | Persona building, paid ad targeting | Use for structured audience info inputs |
| Psychographics | Values, beliefs, motivators, attitudes | Emotional messaging, CTA tuning | Insert when prompt includes psychological or emotional descriptors |
| Buyer Personas | Semi-fictional audience segments | Content strategy, product positioning | Place if prompt includes defined personas by name, title, or scenario |
| Audience Tone Preferences | How the audience prefers to be spoken to | Copywriting style, UX writing | Insert if style matching to audience is required (e.g., technical vs casual) |

<br>
<br>

## MODULE 3: Brand Messaging System
**Definition**: The structured language and communication strategy of the brand.

| Submodule | Definition | Example Use Cases | Placement Rules |
|----------|-------------|--------------------|-----------------|
| Value Propositions | Benefits that differentiate brand/products | Website headlines, sales decks | Insert if user asks "Why choose us?" or similar |
| Brand Pillars | Strategic themes supporting brand position | Thought leadership, campaign planning | Use if prompt includes "main messages" or "key ideas" |
| Taglines & Slogans | Short-form phrases encapsulating the brand | Logo lockups, ads, product launches | Place if short, punchy lines are mentioned |
| Messaging by Funnel Stage | Messaging tailored to buyer's journey | Lifecycle email copy, PPC ads | Insert when content is tied to funnel stages |
| Signature Phrases & Keywords | Repeated brand-specific language | SEO, branded copy templates | Include if prompt asks for unique brand language or phrases |

<br>
<br>

## MODULE 4: Brand Voice & Style
**Definition**: Rules and personality of the brand's written expression.

| Submodule | Definition | Example Use Cases | Placement Rules |
|----------|-------------|--------------------|-----------------|
| Voice Principles | Foundational voice characteristics | Brand guideline creation, tone review | Insert when defining brand's personality in language |
| Grammar Rules | Punctuation, spelling, formatting preferences | UX writing, legal reviews | Include if prompt involves linguistic correctness |
| Sentence Structures | Rhythm, length, and tone style | Blog articles, product pages | Use when prompt asks for tone clarity or pacing |
| Tone Variations | Voice shifting across contexts/channels | Multichannel campaign content | Insert if multiple brand contexts are involved |
| Writing Do's and Don'ts | Prescriptive copy rules | Onboarding content, agency handoffs | Include when prompt refers to guidelines or rules |
| Tone by Channel |  Social, Blog, Email, etc. | Descriptive tone words per channel (e.g., playful, professional) | Include when prompt refers to guidelines or rules |

<br>
<br>

### EXPANDED: Voice Matrix Severity Levels

The Voice Matrix uses severity levels to indicate the importance of compliance with each rule. This creates a spectrum from absolute requirements to stylistic preferences.

**Severity Taxonomy:**

| Severity | Definition | Usage | Violation Impact |
|----------|------------|-------|------------------|
| **must** | Non-negotiable requirements | Legal compliance, brand safety, factual accuracy | Hard failure, blocks publication |
| **should** | Strong recommendations | Core voice attributes, key differentiators | Warning flag, requires review |
| **prefer** | Stylistic preferences | Sentence structure, word choice nuances | Suggestion only, no blocking |
| **avoid** | Discouraged but not prohibited | Overused phrases, weak language | Guidance, coach alternative |
| **never** | Absolute prohibitions | Off-brand language, competitor mentions | Hard failure, blocks publication |

**Implementation Example:**

```json
{
  "id": "vm-data-accuracy-must",
  "text": "Data Accuracy — Must: Verify all statistics and cite sources before publication.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Matrix",
    "attribute": "Data Accuracy",
    "rule_type": "do",
    "severity": "must",
    "violation_action": "block_publication",
    "example_good": "According to STR's Q3 2025 report, ADR increased 3.2%.",
    "example_bad": "ADR went up significantly.",
    "weight": 1.0,
    "channel": "All"
  }
}
```

```json
{
  "id": "vm-sentence-brevity-prefer",
  "text": "Sentence Brevity — Prefer: Keep sentences under 25 words when possible.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Matrix",
    "attribute": "Sentence Brevity",
    "rule_type": "do",
    "severity": "prefer",
    "violation_action": "suggest_edit",
    "example_good": "Our platform optimizes pricing in real-time.",
    "example_bad": "Our sophisticated algorithmic platform leverages machine learning to dynamically optimize pricing strategies in real-time based on market conditions.",
    "weight": 0.4,
    "channel": "All"
  }
}
```

**Severity-Based Querying:**

```typescript
// Fetch only critical rules for validation
const criticalRules = await env.PERSONA.query(contextEmbedding, {
  filter: { 
    submodule: "Voice Matrix",
    severity: ["must", "never"]
  }
});

// Fetch all guidance for training
const allGuidance = await env.PERSONA.query(contextEmbedding, {
  filter: { submodule: "Voice Matrix" }
});
```

<br>

## MODULE 5: Visual Identity System
**Definition**: Visual rules and elements that express the brand.

| Submodule | Definition | Example Use Cases | Placement Rules |
|----------|-------------|--------------------|-----------------|
| Logos | Approved logo variations | Print, digital, packaging | Use if logo files or spacing rules are referenced |
| Brand Colors | Brand color palette with codes | UI/UX design, print assets | Place if colors or palette mentioned explicitly |
| Typography | Fonts used and their usage rules | Style guides, website design | Insert if fonts or typesetting guidelines are discussed |
| Image Style | Direction for photos, graphics, illustrations | AI-generated visuals, moodboards | Use when discussing image direction or aesthetic |
| Design Do's & Don'ts | Visual rules of what to avoid or use | Brand audits, new campaign QA | Include for consistency checks or visual guardrails |
| Moodboards | Visual style boards for inspiration | Art direction, concept development | Insert if user needs visual inspiration aligned with brand |

<br>
<br>

## MODULE 6: Brand Comparison & Inspiration
**Definition**: Metaphorical and competitive framing for stylistic alignment.

| Submodule | Definition | Example Use Cases | Placement Rules |
|----------|-------------|--------------------|-----------------|
| Brand Emulators | "If the brand were…" comparisons | Creative exploration, persona shaping | Use if user makes brand analogies (e.g., "We're the Tesla of...") |
| Analogies & Metaphors | Figurative descriptions of brand essence | Narrative crafting, pitch decks | Insert if prompt contains metaphorical framing |
| Tone Benchmarks | Brands we admire or align with | Competitive brand tone analysis | Use if brand tone is compared to others |
| Differentiators | How the brand stands out vs competitors | Messaging, pitch decks | Include if prompt asks for what makes us different |

<br>
<br>


## MODULE 7: Tactical Brand Usage
**Definition**: Application-specific expressions of the brand.

| Submodule | Definition | Example Use Cases | Placement Rules |
|----------|-------------|--------------------|-----------------|
| Use Cases | Where/why brand elements are applied | Channel strategy, training manuals | Insert if user provides a goal or format (e.g., email, tweet) |
| Touchpoint Guidance | Brand behavior across platforms | Omnichannel planning, social media kits | Use for cross-channel campaign prompts |
| Common Mistakes | Examples of off-brand behavior | Internal QA, brand training | Insert if user asks "what to avoid" or shows inconsistency |
| Template Outputs | Pre-approved example content | Training GPTs, new hire onboarding | Use when referencing real past campaigns or templates |

<br>
---
<br>

## DECISION TREE OVERVIEW (SIMPLIFIED)

```
[User Prompt Received]
        |
        +-- Does it describe WHO we are? ---------+--> Brand Core
        |
        +-- Does it describe WHO we serve? -------+--> Audience Insight
        |
        +-- Is it about WHAT we say or HOW? ------+--> Brand Messaging System
        |
        +-- Does it describe HOW we speak? -------+--> Brand Voice & Style
        |
        +-- Is it about what we LOOK like? -------+--> Visual Identity System
        |
        +-- Does it compare/position us? ---------+--> Brand Comparison & Inspiration
        |
        +-- Is it application-specific? ----------+--> Tactical Brand Usage
```

<br>
---
<br>

## Status Field Definition

Include a `status` field in all metadata objects.

```json
"status": "active" | "deprecated" | "draft"
```

| Status         | Definition                                                | Typical Use                                   |
| -------------- | --------------------------------------------------------- | --------------------------------------------- |
| **active**     | In current use; approved for all production applications. | Live brand references, canonical entries.     |
| **deprecated** | Retained for historical context but no longer in use.     | Outdated tone, visuals, or strategy examples. |
| **draft**      | Under review or pending approval.                         | New entries not yet validated.                |

<br>

### Active Record

```json
{
  "id": "voice-authority-approachability-v2",
  "text": "Our brand voice balances confident authority with human approachability...",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Principles",
    "status": "active",
    "version": "2.0",
    "language": "en"
  }
}
```
<br>

### Deprecated Record

```json
{
  "id": "voice-authority-approachability-v1",
  "text": "Legacy tone definition prior to 2025-Q3 update.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Principles",
    "status": "deprecated",
    "version": "1.0",
    "deprecated_reason": "Superseded by 2025 tone calibration update",
    "language": "en"
  }
}
```

<br>
---
<br>

## Versioning Guidance

REVREBEL uses `persona_version` to track voice iterations. We recommend using a simplified format like `v1.0`, `v2.0`, etc., unless a third digit is needed for hotfixes or microadjustments (e.g., `v1.0.1`).

| Version Type | When to Use                                           | Example                       |
| ------------ | ----------------------------------------------------- | ----------------------------- |
| `v1.0`       | Initial stable release of persona style               | Foundational voice definition |
| `v2.0`       | Major shift in tone, rewritten guidance, or a rebrand | Voice overhaul or pivot       |
| `v2.1`       | Minor tweaks or modular expansion                     | Added new scaffold type       |
| `v1.0.1`     | Patch or correction to existing version               | Typo fix or metadata update   |

<br>

**Rules for Updating:**

* Only one `persona_version` should be marked `active` at a time.
* When a new version is made active, previous version should be set to `deprecated`.
* A `version bump` should be logged when voice direction, formatting style, or rules meaningfully shift.
* Use consistent author metadata to track who made the update.

> ⚠️ All GPT insertions and queries should check for the latest `status=active` version unless instructed otherwise.

<br>
---
<br>

## ADVANCED FEATURES

### 1. Cross-Database Relationships

While the persona database (`persona:revrebel`) remains separate from knowledge/asset databases, establishing cross-references enables richer context and example-driven guidance.

**Implementation:**

```json
{
  "id": "voice-witty-irreverent",
  "text": "Witty, irreverent tone with pop culture references and dry humor. Think Aesop meets ThinkGeek.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Principles",
    "related_examples": [
      "doc:campaign-retro-arcade-launch",
      "doc:blog-post-revenue-hacks-2025",
      "asset:photo-retro-tech-moodboard"
    ],
    "use_case_refs": [
      "prod-doc-search:social-media-guide",
      "prod-asset-embeddings:logo-primary-001"
    ],
    "persona_version": "v2.0",
    "status": "active"
  }
}
```

**Query Pattern:**

```typescript
// Fetch voice principle
const voicePrinciple = await env.PERSONA.query(embedding, {
  filter: { submodule: "Voice Principles" },
  topK: 1
});

// Fetch related examples from other databases
const relatedDocs = await env.PROD_DOCS.getByIds(
  voicePrinciple.metadata.related_examples
    .filter(ref => ref.startsWith('doc:'))
    .map(ref => ref.replace('doc:', ''))
);

const relatedAssets = await env.PROD_ASSETS.getByIds(
  voicePrinciple.metadata.related_examples
    .filter(ref => ref.startsWith('asset:'))
    .map(ref => ref.replace('asset:', ''))
);
```

**Benefits:**
- "Show me examples of this tone in practice"
- "What docs align with this voice principle?"
- Links abstract guidance to concrete implementations

<br>

### 2. Temporal Context Awareness

Track when persona elements were valid and when they evolved. This enables historical queries and gradual transitions.

**Schema Addition:**

```json
{
  "id": "voice-authority-approachability-v2",
  "text": "Our brand voice balances confident authority with human approachability...",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Principles",
    "persona_version": "v2.0",
    "valid_from": "2025-01-01T00:00:00Z",
    "valid_until": null,
    "supersedes": ["voice-authority-approachability-v1"],
    "superseded_by": null,
    "change_log": "Shifted from quirky humor to dry wit; reduced exclamation point usage",
    "change_author": "brand-team",
    "change_reason": "Brand maturity; targeting enterprise clients",
    "status": "active"
  }
}
```

**Use Cases:**

1. **Historical Analysis:**
   ```typescript
   // "How would v1.0 voice have written this?"
   const historicalVoice = await env.PERSONA.query(embedding, {
     filter: { 
       persona_version: "v1.0",
       valid_from: { $lte: "2024-12-31" }
     }
   });
   ```

2. **Transition Periods:**
   ```typescript
   // During brand evolution, blend old and new
   const currentVoice = await env.PERSONA.query(embedding, {
     filter: { status: "active", persona_version: "v2.0" }
   });
   
   const legacyVoice = await env.PERSONA.query(embedding, {
     filter: { status: "deprecated", persona_version: "v1.0" }
   });
   
   // Blend for gradual transition (70% new, 30% old)
   const transitionGuidance = blendVoices(currentVoice, legacyVoice, 0.7);
   ```

3. **Audit Trails:**
   - "When did we stop using exclamation points?"
   - "What changed between v1.5 and v2.0?"

<br>

### 3. Confidence Scoring

Add confidence metadata to indicate certainty about persona guidance. Useful for flagging experimental or contested elements.

**Schema Addition:**

```json
{
  "id": "vm-emoji-usage-experimental",
  "text": "Emoji Usage — Avoid: Minimize emoji use in professional contexts; test sparingly in social.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Matrix",
    "attribute": "Emoji Usage",
    "rule_type": "avoid",
    "severity": "prefer",
    "confidence_score": 0.65,
    "confidence_reason": "Limited testing; mixed feedback from audience",
    "verified_by": "design-team",
    "last_verified": "2025-10-15",
    "verification_method": "A/B test (n=500)",
    "dispute_count": 2,
    "status": "active"
  }
}
```

**Confidence Levels:**

| Score Range | Interpretation | Usage |
|-------------|----------------|-------|
| **0.95-1.0** | Highly confident | Core brand attributes, validated principles |
| **0.80-0.94** | Confident | Established guidelines with evidence |
| **0.65-0.79** | Moderate confidence | Recent additions, limited validation |
| **0.50-0.64** | Low confidence | Experimental, contested, or outdated |
| **< 0.50** | Uncertain | Flag for review or deprecation |

**Query Pattern:**

```typescript
// Fetch only high-confidence rules for critical content
const reliableGuidance = await env.PERSONA.query(embedding, {
  filter: { 
    submodule: "Voice Matrix",
    confidence_score: { $gte: 0.80 }
  }
});

// Flag low-confidence areas for human review
const uncertainGuidance = await env.PERSONA.query(embedding, {
  filter: { 
    confidence_score: { $lt: 0.65 }
  }
});
```

**Benefits:**
- Flags potentially outdated or contested information
- Enables gradual confidence building through validation
- Prioritizes high-confidence guidance for production use

<br>

### 4. Contextual Personas (Sub-Personas)

While the main persona (`revrebel_core`) defines overall brand voice, contextual personas handle specific use cases that require different tones.

**Use Cases:**

| Context | Persona ID | Tone Shift | When to Use |
|---------|------------|------------|-------------|
| **Founder Voice** | `revrebel_founder` | Visionary, bold, aspirational | Keynotes, manifestos, origin stories |
| **Customer Support** | `revrebel_support` | Helpful, patient, empathetic | Help docs, support tickets, onboarding |
| **Technical Docs** | `revrebel_technical` | Precise, clear, instructional | API docs, integration guides, tutorials |
| **Sales** | `revrebel_sales` | Confident, value-focused, consultative | Pitch decks, proposals, discovery calls |
| **Social Media** | `revrebel_social` | Casual, witty, conversational | Twitter, LinkedIn, Instagram |

**Implementation:**

```json
{
  "id": "persona-founder-visionary",
  "text": "Founder voice is bold and visionary. Use first-person perspective, share origin stories, and paint aspirational futures. Reference the 'why' behind decisions. Think Steve Jobs keynotes meets manifesto energy.",
  "metadata": {
    "persona_id": "revrebel_founder",
    "persona_version": "v2.0",
    "tone": "visionary, bold, inspirational",
    "use_case": "keynotes, founder statements, origin stories",
    "first_person": true,
    "example_phrases": [
      "When we started REVREBEL, we saw a broken system...",
      "The future of revenue management isn't about...",
      "We believe every hotel deserves..."
    ],
    "avoid_phrases": [
      "Our product offers...",
      "According to our data...",
      "Please contact support..."
    ],
    "inherits_from": "revrebel_core",
    "overrides": ["formality", "use_of_I_we"],
    "status": "active"
  }
}
```

```json
{
  "id": "persona-support-helpful",
  "text": "Support voice is patient, helpful, and empathetic. Use second-person perspective, break down complex steps, and validate user frustrations. Think helpful friend meets technical expert.",
  "metadata": {
    "persona_id": "revrebel_support",
    "persona_version": "v2.0",
    "tone": "helpful, patient, empathetic",
    "use_case": "help docs, support tickets, troubleshooting",
    "formality": "casual-professional",
    "example_phrases": [
      "Let's walk through this together...",
      "I understand that can be frustrating. Here's what to do...",
      "Great question! Here's how that works..."
    ],
    "avoid_phrases": [
      "This is obvious...",
      "You should have...",
      "RTFM"
    ],
    "inherits_from": "revrebel_core",
    "overrides": ["humor_level", "technical_depth"],
    "status": "active"
  }
}
```

**Query Pattern:**

```typescript
// Fetch appropriate persona based on context
async function getContextualPersona(context: string, env: Env) {
  const personaMap = {
    'keynote': 'revrebel_founder',
    'support': 'revrebel_support',
    'technical': 'revrebel_technical',
    'sales': 'revrebel_sales',
    'social': 'revrebel_social',
    'default': 'revrebel_core'
  };
  
  const personaId = personaMap[context] || personaMap.default;
  
  return await env.PERSONA.query(embedding, {
    filter: { 
      persona_id: personaId,
      status: "active"
    }
  });
}
```

**Benefits:**
- Maintains brand consistency while allowing contextual flexibility
- Prevents support docs from sounding like sales pitches
- Enables appropriate tone for each customer journey stage

<br>

### 5. A/B Testing Framework

Track experimental voice variations to enable data-driven persona evolution.

**Schema Addition:**

```json
{
  "id": "voice-witty-increased-test",
  "text": "EXPERIMENTAL: Increased wit and pop culture references. More sentence fragments, bolder metaphors, heavier use of retro-tech analogies.",
  "metadata": {
    "persona_version": "v2.1-experimental",
    "experiment_id": "tone-test-001",
    "experiment_name": "Increased Wit Variant",
    "hypothesis": "More wit will increase engagement on social media",
    "variant": "witty-increased",
    "control": "v2.0",
    "test_start_date": "2025-11-01",
    "test_end_date": "2025-11-30",
    "sample_size_target": 1000,
    "metrics": {
      "engagement_rate": null,
      "conversion_rate": null,
      "sentiment_score": null,
      "brand_recall": null
    },
    "status": "draft",
    "approved_channels": ["twitter", "linkedin"],
    "restricted_channels": ["support", "legal"]
  }
}
```

**Workflow:**

1. **Create Experimental Variant:**
   ```typescript
   await env.PERSONA.insert({
     id: `voice-${experimentId}`,
     values: experimentEmbedding,
     metadata: {
       persona_version: "v2.1-experimental",
       experiment_id: experimentId,
       status: "draft"
     }
   });
   ```

2. **Run A/B Test:**
   ```typescript
   // Randomly assign users to control or variant
   const persona = Math.random() < 0.5 
     ? await getPersona("v2.0") // Control
     : await getPersona("v2.1-experimental"); // Variant
   ```

3. **Collect Metrics:**
   ```typescript
   await logMetric(experimentId, {
     engagement_rate: 0.042,
     conversion_rate: 0.018,
     sentiment_score: 0.72
   });
   ```

4. **Promote or Deprecate:**
   ```typescript
   if (variantPerformance > controlPerformance) {
     await promoteToActive("v2.1-experimental");
     await deprecateVersion("v2.0");
   }
   ```

**Benefits:**
- Data-driven persona evolution
- Reduces risk of brand voice changes
- Enables gradual, validated improvements

<br>

### 6. Compliance & Legal Guardrails

Flag content that requires legal review or has regulatory implications.

**Schema Addition:**

```json
{
  "id": "vm-claims-legal-review",
  "text": "Marketing Claims — Must: Any performance guarantees, ROI promises, or competitive comparisons require legal review before publication.",
  "metadata": {
    "module": "Brand Voice & Style",
    "submodule": "Voice Matrix",
    "attribute": "Marketing Claims",
    "rule_type": "dont",
    "severity": "must",
    "legal_reviewed": true,
    "legal_reviewer": "legal-team@revrebel.com",
    "last_legal_review": "2025-10-01",
    "compliance_tags": ["FTC", "advertising-standards"],
    "restricted_terms": [
      "guaranteed results",
      "always increase revenue",
      "never fail",
      "best in industry"
    ],
    "requires_disclaimer": true,
    "disclaimer_text": "Results may vary. Past performance does not guarantee future results.",
    "violation_action": "block_publication",
    "status": "active"
  }
}
```

**Restricted Term Detection:**

```typescript
async function checkCompliance(content: string, env: Env) {
  // Fetch compliance rules
  const complianceRules = await env.PERSONA.query(contentEmbedding, {
    filter: { 
      compliance_tags: { $exists: true },
      severity: "must"
    }
  });
  
  // Check for restricted terms
  const violations = [];
  for (const rule of complianceRules.matches) {
    const restrictedTerms = rule.metadata.restricted_terms || [];
    for (const term of restrictedTerms) {
      if (content.toLowerCase().includes(term.toLowerCase())) {
        violations.push({
          rule_id: rule.id,
          term: term,
          action: rule.metadata.violation_action,
          requires_review: rule.metadata.legal_reviewed
        });
      }
    }
  }
  
  return violations;
}
```

**Compliance Categories:**

| Category | Tags | Severity | Review Required |
|----------|------|----------|-----------------|
| **Marketing Claims** | FTC, advertising-standards | must | Yes |
| **Data Privacy** | GDPR, CCPA, privacy | must | Yes |
| **Financial Advice** | SEC, financial-regulations | must | Yes |
| **Medical/Health** | FDA, health-claims | must | Yes |
| **Accessibility** | ADA, WCAG | should | No |

**Benefits:**
- Prevents legal liability
- Automates compliance checking
- Flags content for legal review before publication

<br>
---
<br>

## MAINTENANCE WORKFLOW

Regular maintenance ensures the persona database remains accurate, consistent, and performant.

### Weekly Tasks

**1. Status Audit**
```bash
# Check for entries still marked as "draft" after 30 days
wrangler vectorize query persona:revrebel \
  --filter '{"status":"draft","created_ym":{"$lte":"2025-09"}}' \
  --topK 100
```

**2. Confidence Score Review**
```typescript
// Flag low-confidence entries for validation
const lowConfidence = await env.PERSONA.query(embedding, {
  filter: { 
    confidence_score: { $lt: 0.65 }
  }
});

// Schedule for review
for (const entry of lowConfidence.matches) {
  await scheduleReview(entry.id, "confidence_validation");
}
```

**3. Cross-Reference Validation**
```typescript
// Check that related_examples still exist
const entriesWithRefs = await getAllEntriesWithReferences();
for (const entry of entriesWithRefs) {
  const brokenRefs = await validateReferences(entry.metadata.related_examples);
  if (brokenRefs.length > 0) {
    await flagForUpdate(entry.id, { broken_refs: brokenRefs });
  }
}
```

### Monthly Tasks

**1. Version Cleanup**
- Review deprecated entries older than 6 months
- Archive to separate cold storage if no longer referenced
- Update documentation with version change log

**2. A/B Test Analysis**
```typescript
// Analyze ongoing experiments
const activeExperiments = await env.PERSONA.query(embedding, {
  filter: { 
    experiment_id: { $exists: true },
    status: "draft"
  }
});

for (const experiment of activeExperiments.matches) {
  const metrics = await getExperimentMetrics(experiment.metadata.experiment_id);
  if (metrics.significance > 0.95) {
    await promoteOrDeprecate(experiment, metrics);
  }
}
```

**3. Compliance Review**
```typescript
// Re-validate legal reviewed content
const legalContent = await env.PERSONA.query(embedding, {
  filter: { 
    legal_reviewed: true,
    last_legal_review: { $lt: sixMonthsAgo }
  }
});

await notifyLegalTeam(legalContent.matches);
```

### Quarterly Tasks

**1. Persona Version Audit**
- Evaluate if major version bump is needed
- Gather feedback from content teams
- Run sentiment analysis on content generated with current persona
- Plan transition strategy if update warranted

**2. Contextual Persona Review**
- Validate sub-personas are still appropriate
- Check for new contexts requiring dedicated personas
- Ensure inheritance relationships are correct

**3. Performance Optimization**
```bash
# Analyze query patterns
wrangler vectorize stats persona:revrebel

# Check for:
# - Most queried entries (cache candidates)
# - Rarely queried entries (deprecation candidates)
# - Query latency trends
```

### Automation Recommendations

```typescript
// Automated health check script
async function personaHealthCheck(env: Env) {
  const checks = {
    total_entries: 0,
    active_entries: 0,
    deprecated_entries: 0,
    draft_entries: 0,
    low_confidence_entries: 0,
    broken_references: 0,
    stale_legal_reviews: 0,
    active_experiments: 0
  };
  
  // Run all checks
  checks.total_entries = await countAllEntries();
  checks.active_entries = await countByStatus("active");
  checks.deprecated_entries = await countByStatus("deprecated");
  checks.draft_entries = await countByStatus("draft");
  checks.low_confidence_entries = await countByConfidence({ $lt: 0.65 });
  checks.broken_references = await validateAllReferences();
  checks.stale_legal_reviews = await countStaleLegalReviews(6); // months
  checks.active_experiments = await countActiveExperiments();
  
  // Alert if thresholds exceeded
  if (checks.low_confidence_entries > 10) {
    await alertTeam("High number of low-confidence entries");
  }
  
  if (checks.stale_legal_reviews > 0) {
    await alertLegal("Compliance content needs review");
  }
  
  return checks;
}
```

<br>
---
<br>

## METADATA SCHEMA REFERENCE

### Core Persona Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `persona_id` | string | Yes | Unique persona identifier (e.g., `revrebel_core`, `revrebel_founder`) |
| `persona_version` | string | Yes | Semantic version (e.g., `v2.0`, `v2.1-experimental`) |
| `module` | string | Yes | Top-level module (Brand Core, Brand Voice & Style, etc.) |
| `submodule` | string | Yes | Specific submodule within module |
| `status` | string | Yes | `active`, `deprecated`, or `draft` |
| `tone` | string | No | Tone descriptors (e.g., `witty, confident, rebellious`) |
| `use_case` | string | No | Primary application context |
| `language` | string | Yes | Content language (default: `en`) |
| `created_ym` | string | Yes | Creation date (YYYY-MM format) |
| `author` | string | Yes | Creator identifier |

### Extended Fields (Optional)

| Field | Type | Description |
|-------|------|-------------|
| `channel` | string | Specific channel (LinkedIn, Blog, Email, etc.) |
| `platform` | string | Sub-platform (e.g., `linkedin` under `social`) |
| `audience` | string | Target audience |
| `funnel_stage` | string | Buyer journey stage |
| `severity` | string | Rule importance (`must`, `should`, `prefer`, `avoid`, `never`) |
| `confidence_score` | number | Certainty level (0.0-1.0) |
| `weight` | number | Importance weighting (0.0-1.0) |

### Relationship Fields

| Field | Type | Description |
|-------|------|-------------|
| `related_examples` | array | Cross-references to other databases |
| `use_case_refs` | array | Related use case documents |
| `inherits_from` | string | Parent persona for sub-personas |
| `overrides` | array | Attributes overridden from parent |
| `supersedes` | array | Previous version IDs |
| `superseded_by` | string | Newer version ID |

### Temporal Fields

| Field | Type | Description |
|-------|------|-------------|
| `valid_from` | string | ISO timestamp when record became active |
| `valid_until` | string | ISO timestamp when record deprecated (null if active) |
| `last_updated` | string | ISO timestamp of last modification |
| `last_verified` | string | ISO timestamp of last review |

### Compliance Fields

| Field | Type | Description |
|-------|------|-------------|
| `legal_reviewed` | boolean | Has legal team reviewed |
| `legal_reviewer` | string | Legal team member email |
| `last_legal_review` | string | ISO timestamp of legal review |
| `compliance_tags` | array | Regulatory categories (FTC, GDPR, etc.) |
| `restricted_terms` | array | Terms that trigger violations |
| `requires_disclaimer` | boolean | Needs legal disclaimer |

### Experimental Fields

| Field | Type | Description |
|-------|------|-------------|
| `experiment_id` | string | Unique experiment identifier |
| `experiment_name` | string | Human-readable experiment name |
| `variant` | string | Variant identifier |
| `control` | string | Control version identifier |
| `test_start_date` | string | ISO timestamp |
| `test_end_date` | string | ISO timestamp |
| `metrics` | object | Performance metrics (engagement, conversion, etc.) |

<br>
---
<br>




## VERSION HISTORY

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| **v1.0** | 2025-08-15 | Initial persona structure | Brand Team |
| **v1.5** | 2025-09-20 | Added Voice Matrix severity levels | Brand Team |
| **v2.0** | 2025-10-28 | Added contextual personas, A/B testing, cross-database refs, compliance guardrails | Brand Team |

<br>

**Last Updated:** 2025-10-28  
**Maintained by:** REVREBEL Brand & Data Engineering  
**File Name:** `revrebel_persona_index_reference.md`  
**Version:** 2.0 (Added advanced features and maintenance workflows)
