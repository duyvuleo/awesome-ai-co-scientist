# Explore the collection

[Open the explorer](https://duyvuleo.github.io/awesome-ai-co-scientist/) · [Repository](../README.md) · [Data reference](data-reference.md) · [Implementation guide](explorer-development.md)

The explorer combines a clickable theme cloud, a resource graph, and a filtered reading list. Select one or more themes, narrow the year/domain/resource filters, or inspect a work to see its records and sources. The graph uses the full width until a work is selected; closing the details restores it. Use **Table / Cards** to compare compact rows or read full summaries in a responsive card grid. Both views retain the same filters, ordering, member records, and evidence links. Table is the default; `view=cards` preserves the card view in shared URLs. The URL preserves the current selection for sharing. JSON export retains full records and source links.

## Reading the visuals

| Element | Meaning |
| --- | --- |
| Word size and count | Number of matching **grouped works** carrying a theme, counted once per work. The cloud shows up to 26 leading themes (16 on narrow screens); the expanded list includes all matches. |
| Work node | Records sharing a verified primary identity, using the same conservative grouping rules as Recent additions. Color and shape follow the main record, usually the paper. All member records remain accessible in the inspector. |
| Theme circle and link | An outer circle represents a normalized catalog tag; its size and number show matching works. A line connects it to an inner work node. Shared tags indicate topical association, not citation, influence, or experimental support. |
| Related catalog entries | Navigation links in work details. They are not drawn as graph edges because `related` does not specify a research relationship. |
| Code filter | A code or repository link is recorded. It does not establish a complete runnable implementation or unrestricted access. |
| Capability evidence | Source-backed comparison cells for system records, with their evidence basis, limitations, and citations. Source inspection is not independent execution. |

Work names remain visible as more themes are selected. Use **Show labels** to hide or restore them in a dense view; theme names stay visible, and hovering still reveals the full work name. The URL preserves this preference.

Hover over a node to highlight its connections. Use **Find a work in the graph** and **Inspect work** to open sources through the keyboard-accessible selector. The toolbar reports the visible graph counts; **Reset view** fits the graph and restores the displayed zoom to 100%.

Node placement is a reading aid, not a similarity score. The graph shows up to ten leading theme hubs for readability. Selected themes become graph hubs. **Match any** includes works carrying at least one selected theme; **Match all** requires every selected theme. Select a theme again to remove it, or use **Clear themes**. The full filtered set of works remains in the table, including isolated nodes. **Focus neighborhood** retains the selected work and works sharing any of its themes. Other filters continue to apply.

The former Catalog relationships view has been removed. Its generic cross-references did not explain whether a work extended, evaluated, or implemented another. Existing `mode=catalog` URLs now open the theme graph while preserving the other filters.

Resource, year, and code filters must be satisfied by the same member record. The displayed date belongs to the main record; dates for each system, tool, and benchmark appear in the inspector. Cloud counts respond to the other filters but ignore the selected themes, making alternative themes easy to select.

## Data and maintenance

The canonical catalogs remain in `data/`. [explorer-taxonomy.json](../data/explorer-taxonomy.json) defines a small, explicit set of tag aliases and excludes availability/administrative tags from the cloud. Original tags are preserved in each record. The cloud describes this collection’s coverage, not the importance or prevalence of themes across the entire research field.

`python3 scripts/render.py` regenerates the Markdown views, `site/data.json`, and `assets/explorer-preview.svg`. The preview is a static sample of actual theme associations; the site contains the full graph. `--check` detects stale output, so ordinary catalog updates refresh the explorer through the existing rendering step.

The site uses local HTML, CSS, JavaScript, and a pinned MIT-licensed [Cytoscape.js](https://js.cytoscape.org/) distribution. It requires no model service, database, tracking scripts, or runtime CDN. The accessible HTML table and theme buttons provide alternatives to the canvas graph. GitHub Pages hosts the published site under GitHub’s normal hosting policies.

## Local preview and checks

```bash
python3 scripts/render.py
python3 scripts/validate.py
python3 scripts/render.py --check
python3 -m unittest discover -s tests -v
node --test tests/explorer.test.mjs
python3 -m http.server 8768 --bind 127.0.0.1 --directory site
```

Open `http://127.0.0.1:8768/`. Serve the directory over HTTP; opening `index.html` directly as a file does not support the data request consistently across browsers.

The deployment workflow validates the catalog and generated data, runs the offline tests, and publishes only `site/`. Dated research reports and local experiment artifacts are never copied into the site.
