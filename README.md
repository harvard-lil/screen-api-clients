screen-api-clients
==================

Here are scripts for posting to the API presented by
https://github.com/jcushman/dostuff. They use the function `go` from
`screen_api_client.py`, and need config values set in the code: URL,
room name, and token.

- `last-capture.py` reports on the last [Perma](https://perma.cc)
  capture. It uses `get_objects` from `perma_times.py` to query
  Perma's public API.
  
- `cap-ingest-progress.py` is an ephemeral script for reporting on a
  long-running ingest process for the Caselaw Access Project.

