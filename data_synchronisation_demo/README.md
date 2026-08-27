# Data Synchronisation – Code Demonstration

This small Python example demonstrates bandwidth management and integrity
checking for a file synchronisation utility.

The client divides a file into chunks and calculates a SHA-256 hash for each
chunk. The server can compare these hashes with the chunks it already stores
and request only missing chunks. A complete-file SHA-256 hash is also produced
for final integrity verification.

Fixed-size chunks are used to keep the demonstration short. A full
implementation could use content-defined chunking, such as FastCDC, to improve
efficiency when content is inserted or deleted.
