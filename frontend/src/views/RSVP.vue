<template>
  <div class="rsvp">
    <div class="container">
      <h1>RSVP</h1>
      <p class="subtitle">We can't wait to celebrate with you!</p>
      
      <form @submit.prevent="submitRSVP" class="rsvp-form" v-if="!submitted && !existingRSVP">
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

      <div v-if="existingRSVP && !showUpdateForm" class="existing-rsvp-message">
        <h2>You&apos;ve Already RSVP&apos;d!</h2>
        <p class="existing-info">We found an existing RSVP for <strong>{{ existingRSVP.name }}</strong> ({{ existingRSVP.email }}).</p>
        <div class="existing-details">
          <p><strong>Status:</strong> {{ existingRSVP.attending === 'yes' ? 'Attending' : 'Not Attending' }}</p>
          <p><strong>Guests:</strong> {{ existingRSVP.guests }}</p>
        </div>
        <p class="update-prompt">Would you like to update your RSVP?</p>
        <button @click="showUpdate" class="update-button">Update My RSVP</button>
        <button @click="goHome" class="cancel-button">Return to Home</button>
      </div>

      <div v-if="existingRSVP && showUpdateForm" class="existing-rsvp-message">
        <h2>Update Your RSVP</h2>
        <p class="existing-info">Update your information below:</p>
        
        <form @submit.prevent="updateExistingRSVP" class="update-form">
          <div class="form-group">
            <label for="update-name">Full Name *</label>
            <input 
              type="text" 
              id="update-name" 
              v-model="updateData.name" 
              required 
              placeholder="John Doe"
            />
          </div>

          <div class="form-group">
            <label for="update-email">Email Address *</label>
            <input 
              type="email" 
              id="update-email" 
              v-model="updateData.email" 
              required 
              placeholder="john@example.com"
            />
          </div>

          <div class="form-group">
            <label for="update-phone">Phone Number</label>
            <input 
              type="tel" 
              id="update-phone" 
              v-model="updateData.phone" 
              placeholder="(123) 456-7890"
            />
          </div>

          <div class="form-group">
            <label for="update-guests">Number of Guests *</label>
            <input 
              type="number" 
              id="update-guests" 
              v-model="updateData.guests" 
              required 
              min="1"
              max="10"
            />
          </div>

          <div class="form-group">
            <label>Will you be attending? *</label>
            <div class="radio-group">
              <label class="radio-label">
                <input type="radio" v-model="updateData.attending" value="yes" required />
                <span>Yes, I'll be there!</span>
              </label>
              <label class="radio-label">
                <input type="radio" v-model="updateData.attending" value="no" />
                <span>Sorry, can't make it</span>
              </label>
            </div>
          </div>

          <div class="form-group">
            <label for="update-dietary">Dietary Restrictions</label>
            <textarea 
              id="update-dietary" 
              v-model="updateData.dietary" 
              rows="3"
              placeholder="Please let us know if you have any dietary restrictions..."
            ></textarea>
          </div>

          <div class="form-group">
            <label for="update-message">Message to the Couple</label>
            <textarea 
              id="update-message" 
              v-model="updateData.message" 
              rows="4"
              placeholder="Share your thoughts and well wishes..."
            ></textarea>
          </div>

          <button type="submit" class="submit-button" :disabled="loading">
            {{ loading ? 'Updating...' : 'Update RSVP' }}
          </button>

          <button type="button" @click="cancelUpdate" class="cancel-button">
            Cancel
          </button>

          <p v-if="error" class="error-message">{{ error }}</p>
        </form>
      </div>

      <div v-if="submitted" class="success-message">
        <h2>Thank You!</h2>
        <p>Your RSVP has been received. We're looking forward to seeing you!</p>
        <button @click="goHome" class="reset-button">Return to Home</button>
      </div>
      
      <div class="update-link" v-if="!submitted">
        <router-link to="/update-rsvp" class="update-rsvp-link">Need to update your RSVP?</router-link>
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
      submitted: false,
      existingRSVP: null,
      showUpdateForm: false,
      updateData: {
        id: null,
        name: '',
        email: '',
        phone: '',
        guests: 1,
        attending: '',
        dietary: '',
        message: ''
      }
    }
  },
  methods: {
    async submitRSVP() {
      this.loading = true
      this.error = ''
      
      try {
        // First check if RSVP already exists
        const checkResponse = await axios.post('/api/rsvp/check', {
          email: this.formData.email,
          phone: this.formData.phone
        })
        
        if (checkResponse.data.exists) {
          this.existingRSVP = checkResponse.data
          this.loading = false
          return
        }
        
        // If no existing RSVP, create new one
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
      this.showUpdateForm = false
      this.error = ''
    },
    showUpdate() {
      this.updateData = {
        id: this.existingRSVP.id,
        name: this.existingRSVP.name,
        email: this.existingRSVP.email,
        phone: this.existingRSVP.phone || '',
        guests: this.existingRSVP.guests,
        attending: this.existingRSVP.attending,
        dietary: this.existingRSVP.dietary || '',
        message: this.existingRSVP.message || ''
      }
      this.showUpdateForm = true
    },
    async updateExistingRSVP() {
      this.loading = true
      this.error = ''
      
      try {
        await axios.put(`/api/rsvp/${this.updateData.id}`, this.updateData)
        this.submitted = true
        this.existingRSVP = null
        this.showUpdateForm = false
      } catch (err) {
        console.error('Error updating RSVP:', err)
        this.error = 'Failed to update RSVP. Please try again.'
      } finally {
        this.loading = false
      }
    },
    cancelUpdate() {
      this.showUpdateForm = false
    },
    goHome() {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.rsvp {
  padding: 4rem 2rem;
  background: #ffffff;
  min-height: calc(100vh - 200px);
}

.container {
  max-width: 700px;
  margin: 0 auto;
}

h1 {
  font-size: 4rem;
  text-align: center;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 3rem;
}

.rsvp-form {
  background: #f5f5f5;
  padding: 3rem;
  border: 1px solid #1a1a1a;
}

.form-group {
  margin-bottom: 2rem;
}

label {
  display: block;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  font-size: 0.85rem;
  letter-spacing: 1px;
}

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="number"],
textarea {
  width: 100%;
  padding: 0.9rem;
  border: 1px solid #1a1a1a;
  font-size: 1rem;
  transition: all 0.3s;
  background: #ffffff;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #1a1a1a;
  background: white;
  box-shadow: 0 0 0 2px rgba(26, 26, 26, 0.1);
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
  padding: 0.5rem 1rem;
  transition: all 0.3s;
}

.radio-label:hover {
  background: #e5e5e5;
}

.radio-label input[type="radio"] {
  width: auto;
  cursor: pointer;
  accent-color: #1a1a1a;
}

.submit-button {
  width: 100%;
  background: #1a1a1a;
  color: #ffffff;
  padding: 1.2rem;
  border: 2px solid #1a1a1a;
  font-size: 1.1rem;
  font-weight: 400;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.submit-button:hover:not(:disabled) {
  background: #ffffff;
  color: #1a1a1a;
  transform: translateY(-2px);
}

.submit-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  color: #dc2626;
  text-align: center;
  margin-top: 1rem;
  font-weight: 600;
  background: #fee2e2;
  padding: 0.75rem;
  border: 1px solid #dc2626;
}

.success-message {
  background: #f5f5f5;
  padding: 3rem;
  text-align: center;
  border: 1px solid #1a1a1a;
}

.success-message h2 {
  color: #1a1a1a;
  font-size: 3rem;
  margin-bottom: 1rem;
  font-family: 'Playfair Display', serif;
  font-weight: 700;
}

.success-message p {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 2rem;
}

.reset-button {
  background: #1a1a1a;
  color: #ffffff;
  padding: 0.75rem 2rem;
  border: 2px solid #1a1a1a;
  font-size: 1rem;
  font-weight: 400;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.reset-button:hover {
  background: #ffffff;
  color: #1a1a1a;
  transform: translateY(-2px);
}

.update-link {
  margin-top: 3rem;
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid #e5e5e5;
}

.update-link p {
  font-size: 1rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.update-rsvp-link {
  display: inline-block;
  color: #1a1a1a;
  text-decoration: underline;
  font-size: 1rem;
  font-weight: 600;
  transition: all 0.3s;
}

.update-rsvp-link:hover {
  color: #666;
}

.existing-rsvp-message {
  background: #f5f5f5;
  padding: 3rem;
  text-align: center;
  border: 1px solid #1a1a1a;
}

.existing-rsvp-message h2 {
  color: #1a1a1a;
  font-size: 3rem;
  margin-bottom: 1.5rem;
  font-family: 'Playfair Display', serif;
  font-weight: 700;
}

.existing-info {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 2rem;
}

.existing-details {
  background: #ffffff;
  padding: 1.5rem;
  border: 1px solid #1a1a1a;
  margin-bottom: 2rem;
  text-align: left;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}

.existing-details p {
  font-size: 1rem;
  color: #1a1a1a;
  margin: 0.5rem 0;
}

.update-prompt {
  font-size: 1.2rem;
  color: #1a1a1a;
  font-weight: 600;
  margin-bottom: 2rem;
}

.update-button {
  display: inline-block;
  background: #1a1a1a;
  color: #ffffff;
  padding: 1rem 2rem;
  text-decoration: none;
  border: 2px solid #1a1a1a;
  font-size: 1rem;
  font-weight: 400;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-right: 1rem;
  cursor: pointer;
}

.update-button:hover {
  background: #ffffff;
  color: #1a1a1a;
  transform: translateY(-2px);
}

.cancel-button {
  display: inline-block;
  background: #ffffff;
  color: #1a1a1a;
  padding: 1rem 2rem;
  border: 2px solid #1a1a1a;
  font-size: 1rem;
  font-weight: 400;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
}

.cancel-button:hover {
  background: #1a1a1a;
  color: #ffffff;
  transform: translateY(-2px);
}

.update-form {
  margin-top: 2rem;
  text-align: left;
}

.update-form .submit-button {
  margin-bottom: 1rem;
}

.update-form .cancel-button {
  width: 100%;
  background: #ffffff;
  color: #1a1a1a;
  padding: 1.2rem;
  border: 2px solid #1a1a1a;
  font-size: 1.1rem;
  font-weight: 400;
  transition: all 0.3s;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  margin-top: 0;
}

.update-form .cancel-button:hover {
  background: #1a1a1a;
  color: #ffffff;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .rsvp-form {
    padding: 2rem 1.5rem;
  }
  
  h1 {
    font-size: 2.5rem;
  }
  
  .radio-group {
    flex-direction: column;
    gap: 1rem;
  }
  
  .existing-rsvp-message h2 {
    font-size: 2rem;
  }
  
  .update-button,
  .cancel-button {
    display: block;
    width: 100%;
    margin: 0.5rem 0;
  }
}
</style>
