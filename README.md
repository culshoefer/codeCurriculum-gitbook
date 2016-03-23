% Introduction to Python and PyGame
% Jaromir Latal; George Pîrlea; Janós Potecki; Christoph Ulshöfer
% March 24th, 2016

Introduction to Python and PyGame
=======

This introduction to Programming in Python (and PyGame) is divided into four distinct chapters.

## Intended audience and learning outcome

There are many tutorials on-line for learning Python or PyGame, but we wanted to create something different. We believe that the most valuable lessons are those which actually have a practical component, an end-product that students can work towards and, once finished, show to others.

We structured our curriculum so students get to apply the concepts they've learned as quickly as possible, and, at the end, we encourage students to complete a final project.

Throughout the course, our aim is to introduce Python concepts thoroughly, but quickly move towards practical applications using PyGame. This is because we believe that students can quickly get frustrated if they don't see why what they are learning is useful. However, this means that the learning curve for this course is *steep*. That's why this curriculum is intended for students **16 years old and up**.

As the audience is quite mature, we do not include a framework story, but rather stick to the topic and provide guidance throughout (and the occasional funny picture to loosen up). From our perspective, learning at this age is more about **discovering your own capabilities**, rather than following a restrictive set of instructions. In our opinion, students should jump into coding as soon as possible in order to keep them interested.

From our own experience, it is difficult to come up with good project ideas yourself. This is why we include a third and fourth chapter that gradually build up the student's knowledge, train them how to think about problems and slowly lay the responsibility for program design in the student's hands.

In terms of objectives, we want students who finish this curriculum to be able to understand core programming concepts like control flow, variables and data types, input/output, functions, as well as more advanced concepts like object-oriented programming. Ideally, by the end of the course, students should be able to come up with solutions on their own, without external help.

From machine learning and artificial intelligence to the newest killer-app and virtual reality gadget, there's no lack of things to be excited about when it comes to Computer Science. In addition, programming skills are rapidly becoming basic necessities, just like reading, writing and scientific literacy. Even if you don't intend to become a programmer, understanding the fundamental concepts behind programming is going to help you later on. And if that doesn't persuade you, *well*, making games is a lot of fun!

All that being said, students are encouraged to work on their own with these materials. The role of the teacher here is to stand by the students should they have questions or experience problems with the exercises. We also recommend having a period at the start of the class in which problems from the last lesson are explained or where the teacher goes through solutions of exercises.

Finally, we tried to make these teaching materials suitable for students at different levels. For a lot of the exercises, we propose challenge questions for the more advanced students to tackle.

## Our team
We are a team of four first-year Computer Science students at University College London. All four of us have done programming in high school, either through self-study or because it was in the curriculum and this had a big influence on our decision to study it formally. All four of us are very passionate about programming and we want to help more students get involved into Computer Science. Our special interests mainly lie in Machine Learning and Professional Software Development.

All things aside, we love programming very much and want to pass on some of that enthusiasm! One more tip from us: something that we all experience when programming is frustration. Don't let that frustration get the better of you. Just carry on, it will all be fine. That said, have fun exploring the world of Python!

Something we all share is a great passion for fun stuff. That is why we decided to make these materials as enjoyable as possible. However, we can only do so much. So dear novice, please take this advice: programming is super frustrating. If you find that your program is not working after you tried for HOURS, don't give up. In the end, you will come out smarter!

## Installing Python and PyGame

### Installation requirements for Windows
Before we can start coding, we have to install Python first. Python can be downloaded at [https://www.python.org/downloads/](https://www.python.org/downloads/). There are multiple version available, but for this tutorial we will use *Python 2.7*.

If you are using *Windows*, simply click at *Download Python 2.7*. Once the download has finished, open your **Downloads** folder and open the file you have just downloaded. Then simply follow the instructions.

Later through this course we will use PyGame, a Python `module` or `library` designed for writing games. PyGame allows us to create fully featured games without having to write excessive amount of code and runs almost on every system - those are the main reasons why to use it.

PyGame can be downloaded at [www.pygame.org/downloads.shtml](www.pygame.org/downloads.shtml). Again, there are multiple version available, but for the purpose of this tutorial we will use *PyGame 1.9.1*. Since we are using *Python 2.7*, we need download the version of PyGame compatible with our Python version, named `pygame-1.9.1.win32-py2.7.msi` (which is PyGame 1.9.1. for Python 2.7).

### Installation requirements for Mac OS X
If you are using *Mac OS X, El Capitan*, you do NOT need to actually install anything - it comes with *Python 2.7* installed already. Otherwise we need to visit Python website, where we can download the installation package. Visit [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/) and find *Python 2.7*, which is the version we will be using for this tutorial.

Download the *Mac OS X 32-bit i386/PPC* installer - this is the version which runs on every Mac. Afterwards open your **Downloads** folder and open the file you have just downloaded. Then simply follow the instructions.

PyGame can be downloaded at [www.pygame.org/downloads.shtml](www.pygame.org/downloads.shtml). Again, there are multiple version available, but for the purpose of this tutorial we will use *PyGame 1.9.1*. Since we are using *Python 2.7*, we need download the version of PyGame compatible with our Python version, named `pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg` (which is PyGame 1.9.1. for Python 2.7).

### Installation requirements for Linux
*Python 2.7* is preinstalled at all Linux computers, however we need to install IDLE (Integrated Development Environment being used) and PyGame.

Open your Terminal and then:

 * If you are using *Ubuntu*, enter `sudo apt-get install idle-python2.7 python-pygame`.
 * If you are using *ArchLinux*, enter `sudo pacman install idle-python2.7 python-pygame`.

It might ask your a password, in that case enter it to start the installation.
