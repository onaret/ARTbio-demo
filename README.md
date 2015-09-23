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

##Make demo.py works
You need to install [biopython](http://biopython.org/wiki/Download)

![ARTbio Logo][ARTbio]

[ARTbio]: https://mississippi.snv.jussieu.fr/artbio/wp-content/uploads/2015/07/ARTbio_logo_wo_IBPS_small.png 