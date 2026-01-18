<template>
  <div class="admin">
    <div class="container">
      <h1>RSVP Management</h1>
      
      <div class="stats-grid" v-if="stats">
        <div class="stat-card attending">
          <h3>Attending</h3>
          <p class="stat-number">{{ stats.attending }}</p>
          <p class="stat-label">{{ stats.total_guests }} Total Guests</p>
        </div>
        <div class="stat-card not-attending">
          <h3>Not Attending</h3>
          <p class="stat-number">{{ stats.not_attending }}</p>
        </div>
        <div class="stat-card total">
          <h3>Total RSVPs</h3>
          <p class="stat-number">{{ stats.total_rsvps }}</p>
        </div>
      </div>

      <div class="rsvp-list">
        <h2>Guest List</h2>
        <div v-if="loading" class="loading">Loading RSVPs...</div>
        <div v-else-if="error" class="error">{{ error }}</div>
        <div v-else-if="rsvps.length === 0" class="empty">No RSVPs yet.</div>
        
        <div v-else class="table-container">
          <table class="rsvp-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Guests</th>
                <th>Attending</th>
                <th>Dietary</th>
                <th>Message</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="rsvp in rsvps" :key="rsvp.id" :class="{ 'attending-row': rsvp.attending === 'yes', 'not-attending-row': rsvp.attending === 'no' }">
                <td class="name-cell">{{ rsvp.name }}</td>
                <td>{{ rsvp.email }}</td>
                <td>{{ rsvp.phone || 'N/A' }}</td>
                <td class="centered">{{ rsvp.guests }}</td>
                <td class="centered">
                  <span :class="['status-badge', rsvp.attending === 'yes' ? 'yes-badge' : 'no-badge']">
                    {{ rsvp.attending === 'yes' ? 'Yes' : 'No' }}
                  </span>
                </td>
                <td>{{ rsvp.dietary || 'None' }}</td>
                <td class="message-cell">{{ rsvp.message || '-' }}</td>
                <td class="date-cell">{{ formatDate(rsvp.created_at) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Admin',
  data() {
    return {
      rsvps: [],
      stats: null,
      loading: true,
      error: ''
    }
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      this.loading = true
      this.error = ''
      
      try {
        const [rsvpsResponse, statsResponse] = await Promise.all([
          axios.get('/api/rsvp'),
          axios.get('/api/stats')
        ])
        
        this.rsvps = rsvpsResponse.data
        this.stats = statsResponse.data
      } catch (err) {
        console.error('Error fetching data:', err)
        this.error = 'Failed to load RSVP data. Please try again.'
      } finally {
        this.loading = false
      }
    },
    formatDate(dateString) {
      const date = new Date(dateString)
      return date.toLocaleDateString('en-US', { 
        month: 'short', 
        day: 'numeric', 
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  }
}
</script>

<style scoped>
.admin {
  padding: 3rem 2rem;
  background: #ffffff;
  min-height: calc(100vh - 200px);
}

.container {
  max-width: 1400px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  font-size: 4rem;
  margin-bottom: 3rem;
  color: #1a1a1a;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: #f5f5f5;
  padding: 2rem;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  text-align: center;
  border: 1px solid #1a1a1a;
  transition: all 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}

.stat-card h3 {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 400;
  font-family: 'Lato', sans-serif;
}

.stat-number {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #1a1a1a;
  font-family: 'Playfair Display', serif;
}

.stat-label {
  font-size: 1rem;
  color: #999;
}

.rsvp-list {
  background: #f5f5f5;
  padding: 2rem;
  border: 1px solid #1a1a1a;
}

.rsvp-list h2 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #1a1a1a;
  font-family: 'Playfair Display', serif;
  font-weight: 700;
}

.loading, .error, .empty {
  text-align: center;
  padding: 3rem;
  font-size: 1.2rem;
  color: #999;
}

.error {
  color: #dc2626;
  background: #fee2e2;
  border: 1px solid #dc2626;
}

.table-container {
  overflow-x: auto;
}

.rsvp-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}

.rsvp-table thead {
  background: #1a1a1a;
  border-bottom: 2px solid #1a1a1a;
}

.rsvp-table th {
  padding: 1rem;
  text-align: left;
  font-weight: 600;
  color: #ffffff;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.85rem;
}

.rsvp-table td {
  padding: 1rem;
  border-bottom: 1px solid #e5e5e5;
}

.rsvp-table tbody tr {
  transition: all 0.2s;
  background: #ffffff;
}

.rsvp-table tbody tr:hover {
  background-color: #f5f5f5;
}

.attending-row {
  border-left: 3px solid #1a1a1a;
}

.not-attending-row {
  border-left: 3px solid #999;
}

.name-cell {
  font-weight: 600;
  color: #1a1a1a;
}

.centered {
  text-align: center;
}

.status-badge {
  display: inline-block;
  padding: 0.4rem 1rem;
  font-weight: 600;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.yes-badge {
  background: #1a1a1a;
  color: #ffffff;
  border: 1px solid #1a1a1a;
}

.no-badge {
  background: #ffffff;
  color: #1a1a1a;
  border: 1px solid #1a1a1a;
}

.message-cell {
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.date-cell {
  font-size: 0.85rem;
  color: #999;
  white-space: nowrap;
}

@media (max-width: 768px) {
  .admin {
    padding: 2rem 1rem;
  }
  
  h1 {
    font-size: 2.5rem;
  }
  
  .table-container {
    font-size: 0.85rem;
  }
  
  .rsvp-table th,
  .rsvp-table td {
    padding: 0.5rem;
  }
}
</style>
