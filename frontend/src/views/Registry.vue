<template>
  <div class="registry">
    <div class="container">
      <h1>Gift Registry</h1>
      <p class="subtitle">Your presence is the greatest gift, but if you wish to honor us with a gift, we've registered at the following stores.</p>
      
      <div class="registry-grid">
        <div class="registry-card">
          <h2>Amazon</h2>
          <p>For all our home essentials and wish list items</p>
          <a href="https://www.amazon.com/wedding/registry" target="_blank" class="registry-button">View Registry</a>
        </div>
        
        <div class="registry-card">
          <h2>Target</h2>
          <p>Kitchen, bedding, and home decor</p>
          <a href="https://www.target.com/gift-registry" target="_blank" class="registry-button">View Registry</a>
        </div>
        
        <div class="registry-card">
          <h2>Crate & Barrel</h2>
          <p>Fine dinnerware and entertaining pieces</p>
          <a href="https://www.crateandbarrel.com/gift-registry" target="_blank" class="registry-button">View Registry</a>
        </div>
      </div>
      
      <div class="cash-gift-section">
        <h2>Monetary Gifts</h2>
        <p>If you prefer to give a monetary gift, we are saving for our honeymoon and first home together.</p>
        <p class="note">Details will be provided closer to the wedding date.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Registry'
}
</script>

<style scoped>
.registry {
  padding: 4rem 2rem;
  background: #ffffff;
  min-height: calc(100vh - 200px);
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
}

h1 {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #1a1a1a;
}

.subtitle {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 4rem;
  line-height: 1.6;
}

.registry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.registry-card {
  background: #f5f5f5;
  padding: 3rem 2rem;
  border: 1px solid #1a1a1a;
  transition: all 0.3s;
}

.registry-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.registry-card h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #1a1a1a;
  font-family: 'Playfair Display', serif;
  font-weight: 700;
}

.registry-card p {
  font-size: 1rem;
  color: #666;
  margin-bottom: 2rem;
}

.registry-button {
  display: inline-block;
  background: #1a1a1a;
  color: #ffffff;
  padding: 0.75rem 2rem;
  text-decoration: none;
  border: 2px solid #1a1a1a;
  font-size: 0.9rem;
  font-weight: 400;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.registry-button:hover {
  background: #ffffff;
  color: #1a1a1a;
}

.cash-gift-section {
  background: #f5f5f5;
  padding: 3rem 2rem;
  border: 1px solid #1a1a1a;
  margin-top: 3rem;
}

.cash-gift-section h2 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: #1a1a1a;
  font-family: 'Playfair Display', serif;
  font-weight: 700;
}

.cash-gift-section p {
  font-size: 1rem;
  color: #666;
  line-height: 1.6;
  margin: 1rem 0;
}

.note {
  font-style: italic;
  font-size: 0.95rem;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }
  
  .registry-grid {
    grid-template-columns: 1fr;
  }
}
</style>
