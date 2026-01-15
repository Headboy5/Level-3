# Front End vs Back End

```mermaid
graph TB
    subgraph "Client Side - Front End"
        A[User Interface<br/>HTML/CSS/JavaScript]
        B[Browser]
        C[User Interactions]
        D[Visual Presentation]
        E[Client-Side Validation]
        
        C --> A
        A --> D
        A --> E
        A --> B
    end
    
    subgraph "Server Side - Back End"
        F[Web Server<br/>PHP/Node.js/Python]
        G[Database<br/>MySQL/PostgreSQL/MongoDB]
        H[Business Logic]
        I[Authentication]
        J[Data Processing]
        K[APIs & Services]
        
        F --> H
        F --> I
        F --> J
        F --> G
        F --> K
    end
    
    B <-->|HTTP/HTTPS<br/>Requests & Responses| F
    
    style A fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#f39c12,stroke:#333,stroke-width:2px,color:#fff
```

## Front End (Client Side)
- **Technologies**: HTML, CSS, JavaScript, React, Vue, Angular
- **Responsibilities**:
  - User interface and experience
  - Visual presentation
  - Client-side validation
  - User interactions and events
  - Runs in the user's browser

## Back End (Server Side)
- **Technologies**: PHP, Node.js, Python, Java, Ruby, C#
- **Responsibilities**:
  - Server-side logic
  - Database operations
  - Authentication and security
  - Data processing
  - API endpoints
  - Runs on the server

## Communication
- Front end and back end communicate via **HTTP/HTTPS** protocols
- Data is typically exchanged in **JSON** or **XML** format
- RESTful APIs or GraphQL commonly used for data transfer
