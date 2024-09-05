# Order-Execution-and-Management-System-for-OKX-Demo-Trading-Platform
Objective: To create an order execution and management system to trade on OKX.

      Functions:
            - Place order

            - Cancel order

            - Modify order

            - Get orderbook

            - View current positions
            
      Scope:
            - Spot, futures and options.

            - All supported symbols.

            - Create a new OKX account.

            - Generate a set of API Keys for their "demo trading" testnet.

      Focus:
            - Full functionality of above functions with low latency.

            - Created a websocket server that clients can connect to and subscribe to a symbol by sending a message.

            - The server responds with a stream of messages with the orderbook updates for each symbol that is subscribed to.
