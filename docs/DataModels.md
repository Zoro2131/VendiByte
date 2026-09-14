User
----------------------------------
UserId      UUID    /   PK
FirebaseUid     String  / Unique
Email       String
DisplayName     string  /   Nullable    /   with default
ProfileImageUrl     string/ Nullable    /    with default
CreatedAt       datetime
LastLogInAt      datetime
IsActive        Boolean
UserVendingMachine

Users Relationship
-----------------------------------------------
- One User has many InventoryItems
- One User has many Rolls
- One User has many StepFreezes
- One User has many TokenTransactions
- One User has many Purchases
- One User has many DailyActivity records
- One User can access many VendingMachines through UserVendingMachine

UserVendingMachine
-----------------------------------------
UservendingMachineId    UUID    /   OK
UserId  UUID    / FK
vendingMachineId     UUID /     FK
UnlockType string 
UnlockAt    datetime
PurchasedId     UUID    /    nullable   /    FK

UserVendingMachine Relationship
------------------------------------------
- One UserVendingMachine belongs to one User
- One UserVendingMachine belongs to one VendingMachine
- One UserVendingMachine may be linked to one Purchase


VendingMachine
----------------------------------------
vendingMachineId        UUID    /   PK
name    string 
ItemType    string describes the items held in the machine 
Description     string / nullable
ImageURl    string  / nullable
IsActive    boolean 
IsDefault   boolean 
CreatedAt   datetime
AccessType string   has set values 


VendingMachine Relationship
-----------------------------------
- One VendingMachine has many Items
- One VendingMachine has many UserVendingMachine records
- One VendingMachine can be accessed by many Users through UserVendingMachine
- One VendingMachine has many Rolls


Item
----------------------------------------
ItemId        UUID    /    PK
VendingMachineId    UUID    /    FK
Name    string
Description    string    / nullable
Rarity    string    / has set values
ImageUrl    string    / nullable
IsActive    boolean
CreatedAt    datetime


Item Relationship
-----------------------------------
- One Item belongs to one VendingMachine
- One Item can appear in many InventoryItem records
- One Item can appear in many Roll records


InventoryItem
---------------------------------------------
InventoryItemId    UUID    /    PK
UserId    UUID    /    FK
ItemId    UUID    /    FK
Quantity    integer
FirstObtainedAt    datetime
LastObtainedAt    datetime

InventoryItem Relationship
---------------------------------------------------
- One InventoryItem belongs to one User
- One InventoryItem belongs to one Item
- One User can have many InventoryItem records
- One Item can belong to many Users through InventoryItem

Roll
---------------------------------------------
RollId    UUID    /    PK
UserId    UUID    /    FK
VendingMachineId    UUID    /    FK
ItemId    UUID    /    FK
RarityRolled    string
WasDuplicate    boolean
CreatedAt    datetime

Roll Relationship
---------------------------------------
- One Roll belongs to one User
- One Roll belongs to one VendingMachine
- One Roll results in one Item
- One User can have many Rolls
- One VendingMachine can have many Rolls
- One Item can appear in many Rolls


TokenTransaction
------------------------------------------------
TokenTransactionId    UUID    /    PK
UserId    UUID    /    FK
Amount    integer
TransactionType    string    / has set values
BalanceAfter    integer
RelatedRollId    UUID    / nullable    / FK
RelatedPurchaseId    UUID    / nullable    / FK
CreatedAt    datetime

Token Relationship
------------------------------------
- One TokenTransaction belongs to one User
- One TokenTransaction may be linked to one Roll
- One TokenTransaction may be linked to one Purchase
- One User can have many TokenTransaction records


DailyActivity
---------------------------------------------
DailyActivityId    UUID    /    PK
UserId    UUID    /    FK
ActivityDate    date
StepsRecorded    integer
RewardedSteps    integer
RemainingSteps    integer
TokensEarned    integer
CreatedAt    datetime
UpdatedAt    datetime


DailyActivity Relationship
-------------------------------------------------
- One DailyActivity belongs to one User
- One User can have many DailyActivity records
- A User should only have one DailyActivity record per date


LoginReward
-----------------------------------------
LoginRewardId    UUID    /    PK
UserId    UUID    /    FK
RewardDate    date
TokenAmount    integer
ClaimedAt    datetime


LoginReward Relationship
-------------------------------------------
- One LoginReward belongs to one User
- One User can have many LoginReward records
- A User can only receive one LoginReward per date

StepFreeze
------------------------------------------
StepFreezeId    UUID    /    PK
UserId    UUID    /    FK
EarnedAt    datetime
UsedAt    datetime    / nullable
RemainingStepsCarried    integer    / nullable
IsUsed    boolean


StepFreeze Relationship
--------------------------------------------
- One StepFreeze belongs to one User
- One User can have many StepFreeze records


Purchase
------------------------------------------------
PurchaseId    UUID    /    PK
UserId    UUID    /    FK
ProductId    string
ProductType    string    / has set values
GooglePurchaseToken    string    / unique
Quantity    integer
AmountPaid    decimal    / nullable
Currency    string    / nullable
PurchaseStatus    string    / has set values
PurchasedAt    datetime
VerifiedAt    datetime    / nullable


Purchase Relationship
---------------------------------------------
- One Purchase belongs to one User
- One User can have many Purchases
- One Purchase may create one or more TokenTransaction records
- One Purchase may unlock content through another related record