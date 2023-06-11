# Declaration of the Dictionary of the Courses

# We store the data in a different python file to increase readability in app.py

class Course:
    def __init__(self, course_id, name, price, description):
        self.course_id = course_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price}"


courses = [
    {
        'id': 1,
        'name': 'Piano',
        'price': '5000',
        'description': 'The piano is a versatile and timeless musical instrument that has captivated audiences for '
                       'centuries. With its rich and expressive sound, the piano offers a wide range of musical '
                       'possibilities, from delicate and introspective melodies to powerful and virtuosic '
                       'performances. Its distinctive keyboard layout and ability to produce both melodic and '
                       'harmonic elements make it a fundamental instrument in classical, jazz, and popular music '
                       'genres.'
    },
    {
        'id': 2,
        'name': 'Guitar',
        'price': '4000',
        'description': 'The guitar is a versatile and popular musical instrument with six strings and a hollow or '
                       'solid body. It is played by plucking or strumming the strings to produce notes and chords. '
                       'The guitar is commonly used in various genres of music, ranging from classical and jazz to '
                       'rock and pop, making it a fundamental instrument in contemporary music.'
    },
    {
        'id': 3,
        'name': 'Acoustic Guitar',
        'price': '3750',
        'description': 'The acoustic guitar is a popular stringed instrument known for its rich and resonant sound. '
                       'It features a hollow body and a soundboard that amplifies the vibrations of the strings, '
                       'producing a warm and natural tone. With its versatile nature, the acoustic guitar is widely '
                       'used in various musical genres, from folk and country to rock and pop.'
    },
    {
        'id': 4,
        'name': 'Electric Guitar',
        'price': '4250',
        'description': 'The electric guitar is a stringed musical instrument that produces sound through electronic '
                       'amplification. It features a solid body, pickups to convert string vibrations into electrical '
                       'signals, and various controls to shape the tone. The electric guitar revolutionized popular '
                       'music in the 20th century, enabling musicians to achieve louder volumes, experiment with '
                       'different sounds, and play a wide range of genres, from rock and blues to jazz and metal.'
    },
    {
        'id': 5,
        'name': 'Classical Guitar',
        'price': '4500',
        'description': 'The classical guitar, also known as the Spanish guitar, is a six-stringed instrument with a '
                       'rich history and distinctive sound. It is characterized by its nylon strings, wide neck, '
                       'and a resonant body, typically made of wood. Classical guitar music is often associated with '
                       'genres like classical, flamenco, and Latin, and its intricate finger-style technique allows '
                       'for expressive playing and a wide range of musical possibilities.'
    },
    {
        'id': 6,
        'name': 'Bass Guitar',
        'price': '3500',
        'description': 'Bass is a low-pitched stringed instrument that is larger than a cello and produces deep and '
                       'rich tones. It is played by using a bow or plucking the strings with the fingers. Bass is an '
                       'important instrument in many genres of music, including classical, jazz, and rock.'
    },
    {
        'id': 7,
        'name': 'Drums',
        'price': '4500',
        'description': 'Drums are a widely recognized percussion instrument, known for their powerful and rhythmic '
                       'presence in various musical genres. Consisting of a combination of drums and cymbals, '
                       'this versatile instrument provides the backbone of a band or ensemble, driving the beat and '
                       'adding depth and energy to the music. Drummers employ a wide range of techniques to create a '
                       'diverse array of sounds, making the drums an essential element in shaping the overall musical '
                       'experience.'
    },
    {
        'id': 8,
        'name': 'Percussion',
        'price': '3500',
        'description': 'Percussion is a family of musical instruments that produce sound by being struck, shaken, '
                       'or scraped. It encompasses a wide range of instruments, including drums, cymbals, '
                       'tambourines, maracas, and xylophones. Percussion instruments add rhythm, texture, and energy '
                       'to music, providing a vital foundation for many musical styles and genres.'
    },
    {
        'id': 9,
        'name': 'Bongo drum',
        'price': '2500',
        'description': 'Bongo drums are a pair of small, open-bottomed drums that are typically played with the '
                       'hands. They originated in Cuba and are an integral part of Afro-Cuban and Latin American '
                       'music. The drums are different in size, with the smaller drum called the "macho" and the '
                       'larger one known as the "hembra." Together, they produce a rich and distinctive sound, '
                       'making them popular in various genres of music around the world.'
    },
    {
        'id': 10,
        'name': 'Tambourine',
        'price': '2000',
        'description': 'The tambourine is a percussion instrument that consists of a shallow, circular frame usually '
                       'made of wood or plastic, with pairs of small metal jingles or "zils" attached to the frame. '
                       'It is played by shaking or striking the instrument, producing a jingling sound. The '
                       'tambourine is commonly used in various musical genres, including folk, pop, rock, '
                       'and traditional music from around the world, adding a distinctive rhythmic texture to the '
                       'music.'
    },
    {
        'id': 11,
        'name': 'Shakers',
        'price': '1500',
        'description': 'Shakers are percussion instruments commonly used in various musical genres and performances. '
                       'They consist of a hollow container filled with small objects, such as beads, seeds, '
                       'or metal pieces, that produce a shaking or rattling sound when the instrument is moved. '
                       'Shakers are often handheld and played by shaking, striking, or rolling them, adding rhythmic '
                       'texture and accents to music. They are popular for their simplicity, versatility, and ability '
                       'to enhance the groove and rhythm of a musical piece.'
    },
    {
        'id': 12,
        'name': 'Timpani',
        'price': '4000',
        'description': 'Timpani, also known as kettle drums, are a type of percussion instrument widely used in '
                       'orchestras and ensembles. They consist of a set of large, bowl-shaped drums with a skin or '
                       'membrane stretched over the top. Timpani produce rich, resonant sounds that can be tuned to '
                       'different pitches by adjusting the tension of the drum heads. They are played with special '
                       'mallets or sticks, and their deep, thunderous tones provide a strong rhythmic foundation and '
                       'dramatic impact in classical music compositions.'
    },
    {
        'id': 13,
        'name': 'Violin',
        'price': '4500',
        'description': 'The violin is a string instrument that is renowned for its enchanting and expressive sound. '
                       'It has a rich history dating back several centuries and is a central instrument in classical '
                       'music orchestras. With its elegant design and versatile capabilities, the violin has '
                       'captivated audiences worldwide and continues to be a beloved instrument for musicians and '
                       'music enthusiasts alike.'
    },
    {
        'id': 14,
        'name': 'Viola',
        'price': '4250',
        'description': 'Viola is a stringed musical instrument that is slightly larger than a violin and has a deeper '
                       'and warmer tone. It is played by using a bow to vibrate the strings and produce sound. Violas '
                       'are commonly used in orchestras and chamber music ensembles.'
    },
    {
        'id': 15,
        'name': 'Saxophone',
        'price': '4000',
        'description': 'Saxophone is a woodwind instrument that is widely used in many genres of music, including '
                       'jazz, blues, and classical. It was invented in the 1840s and has since become a popular '
                       'choice for musicians due to its unique sound and versatility. Saxophone come in different sizes '
                       'and pitches to suit various musical styles.'
    },
    {
        'id': 16,
        'name': ' Baritone Sax',
        'price': '3750',
        'description': 'Baritone is a low-pitched brass instrument commonly used in many genres of music, including '
                       'classical, jazz, and marching bands. is larger than a trombone and produces deep and rich '
                       'tones that are essential in creating the overall sound of an ensemble. Baritones are played '
                       'by using a mouthpiece and valves to control airflow and pitch.'
    },
    {
        'id': 17,
        'name': 'Tenor Sax',
        'price': '3500',
        'description': 'Tenor is a high-pitched brass or woodwind instrument commonly used in many genres of music, '
                       'including classical, jazz, and marching bands. It produces a bright and clear sound that is '
                       'essential in creating the overall sound of an ensemble. Tenors are played by using a '
                       'mouthpiece and valves to control airflow and pitch.'
    },
    {
        'id': 18,
        'name': 'Alto Sax',
        'price': '3250',
        'description': 'Alto is a medium-pitched brass or woodwind instrument commonly used in many genres of music, '
                       'including classical, jazz, and marching bands. It produces a warm and mellow sound that is '
                       'essential in creating the overall sound of an ensemble. Altos are played by using a '
                       'mouthpiece and valves to control airflow and pitch.'
    },
    {
        'id': 19,
        'name': 'Flute',
        'price': '3750',
        'description': "Flute is a woodwind instrument that produces a high-pitched and delicate sound. It is "
                       "commonly used in classical music but can also be heard in various genres such as jazz and "
                       "folk. Flutes are played by blowing across a hole in the instrument's head joint and "
                       "manipulating the keys to produce different notes."
    },
    {
        'id': 20,
        'name': 'Clarinet',
        'price': '3500',
        'description': 'Clarinet is a woodwind instrument that produces a warm and expressive sound. It is commonly '
                       'used in classical music, jazz, and other genres. The clarinet is played by using a single '
                       'reed and manipulating the keys to produce different notes.'
    },
    {
        'id': 21,
        'name': 'Piccolo',
        'price': '3000',
        'description': "Piccolo is a small and high-pitched member of the woodwind family that is commonly used in "
                       "orchestral and marching band music. It produces a bright and piercing sound that can cut "
                       "through other instruments in an ensemble. Piccolos are played by blowing across a hole in the "
                       "instrument's head joint and manipulating the keys to produce different notes."
    },
    {
        'id': 22,
        'name': 'Oboe',
        'price': '4000',
        'description': 'Oboe is a woodwind instrument that produces a distinctive and expressive sound. It is '
                       'commonly used in classical music but can also be heard in various genres such as folk and '
                       'jazz. Oboes are played by using a double reed and manipulating the keys to produce different '
                       'notes.'
    },
    {
        'id': 23,
        'name': 'Cello',
        'price': '4750',
        'description': 'Cello is a stringed musical instrument that is larger than a violin and produces warm and '
                       'rich tones. It is commonly used in classical music but can also be found in various genres '
                       'such as jazz and rock. Cellos are played by using a bow to vibrate the strings or by plucking '
                       'the strings with the fingers.'
    },
    {
        'id': 24,
        'name': 'Banjo',
        'price': '4000',
        'description': 'Banjo is a stringed musical instrument that is commonly used in folk and bluegrass music. It '
                       'has a distinctive twangy sound and is played by plucking the strings with the fingers or a '
                       'pick. Banjos are typically made with a circular body and a long neck with frets, and they can '
                       'have four, five, or six strings.'
    },
    {
        'id': 25,
        'name': 'Octavina',
        'price': '2000',
        'description': 'Octavina is a stringed instrument that is commonly used in traditional Philippine music. It '
                       'is similar to a guitar but produces a higher-pitched sound due to its shorter length and '
                       'higher tuning. Octavinas are played by plucking the strings with the fingers or a pick and '
                       'are often used in ensembles with other Philippine instruments.'
    },
    {
        'id': 26,
        'name': 'Banduria',
        'price': '3000',
        'description': 'Banduria is a stringed instrument that is commonly used in traditional Philippine music. It '
                       'has 14 strings that are tuned in pairs and is played by plucking the strings with a pick. '
                       'Bandurias are often used in ensembles with other Philippine instruments and are known for '
                       'their bright and lively sound.'
    },
    {
        'id': 27,
        'name': 'Mandolin',
        'price': '3500',
        'description': 'Mandolin is a stringed musical instrument that is commonly used in various genres of music, '
                       'including folk,grass, and classical. It is similar to a guitar but is smaller in size and '
                       'produces a bright and crisp sound. Mandolins are played by plucking the strings with a pick '
                       'and can have four, eight, or more strings.'
    },
    {
        'id': 28,
        'name': 'Double Bass',
        'price': '4750',
        'description': 'Double bass is a large and deep-pitched stringed instrument that is commonly used in '
                       'classical music, jazz, and other genres. It is similar to a cello but is larger in size and '
                       'produces lower tones. Double basses are played by using a bow to vibrate the strings or by '
                       'plucking the strings with the fingers.'
    },
    {
        'id': 29,
        'name': 'Tuba',
        'price': '4500',
        'description': "Tuba is a large and low-pitched brass instrument that is commonly used in orchestral, "
                       "marching band, and other ensemble music. It produces a deep and powerful sound that serves as "
                       "the foundation of the ensemble's overall sound. Tubas are played by using a mouthpiece and "
                       "valves to control airflow and pitch."
    },
    {
        'id': 30,
        'name': 'Trumpet',
        'price': '4000',
        'description': 'Trumpet is a brass instrument commonly used in jazz, classical, and other genres of music. It '
                       'produces a bright and powerful sound that can create melody and harmony. Trumpets are played '
                       'by using a mouthpiece and valves to control airflow and pitch.'
    },
    {
        'id': 31,
        'name': 'Trombone',
        'price': '4250',
        'description': 'Trombone is a brass instrument that is commonly used in many genres of music, including '
                       'classical, jazz, and marching bands. It produces a rich, mellow sound and is played by using '
                       'a mouthpiece and slide to control airflow and pitch. Trombones are essential in creating the '
                       'overall sound of an ensemble.'
    },
    {
        'id': 32,
        'name': 'French horn',
        'price': '4250',
        'description': 'French horn is a brass instrument that is commonly used in orchestral and chamber music. It '
                       'produces a warm and mellow sound that can create melody and harmony. French horns are played '
                       'by using a mouthpiece and valves to control airflow and pitch, and they require a high level '
                       'of skill and technique to play.'
    },
    {
        'id': 32,
        'name': 'Harp',
        'price': '5000',
        'description': 'Harp is a stringed musical instrument that produces a soothing and majestic sound. It is'
                       'commonly used in classical music but can also be found in various genres such as folk and '
                       'jazz. Harps are played by plucking the strings with the fingers and are known for their '
                       'intricate and complex arrangements.'
    },
    {
        'id': 33,
        'name': 'Xylophone',
        'price': '3000',
        'description': 'Xylophone is a percussion instrument that produces a bright and percussive sound. It is '
                       'commonly used in orchestral and marching band music, as well as in various genres such as '
                       'jazz and popular music. Xylophones are played by striking wooden bars with mallets to produce '
                       'different notes.'
    },
    {
        'id': 34,
        'name': 'Pipe Organ',
        'price': '6000',
        'description': 'Pipe organ is a keyboard instrument that produces a grand and majestic sound through a '
                       'complex system of pipes. It is commonly used in classical music and is often found in large '
                       'churches and concert halls. Pipe organs are played by pressing keys on the keyboard, '
                       'which activate air flow through the pipes to produce different notes.'
    },
    {
        'id': 35,
        'name': 'Bandolin',
        'price': '2500',
        'description': 'Bandolin is a stringed musical instrument that is commonly used in traditional Portuguese '
                       'music. It is similar to a mandolin but has a longer neck and a body. Bandolins are played by '
                       'plucking the strings with a pick and are known for their intricate and complex arrangements.'
    },
    {
        'id': 36,
        'name': 'Harpsichord',
        'price': '5500',
        'description': 'Harpsichord is a keyboard instrument that was popular in the Baroque era. It produces a '
                       'bright and percussive sound through plucking strings with a quill. Harpsichords are commonly '
                       'used in Baroque music and are often found in historical performances and recordings.'
    },
    {
        'id': 37,
        'name': 'Clavinet',
        'price': '4500',
        'description': 'Clavinet is an electronic keyboard instrument that was popular in funk and soul music. It '
                       'produces a percussive and metallic sound that is achieved through the of pickups and strings. '
                       'Clavinets are played by pressing keys on the keyboard, which activate the pickups to produce '
                       'different notes.'
    },
    {
        'id': 38,
        'name': 'Accordion',
        'price': '4750',
        'description': "Accordion is a musical instrument that is popular in various genres, including folk, jazz, "
                       "and classical music. It produces a distinctive sound through the use of multiple reeds and a "
                       "bellows that creates airflow. Accordions are played by pressing buttons or keys on the "
                       "instrument's side to control the airflow and produce different notes and chords."
    },
    {
        'id': 39,
        'name': 'Bagpipe',
        'price': '4000',
        'description': "Bagpipe is a wind instrument that is popular in traditional Scottish and Irish music. It "
                       "produces a distinct and powerful sound through the use of a bag that is filled with air, "
                       "which is then released through pipes. Bagpipes are played by blowing air into the bag and "
                       "squeezing it with the arm to create airflow through the pipes."
    },
    {
        'id': 40,
        'name': 'Bass Drum',
        'price': '2500',
        'description': "Bass drum is a percussion instrument that produces a deep and booming sound. It is commonly "
                       "used in various genres of music, including orchestral, marching band, and rock. Bass drums "
                       "are played by striking the drum head with a mallet or drumstick and can create rhythm and "
                       "emphasis in a musical composition."
    },
    {
        'id': 41,
        'name': 'Bell',
        'price': '2000',
        'description': "A bell is a percussion instrument that produces a ringing sound when struck. It is commonly "
                       "used in orchestral music, church services, and other ceremonies. Bells come in various sizes "
                       "and shapes, from small handbells to large tower bells, and can create a range of pitches and "
                       "tones."
    },
    {
        'id': 42,
        'name': 'Bugle',
        'price': '2500',
        'description': "Bugle is a brass instrument that is commonly used in military and marching band music. It "
                       "produces a simple and clear sound and is played by using a mouthpiece and valveless tubing to "
                       "control airflow and pitch. Bugles were originally used as a signal instrument for the "
                       "military, but they are also used in various musical compositions."
    },
    {
        'id': 43,
        'name': 'Castanets',
        'price': '1500',
        'description': "Castanets are a percussion instrument that is commonly used in Spanish and flamenco music. "
                       "They consist of two small wooden shells that are held in the hand and are played by striking "
                       "them together to create a clicking sound. Castanets can create rhythmic patterns and add a "
                       "lively and vibrant sound to a musical composition."
    },
    {
        'id': 44,
        'name': 'Concertina',
        'price': '3000',
        'description': "Concertina is a small, bellows-driven accordion-like instrument popular in traditional Irish "
                       "music. It has a unique sound that is produced when the bellows are pushed and pulled while "
                       "pressing the instrument's buttons. Concertinas are commonly used in Irish folk music and can "
                       "create a range of melodic and rhythmic patterns."
    },
    {
        'id': 45,
        'name': 'Conga',
        'price': '3500',
        'description': "Conga is a tall and narrow drum that is commonly used in Latin American and Afro-Cuban music. "
                       "It produces a deep and resonant sound and is played by striking the drum head with the hands "
                       "or fingers. Congas are often played in sets of two or more and are essential in creating a "
                       "rhythmic foundation in Latin American music."
    },
    {
        'id': 46,
        'name': 'Cornet',
        'price': '3750',
        'description': "Cornet is a brass instrument that is similar to a trumpet but has a more mellow and subdued "
                       "sound. It is commonly used in brass bands and is often played as a solo instrument in jazz "
                       "and classical music. Cornets are played by using a mouthpiece and valves to control airflow "
                       "and pitch."
    },
    {
        'id': 47,
        'name': 'Cymbal',
        'price': '2500',
        'description': "Cymbals are a percussion instrument that produces a metallic and crashing sound when struck "
                       "together. They are commonly used in various genres of music, including orchestral, rock, "
                       "and jazz. Cymbals come in various sizes and shapes, from small hi-hats to large crash "
                       "cymbals, and can create a range of dynamic and expressive sounds."
    },
    {
        'id': 48,
        'name': 'Glockenspiel',
        'price': '3000',
        'description': "Glockenspiel is a percussion instrument consisting of tuned metal bars that are struck with"
                       "mallets to produce a bright and sparkling sound. It is commonly used in orchestral and "
                       "marching band music, as well as in various genres such as pop and rock. Glockenspiels can "
                       "create melody and harmony and add a playful and whimsical sound to a musical composition."
    },
    {
        'id': 49,
        'name': 'Gong',
        'price': '4000',
        'description': "Gong is a percussion instrument that produces a deep and resonant sound when struck with a"
                       "mallet. It is commonly used in orchestral and ceremonial music, as well as in various genres "
                       "such as jazz and rock. Gongs come in various sizes and can create a wide range of dynamic and "
                       "expressive sounds."
    },
    {
        'id': 50,
        'name': 'Harmonica',
        'price': '2500',
        'description': "Harmonica is a small wind instrument that is commonly used in blues, folk, and country music. "
                       "It produces a distinctive and soulful sound when the musician inhales and exhales through the "
                       "instrument's reeds. Harmonicas come in various keys and can be played in different styles, "
                       "from single notes to complex chords and rhythms."
    },
    {
        'id': 51,
        'name': 'Electronic keyboard',
        'price': '3500',
        'description': "Electronic keyboard is a versatile musical instrument that can simulate the sounds of various"
                       "instruments and produce a wide range of tones and effects. It is commonly used in pop, rock, "
                       "and electronic music, as well as in many other genres. Electronic keyboards can be played "
                       "using different techniques, including pressing keys, using pedals, and manipulating knobs and "
                       "sliders, making it a popular choice for musicians and composers."
    },
    {
        'id': 52,
        'name': 'Maracas',
        'price': '2000',
        'description': "Maracas are a percussion instrument that consists of hollow balls or gourds filled with"
                       "seeds, beans, or beads. They produce a rattling sound when shaken, and are commonly used in "
                       "Latin American and Caribbean music. Maracas can create a range of rhythms and add a lively "
                       "and festive sound to a musical composition."
    },
    {
        'id': 53,
        'name': 'Marimba',
        'price': '4000',
        'description': "Marimba is a percussion instrument that consists of wooden bars that are struck with mallets "
                       "to produce a warm and resonant sound. It is commonly used in orchestral and Latin American "
                       "music, as well as in various genres such as jazz and pop. Marimbas can create melody and "
                       "harmony and add a rich and vibrant sound to a musical composition."
    },
    {
        'id': 54,
        'name': 'Hand Pan',
        'price': '6000',
        'description': "A handpan, also known as a hang drum, is a musical instrument that belongs to the idiophone family.The instrument is played by striking the notes with the hands or fingers. Each note on the handpan produces a resonant sound with a distinct pitch. The layout of the notes is usually arranged in a circular pattern, with a central note surrounded by several additional notes. The notes are typically tuned to a specific scale, such as a pentatonic or diatonic scale, which allows for easy melodic improvisation."
    },
    {
        'id': 55,
        'name': 'Recorder',
        'price': '3000',
        'description': "Recorder is a woodwind instrument that produces a clear and gentle sound. It is commonly used "
                       "in early music and is often played by beginners in music education. Recorders are played by "
                       "blowing air into a mouthpiece and covering and uncovering finger holes to produce different "
                       "notes. They come in various sizes and can create a range of melodic and rhythmic patterns."
    },
    {
        'id': 56,
        'name': 'Sitar',
        'price': '4500',
        'description': "Sitar is a stringed instrument that is commonly used in classical Indian music. It has a "
                       "distinctive sound that is produced by plucking the strings while pressing them against the "
                       "frets with the other hand. Sitar is known for its intricate and complex arrangements, "
                       "and can create a range of melodic and rhythmic patterns."
    },
    {
        'id': 57,
        'name': 'Snare drum',
        'price': '3500',
        'description': "Snare drum is a percussion instrument that produces a sharp and staccato sound. It is "
                       "commonly used in various genres of music, including orchestral, marching band, "
                       "and rock. Snare drums are played by striking the drum head with drumsticks or brushes and can "
                       "create a range of rhythms and dynamics in a musical composition."
    },
    {
        'id': 58,
        'name': 'Triangle',
        'price': '1500',
        'description': "The triangle is a musical instrument that belongs to the percussion family. It consists of a "
                       "steel or brass rod bent into a triangular shape, with one corner left open. When struck with "
                       "a metal beater, the triangle produces a clear, high-pitched sound that can be sustained by "
                       "damping the vibrations with the hand. Its simplicity and versatility make it a popular choice "
                       "in various musical genres, including classical, orchestral, and contemporary compositions."
    },
    {
        'id': 59,
        'name': 'Ukulele',
        'price': '3000',
        'description': "The ukulele is a small, four-stringed instrument that originated in Hawaii. It is known for "
                       "its bright and cheerful sound, making it a popular choice for beginners and experienced "
                       "musicians alike. With its compact size and simple chord structure, the ukulele is often "
                       "associated with relaxation, island vibes, and joyful music."
    },
    {
        'id': 60,
        'name': 'Vibraphone',
        'price': '4500',
        'description': "The vibraphone is a musical instrument that belongs to the percussion family. It consists of "
                       "a set of metal bars arranged in a keyboard-like layout and is played by striking the bars "
                       "with mallets. The bars are tuned to specific pitches, and the instrument produces a resonant "
                       "and melodic sound similar to a xylophone but with a distinct vibrato effect created by "
                       "rotating metal discs beneath each bar."
    },

]
