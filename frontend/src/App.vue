<template>
  <div id="app">
    <nav class="navbar">
      <div class="nav-content">
        <h1 class="nav-title">The Kendalls</h1>
        <div class="nav-links">
          <router-link to="/">Home</router-link>
          <router-link to="/rsvp">RSVP</router-link>
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1rem 0;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.nav-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-title {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  margin: 0;
  font-weight: 700;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-family: 'Lato', sans-serif;
  font-size: 1.1rem;
  transition: opacity 0.3s;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  opacity: 0.8;
  text-decoration: underline;
}

main {
  min-height: calc(100vh - 200px);
}

footer {
  background: #2d3748;
  color: white;
  text-align: center;
  padding: 2rem;
  margin-top: 4rem;
  font-family: 'Lato', sans-serif;
}
</style>
