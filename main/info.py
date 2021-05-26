def bold(string):
    return f'<span class="mytextcolor">{string}</span>'


def link(string, url):
    return f'<a href="{url}" target="blank">{string}</a>'


github = "https://github.com/anhsirk0"

about = [
    f"I'm {bold('Aman Kumar')}, also known as Krishna ({link(bold('Anhsirk0'), github)})",
    f"I'm currently studying {bold('Computer Science')} at Kurukshetra University",
    f"{bold('FOSS')} enthusiast, and {bold('Open Source')} contributor",
    f"I'm a {bold('GNU/Linux')} fan, been using it for Four years"
]

likes = [
    f"{bold('Linux')}, {bold('Text editors')} and working in a {bold('terminal')}",
    f"{bold('Programming')}, particularly {bold('Scripting')}",
    f"Any {bold('crafty')} stuff like {bold('Origami')}, {bold('Kirigami')} and {bold('Inkscaping')}",
    f"solving mathematical puzzles, like {bold('Sudoku')}, {bold('Kakuro')} and {bold('Unequal')}",
    f"Playing {bold('Chess')} and watching Chess games",
]

skills = [
    {'name': 'Bash', 'pic': 'bash.png'},
    {'name': 'Perl', 'pic': 'perl.png'},
    {'name': 'Python', 'pic': 'python.png'},
    {'name': 'Django', 'pic': 'django.png'},
    {'name': 'Materialize', 'pic': 'materialize.png'},
    {'name': 'Rust', 'pic': 'rust.png'},
    {'name': 'R', 'pic': 'r.png'},
    {'name': 'Javascript', 'pic': 'js.png'},
]

web_projects = [
    {
        'title': 'Hotels',
        'description': 'Hotel booking website with payment gateway',
        'pic': 'hotel.png',
        'video': 'https://www.youtube.com/embed/T2YO75QdiM0?enablejsapi=1',
        'modal': 'modal1',
        'color': 'blue darken-4',
        'playcolor': 'blue darken-2',
        'github': 'github/anhsirk0',
        'more': [
            '''
            Search for hotels or browse locations.
            Database includes Indian hotels from makemytrip.
            Payments via Paytm gateway.
            '''
        ]
    },

    {
        'title': 'Network',
        'description': 'Social networking site post, like, follow people',
        'pic': 'network.png',
        'video': 'https://www.youtube.com/embed/o4loHm9E-_4?enablejsapi=1',
        'modal': 'modal2',
        'color': 'deep-purple darken-2',
        'playcolor': 'deep-purple lighten-1',
        'github': 'github/anhsirk0',
        'more': [
            '''
            Simple social networking site.
            Create posts, like and comment on posts, follow people.
            View all posts.
            Posts can be edited later.
            '''
        ]
    },

    {
        'title': 'Finance',
        'description': 'Buy and sell stocks, stock data used from iexcloud api',
        'pic': 'finance.png',
        'video': 'https://www.youtube.com/embed/vgEEhBSzJrk?enablejsapi=1',
        'modal': 'modal3',
        'color': 'red darken-1',
        'playcolor': 'red lighten-1',
        'github': 'github/anhsirk0',
        'more': [
            '''
            View share values, buy and sell shares.
            Uses iexcloud API to get share data in real time.
            Keeps history of all the transactions.
            '''
        ]
    },

    {
        'title': 'Auctions',
        'description': 'Ebay like website, auctions & bidding on items',
        'pic': 'auction.png',
        'video': 'https://www.youtube.com/embed/7hyqdiwGjto?enablejsapi=1',
        'modal': 'modal4',
        'color': 'indigo',
        'playcolor': 'indigo lighten-2',
        'github': 'github/anhsirk0',
        'more': [
            '''
            Create item listing or bid on items.
            Browse items by categories, add to watchlist.
            Notifications related to user's items and bids.
            '''
        ]
    },
]

cli_projects = [
    {
        'title': 'fm6000',
        'description': 'Fetch-master-6000 system information fetch tool',
        'pic': 'fm6000.png',
        'video': 'https://www.youtube.com/embed/xoNMVz4_YHM?enablejsapi=1',
        'modal': 'modal5',
        'color': 'teal darken-2',
        'playcolor': 'teal',
        'github': 'https://github.com/anhsirk0/fetch-master-6000',
        'more': [
            'Simple Dilbert themed system information fetching tool for Linux, BSD and MacOS.',
            'Written in Perl.'
        ]
    },

    {
        'title': 'Arranger',
        'description': 'Simple and capable Files and Directory arranger/cleaner',
        'pic': 'arranger.png',
        'video': 'https://www.youtube.com/embed/94wBYYuPHdM?enablejsapi=1',
        'modal': 'modal6',
        'color': 'indigo darken-2',
        'playcolor': 'indigo',
        'github': 'https://github.com/anhsirk0/file-arranger',
        'more': [
            'Arrange and clean Directories by moving files according to their extension type.',
            'Written in Perl',
        ]
    },

    {
        'title': 'Quploader',
        'description': 'Create slide-show of quotes & upload on Dailymotion',
        'pic': 'qupload.png',
        'video': 'https://www.youtube.com/embed/6SPltQMETTM?enablejsapi=1',
        'modal': 'modal7',
        'color': 'blue-grey darken-3',
        'playcolor': 'blue-grey darken-1',
        'github': 'https://github.com/anhsirk0/quote-uploader',
        'more': [
            'Scrape images from Brainyquote, create slideshow and upload to Dailymotion',
            'Written in Bash'
        ]
    },

    {
        'title': 'News',
        'description': 'News and article viewing utility using New-York times API',
        'pic': 'news.png',
        'video': 'https://www.youtube.com/embed/Ov5L_VqU85k?enablejsapi=1',
        'modal': 'modal8',
        'color': 'brown darken-2',
        'playcolor': 'brown',
        'github': 'https://github.com/anhsirk0/news-cli',
        'more': [
            'View news provided by NY times API. Print colored output, with title and url for each article.',
            'Written in Rust',
        ]
    },
]

game_projects = [
    {
        'title': 'Game of life',
        'description': "Conway's game of life simulation",
        'pic': 'life.png',
        'color': 'blue-grey darken-3',
        'github': 'https://github.com/anhsirk0/pygames/tree/master/Game_of_Life',
        'more': [
            "Simulation of John Conway's game of life.",
            "Made with pygame.",
        ]
    },

    {
        'title': 'Barasingga',
        'description': 'Two player strategy board game',
        'pic': 'barasingga.png',
        'color': 'brown darken-4',
        'github': 'https://github.com/anhsirk0/barasingga-ai',
        'more': [
            "Much like chess",
            "Capture opponents pieces to win",
            "Made with pygame.",
        ]
    },

    {
        'title': 'Pong',
        'description': 'Simple one player Pong game',
        'pic': 'pong.png',
        'color': 'indigo darken-3',
        'github': 'https://github.com/anhsirk0/pygames/tree/master/Pong',
        'more': [
            "Control the hitting pad with up & down, hit the ball and score points.",
            "Made with pygame.",
        ]
    },

    {
        'title': 'Snake',
        'description': 'Classic snake game, eat food & grow',
        'pic': 'snake.png',
        'color': 'grey darken-3',
        'github': 'https://github.com/anhsirk0/pygames/tree/master/Snake',
        'more': [
            "Control snake via arrow keys, eat food and avoid collision with self.",
            "Made with pygame.",
        ]
    },
]

tools = [
    {'name': 'Kakoune', 'pic': 'kakoune.png'},
    {'name': 'Atom', 'pic': 'atom.png'},
    {'name': 'Git', 'pic': 'git.png'},
    {'name': 'Github', 'pic': 'github.png'},
    {'name': 'Inkscape', 'pic': 'inkscape.png'},
    {'name': 'Fish', 'pic': 'fish.png'},
]

award1 = [
    {
        'name': 'CS50x',
        'about': 'Introduction to Computer Science',
        'content': [
            f"{bold('About the course:')}",
            f"CS50, is {bold('Harvard')}'s largest course.",
            f"Topics include {bold('abstraction')}, {bold('algorithms')}, {bold('data structures')}, {bold('resource management')}, {bold('security')}, {bold('software engineering')}, and {bold('web development')}.",
            f"Languages include {bold('C')}, {bold('Python')}, {bold('SQL')}, and {bold('JavaScript')} plus {bold('CSS')} and {bold('HTML')}.",
            f"Problem sets inspired by {bold('real-world domains')} of biology, cryptography, finance, forensics, and gaming.",
        ],
        'link':'https://cs50.harvard.edu/certificates/36ed6300-0616-4e84-bdef-c9f545f00772'
    },

    {
        'name': "CS50's",
        'about': 'Introduction to Artificial Intelligence with Python',
        'content': [
            f"{bold('About the course:')}",
            f"CS50ai explores the concepts & algorithms at the foundation of modern {bold('artificial intelligence')}.",
            f"Diving into the ideas that give rise to technologies like {bold('game-playing engines')}, {bold('handwriting recognition')}, and {bold('machine translation')}.",
            f"Topics includes {bold('graph search')} algorithms, {bold('classification')}, {bold('optimization')}, {bold('reinforcement learning')} and {bold('deep-learning')}."
        ],
        'link':'https://cs50.harvard.edu/certificates/cc2431ae-68d7-4c3c-acb1-3b6f31a5115c'
    },

    {
        'name': 'Microsoft -',
        'about': 'Introduction to Python for Data Science!',
        'content': [
            f"{bold('About the course:')}",
            f"This course explores some basics concepts of {bold('Data Science')}",
            f"Topics include {bold('Python')} basics, {bold('numpy')}, plotting with {bold('matplotlib')} and the basics of {bold('pandas')}"
        ],
        'link':'https://courses.edx.org/certificates/67a96f61fbc34dbf8f27a24958ab34f2'
    },
]

award2 = [
    {
        'name': 'CS50',
        'about': 'Web programming with Python and Javascript',
        'content': [
            f"{bold('About the course:')}",
            f"This course picks up where {bold('CS50x')} leaves off.",
            f"Create ",
            f"Topics include {bold('database')} design, {bold('scalability')}, {bold('security')}, and {bold('user experience')}.",
            f"Through {bold('hands-on projects')}, learn to write and use {bold('APIs')}, create {bold('interactive UIs')}, and leverage {bold('cloud services')} like GitHub and Heroku.",
        ],
        'link':'https://cs50.harvard.edu/certificates/1dad5ec0-ae1c-42ff-97c0-5bff142a04d6'
    },

    {
        'name': 'HarvardX -',
        'about': 'Data Science: R Basics',
        'content': [
            f"{bold('About the course:')}",
            f"Basic {bold('R')} syntax",
            f"Foundational R programming concepts such as {bold('data types')}, {bold('vectors arithmetic')}, and {bold('indexing')}",
            f"How to perform operations in R including sorting, {bold('data wrangling')} using {bold('dplyr')}, and {bold('making plots')}",
        ],
        'link':'https://courses.edx.org/certificates/1d2e8d17aba84ff6a5fb908fdd6f7807'
    },

    {
        'name': 'HarvardX -',
        'about': 'Data Science: Probability',
        'content': [
            f"{bold('About the course:')}",
            f"Important concepts in {bold('probability theory')} including random variables and independence",
            f"How to perform a {bold('Monte Carlo simulation')}",
            f"The meaning of expected values and {bold('standard errors')} and how to compute them in R",
            f"The importance of the {bold('Central Limit Theorem')}",
        ],
        'link':'https://courses.edx.org/certificates/ae307c9c39dd4cd189a0b88e5f2cc9d3'
    },

]

info = [
    # {
    #     'name': 'Birthday',
    #     'detail': '15 August, 1997',
    #     'icon': 'cake'
    # },

    {
        'name': 'Lives in',
        'detail': 'Kurukshetra, India',
        'icon': 'room'
    },

    {
        'name': 'Email',
        'detail': 'krishna404@yandex.com',
        'icon': 'email'
    },
    {
        'name': 'Phone',
        'detail': '+91 81307 31427',
        'icon': 'phone'
    },
]

social = [
    {
        'name': 'github',
        'link': github
    },
    {
        'name': 'linkedin',
        'link': 'https://www.linkedin.com/in/aman-kumar-b42589212/'
    },
    {
        'name': 'reddit',
        'link': 'https://www.reddit.com/user/anhsirk0'
    },
    {
        'name': 'telegram',
        'link': 'https://t.me/anhsirk0'
    },
]
