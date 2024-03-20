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
    <div class="contain">
      <div id="catering">
          <div class="txt-c">
          <h1>Catering</h1>
          <p>
            Discover the perfect caterer for your 
            event among our array of Catering Solutionists 
            tailored to your every culinary need.
          </p><br>
          <span class="btn-white">
            <router-link to="/services/caterers">
              Find a Caterer
            </router-link>
          </span>
        </div>
        <div class="food"></div>
      </div>
      <div id="mc">
          <div class="txt-c">
          <h1>emcees</h1>
          <p>
            Unearth the ideal Master of Ceremony 
            for your event amidst our lineup of 
            charismatic and skilled hosts, ensuring 
            seamless engagement throughout.
          </p><br>
          <span class="btn-white">
            <router-link to="/services/emcees">
              Find an MC
            </router-link>
          </span>
        </div>
        <div class="ceremony"></div>
      </div>
      <div id="music_band">
          <div class="txt-c">
          <h1>Artists</h1>
          <p>
            Uncover the ultimate musical ensemble for 
            your gathering among our selection of dynamic 
            Music Bands, setting the tone for unforgettable moments.
          </p><br>
          <span class="btn-white">
            <router-link to="/services/artists">
              Find a Band
            </router-link>
          </span>
        </div>
        <div class="music"></div>
      </div>
      <div id="equipment">
          <div class="txt-c">
          <h1>Equipment Hire</h1>
          <p>
            Explore a range of top-tier Equipment Hire options, 
            ensuring your event is equipped with the finest 
            audiovisual gear for a seamless experience.
          </p><br>
          <span class="btn-white">
            <router-link to="/services/equipment">
              Hire Equipment
            </router-link>
          </span>
        </div>
        <div class="equip"></div>
      </div>
    </div><br><br><br>
    <Contact id="contact"/>
  </div>
</template>

<script lang="js">
  import NavBar from './NavBar2.vue';
  import Contact from './Contact.vue';
  import axios from 'axios';

  export default {
    components: {
      NavBar, Contact,
    },
    data() {
      return {
        msg: '',
      }
    },
    methods: {
      getCaterer() {
        const path = 'http://localhost:5000/api/catering';

        axios.get(path)
          .then((res) => {
            // Assuming res.data is already in JSON format, no need to stringify
            const users = res.data.users;
            // Create a new list containing the first 10 users
            const firstTenUsers = users.slice(0, 10);
            let content = JSON.stringify(firstTenUsers);
            let caterer_list = JSON.parse(content);
            // this retrieves the firstname of the user
            this.msg = caterer_list[0].firstName;
          })
          .catch((error) => {
            console.error('Error fetching data:', error);
          });
      },
    },
    created() {
      this.getCaterer();
    },
  };
</script>

<style scoped>
.start {
  background-image: url('../assets/hero-one.jpg');
  height: 100vh;
  width: 100%;
  background-size: cover;
}

.start h1 {
  font-family: "Truculenta", sans-serif;
  font-size: 100px;
  text-align: center;
  padding-top: 140px;
  color: var(--color-link); /* Use semantic color variable for heading */
  text-transform: uppercase;
  text-shadow: 2px 2px 50px #333;
}

.start p {
  font-family: "Open Sans", sans-serif;
  text-align: center;
  text-shadow: 2px 2px 50px #333;
  color: var(--color-link); /* Use semantic color variable for text */
  font-size: 20px;
  margin-top: 100px;
}

.start a {
  color: var(--color-link); /* Use semantic color variable for links */
  text-decoration: none;
  letter-spacing: 1.2px;
}

.start a:hover {
  text-decoration: underline;
}

.contain {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Apply color variables to sections */
#catering,
#mc,
#equipment,
#music_band {
  margin: 120px 50px auto 50px;
  background-color: var(--color-background);
  padding: 65px 95px;
  border-radius: 5px;
  transition: all ease-in-out 0.3s;
}

#catering {
  display: flex;
  background-image: url('../assets/food-two.jpg');
  background-position: right;
  background-size: contain;
  background-repeat: no-repeat;
  transition: all ease 0.5s;
}

#mc {
  display: flex;
  background-image: url('../assets/emcee.webp');
  background-position: right;
  background-size: contain;
  background-repeat: no-repeat;
}

#music_band {
  border-radius: 5px;background-image: url('../assets/hero-two.jpg');
  background-position: right;
  background-size: contain;
  background-repeat: no-repeat;
}

#equipment {
  border-radius: 5px;background-image: url('../assets/drummer.jpg');
  background-position: right;
  background-size: contain;
  background-repeat: no-repeat;
}

.txt-c h1 {
  font-family: "Truculenta", sans-serif;
  font-size: 60px;
  text-transform: uppercase;
  font-weight: 500;
  color: var(--color-heading); /* Use semantic color variable for heading */
}

.txt-c p {
  font-family: "Open Sans", sans-serif;
  font-size: 15px;
  margin: 2px 0;
  padding-bottom: 20px;
  width: 30%;
  line-height: 2;
  text-align: justify;
}

/* Apply color variables to hover effect */
#catering:hover,
#mc:hover,
#equipment:hover,
#music_band:hover {
  box-shadow: 5px 5px 70px 5px var(--vt-c-black-mute);
  transform: scale(1.1);
  transition: transform 0.5s;
}

</style>
