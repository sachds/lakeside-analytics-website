# Single content model for both builds. Every figure here traces to a published
# source; see PROVENANCE notes inline. Nothing is invented.

NAV = [
    ("Insights", "writing.html"),
    ("Work", "work.html"),
    ("Services", "services.html"),
    ("About", "about.html"),
]

# kind: the editorial type label, following the BCG/PwC pattern of typing every item.
STUDIES = [
    dict(kind="Analysis", date="Jul 2026", venue="Capital One Software",
         url="https://capitalonesoftware.com/blog/fable5-mythos5-enterprise-data",
         title="How to use Claude Fable 5 and Mythos models with enterprise data",
         desc="Claude Fable 5 ships with a 30-day prompt and output retention window. The case for tokenizing at the source, before the API boundary, so protection survives the workload."),
    dict(kind="Framework", date="Jun 2026", venue="Capital One Software",
         url="https://capitalonesoftware.com/blog/graph-database-evaluation",
         title="Do I need a graph database? A framework to evaluate graph DBs",
         desc="When a dedicated graph database earns its place against relational primitives — and when it does not."),
    dict(kind="Guide", date="May 2026", venue="Capital One Software",
         url="https://capitalonesoftware.com/blog/scaling-agent-context-snowflake-knowledge-graphs",
         title="Scaling agent context with knowledge graphs on Snowflake",
         desc="How knowledge graphs extend the working context available to AI agents beyond fixed dashboards and flat retrieval, using Cortex features and relational primitives. No dedicated graph database required."),
    dict(kind="Review", date="Apr 2026", venue="Capital One Software",
         url="https://capitalonesoftware.com/blog/snowflake-coco-cli",
         title="Snowflake CoCo CLI: hands-on review for TPC-DS 10TB",
         desc="Five test areas, from catalog discovery through dbt model generation, run against TPC-DS at 10TB — 55.8 billion rows."),
    dict(kind="Build", date="Mar 2026", venue="Capital One Software",
         url="https://capitalonesoftware.com/blog/databricks-genai-cost-supervisor-agent",
         title="Building a GenAI cost supervisor agent in Databricks",
         desc="Registers 20 Unity Catalog SQL functions over Databricks system tables so an agent answers GenAI cost, governance, and attribution questions on demand — and makes the case for catalog functions over text-to-SQL to eliminate the injection surface."),
    dict(kind="Benchmark", date="Feb 2026", venue="Capital One Software",
         url="https://capitalonesoftware.com/blog/snowflake-warehouse-benchmark-gen1-gen2-snowpark-optimized",
         title="Snowflake Gen1 vs. Gen2 vs. Snowpark-optimized warehouses",
         desc="TPC-DS at 1TB across warehouse generations. On small warehouses Gen2 finished in 0.64 minutes where Gen1 took 38.24, driven by memory spilling — but at large sizes, with no memory pressure, Gen1 won the majority of queries."),
    dict(kind="Benchmark", date="Jan 2026", venue="Capital One Software",
         url="https://capitalonesoftware.com/blog/databricks-benchmarks-classic-jobs-serverless-jobs-dbsql-comparison",
         title="Jobs Classic vs. Jobs Serverless vs. DBSQL: who wins on TPC-DS?",
         desc="The full TPC-DS suite — 4,750+ query executions — across three Databricks compute planes via Apache JMeter. Serverless SQL warehouses won overall, faster at the tail and cheaper for the same workload, while Jobs Classic beat both Jobs Serverless variants on cost and consistency."),
    dict(kind="Build", date="Mar 2024", venue="Plotly", role="Lead author",
         url="https://medium.com/plotly/amplify-your-organizations-custom-llm-strategy-using-databricks-with-plotly-part-1-6bfb8a86872b",
         title="Amplify your organization&rsquo;s custom LLM strategy using Databricks with Plotly",
         desc="A full-stack Dash application that deploys Hugging Face and Databricks models to GPU serving endpoints."),
    dict(kind="Build", date="Oct 2023", venue="DBSQL SME Engineering", role="Lead author",
         url="https://medium.com/dbsql-sme-engineering/visualizing-a-billion-points-databricks-plotly-dash-and-the-plotly-resampler-45461bc3f466",
         title="Visualizing a billion points: Databricks SQL, Plotly Dash, and the Plotly Resampler",
         desc="At-scale interactive Dash apps over large IoT time-series via the Databricks SQL connector, with Plotly Resampler downsampling on a Polars backend."),
    dict(kind="Build", date="Oct 2023", venue="Plotly", role="Lead author",
         url="https://medium.com/plotly/build-real-time-production-data-apps-with-databricks-plotly-dash-269cb64b7575",
         title="Build real-time production data apps with Databricks and Plotly Dash",
         desc="A Databricks Structured Streaming pipeline ingesting real-time IoT sensor data, aggregated through Auto Loader and windowing into Gold-level Delta views, served to a Dash app over Databricks SQL endpoints."),
    dict(kind="Guide", date="2023", venue="Plotly", role="Lead author",
         url="https://medium.com/plotly/building-plotly-dash-apps-on-a-lakehouse-with-databricks-sql-advanced-edition-4e1015593633",
         title="Building Plotly Dash apps on a lakehouse with Databricks SQL (advanced edition)",
         desc="Connecting Dash to Databricks via the SQL connector or SQLAlchemy ORM — streaming dashboards, DDL and object mapping, and advanced visuals."),
    dict(kind="Guide", date="2023", venue="Plotly", role="Contributor",
         url="https://medium.com/plotly/databricks-sdk-plotly-dash-the-easiest-way-to-get-jobs-done-70d44e1cd9c3",
         title="Databricks SDK + Plotly Dash — the easiest way to get jobs done",
         desc="Dash as a front end for the Databricks SDK and Jobs API."),
    dict(kind="Case study", date="Feb 2023", venue="Plotly", role="Contributor",
         url="https://medium.com/plotly/molson-coors-streamlines-supply-planning-workflows-with-databricks-plotly-dash-d26de907142c",
         title="Molson Coors streamlines supply planning workflows with Databricks &amp; Plotly Dash",
         desc="Replacing a manual spreadsheet process for tracking product ship dates with a Databricks SQL&ndash;backed Dash application — AG Grid editing with SQLAlchemy write-back, taking the workflow from 60+ steps to fewer than 10."),
    dict(kind="Talk", date="2024", venue="Data + AI Summit", role="Speaker",
         url="https://www.youtube.com/watch?v=g3cOFicI8O4",
         title="Petabyte Pitstops with Mercedes, Databricks SQL and Plotly Resampler",
         desc="A high-density visualization tool combining Rust-based downsampling, Databricks SQL, and Apache Arrow zero-copy buffers, with queries that adapt to the analyst&rsquo;s zoom level."),
]

CASES = [
    dict(
        client="Mercedes", sector="Automotive", years="2023&ndash;2024",
        scope="Petabyte time-series visualization",
        title="Trillions of rows, explorable in real time.",
        body=[
            "The analytics team needed to explore time-series data at a scale where the usual answer — pre-aggregate everything and accept the loss of resolution — destroyed the signal they were looking for.",
            "We built a high-density visualization tool combining Rust-based downsampling with Databricks SQL and Apache Arrow zero-copy memory buffers. Queries adapt to the analyst&rsquo;s zoom level: aggregated views by default, with SQL pushdown retrieving original high-resolution data on demand. Larger-than-memory datasets stay interactive instead of being flattened into something smaller and less useful.",
        ],
        measures=[
            ("Trillions", "of rows handled without pre-aggregation"),
            ("Zero-copy", "Arrow buffers for larger-than-memory datasets"),
            ("DAIS 2024", "presented at Data + AI Summit"),
        ],
        prov='&ldquo;Petabyte Pitstops with Mercedes, Databricks SQL and Plotly Resampler&rdquo; &middot; <a href="https://www.youtube.com/watch?v=g3cOFicI8O4">Data + AI Summit 2024</a>',
    ),
    dict(
        client="Capital One Software", sector="Enterprise software", years="Ongoing since Jan 2026",
        scope="Published benchmark program",
        title="Full workloads, at scale, with the method published.",
        body=[
            "An ongoing research program measuring compute economics and agent architecture across Databricks and Snowflake — the questions platform teams actually decide on, answered with standard suites run under controlled conditions.",
            "Every study ships with the notebooks, worksheets, or prompt lists needed to check the work, including the findings that cut against the obvious answer. When Gen2 warehouses lost to Gen1 at large sizes, that went in the piece.",
        ],
        measures=[
            ("4,750+", "TPC-DS query executions across three compute planes"),
            ("55.8B", "rows in the largest test environment, at 10TB"),
            ("7", "studies published, Jan&ndash;Jul 2026"),
        ],
        prov='seven studies, Jan&ndash;Jul 2026 &middot; <a href="writing.html">read the research</a>',
    ),
    dict(
        client="Molson Coors", sector="Consumer goods", years="2023",
        scope="Supply planning on Databricks SQL",
        title="Planners write to the warehouse, not to a spreadsheet.",
        body=[
            "The supply planning team tracked product ship dates through a manual spreadsheet process — extracts passed between people, with no auditable record of what changed or why.",
            "We replaced it with a Databricks SQL&ndash;backed application: an editable AG Grid with SQLAlchemy ORM write-back, so planners keep the workflow they trust while the numbers live somewhere auditable. The published write-up puts the workflow at 60+ steps before and fewer than 10 after.",
        ],
        measures=[
            ("60+ &rarr; &lt;10", "steps in the supply planning workflow, as published"),
            ("Write-back", "native ORM writes to the warehouse from the app"),
        ],
        prov='written up by Plotly &middot; <a href="https://medium.com/plotly/molson-coors-streamlines-supply-planning-workflows-with-databricks-plotly-dash-d26de907142c">feb 2023</a>',
    ),
]

# Resume work that has no public write-up. Listed plainly, without metrics,
# because there is no published source to cite for them.
ALSO_BUILT = [
    ("DbxOauth", "An extension letting Dash applications authenticate against Databricks APIs over OAuth — both M2M service principals and U2M user-level requests — with automatic encryption, storage, and refresh of tokens."),
    ("Databricks Delta Optimizer", "An application for optimizing Delta tables from user-defined strategies, integrating the Jobs API, Databricks SQL connector, SDK, and OAuth to manage authentication and scheduled runs."),
    ("Custom LLM management app", "A Dash interface for non-technical users to select, register, and deploy custom and Hugging Face models to Databricks serving endpoints, with an interactive chat surface for querying them."),
    ("Real-time IoT streaming pipeline", "A Databricks Structured Streaming pipeline ingesting sensor data from an Azure IoT Hub into ADLS, using Auto Loader, watermarking, and windowing to build Gold-level Delta views."),
]

PRACTICES = [
    dict(num="01", area="Architecture",
         title="Databricks &amp; Snowflake platform architecture",
         body="Platform design and remediation for teams already committed to a lakehouse or cloud warehouse — and for teams deciding between them. We work on the structure that determines cost and speed for years: compute topology, storage layout, governance model, and the migration path between them.",
         scope=["Lakehouse and warehouse design reviews, with a written findings document",
                "Unity Catalog rollout: governance model, permissions, catalog structure",
                "Compute topology — warehouse sizing, cluster policy, workload isolation",
                "Migration planning between platforms or between compute planes",
                "Query and pipeline tuning against a measured baseline"]),
    dict(num="02", area="Benchmarking",
         title="Compute benchmarking &amp; cost optimization",
         body="Independent measurement of what your platform actually costs and how fast it actually is. We build reproducible harnesses over standard suites and over your own workloads, so the numbers survive scrutiny and can be re-run after the engagement ends. This is the practice the rest of the work is built on.",
         scope=["TPC-DS and custom workload benchmarking with JMeter-driven harnesses",
                "Compute plane comparisons — serverless vs. classic vs. SQL warehouse",
                "Spend analysis from system tables and account usage views",
                "Cost-per-query and price/performance modeling at your concurrency",
                "A harness your team owns, so results can be reproduced later"]),
    dict(num="03", area="Applications",
         title="Custom data &amp; analytics applications",
         body="Data products for the cases a BI tool cannot reach: very large time-series, real-time streams, custom interaction models, or performance requirements that need work below the framework. We build full-stack — warehouse connection through interface — and drop into Rust and Arrow when the performance ceiling is the actual constraint.",
         scope=["Interactive analytics apps over Databricks SQL and Snowflake",
                "Billion-point time-series visualization with server-side downsampling",
                "Real-time and streaming dashboards",
                "High-performance data engines in Rust, Arrow, and Polars",
                "Model-serving front ends and internal analytical tooling"]),
    dict(num="04", area="AI agents",
         title="AI agents &amp; GenAI on the data platform",
         body="Agents that are actually grounded in your data and actually governed. The hard parts are context and safety: giving an agent more working context than flat retrieval provides, and exposing your warehouse through a tool surface that cannot be talked into arbitrary SQL. We also make GenAI spend legible before it becomes a line item nobody can explain.",
         scope=["Knowledge-graph context so agents reason past fixed dashboards",
                "Governed tool surfaces — catalog functions instead of open text-to-SQL",
                "MCP server design and integration against internal data systems",
                "GenAI cost supervision built on platform system tables",
                "Evaluation harnesses so agent quality is measured, not assumed"]),
]

SHAPES = [
    ("Two to four weeks", "Assessment",
     "A focused review — architecture, spend, or a specific workload — producing a written findings document with measured evidence and a prioritized set of recommendations."),
    ("Fixed scope", "Project",
     "A scoped build: a benchmark harness, a migration, an application, or an agent. Agreed acceptance criteria, documentation and handover included."),
    ("Month to month", "Advisory",
     "Recurring time for teams who want a second set of eyes on architecture decisions, vendor claims, and performance work as they come up."),
]

STATS = [
    ("4,750+", "TPC-DS query executions benchmarked across three Databricks compute planes"),
    ("55.8B", "rows in the largest test environment, TPC-DS at 10TB on Snowflake"),
    ("Trillions", "of rows made explorable in real time, without pre-aggregation"),
    ("13", "studies published, every figure dated and sourced"),
]

METHOD = [
    ("Step 01", "Establish the baseline",
     "Your real workloads, your data volumes, your query patterns — not a synthetic benchmark from a vendor&rsquo;s marketing page. This frequently changes the brief. The problem is often not where the team thought it was."),
    ("Step 02", "Decide with evidence",
     "Architecture choices get argued on measured trade-offs: cost per query, latency at your concurrency, governance surface. When two options are close, we say so instead of papering over it with a recommendation."),
    ("Step 03", "Hand over the harness",
     "Engagements end with something reproducible. The numbers can be re-run after we leave — against the next platform version, by your team, without us."),
]

ABOUT = dict(
    lede="Lakeside Analytics is the consulting practice of Sachin Seth — a data platform architect and analytics product builder working on the systems that decide what a platform costs and how fast it runs.",
    body=[
        "The practice was established in 2021 and works remotely from Brooklyn, New York. It is deliberately small: you talk to the person doing the work, and engagements are scoped to end rather than to renew.",
        "The through-line is measurement. Most platform decisions get made on vendor documentation and what worked somewhere else, which produces architecture built on assumptions nobody tested. Every engagement here starts by measuring what your platform actually does, and ends with a harness your team can re-run without us.",
        "That method is public. Thirteen articles and a conference talk, published under bylines at Capital One Software, Plotly, and Databricks SME Engineering, carry the full methodology — including the results that contradict the conventional answer.",
    ],
    facts=[
        ("Established", "2021"),
        ("Based", "Brooklyn, New York &middot; remote"),
        ("Principal", "Sachin Seth"),
        ("Published", "13 articles, 1 conference talk"),
    ],
    education=dict(
        degree="BA, Mathematics, Physics, and Classical Literature",
        school="SUNY Stony Brook",
        years="2013&ndash;2017",
        note="Advanced coursework in holomorphic dynamics, including a term thesis on Riemann spheres exploring complex analysis and geometric structures.",
    ),
    venues=["Capital One Software", "Plotly", "Databricks SME Engineering", "Data + AI Summit"],
)

CONTACT = dict(
    title="Start with the problem.",
    sub="No discovery deck, no junior on the call. A paragraph about what your platform is doing, or should be doing, is enough to begin — and we will say plainly if it isn&rsquo;t work we should take.",
    email="sachin@lakesideanalytics.io",
)
