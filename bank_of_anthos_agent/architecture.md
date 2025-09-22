```
+-----------------+
|      User       |
+-----------------+
        ^
        | (Interaction)
        v
+----------------------------------+
|      Root Agent: "Aura"          |
|    (financial_agent)             |
| - Manages conversation           |
| - Synthesizes sub-agent outputs  |
| - Presents final response        |
+----------------------------------+
        |
        | (Delegates tasks & uses tools)
        |
        +--------------------------------+--------------------------------+
        |                                |                                |
        v                                v                                v
+-----------------+              +-----------------------------+  +----------------------+
|      Tools      |              |         Sub-Agents          |  | External Financial   |
+-----------------+              |      (Silent Research Team) |  |    Data / APIs     |
|                 |              +-----------------------------+  +----------------------+
|  +-----------+  |                      |         ^                         ^
|  | Exporter  |  |                      |         | (Data)                  | (MCP Communication)
|  +-----------+  |                      |         |                         |
|                 |                      v         +-------------------------+
|  +-----------+  |              +-----------------------------+
|  | MCP Tool  |<-+------------->|      Goal Planner Agent     |
|  +-----------+  |              +-----------------------------+
|      ^          |              +-----------------------------+
|      |          |              |      Simulator Agent        |
+------+----------+              +-----------------------------+
       |                         +-----------------------------+
(Fetches Data)                   |      Optimizer Agent        |
       |                         +-----------------------------+
       v                         +-----------------------------+
+------------------+             |      Fact Checker Agent     |
| External Systems |             +-----------------------------+
+------------------+

```

### **Workflow Explanation:**

1.  **User Interaction:** You communicate directly and exclusively with **Aura**, the `root_agent`.
2.  **Task Delegation:** When you ask a question or give a command, Aura analyzes it. It then delegates the necessary analysis and data processing tasks to its specialized `sub_agents` (Goal Planner, Simulator, Optimizer, Fact Checker).
3.  **Data Retrieval (MCP):** Aura's first step is almost always to use the **MCP Tool** (`toolset`) to securely fetch your latest financial data from external sources (like your bank or investment accounts). This ensures its advice is based on real-time information.
4.  **Internal Processing:** The sub-agents perform their specific functions on the data. For example, the Simulator might run projections while the Optimizer looks for better financial strategies. The Fact Checker verifies any financial tips before they are presented.
5.  **Synthesis and Response:** Aura gathers the processed information and insights from all its sub-agents and tools. It synthesizes this complex data into a single, easy-to-understand, and friendly response, which it then delivers to you.
