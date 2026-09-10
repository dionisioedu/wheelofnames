# Engagement analytics

`engagement.js` adds privacy-safe engagement events to the existing Google
Analytics tag. It does not create pageviews and silently does nothing until the
existing cookie consent (`wol_consent_v1`) has been accepted or when `gtag` is
unavailable.

## Events

| Event | Safe parameters | Trigger |
| --- | --- | --- |
| `wheel_spin_start` | `item_count` | A valid wheel spin starts |
| `wheel_result` | `item_count`, `remaining_count` | A result is added to the scoreboard |
| `wheel_items_update` | `item_count` | The wheel list is applied |
| `wheel_save` | `item_count` | A named wheel is saved locally |
| `wheel_share` | `method` | Native share or clipboard fallback succeeds |
| `wheel_image_download` | none | A result image is generated for download |
| `theme_change` | `theme` | Light/dark theme changes |
| `tool_navigation` | `tool`, `source` | Navigation to a tool or hub |
| `template_open` | `template`, `source` | A wheel template link is opened |
| `tool_action` | `tool`, `action` | A primary action runs on a tool page |

Only allowlisted numbers and short categorical values are accepted. Names,
wheel items, winners, saved-wheel names, clipboard contents, URLs with query
parameters and other free text must never be passed to this helper.
