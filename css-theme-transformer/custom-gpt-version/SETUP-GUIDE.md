# Custom GPT Setup Guide: CSS Theme Transformer

## Overview
This guide walks you through setting up a Custom ChatGPT for CSS theme transformation. The GPT will be able to analyze stylesheets, understand design systems, and transform them to match new brand guidelines while maintaining accessibility and code quality.

---

## Step 1: Create the Custom GPT

1. Go to **ChatGPT** (https://chat.openai.com)
2. Click your profile icon → **My GPTs**
3. Click **Create a GPT** button
4. Switch to **Configure** tab (skip the Create tab)

---

## Step 2: Basic Configuration

### Name
```
CSS Theme Transformer
```

### Description
```
Expert at analyzing CSS stylesheets and transforming them to match new themes. Specializes in white-labeling, brand customization, and design system migrations while maintaining accessibility standards and code structure.
```

### Instructions
Copy the **entire contents** of the `INSTRUCTIONS.md` file into the Instructions field.

**File location**: `custom-gpt-version/INSTRUCTIONS.md`

**Important**: 
- The instructions field has a character limit (~32,000 characters)
- If you hit the limit, you can move some content to Knowledge files
- Prioritize the workflow and core behavior in Instructions

### Conversation Starters
Add these starter prompts for users:

```
1. "Analyze this stylesheet and show me its current theme"
2. "Transform this CSS to match my brand guidelines"
3. "Help me create a dark mode version of this theme"
4. "Check the accessibility of these color combinations"
```

---

## Step 3: Upload Knowledge Files

Click **Upload files** under the Knowledge section and upload these files:

### File 1: Theme Formats Reference
**File**: `KNOWLEDGE-theme-formats.md`

**Purpose**: Provides examples of how users can specify themes in different formats (JSON, CSS variables, SCSS, etc.). The GPT will reference this when asking users for theme specifications.

### File 2: Accessibility Standards
**File**: `KNOWLEDGE-accessibility.md`

**Purpose**: Contains WCAG guidelines, contrast ratio calculations, and auto-fix strategies. The GPT references this for accessibility validation.

### Optional: Add Your Own Design System
If you have a specific design system documentation (like your REVREBEL style framework docs), upload it as well. The GPT can then reference your actual system when transforming stylesheets.

---

## Step 4: Capabilities Configuration

### Recommended Settings

**Web Browsing**: ✅ **ON**
- Allows the GPT to look up color theory, accessibility guidelines, and latest CSS standards
- Can fetch external font references or design tokens from URLs

**DALL·E Image Generation**: ❌ **OFF** (Not needed)

**Code Interpreter**: ✅ **ON** (Recommended)
- Enables complex calculations for:
  - Contrast ratio calculations
  - Color space conversions
  - Batch processing multiple files
  - Generating comparison reports

---

## Step 5: Actions (Optional - Advanced)

If you want the GPT to integrate with external tools, you can add actions. Examples:

### Option 1: GitHub Integration
Allow the GPT to commit transformed stylesheets directly to your repo.

### Option 2: Figma API
Fetch design tokens directly from Figma design systems.

### Option 3: Custom Validation API
Connect to your own accessibility validation service.

**For most users**: Skip this section. Actions are optional and require API setup.

---

## Step 6: Test Your GPT

Before publishing, test with these scenarios:

### Test 1: Simple Color Transformation
```
Prompt: "I have a button with background #FF6B35. 
Transform it to use #0066CC instead."
```

**Expected**: Should provide transformed CSS immediately.

### Test 2: Full Stylesheet Analysis
```
Prompt: "Analyze this stylesheet and tell me what theme it uses."
[Paste a sample CSS file]
```

**Expected**: Should present organized breakdown of colors, fonts, spacing.

### Test 3: Accessibility Validation
```
Prompt: "Check if #999999 text on #F5F5F5 background 
meets WCAG AA standards."
```

**Expected**: Should calculate contrast ratio and report pass/fail.

### Test 4: Complete Transformation
```
Prompt: "Transform this stylesheet to match our new brand:
- Primary: #0066CC
- Secondary: #6C757D  
- Font: Inter"
[Paste CSS]
```

**Expected**: Should follow the 5-phase workflow and deliver transformed CSS.

---

## Step 7: Publish Settings

### Privacy Options

**Private**: Only you can access
- Recommended for internal company use
- Use with proprietary stylesheets

**Shared via Link**: Anyone with link can access
- Good for team collaboration
- Don't share if working with confidential designs

**Public**: Listed in GPT store
- Consider if you want to share with community
- Review uploaded knowledge files for sensitive info

---

## Usage Tips

### For Best Results

1. **Be Specific**: Provide exact hex values, not color names
   - ❌ "Change blue to red"
   - ✅ "Change #0066CC to #DC3545"

2. **Provide Context**: Mention your framework if relevant
   - "This uses Bootstrap 5 Sass variables"
   - "This is a Tailwind config file"

3. **Specify Standards**: State accessibility requirements
   - "Must meet WCAG AAA"
   - "Minimum AA contrast for all text"

4. **Upload Full Files**: Use file uploads for large stylesheets
   - Don't paste truncated CSS
   - Include all dependencies if using imports

### Iterative Refinement

The GPT works best with iteration:
```
1. First pass: "Transform this stylesheet to my theme"
2. Review output
3. Refinements: "Darken the secondary color by 10%"
4. Validation: "Check accessibility again"
```

---

## Customization for Your Organization

### Add Your Company's Design System

**Example**: For REVREBEL style framework:

1. Upload your `rebel-style/style-framework` documentation
2. Update instructions to reference your system:
   ```
   When working with REVREBEL projects, reference the 
   rebel-style framework documentation in Knowledge files.
   ```

### Add Custom Naming Conventions

If your team uses specific naming patterns:
```
Additional Instructions:
- Use BEM naming for all classes
- Prefix all custom properties with --rb-
- Follow our component naming guide in [knowledge file]
```

### Add Approval Workflows

For enterprise use:
```
Additional Instructions:
After transformation, ALWAYS:
1. Generate a detailed change report
2. List items requiring manual review
3. Suggest review by: [design lead, accessibility specialist]
4. Don't commit changes until approved
```

---

## Troubleshooting

### Issue: GPT doesn't follow the 5-phase workflow
**Fix**: Ensure INSTRUCTIONS.md was fully copied. The workflow should be in the "Workflow: Always Follow These 5 Phases" section.

### Issue: Accessibility checks are inaccurate
**Fix**: Verify KNOWLEDGE-accessibility.md was uploaded. Enable Code Interpreter for calculations.

### Issue: Responses are too verbose
**Fix**: Add to instructions: "Be concise. Avoid over-explaining obvious steps."

### Issue: GPT makes too many assumptions
**Fix**: Add to instructions: "ALWAYS ask before making major decisions. Never assume color mappings."

### Issue: Can't handle large files
**Solution**: 
- Enable Code Interpreter
- Or instruct users to split files
- Or use file uploads instead of copy-paste

---

## Maintenance

### Regular Updates

**Monthly**: Review conversation logs for common issues
**Quarterly**: Update accessibility standards (WCAG evolves)
**As Needed**: Add new framework support (Tailwind updates, new CSS features)

### Feedback Loop

Collect user feedback:
- What transformations failed?
- What questions does the GPT keep asking?
- What could be automated better?

Use feedback to refine instructions and knowledge files.

---

## Advanced: Version Control for Your GPT

Keep your GPT configuration in version control:

```
/css-theme-transformer/
  /custom-gpt-version/
    - INSTRUCTIONS.md (v1.0)
    - KNOWLEDGE-theme-formats.md (v1.0)
    - KNOWLEDGE-accessibility.md (v1.0)
    - SETUP-GUIDE.md (this file)
    - CHANGELOG.md (track updates)
```

When you update the GPT:
1. Edit local files
2. Commit changes with clear messages
3. Re-upload to Custom GPT
4. Test thoroughly
5. Document changes in CHANGELOG.md

---

## Comparison: Claude Skill vs Custom GPT

### Claude Skill Advantages
✅ Better file system integration
✅ Can run code directly
✅ More reliable structured outputs
✅ Better for complex multi-file projects

### Custom GPT Advantages
✅ Accessible to OpenAI users
✅ Can be shared publicly (GPT Store)
✅ Easier to update instructions (no code needed)
✅ Web browsing for latest standards

### Use Both?
Consider maintaining both versions:
- **Claude Skill**: For your team's development workflow
- **Custom GPT**: For client-facing theme consultations

---

## Support Resources

- OpenAI Custom GPT Docs: https://help.openai.com/en/articles/8554397-creating-a-gpt
- WCAG Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
- CSS Specs: https://www.w3.org/Style/CSS/

---

## Next Steps

1. ✅ Complete Steps 1-6 above
2. ✅ Test with sample stylesheets
3. ✅ Share with your team (if applicable)
4. ✅ Gather feedback after 1 week of use
5. ✅ Iterate and improve

Your CSS Theme Transformer is ready! 🎨
