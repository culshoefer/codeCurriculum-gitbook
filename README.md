Introduction to Python and PyGame
=======

This introduction to Programming in Python (and PyGame) is divided into four distinct chapters.

## Intended audience and learning outcome

There are many tutorials online for learning Python or PyGame, but we wanted to create something different. We believe that the most valuable lessons are those which actually have a practical component, an end-product that students can work towards and, once finished, show to others.

We structured our curriculum so students get to apply the concepts they've learned as quickly as possible, and, at the end, we encourage students to complete a final project.

Throughout the course, our aim is to introduce Python concepts thoroughly, but quickly move towards practical applications using PyGame. This is because we believe that students can quickly get frustated if they don't see why what they are learning is useful. However, this means that the learning curve for this course is *steep*. That's why this curriculum is intended for students **16 years and up**.

We want to keep it close to the application, without any additional distraction (apart from the occasional motivational funny picture to loosen up). As the audience is quite mature, therefore we do not want to include a framework story, but rather stick to the topic and provide guidance throughout. From our perspective, in this age, it is more about **discovering your own capabilities** rather than adapting the given framework. In our opinion students should be expected to jump directly into coding in order to keep them interested.

From our own experience, it is very hard to come up with good project ideas by oneself. This is why we include a third and fourth chapter that gradually builds up knowledge and student expectation on how to think about problems and slowly lays the responsibility for program design in the hands of the student.

What we want from students is to be able to understand the very core concepts of programming like control flow and branching and to be able to apply them together with more advanced concepts such as classes and modules. Ideally, students should be able to come up with solutions on their own.

After all, Computer Science is a very important subject having many industrial applications. Apart from that, without it we would not be able to enjoy the lovely games that we play, the apps that we use or even write an email. This wide usage of Computer Science makes it so compelling to study. A particularly fun application is game development. The simplest way to convey that is via the extremely widely used language `Python` and one of its libraries `PyGame`.

All that said, the students are encouraged to work on their own with these materials. The role of the teacher here is to stand by the students should they have questions, experience problems with the exercises etc. We also recommend having a period at the start of the class in which problems from the last time are explained or where the teacher goes through solutions of exercises.

Finally, we tried to make these teaching materials suitable for multiple levels. In the first chapters, for a lot of the exercises, there are challenge questions which the more advanced students can tackle. At parts of these exercises, the student is also encouraged to expand the exercise content by himself.

## Our team
We are a team of four first-year Computer Science students at University College London. All four of us have done programming in high school, either through self-study or because it was in the curriculum and this had a big influence on our decision to study it formally. All four of us are very passionate about programming and we want to help more students get involved into Computer Science. Our special interests mainly lie in Machine Learning and Professional Software Development.

All things aside, we love programming very much and want to pass on some of that enthusiasm! One more tip from us: Something that we all experience when programming is frustration. Don't let that frustration get the better of you. Just carry on, it will all be fine. That said, have fun exploring the world of Python!

Something we all share is a great passion for fun stuff. That is why we decided to make these materials as enjoyable as possible. However, we can only do so much. So dear novice, please take this advice: Programming is super frustrating. If you find that your program is not working after you tried for HOURS, don't give up. In the end, you will come out smarter!

## Installing Python and Pygame

### Installation requirements for Windows
Before we can start coding, we have to install Python first. Python can be downloaded at [https://www.python.org/downloads/](https://www.python.org/downloads/). There are multiple version available, but for this tutorial we will use *Python 2.7*.

If you are using *Windows*, simply click at *Download Python 2.7*. Once the download has finished, open your **Downloads** folder and open the file you have just downloaded. Then simply follow the instructions.

Later through this course we will use Pygame, a Python `module` or `library` designed for writing games. Pygame allows us to create fully featured games without having to write excessive amount of code and runs almost on every system - those are the main reasons why to use it.

Pygame can be downloaded at [www.pygame.org/downloads.shtml](www.pygame.org/downloads.shtml). Again, there are multiple version available, but for the purpose of this tutorial we will use *Pygame 1.9.1*. Since we are using *Python 2.7*, we need download the version of Pygame compatible with our Python version, named `pygame-1.9.1.win32-py2.7.msi` (which is Pygame 1.9.1. for Python 2.7).

### Installation requirements for Mac OS X
If you are using *Mac OS X, El Capitan*, you do NOT need to actually install anything - it comes with *Python 2.7* installed already. Otherwise we need to visit Python website, where we can download the installation package. Visit [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/) and find *Python 2.7*, which is the version we will be using for this tutorial.

Download the *Mac OS X 32-bit i386/PPC* installer - this is the version which runs on every Mac. Afterwards open your **Downloads** folder and open the file you have just downloaded. Then simply follow the instructions.

Pygame can be downloaded at [www.pygame.org/downloads.shtml](www.pygame.org/downloads.shtml). Again, there are multiple version available, but for the purpose of this tutorial we will use *Pygame 1.9.1*. Since we are using *Python 2.7*, we need download the version of Pygame compatible with our Python version, named `pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg` (which is Pygame 1.9.1. for Python 2.7).

### Installation requirements for Linux
*Python 2.7* is preinstalled at all Linux computers, however we need to install IDLE (Integrated Development Environment being used) and PyGame.

Open your Terminal and then:

 * If you are using *Ubuntu*, enter `sudo apt-get install idle-python2.7 python-pygame`.
 * If you are using *ArchLinux*, enter `sudo pacman install idle-python2.7 python-pygame`.

It might ask your a password, in that case enter it to start the installation.
