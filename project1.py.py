import media
import fresh_tomatoes

divergent = media.Movie("Divergent",
                        "A girl with extra ordinary abilities",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")

me_before_you = media.Movie("Me before you",
                            "An amazing love story",
                            "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
                            "https://www.youtube.com/watch?v=Eh993__rOxA")

xXx = media.Movie("xXx",
                  "Return of the Xander Cage",
                  "https://upload.wikimedia.org/wikipedia/en/9/9c/Xxx_return_of_xander_cage_film_poster.jpeg",
                  "https://www.youtube.com/watch?v=MQEFmHsseaU")

insurgent = media.Movie("Insurgent",
                         "A story about a girl who unravel a conspiracy that threatens their lives.",
                         "https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg",
                         "https://www.youtube.com/watch?v=IR-l_TSjlEo")

iron_sky = media.Movie("Iron Sky",
                       "Enter the hollow Earth",
                       "https://upload.wikimedia.org/wikipedia/en/6/6f/Iron_sky_poster.png",
                       "https://www.youtube.com/watch?v=NG2utrMwTyY")

hidden_figures = media.Movie("Hidden figures",
                              "The launch of astronaut John Glenn into orbit, a stunning achievement that restored the nation's confidence, turned around the Space Race, and galvanized the world.",
                              "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",
                              "https://www.youtube.com/watch?v=5wfrDhgUMGI")


movies = [divergent, me_before_you, xXx, insurgent, iron_sky, hidden_figures]
fresh_tomatoes.open_movies_page(movies)                 
