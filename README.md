<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gurukul Shop - Your Online Store</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        /* Header Styles */
        .navbar {
            background: #333;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 2rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
        }

        .cart {
            background: #007bff;
            padding: 0.5rem 1rem;
            border-radius: 5px;
        }

        .menu-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Hero Styles */
        .hero {
            background: #f4f4f4;
            padding: 4rem 2rem;
            text-align: center;
        }

        .hero-content h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .hero-content p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }

        .shop-now {
            background: #007bff;
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1.1rem;
            cursor: pointer;
            border-radius: 5px;
        }

        /* Products Styles */
        .products {
            padding: 4rem 2rem;
            text-align: center;
        }

        .products h2 {
            margin-bottom: 2rem;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .product-card {
            background: white;
            padding: 1rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
        }

        .product-img {
            width: 100%;
            height: 200px;
            object-fit: cover; /* Ensures images maintain aspect ratio while filling container */
            border-radius: 5px;
            margin-bottom: 1rem;
        }

        .product-card h3 {
            margin-bottom: 0.5rem;
        }

        .product-card p {
            color: #007bff;
            margin-bottom: 1rem;
        }

        .product-card button {
            background: #28a745;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            cursor: pointer;
            border-radius: 5px;
            margin-top: auto; /* Pushes button to bottom of card */
        }

        /* Footer Styles */
        footer {
            background: #333;
            color: white;
            padding: 2rem;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .footer-section h3 {
            margin-bottom: 1rem;
        }

        .footer-section ul {
            list-style: none;
        }

        .footer-section a {
            color: white;
            text-decoration: none;
        }

        .footer-bottom {
            text-align: center;
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #555;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .menu-toggle {
                display: block;
            }

            .nav-links {
                display: none;
                position: absolute;
                top: 60px;
                left: 0;
                right: 0;
                background: #333;
                flex-direction: column;
                padding: 1rem;
            }

            .nav-links.active {
                display: flex;
            }

            .nav-links li {
                margin: 1rem 0;
            }

            .hero-content h1 {
                font-size: 2rem;
            }

            .hero-content p {
                font-size: 1rem;
            }
        }

        @media (max-width: 480px) {
            .hero {
                padding: 2rem 1rem;
            }

            .products {
                padding: 2rem 1rem;
            }

            .shop-now {
                padding: 0.8rem 1.5rem;
            }

            .product-img {
                height: 150px; /* Slightly smaller on mobile */
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <nav class="navbar">
            <div class="logo">Gurukul Shop</div>
            <div class="menu-toggle">☰</div>
            <ul class="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#">Shop</a></li>
                <li><a href="#">Categories</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#" class="cart">Cart (0)</a></li>
            </ul>
        </nav>
    </header>

    <!-- body -->
    <section class="hero">
        <div class="hero-content">
            <h1>Welcome to E-Shop</h1>
            <p>Discover amazing products at unbeatable prices</p>
            <button class="shop-now">Shop Now</button>
        </div>
    </section>

    <!-- Products Section -->
    <section class="products">
        <h2>Featured Products</h2>
        <div class="product-grid">
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cHJvZHVjdHxlbnwwfHwwfHx8MA%3D%3D" 
                     alt="Product 1" class="product-img">
                <h3>Product 1</h3>
                <p>$29.99</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-card">
                <img src="https://plus.unsplash.com/premium_photo-1679913792906-13ccc5c84d44?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cHJvZHVjdHxlbnwwfHwwfHx8MA%3D%3D" 
                     alt="Product 2" class="product-img">
                <h3>Product 2</h3>
                <p>$39.99</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8cHJvZHVjdHxlbnwwfHwwfHx8MA%3D%3D" 
                     alt="Product 3" class="product-img">
                <h3>Product 3</h3>
                <p>$19.99</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1553456558-aff63285bdd1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHByb2R1Y3R8ZW58MHx8MHx8fDA%3D" 
                     alt="Product 4" class="product-img">
                <h3>Product 4</h3>
                <p>$49.99</p>
                <button>Add to Cart</button>
            </div>
            <div class="product-card">
                <img src="https://media.istockphoto.com/id/1466000525/photo/woman-shopping-denim-jeans-in-a-clothing-store.webp?s=1024x1024&w=is&k=20&c=Aygyk8zu_3c9W-SlhqHzRr0a0MkzbcoVNQ4S4BqUK3s=" 
                     alt="Product 4" class="product-img">
                <h3>men febric jeans</h3>
                <p>$109.99</p>
                <button>Add to Cart</button>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>E-Shop</h3>
                <p>Your one-stop online store</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Service</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Contact</h3>
                <p>Email: support@eshop.com</p>
                <p>Phone: (555) 123-4567</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2025 E-Shop. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Simple mobile menu toggle
        document.querySelector('.menu-toggle').addEventListener('click', () => {
            document.querySelector('.nav-links').classList.toggle('active');
        });
    </script>
</body>
</html>
