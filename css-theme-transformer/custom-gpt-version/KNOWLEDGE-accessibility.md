# Accessibility Standards for CSS Theme Transformation

## WCAG Color Contrast Requirements

### Contrast Ratio Standards

**WCAG 2.1 Level AA (Minimum)**:
- Normal text (< 18pt or < 14pt bold): **4.5:1**
- Large text (≥ 18pt or ≥ 14pt bold): **3:1**

**WCAG 2.1 Level AAA (Enhanced)**:
- Normal text: **7:1**
- Large text: **4.5:1**

**WCAG 3.0 (APCA) - Future Standard**:
- Uses Advanced Perceptual Contrast Algorithm
- Context-dependent thresholds
- More nuanced than simple ratios

### Calculating Contrast Ratios

**Formula**:
```
contrast ratio = (L1 + 0.05) / (L2 + 0.05)
where:
- L1 is the relative luminance of the lighter color
- L2 is the relative luminance of the darker color
- Luminance ranges from 0 (black) to 1 (white)
```

**Relative Luminance Calculation**:
```
For RGB values (0-255), convert to sRGB:
1. Divide by 255: R/255, G/255, B/255
2. For each channel (Rc, Gc, Bc):
   if channel ≤ 0.03928:
     channel = channel / 12.92
   else:
     channel = ((channel + 0.055) / 1.055) ^ 2.4
3. L = 0.2126 * R + 0.7152 * G + 0.0722 * B
```

### Examples with Calculations

**Example 1: White text on blue background**
```
Text: #FFFFFF (RGB 255, 255, 255) → L = 1.0
Background: #0066CC (RGB 0, 102, 204) → L ≈ 0.142
Contrast: (1.0 + 0.05) / (0.142 + 0.05) = 5.47:1
Result: ✅ PASS AA (needs 4.5:1), ❌ FAIL AAA (needs 7:1)
```

**Example 2: Dark gray text on white**
```
Text: #333333 (RGB 51, 51, 51) → L ≈ 0.0146
Background: #FFFFFF (RGB 255, 255, 255) → L = 1.0
Contrast: (1.0 + 0.05) / (0.0146 + 0.05) = 16.24:1
Result: ✅ PASS AAA (excellent contrast)
```

**Example 3: Gray text on light gray - FAIL**
```
Text: #999999 (RGB 153, 153, 153) → L ≈ 0.262
Background: #F5F5F5 (RGB 245, 245, 245) → L ≈ 0.913
Contrast: (0.913 + 0.05) / (0.262 + 0.05) = 3.09:1
Result: ❌ FAIL AA (needs 4.5:1)
Fix: Darken text to #767676 for 4.54:1 ratio
```

## Common Contrast Issues in Theming

### Issue 1: Light Colors on White
```
❌ #FFC107 (yellow/warning) on #FFFFFF = 1.74:1 (FAIL)
✅ Fix: Add dark text color or use #856404 = 4.52:1
```

### Issue 2: Pastels with Poor Contrast
```
❌ #B8E6F0 (light blue) on #FFFFFF = 1.28:1 (FAIL)
✅ Fix: Use darker shade #0891B2 = 4.51:1
```

### Issue 3: Gray Scale Insufficient Differentiation
```
❌ #CCCCCC text on #F0F0F0 = 1.92:1 (FAIL)
✅ Fix: Darken to #707070 for 4.51:1
```

## Auto-Fix Strategies

### Strategy 1: Darken Light Text
When light text on light background fails:
```python
1. Calculate current luminance of text
2. Find target luminance for 4.5:1 ratio
3. Darken text color iteratively until ratio met
4. Preserve hue and saturation when possible
```

Example:
```
Original: #999999 on #FFFFFF = 3.09:1 ❌
Darkened: #767676 on #FFFFFF = 4.54:1 ✅
```

### Strategy 2: Lighten Dark Backgrounds
When dark text on dark background fails:
```python
1. Calculate current luminance of background
2. Find target luminance for 4.5:1 ratio
3. Lighten background iteratively until ratio met
4. Preserve hue and saturation when possible
```

Example:
```
Original: #333333 text on #555555 = 1.86:1 ❌
Lightened: #333333 text on #AAAAAA = 4.51:1 ✅
```

### Strategy 3: Increase Saturation
For muted colors that fail contrast:
```
Original: hsl(210, 20%, 60%) on white = 2.8:1 ❌
Increased: hsl(210, 50%, 45%) on white = 4.52:1 ✅
```

## Special Considerations

### Gradients
Ensure text contrast meets standards at ALL gradient stops:
```css
/* ❌ BAD: Text may fail contrast at gradient midpoint */
background: linear-gradient(to right, #0066CC, #FFFFFF);
color: #FFFFFF;

/* ✅ GOOD: Text maintains contrast across entire gradient */
background: linear-gradient(to right, #0066CC, #004C99);
color: #FFFFFF;
```

### Transparent Colors
Account for transparency in contrast calculations:
```
rgba(0, 102, 204, 0.8) on white:
1. Calculate resulting composite color
2. Composite = (fg × alpha) + (bg × (1 - alpha))
3. Then calculate contrast of composite vs text
```

### Hover/Focus States
Interactive states must also meet contrast requirements:
```css
.button {
  background: #0066CC;
  color: #FFFFFF; /* 7.04:1 ✅ */
}
.button:hover {
  background: #3384D6; /* Must still be ≥4.5:1 */
  color: #FFFFFF; /* 5.12:1 ✅ */
}
```

## Testing Tools Reference

### Automated Checks
- WebAIM Contrast Checker
- Chrome DevTools Accessibility panel
- axe DevTools browser extension
- Lighthouse accessibility audit

### Manual Verification
Verify in actual browser rendering, not just calculations:
- Font smoothing affects perceived contrast
- Different displays render colors differently
- Operating system font rendering varies

## Color Blindness Considerations

### Deuteranopia (Red-Green)
- Don't rely solely on red/green for success/error
- Use additional indicators (icons, patterns, text labels)
- Test with color blindness simulators

### Protanopia (Red-Weak)
- Similar to deuteranopia
- Red colors appear darker
- Ensure sufficient contrast even with red perception loss

### Tritanopia (Blue-Yellow)
- Blue/yellow distinction difficult
- Use additional cues beyond color

### Achromatopsia (Total Color Blindness)
- See only grayscale
- Contrast ratios become critical
- All information must be conveyed through contrast alone

## Theme Transformation Accessibility Checklist

When transforming themes, verify:

✅ **All text** meets minimum 4.5:1 contrast (AA)
✅ **Large text** meets minimum 3:1 contrast (AA)
✅ **Links** are distinguishable from surrounding text (not just by color)
✅ **Focus indicators** are clearly visible (3:1 contrast with background)
✅ **Hover states** maintain required contrast
✅ **Disabled states** are visually distinct (but contrast rules relaxed)
✅ **Icons** have sufficient contrast if conveying information
✅ **Form inputs** have clear boundaries (3:1 contrast for borders)

## When to Flag for Manual Review

Flag accessibility issues that can't be auto-fixed:
- Custom gradients with multiple stops
- Background images with text overlay
- SVG fills that aren't easily adjustable
- Complex color schemes where semantic meaning would be lost
- Brand colors that are specifically required but fail contrast

## Reporting Accessibility Issues

Format for reporting:
```
🔴 CRITICAL: [count] AA violations
Element: .btn-secondary
Current: #6C757D text on #E9ECEF background = 2.97:1
Required: 4.5:1 (AA normal text)
Fix: Darken text to #495057 for 4.62:1 ✅

🟡 WARNING: [count] AAA violations  
Element: .card-subtitle
Current: #6C757D text on #FFFFFF = 4.24:1
Passes: AA (4.5:1) ✅
Fails: AAA (7:1) ❌
Fix: Darken to #3C4247 for 7.05:1 (optional)
```

## Resources

- WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Accessible Colors: https://accessible-colors.com/
- Contrast Ratio: https://contrast-ratio.com/
- Color Review: https://color.review/
