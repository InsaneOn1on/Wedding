<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h1 class="couple-names">The Kendalls</h1>
        <p class="tagline">Join us in celebrating our love</p>
        <div class="wedding-date">
          <p class="date">June 15, 2026</p>
          <p class="venue">The Grand Ballroom</p>
        </div>
        <router-link to="/rsvp" class="cta-button">RSVP Now</router-link>
      </div>
    </section>

    <section class="info-section">
      <div class="container">
        <div class="info-grid">
          <div class="info-card">
            <h2>Ceremony</h2>
            <p>3:00 PM</p>
            <p>Garden Terrace</p>
          </div>
          <div class="info-card">
            <h2>Reception</h2>
            <p>5:00 PM</p>
            <p>Grand Ballroom</p>
          </div>
          <div class="info-card">
            <h2>Dress Code</h2>
            <p>Formal Attire</p>
            <p>Black Tie Optional</p>
          </div>
        </div>
      </div>
    </section>

    <section class="story-section">
      <div class="container">
        <h2>Our Story</h2>
        <p class="story-text">
          We are so excited to celebrate this special day with our family and friends. 
          Your presence means the world to us as we begin this new chapter together.
        </p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 8rem 2rem;
  text-align: center;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
}

.couple-names {
  font-size: 4rem;
  margin-bottom: 1rem;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.tagline {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  font-weight: 300;
}

.wedding-date {
  margin: 3rem 0;
  padding: 2rem;
  background: rgba(255,255,255,0.1);
  border-radius: 10px;
  backdrop-filter: blur(10px);
}

.date {
  font-size: 2rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.venue {
  font-size: 1.3rem;
  font-weight: 300;
}

.cta-button {
  display: inline-block;
  background: white;
  color: #667eea;
  padding: 1rem 3rem;
  text-decoration: none;
  border-radius: 50px;
  font-size: 1.2rem;
  font-weight: 600;
  transition: transform 0.3s, box-shadow 0.3s;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

.info-section {
  padding: 4rem 2rem;
  background: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.info-card {
  padding: 2rem;
  background: #f7fafc;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  transition: transform 0.3s;
}

.info-card:hover {
  transform: translateY(-5px);
}

.info-card h2 {
  color: #667eea;
  margin-bottom: 1rem;
  font-size: 1.8rem;
}

.info-card p {
  font-size: 1.1rem;
  margin: 0.5rem 0;
}

.story-section {
  padding: 4rem 2rem;
  background: linear-gradient(to bottom, #f7fafc, #edf2f7);
  text-align: center;
}

.story-section h2 {
  font-size: 2.5rem;
  color: #667eea;
  margin-bottom: 2rem;
}

.story-text {
  max-width: 800px;
  margin: 0 auto;
  font-size: 1.2rem;
  line-height: 1.8;
  color: #4a5568;
}

@media (max-width: 768px) {
  .couple-names {
    font-size: 2.5rem;
  }
  
  .tagline {
    font-size: 1.2rem;
  }
  
  .info-grid {
    grid-template-columns: 1fr;
  }
}
</style>
