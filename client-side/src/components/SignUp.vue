<template>
    <div class="backd">
        <router-link to="/">
            <img id="logo_" src="../assets/icon-white.png" alt="">
        </router-link>
        <img id="blurr" src="../assets/open_two.jpg" alt="">
        <div class="over">
            <h1>Join Our List</h1>
            <h2>of excellent talents</h2>
            <span>
                <input type="text" name="firstName" placeholder="First Name" id="fn">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <input type="text" name="lastName" placeholder="Last Name" id="ln">
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <input type="email" name="" placeholder="E-mail" id="email">
                <input type="number" name="phone" placeholder="Phone" id="phone">
            </span>
            <button type="submit">sign up</button>
        </div>
    <span class="ftr">© 2024 <router-link to="/">Event Ease</router-link> | All Rights Reserved | <router-link to="/register">List Your Service</router-link></span>
    </div>
</template>

<script setup>

</script>

<style scoped>
.backd {
    width: 100%;
    height: 100vh;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

#logo_ {
    width: 200px;
    top: -250px;
    left: 170px;
    z-index: 2;
}

#blurr {
    filter: blur(10px);
    width: 100%;
    height: 100vh;
    position: absolute;
    top: 0;
    left: 0;
}

.over {
    background-color: #22222282;
    width: 55%;
    height: 55%;
    z-index: 1;
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* Additional styles for text inside .over to ensure it's centered */
.over {
    color: white;
    h1 {
        font-family: "Truculenta", sans-serif;
        font-size: 55px;
    }
    h2 {
        font-family: 'Open sans', sans-serif;
        font-size: medium;
        margin-top: -20px;
    }
}

.over span {
    margin: 35px 85px;
}

.over span input {
    padding: 20px 20px;
    margin: 10px 10px 20px 10px;
    border-radius: 8px;
    width: 290px;
    height: 45px;
    border: none;
    display: inline-flexex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
}

.over button {
    padding: 10px 25px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 14px;
    border: none;
    transition: all ease 0.3s;
}

.over button:hover {
    background-color: #67262682;
    color: white;
    transition: all ease 0.3s;
}
.ftr {
    left: -100px;
    margin-top: 700px;
    color: #444;
    font-size: 12px;
    a {
        text-decoration: none;
        color: #444;
    }
}

.ftr a:hover {
    text-decoration: underline;
    color: #555;
}
</style>
