<template>
  <div id="app">
    <nav class="navbar">
      <div class="nav-content">
        <h1 class="nav-title">The Kendalls</h1>
        <div class="nav-links">
          <router-link to="/">Home</router-link>
          <router-link to="/our-story">Our Story</router-link>
          <router-link to="/schedule">Schedule</router-link>
          <router-link to="/registry">Registry</router-link>
          <router-link to="/qa">Q&A</router-link>
          <router-link to="/rsvp">RSVP</router-link>
          <router-link to="/admin">Admin</router-link>
        </div>
      </div>
    </nav>
    <main>
      <router-view></router-view>
    </main>
    <footer>
      <p>&copy; 2026 The Kendalls</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
.navbar {
  background: #1a1a1a;
  color: #ffffff;
  padding: 1.5rem 0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
}

.navbar::before {
  content: '';
  display: none;
}

.navbar::after {
  content: '';
  display: none;
}

.nav-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 1;
}

.nav-title {
  font-family: 'Great Vibes', cursive;
  font-size: 2.5rem;
  margin: 0;
  font-weight: 400;
  color: #ffffff;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-family: 'Lato', sans-serif;
  font-size: 1rem;
  transition: all 0.3s;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.nav-links a:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
}

.nav-links a.router-link-active {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
}

main {
  min-height: calc(100vh - 200px);
}

footer {
  background: #1a1a1a;
  color: #ffffff;
  text-align: center;
  padding: 2rem;
  margin-top: 4rem;
  font-family: 'Lato', sans-serif;
  position: relative;
  border-top: 1px solid #333;
}

footer::before {
  content: '';
  display: none;
}

footer p {
  font-weight: 500;
}

@media (max-width: 768px) {
  .nav-title {
    font-size: 1.5rem;
  }
  
  .nav-links {
    gap: 1rem;
  }
  
  .nav-links a {
    font-size: 0.9rem;
    padding: 0.4rem 0.8rem;
  }
  
  .navbar::before,
  .navbar::after {
    display: none;
  }
}
</style>
