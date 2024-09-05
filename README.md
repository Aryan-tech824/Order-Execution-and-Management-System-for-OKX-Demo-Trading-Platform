# Order-Execution-and-Management-System-for-OKX-Demo-Trading-Platform
Objective: To create an order execution and management system to trade on OKX.
Functions:
•	Place order
•	Cancel order
•	Modify order
•	Get order book
•	View current positions
 Scope:
•	Spot, futures and options
•	All supported symbols.
•	Created a new OKX account and generated a set of API Keys for their "demo trading" testnet.
Focus:
•	Full functionality of above functions with low latency.
•	Created a websocket server that clients can connect to and subscribe to a symbol by sending a message.
•	The server responds with a stream of messages with the orderbook updates for each symbol that is subscribed to.
