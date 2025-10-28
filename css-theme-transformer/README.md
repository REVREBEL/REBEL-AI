# CSS Theme Transformer - README

## 📋 Overview

This repository contains a comprehensive CSS Theme Transformer tool available in **two versions**:

1. **Claude Skill** - For use with Claude AI (Anthropic)
2. **Custom ChatGPT** - For use with OpenAI's Custom GPT platform

Both versions provide the same core functionality: analyzing CSS stylesheets and systematically transforming them to match different themes while maintaining accessibility, code structure, and design system integrity.

---

## 🎯 What This Tool Does

### Core Capabilities
- **Analyzes** existing CSS stylesheets to extract theme properties
- **Transforms** colors, typography, spacing, and effects to match new brand guidelines
- **Validates** accessibility compliance (WCAG AA/AAA)
- **Preserves** layout, structure, and functional CSS
- **Generates** detailed transformation reports

### Use Cases
- White-labeling applications for different clients
- Migrating between design systems
- Creating theme variants (light/dark mode)
- Batch updating styles across projects
- Ensuring brand consistency
- Converting between CSS methodologies

---

## 📂 Repository Structure

```
/css-theme-transformer/
│
├── SKILL.md                          # Claude Skill version (detailed)
│
└── /custom-gpt-version/
    ├── INSTRUCTIONS.md               # Copy to Custom GPT Instructions field
    ├── KNOWLEDGE-theme-formats.md    # Upload to Custom GPT Knowledge
    ├── KNOWLEDGE-accessibility.md    # Upload to Custom GPT Knowledge
    └── SETUP-GUIDE.md                # Step-by-step Custom GPT setup
```

---

## 🚀 Quick Start

### Option 1: Using with Claude (Anthropic)

1. **Read the skill**: Open `SKILL.md`
2. **Upload to Claude**: In a Claude conversation, simply reference the concepts from the skill
3. **Provide your stylesheet**: Paste or upload your CSS file
4. **Define your theme**: Specify your new brand colors, fonts, etc.
5. **Get transformed CSS**: Claude will follow the transformation workflow

**Best for**: Development teams already using Claude, complex projects needing file system access

### Option 2: Using with Custom ChatGPT (OpenAI)

1. **Follow setup guide**: Open `custom-gpt-version/SETUP-GUIDE.md`
2. **Create your GPT**: Follow Step 1-7 in the guide
3. **Upload knowledge files**: Add the accessibility and theme format references
4. **Test and deploy**: Try sample transformations
5. **Share with team**: Make available to your organization

**Best for**: Teams using ChatGPT Plus, public sharing via GPT Store, simpler setup

---

## 🎨 Example Workflow

```
1. User: "Transform this stylesheet to our new brand"
   [Provides CSS file]

2. Tool: Analyzes stylesheet
   → Identifies colors, fonts, spacing
   → Presents current theme

3. User: Provides new theme
   → Primary: #0066CC
   → Font: Inter

4. Tool: Creates mapping
   → Shows old → new transformations
   → Asks for confirmation

5. User: Confirms

6. Tool: Transforms CSS
   → Validates accessibility
   → Reports any issues
   → Delivers transformed stylesheet

7. User: Reviews and applies
```

---

## 🔑 Key Features

### Intelligent Analysis
- Detects CSS preprocessors (Sass, Less)
- Identifies design tokens and variables
- Maps component patterns
- Understands framework conventions (Bootstrap, Tailwind, etc.)

### Smart Transformation
- Preserves functional CSS (layout, positioning)
- Groups similar color variants
- Maintains selector specificity
- Handles gradients and complex effects
- Scales spacing proportionally (optional)

### Accessibility First
- Calculates WCAG contrast ratios
- Auto-fixes contrast violations when possible
- Flags issues requiring manual review
- Tests hover and focus states
- Considers color blindness implications

### Comprehensive Reporting
- Before/after comparison
- Detailed change log
- Accessibility audit results
- Manual review checklist
- Migration guide

---

## 📊 Supported Formats

### Input (Source Stylesheets)
- ✅ Vanilla CSS (.css)
- ✅ SCSS/Sass (.scss, .sass)
- ✅ Less (.less)
- ✅ CSS-in-JS (styled-components, emotion)
- ✅ Tailwind config (tailwind.config.js)
- ✅ Design tokens (JSON, YAML)

### Output (Theme Definitions)
- ✅ JSON design tokens
- ✅ CSS custom properties
- ✅ SCSS/Less variables
- ✅ Simple text lists
- ✅ Framework-specific configs

---

## 🆚 Version Comparison

| Feature | Claude Skill | Custom GPT |
|---------|-------------|------------|
| **File System Access** | ✅ Full | ⚠️ Limited |
| **Code Execution** | ✅ Yes | ✅ With Code Interpreter |
| **Batch Processing** | ✅ Multiple files | ⚠️ One at a time |
| **Web Search** | ✅ Built-in | ✅ Built-in |
| **Sharing** | ⚠️ Project-based | ✅ Public/Private/Link |
| **Setup Complexity** | 🟢 Simple | 🟡 Moderate |
| **Best For** | Development teams | Broader audiences |

---

## 💡 Usage Tips

### For Best Results

**1. Be Specific**
```
❌ "Make it red"
✅ "Change primary color from #FF6B35 to #DC3545"
```

**2. Provide Complete Context**
```
✅ "This is a Bootstrap 5 Sass file"
✅ "We use BEM naming conventions"
✅ "Must meet WCAG AAA standards"
```

**3. Upload Full Files**
- Use file uploads for large stylesheets
- Include all dependencies (imports, variables)
- Provide design system documentation if available

**4. Iterate**
- Review initial transformation
- Refine specific elements
- Validate incrementally

---

## 🎓 Learning Resources

### Included Knowledge
- **Theme Formats**: Examples of JSON tokens, CSS variables, SCSS, etc.
- **Accessibility**: WCAG standards, contrast calculations, auto-fix strategies
- **CSS Patterns**: Common design system structures

### External Resources
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [CSS Specifications](https://www.w3.org/Style/CSS/)
- [Design Tokens W3C](https://design-tokens.github.io/community-group/format/)

---

## 🔧 Customization

### For Your Organization

Both versions can be customized with:
- **Your design system docs**: Upload your style guide
- **Custom naming conventions**: BEM, SMACSS, custom patterns
- **Specific approval workflows**: Add review steps
- **Framework preferences**: Tailwind, Bootstrap, custom

See `SKILL.md` (Claude) or `SETUP-GUIDE.md` (Custom GPT) for details.

---

## 🐛 Troubleshooting

### Common Issues

**Colors not transforming correctly**
- Ensure exact hex values provided
- Check for similar color variants (group them)
- Verify theme mapping is complete

**Accessibility errors persist**
- Review contrast calculations manually
- Some color combinations may not be auto-fixable
- Consider adjusting brand colors for compliance

**Large files timing out**
- Split into smaller files
- Use batch processing (Claude version)
- Enable Code Interpreter (Custom GPT)

**Syntax errors in output**
- Verify source CSS is valid
- Check for malformed rules (tool will skip)
- Review framework-specific syntax

---

## 📝 Examples

### Example 1: Simple Color Swap
```css
/* Before */
.button {
  background: #FF6B35;
  color: #FFFFFF;
}

/* After (Theme: Primary #0066CC) */
.button {
  background: #0066CC;
  color: #FFFFFF;
}
```

### Example 2: Design Token Migration
```css
/* Before */
.card {
  background: #F5F5F5;
  border: 1px solid #CCCCCC;
  padding: 16px;
}

/* After */
.card {
  background: var(--color-neutral-100);
  border: 1px solid var(--color-neutral-300);
  padding: var(--spacing-md);
}
```

### Example 3: With Accessibility Fix
```css
/* Before (Contrast: 3.1:1 ❌) */
.subtitle {
  color: #999999;
  background: #FFFFFF;
}

/* After (Contrast: 4.6:1 ✅) */
.subtitle {
  color: #767676; /* Auto-darkened for AA compliance */
  background: #FFFFFF;
}
```

---

## 🤝 Contributing

### Improvements Welcome
- Additional framework support
- Enhanced accessibility algorithms
- New transformation strategies
- Better error handling
- Documentation improvements

---

## 📄 License

This tool is provided as-is for internal and commercial use. Modify and adapt as needed for your organization.

---

## 🎯 Next Steps

1. **Choose your version** (Claude or Custom GPT)
2. **Follow the setup guide** for your platform
3. **Test with sample stylesheets**
4. **Integrate into your workflow**
5. **Provide feedback** for improvements

---

## 📞 Support

For issues or questions:
- Review the detailed SKILL.md (Claude) or SETUP-GUIDE.md (Custom GPT)
- Check troubleshooting sections
- Reference knowledge files for standards
- Test with simple examples first

---

**Ready to transform your themes? Pick your platform and get started!** 🚀
