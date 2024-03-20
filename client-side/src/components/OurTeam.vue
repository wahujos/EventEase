<template>
    <div class="container">

    <h1>
        Meet Our Team
    </h1>

      <div class="card-slider" ref="slider">
        <!-- Cards go here -->
        <span class="c1">
            <div class="card1"></div>
            <h3>Jessie Klaine</h3>
            <h5>Creative Liason</h5>
        </span>
        <span class="c2">
            <div class="card2"></div>
            <h3>Felicity Noormie</h3>
            <h5>Digital Marketer</h5>
        </span>
        <span class="c3">
            <div class="card3"></div>
            <h3>Josphine W.</h3>
            <h5>Software Developer</h5>
        </span>
        <span class="c4">
            <div class="card4"></div>
            <h3>Kwame C. Abbey</h3>
            <h5>Software Engineer</h5>
        </span>
        <span class="c6">
            <div class="card6"></div>
            <h3>John-Livingprooff</h3>
            <h5>Digital Creative</h5>
        </span>
        <span class="c5">
            <div class="card5"></div>
            <h3>Jeffery the Parrot</h3>
            <h5>Office Pet</h5>
        </span>
        
        <span class="c1">
            <div class="card1"></div>
            <h3>Jessie Klaine</h3>
            <h5>Creative Liason</h5>
        </span>
        <span class="c2">
            <div class="card2"></div>
            <h3>Felicity Noormie</h3>
            <h5>Digital Marketer</h5>
        </span>
        <span class="c3">
            <div class="card3"></div>
            <h3>Josphine W.</h3>
            <h5>Software Developer</h5>
        </span>
        <span class="c4">
            <div class="card4"></div>
            <h3>Kwame C. Abbey</h3>
            <h5>Software Engineer</h5>
        </span>
        <span class="c5">
            <div class="card5"></div>
            <h3>Jeffery the Parrot</h3>
            <h5>Office Pet</h5>
        </span>
        <span class="c6">
            <div class="card6"></div>
            <h3>John-Livingprooff</h3>
            <h5>Digital Creative</h5>
        </span>
        <span class="c2">
            <div class="card2"></div>
            <h3>Felicity Noormie</h3>
            <h5>Digital Marketer</h5>
        </span>
        <span class="c3">
            <div class="card3"></div>
            <h3>Josphine W.</h3>
            <h5>Software Developer</h5>
        </span>
        <span class="c4">
            <div class="card4"></div>
            <h3>Kwame C. Abbey</h3>
            <h5>Software Engineer</h5>
        </span>
        <span class="c1">
            <div class="card1"></div>
            <h3>Jessie Klaine</h3>
            <h5>Creative Liason</h5>
        </span>
        <span class="c5">
            <div class="card5"></div>
            <h3>Jeffery the Parrot</h3>
            <h5>Office Pet</h5>
        </span>
        <span class="c6">
            <div class="card6"></div>
            <h3>John-Livingprooff</h3>
            <h5>Digital Creative</h5>
        </span>
        <!-- End of cards -->
      </div>
      <div class="controls">
        <span @click="prevCard"> &twoheadleftarrow; </span>
        <span @click="nextCard"> &twoheadrightarrow; </span>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const slider = ref(null); // Reference to the slider element
let autoSlideInterval; // Interval ID for auto-slideshow

// Function to move to the next card
const nextCard = () => {
if (slider.value) {
    slider.value.scrollBy({ left: slider.value.offsetWidth, behavior: 'smooth' });
}
};

// Function to move to the previous card
const prevCard = () => {
if (slider.value) {
    slider.value.scrollBy({ left: -slider.value.offsetWidth, behavior: 'smooth' });
}
};

// Function to start auto-slideshow
const startAutoSlide = () => {
autoSlideInterval = setInterval(nextCard, 60000); // Change slide every 60 seconds
};

// Function to stop auto-slideshow
const stopAutoSlide = () => {
clearInterval(autoSlideInterval);
};

// Hook to start auto-slideshow when component is mounted
onMounted(() => {
startAutoSlide();
});

// Hook to stop auto-slideshow when component is unmounted
onUnmounted(() => {
stopAutoSlide();
});
</script>

<style scoped>
.container {
margin: 50px auto 20px auto;
}

.container h1 {
    font-family: 'Truculenta', sans-serif;
    text-transform: uppercase;
    text-align: center;
    padding-bottom: 40px;
    font-size: 45px;
    letter-spacing: 1.5px;
}

.card-slider {
    display: flex;
    overflow-x: hidden; /* Hide scrollbar */
    scroll-behavior: smooth; /* Smooth scrolling behavior */
    width: 100%;
    height: 200px; /* Adjust height as needed */
}

.c1 {
    h3, h5 {
        display: none;
    }
    transition: all ease 0.5s;
}

.c1:hover {
    h3 {
        display: block;
        color: #fff;
        font-size: 30px;
        font-family: 'Truculenta', sans-serif;
        font-weight: 750;
        text-align: center;
        margin: -125px 0 0 -50px;
    }
    h5 {
        display: block;
        color: #fff;
        font-size: 20px;
        text-align: center;
        margin: -10px 0 0 -50px;
        font-family: 'Times New Roman', Times, serif;
        font-style: italic;
    }
    transition: all ease 0.5s;
}

.card1 {
    flex: 0 0 auto; /* Prevent cards from stretching */
    width: 200px; /* Adjust card width as needed */
    height: 100%; /* Make cards the same height as the slider */
    background-color: #222;
    margin-right: 50px; /* Add spacing between cards */
    padding: 20px;
    transition: all ease 0.5s;
    box-sizing: border-box;
    border-radius: 500px;
    background-image: url('../assets/girl-face.jpg');
    background-size: cover;
}

.c2 {
    h3, h5, hr {
        display: none;
    }
    transition: all ease 0.5s;
}

.c2:hover {
    h3 {
        display: block;
        font-family: 'Truculenta', sans-serif;
        font-weight: 750;
        color: #fff;
        font-size: 30px;
        text-align: center;
        margin: -125px 0 0 -50px;
    }
    h5 {
        display: block;
        color: #fff;
        font-size: 20px;
        text-align: center;
        margin: -10px 0 0 -50px;
        font-family: 'Times New Roman', Times, serif;
        font-style: italic;
    }
    
    transition: all ease 0.5s;
}

.card2 {
    flex: 0 0 auto; /* Prevent cards from stretching */
    width: 200px; /* Adjust card width as needed */
    height: 100%; /* Make cards the same height as the slider */
    background-color: #222;
    margin-right: 50px; /* Add spacing between cards */
    padding: 20px;
    transition: all ease 0.5s;
    box-sizing: border-box;
    border-radius: 500px;
    background-image: url('../assets/girl-two.jpeg');
    background-size: cover;
}

.c3 {
    h3, h5, hr {
        display: none;
    }
    transition: all ease 0.5s;
}

.c3:hover {
    h3 {
        display: block;
        font-family: 'Truculenta', sans-serif;
        font-weight: 750;
        color: #fff;
        font-size: 30px;
        text-align: center;
        margin: -125px 0 0 -50px;
    }
    h5 {
        display: block;
        color: #fff;
        font-size: 20px;
        text-align: center;
        margin: -10px 0 0 -50px;
        font-family: 'Times New Roman', Times, serif;
        font-style: italic;
    }
    
    transition: all ease 0.5s;
}

.card3 {
    flex: 0 0 auto; /* Prevent cards from stretching */
    width: 200px; /* Adjust card width as needed */
    height: 100%; /* Make cards the same height as the slider */
    background-color: #222;
    margin-right: 50px; /* Add spacing between cards */
    padding: 20px;
    transition: all ease 0.5s;
    box-sizing: border-box;
    border-radius: 500px;
    background-image: url('../assets/wahu.jpg');
    background-size: cover;
}

.c4 {
    h3, h5, hr {
        display: none;
    }
    transition: all ease 0.5s;
}

.c4:hover {
    h3 {
        display: block;
        font-family: 'Truculenta', sans-serif;
        font-weight: 750;
        color: #fff;
        font-size: 30px;
        text-align: center;
        margin: -125px 0 0 -50px;
    }
    h5 {
        display: block;
        color: #fff;
        font-size: 20px;
        text-align: center;
        margin: -10px 0 0 -50px;
        font-family: 'Times New Roman', Times, serif;
        font-style: italic;
    }
    
    transition: all ease 0.5s;
}

.card4 {
    flex: 0 0 auto; /* Prevent cards from stretching */
    width: 200px; /* Adjust card width as needed */
    height: 100%; /* Make cards the same height as the slider */
    background-color: #222;
    margin-right: 50px; /* Add spacing between cards */
    padding: 20px;
    transition: all ease 0.5s;
    box-sizing: border-box;
    border-radius: 500px;
    background-image: url('../assets/kwame.png');
    background-size: cover;
}

.c5 {
    h3, h5, hr {
        display: none;
    }
    transition: all ease 0.5s;
}

.c5:hover {
    h3 {
        display: block;
        font-family: 'Truculenta', sans-serif;
        font-weight: 750;
        color: #fff;
        font-size: 30px;
        text-align: center;
        margin: -125px 0 0 -50px;
    }
    h5 {
        display: block;
        color: #fff;
        font-size: 20px;
        text-align: center;
        margin: -10px 0 0 -50px;
        font-family: 'Times New Roman', Times, serif;
        font-style: italic;
    }
    
    transition: all ease 0.5s;
}

.card5 {
    flex: 0 0 auto; /* Prevent cards from stretching */
    width: 200px; /* Adjust card width as needed */
    height: 100%; /* Make cards the same height as the slider */
    background-color: #222;
    margin-right: 50px; /* Add spacing between cards */
    padding: 20px;
    transition: all ease 0.5s;
    box-sizing: border-box;
    border-radius: 500px;
    background-image: url('../assets/parrot.jpg');
    background-size: cover;
}

.c6 {
    h3, h5, hr {
        display: none;
    }
    transition: all ease 0.5s;
}

.c6:hover {
    h3 {
        display: block;
        font-family: 'Truculenta', sans-serif;
        font-weight: 750;
        color: #fff;
        font-size: 30px;
        text-align: center;
        margin: -125px 0 0 -50px;
    }
    h5 {
        display: block;
        color: #fff;
        font-size: 20px;
        text-align: center;
        margin: -10px 0 0 -50px;
        font-family: 'Times New Roman', Times, serif;
        font-style: italic;
    }
    
    transition: all ease 0.5s;
}

.card6 {
    flex: 0 0 auto; /* Prevent cards from stretching */
    width: 200px; /* Adjust card width as needed */
    height: 100%; /* Make cards the same height as the slider */
    background-color: #222;
    margin-right: 50px; /* Add spacing between cards */
    padding: 20px;
    transition: all ease 0.5s;
    box-sizing: border-box;
    border-radius: 500px;
    background-image: url('../assets/jlpo.png');
    background-size: cover;
}

.card1:hover, .card2:hover, .card3:hover, .card4:hover, .card5:hover, .card6:hover {
    filter: blur(5px) opacity(0.5);
    transition: all ease 0.5s;
}



.controls {
    margin-top: 10px;
    text-align: center;
}

.controls span {
    margin: 20px auto 0 32px;
    font-family: 'Open Sans', sans-serif;
    font-weight: 900;
    cursor: pointer;
    font-size: 35px;
}

.controls span:hover {
    color: #fff;
    transition: all ease 0.5s;
}
</style>
