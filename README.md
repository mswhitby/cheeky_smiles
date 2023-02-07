# Cheeky Smiles


Cheeky Smiles owns a party hosting company. He would like a more efficient way to charge customers for parties. Cheeky Smiles has decided to write a python algorithm that can automatically email invoices to customers. The invoices should include the line-item prices for the customer's request. 

The party packages starts at **$100** for the basic package. The customers can pay extra for any addons.  

\
**Addons Price List:**
- Bouncy House (H): $50
- Slip & Slide (S): $40
- Yard Sign (Y): $35
- Pizza (p): $10 per pizza
- Burger (b): $2 per burger
- Soda (s): $.50 per soda
- Cake (C): $15
- Cupcakes (c): $.25 per cupcake

\
*Example Input:*

```
1H,20c,20b,4p,20s
```
\
*Example Output:*
```
Thank you for choosing Cheeky Smiles for your party needs! Here is your itemized invoice:

Bouncy House, 1, $50.00
Cupcakes, 20, $5.00
Burgers, 20, $40.00
Pizza, 4, $40.00
Soda, 20, $10.00

Base Price: 100
Total: $245.00
```

[Starter Code](https://onlinegdb.com/btIU7SKMb)

[Code Sandbox](https://codesandbox.io/p/github/mswhitby/cheeky_smiles/main?file=%2FREADME.md&workspace=%257B%2522activeFileId%2522%253A%2522clduk8lek0000fsgzdo9rdo0d%2522%252C%2522openFiles%2522%253A%255B%2522%252FREADME.md%2522%255D%252C%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522gitSidebarPanel%2522%253A%2522COMMIT%2522%252C%2522spaces%2522%253A%257B%2522clduk8nb2000x356h7alc1kcr%2522%253A%257B%2522key%2522%253A%2522clduk8nb2000x356h7alc1kcr%2522%252C%2522name%2522%253A%2522Terminal%2522%252C%2522devtools%2522%253A%255B%257B%2522type%2522%253A%2522TERMINAL%2522%252C%2522shellId%2522%253A%2522cldukdbi90005fsgz0c8whuuj%2522%252C%2522key%2522%253A%2522cldukdbgn00cv356hddpv0sqz%2522%252C%2522isMinimized%2522%253Afalse%257D%255D%257D%257D%252C%2522currentSpace%2522%253A%2522clduk8nb2000x356h7alc1kcr%2522%252C%2522spacesOrder%2522%253A%255B%2522clduk8nb2000x356h7alc1kcr%2522%255D%252C%2522hideCodeEditor%2522%253Afalse%257D))