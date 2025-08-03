# Blogs

* [HOME](index.html)
* [Contact Me](contact.html)
* [PROJECTS](index2.html)
* [Online Resources](resources.html)
* [Support My Work](donate.html)

#### Aug-2-2026

“Inspiration exists, but it has to find you working.” – Pablo Picasso

Since my last blog, I've been studying different programming concepts and creating projects, as well as working on old projects. The website has become dated in my opinion, so I will redesign some aspects—such as the docs on my programs—being repurposed for a brief description and preview.

In my time away, I've factory reset my computer and boot-installed Arch Linux as my kernel and distro. I chose Arch because it's great for developers. Basically, you're given the scaffolding to build your workspace, and I love that! It's definitely not for everybody, but it's certainly for developers in my—and many others’—opinion. I've made my system pretty resilient! The filesystem I chose was BTRFS, so I have a copy-on-write filesystem. This means my computer's FS has the ability to go back in time before a crash or system-killing bug—to when my machine’s files weren’t corrupted or removed. This concept is amazing to me and perfect for tinkering devs!

I learned the hard way when my system crashed and I wasn't able to boot into my Arch environment. I had to navigate through the BIOS and insert my drive (which I installed Arch on) to have some set of tools, then connect to the internet, install some things, mount the system again, and just generally look around for things that were out of place. I did my best not to remove any environment configurations. Eventually, I used the poweroff command and started the computer back up—and sure enough, I’d filled in enough blanks for the system to come back to life.

After this experience, I rushed to commit and push my projects to main on GitHub and started researching and configuring my BTRFS setup. Now, my snapshots of the OS are created by Timeshift once a day, with a max of 3 kept in the list. I also have a button on my GRUB bootloader from grub-btrfs. Grub-btrfs watches the directory that holds my snapshots, and if a change is detected, it updates the button with a regenerated list of OS snapshots.

This is great, because if I ever update something via pacman or my PC crashes really hard and breaks my system, I can just Timeshift into an older OS state instead of navigating the BIOS with my tools from the flash drive. I credit [Chris Power](https://www.youtube.com/watch?v=V1wxgWU0j0E&t=727s) with his help during my config. I really learned a lot from this experience, and now I'm better off because of it. 

Scary stuff, I have to admit—but more from a logical aspect. Personally, I don't let things move me emotionally in that way or discourage me. It was a great experience, and one for the history books pertaining to my journey as a developer. If anything did happen to brick my PC to the point that I can't reach my GRUB boot, I'd just get another PC, install Neovim and Git, clone my Neovim config, and get back to work.

I don't get wrapped up in ricing my environment; I tend to use the default commands in the terminal to be ready for anything. That being said, BTRFS is a great way to keep me going—and going!

#### Jan-12-2025

With the new year comes more progress, projects and challenges to overcome! I have been continuing my classes and learning so much since my last update. Today I added a [macro mouse recorder](ghost_mouse.html) to the projects list. I enjoy learning about and playing with new libraries inside of python, but I have to admit I want to learn more JavaScript for online applications. Instead of abandoning my current classes and jumping right in, ill just stay focused and finished what I started for now. So much to learn out there and I understand that I fall into rabbit holes of development in different languages or software, even cyber security subjects. Nevertheless ill choose a stable path to success. Next courses are heavily leaning towards JavaScript that being said. Hope Everyone had a great holiday season, now lets get back to work!

![2025](static/images/gifs/2025.gif)

#### Oct-20-2024

A quick update, still doing my classes not as much as I would like but managing to stay consistent in my progress. I've been working a lot at my day job and finding some time here and there to work on the website. The docs on my programs not so much, although I did create a program called [Recordings Helper](recording_helper.html). I would say at this point the docs are lacking. That being said I do plan to finish them all completely.

#### Oct-01-2024

Well I've had my fun with the projects and website. Its time to get back learning more lessons from [boot.](https://www.boot.dev/) For now not gonna be posting too much on youtube, although I'm going to be working more on the docs for projects. 

Feel free to reach out and [contact](contact.html) me.

![jackolantern](static/images/gifs/jacko.gif)

#### Sep-29-2024

I have been working on the [ball simulator](balls.html), and am actually having a blast! I'm learning so much while finding and solving these problems. 

People on [youtube](https://www.youtube.com/channel/UCow1BWPWc6YHN-E7I4D9XvA) seem to like the shorts I make demonstrating the different effects I create. I'm pretty satisfied with the response. Thank you everyone for the likes and subs! 

![thankyou](static/images/gifs/thankyou.gif)

#### Sep-26-2024

Today I decided to create a simulation in pygame called [Bouncing Balls.](balls.html) 

I posted a [video on youtube](https://www.youtube.com/shorts/oyrKBz1t34o) that seems to be liked by many! Perhaps ill make more of these simulations.

#### Sep,25,2024

Added a resource section in blogs, aslo learning alot of css and configuring the website. Hope it looks good! I have to admit I got kind of hung up in the web dev of this site, its actually pretty fun! The generation of this site is still from my static site generator, I just personally edit the home and projects pages for css class use. Im implenting the class cases into my program to run completly from markdown. The nav buttons are already transfered over so thats how im automatically generating them on all the pages.

#### Sep,22,2024

Wow check out this [amazing interviw](https://www.youtube.com/watch?v=O9upVbGSBFo) with Brian Kernighan and Lex Fridman! What insights into the industry..

Really exited to start working on my new website! still trying to see what this css stuff is all about. My static site generator is up and working! (This site is made with python and markdown files..) Now I can create project docs and show my work!
