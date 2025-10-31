# REVREBEL Custom GPT Setup Guide

## Overview
Your Custom GPT instructions have been split into two optimized documents:

1. **Core Instructions** (6,239 characters) → Goes in Instructions field
2. **Reference Guide** → Goes in Knowledge base

---

## Setup Instructions

### Step 1: Configure Instructions Field

1. Open your Custom GPT settings
2. Navigate to the **Instructions** section
3. Copy the entire contents of `REVREBEL_GPT_Core_Instructions.md`
4. Paste into the Instructions field
5. Save

✓ This file is **6,239 characters** (well under the 8,000 limit)

---

### Step 2: Upload Knowledge Base Document

1. In Custom GPT settings, navigate to **Knowledge** section
2. Click **Upload files**
3. Upload `REVREBEL_Persona_Reference_Guide_v2.md`
4. Save

The system will now reference this comprehensive guide when needed.

---

## What's in Each Document

### Core Instructions (Instructions Field)
**Purpose:** Essential logic the GPT needs for every interaction

**Contains:**
- Mission and classification framework
- Decision trees for module assignment
- Workflow steps (parse, query, construct, check, upsert)
- Response templates
- Severity taxonomy
- Smart behaviors
- Default metadata
- Quick reference patterns
- Critical rules

**Why it's optimized:**
- Condensed to essential decision logic
- Removes verbose examples
- Focuses on "what to do" vs "how it works"
- References knowledge base for details

---

### Reference Guide (Knowledge Base)
**Purpose:** Comprehensive documentation for complex scenarios

**Contains:**
- Detailed module descriptions with placement rules
- Complete payload examples (8 different types)
- Integration instructions and API setup
- Testing checklist with 20+ scenarios
- Version management procedures
- Sub-persona creation guide
- Troubleshooting guide with solutions
- Error message reference
- Best practices for users and admins
- Maintenance schedule
- Metadata schema reference
- Support information

**Why it's in knowledge:**
- GPT can query it when needed
- Provides deep context without bloating instructions
- Examples can be referenced for complex requests
- Troubleshooting accessible on-demand

---

## How They Work Together

### Example Flow:

**User:** "Our tone should be witty and strategic. Do: Use data. Don't: Use hype."

**Core Instructions (Always Active):**
1. Classify: Detects dual classification (Canonical + Matrix)
2. Parse: Extracts tone descriptors and rules
3. Query: Fetches active persona version
4. Construct: Builds 3 payloads (1 Canonical + 2 Matrix)
5. Check: High confidence → Auto-commit

**Reference Guide (Queried as Needed):**
- If user asks "Show me an example" → Pulls Example 4 (Dual Classification)
- If error occurs → References troubleshooting section
- If uncertain about module → Checks module descriptions
- If version management needed → Follows version procedures

---

## Testing Your Setup

### Quick Test Scenarios

1. **Simple Input:**
   - Input: "Our tone is confident and witty"
   - Expected: Auto-commit, 1 Canonical Principle

2. **Dual Classification:**
   - Input: "We're strategic. Do: Use data. Don't: Use hype."
   - Expected: Preview showing 1 Canonical + 2 Matrix entries

3. **Request Example:**
   - Input: "Show me an example of a brand color entry"
   - Expected: GPT queries knowledge base, returns Example 6

4. **Troubleshooting:**
   - Input: "Why did my classification fail?"
   - Expected: GPT references troubleshooting guide

---

## Configuration Checklist

### Instructions Field
- [ ] Copy REVREBEL_GPT_Core_Instructions.md
- [ ] Paste into Instructions section
- [ ] Verify character count under 8,000
- [ ] Save changes

### Knowledge Base
- [ ] Upload REVREBEL_Persona_Reference_Guide_v2.md
- [ ] Verify upload successful
- [ ] Test query: "Show me module descriptions"
- [ ] Save changes

### API Configuration
- [ ] Set Cloudflare Vectorize endpoint
- [ ] Add authentication token
- [ ] Test connection with version query
- [ ] Enable function calling

### Verification Tests
- [ ] Test simple classification
- [ ] Test dual classification
- [ ] Request example from knowledge base
- [ ] Trigger error handling
- [ ] Test version query

---

## Advanced Configuration

### API Endpoints to Configure

```bash
# Query for active version
GET https://your-worker.workers.dev/persona/query
Headers: Authorization: Bearer [API_KEY]

# Insert records
POST https://your-worker.workers.dev/persona/insert
Headers: Authorization: Bearer [API_KEY]

# Update records (version management)
POST https://your-worker.workers.dev/persona/update
Headers: Authorization: Bearer [API_KEY]
```

### Required Permissions

Your API key needs:
- Read access to persona:revrebel index
- Write access to persona:revrebel index
- Query filtering capability
- Metadata update capability

---

## Optimization Benefits

### Before (Single 18,000 char document):
❌ Too large for instructions field  
❌ All content loaded every time  
❌ Verbose examples bloat responses  
❌ Hard to maintain and update  

### After (Split architecture):
✓ Core logic fits in instructions (6,239 chars)  
✓ Reference loaded only when needed  
✓ Cleaner, faster responses  
✓ Easy to update either component  
✓ Better token efficiency  

---

## Maintenance

### Updating Core Instructions
1. Edit REVREBEL_GPT_Core_Instructions.md
2. Verify character count under 8,000
3. Replace in Custom GPT instructions field
4. Test key workflows

### Updating Reference Guide
1. Edit REVREBEL_Persona_Reference_Guide_v2.md
2. Re-upload to Knowledge section
3. Previous version automatically replaced
4. Test knowledge retrieval

---

## Quick Reference

**Character Limits:**
- Instructions field: 8,000 max
- Your core instructions: 6,239 (✓ fits!)
- Knowledge base: No practical limit

**Files:**
1. `REVREBEL_GPT_Core_Instructions.md` → Instructions
2. `REVREBEL_Persona_Reference_Guide_v2.md` → Knowledge

**System Version:** 2.0  
**Created:** 2025-10-28  
**Documentation:** REVREBEL Persona Index Reference v2.0

---

## Support

If you encounter issues:
1. Check character count of core instructions (must be <8,000)
2. Verify knowledge base uploaded successfully
3. Test API connectivity
4. Review error messages in reference guide
5. Contact REVREBEL Data Engineering Team

---

**Setup complete! Your Custom GPT is ready to intelligently manage the REVREBEL persona vector database.**
