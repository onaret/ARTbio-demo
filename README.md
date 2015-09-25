##Setting up a GitHub repository

####Here is how you can set up a GitHub repository.

1. Let's say you have a folder containing the differents elements you want to provide for the ARTBio test.
 * A **memo** named *README.md* which will be integrated by GitHub as the description of this repositrory.
 * A **screenshot** *welcome.png* of the modified galaxy welcome page.
 * A **python** script *demo.py* and a fasta sample *sample.fasta* to test it


1. Initialise a local git repository
	```zsh
	git init
	```

1. Commit the differents files to the newly created local repository
	```zsh
	git add README.md welcome.jpg demo.py sample.fasta
	git commit -m "initializing repository"
	```

1. From your GitHub account, make a remote repository. Like this one [ARTBio-demo](https://github.com/zakrapovic/ARTbio-demo)

1. Locally add the URL of the remote repository you just made  
	*Here we assume your GitHub account already know your computer by his SSH public key. You could use HTTPS protocol instead by adding 'https://github.com/zakrapovic/ARTbio-demo.git'*
	```zsh
	git remote add origin git@github.com:zakrapovic/ARTbio-demo.git
	```


1. Push the content of the local repository to the remote one
	```zsh
	git push -u origin master
	```

####That's all! You just set up a GitHub repository.

##Setting up a Galaxy server

1. Download galaxy by cloning their GitHub repositry

	```zsh
	git clone https://github.com/galaxyproject/galaxy/
	```

1. Run it once for initialization

	```zsh
	cd galaxy
	sh run.sh
	```

1. Open the welcome.html

1. Here we remove the default message and replace it with a *frame* containing the [artbio website](https://mississippi.snv.jussieu.fr/artbio/)

	replace
	```html
 	<div class="donemessagelarge">
        <p><strong>Your Galaxy is running!</strong></p>
        <hr>
        <ul>
            <li>To learn how to use Galaxy please see the <a href="https://wiki.galaxyproject.org/Learn">wiki</a></li>
            <li>To install new tools to your Galaxy follow the <a href="https://wiki.galaxyproject.org/Admin/Tools/AddToolFromToolShedTutorial">tutorial</a></li>
            <li>To set up your Galaxy for others to use please read <a href="https://wiki.galaxyproject.org/Admin/Config/Performance/ProductionServer">this</a></li>
        </ul>
        <p><h5>Thank you for trying Galaxy.</h5></p>
    </div>
	```
	by

	```html
    <iframe src="https://mississippi.snv.jussieu.fr/artbio/" width="800" height="900" align="center"></iframe>
    <p><strong>You just put a website inside a website</strong></p>
    <div class="donemessagelarge">
        <p><h5>Thank you for considering my application.</h5></p>
    </div>
	```

1. Restart the server

	
####That's all! You just downloaded, customized, and started a Galaxy server

![ARTbio Logo][ARTbio]

[ARTbio]: https://mississippi.snv.jussieu.fr/artbio/wp-content/uploads/2015/07/ARTbio_logo_wo_IBPS_small.png 