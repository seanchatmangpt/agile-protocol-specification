---
name: bff-patterns
description: |
  Backend-for-Frontend architecture patterns for API aggregation, data transformation,
  and client-specific optimization. Activates when designing API layers between
  backends and frontends or implementing data transformation pipelines.
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# Backend-for-Frontend (BFF) Patterns Skill

This skill implements BFF architecture patterns for creating optimized API layers between backends and frontend clients.

## When This Skill Activates

- Designing API aggregation layers
- Creating client-specific backends
- Implementing data transformation pipelines
- Optimizing frontend-backend communication
- Building GraphQL or REST façades

## BFF Decision Framework

### When to Use BFF

Answer these questions to determine if BFF is appropriate:

1. **Multiple Clients?** Do you have web, mobile, and/or desktop clients with different data needs?
2. **Complex Aggregation?** Does the frontend need to combine data from multiple services?
3. **Performance Critical?** Is reducing round-trips and payload size important?
4. **Client Optimization?** Do different clients need different data shapes?
5. **Security Boundary?** Do you need to filter sensitive data before reaching clients?

If 3+ answers are "yes", BFF is recommended.

## Core Patterns

### 1. API Aggregation Pattern

```
Client Request
     ↓
   [BFF]
   ↙   ↘
Service A  Service B
   ↘   ↙
 Aggregated Response
     ↓
   Client
```

```typescript
// BFF aggregation example
async function getUserDashboard(userId: string) {
  const [user, orders, recommendations] = await Promise.all([
    userService.getUser(userId),
    orderService.getRecentOrders(userId),
    recommendationService.getForUser(userId)
  ]);

  return {
    profile: transformUserProfile(user),
    recentOrders: orders.slice(0, 5),
    topRecommendations: recommendations.slice(0, 3)
  };
}
```

### 2. Data Transformation Pattern

```yaml
transformation:
  input: Raw backend response
  operations:
    - filter: Remove sensitive fields
    - map: Rename fields for client conventions
    - reduce: Aggregate related data
    - enrich: Add computed fields
  output: Client-optimized payload
```

```typescript
// Transform backend user to mobile-friendly format
function transformForMobile(backendUser: BackendUser): MobileUser {
  return {
    id: backendUser.userId,
    displayName: `${backendUser.firstName} ${backendUser.lastName}`,
    avatar: backendUser.profileImageUrl || DEFAULT_AVATAR,
    // Omit sensitive fields like SSN, internal IDs
  };
}
```

### 3. Client-Specific BFF Pattern

```
           ┌─────────────┐
Web App ───│  Web BFF    │───┐
           └─────────────┘   │
           ┌─────────────┐   │   ┌──────────────┐
Mobile ────│ Mobile BFF  │───┼───│ Microservices│
           └─────────────┘   │   └──────────────┘
           ┌─────────────┐   │
IoT ───────│  IoT BFF    │───┘
           └─────────────┘
```

### 4. Caching Strategy Pattern

```yaml
caching:
  levels:
    - level: Request
      strategy: Deduplication within request
      ttl: 0

    - level: Session
      strategy: User-specific cache
      ttl: 5m

    - level: Shared
      strategy: Common data cache
      ttl: 1h

    - level: Static
      strategy: Reference data
      ttl: 24h
```

### 5. Error Handling Pattern

```typescript
// Graceful degradation in BFF
async function getDashboard(userId: string) {
  const results = await Promise.allSettled([
    userService.getUser(userId),
    orderService.getOrders(userId),
    recommendationService.get(userId)
  ]);

  return {
    user: results[0].status === 'fulfilled' ? results[0].value : null,
    orders: results[1].status === 'fulfilled' ? results[1].value : [],
    recommendations: results[2].status === 'fulfilled' ? results[2].value : [],
    errors: results
      .filter(r => r.status === 'rejected')
      .map(r => r.reason.message)
  };
}
```

## BFF Implementation Checklist

### Design Phase
- [ ] Identify client types and their specific needs
- [ ] Map backend services to aggregate
- [ ] Define transformation requirements
- [ ] Plan caching strategy
- [ ] Design error handling approach

### Implementation Phase
- [ ] Set up BFF service skeleton
- [ ] Implement service clients
- [ ] Add aggregation logic
- [ ] Create transformation layer
- [ ] Implement caching
- [ ] Add error handling with fallbacks
- [ ] Set up monitoring/logging

### Testing Phase
- [ ] Unit test transformations
- [ ] Integration test aggregations
- [ ] Load test under realistic conditions
- [ ] Test failure scenarios
- [ ] Verify cache behavior

## Technology Recommendations

### PLAN Pro Stack BFF Options

**Python/FastAPI:**
```python
@router.get("/dashboard/{user_id}")
async def get_dashboard(user_id: str):
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_user(session, user_id),
            fetch_orders(session, user_id),
        ]
        user, orders = await asyncio.gather(*tasks)
    return DashboardResponse(user=user, orders=orders)
```

**Elixir/Phoenix:**
```elixir
def dashboard(conn, %{"user_id" => user_id}) do
  tasks = [
    Task.async(fn -> UserService.get(user_id) end),
    Task.async(fn -> OrderService.list(user_id) end),
  ]
  [user, orders] = Task.await_many(tasks)
  render(conn, "dashboard.json", user: user, orders: orders)
end
```

**Nuxt/Nitro:**
```typescript
export default defineEventHandler(async (event) => {
  const userId = event.context.params.userId;
  const [user, orders] = await Promise.all([
    $fetch(`/api/users/${userId}`),
    $fetch(`/api/orders?userId=${userId}`)
  ]);
  return { user, orders };
});
```

## Best Practices

1. **Keep BFF Thin**: Business logic belongs in services, not BFF
2. **Client Ownership**: Each client team owns their BFF
3. **Version Carefully**: BFF APIs should be versioned
4. **Monitor Latency**: Track aggregation overhead
5. **Cache Aggressively**: Use appropriate caching at each level
6. **Fail Gracefully**: Never let one service failure break the whole response
7. **Document Contracts**: Clear API documentation for frontend teams
