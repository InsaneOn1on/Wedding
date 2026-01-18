<template>
  <div class="update-rsvp">
    <div class="container">
      <h1>RSVP</h1>
      <p class="subtitle">Update your wedding RSVP information</p>
      
      <!-- Edit Form -->
      <div v-if="foundRSVP && !updated" class="existing-rsvp-message">
        <h2>Update Your RSVP</h2>
        <p class="existing-info">Update your information below:</p>
        
        <form @submit.prevent="updateRSVP" class="update-form">
          <div class="form-group">
            <label for="edit-name">Full Name *</label>
            <input 
              type="text" 
              id="edit-name" 
              v-model="formData.name" 
              required 
              placeholder="John Doe"
            />
          </div>

          <div class="form-group">
            <label for="edit-email">Email Address *</label>
            <input 
              type="email" 
              id="edit-email" 
              v-model="formData.email" 
              required 
              placeholder="john@example.com"
            />
          </div>

          <div class="form-group">
            <label for="edit-phone">Phone Number</label>
            <input 
              type="tel" 
              id="edit-phone" 
              v-model="formData.phone" 
              placeholder="(123) 456-7890"
            />
          </div>

          <div class="form-group">
            <label for="edit-guests">Number of Guests *</label>
            <input 
              type="number" 
              id="edit-guests" 
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
            <label for="edit-dietary">Dietary Restrictions</label>
            <textarea 
              id="edit-dietary" 
              v-model="formData.dietary" 
              rows="3"
              placeholder="Please let us know if you have any dietary restrictions..."
            ></textarea>
          </div>

          <div class="form-group">
            <label for="edit-message">Message to the Couple</label>
            <textarea 
              id="edit-message" 
              v-model="formData.message" 
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

      <!-- Lookup Form -->
      <form @submit.prevent="findRSVP" class="lookup-form" v-if="!foundRSVP && !updated">
        <p class="instructions">Enter your email, full name, or phone number to find your RSVP:</p>
        
        <div class="form-group">
          <label for="email">Email Address</label>
          <input 
            type="email" 
            id="email" 
            v-model="lookupData.email" 
            placeholder="john@example.com"
          />
        </div>

        <div class="form-group">
          <label for="name">Full Name</label>
          <input 
            type="text" 
            id="name" 
            v-model="lookupData.name" 
            placeholder="John Doe"
          />
        </div>

        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input 
            type="tel" 
            id="phone" 
            v-model="lookupData.phone" 
            placeholder="(123) 456-7890"
          />
        </div>

        <button type="submit" class="submit-button" :disabled="loading || !hasLookupData">
          {{ loading ? 'Searching...' : 'Find My RSVP' }}
        </button>

        <p v-if="error" class="error-message">{{ error }}</p>
      </form>

      <!-- Success Message -->
      <div v-if="updated" class="success-message">
        <h2>RSVP Updated!</h2>
        <p>Your RSVP has been successfully updated. Thank you!</p>
        <button @click="goHome" class="reset-button">Return to Home</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UpdateRSVP',
  data() {
    return {
      lookupData: {
        email: '',
        name: '',
        phone: ''
      },
      formData: {
        id: null,
        name: '',
        email: '',
        phone: '',
        guests: 1,
        attending: '',
        dietary: '',
        message: ''
      },
      foundRSVP: false,
      loading: false,
      error: '',
      updated: false
    }
  },
  mounted() {
    // Check if RSVP data was passed from the duplicate check
    if (history.state && history.state.rsvpData) {
      const rsvpData = history.state.rsvpData
      // Populate form with passed data
      this.formData = {
        id: rsvpData.id,
        name: rsvpData.name,
        email: rsvpData.email,
        phone: rsvpData.phone || '',
        guests: rsvpData.guests,
        attending: rsvpData.attending,
        dietary: rsvpData.dietary || '',
        message: rsvpData.message || ''
      }
      this.foundRSVP = true
    }
  },
  computed: {
    hasLookupData() {
      return this.lookupData.email || this.lookupData.name || this.lookupData.phone
    }
  },
  methods: {
    async findRSVP() {
      this.loading = true
      this.error = ''
      
      try {
        const params = {}
        if (this.lookupData.email) params.email = this.lookupData.email
        if (this.lookupData.name) params.name = this.lookupData.name
        if (this.lookupData.phone) params.phone = this.lookupData.phone
        
        const response = await axios.get('/api/rsvp/find', { params })
        
        // Populate form with found data
        this.formData = {
          id: response.data.id,
          name: response.data.name,
          email: response.data.email,
          phone: response.data.phone || '',
          guests: response.data.guests,
          attending: response.data.attending,
          dietary: response.data.dietary || '',
          message: response.data.message || ''
        }
        
        this.foundRSVP = true
      } catch (err) {
        console.error('Error finding RSVP:', err)
        this.error = err.response?.data?.error || 'RSVP not found. Please check your information and try again.'
      } finally {
        this.loading = false
      }
    },
    async updateRSVP() {
      this.loading = true
      this.error = ''
      
      try {
        await axios.put(`/api/rsvp/${this.formData.id}`, this.formData)
        this.updated = true
      } catch (err) {
        console.error('Error updating RSVP:', err)
        this.error = 'Failed to update RSVP. Please try again.'
      } finally {
        this.loading = false
      }
    },
    cancelUpdate() {
      this.$router.push('/')
    },
    goHome() {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.update-rsvp {
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

.instructions {
  text-align: center;
  font-size: 1.1rem;
  color: #333;
  margin-bottom: 2rem;
}

.lookup-form {
  background: #f5f5f5;
  padding: 3rem;
  border: 1px solid #1a1a1a;
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

.update-form {
  margin-top: 2rem;
  text-align: left;
}

.update-form .submit-button {
  margin-bottom: 1rem;
}

.update-form .cancel-button {
  width: 100%;
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
  cursor: pointer;
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

.cancel-button {
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
  margin-top: 1rem;
}

.cancel-button:hover {
  background: #1a1a1a;
  color: #ffffff;
  transform: translateY(-2px);
}

.error-message {
  color: #d32f2f;
  text-align: center;
  margin-top: 1rem;
  font-weight: 500;
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
  cursor: pointer;
}

.reset-button:hover {
  background: #ffffff;
  color: #1a1a1a;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .update-rsvp {
    padding: 2rem 1rem;
  }

  h1 {
    font-size: 2.5rem;
  }

  .lookup-form,
  .rsvp-form {
    padding: 2rem 1.5rem;
  }

  .success-message h2 {
    font-size: 2rem;
  }

  .radio-group {
    flex-direction: column;
    gap: 1rem;
  }
}

</style>
