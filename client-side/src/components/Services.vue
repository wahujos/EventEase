<template>
  <div>
    <section class="start">
      <NavBar />
      <h1>
        Hire Right, for the Job!
      </h1>
      <p>
        <a href="#catering">Catering</a> /
        <a href="#equipment">Equipment Hire</a> /
        <a href="#mc">Master of Ceremonies</a> /
        <a href="#music_band">Music Band</a>
      </p>
    </section>
    <div class="catering">
      <h1>Catering</h1>
    </div>
  </div>
</template>

<script setup>
import NavBar from './NavBar.vue'
</script>

<style scoped>
.start {
  background-image: url('../assets/hero-one.jpg');
  height: 95vh;
  width: 100%;
  background-size: cover;
}

.start h1 {
  font-family: "Truculenta", sans-serif;
  font-size: 100px;
  text-align: center;
  padding-top: 150px;
  color: white;
  text-transform: uppercase;
  text-shadow: 2px 2px 50px #333;
}

.start p {
  font-family: "Open Sans", sans-serif;
  text-align: center;
  text-shadow: 2px 2px 50px #333;
  color: white;
  font-size: 20px;
  margin-top: 170px;
}

.start a {
  color: white;
  text-decoration: none;
  letter-spacing: 1.2px;
}

.start a:hover {
  text-decoration: underline;
}

.catering {
  margin: 120px 0 auto 120px;
}

.catering h1 {
  font-family: "Truculenta", sans-serif;
  font-size: 50px;
  text-transform: uppercase;
}
</style>