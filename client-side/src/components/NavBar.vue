<template>
  <div>
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
            <a href="#contact" to="/contact">Contact</a href="#contact">
          </li>
          <button>
            <router-link to="/register">Login / SignUp</router-link>
          </button>
        </ul>
      </div>
    </nav>
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
</style>