<template>
  <div class="rsvp">
    <div class="container">
      <h1>RSVP</h1>
      <p class="subtitle">We can't wait to celebrate with you!</p>
      
      <form @submit.prevent="submitRSVP" class="rsvp-form" v-if="!submitted">
        <div class="form-group">
          <label for="name">Full Name *</label>
          <input 
            type="text" 
            id="name" 
            v-model="formData.name" 
            required 
            placeholder="John Doe"
          />
        </div>

        <div class="form-group">
          <label for="email">Email Address *</label>
          <input 
            type="email" 
            id="email" 
            v-model="formData.email" 
            required 
            placeholder="john@example.com"
          />
        </div>

        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input 
            type="tel" 
            id="phone" 
            v-model="formData.phone" 
            placeholder="(123) 456-7890"
          />
        </div>

        <div class="form-group">
          <label for="guests">Number of Guests *</label>
          <input 
            type="number" 
            id="guests" 
            v-model="formData.guests" 
            required 
            min="1"
            max="10"
          />
        </div>

        <div class="form-group">
          <label>Will you be attending? *</label>
          <div class="radio-group">
            <label class="radio-label">
              <input type="radio" v-model="formData.attending" value="yes" required />
              <span>Yes, I'll be there!</span>
            </label>
            <label class="radio-label">
              <input type="radio" v-model="formData.attending" value="no" />
              <span>Sorry, can't make it</span>
            </label>
          </div>
        </div>

        <div class="form-group">
          <label for="dietary">Dietary Restrictions</label>
          <textarea 
            id="dietary" 
            v-model="formData.dietary" 
            rows="3"
            placeholder="Please let us know if you have any dietary restrictions..."
          ></textarea>
        </div>

        <div class="form-group">
          <label for="message">Message to the Couple</label>
          <textarea 
            id="message" 
            v-model="formData.message" 
            rows="4"
            placeholder="Share your thoughts and well wishes..."
          ></textarea>
        </div>

        <button type="submit" class="submit-button" :disabled="loading">
          {{ loading ? 'Submitting...' : 'Submit RSVP' }}
        </button>

        <p v-if="error" class="error-message">{{ error }}</p>
      </form>

      <div v-if="submitted" class="success-message">
        <h2>Thank You!</h2>
        <p>Your RSVP has been received. We're looking forward to seeing you!</p>
        <button @click="resetForm" class="reset-button">Submit Another RSVP</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RSVP',
  data() {
    return {
      formData: {
        name: '',
        email: '',
        phone: '',
        guests: 1,
        attending: '',
        dietary: '',
        message: ''
      },
      loading: false,
      error: '',
      submitted: false
    }
  },
  methods: {
    async submitRSVP() {
      this.loading = true
      this.error = ''
      
      try {
        const response = await axios.post('/api/rsvp', this.formData)
        console.log('RSVP submitted:', response.data)
        this.submitted = true
      } catch (err) {
        console.error('Error submitting RSVP:', err)
        this.error = 'Failed to submit RSVP. Please try again.'
      } finally {
        this.loading = false
      }
    },
    resetForm() {
      this.formData = {
        name: '',
        email: '',
        phone: '',
        guests: 1,
        attending: '',
        dietary: '',
        message: ''
      }
      this.submitted = false
      this.error = ''
    }
  }
}
</script>

<style scoped>
.rsvp {
  padding: 4rem 2rem;
  background: linear-gradient(to bottom, #f7fafc, #edf2f7);
  min-height: calc(100vh - 200px);
}

.container {
  max-width: 700px;
  margin: 0 auto;
}

h1 {
  font-size: 3rem;
  text-align: center;
  color: #667eea;
  margin-bottom: 1rem;
}

.subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: #4a5568;
  margin-bottom: 3rem;
}

.rsvp-form {
  background: white;
  padding: 3rem;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 2rem;
}

label {
  display: block;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 0.5rem;
}

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="number"],
textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #667eea;
}

.radio-group {
  display: flex;
  gap: 2rem;
  margin-top: 0.5rem;
}

.radio-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  font-weight: normal;
}

.radio-label input[type="radio"] {
  width: auto;
  cursor: pointer;
}

.submit-button {
  width: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1rem;
  border: none;
  border-radius: 50px;
  font-size: 1.2rem;
  font-weight: 600;
  transition: transform 0.3s, box-shadow 0.3s;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.submit-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
}

.submit-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  color: #e53e3e;
  text-align: center;
  margin-top: 1rem;
  font-weight: 600;
}

.success-message {
  background: white;
  padding: 3rem;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  text-align: center;
}

.success-message h2 {
  color: #48bb78;
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.success-message p {
  font-size: 1.2rem;
  color: #4a5568;
  margin-bottom: 2rem;
}

.reset-button {
  background: #667eea;
  color: white;
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  transition: transform 0.3s;
}

.reset-button:hover {
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .rsvp-form {
    padding: 2rem 1.5rem;
  }
  
  h1 {
    font-size: 2rem;
  }
  
  .radio-group {
    flex-direction: column;
    gap: 1rem;
  }
}
</style>
