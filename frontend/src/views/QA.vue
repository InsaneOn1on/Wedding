<template>
  <div class="qa">
    <div class="container">
      <h1>Questions & Answers</h1>
      <p class="subtitle">Everything you need to know about our special day</p>
      
      <div class="qa-list">
        <div class="qa-item">
          <h2>What is the dress code?</h2>
          <p>We request formal attire. Think cocktail dresses, suits, and elegant evening wear. We want you to feel comfortable and look your best!</p>
        </div>
        
        <div class="qa-item">
          <h2>Is parking available at the venue?</h2>
          <p>Yes! The Grand Ballroom offers complimentary valet parking for all guests. Please arrive 15-20 minutes early to allow time for parking.</p>
        </div>
        
        <div class="qa-item">
          <h2>Are children welcome?</h2>
          <p>We love your little ones, but we've decided to make this an adults-only celebration. We hope this gives you a chance to let your hair down and enjoy the evening!</p>
        </div>
        
        <div class="qa-item">
          <h2>What about accommodations?</h2>
          <p>We have reserved room blocks at the following hotels:</p>
          <ul>
            <li><strong>The Grand Hotel</strong> - 555-0100</li>
            <li><strong>Marriott Downtown</strong> - 555-0200</li>
            <li><strong>Hampton Inn</strong> - 555-0300</li>
          </ul>
          <p>Please mention the "Kendall Wedding" when booking to receive our group rate.</p>
        </div>
        
        <div class="qa-item">
          <h2>Can I bring a plus-one?</h2>
          <p>Due to venue capacity, we are only able to accommodate guests formally invited on your invitation. If you received a plus-one, it will be indicated on your invitation.</p>
        </div>
        
        <div class="qa-item">
          <h2>Will there be vegetarian/vegan options?</h2>
          <p>Absolutely! Please indicate any dietary restrictions when you RSVP, and we'll make sure there are delicious options for everyone.</p>
        </div>
        
        <div class="qa-item">
          <h2>When is the RSVP deadline?</h2>
          <p>Please RSVP by February 27, 2027. This gives us enough time to finalize details with our caterer and venue.</p>
        </div>
        
        <div class="qa-item">
          <h2>Will the ceremony and reception be indoors or outdoors?</h2>
          <p>Both the ceremony and reception will be held indoors at The Grand Ballroom, so no need to worry about weather!</p>
        </div>
        
        <div class="qa-item">
          <h2>Can we take photos during the ceremony?</h2>
          <p>We ask that you enjoy the ceremony unplugged. Our professional photographer will capture all the special moments, and we'll share them with you afterward. Feel free to take photos during the reception!</p>
        </div>
        
        <div class="qa-item">
          <h2>Is there an after-party?</h2>
          <p>The reception will go until 10:00 PM with our last dance. We encourage everyone to make the most of the evening and dance the night away with us!</p>
        </div>
      </div>
      
      <div class="contact-section">
        <h2>Still have questions?</h2>
        <p>Feel free to reach out to us directly or ask when you RSVP!</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QA'
}
</script>

<style scoped>
.qa {
  padding: 4rem 2rem;
  background: #ffffff;
  min-height: calc(100vh - 200px);
}

.container {
  max-width: 900px;
  margin: 0 auto;
}

h1 {
  font-size: 4rem;
  margin-bottom: 1rem;
  color: #1a1a1a;
  text-align: center;
}

.subtitle {
  font-size: 1.1rem;
  color: #666;
  text-align: center;
  margin-bottom: 4rem;
  line-height: 1.6;
}

.qa-list {
  margin-bottom: 4rem;
}

.qa-item {
  background: #f5f5f5;
  padding: 2.5rem;
  margin-bottom: 2rem;
  border: 1px solid #1a1a1a;
}

.qa-item h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #1a1a1a;
  font-family: 'Playfair Display', serif;
  font-weight: 600;
}

.qa-item p {
  font-size: 1rem;
  color: #666;
  line-height: 1.8;
  margin: 1rem 0;
}

.qa-item ul {
  margin: 1rem 0;
  padding-left: 1.5rem;
}

.qa-item li {
  font-size: 1rem;
  color: #666;
  line-height: 1.8;
  margin: 0.5rem 0;
}

.qa-item strong {
  color: #1a1a1a;
}

.contact-section {
  background: #1a1a1a;
  color: #ffffff;
  padding: 3rem 2rem;
  text-align: center;
}

.contact-section h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-family: 'Playfair Display', serif;
  font-weight: 700;
}

.contact-section p {
  font-size: 1rem;
  line-height: 1.6;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2.5rem;
  }
  
  .qa-item {
    padding: 1.5rem;
  }
  
  .qa-item h2 {
    font-size: 1.5rem;
  }
}
</style>
