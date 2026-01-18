<template>
  <div class="schedule">
    <section class="schedule-section">
      <div class="container">
        <h1>Schedule</h1>
        <div class="timeline">
          <div class="timeline-item">
            <div class="time">3:00 PM</div>
            <div class="event">
              <h3>Ceremony</h3>
              <p>Garden Terrace</p>
              <p class="description">Join us as we exchange vows in a beautiful garden setting</p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="time">4:00 PM</div>
            <div class="event">
              <h3>Cocktail Hour</h3>
              <p>Grand Terrace</p>
              <p class="description">Enjoy drinks and hors d'oeuvres while we take photos</p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="time">5:00 PM</div>
            <div class="event">
              <h3>Reception</h3>
              <p>Grand Ballroom</p>
              <p class="description">Dinner, dancing, and celebration</p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="time">10:00 PM</div>
            <div class="event">
              <h3>Last Dance</h3>
              <p>Grand Ballroom</p>
              <p class="description">Send us off in style</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Schedule'
}
</script>

<style scoped>
.schedule {
  min-height: calc(100vh - 200px);
}

.schedule-section {
  padding: 6rem 2rem;
  background: #ffffff;
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
  margin-bottom: 4rem;
}

.timeline {
  position: relative;
  max-width: 800px;
  margin: 0 auto;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 2px;
  background: #1a1a1a;
  transform: translateX(-50%);
}

.timeline-item {
  display: flex;
  align-items: center;
  margin-bottom: 4rem;
  position: relative;
}

.timeline-item:nth-child(odd) {
  flex-direction: row;
}

.timeline-item:nth-child(even) {
  flex-direction: row-reverse;
}

.time {
  flex: 1;
  text-align: center;
  font-size: 1.5rem;
  font-weight: 600;
  color: #1a1a1a;
  padding: 0 2rem;
}

.event {
  flex: 1;
  text-align: left;
  padding: 2rem;
  background: #f5f5f5;
  border: 1px solid #1a1a1a;
  position: relative;
}

.timeline-item:nth-child(even) .event {
  text-align: right;
}

.event h3 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #1a1a1a;
  font-family: 'Playfair Display', serif;
  font-weight: 600;
}

.event p {
  font-size: 1rem;
  color: #666;
  margin: 0.25rem 0;
}

.event .description {
  font-size: 0.9rem;
  font-style: italic;
  margin-top: 0.5rem;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }
  
  .timeline::before {
    left: 0;
  }
  
  .timeline-item {
    flex-direction: column !important;
    align-items: flex-start;
  }
  
  .time {
    margin-bottom: 1rem;
    text-align: left;
    padding: 0;
  }
  
  .event {
    text-align: left !important;
    margin-left: 2rem;
  }
}
</style>
