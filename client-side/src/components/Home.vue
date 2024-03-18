<template>
  <div>
    <section class="open">
    <nav class="navbar">
      <div class="container">
        <div class="logo">
          <router-link to="/">
            <img id="logo" src="../assets/icon-white.png" alt="logo">
          </router-link>
        </div>
        <ul>
          <li>
            <a href="#about">About</a>
          </li>
          <li>
            <router-link to="/services">Service</router-link>
          </li>
          <li>
            <router-link to="/contact">Contact</router-link>
          </li>
          <button>
            <router-link to="/book">Book a Service</router-link>
          </button>
        </ul>
      </div>
    </nav>
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
    <br><br><br><br><br><br><br><br>
  </div>
</template>

<script>

</script>

<style scoped>
.navbar {
  padding: 10px 0;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar ul {
  list-style-type: none;
  margin: 0;
  padding: 0 50px;
  display: flex;
}

.navbar ul li {
  margin: 0 25px;
  padding: 0;
  font-size: 15px;
  align-self: center;
}

.navbar ul button {
  width: 180px;
  height: 40px;
  font-size: 15px;
  padding: 10px 10px;
  align-self: center;
  background-color: #333;
  border: none;
  transition: all ease 0.3s;
  border-radius: 4px;
}

.navbar ul button:hover {
  background-color: #fff;
  color: #333;
}

.navbar ul button a {
  color: #fff;
  text-transform: uppercase;
  text-decoration: none;
  transition: all ease 0.3s;
}

.navbar ul button a:hover {
  color: #333;
  text-decoration: none;
}

.navbar ul li a {
  color: #fff;
  text-decoration: none;
  font-size: 15px;
  text-transform: uppercase;
  transition: all ease 0.3s;
}

.navbar ul li a:hover {
  letter-spacing: 2px;
  color: rgb(62, 64, 64);
  background-color: #fff;
  padding: 10px 15px;
  font-size: 15px;
}

.logo {
  padding: 10px 50px;
  img {
    width: 100px;
    text-shadow: 2px 2px 4px #000000;
  }
}

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