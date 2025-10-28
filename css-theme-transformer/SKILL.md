# CSS Theme Transformer Skill

## Purpose
Systematically analyze and transform CSS stylesheets to adapt them to different predefined themes. Designed for white-labeling, brand customization, and theme migration scenarios where applications need to maintain their existing structure while applying new visual identities.

## When to Use This Skill
Use this skill when you need to:
- White-label applications for different clients
- Migrate between design systems or brand guidelines
- Create theme variants (light/dark mode, seasonal themes, brand refresh)
- Batch update styles across large codebases
- Ensure brand consistency across custom implementations
- Convert between CSS methodologies (design tokens, CSS variables, Sass/Less)
- Adapt third-party stylesheets to match your brand

## Core Workflow

### Phase 1: Analysis
**Extract the Design System**
1. Parse CSS/SCSS/Less files and identify structure
2. Categorize properties:
   - **Colors**: backgrounds, borders, text, shadows, fills
   - **Typography**: font-families, sizes, weights, line-heights
   - **Spacing**: margins, padding, gaps
   - **Effects**: shadows, borders, border-radius, opacity
   - **Layout**: breakpoints, grid systems
3. Identify patterns:
   - Design tokens (CSS custom properties like `--color-primary`)
   - Preprocessor variables (`$brand-blue`, `@spacing-md`)
   - Utility classes (`.text-primary`, `.btn-large`)
   - Component patterns (`.card`, `.button`, `.nav`)
4. Map dependencies and cascades
5. Document the existing theme schema

### Phase 2: Theme Definition
**Define the Target Theme**
1. Accept theme specification in formats:
   - JSON design tokens
   - CSS custom properties
   - Sass/Less variables
   - Plain color/font lists
2. Validate theme completeness
3. Create mapping between source → target
4. Flag missing mappings for user decision

### Phase 3: Transformation
**Apply the New Theme**
1. **Strategy Selection** (automatic or user-specified):
   - **Direct Replacement**: Replace hex colors, font names directly
   - **Variable Update**: Update only variable definitions
   - **Token Migration**: Convert to design token system
   - **Hybrid**: Combination approach based on complexity

2. **Transformation Rules**:
   - Preserve functional CSS (layout, positioning, display properties)
   - Transform only theme-related properties
   - Maintain selector specificity and cascade order
   - Keep media queries and responsive breakpoints
   - Preserve animations and transitions (update colors within them)

3. **Smart Replacements**:
   - Color matching with tolerance (handle slight variations)
   - Proportional spacing adjustments
   - Font-stack preservation (fallbacks)
   - Shadow property adaptation

### Phase 4: Validation
**Ensure Quality**
1. **Accessibility checks**:
   - WCAG contrast ratios (AA/AAA compliance)
   - Color blindness simulation
   - Readability scores
2. **Consistency checks**:
   - No orphaned colors or fonts
   - Consistent spacing scale
   - Proper variable usage
3. **Regression detection**:
   - Compare before/after structure
   - Flag unintended changes

### Phase 5: Output
**Deliver Results**
1. Generate transformed stylesheet(s)
2. Provide transformation report:
   - Changes summary
   - Accessibility warnings
   - Manual review needed (if any)
3. Create side-by-side comparison
4. Generate migration guide

## Input Formats Supported

### Source Stylesheets
- Vanilla CSS (.css)
- SCSS/Sass (.scss, .sass)
- Less (.less)
- CSS-in-JS (styled-components, emotion)
- Tailwind config files
- Design tokens (JSON, YAML)

### Theme Definitions
```json
{
  "colors": {
    "primary": "#0066CC",
    "secondary": "#6C757D",
    "success": "#28A745",
    "text": {
      "base": "#212529",
      "muted": "#6C757D"
    }
  },
  "typography": {
    "fontFamily": {
      "base": "'Inter', sans-serif",
      "heading": "'Poppins', sans-serif"
    },
    "fontSize": {
      "base": "16px",
      "scale": 1.25
    }
  },
  "spacing": {
    "unit": "8px",
    "scale": [0, 4, 8, 16, 24, 32, 48, 64]
  }
}
```

## Example Usage Patterns

### Pattern 1: Complete White-Label
```
User: "Transform this stylesheet to match our client's brand"
[Provides source CSS + brand guidelines]

Process:
1. Analyze existing stylesheet
2. Extract current theme values
3. Map to new brand colors/fonts
4. Transform all instances
5. Validate accessibility
6. Output transformed CSS + report
```

### Pattern 2: Design Token Migration
```
User: "Convert our hardcoded colors to design tokens"

Process:
1. Identify all color values
2. Group similar colors (with tolerance)
3. Generate token names
4. Create CSS custom properties
5. Replace values with var() references
6. Output refactored CSS + tokens file
```

### Pattern 3: Dark Mode Creation
```
User: "Create a dark mode version of this theme"

Process:
1. Identify light theme colors
2. Calculate dark mode equivalents (invert + adjust)
3. Maintain contrast ratios
4. Generate prefers-color-scheme media queries
5. Output dual-theme stylesheet
```

## Best Practices

### Preservation Rules
**Always Preserve:**
- Layout properties (display, position, flexbox, grid)
- Sizing and dimensions
- Z-index layering
- Transform and transition durations
- Accessibility attributes
- Comments explaining business logic

**Transform:**
- Color values (hex, rgb, hsl, named colors)
- Font families and typography properties
- Spacing values (if scaling factor provided)
- Border properties (colors, but not widths unless specified)
- Shadow values (colors only)

### Color Matching Strategy
1. **Exact Match**: Direct hex/rgb replacement
2. **Fuzzy Match**: Group similar colors (delta E < 10)
3. **Semantic Match**: primary → primary, danger → danger
4. **Accessibility-First**: Ensure contrast before replacement

### Variable Naming Conventions
When generating design tokens:
- Use semantic names: `--color-primary` not `--blue`
- Include context: `--text-color-muted` not `--color-gray`
- Follow scale: `--spacing-sm/md/lg` not `--spacing-1/2/3`
- Maintain hierarchy: `--button-bg-primary` vs `--button-bg-secondary`

## Advanced Features

### Batch Processing
Transform multiple stylesheets simultaneously while maintaining cross-file variable references:
```
Input: [main.css, components.css, utilities.css]
Output: [main-themed.css, components-themed.css, utilities-themed.css]
```

### Incremental Updates
Only transform changed files in a larger system:
```
--mode incremental
--changed-files: header.css, footer.css
--preserve-unchanged: true
```

### Framework-Specific Handlers

**Tailwind CSS**:
- Transform tailwind.config.js
- Update color palette
- Modify typography scale
- Adjust spacing units

**Bootstrap**:
- Update Sass variables
- Maintain component structure
- Preserve utility classes

**Material-UI/MUI**:
- Transform theme object
- Update palette definitions
- Adjust component overrides

## Output Examples

### Transformation Report
```
=== CSS THEME TRANSFORMATION REPORT ===

Source: rebel-style.css (2,458 lines)
Target Theme: Acme Corp Brand Guidelines

CHANGES APPLIED:
✓ Colors transformed: 47 instances
  - Primary: #FF6B35 → #0066CC
  - Secondary: #004E89 → #6C757D
  - Accent: #F7B801 → #FFC107

✓ Typography updated: 23 instances
  - Headings: 'Montserrat' → 'Poppins'
  - Body: 'Open Sans' → 'Inter'
  
✓ Spacing adjusted: 15 instances (1.2x scale)

ACCESSIBILITY:
⚠ 2 contrast issues detected (AA compliance)
  - .btn-secondary text needs darker shade
  - .footer-link hover state below 4.5:1

MANUAL REVIEW NEEDED:
• Logo colors in .brand-header (line 145)
• Custom gradient in .hero-section (line 892)

FILES GENERATED:
1. rebel-style-acme.css (transformed)
2. theme-tokens-acme.css (new variables)
3. comparison-report.html (visual diff)
```

## Error Handling

### Common Issues & Solutions

**Missing Theme Values**:
```
Error: No mapping found for color #E8F4F8
Solution: Suggest closest theme color or request mapping
```

**Accessibility Violations**:
```
Warning: New color contrast ratio 3.2:1 (needs 4.5:1)
Action: Automatically darken/lighten to meet WCAG AA
```

**Syntax Errors**:
```
Error: Invalid CSS in source file (line 234)
Action: Skip malformed rules, log for manual review
```

## Integration Points

### Version Control
- Generate git-friendly diffs
- Create feature branches automatically
- Commit messages with transformation summary

### CI/CD Pipeline
- Validate themes before deployment
- Run accessibility checks in CI
- Generate preview builds for each theme

### Design Tools
- Import from Figma styles
- Export to design token formats (Style Dictionary)
- Sync with design system documentation

## Limitations & Considerations

**Cannot Automatically Handle:**
- Images and icons (requires manual asset replacement)
- Complex CSS animations with multiple color stops
- Vendor-prefixed experimental properties
- JavaScript-calculated styles
- External font loading (CDN URLs need manual update)

**Requires Human Review:**
- Brand-specific graphics (logos, illustrations)
- Custom gradients with 3+ stops
- Filter effects with color matrices
- Semantic color meanings (success/danger may vary)

## Continuous Improvement

The skill learns from:
- User corrections and overrides
- Common transformation patterns
- Accessibility adjustments
- Framework-specific quirks

Track metrics:
- Transformation accuracy rate
- Accessibility compliance rate
- Manual intervention frequency
- User satisfaction scores

---

## Quick Start Guide

1. **Provide source stylesheet(s)**
2. **Define target theme** (JSON, variables, or describe)
3. **Specify transformation strategy** (or use auto-detect)
4. **Review transformation report**
5. **Apply changes** or request adjustments
6. **Validate** in browser/design tools

## Support

For complex transformations:
- Provide sample HTML showing usage
- Share design system documentation
- Include brand guidelines
- Specify accessibility requirements (AA/AAA)
