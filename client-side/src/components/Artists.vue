<template>
    <div>
        <NavBar />
        <h2>Get your favourite artist</h2>
            <section class="listed">
                <div class="card" v-for="(artist, index) in artists_list" :key="index">
                    <img :src="artist.image" :alt="artist.firstName" />
                    <div class="txt">
                        <h2>{{  artist.firstName }} {{ artist.lastName }}</h2>
                        <h5>aka {{ artist.maidenName }}</h5>
                        <h3>{{ artist.phone }} &nbsp;|&nbsp; {{ artist.email }}</h3>
                        <p>You can contact  {{ artist.firstName }}, to request their service via email, or give them a Call/WhatsApp</p>
                        <span>
                            <a :href="'mailto:' + artist.email">Send Email</a>
                            <a :href="'tel:' + artist.phone">Call {{ artist.firstName }}</a>
                        </span>
                    </div>
                </div>
            </section>
        <Contact />
    </div>
</template>

<script>
import NavBar from './NavBar2.vue'
import Contact from './Contact.vue'
import axios from 'axios';

export default {
    components: {
        NavBar, Contact
    },
    data() {
        return {
            artists_list: {},
        }
    },
    methods: {
        getArtists() {
            const path = "http://localhost:5000/api/music_band";
            axios.get(path)
            .then((res) => {
                const users = res.data.users;
                const startIndex = 5;
                const endIndex = 21;

                const  firstTenUsers = users.slice(startIndex, endIndex).reverse();
                this.artists_list = firstTenUsers;
            })
            .catch ((error) => {
                console.error("Error fetching data", error);
            });

        },
    },
    created() {
        this.getArtists();
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

h2 {
    font-family: 'Truculenta', sans-serif;
    font-size: 45px;
    text-align: center;
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
.txt h5 {
    font-style: italic;
    font-weight: bold;
}

</style>
