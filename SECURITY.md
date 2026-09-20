# Security

This plugin ships skills and an agent. It does not ship hooks, install scripts, or an MCP server in v0.1.0.

## What it does not do

- No shell hooks
- No postinstall scripts
- No reading of ~/.ssh, .env, or browser cookies
- No telemetry
- No training on user job data
- No hidden network endpoints

## Network

v0.1.0 has no bundled MCP URL. The Bot may open public supplier product pages in its own browser when the user asks for a live comparison. That traffic is the Bot computer talking to the supplier, not this repo calling home.

A future optional MCP will be declared here and in the README before it is added to a marketplace pin. The plugin will keep working if that MCP is disconnected.

## Reporting

Open a GitHub issue on this repository for security problems.
