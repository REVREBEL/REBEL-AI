# REVREBEL Persona Vector Database Reference Guide
## Knowledge Base Document v2.0

---

## Module Reference Guide

### Brand Core
**Purpose:** Captures the strategic essence and foundational beliefs of the brand.

**Submodules:**
- Mission & Vision
- Brand Values
- Brand Purpose
- Brand Personality
- Brand Archetype

**Placement Rules:**
- Use when request includes "why we exist" or "what we aim to become"
- Insert if prompt includes "principles" or "values-driven" keywords
- Include when archetype words (Hero, Sage, etc.) are used

**Example Use Case:** "We exist to help independent hoteliers punch above their weight."

---

### Audience Insight
**Purpose:** Describes who the brand is talking to and how to emotionally resonate.

**Submodules:**
- Demographics
- Psychographics
- Buyer Personas
- Audience Tone Preferences

**Placement Rules:**
- Use for structured audience info inputs
- Insert when prompt includes psychological or emotional descriptors
- Place if prompt includes defined personas by name, title, or scenario
- Insert if style matching to audience is required (e.g., technical vs casual)

**Example Use Case:** "Our clients are ambitious, independent-minded operators who value performance over convention."

---

### Brand Messaging System
**Purpose:** The structured language and communication strategy of the brand.

**Submodules:**
- Value Propositions
- Brand Pillars
- Taglines & Slogans
- Messaging by Funnel Stage
- Signature Phrases & Keywords

**Placement Rules:**
- Insert if user asks "Why choose us?" or similar
- Use if prompt includes "main messages" or "key ideas"
- Place if short, punchy lines are mentioned
- Insert when content is tied to funnel stages
- Include if prompt asks for unique brand language or phrases

**Example Use Case:** "Revenue intelligence meets arcade-era clarity."

---

### Brand Voice & Style
**Purpose:** Rules and personality of the brand's written expression.

**Submodules:**
- Voice Principles (Canonical philosophical guidance)
- Voice Matrix (Atomic actionable rules)
- Grammar Rules
- Sentence Structures
- Tone Variations
- Tone by Channel

**Placement Rules:**
- Insert when defining brand's personality in language
- Include if prompt involves linguistic correctness
- Use when prompt asks for tone clarity or pacing
- Insert if multiple brand contexts are involved
- Include when prompt refers to guidelines or rules

**Example Use Case:** "Do: Write like a strategist. Don't: Use marketing hype."

---

### Visual Identity System
**Purpose:** Visual rules and elements that express the brand.

**Submodules:**
- Logos
- Brand Colors
- Typography
- Image Style
- Design Do's & Don'ts
- Moodboards

**Placement Rules:**
- Use if logo files or spacing rules are referenced
- Place if colors or palette mentioned explicitly
- Insert if fonts or typesetting guidelines are discussed
- Use when discussing image direction or aesthetic
- Include for consistency checks or visual guardrails
- Insert if user needs visual inspiration aligned with brand

**Example Use Case:** Brand color palette with hex codes and usage rules.

---

### Brand Comparison & Inspiration
**Purpose:** Metaphorical and competitive framing for stylistic alignment.

**Submodules:**
- Brand Emulators
- Analogies & Metaphors
- Tone Benchmarks
- Differentiators

**Placement Rules:**
- Use if user makes brand analogies (e.g., "We're the Tesla of...")
- Insert if prompt contains metaphorical framing
- Use if brand tone is compared to others
- Include if prompt asks for what makes us different

**Example Use Case:** "We're the lovechild of a Star Wars production designer and a Linux developer."

---

### Tactical Brand Usage
**Purpose:** Application-specific expressions of the brand.

**Submodules:**
- Use Cases
- Touchpoint Guidance
- Common Mistakes
- Template Outputs

**Placement Rules:**
- Insert if user provides a goal or format (e.g., email, tweet)
- Use for cross-channel campaign prompts
- Insert if user asks "what to avoid" or shows inconsistency
- Use when referencing real past campaigns or templates

**Example Use Case:** "On LinkedIn, maintain professional authority while being approachable."

---

## Complete Payload Examples

### Example 1: Canonical Principle (Brand Personality)

```json
{
    "id": "brand-personality-witty-intellectual",
    "text": "REVREBEL's personality is witty, sarcastic, and intellectually sharp. Its humor is dry and layered – pop culture nods fused with strategic intelligence. It makes the smart feel cool, replacing overt humor with refined wit that respects the user's intellect.",
    "metadata": {
        "module": "Brand Core",
        "submodule": "Brand Personality",
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "tone": "Witty, Intellectual, Rebellious",
        "use_case": "Brand storytelling and AI persona definition",
        "audience": "Internal Creative Teams, AI Systems",
        "language": "en",
        "channel": "All",
        "funnel_stage": "Foundational",
        "status": "active",
        "created_ym": "2025-10",
        "author": "REVREBEL"
    }
}
```

### Example 2: Voice Matrix Entry (Do Rule)

```json
{
    "id": "vm-strategist-voice-do",
    "text": "Strategist Voice – Do: Write like a seasoned strategist, not a marketer. Focus on what matters and why.",
    "metadata": {
        "module": "Brand Voice & Style",
        "submodule": "Voice Matrix",
        "attribute": "Strategist Voice",
        "rule_type": "do",
        "severity": "must",
        "example_good": "Here's what matters and why.",
        "example_bad": "Let's revolutionize your business!",
        "channel": "All",
        "weight": 1.0,
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "language": "en",
        "status": "active",
        "created_ym": "2025-10",
        "author": "REVREBEL"
    }
}
```

### Example 3: Voice Matrix Entry (Don't Rule)

```json
{
    "id": "vm-marketing-hype-dont",
    "text": "Marketing Hype – Don't: Rely on hype or generic marketing language.",
    "metadata": {
        "module": "Brand Voice & Style",
        "submodule": "Voice Matrix",
        "attribute": "Marketing Hype",
        "rule_type": "dont",
        "severity": "must",
        "example_good": "We optimize for revenue, not impressions.",
        "example_bad": "Revolutionize your business with cutting-edge solutions!",
        "channel": "All",
        "weight": 1.0,
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "language": "en",
        "status": "active",
        "created_ym": "2025-10",
        "author": "REVREBEL"
    }
}
```

### Example 4: Dual Classification (Strategic Voice + Rules)

**User Input:**
> "Our writing voice is grounded in strategic intelligence. Do: Write like a strategist. Don't: Use marketing hype."

**System Creates 3 Records:**

**Record 1 - Canonical Principle:**
```json
{
    "id": "voice-strategic-intelligence-philosophy",
    "text": "Our writing voice is grounded in strategic intelligence, focusing on clarity, precision, and insight-driven communication.",
    "metadata": {
        "module": "Brand Voice & Style",
        "submodule": "Voice Principles",
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "tone": "Strategic, Intelligent, Confident",
        "use_case": "Tone calibration",
        "status": "active",
        "created_ym": "2025-10"
    }
}
```

**Record 2 - Voice Matrix (Do):**
```json
{
    "id": "vm-strategist-voice-do",
    "text": "Strategist Voice – Do: Write like a strategist, not a marketer",
    "metadata": {
        "module": "Brand Voice & Style",
        "submodule": "Voice Matrix",
        "attribute": "Strategist Voice",
        "rule_type": "do",
        "severity": "must",
        "weight": 1.0,
        "persona_version": "v1.0",
        "status": "active"
    }
}
```

**Record 3 - Voice Matrix (Don't):**
```json
{
    "id": "vm-marketing-hype-dont",
    "text": "Marketing Hype – Don't: Use marketing hype or generic language",
    "metadata": {
        "module": "Brand Voice & Style",
        "submodule": "Voice Matrix",
        "attribute": "Marketing Hype",
        "rule_type": "dont",
        "severity": "must",
        "weight": 1.0,
        "persona_version": "v1.0",
        "status": "active"
    }
}
```

### Example 5: Tone by Channel

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
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "status": "active",
        "created_ym": "2025-10",
        "author": "REVREBEL",
        "language": "en"
    }
}
```

### Example 6: Brand Color

```json
{
    "id": "color-dark-blue",
    "text": "Dark Blue (#163666) is a primary brand color used to convey trust and professionalism. Its inverse for contrast is #B2D3DE.",
    "metadata": {
        "module": "Visual Identity System",
        "submodule": "Brand Colors",
        "use_case": "Palette usage",
        "audience": "Designers, Developers, Brand Managers",
        "language": "en",
        "channel": "Web, Print, UI/UX",
        "role": "Primary",
        "hex": "#163666",
        "inverse": "#B2D3DE",
        "color_name": "Dark Blue",
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "status": "active",
        "created_ym": "2025-10",
        "author": "REVREBEL"
    }
}
```

### Example 7: Brand Emulator (Metaphorical Positioning)

```json
{
    "id": "brand-emulators-cultural-references",
    "text": "The brand blends the innovation of FAST COMPANY, design sophistication of MONOCLE, retro cool of early WIRED, and gaming culture edge of EDGE. Influences span Ocean's Eleven's suave execution, TRON: LEGACY's digital artistry, and Daft Punk's analog-futurism. It's ThinkGeek meets Aesop—with a sprinkle of Supreme swagger.",
    "metadata": {
        "module": "Brand Comparison & Inspiration",
        "submodule": "Brand Emulators",
        "use_case": "Cultural positioning and tonal alignment",
        "tone": "Stylish, Irreverent, Geeky, Strategic",
        "audience": "Brand & Creative Teams",
        "language": "en",
        "channel": "Strategy & Design",
        "funnel_stage": "Foundational",
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "status": "active",
        "created_ym": "2025-10",
        "author": "REVREBEL"
    }
}
```

### Example 8: Audience Psychographics

```json
{
    "id": "audience-psychographics-hospitality-performance",
    "text": "Our client base is independent-minded and ambitious – operators who refuse cookie-cutter solutions. They're performance-obsessed and style-conscious, balancing aesthetics with analytics. Time-strapped but thoughtful, they seek partners who simplify complexity. Having tried the traditional path, they now crave transformation – ready to hack the hospitality matrix to achieve results.",
    "metadata": {
        "module": "Audience Insight",
        "submodule": "Psychographics",
        "use_case": "Persona development",
        "tone": "Strategic, Ambitious, Empathetic",
        "audience": "Internal Strategy, Marketing, and AI Training Teams",
        "language": "en",
        "channel": "Brand Messaging, Campaign Strategy",
        "funnel_stage": "Awareness & Consideration",
        "persona_id": "revrebel_core",
        "persona_version": "v1.0",
        "status": "active",
        "created_ym": "2025-10",
        "author": "REVREBEL"
    }
}
```

---

## Integration Instructions

### Custom GPT Configuration

1. **Copy core instructions** from `REVREBEL_GPT_Core_Instructions.md` into your Custom GPT's instructions field (under 8000 characters)

2. **Upload this reference guide** to the knowledge base section

3. **Configure API access** to your Cloudflare Vectorize endpoint:
   ```
   GET  /query    # For version checking and retrieval
   POST /insert   # For upserting new records
   POST /update   # For version management
   
   Authorization: Bearer [API_KEY]
   Base URL: https://your-worker.workers.dev/persona
   ```

4. **Enable function calling** for:
   - Query operations (to fetch active persona_version)
   - Insert operations (to upsert records)
   - Update operations (for version management)

5. **Set system behavior** to:
   - Always query for active version before upserting
   - Default to preview mode for ambiguous inputs
   - Atomize multi-rule inputs into separate records

### API Requirements

```python
# Query for active version
response = requests.get(
    "https://your-worker.workers.dev/persona/query",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"filter": {"status": "active", "persona_id": "revrebel_core"}}
)

# Insert new record
response = requests.post(
    "https://your-worker.workers.dev/persona/insert",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"records": [payload]}
)

# Update version (deprecate old)
response = requests.post(
    "https://your-worker.workers.dev/persona/update",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"filter": {"persona_version": "v1.0"}, "update": {"status": "deprecated"}}
)
```

---

## Testing Checklist

### Basic Classification Tests

- [ ] **Simple tone descriptor:** "Our tone is confident and witty"
  - Expected: 1 Canonical Principle (Voice Principles)
  
- [ ] **Do/Don't rules:** "Do: Use data. Don't: Use hype."
  - Expected: 2 Voice Matrix entries (atomic rules)
  
- [ ] **Dual classification:** "Our voice is strategic. Do: Write like a strategist."
  - Expected: 1 Canonical + 1 Voice Matrix
  
- [ ] **Channel-specific:** "On LinkedIn, we're professional but approachable"
  - Expected: 1 Canonical (Tone by Channel)

### Complex Scenarios

- [ ] **Brand colors:** Paste JSON with multiple hex codes
  - Expected: N separate records (one per color)
  
- [ ] **Ambiguous input:** "Add something about emotional range"
  - Expected: Clarification request
  
- [ ] **Version bump:** "Create new version v2.0"
  - Expected: New version created, old deprecated
  
- [ ] **Sub-persona:** "For customer support, be patient and helpful"
  - Expected: New persona_id with inherits_from

### Edge Cases

- [ ] **Multiple rules in one input:** List of 5 Do's and Don'ts
  - Expected: 10 atomic Voice Matrix entries
  
- [ ] **Examples included:** "Do: Use data (e.g., 'According to STR...')"
  - Expected: example_good extracted to metadata
  
- [ ] **Implicit severity:** "This is absolutely critical"
  - Expected: severity set to "must"

### Validation

- [ ] All records have persona_version (not hardcoded)
- [ ] created_ym matches current month
- [ ] Status always "active" for new entries
- [ ] Weights assigned correctly based on severity
- [ ] Module/submodule names match documentation exactly

---

## Version Management

### Creating New Version

**User Request:** "Bump version to v2.0"

**System Actions:**
1. Query all records with current active version
2. Create new version entry as "active"
3. Update all old version records to "deprecated"
4. Log change with change_log and change_reason

**Example:**
```python
# New version marker
{
    "id": "persona-version-v2-0",
    "text": "Version 2.0 introduces refined wit and reduced exclamation point usage",
    "metadata": {
        "persona_id": "revrebel_core",
        "persona_version": "v2.0",
        "change_log": "Shifted from quirky humor to dry wit",
        "change_reason": "Brand maturity; targeting enterprise clients",
        "change_author": "brand-team",
        "valid_from": "2025-11-01T00:00:00Z",
        "supersedes": ["v1.0"],
        "status": "active"
    }
}

# Update all v1.0 records
UPDATE WHERE persona_version = "v1.0"
SET status = "deprecated", valid_until = "2025-11-01T00:00:00Z"
```

### Version History Tracking

```json
{
    "id": "voice-authority-v2",
    "text": "Updated voice principle...",
    "metadata": {
        "persona_version": "v2.0",
        "supersedes": ["voice-authority-v1"],
        "change_log": "Refined professional tone",
        "valid_from": "2025-11-01T00:00:00Z",
        "status": "active"
    }
}
```

---

## Sub-Personas

### Contextual Personas

When content requires different tone for specific contexts, create sub-personas:

| Context | Persona ID | Tone Shift | Use Case |
|---------|------------|------------|----------|
| **Founder Voice** | `revrebel_founder` | Visionary, bold, aspirational | Keynotes, manifestos |
| **Customer Support** | `revrebel_support` | Helpful, patient, empathetic | Help docs, tickets |
| **Technical Docs** | `revrebel_technical` | Precise, clear, instructional | API docs, guides |
| **Sales** | `revrebel_sales` | Confident, value-focused | Pitch decks, proposals |
| **Social Media** | `revrebel_social` | Casual, witty, conversational | Twitter, LinkedIn |

### Sub-Persona Example

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

---

## Troubleshooting Guide

### Common Issues & Solutions

**Issue:** "Cannot determine module"  
**Cause:** Input too vague or spans multiple modules  
**Solution:** 
- Ask: "Does this describe WHO we are, HOW we speak, or WHAT we look like?"
- Provide context about brand element being described
- Specify module explicitly if known

---

**Issue:** "Version query failed"  
**Cause:** API connectivity or index doesn't exist  
**Solution:**
- Check API endpoint accessibility
- Verify persona:revrebel index exists in Vectorize
- Fallback to default v1.0 with warning
- Verify API key permissions

---

**Issue:** "Too many records created"  
**Cause:** System atomized rules correctly (expected behavior)  
**Solution:**
- This is correct - each rule should be separate
- Review preview to confirm structure
- Commit if all rules are intentional

---

**Issue:** "Classification seems wrong"  
**Cause:** Ambiguous input or edge case  
**Solution:**
- Type "REVISE" to manually specify module/submodule
- Provide more context about intent
- Explicitly state desired classification

---

**Issue:** "Examples not extracted"  
**Cause:** Examples not in recognizable format  
**Solution:**
- Use clear format: "e.g., 'example text'" or "(example text)"
- Separate good/bad examples clearly
- Manually add to metadata if needed

---

**Issue:** "Severity not assigned"  
**Cause:** Implicit importance not recognized  
**Solution:**
- Use explicit keywords: "must", "critical", "important"
- Or manually specify: "This is a MUST rule"
- Default will be "should" if unclear

---

**Issue:** "Sub-persona not created"  
**Cause:** Context not recognized as needing separate persona  
**Solution:**
- Explicitly state: "Create founder voice sub-persona"
- Or: "This is for customer support context"
- Specify inherits_from and overrides

---

**Issue:** "Channel constraints missing"  
**Cause:** Platform-specific rules not detailed enough  
**Solution:**
- Specify constraints explicitly: "max 280 chars", "no emojis"
- Reference platform: "for LinkedIn" vs "for Twitter"
- Include example_phrases and avoid_phrases

---

## Error Messages

### API Errors

```
❌ UPSERT FAILED
Error: 401 Unauthorized
Payload attempted: [payload]
Action: Check API key configuration
```

```
❌ UPSERT FAILED
Error: 413 Payload Too Large
Payload attempted: [payload]
Action: Text exceeds max length. Break into smaller chunks.
```

```
⚠ VERSION QUERY FAILED
Error: Timeout
Action: Using fallback version v1.0. Verify before committing.
```

### Classification Errors

```
🔍 CLASSIFICATION UNCLEAR
Detected: Possible Brand Core or Brand Voice & Style
Input contains: [ambiguous phrases]
Please clarify: Which module should I use?
```

```
⚠ MISSING REQUIRED FIELD
Field: rule_type
Context: Voice Matrix entry requires "do" or "dont"
Action: Please specify whether this is a Do or Don't rule
```

---

## Best Practices

### For Users

1. **Be explicit about context** - "For LinkedIn posts" vs "For all channels"
2. **Separate rules clearly** - One Do/Don't per line for atomization
3. **Include examples** - Helps system extract good/bad examples
4. **Specify severity** - Use keywords: "must", "critical", "prefer"
5. **Request preview** - Type "preview" for complex inputs
6. **Provide version context** - Specify if creating new version

### For Administrators

1. **Regular version audits** - Review active versions quarterly
2. **Deprecation cleanup** - Archive old deprecated records after 6 months
3. **Consistency checks** - Validate module/submodule names match docs
4. **Metadata validation** - Ensure required fields present
5. **API monitoring** - Track upsert success rates
6. **Documentation sync** - Keep reference guide updated with core docs

---

## Maintenance Schedule

### Weekly
- [ ] Check for draft entries pending approval
- [ ] Validate recent upserts for accuracy
- [ ] Review error logs

### Monthly
- [ ] Audit active versions
- [ ] Check for duplicate entries
- [ ] Validate metadata consistency
- [ ] Review sub-persona usage

### Quarterly
- [ ] Consider version bump if major changes
- [ ] Archive deprecated records >6 months old
- [ ] Update reference documentation
- [ ] Review and update severity levels

---

## Metadata Schema Reference

### Core Fields (Required)

| Field | Type | Description |
|-------|------|-------------|
| `persona_id` | string | Core or sub-persona ID |
| `persona_version` | string | Semantic version (v1.0, v2.0) |
| `module` | string | Top-level module name |
| `submodule` | string | Specific submodule |
| `status` | string | active, deprecated, draft |
| `language` | string | Content language (default: en) |
| `created_ym` | string | Creation date (YYYY-MM) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `tone` | string | Tone descriptors |
| `use_case` | string | Primary application |
| `audience` | string | Target users |
| `channel` | string | Applicable channels |
| `platform` | string | Specific platform |
| `funnel_stage` | string | Buyer journey stage |

### Voice Matrix Fields

| Field | Type | Description |
|-------|------|-------------|
| `attribute` | string | Style attribute name |
| `rule_type` | string | do or dont |
| `severity` | string | must, should, prefer, avoid, never |
| `example_good` | string | Positive example |
| `example_bad` | string | Negative example |
| `weight` | number | Importance (0.0-1.0) |

### Version Management Fields

| Field | Type | Description |
|-------|------|-------------|
| `valid_from` | string | ISO timestamp |
| `valid_until` | string | ISO timestamp |
| `supersedes` | array | Previous version IDs |
| `change_log` | string | Description of changes |
| `change_reason` | string | Why version changed |
| `change_author` | string | Who made change |

---

## Support & Contact

**Documentation:** REVREBEL Persona Index Reference v2.0  
**System Version:** 2.0  
**Last Updated:** 2025-10-28  
**Maintained By:** REVREBEL Data Engineering Team  
**Compatible With:** Cloudflare Vectorize, OpenAI Custom GPT

For issues or questions:
1. Check this reference guide first
2. Review core instructions
3. Contact: REVREBEL Data Engineering Team

---

## Quick Reference Card

**Classification:**
- WHO we are → Brand Core
- WHO we serve → Audience Insight
- WHAT we say → Brand Messaging
- HOW we speak → Brand Voice & Style
- What we LOOK like → Visual Identity
- Comparisons → Brand Comparison
- Application → Tactical Usage

**Record Types:**
- Strategic content → Canonical Principle
- Actionable rules → Voice Matrix
- Both → Dual Classification

**Severity:**
- must (1.0) - Non-negotiable
- should (0.85) - Strong recommendation
- prefer (0.4) - Stylistic preference
- avoid (0.6) - Discouraged
- never (1.0) - Prohibited

**Commands:**
- "preview" - Show before committing
- "COMMIT" - Proceed with upsert
- "REVISE" - Modify classification

---

**End of Reference Guide**
