<template>
  <div class="our-story">
    <section class="our-story-section">
      <div class="container">
        <h1>Our Story</h1>
        <div class="story-content">
          <p class="story-text">
            We are so excited to celebrate this special day with our family and friends. 
            Your presence means the world to us as we begin this new chapter together.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'OurStory'
}
</script>

<style scoped>
.our-story {
  min-height: calc(100vh - 200px);
}

.our-story-section {
  padding: 6rem 2rem;
  background: #f5f5f5;
  text-align: center;
  min-height: calc(100vh - 200px);
}

.container {
  max-width: 1000px;
  margin: 0 auto;
}

h1 {
  font-size: 4rem;
  color: #1a1a1a;
  margin-bottom: 2rem;
}

.story-content {
  max-width: 800px;
  margin: 0 auto;
}

.story-text {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #666;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }
}
</style>
