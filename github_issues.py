import pathway as pw

commits_table = pw.io.airbyte.read(
    "./connections/github.yaml",
    streams=["issues"],
)
pw.io.jsonlines.write(commits_table, "commits.jsonlines")
pw.run()
