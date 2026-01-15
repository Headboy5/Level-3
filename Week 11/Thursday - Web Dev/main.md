# Front End vs Back End

```mermaid
graph TB
    User([User]) --> SearchEngine[Search Engine<br/>Google/Bing]
    SearchEngine --> Browser[Web Browser<br/>Chrome/Firefox/Safari]
    
    Browser -->|1. HTTP Request| WebServer
    
    subgraph "Client Side - Front End"
        Browser
        Browser --> Render[Render HTML/CSS/JS]
        Render --> UI[User Interface]
        UI --> Interact[User Interactions]
    end
    
    subgraph "Server Side - Back End"
        WebServer[Web Server<br/>Apache/Nginx]
        WebServer --> App[Application Logic<br/>PHP/Node.js/Python]
        App --> DB[(Database<br/>MySQL/MongoDB)]
        DB --> App
        App --> WebServer
    end
    
    WebServer -->|2. HTTP Response| Browser
    Interact -.->|AJAX Request| WebServer
    
    style User fill:#e74c3c,stroke:#333,stroke-width:2px,color:#fff
    style SearchEngine fill:#3498db,stroke:#333,stroke-width:2px,color:#fff
    style Browser fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style UI fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style WebServer fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style App fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff
    style DB fill:#f39c12,stroke:#333,stroke-width:2px,color:#fff
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
