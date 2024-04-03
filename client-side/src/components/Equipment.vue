<template>
    <div>
        <NavBar />
        <section class="listed">
            <div class="card" v-for="(lessor, idx) in equipment_list" :key="idx">
                <img :src="lessor.image" :alt="lessor.category">
                <div class="txt">
                    <h2>{{ lessor.title }}</h2>
                    <h3>Product Rating: {{ lessor.rating.rate }}</h3>
                    <p>{{ lessor.description }}</p>
                    <span>
                        <h4>${{ lessor.price }}</h4>
                        <a href="#">Hire</a>
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
            equipment_list: {},
        }
    },
    methods: {
        getEquipment() {
            const path = "http://localhost:5000/api/equipment";
            axios.get(path)
            .then((res) => {
                const equipment = res.data.products;
                const startIndex = 5;
                const endIndex = 21;

                const  firstTenEquipment = equipment.slice(startIndex, endIndex);
                this.equipment_list = firstTenEquipment;
            })
            .catch ((error) => {
                console.error("Error fetching data", error);
            });

        },
    },
    created() {
        this.getEquipment();
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

.txt span {
    display: flex;
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

.txt h4 {
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