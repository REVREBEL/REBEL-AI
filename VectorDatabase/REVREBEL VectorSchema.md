## persona_revrebel Schema 

<br>

| Field Name       | Field Type              | Nullable | Default Value | Description                                                       | Index |
| ---------------- | ----------------------- | :------: | ------------- | ----------------------------------------------------------------- | :---: |
| primary_key (PK) | VARCHAR (128)           |    No    | —             | The Primary Key                                                   |       |
| vector           | FLOAT_VECTOR (156)      |    No    | —             | —                                                                 |   ✅   |
| persona_id       | VARCHAR (32)            |    No    | —             | Unique persona identifier (e.g., revrebel_core, revrebel_founder) |       |
| persona_version  | VARCHAR (32)            |    No    | —             | Semantic version (e.g., v2.0, v2.1-experimental)                  |   ✅   |
| module           | VARCHAR (64)            |    No    | —             | Top-level module (Brand Core, Brand Voice & Style, etc.)          |   ✅   |
| submodule        | VARCHAR (64)            |    No    | —             | Specific submodule within module                                  |   ✅   |
| status           | VARCHAR (14)            |    No    | —             | active, deprecated, or draft                                      |   ✅   |
| tone             | ARRAY<VARCHAR (24)>[10] |    Yes   | —             | Tone descriptors (e.g., witty, confident, rebellious)             |   ✅   |
| use_case         | VARCHAR (64)            |    Yes   | —             | Primary application context                                       |   ✅   |
| audience         | ARRAY<VARCHAR (32)>[10] |    Yes   | —             | Target audience                                                   |   ✅   |
| platform         | ARRAY<VARCHAR (24)>[8]  |    Yes   | —             | Sub-platform (e.g., linkedin under social)                        |   ✅   |
| channel          | ARRAY<VARCHAR (24)>[8]  |    Yes   | —             | Specific channel (LinkedIn, Blog, Email, etc.)                    |   ✅   |
| severity         | VARCHAR (10)            |    Yes   | —             | Rule importance (must, should, prefer, avoid, never)              |       |
| author           | VARCHAR (32)            |    Yes   | REVREBEL      | Creator identifier                                                |       |
| language         | VARCHAR (2)             |    Yes   | en            | Content language (default: en)                                    |       |
| created_ym       | VARCHAR (8)             |    No    | —             | Creation date (YYYY-MM format)                                    |       |
| confidence_score | FLOAT                   |    Yes   | —             | Certainty level (0.0–1.0)                                         |   ✅   |
| weight           | FLOAT                   |    Yes   | —             | Importance weighting (0.0–1.0)                                    |   ✅   |
| dynamic field    | —                   |     —    | —             | Flexible fields for evolving metadata                     |       |

<br> 
<br> 

## prod\_asset_embeddings Schema 

<br>

| Field Name       | Field Type              | Nullable | Default Value | Description                                               | Index |
| ---------------- | ----------------------- | :------: | ------------- | --------------------------------------------------------- | :---: |
| primary_key (PK) | VARCHAR (128)           |    No    | —             | The Primary Key                                           |       |
| vector           | FLOAT_VECTOR (156)      |    No    | —             | —                                                         |   ✅   |
| domain           | VARCHAR (32)            |    No    | —             | Primary content category (e.g., coding, design, strategy) |   ✅   |
| asset_type       | VARCHAR (32)            |    Yes   | —             | Type of asset (logo, photo, graphic, video, audio)        |   ✅   |
| format           | VARCHAR (4)             |    Yes   | —             | File format (png, svg, jpg, ttf, mp4, wav, pdf)           |   ✅   |
| visual_tags      | ARRAY<VARCHAR (16)>[10] |    Yes   | —             | Visual characteristics (e.g., ["geometric","bold"])       |   ✅   |
| color_palette    | ARRAY<VARCHAR (7)>[20]  |    Yes   | —             | Dominant colors (e.g., ["#163666","#047C97"])             |       |
| style_era        | ARRAY<VARCHAR (32)>[6]  |    Yes   | —             | Design era (e.g., "arcade","retro-future")                |       |
| variant          | VARCHAR (32)            |    Yes   | —             | Asset variant (primary, secondary, icon, stacked, circle) |   ✅   |
| approval_status  | VARCHAR (12)            |    Yes   | —             | Approval state (approved, review, draft)                  |   ✅   |
| last_updated     | VARCHAR (11)            |    No    | —             | Last date updated in yyyy-MM-dd format                    |       |
| created_ym       | VARCHAR (8)             |    No    | —             | Creation month in yyyy-MM format                          |   ✅   |
| dynamic field     | —                   |     —    | —             | Flexible fields for evolving metadata                     |       |

<br> 
<br> 

## prod\_doc\_search Schema

<br> 

| Field Name       | Field Type          | Nullable | Default Value | Description                                               | Index |
| ---------------- | ------------------- | :------: | ------------- | --------------------------------------------------------- | :---: |
| primary_key (PK) | VARCHAR (128)       |    No    | —             | Primary Key                                               |       |
| vector           | FLOAT_VECTOR (1536) |    No    | —             | Vector                                                    |   ✅   |
| domain           | VARCHAR (32)        |    No    | —             | Primary content category (e.g., coding, design, strategy) |   ✅   |
| program          | VARCHAR (64)        |    Yes   | —             | System or app area (e.g., webflow, budibase, n8n)         |   ✅   |
| artifact_type    | VARCHAR (64)        |    Yes   | —             | Content type (e.g., howto, checklist, prompt)             |   ✅   |
| created_ym       | VARCHAR (8)         |    No    | —             | Creation month (YYYY-MM)                                  |   ✅   |
| dynamic field | —                   |     —    | —             | Flexible fields for evolving metadata                     |       |

<br> 
<br> 

## prod_recommendations Schema

<br> 

| Field Name       | Field Type              | Nullable | Default Value | Description                                                       | Index |
| ---------------- | ----------------------- | :------: | ------------- | ----------------------------------------------------------------- | :---: |
| primary_key (PK) | VARCHAR (128)           |    No    | —             | The Primary Key                                                   |       |
| vector           | FLOAT_VECTOR (156)      |    No    | —             | —                                                                 |   ✅   |
| persona_id       | VARCHAR (32)            |    No    | —             | Unique persona identifier (e.g., revrebel_core, revrebel_founder) |       |
| persona_version  | VARCHAR (32)            |    No    | —             | Semantic version (e.g., v2.0, v2.1-experimental)                  |   ✅   |
| module           | VARCHAR (64)            |    No    | —             | Top-level module (Brand Core, Brand Voice & Style, etc.)          |   ✅   |
| submodule        | VARCHAR (64)            |    No    | —             | Specific submodule within module                                  |   ✅   |
| status           | VARCHAR (14)            |    No    | —             | active, deprecated, or draft                                      |   ✅   |
| tone             | ARRAY<VARCHAR (24)>[10] |    Yes   | —             | Tone descriptors (e.g., witty, confident, rebellious)             |   ✅   |
| use_case         | VARCHAR (64)            |    Yes   | —             | Primary application context                                       |   ✅   |
| audience         | ARRAY<VARCHAR (32)>[10] |    Yes   | —             | Target audience                                                   |   ✅   |
| platform         | ARRAY<VARCHAR (24)>[8]  |    Yes   | —             | Sub-platform (e.g., linkedin under social)                        |   ✅   |
| channel          | ARRAY<VARCHAR (24)>[8]  |    Yes   | —             | Specific channel (LinkedIn, Blog, Email, etc.)                    |   ✅   |
| severity         | VARCHAR (10)            |    Yes   | —             | Rule importance (must, should, prefer, avoid, never)              |       |
| author           | VARCHAR (32)            |    Yes   | REVREBEL      | Creator identifier                                                |       |
| language         | VARCHAR (2)             |    Yes   | en            | Content language (default: en)                                    |       |
| created_ym       | VARCHAR (8)             |    No    | —             | Creation date (YYYY-MM format)                                    |       |
| confidence_score | FLOAT                   |    Yes   | —             | Certainty level (0.0–1.0)                                         |   ✅   |
| weight           | FLOAT                   |    Yes   | —             | Importance weighting (0.0–1.0)                                    |   ✅   |
| dynamic field    | —                   |     —    | —             | Flexible fields for evolving metadata                     |       |