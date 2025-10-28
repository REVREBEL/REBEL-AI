# Theme Specification Format Guide

This document provides standard formats for defining themes that can be transformed.

## Format 1: JSON Design Tokens (Recommended)

```json
{
  "name": "Acme Corp Theme",
  "version": "2.0",
  "colors": {
    "primary": {
      "main": "#0066CC",
      "light": "#3384D6",
      "dark": "#004C99",
      "contrast": "#FFFFFF"
    },
    "secondary": {
      "main": "#6C757D",
      "light": "#ADB5BD",
      "dark": "#495057",
      "contrast": "#FFFFFF"
    },
    "neutral": {
      "50": "#F8F9FA",
      "100": "#E9ECEF",
      "200": "#DEE2E6",
      "300": "#CED4DA",
      "400": "#ADB5BD",
      "500": "#6C757D",
      "600": "#495057",
      "700": "#343A40",
      "800": "#212529",
      "900": "#000000"
    },
    "success": "#28A745",
    "warning": "#FFC107",
    "error": "#DC3545",
    "info": "#17A2B8"
  },
  "typography": {
    "fontFamily": {
      "base": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      "heading": "'Poppins', 'Inter', sans-serif",
      "monospace": "'Fira Code', 'Courier New', monospace"
    },
    "fontSize": {
      "xs": "0.75rem",
      "sm": "0.875rem",
      "base": "1rem",
      "lg": "1.125rem",
      "xl": "1.25rem",
      "2xl": "1.5rem",
      "3xl": "1.875rem",
      "4xl": "2.25rem",
      "5xl": "3rem"
    },
    "fontWeight": {
      "light": 300,
      "normal": 400,
      "medium": 500,
      "semibold": 600,
      "bold": 700,
      "extrabold": 800
    },
    "lineHeight": {
      "tight": 1.25,
      "normal": 1.5,
      "relaxed": 1.75,
      "loose": 2
    }
  },
  "spacing": {
    "unit": "0.25rem",
    "scale": {
      "0": "0",
      "1": "0.25rem",
      "2": "0.5rem",
      "3": "0.75rem",
      "4": "1rem",
      "5": "1.25rem",
      "6": "1.5rem",
      "8": "2rem",
      "10": "2.5rem",
      "12": "3rem",
      "16": "4rem",
      "20": "5rem",
      "24": "6rem"
    }
  },
  "borderRadius": {
    "none": "0",
    "sm": "0.125rem",
    "base": "0.25rem",
    "md": "0.375rem",
    "lg": "0.5rem",
    "xl": "0.75rem",
    "2xl": "1rem",
    "3xl": "1.5rem",
    "full": "9999px"
  },
  "shadows": {
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "base": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
  }
}
```

## Format 2: CSS Custom Properties

```css
:root {
  /* Colors */
  --color-primary: #0066CC;
  --color-primary-light: #3384D6;
  --color-primary-dark: #004C99;
  --color-secondary: #6C757D;
  --color-success: #28A745;
  --color-warning: #FFC107;
  --color-error: #DC3545;
  
  /* Typography */
  --font-family-base: 'Inter', sans-serif;
  --font-family-heading: 'Poppins', sans-serif;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;
  --font-weight-normal: 400;
  --font-weight-bold: 700;
  
  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  
  /* Effects */
  --border-radius: 0.25rem;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

## Format 3: SCSS Variables

```scss
// Colors
$color-primary: #0066CC;
$color-primary-light: #3384D6;
$color-primary-dark: #004C99;
$color-secondary: #6C757D;
$color-success: #28A745;
$color-warning: #FFC107;
$color-error: #DC3545;

// Typography
$font-family-base: 'Inter', sans-serif;
$font-family-heading: 'Poppins', sans-serif;
$font-size-base: 1rem;
$font-weight-normal: 400;
$font-weight-bold: 700;

// Spacing Scale
$spacing-unit: 0.25rem;
$spacing: (
  'xs': $spacing-unit,
  'sm': $spacing-unit * 2,
  'md': $spacing-unit * 4,
  'lg': $spacing-unit * 6,
  'xl': $spacing-unit * 8
);

// Border Radius
$border-radius: 0.25rem;
$border-radius-lg: 0.5rem;

// Shadows
$shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
$shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
```

## Format 4: Simple List (Text Description)

```
Primary Color: #0066CC (blue)
Secondary Color: #6C757D (gray)
Success Color: #28A745 (green)
Error Color: #DC3545 (red)

Heading Font: Poppins
Body Font: Inter

Base Font Size: 16px
Large Font Size: 20px
```

## Format 5: Tailwind Config

```javascript
module.exports = {
  theme: {
    colors: {
      primary: {
        DEFAULT: '#0066CC',
        light: '#3384D6',
        dark: '#004C99'
      },
      secondary: {
        DEFAULT: '#6C757D',
        light: '#ADB5BD',
        dark: '#495057'
      },
      gray: {
        50: '#F8F9FA',
        100: '#E9ECEF',
        200: '#DEE2E6',
        300: '#CED4DA',
        400: '#ADB5BD',
        500: '#6C757D',
        600: '#495057',
        700: '#343A40',
        800: '#212529',
        900: '#000000'
      }
    },
    fontFamily: {
      sans: ['Inter', 'system-ui', 'sans-serif'],
      serif: ['Georgia', 'serif'],
      mono: ['Fira Code', 'monospace']
    },
    fontSize: {
      xs: '0.75rem',
      sm: '0.875rem',
      base: '1rem',
      lg: '1.125rem',
      xl: '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem'
    }
  }
}
```

## Mapping Old Theme to New Theme

### Example: Color Mapping
```
Old Theme → New Theme
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#FF6B35 → #0066CC (Primary)
#004E89 → #6C757D (Secondary)
#F7B801 → #FFC107 (Accent/Warning)
#00A8E8 → #17A2B8 (Info)
#333333 → #212529 (Text Dark)
#666666 → #6C757D (Text Muted)
#FAFAFA → #F8F9FA (Background Light)
```

### Example: Typography Mapping
```
Old → New
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'Montserrat' → 'Poppins' (Headings)
'Open Sans' → 'Inter' (Body)
'Courier New' → 'Fira Code' (Code)

Font Size Scale:
14px → 0.875rem (14px)
16px → 1rem (16px)
18px → 1.125rem (18px)
20px → 1.25rem (20px)
```

## Incomplete Theme Handling

If user provides incomplete information, ask for specifics:

**Missing Colors**:
- "I found 3 shades of blue in the current theme. Should they all map to your primary color #0066CC, or do you have light/dark variants?"
- "What should replace the accent color #F7B801?"

**Missing Typography**:
- "What font family should replace 'Montserrat'?"
- "Should I maintain the same font size scale or adjust it?"

**Missing Spacing**:
- "Should spacing stay the same, or would you like to scale it? (e.g., 1.2x larger)"

## Color Grouping Strategy

When source stylesheet has many similar colors:
```
Found similar shades that could map to primary:
- #0056B3 (used 12 times)
- #0060C0 (used 8 times)
- #0066CC (used 5 times)
- #0062C7 (used 3 times)

Suggestion: Group all as Primary (#0066CC)
Confirm? [Yes / No / Specify different mapping]
```

## Semantic Color Preservation

Maintain semantic meaning across themes:
```
State Colors:
- Success/Positive → Green spectrum
- Warning/Caution → Yellow/Orange spectrum
- Error/Danger → Red spectrum
- Info/Neutral → Blue/Gray spectrum
```

## Accessibility Considerations in Theme Definition

When defining themes, ensure:
1. **Sufficient Contrast**: Background-to-text contrast ≥ 4.5:1 (AA)
2. **Focus Indicators**: Clear, visible focus states
3. **Interactive States**: Hover/active states meet contrast requirements
4. **Color Independence**: Don't rely solely on color for meaning

Example good pairing:
```
✅ PASS: #FFFFFF text on #0066CC background = 7.04:1
✅ PASS: #212529 text on #FFFFFF background = 16.12:1
❌ FAIL: #6C757D text on #FFFFFF background = 4.24:1 (below 4.5:1)
```
