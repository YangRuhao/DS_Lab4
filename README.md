# COMP41720 Lab 4: Microservices URL Shortener

A distributed URL shortener application built with microservices architecture, containerized with Docker, and deployed on Kubernetes.

## Architecture Overview

```mermaid
graph TB
    subgraph Kubernetes Cluster
        subgraph "Shortener Namespace"
            S1[Shortener Pod 1]
            S2[Shortener Pod 2]
            SS[shortener-service<br/>ClusterIP:5001]
        end
        
        subgraph "Redirect Namespace"  
            R1[Redirect Pod 1]
            R2[Redirect Pod 2]
            R3[Redirect Pod 3]
            RS[redirect-service<br/>NodePort:30002]
        end
        
        SS --> S1
        SS --> S2
        RS --> R1
        RS --> R2
        RS --> R3
    end
    
    Client1[User: Create URL] --> SS
    Client2[User: Redirect] --> RS
    R1 -.->|HTTP Lookup| SS
    R2 -.->|HTTP Lookup| SS
    R3 -.->|HTTP Lookup| SS
    
    style SS fill:#e1f5fe
    style RS fill:#f3e5f5
    style S1 fill:#f1f8e9
    style R1 fill:#fff3e0