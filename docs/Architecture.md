                         EXTERNAL SERVICES
        ┌───────────────────────────────────────────┐
        │                                           │
        │  Firebase Auth          Google Play       │
        │  - Google Login         - Billing         │
        │  - User identity        - Purchases       │
        │                                           │
        │  Health Connect         Google Play       │
        │  - Steps                - App distribution│
        │                         - Testing          │
        │                                           │
        └───────┬───────────────────┬───────────────┘
                │                   │
                ↓                   ↓

                 VENDISTEP ANDROID APP
                 Kotlin + Jetpack Compose
                         │
                         │ HTTPS / JSON
                         │ Firebase ID Token
                         ↓
              ┌─────────────────────────┐
              │         FastAPI         │
              │         Python          │
              │                         │
              │  API Routes             │
              │       ↓                 │
              │  Authentication         │
              │       ↓                 │
              │  Services / Game Logic  │
              │       ↓                 │
              │  Database Layer         │
              └────────────┬────────────┘
                           │
                        SQLAlchemy
                           │
                           ↓
                    ┌──────────────┐
                    │ PostgreSQL   │
                    │              │
                    │ Users        │
                    │ Machines     │
                    │ Items        │
                    │ Inventory    │
                    │ Rolls        │
                    │ Activity     │
                    │ Purchases    │
                    └──────────────┘


                VENDISTEP WEAR OS APP
                   Kotlin / Compose
                          ↕
                    Android App


## System Ownership

Android
- User interface
- Animations
- Health Connect access
- Local temporary state
- Google Play Billing interaction

FastAPI
- Game rules
- Roll generation
- Rarity calculation
- Duplicate protection
- Token rewards
- Purchase verification
- Authorization

PostgreSQL
- Users
- Vending machines
- Items
- Inventory
- Rolls
- Transactions
- Purchases
- Activity history

Firebase
- Authentication
- Google Sign-In identity

Health Connect
- Health and step data

Google Play
- Payment processing
- App distribution