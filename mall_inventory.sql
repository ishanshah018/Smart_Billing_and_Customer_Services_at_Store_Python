PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
);
INSERT INTO products VALUES(1,'Milk (1L)','Dairy',120.0,816);
INSERT INTO products VALUES(2,'Butter (500g)','Dairy',200.0,470);
INSERT INTO products VALUES(3,'Cheddar Cheese (200g)','Dairy',250.0,30);
INSERT INTO products VALUES(4,'Yogurt (Plain, 1kg)','Dairy',150.0,30);
INSERT INTO products VALUES(5,'Paneer (250g)','Dairy',250.0,30);
INSERT INTO products VALUES(6,'Cream (250ml)','Dairy',200.0,30);
INSERT INTO products VALUES(7,'Ghee (1kg)','Dairy',650.0,27);
INSERT INTO products VALUES(8,'Milk Powder (500g)','Dairy',350.0,27);
INSERT INTO products VALUES(9,'Mozzarella Cheese (200g)','Dairy',250.0,30);
INSERT INTO products VALUES(10,'Flavored Milk (200ml)','Dairy',90.0,30);
INSERT INTO products VALUES(11,'Condensed Milk (400g)','Dairy',350.0,30);
INSERT INTO products VALUES(12,'Whipping Cream (250ml)','Dairy',250.0,30);
INSERT INTO products VALUES(13,'Butter Milk (1L)','Dairy',120.0,30);
INSERT INTO products VALUES(14,'Lassi (1L)','Dairy',150.0,27);
INSERT INTO products VALUES(15,'Greek Yogurt (100g)','Dairy',80.0,30);
INSERT INTO products VALUES(16,'Chocolate Milk (1L)','Dairy',200.0,30);
INSERT INTO products VALUES(17,'Skim Milk (1L)','Dairy',120.0,28);
INSERT INTO products VALUES(18,'Cottage Cheese (200g)','Dairy',200.0,30);
INSERT INTO products VALUES(19,'Ricotta Cheese (200g)','Dairy',250.0,30);
INSERT INTO products VALUES(20,'Parmesan Cheese (200g)','Dairy',300.0,30);
INSERT INTO products VALUES(21,'Potato Chips (150g)','Snacks',100.0,30);
INSERT INTO products VALUES(22,'Nachos (200g)','Snacks',150.0,6);
INSERT INTO products VALUES(23,'Salted Peanuts (100g)','Snacks',70.0,30);
INSERT INTO products VALUES(24,'Popcorn (Microwave Pack)','Snacks',120.0,30);
INSERT INTO products VALUES(25,'Trail Mix (200g)','Snacks',200.0,30);
INSERT INTO products VALUES(26,'Energy Bars (50g)','Snacks',120.0,30);
INSERT INTO products VALUES(27,'Chocolate Bars (100g)','Snacks',150.0,30);
INSERT INTO products VALUES(28,'Candy (50g)','Snacks',70.0,30);
INSERT INTO products VALUES(29,'Cookies (200g)','Snacks',140.0,30);
INSERT INTO products VALUES(30,'Pretzels (150g)','Snacks',100.0,30);
INSERT INTO products VALUES(31,'Crackers (200g)','Snacks',120.0,30);
INSERT INTO products VALUES(32,'Corn Chips (150g)','Snacks',140.0,30);
INSERT INTO products VALUES(33,'Granola Bars (100g)','Snacks',150.0,30);
INSERT INTO products VALUES(34,'Cheese Puffs (150g)','Snacks',120.0,30);
INSERT INTO products VALUES(35,'Roasted Almonds (100g)','Snacks',200.0,30);
INSERT INTO products VALUES(36,'Roasted Cashews (100g)','Snacks',225.0,30);
INSERT INTO products VALUES(37,'Veggie Chips (150g)','Snacks',150.0,30);
INSERT INTO products VALUES(38,'Popcorn (Ready-to-Eat)','Snacks',100.0,30);
INSERT INTO products VALUES(39,'Sweet Biscuits (200g)','Snacks',120.0,30);
INSERT INTO products VALUES(40,'Savory Biscuits (200g)','Snacks',140.0,30);
INSERT INTO products VALUES(41,'Orange Juice (1L)','Beverages',200.0,30);
INSERT INTO products VALUES(42,'Apple Juice (1L)','Beverages',200.0,30);
INSERT INTO products VALUES(43,'Cola (500ml)','Beverages',90.0,30);
INSERT INTO products VALUES(44,'Energy Drink (250ml)','Beverages',150.0,30);
INSERT INTO products VALUES(45,'Green Tea (20 bags)','Beverages',250.0,30);
INSERT INTO products VALUES(46,'Black Tea (20 bags)','Beverages',200.0,30);
INSERT INTO products VALUES(47,'Coffee Beans (200g)','Beverages',350.0,30);
INSERT INTO products VALUES(48,'Herbal Tea (20 bags)','Beverages',250.0,30);
INSERT INTO products VALUES(49,'Mineral Water (1L)','Beverages',60.0,30);
INSERT INTO products VALUES(50,'Soda Water (500ml)','Beverages',80.0,30);
INSERT INTO products VALUES(51,'Iced Tea (500ml)','Beverages',120.0,30);
INSERT INTO products VALUES(52,'Chocolate Milkshake (500ml)','Beverages',200.0,30);
INSERT INTO products VALUES(53,'Mango Shake (500ml)','Beverages',200.0,30);
INSERT INTO products VALUES(54,'Lemonade (500ml)','Beverages',120.0,30);
INSERT INTO products VALUES(55,'Tonic Water (500ml)','Beverages',90.0,30);
INSERT INTO products VALUES(56,'Sparkling Water (1L)','Beverages',80.0,30);
INSERT INTO products VALUES(57,'Smoothie (500ml)','Beverages',225.0,30);
INSERT INTO products VALUES(58,'Coconut Water (500ml)','Beverages',150.0,30);
INSERT INTO products VALUES(59,'Hot Chocolate (500ml)','Beverages',200.0,30);
INSERT INTO products VALUES(60,'Protein Shake (500ml)','Beverages',250.0,30);
INSERT INTO products VALUES(61,'Apples (1kg)','Fruits',200.0,30);
INSERT INTO products VALUES(62,'Bananas (1kg)','Fruits',120.0,30);
INSERT INTO products VALUES(63,'Oranges (1kg)','Fruits',160.0,30);
INSERT INTO products VALUES(64,'Strawberries (500g)','Fruits',250.0,30);
INSERT INTO products VALUES(65,'Grapes (1kg)','Fruits',225.0,30);
INSERT INTO products VALUES(66,'Watermelon (1pc)','Fruits',300.0,30);
INSERT INTO products VALUES(67,'Papaya (1pc)','Fruits',200.0,30);
INSERT INTO products VALUES(68,'Pineapple (1pc)','Fruits',225.0,30);
INSERT INTO products VALUES(69,'Mangoes (1kg)','Fruits',350.0,28);
INSERT INTO products VALUES(70,'Kiwi (1pc)','Fruits',60.0,30);
INSERT INTO products VALUES(71,'Peaches (1kg)','Fruits',240.0,30);
INSERT INTO products VALUES(72,'Plums (1kg)','Fruits',225.0,30);
INSERT INTO products VALUES(73,'Cherries (500g)','Fruits',300.0,30);
INSERT INTO products VALUES(74,'Avocados (1pc)','Fruits',150.0,30);
INSERT INTO products VALUES(75,'Pears (1kg)','Fruits',200.0,30);
INSERT INTO products VALUES(76,'Guavas (1kg)','Fruits',160.0,30);
INSERT INTO products VALUES(77,'Lemons (1kg)','Fruits',120.0,30);
INSERT INTO products VALUES(78,'Blueberries (250g)','Fruits',225.0,30);
INSERT INTO products VALUES(79,'Blackberries (250g)','Fruits',250.0,30);
INSERT INTO products VALUES(80,'Cranberries (250g)','Fruits',300.0,30);
INSERT INTO products VALUES(81,'Whole Wheat Bread (500g)','Bakery',40.0,25);
INSERT INTO products VALUES(82,'White Bread (500g)','Bakery',30.0,22);
INSERT INTO products VALUES(83,'Multigrain Bread (500g)','Bakery',50.0,4);
INSERT INTO products VALUES(84,'Croissants (Pack of 6)','Bakery',120.0,25);
INSERT INTO products VALUES(85,'Chocolate Cake (500g)','Bakery',250.0,25);
INSERT INTO products VALUES(86,'Cupcakes (Pack of 6)','Bakery',150.0,25);
INSERT INTO products VALUES(87,'Muffins (Pack of 6)','Bakery',120.0,25);
INSERT INTO products VALUES(88,'Baguette (300g)','Bakery',70.0,25);
INSERT INTO products VALUES(89,'Bagels (Pack of 4)','Bakery',100.0,23);
INSERT INTO products VALUES(90,'Cinnamon Rolls (Pack of 4)','Bakery',120.0,25);
INSERT INTO products VALUES(91,'Cheese Buns (Pack of 4)','Bakery',80.0,25);
INSERT INTO products VALUES(92,'Garlic Bread (Pack of 4)','Bakery',90.0,23);
INSERT INTO products VALUES(93,'Donuts (Pack of 6)','Bakery',150.0,20);
INSERT INTO products VALUES(94,'Brown Bread (500g)','Bakery',45.0,25);
INSERT INTO products VALUES(95,'Sourdough Bread (500g)','Bakery',80.0,25);
INSERT INTO products VALUES(96,'Rye Bread (500g)','Bakery',70.0,25);
INSERT INTO products VALUES(97,'Pita Bread (Pack of 6)','Bakery',100.0,21);
INSERT INTO products VALUES(98,'Naan Bread (Pack of 4)','Bakery',60.0,25);
INSERT INTO products VALUES(99,'Focaccia (500g)','Bakery',120.0,23);
INSERT INTO products VALUES(100,'Challah Bread (500g)','Bakery',150.0,25);
INSERT INTO products VALUES(101,'Breadsticks (Pack of 6)','Bakery',90.0,20);
INSERT INTO products VALUES(102,'Brioche (500g)','Bakery',130.0,25);
INSERT INTO products VALUES(103,'Parker House Rolls (Pack of 12)','Bakery',150.0,25);
INSERT INTO products VALUES(104,'Garlic Knots (Pack of 6)','Bakery',100.0,25);
INSERT INTO products VALUES(105,'Potatoes (1kg)','Vegetables',40.0,25);
INSERT INTO products VALUES(106,'Onions (1kg)','Vegetables',35.0,22);
INSERT INTO products VALUES(107,'Tomatoes (1kg)','Vegetables',50.0,25);
INSERT INTO products VALUES(108,'Carrots (1kg)','Vegetables',40.0,25);
INSERT INTO products VALUES(109,'Cucumbers (1kg)','Vegetables',30.0,25);
INSERT INTO products VALUES(110,'Spinach (500g)','Vegetables',25.0,25);
INSERT INTO products VALUES(111,'Lettuce (1pc)','Vegetables',30.0,25);
INSERT INTO products VALUES(112,'Cauliflower (1pc)','Vegetables',60.0,25);
INSERT INTO products VALUES(113,'Cabbage (1pc)','Vegetables',40.0,25);
INSERT INTO products VALUES(114,'Broccoli (500g)','Vegetables',70.0,25);
INSERT INTO products VALUES(115,'Bell Peppers (1kg)','Vegetables',100.0,25);
INSERT INTO products VALUES(116,'Zucchini (1kg)','Vegetables',80.0,25);
INSERT INTO products VALUES(117,'Green Beans (500g)','Vegetables',50.0,25);
INSERT INTO products VALUES(118,'Peas (500g)','Vegetables',50.0,25);
INSERT INTO products VALUES(119,'Mushrooms (250g)','Vegetables',60.0,22);
INSERT INTO products VALUES(120,'Eggplant (1kg)','Vegetables',70.0,25);
INSERT INTO products VALUES(121,'Pumpkin (1kg)','Vegetables',60.0,25);
INSERT INTO products VALUES(122,'Radish (500g)','Vegetables',25.0,25);
INSERT INTO products VALUES(123,'Sweet Potatoes (1kg)','Vegetables',70.0,25);
INSERT INTO products VALUES(124,'Asparagus (500g)','Vegetables',120.0,25);
INSERT INTO products VALUES(125,'Brussels Sprouts (500g)','Vegetables',90.0,25);
INSERT INTO products VALUES(126,'Leeks (500g)','Vegetables',60.0,25);
INSERT INTO products VALUES(127,'Artichokes (500g)','Vegetables',150.0,25);
INSERT INTO products VALUES(128,'Kale (500g)','Vegetables',80.0,25);
INSERT INTO products VALUES(129,'Shampoo (500ml)','Personal Care',150.0,25);
INSERT INTO products VALUES(130,'Toothpaste (100g)','Personal Care',50.0,23);
INSERT INTO products VALUES(131,'Body Lotion (500ml)','Personal Care',200.0,25);
INSERT INTO products VALUES(132,'Hand Wash (250ml)','Personal Care',80.0,25);
INSERT INTO products VALUES(133,'Face Cream (50g)','Personal Care',300.0,23);
INSERT INTO products VALUES(134,'Deodorant (150ml)','Personal Care',120.0,25);
INSERT INTO products VALUES(135,'Lip Balm (4g)','Personal Care',60.0,25);
INSERT INTO products VALUES(136,'Shaving Cream (200g)','Personal Care',150.0,25);
INSERT INTO products VALUES(137,'Hair Gel (200g)','Personal Care',120.0,25);
INSERT INTO products VALUES(138,'Toothbrush (Pack of 2)','Personal Care',100.0,25);
INSERT INTO products VALUES(139,'Hair Conditioner (500ml)','Personal Care',180.0,25);
INSERT INTO products VALUES(140,'Shaving Razor (Pack of 3)','Personal Care',200.0,25);
INSERT INTO products VALUES(141,'Face Wash (100ml)','Personal Care',150.0,25);
INSERT INTO products VALUES(142,'Hand Cream (100ml)','Personal Care',120.0,25);
INSERT INTO products VALUES(143,'Shampoo Bar (100g)','Personal Care',100.0,25);
INSERT INTO products VALUES(144,'Nail Polish (10ml)','Personal Care',80.0,25);
INSERT INTO products VALUES(145,'Perfume (50ml)','Personal Care',500.0,25);
INSERT INTO products VALUES(146,'Face Mask (100g)','Personal Care',200.0,25);
INSERT INTO products VALUES(147,'Hair Oil (200ml)','Personal Care',150.0,23);
INSERT INTO products VALUES(148,'Sunscreen (100ml)','Personal Care',300.0,25);
INSERT INTO products VALUES(149,'Shaving Brush (1pc)','Personal Care',250.0,25);
INSERT INTO products VALUES(150,'Foot Cream (100g)','Personal Care',100.0,25);
INSERT INTO products VALUES(151,'Shower Gel (500ml)','Personal Care',180.0,25);
INSERT INTO products VALUES(152,'Tooth Whitening Gel (100g)','Personal Care',400.0,25);
INSERT INTO products VALUES(153,'Dish Soap (500ml)','Household',50.0,25);
INSERT INTO products VALUES(154,'Laundry Detergent (1L)','Household',150.0,25);
INSERT INTO products VALUES(155,'Toilet Paper (Pack of 6)','Household',120.0,25);
INSERT INTO products VALUES(156,'Trash Bags (Pack of 20)','Household',100.0,25);
INSERT INTO products VALUES(157,'Multipurpose Cleaner (500ml)','Household',80.0,25);
INSERT INTO products VALUES(158,'Sponges (Pack of 6)','Household',50.0,25);
INSERT INTO products VALUES(159,'Glass Cleaner (500ml)','Household',90.0,25);
INSERT INTO products VALUES(160,'Air Freshener (300ml)','Household',120.0,25);
INSERT INTO products VALUES(161,'Broom (1pc)','Household',150.0,25);
INSERT INTO products VALUES(162,'Mop (1pc)','Household',200.0,25);
INSERT INTO products VALUES(163,'Dishwasher Tablets (Pack of 20)','Household',250.0,25);
INSERT INTO products VALUES(164,'Iron (1pc)','Household',1000.0,25);
INSERT INTO products VALUES(165,'Toilet Cleaner (500ml)','Household',60.0,25);
INSERT INTO products VALUES(166,'Washing Machine Cleaner (500g)','Household',150.0,25);
INSERT INTO products VALUES(167,'Pillows (Set of 2)','Household',500.0,25);
INSERT INTO products VALUES(168,'Bed Sheets (Single)','Household',300.0,25);
INSERT INTO products VALUES(169,'Towels (Set of 2)','Household',200.0,25);
INSERT INTO products VALUES(170,'Curtains (Pair)','Household',400.0,25);
INSERT INTO products VALUES(171,'Doormat (1pc)','Household',150.0,25);
INSERT INTO products VALUES(172,'Furniture Polish (500ml)','Household',180.0,25);
INSERT INTO products VALUES(173,'Scented Candles (Pack of 3)','Household',250.0,25);
INSERT INTO products VALUES(174,'Batteries (Pack of 4)','Household',100.0,25);
INSERT INTO products VALUES(175,'Lamps (1pc)','Household',500.0,25);
INSERT INTO products VALUES(176,'Fan (1pc)','Household',1200.0,24);
INSERT INTO products VALUES(177,'Protein Powder (500g)','Health & Fitness',900.0,25);
INSERT INTO products VALUES(178,'Multivitamins (60 tablets)','Health & Fitness',600.0,25);
INSERT INTO products VALUES(179,'Omega-3 Capsules (30 capsules)','Health & Fitness',350.0,25);
INSERT INTO products VALUES(180,'Vitamin C Tablets (60 tablets)','Health & Fitness',300.0,25);
INSERT INTO products VALUES(181,'Sports Drink (500ml)','Health & Fitness',100.0,25);
INSERT INTO products VALUES(182,'Yoga Mat (1pc)','Health & Fitness',500.0,18);
INSERT INTO products VALUES(183,'Dumbbells (Pair)','Health & Fitness',600.0,24);
INSERT INTO products VALUES(184,'Skipping Rope (1pc)','Health & Fitness',150.0,25);
INSERT INTO products VALUES(185,'Resistance Bands (Set of 3)','Health & Fitness',200.0,25);
INSERT INTO products VALUES(186,'Treadmill (1pc)','Health & Fitness',25000.0,25);
INSERT INTO products VALUES(187,'Barbell Set (1pc)','Health & Fitness',10000.0,25);
INSERT INTO products VALUES(188,'Running Shoes (1 pair)','Health & Fitness',1500.0,25);
INSERT INTO products VALUES(189,'Fitness Tracker (1pc)','Health & Fitness',3000.0,25);
INSERT INTO products VALUES(190,'Jumping Jacks (1pc)','Health & Fitness',120.0,25);
INSERT INTO products VALUES(191,'Exercise Ball (1pc)','Health & Fitness',300.0,25);
INSERT INTO products VALUES(192,'Foam Roller (1pc)','Health & Fitness',400.0,25);
INSERT INTO products VALUES(193,'Kettlebell (1pc)','Health & Fitness',700.0,25);
INSERT INTO products VALUES(194,'Cycling Gloves (1 pair)','Health & Fitness',200.0,25);
INSERT INTO products VALUES(195,'Ankle Weights (Pair)','Health & Fitness',300.0,25);
INSERT INTO products VALUES(196,'Fitness Tracker Strap (1pc)','Health & Fitness',150.0,25);
INSERT INTO products VALUES(197,'Massage Gun (1pc)','Health & Fitness',3500.0,24);
INSERT INTO products VALUES(198,'Resistance Tube Set (1 set)','Health & Fitness',400.0,25);
INSERT INTO products VALUES(199,'Tennis Racket (1pc)','Health & Fitness',1500.0,25);
INSERT INTO products VALUES(200,'Swimming Goggles (1pc)','Health & Fitness',200.0,25);
INSERT INTO products VALUES(201,'Phone Case (1pc)','Electronics Accessories',300.0,25);
INSERT INTO products VALUES(202,'Screen Protector (1pc)','Electronics Accessories',150.0,25);
INSERT INTO products VALUES(203,'Charging Cable (1pc)','Electronics Accessories',200.0,25);
INSERT INTO products VALUES(204,'Earbuds (1pc)','Electronics Accessories',1000.0,25);
INSERT INTO products VALUES(205,'Laptop Bag (1pc)','Electronics Accessories',800.0,25);
INSERT INTO products VALUES(206,'Power Adapter (1pc)','Electronics Accessories',1200.0,25);
INSERT INTO products VALUES(207,'Wireless Charger (1pc)','Electronics Accessories',1500.0,25);
INSERT INTO products VALUES(208,'Bluetooth Adapter (1pc)','Electronics Accessories',400.0,25);
INSERT INTO products VALUES(209,'USB Flash Drive (16GB)','Electronics Accessories',300.0,25);
INSERT INTO products VALUES(210,'External Hard Drive (1TB)','Electronics Accessories',5000.0,25);
INSERT INTO products VALUES(211,'Car Charger (1pc)','Electronics Accessories',600.0,23);
INSERT INTO products VALUES(212,'MicroSD Card (32GB)','Electronics Accessories',350.0,25);
INSERT INTO products VALUES(213,'Laptop Stand (1pc)','Electronics Accessories',500.0,25);
INSERT INTO products VALUES(214,'Phone Holder (1pc)','Electronics Accessories',250.0,25);
INSERT INTO products VALUES(215,'Camera Lens (1pc)','Electronics Accessories',3000.0,25);
INSERT INTO products VALUES(216,'Bluetooth Receiver (1pc)','Electronics Accessories',500.0,25);
INSERT INTO products VALUES(217,'Smartphone Mount (1pc)','Electronics Accessories',350.0,25);
INSERT INTO products VALUES(218,'Portable Speaker (1pc)','Electronics Accessories',2500.0,21);
INSERT INTO products VALUES(219,'Noise Cancelling Headphones (1pc)','Electronics Accessories',5000.0,25);
INSERT INTO products VALUES(220,'Laptop Cooling Pad (1pc)','Electronics Accessories',600.0,25);
INSERT INTO products VALUES(221,'Smartphone Tripod (1pc)','Electronics Accessories',450.0,25);
INSERT INTO products VALUES(222,'Wireless Earphones (1pc)','Electronics Accessories',2000.0,20);
INSERT INTO products VALUES(223,'Charging Dock (1pc)','Electronics Accessories',700.0,25);
INSERT INTO products VALUES(224,'Stylus Pen (1pc)','Electronics Accessories',300.0,25);
INSERT INTO products VALUES(225,'Laptop Sleeve (1pc)','Electronics Accessories',500.0,25);
INSERT INTO products VALUES(226,'Blender (1pc)','Home Appliances',2500.0,25);
INSERT INTO products VALUES(227,'Mixer Grinder (1pc)','Home Appliances',3000.0,25);
INSERT INTO products VALUES(228,'Juicer (1pc)','Home Appliances',2000.0,25);
INSERT INTO products VALUES(229,'Coffee Maker (1pc)','Home Appliances',2000.0,25);
INSERT INTO products VALUES(230,'Toaster (1pc)','Home Appliances',1200.0,25);
INSERT INTO products VALUES(231,'Electric Kettle (1pc)','Home Appliances',800.0,25);
INSERT INTO products VALUES(232,'Rice Cooker (1pc)','Home Appliances',2500.0,25);
INSERT INTO products VALUES(233,'Oven Toaster Grill (1pc)','Home Appliances',5000.0,25);
INSERT INTO products VALUES(234,'Induction Cooktop (1pc)','Home Appliances',3000.0,25);
INSERT INTO products VALUES(235,'Washing Machine (1pc)','Home Appliances',15000.0,25);
INSERT INTO products VALUES(236,'Microwave Oven (1pc)','Home Appliances',8000.0,25);
INSERT INTO products VALUES(237,'Refrigerator (1pc)','Home Appliances',20000.0,25);
INSERT INTO products VALUES(238,'Air Purifier (1pc)','Home Appliances',35000.0,25);
INSERT INTO products VALUES(239,'Dishwasher (1pc)','Home Appliances',15000.0,25);
INSERT INTO products VALUES(240,'Vacuum Cleaner (1pc)','Home Appliances',6000.0,25);
INSERT INTO products VALUES(241,'Air Conditioner (1pc)','Home Appliances',25000.0,25);
INSERT INTO products VALUES(242,'Water Heater (1pc)','Home Appliances',5000.0,24);
INSERT INTO products VALUES(243,'Deep Fryer (1pc)','Home Appliances',3500.0,25);
INSERT INTO products VALUES(244,'Food Processor (1pc)','Home Appliances',4000.0,25);
INSERT INTO products VALUES(245,'Slow Cooker (1pc)','Home Appliances',2500.0,25);
INSERT INTO products VALUES(246,'Bread Maker (1pc)','Home Appliances',6000.0,25);
INSERT INTO products VALUES(247,'Electric Grill (1pc)','Home Appliances',3000.0,25);
INSERT INTO products VALUES(248,'Hair Dryer (1pc)','Home Appliances',1500.0,22);
INSERT INTO products VALUES(249,'Electric Iron (1pc)','Home Appliances',1000.0,25);
INSERT INTO products VALUES(250,'Dehumidifier (1pc)','Home Appliances',8000.0,25);
INSERT INTO products VALUES(251,'Building Blocks (100 pcs)','Toys & Games',500.0,25);
INSERT INTO products VALUES(252,'Action Figures (Set of 5)','Toys & Games',700.0,25);
INSERT INTO products VALUES(253,'Board Game (1pc)','Toys & Games',800.0,25);
INSERT INTO products VALUES(254,'Dolls (Set of 2)','Toys & Games',600.0,25);
INSERT INTO products VALUES(255,'Jigsaw Puzzle (500 pcs)','Toys & Games',400.0,25);
INSERT INTO products VALUES(256,'RC Car (1pc)','Toys & Games',1200.0,25);
INSERT INTO products VALUES(257,'Rubiks Cube (1pc)','Toys & Games',200.0,25);
INSERT INTO products VALUES(258,'Toy Train Set (1pc)','Toys & Games',1500.0,25);
INSERT INTO products VALUES(259,'Action Figures (Set of 3)','Toys & Games',600.0,25);
INSERT INTO products VALUES(260,'Stuffed Toys (1pc)','Toys & Games',350.0,25);
INSERT INTO products VALUES(261,'Toy Kitchen Set (1pc)','Toys & Games',700.0,25);
INSERT INTO products VALUES(262,'Pretend Play Set (1pc)','Toys & Games',400.0,25);
INSERT INTO products VALUES(263,'Soft Toy (1pc)','Toys & Games',300.0,25);
INSERT INTO products VALUES(264,'Toy Cars (Pack of 5)','Toys & Games',500.0,24);
INSERT INTO products VALUES(265,'Puzzle Cube (1pc)','Toys & Games',250.0,25);
INSERT INTO products VALUES(266,'Play-Doh (Set of 4)','Toys & Games',300.0,25);
INSERT INTO products VALUES(267,'Dollhouse (1pc)','Toys & Games',1500.0,25);
INSERT INTO products VALUES(268,'Bicycle (1pc)','Toys & Games',3000.0,25);
INSERT INTO products VALUES(269,'Teddy Bear (1pc)','Toys & Games',400.0,25);
INSERT INTO products VALUES(270,'Kite (1pc)','Toys & Games',150.0,25);
INSERT INTO products VALUES(271,'Toy Robot (1pc)','Toys & Games',1000.0,25);
INSERT INTO products VALUES(272,'Outdoor Play Set (1pc)','Toys & Games',1500.0,25);
INSERT INTO products VALUES(273,'Magic Tricks Set (1pc)','Toys & Games',250.0,25);
INSERT INTO products VALUES(274,'Basketball (1pc)','Toys & Games',500.0,24);
INSERT INTO products VALUES(275,'Bow & Arrow Set (1pc)','Toys & Games',400.0,25);
INSERT INTO products VALUES(276,'T-Shirt (1pc)','Clothing & Apparel',300.0,25);
INSERT INTO products VALUES(277,'Jeans (1pc)','Clothing & Apparel',800.0,25);
INSERT INTO products VALUES(278,'Jacket (1pc)','Clothing & Apparel',1500.0,25);
INSERT INTO products VALUES(279,'Sweater (1pc)','Clothing & Apparel',1200.0,24);
INSERT INTO products VALUES(280,'Hoodie (1pc)','Clothing & Apparel',1500.0,25);
INSERT INTO products VALUES(281,'Dress (1pc)','Clothing & Apparel',1200.0,21);
INSERT INTO products VALUES(282,'Shirt (1pc)','Clothing & Apparel',600.0,19);
INSERT INTO products VALUES(283,'Shorts (1pc)','Clothing & Apparel',400.0,25);
INSERT INTO products VALUES(284,'Skirt (1pc)','Clothing & Apparel',700.0,25);
INSERT INTO products VALUES(285,'Blouse (1pc)','Clothing & Apparel',600.0,25);
INSERT INTO products VALUES(286,'Sweatpants (1pc)','Clothing & Apparel',700.0,22);
INSERT INTO products VALUES(287,'Cargo Pants (1pc)','Clothing & Apparel',900.0,25);
INSERT INTO products VALUES(288,'Pajama Set (1pc)','Clothing & Apparel',800.0,25);
INSERT INTO products VALUES(289,'Socks (Pack of 3)','Clothing & Apparel',150.0,16);
INSERT INTO products VALUES(290,'Underwear (Pack of 3)','Clothing & Apparel',200.0,25);
INSERT INTO products VALUES(291,'Tights (1pc)','Clothing & Apparel',300.0,25);
INSERT INTO products VALUES(292,'Shoes (1 pair)','Clothing & Apparel',1200.0,25);
INSERT INTO products VALUES(293,'Boots (1 pair)','Clothing & Apparel',1500.0,21);
INSERT INTO products VALUES(294,'Sandals (1 pair)','Clothing & Apparel',600.0,25);
INSERT INTO products VALUES(295,'Flip Flops (1 pair)','Clothing & Apparel',200.0,25);
INSERT INTO products VALUES(296,'Scarf (1pc)','Clothing & Apparel',300.0,25);
INSERT INTO products VALUES(297,'Gloves (1 pair)','Clothing & Apparel',250.0,25);
INSERT INTO products VALUES(298,'Belt (1pc)','Clothing & Apparel',400.0,25);
INSERT INTO products VALUES(299,'Hat (1pc)','Clothing & Apparel',500.0,23);
INSERT INTO products VALUES(300,'Fiction Book (1pc)','Books',400.0,25);
INSERT INTO products VALUES(301,'Non-Fiction Book (1pc)','Books',500.0,25);
INSERT INTO products VALUES(302,'Childrens Book (1pc)','Books',300.0,18);
INSERT INTO products VALUES(303,'Cookbook (1pc)','Books',600.0,25);
INSERT INTO products VALUES(304,'Science Fiction (1pc)','Books',450.0,25);
INSERT INTO products VALUES(305,'Mystery Novel (1pc)','Books',350.0,25);
INSERT INTO products VALUES(306,'Biography (1pc)','Books',550.0,25);
INSERT INTO products VALUES(307,'Travel Book (1pc)','Books',400.0,25);
INSERT INTO products VALUES(308,'Self-Help Book (1pc)','Books',500.0,25);
INSERT INTO products VALUES(309,'Textbook (1pc)','Books',800.0,25);
INSERT INTO products VALUES(310,'Art Book (1pc)','Books',600.0,24);
INSERT INTO products VALUES(311,'Poetry Book (1pc)','Books',350.0,25);
INSERT INTO products VALUES(312,'History Book (1pc)','Books',600.0,25);
INSERT INTO products VALUES(313,'Philosophy Book (1pc)','Books',700.0,25);
INSERT INTO products VALUES(314,'Motivational Book (1pc)','Books',450.0,25);
INSERT INTO products VALUES(315,'Spiritual Book (1pc)','Books',400.0,25);
INSERT INTO products VALUES(316,'Language Learning Book (1pc)','Books',300.0,25);
INSERT INTO products VALUES(317,'Comic Book (1pc)','Books',250.0,25);
INSERT INTO products VALUES(318,'Graphic Novel (1pc)','Books',500.0,25);
INSERT INTO products VALUES(319,'Poetry Anthology (1pc)','Books',350.0,25);
INSERT INTO products VALUES(320,'Philosophy Guide (1pc)','Books',600.0,25);
INSERT INTO products VALUES(321,'Travel Guide (1pc)','Books',500.0,25);
INSERT INTO products VALUES(322,'Photography Book (1pc)','Books',700.0,25);
INSERT INTO products VALUES(323,'Cookbook (Vegetarian) (1pc)','Books',500.0,25);
INSERT INTO products VALUES(324,'Motivational Speaker (1pc)','Books',600.0,25);
INSERT INTO products VALUES(325,'Camping Tent (1pc)','Sports & Outdoors',5000.0,25);
INSERT INTO products VALUES(326,'Hiking Boots (1 pair)','Sports & Outdoors',2000.0,24);
INSERT INTO products VALUES(327,'Sleeping Bag (1pc)','Sports & Outdoors',1500.0,25);
INSERT INTO products VALUES(328,'Fishing Rod (1pc)','Sports & Outdoors',1000.0,25);
INSERT INTO products VALUES(329,'Tent Light (1pc)','Sports & Outdoors',600.0,25);
INSERT INTO products VALUES(330,'Trekking Poles (1 pair)','Sports & Outdoors',700.0,25);
INSERT INTO products VALUES(331,'Backpack (1pc)','Sports & Outdoors',1200.0,22);
INSERT INTO products VALUES(332,'Cycling Helmet (1pc)','Sports & Outdoors',1000.0,25);
INSERT INTO products VALUES(333,'Tennis Racket (1pc)','Sports & Outdoors',1500.0,25);
INSERT INTO products VALUES(334,'Soccer Ball (1pc)','Sports & Outdoors',500.0,19);
INSERT INTO products VALUES(335,'Basketball (1pc)','Sports & Outdoors',600.0,24);
INSERT INTO products VALUES(336,'Golf Clubs (Set)','Sports & Outdoors',3000.0,21);
INSERT INTO products VALUES(337,'Badminton Racket (1pc)','Sports & Outdoors',600.0,25);
INSERT INTO products VALUES(338,'Camping Stove (1pc)','Sports & Outdoors',1500.0,25);
INSERT INTO products VALUES(339,'Yoga Mat (1pc)','Sports & Outdoors',500.0,18);
INSERT INTO products VALUES(340,'Water Bottle (1pc)','Sports & Outdoors',200.0,17);
INSERT INTO products VALUES(341,'Climbing Gear Set (1 set)','Sports & Outdoors',2500.0,25);
INSERT INTO products VALUES(342,'Football Cleats (1 pair)','Sports & Outdoors',1500.0,23);
INSERT INTO products VALUES(343,'Running Shoes (1 pair)','Sports & Outdoors',1000.0,25);
INSERT INTO products VALUES(344,'Ski Goggles (1pc)','Sports & Outdoors',2000.0,22);
INSERT INTO products VALUES(345,'Outdoor Chair (1pc)','Sports & Outdoors',800.0,13);
INSERT INTO products VALUES(346,'Bicycle Pump (1pc)','Sports & Outdoors',300.0,21);
INSERT INTO products VALUES(347,'Camping Lantern (1pc)','Sports & Outdoors',500.0,23);
INSERT INTO products VALUES(348,'First Aid Kit (1pc)','Sports & Outdoors',800.0,25);
INSERT INTO products VALUES(349,'Hand Warmer (1pc)','Sports & Outdoors',200.0,23);
INSERT INTO products VALUES(350,'Beach Towel (1pc)','Clothing & Apparel',500.0,30);
INSERT INTO products VALUES(351,'Sunglasses (1pc)','Clothing & Apparel',300.0,100);
INSERT INTO products VALUES(352,'Beach Umbrella (1pc)','Sports & Outdoors',1800.0,25);
INSERT INTO products VALUES(353,'Shower Curtain (1pc)','Household',499.0,50);
INSERT INTO products VALUES(354,'Stain Remover (500ml)','Household',299.0,100);
INSERT INTO products VALUES(355,'Hand Wash (500ml)','Household',149.0,200);
INSERT INTO products VALUES(356,'Clothes Drying Rack (1pc)','Household',899.0,30);
INSERT INTO products VALUES(357,'Lint Roller (1pc)','Household',199.0,150);
INSERT INTO products VALUES(358,'Cloth Napkins (Set of 4)','Household',349.0,75);
INSERT INTO products VALUES(359,'Kitchen Wipes (Pack of 20)','Household',249.0,120);
INSERT INTO products VALUES(360,'Microwave-Safe Bowls (Set of 3)','Household',599.0,60);
INSERT INTO products VALUES(361,'Oven Cleaner (500ml)','Household',349.0,80);
INSERT INTO products VALUES(362,'Food Storage Containers (Set of 3)','Household',699.0,88);
INSERT INTO products VALUES(363,'Baking Paper (Roll)','Household',199.0,200);
INSERT INTO products VALUES(364,'Bath Mat (1pc)','Household',499.0,69);
INSERT INTO products VALUES(365,'Paper Towels (Pack of 2)','Household',199.0,150);
INSERT INTO products VALUES(366,'Disinfectant Spray (500ml)','Household',299.0,100);
INSERT INTO products VALUES(367,'Fabric Softener (1L)','Household',399.0,80);
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    smart_coins REAL DEFAULT 0.0
);
INSERT INTO customers VALUES(1,'Neel','+919313096094','neel123',0.0);
INSERT INTO customers VALUES(2,'Priya Sharma','+919123456789','priya2025',0.0);
INSERT INTO customers VALUES(3,'Amit Patel','+919988776655','amit@1234',0.0);
INSERT INTO customers VALUES(4,'Neha Verma','+918999001122','neha5678',0.0);
INSERT INTO customers VALUES(5,'Suresh Rao','+919909956635','suresh@987',0.0);
INSERT INTO customers VALUES(6,'Ishan','+919106550238','abc@123',351.3299999999996998);
CREATE TABLE discount_coupons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coupon_code TEXT UNIQUE NOT NULL,
    category TEXT NOT NULL,  
    discount_percentage REAL NOT NULL,
    expiry_date DATE NOT NULL
);
INSERT INTO discount_coupons VALUES(1,'DISCOUNT15','Electronics Accessories',15.0,'2025-12-31');
INSERT INTO discount_coupons VALUES(2,'FESTIVE20','Clothing & Apparel',20.0,'2025-12-31');
INSERT INTO discount_coupons VALUES(3,'SUMMER10','Snacks',10.0,'2025-06-30');
INSERT INTO discount_coupons VALUES(4,'NEWYEAR25','Personal Care',25.0,'2025-01-31');
INSERT INTO discount_coupons VALUES(5,'WINTER30','Household',30.0,'2025-12-31');
INSERT INTO discount_coupons VALUES(8,'SPRING5','Household',5.0,'2025-04-22');
INSERT INTO discount_coupons VALUES(9,'TEST10','Bakery',10.0,'2025-04-21');
INSERT INTO discount_coupons VALUES(10,'TEST33','Personal Care',33.0,'2025-04-21');
INSERT INTO discount_coupons VALUES(11,'HELLO10','Bakery',22.0,'2025-06-02');
CREATE TABLE product_discounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,   -- Exact product name for the discount
    discount_type TEXT NOT NULL,  -- Type of discount (e.g., "Buy 2 Get 1 Free")
    discount_description TEXT NOT NULL  -- Description of the discount
);
INSERT INTO product_discounts VALUES(1,'Milk (1L)','Buy 10 Get 1 Free','Buy 10 Milk and get 1 Milk free');
INSERT INTO product_discounts VALUES(2,'Multigrain Bread (500g)','Buy 20 Get 1 Free','Buy 20 Bread and get 1 Bread Free');
INSERT INTO product_discounts VALUES(3,'Apples (1kg)','Buy 15 Get 1 Free','Buy 15 Apples and get 1 Apple free');
INSERT INTO product_discounts VALUES(4,'Bananas (1kg)','Buy 20 Get 1 Free','Buy 20 Bananas and get 1 Banana free');
INSERT INTO product_discounts VALUES(5,'Toothpaste (100g)','Buy 3 Get 1 Free','Buy 3 Toothpaste and get 1 Toothpaste free');
INSERT INTO product_discounts VALUES(6,'Shirt (1pc)','Buy 5 Get 1 Free','Buy 5 Shirt and get 1 Shirt free');
INSERT INTO product_discounts VALUES(7,'Coffee Beans (200g)','Buy 20 Get 2 Free','Buy 20 Coffee Beans and get 2 Coffee Beans  free');
CREATE TABLE returned_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_id INTEGER,
    product_name TEXT,
    reason TEXT,
    quantity INTEGER,
    FOREIGN KEY (bill_id) REFERENCES bills(id)
);
INSERT INTO returned_products VALUES(15,37,'Outdoor Chair (1pc)','Don''t Like the Quality of Product',2);
CREATE TABLE top_items (
    customer_mobile TEXT,
    item_name TEXT,
    total_quantity INTEGER,
    PRIMARY KEY (customer_mobile, item_name)
);
INSERT INTO top_items VALUES('+919106550238','Milk (1L)',4);
INSERT INTO top_items VALUES('+919106550238','Outdoor Chair (1pc)',2);
INSERT INTO top_items VALUES('+919106550238','Milk Powder (500g)',3);
INSERT INTO top_items VALUES('+919106550238','Ghee (1kg)',3);
INSERT INTO top_items VALUES('+919106550238','Skim Milk (1L)',2);
INSERT INTO top_items VALUES('+919106550238','Hair Oil (200ml)',2);
INSERT INTO top_items VALUES('+919106550238','Football Cleats (1 pair)',2);
INSERT INTO top_items VALUES('+919106550238','Soccer Ball (1pc)',3);
CREATE TABLE bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_mobile TEXT NOT NULL,
    bill_date TEXT NOT NULL,
    total_amount REAL NOT NULL,
    discount REAL NOT NULL,
    final_amount REAL NOT NULL,
    FOREIGN KEY (customer_mobile) REFERENCES customers(phone)  -- Assuming the phone number is unique in the customers table
);
INSERT INTO bills VALUES(36,'+919106550238','2025-02-13',480.0,0.0,566.3999999999999773);
INSERT INTO bills VALUES(37,'+919106550238','2025-02-13',1600.0,28.0,1860.0);
INSERT INTO bills VALUES(38,'+919106550238','2025-02-14',8740.0,3293.0,7020.199999999999819);
CREATE TABLE category_spending (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_mobile TEXT NOT NULL,
    category TEXT NOT NULL,
    total_spent REAL NOT NULL,
    total_items INTEGER NOT NULL,
    bill_id INTEGER NOT NULL,
    FOREIGN KEY (bill_id) REFERENCES bills(id),
    UNIQUE (customer_mobile, category, bill_id)
);
INSERT INTO category_spending VALUES(63,'+919106550238','Dairy',566.3999999999999773,4,36);
INSERT INTO category_spending VALUES(64,'+919106550238','Sports & Outdoors',1860.0,2,37);
INSERT INTO category_spending VALUES(65,'+919106550238','Dairy',9210.200000000000728,8,38);
INSERT INTO category_spending VALUES(68,'+919106550238','Personal Care',7020.199999999999819,2,38);
INSERT INTO category_spending VALUES(69,'+919106550238','Sports & Outdoors',8520.200000000000728,5,38);
INSERT INTO category_spending VALUES(71,'+919106550238','Fruits',7020.199999999999819,2,38);
CREATE TABLE monthly_spending (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_mobile TEXT NOT NULL,
    category TEXT NOT NULL,
    total_spent REAL NOT NULL,
    total_items INTEGER NOT NULL,
    bill_date TEXT NOT NULL,
    bill_id INTEGER NOT NULL,
    FOREIGN KEY (bill_id) REFERENCES bills(id),
    UNIQUE (customer_mobile, category, bill_date, bill_id)
);
INSERT INTO monthly_spending VALUES(63,'+919106550238','Dairy',566.3999999999999773,4,'13-02-2025',36);
INSERT INTO monthly_spending VALUES(64,'+919106550238','Sports & Outdoors',1860.0,2,'13-02-2025',37);
INSERT INTO monthly_spending VALUES(65,'+919106550238','Dairy',9210.200000000000728,8,'14-02-2025',38);
INSERT INTO monthly_spending VALUES(68,'+919106550238','Personal Care',7020.199999999999819,2,'14-02-2025',38);
INSERT INTO monthly_spending VALUES(69,'+919106550238','Sports & Outdoors',8520.200000000000728,5,'14-02-2025',38);
INSERT INTO monthly_spending VALUES(71,'+919106550238','Fruits',7020.199999999999819,2,'14-02-2025',38);
CREATE TABLE item_purchase_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_mobile TEXT NOT NULL,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    bill_id INTEGER,
    price REAL,
    FOREIGN KEY (bill_id) REFERENCES bills(id),
    UNIQUE(customer_mobile, item_name, bill_id)  -- Ensure no duplicate records for a combination of these three columns
);
INSERT INTO item_purchase_history VALUES(62,'+919106550238','Milk (1L)',4,36,120.0);
INSERT INTO item_purchase_history VALUES(63,'+919106550238','Outdoor Chair (1pc)',2,37,800.0);
INSERT INTO item_purchase_history VALUES(64,'+919106550238','Milk Powder (500g)',3,38,350.0);
INSERT INTO item_purchase_history VALUES(65,'+919106550238','Ghee (1kg)',3,38,650.0);
INSERT INTO item_purchase_history VALUES(66,'+919106550238','Skim Milk (1L)',2,38,120.0);
INSERT INTO item_purchase_history VALUES(67,'+919106550238','Hair Oil (200ml)',2,38,150.0);
INSERT INTO item_purchase_history VALUES(68,'+919106550238','Football Cleats (1 pair)',2,38,1500.0);
INSERT INTO item_purchase_history VALUES(69,'+919106550238','Soccer Ball (1pc)',3,38,500.0);
INSERT INTO item_purchase_history VALUES(70,'+919106550238','Mangoes (1kg)',2,38,350.0);
CREATE TABLE manager (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
INSERT INTO manager VALUES(1,'admin1','abcd');
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_mobile TEXT NOT NULL,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5) NOT NULL,
    feedback TEXT
);
INSERT INTO feedback VALUES(1,'Ishan','+919106550238',4,'good man');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('products',367);
INSERT INTO sqlite_sequence VALUES('customers',9);
INSERT INTO sqlite_sequence VALUES('discount_coupons',11);
INSERT INTO sqlite_sequence VALUES('product_discounts',7);
INSERT INTO sqlite_sequence VALUES('bills',38);
INSERT INTO sqlite_sequence VALUES('category_spending',71);
INSERT INTO sqlite_sequence VALUES('monthly_spending',71);
INSERT INTO sqlite_sequence VALUES('item_purchase_history',70);
INSERT INTO sqlite_sequence VALUES('returned_products',15);
INSERT INTO sqlite_sequence VALUES('manager',1);
INSERT INTO sqlite_sequence VALUES('feedback',1);
COMMIT;
