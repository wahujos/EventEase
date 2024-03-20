<template>
  <div>
    <section class="open">
    <NavBar />
      <div class="heroMsg">
        <h1>Where happening people meet</h1>
        <p>Your Premier Hub for Music Bands, MCs, Artists, and Equipment Hire!</p>
        <br><br><p>&darr;</p>
      </div>
      <br><br><br>
    </section>
    <section id="about" class="about-us">
      <div class="ab-txt">
        <h2>What we do</h2>
        <p>We are your go-to platform for
          streamlining event management, tailored
          specifically for small and mid-sized organizations.
          Our mission is to simplify the event planning process
          by connecting you directly with the resources you need,
          from entertainers to event planners, effortlessly saving
          you time and hassle.</p><br><br>
          <router-link to="/services">Book a Service</router-link>
      </div>
      <div class="ab-img"></div>
    </section>
    <OurTeam />
    <Contact id="contact"/>
  </div>
</template>

<script setup>
import NavBar from './NavBar.vue'
import Contact from './Contact.vue';
import OurTeam from './OurTeam.vue';
</script>

<style scoped>
.open {
  position: relative;
  background-image: url('../assets/open.png');
  width: 100%;
  height: auto;
  background-size: cover;
  background-position: bottom;
}

.overlay {
  background-color: #000000b9;
}


</style>
