# Building the collection explorer

[Live explorer](https://duyvuleo.github.io/awesome-ai-co-scientist/) · [Reader guide](explorer.md) · [Data reference](data-reference.md)

The explorer provides three views of the same catalog: a theme cloud, a graph, and a reading table. Python generates the public dataset; browser JavaScript handles filtering and interaction. This separates source records from presentation and lets contributors reproduce the site without a database, model API, or frontend build service.

## Architecture

| Component | Implementation | Responsibility |
| --- | --- | --- |
| Catalogs | [papers.json](../data/papers.json), [systems-tools.json](../data/systems-tools.json), [benchmarks.json](../data/benchmarks.json) | Resource identities, summaries, dates, tags, and primary sources. |
| Evidence matrix | [comparisons.json](../data/comparisons.json) | System capabilities, evidence bases, source locators, and limitations. |
| Theme vocabulary | [explorer-taxonomy.json](../data/explorer-taxonomy.json) | Explicit aliases, display labels, and excluded administrative tags. |
| Identity and ordering | [catalog.py](../scripts/catalog.py) | Shared identity rules, conservative work grouping, and date ordering. |
| Data generation | [explorer_data.py](../scripts/explorer_data.py) | Builds grouped works, preserves member records, and derives themes and catalog links. |
| Rendering entry point | [render.py](../scripts/render.py) | Writes Markdown views, `site/data.json`, and `assets/explorer-preview.svg`; checks for stale generated files. |
| Selection model | [model.mjs](../site/model.mjs) | Pure functions for filters, counts, graph elements, URL state, and exports. |
| Graph layout | [graph-layout.mjs](../site/graph-layout.mjs) | Deterministic outer theme hubs and inner work rings, with a narrower arrangement for small containers. |
| Interface | [index.html](../site/index.html), [styles.css](../site/styles.css), [app.mjs](../site/app.mjs) | Renders controls, cloud, graph, table, and selected-work details. |
| Graph renderer | [Vendored Cytoscape.js](../site/vendor/README.md) | Draws nodes and edges and handles graph interaction. Version 3.34.4 is pinned locally with its MIT license. |
| Publication | [pages.yml](../.github/workflows/pages.yml) | Checks the generated site and uploads only `site/` to GitHub Pages. |

The stylesheet, application module, and imported model module use versioned asset URLs. When changing their interface together, update these URL versions together to avoid mixing cached releases.

There is no bundler or package installation step. The browser fetches `./data.json` once, then filters it locally. JavaScript modules and the graph library are served with the site; fonts use local system families. External paper and repository links open only when followed.

## From records to works

`build_payload()` in `explorer_data.py` reuses `recent_groups()` from the catalog renderer. A record's grouping key is its `paper_url`, falling back to `url`, normalized through `canonical_identity()`.

| Rule | Consequence |
| --- | --- |
| Known arXiv, DOI, and GitHub URL aliases share an identity. | Alternate URL forms do not create extra work nodes. |
| A group may contain one record of each resource kind. | A paper, implementation, and benchmark can share a node while retaining separate records. |
| A bucket containing repeated kinds is ambiguous. | Every record in that bucket remains separate. |
| A paper is preferred as the main record. | Its ID, title, summary, and date represent the work; member metadata remains available. |
| Titles, shared tags, citations in `sources`, and `related` links are not identity keys. | Similar names or research topics do not cause automatic merging. |

Grouping is a conservative presentation rule, not a claim that all versions or releases are equivalent. See the [identity rules](data-reference.md#catalog-field-meanings) for supported normalization and unresolved cases.

The generated payload uses `schema_version: 1`:

| Field | Contents |
| --- | --- |
| `records` | Every original catalog record, augmented with `work_id`, `catalog_url`, and extracted `code_links`. |
| `works` | Main-record metadata, member `entry_ids`, normalized themes, and aggregate resource kinds, years, and code availability. |
| `themes` | Stable tag IDs, display labels, and counts of distinct grouped works. |
| `relations` | Undirected cross-work navigation associations for the inspector, with original `entry_pairs` retained for traceability. They are not graph edges. |
| `comparisons` | System comparison records, including sources and evidence qualifications. |
| `checked`, `counts`, `repository` | Latest recorded source-check date, per-kind record counts, and repository URL. `checked` does not mean every source was reviewed on that date. |

Generation preserves original tags and sources. Within-work cross-references are omitted from `relations` because their records already share a node. Reciprocal cross-work links become one navigation association. The inspector retains these links; the graph does not draw them.

## Constructing the visuals

| View | Construction | Interpretation |
| --- | --- | --- |
| Theme cloud | Exclude administrative tags, apply explicit aliases, and count each resulting theme once per work. Font size follows `14 + 22 × sqrt(count / maximum count)` before narrow-screen styling. | Size represents coverage in this collection, not research quality or field-wide importance. |
| Theme graph | Add work nodes and up to ten leading theme hubs; connect each hub to works carrying that tag. Selected themes show their matching hubs. | Solid, faint edges express theme membership; hover and selection highlight connected nodes. |
| Node layout | `graph-layout.mjs` places theme hubs on an outer ellipse and works on inner rings. More than 45 works use two staggered rings. Theme diameter grows with the square root of the matching-work count. | Positions and distances do not encode semantic similarity. |
| Reading table | Render every filtered work in the chosen order, including isolated graph nodes. | The table provides a text-based route to the same records and sources. |
| README preview | `preview_svg()` draws the leading themes and a small sample of actual theme associations. | A generated overview, not a screenshot or a complete graph. |

The radial layout and muted-edge interaction follow [Awesome Agents That Learn](https://duyvuleo.github.io/awesome-agents-that-learn/). This explorer retains grouped-work identities, its existing color-scheme support, and explicit label control. Work placement is deterministic within a filtered set and independent of reading-list order.

The cloud shows up to 26 themes on larger screens and 16 on narrow screens, with all counts available in an expandable list. Work labels are visible by default at every collection size. The **Show labels** checkbox hides or restores work labels without changing the current zoom or pan; theme names remain visible. Hovering reveals full names and selection opens details. The table retains every filtered work.

The toolbar reports visible works, theme hubs, membership links, and zoom relative to the fitted view. **Reset view** fits the current graph. The **Find a work in the graph** selector highlights a work; **Inspect work** opens its evidence panel without requiring a canvas click.

The graph occupies the full row until a work is selected. Selection opens the inspector; closing it or pressing Escape restores the width. A visibility change rebuilds the graph for its new dimensions. On narrow screens, details appear below the graph.

## Interaction and state

`model.mjs` contains the selection logic independently of the DOM and graph library. `app.mjs` renders its results and updates the query string with `history.replaceState()`.

| State | Behavior |
| --- | --- |
| `q` | Case-insensitive search across member names, IDs, summaries, and original tags; all whitespace-separated terms must match. |
| `kind`, `year`, `code=1` | One member record must satisfy these filters together. A paper's year cannot be combined with a different member's code link to create a match. |
| `domain`, `theme`, `match` | Match normalized work themes. Repeated `theme` parameters select multiple themes; `match=any` (default) accepts at least one, while `match=all` requires every selected theme. Cloud counts ignore the theme selection but retain the other filters; selected themes with no matches remain removable. |
| `view=cards` | Show full summaries in a responsive card grid. Table is the default. Switching views leaves filters, sort order, selected work, exports, and graph zoom unchanged. |
| `labels=0` | Hide work labels; the default shows them regardless of the number of matching works. The preference survives filtering and shared URLs. Reset restores visible labels. |
| Legacy `mode` | Ignored and removed from the URL. Former catalog views open the theme graph with the other filters preserved. |
| `selected` | Open a work's details. A member record ID resolves to its work; a selection outside the filtered results is cleared. |
| `focus` | Restrict to the selected work and works sharing any theme, even one omitted from the ten visible hubs. Generic catalog links do not establish topical neighbors. Other filters still apply. |
| `sort` | Newest first by default; `oldest` reverses the generated order, and `name` sorts alphabetically. |

For example, `?theme=ideation` opens the ideation view; `?theme=ideation&theme=verification&match=all` requires both themes. Single-theme links remain compatible. Default and empty values are omitted from shared URLs. Unknown resource IDs and unsupported filter values are normalized rather than trusted.

JSON export includes all member records for the selected works, their original sources, the source-check date, and a scope statement. It does not export the capability matrix or constitute a report of executed experiments.

## Reproduce the build

Run from the repository root. Python 3.10 or newer supports catalog generation; the Pages workflow uses Python 3.12 and Node.js 22. Node is used for tests, not to serve or bundle the site.

```bash
python3 scripts/render.py
python3 scripts/validate.py
python3 scripts/render.py --check
python3 scripts/build_visuals.py --check
python3 -m unittest discover -s tests -v
node --test tests/explorer.test.mjs
node --check site/app.mjs
python3 -m http.server 8768 --bind 127.0.0.1 --directory site
```

Open `http://127.0.0.1:8768/`. Use HTTP rather than opening `index.html` directly, so the JSON request works consistently. Stop the preview server with Ctrl+C. Edit source catalogs or generation code rather than `site/data.json` and `assets/explorer-preview.svg` directly.

## Verification

| Check | What it establishes |
| --- | --- |
| [Python explorer tests](../tests/test_explorer_data.py) | Record conservation, grouping counts, preserved sources and original tags, relationship semantics, deterministic data, and valid SVG output. |
| [JavaScript model tests](../tests/explorer.test.mjs) | Combined filters, empty results, valid graph endpoints, URL round trips, member-ID resolution, theme neighborhoods, legacy URL compatibility, exclusion of catalog links from graph edges, source-preserving export, and deterministic radial coordinates for desktop and narrow containers. |
| Catalog validation and render checks | Valid catalog structure and links within Markdown, plus consistency between source data and committed generated views. |
| Browser checks | Layout and interaction behavior that pure model tests do not exercise. |

For interface changes, check multiple theme selections in both match modes, individual removal and clearing, combined filters, an empty result, work selection and dismissal, a shared URL, and JSON export. Inspect both desktop and narrow layouts, including document overflow. Confirm that the graph expands after closing details and that the table remains usable without relying on canvas labels.

Automated model tests do not establish visual correctness, scientific validity, source availability, or complete accessibility conformance. External-link checks are separate from local rendering checks.

## Deployment and extension

GitHub Pages uses the repository's **GitHub Actions** publishing source. The Pages workflow runs on pushes to `main` affecting `site/`, `data/`, `scripts/`, `tests/`, or the workflow itself; it also supports manual dispatch. It validates the catalog, checks generated outputs, runs Python and JavaScript tests, and uploads `site/`. A separate deployment job publishes that artifact using `pages: write` and `id-token: write`. Documentation-only commits do not trigger a Pages deployment.

The general [validation workflow](../.github/workflows/validate.yml) runs on pushes and pull requests. Generated outputs must be committed before publication: deployment checks them but does not regenerate them. Research reports and local artifacts are not included in the uploaded site directory.

| Intended change | Where to work |
| --- | --- |
| Add or correct a resource | Source catalogs, then run `render.py`. |
| Merge synonymous themes or change labels | `explorer-taxonomy.json`, with examples verifying counts and preserved original tags. |
| Add a filter or export field | Pure functions in `model.mjs`, model tests, then controls in `app.mjs` and `index.html`. |
| Change layout or selection behavior | `graph-layout.mjs`, `app.mjs`, and `styles.css`, followed by browser checks. |
| Add citation or derivation edges | Extend the data model with explicit relation types and supporting evidence before changing the graph. |
| Upgrade the graph library | Replace the pinned vendor distribution, preserve its license, update the script integrity value in `index.html`, and verify interactions. |

The initial Catalog relationships view used generic `related` links. Most links joined records already grouped into one work, while the remaining links lacked a specific research meaning. This mode was removed rather than treating navigation metadata as a research graph. Adding relations such as “evaluated on” or “extends” requires a relation type, direction, primary source, and an evidence locator for each claim.

The current graph has no citation harvesting, embeddings, inferred influence scores, or learned topic extraction. Those would require additional sources, validation, and explicit visual semantics.
