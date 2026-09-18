const videoCard = document.querySelector(".video-card");
const video = document.querySelector("#animeVideo");
const playButton = document.querySelector("#videoPlay");

const vhsTime = document.querySelector("#vhsTime");
const vhsDate = document.querySelector("#vhsDate");

let playing = false;


function playVideo() {

  video
    .play()
    .then(() => {

      playing = true;

      videoCard.classList.add("playing");

    })
    .catch(() => {});

}


function pauseVideo() {

  video.pause();

  playing = false;

  videoCard.classList.remove("playing");

}


function toggleVideo() {

  if (playing) {

    pauseVideo();

  } else {

    playVideo();

  }

}


playButton.addEventListener(
  "click",
  event => {

    event.stopPropagation();

    toggleVideo();

  }
);


videoCard.addEventListener(
  "click",
  () => {

    toggleVideo();

  }
);


const hoverAvailable =
  window.matchMedia(
    "(hover: hover) and (pointer: fine)"
  );


if (hoverAvailable.matches) {

  videoCard.addEventListener(
    "mouseenter",
    () => {

      playVideo();

    }
  );


  videoCard.addEventListener(
    "mouseleave",
    () => {

      pauseVideo();

    }
  );

}


function updateVHSClock() {

  const now =
    new Date();

  let hours =
    now.getHours();

  const minutes =
    String(
      now.getMinutes()
    ).padStart(
      2,
      "0"
    );

  const period =
    hours >= 12
      ? "PM"
      : "AM";

  hours =
    hours % 12 || 12;

  const formattedHour =
    String(hours)
      .padStart(
        2,
        "0"
      );

  vhsTime.textContent =
    `${period} ${formattedHour}:${minutes}`;

}


updateVHSClock();


setInterval(
  updateVHSClock,
  30000
);


function randomGlitch() {

  videoCard.classList.add(
    "glitch"
  );


  setTimeout(
    () => {

      videoCard.classList.remove(
        "glitch"
      );

    },
    340
  );


  const next =
    2500 +
    Math.random() * 5500;


  setTimeout(
    randomGlitch,
    next
  );

}


setTimeout(
  randomGlitch,
  1800
);


const navLinks =
  document.querySelectorAll(
    ".nav a"
  );


const sections =
  document.querySelectorAll(
    "section[id], article[id]"
  );


function updateNavigation() {

  let current =
    "home";


  sections.forEach(
    section => {

      const sectionTop =
        section.offsetTop - 180;


      if (
        window.scrollY >=
        sectionTop
      ) {

        current =
          section.getAttribute(
            "id"
          );

      }

    }
  );


  navLinks.forEach(
    link => {

      link.classList.remove(
        "active"
      );


      if (
        link.getAttribute(
          "href"
        ) ===
        `#${current}`
      ) {

        link.classList.add(
          "active"
        );

      }

    }
  );

}


window.addEventListener(
  "scroll",
  updateNavigation
);



const galleries =
  document.querySelectorAll(
    ".project-gallery"
  );


galleries.forEach(
  gallery => {

    const track =
      gallery.querySelector(
        ".gallery-track"
      );

    const slides =
      Array.from(
        gallery.querySelectorAll(
          ".gallery-slide"
        )
      );

    const dots =
      Array.from(
        gallery.querySelectorAll(
          ".gallery-dot"
        )
      );

    const counter =
      gallery.querySelector(
        ".gallery-counter"
      );

    const previousButton =
      gallery.querySelector(
        ".gallery-prev"
      );

    const nextButton =
      gallery.querySelector(
        ".gallery-next"
      );


    let currentSlide = 0;


    function updateGallery(index) {

      currentSlide =
        Math.max(
          0,
          Math.min(
            index,
            slides.length - 1
          )
        );


      slides[currentSlide]
        .scrollIntoView({
          behavior: "smooth",
          block: "nearest",
          inline: "start"
        });


      dots.forEach(
        (dot, dotIndex) => {

          dot.classList.toggle(
            "active",
            dotIndex === currentSlide
          );

        }
      );


      counter.textContent =
        `${String(currentSlide + 1)
          .padStart(2, "0")} / ${String(slides.length)
          .padStart(2, "0")}`;

    }


    previousButton.addEventListener(
      "click",
      () => {

        updateGallery(
          currentSlide - 1
        );

      }
    );


    nextButton.addEventListener(
      "click",
      () => {

        updateGallery(
          currentSlide + 1
        );

      }
    );


    dots.forEach(
      (dot, index) => {

        dot.addEventListener(
          "click",
          () => {

            updateGallery(index);

          }
        );

      }
    );


    let scrollTimeout;


    track.addEventListener(
      "scroll",
      () => {

        clearTimeout(
          scrollTimeout
        );


        scrollTimeout =
          setTimeout(
            () => {

              const trackLeft =
                track.getBoundingClientRect().left;


              let closestIndex = 0;

              let closestDistance =
                Infinity;


              slides.forEach(
                (slide, index) => {

                  const slideLeft =
                    slide
                      .getBoundingClientRect()
                      .left;


                  const distance =
                    Math.abs(
                      slideLeft -
                      trackLeft
                    );


                  if (
                    distance <
                    closestDistance
                  ) {

                    closestDistance =
                      distance;

                    closestIndex =
                      index;

                  }

                }
              );


              currentSlide =
                closestIndex;


              dots.forEach(
                (dot, index) => {

                  dot.classList.toggle(
                    "active",
                    index ===
                    currentSlide
                  );

                }
              );


              counter.textContent =
                `${String(currentSlide + 1)
                  .padStart(2, "0")} / ${String(slides.length)
                  .padStart(2, "0")}`;

            },
            80
          );

      }
    );

  }
);