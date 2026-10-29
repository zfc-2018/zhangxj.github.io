#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
node build.mjs
printf '%s\n' 'Static page generated. Commit index.html and publish the repository root with GitHub Pages.'
