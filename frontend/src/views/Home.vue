<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h1 class="couple-names">The Kendalls</h1>
        <p class="tagline">Join us in celebrating our love</p>
        <div class="wedding-date">
          <p class="date">March 27, 2027</p>
          <p class="venue">The Grand Ballroom</p>
        </div>
        <router-link to="/rsvp" class="cta-button">RSVP Now</router-link>
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
  background: #ffffff;
  color: #1a1a1a;
  padding: 8rem 2rem 4rem 2rem;
  text-align: center;
  position: relative;
  border-bottom: 1px solid #e0e0e0;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.couple-names {
  font-size: 5rem;
  margin-bottom: 1rem;
  font-weight: 400;
  color: #1a1a1a;
}

.tagline {
  font-size: 1.3rem;
  margin-bottom: 2rem;
  font-weight: 300;
  color: #666;
  font-style: italic;
}

.wedding-date {
  margin: 3rem 0;
  padding: 2rem;
  background: #f5f5f5;
  border-radius: 0;
  border: 1px solid #1a1a1a;
}

.date {
  font-size: 2rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #1a1a1a;
  font-family: 'Lato', sans-serif;
}

.venue {
  font-size: 1.2rem;
  font-weight: 300;
  color: #666;
}

.cta-button {
  display: inline-block;
  background: #1a1a1a;
  color: #ffffff;
  padding: 1rem 3rem;
  text-decoration: none;
  border-radius: 0;
  font-size: 1rem;
  font-weight: 400;
  transition: all 0.3s;
  border: 2px solid #1a1a1a;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.cta-button:hover {
  background: #ffffff;
  color: #1a1a1a;
}

@media (max-width: 768px) {
  .couple-names {
    font-size: 3rem;
  }
  
  .tagline {
    font-size: 1.1rem;
  }
}
</style>
