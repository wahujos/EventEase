<template>
    <div>
        <NavBar />
        <h2>Master of Ceremonies</h2>
            <section class="listed">
                <div class="card" v-for="(emcees, index) in emcees_list" :key="index">
                    <img :src="emcees.image" :alt="emcees.firstName" />
                    <div class="txt">
                        <h2>{{  emcees.firstName }} {{ emcees.lastName }}</h2>
                        <h5>aka {{ emcees.maidenName }}</h5>
                        <h3>{{ emcees.phone }} &nbsp;|&nbsp; {{ emcees.email }}</h3>
                        <p>You can contact  {{ emcees.firstName }}, to request their service via email, or give them a Call/WhatsApp</p>
                        <span>
                            <a :href="'mailto:' + emcees.email">Send Email</a>
                            <a :href="'tel:' + emcees.phone">Call {{ emcees.firstName }}</a>
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
            emcees_list: {},
        }
    },
    methods: {
        getEmcees() {
            const path = "http://localhost:5000/api/mc";
            axios.get(path)
            .then((res) => {
                const users = res.data.users;
                const startIndex = 5;
                const endIndex = 21;

                const  firstTenUsers = users.slice(startIndex, endIndex);
                this.emcees_list = firstTenUsers;
            })
            .catch ((error) => {
                console.error("Error fetching data", error);
            });

        },
    },
    created() {
        this.getEmcees();
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