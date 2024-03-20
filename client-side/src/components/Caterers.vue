<template>
  <div>
    <NavBar />
    <section class="listed">
      <div class="card" v-for="(caterer, idx) in caterer_list" :key="idx">
        <img :src="caterer.image" :alt="caterer.firstName">
        <div class="txt">
          <h2>{{ caterer.firstName }} {{ caterer.lastName }}</h2>
          <h3>{{ caterer.phone }} &nbsp;|&nbsp; {{ caterer.email }}</h3>
          <p>You can contact  {{ caterer.firstName }}, to request their service via email, or give them a Call/WhatsApp</p>
          <span>
            <a :href="'mailto:' + caterer.email">Send Email</a>
            <a :href="'tel:' + caterer.phone">Call {{ caterer.firstName }}</a>
          </span>
        </div>
      </div>
    </section>
    <Contact />
  </div>
</template>

<script>
import NavBar from './NavBar2.vue';
import Contact from './Contact.vue';
import axios from 'axios';

export default {
  components: {
    NavBar, Contact,
  },
  data() {
    return {
      caterer_list: {},
    }
  },
  methods: {
    getCaterers() {
      const path = 'http://localhost:5000/api/catering';
      axios.get(path)
        .then((res) => {
          // Assuming res.data is already in JSON format, no need to stringify
          const users = res.data.users;
          // Create a new list containing the first 10 users
          const firstTenUsers = users.slice(5, 21);
          let content = JSON.stringify(firstTenUsers);
          this.caterer_list = JSON.parse(content);
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });
    },
  },
  created() {
    this.getCaterers();
  },
};
</script>

<style scoped>
.listed {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}

.card {
  display: flex;
  align-items: center;
  margin: auto auto 45px auto;
  background-color: var(--color-card);
  transition: all ease-in-out 0.2s;
}

.card:hover {
  box-shadow: 10px 10px 30px 10px #0a0a0a79;
  transform: scale(1.01);
}

.card img {
  margin: 50px;
  width: 250px;
}

.txt {
  width: 250px;
  margin: 50px;
}

.txt h2 {
  font-family: 'Truculenta', sans-serif;
  font-size: 45px;
}

.txt h3 {
  font-family: "Open sans", sans-serif;
  font-size: 12px;
  padding-bottom: 25px;
}

.txt p {
  font-family: "Esteban", serif;
  font-size: 15px;
  font-style: italic;
  padding-bottom: 25px;
}

.txt a {
  margin-right: 10px;
  font-family: 'Open sans', sans-serif;
  text-transform: uppercase;
  background-color: var(--color-btn);
  text-decoration: none;
  color: var(--color-text);
  padding: 10px 20px;
  font-size: 10px;
}

.txt a:hover {
  background-color: var(--color-btn-hover);
  transition: all ease 0.3s;
}
</style>