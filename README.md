Introduction to Python and small-scale game development with PyGame
=======


This introduction to Programming in Python (and PyGame) is divided into four distinct chapters.

##Intended audience and learning outcome

These resources are different from many other tutorials on Python or PyGame. We believe that the most valuable lessons are those which actually have a practical application. As such, we want students to experience fast feedback and actually include a final project (or multiple projects) into our curriculum.

Throughout the course, we aim to move to PyGame as quickly as possible while still being able to understand what is going on. This is because we believe that students can get quite frustrated quickly if concepts are not properly introduced. At the same time, it means that the learning curve is steep. Finally, this is why this curriculum is intended for **16 years and up**.

Continuing in this manner, we do not understand this project to be about theoretical digressions. We want to keep it close to the application, without any additional distraction (apart from the occasional motivational funny picture to loosen up). As the audience is quite old, we do not want to include a framework story, but keep it to the topic and provide guidance throughout. From our perspective, in this age, it is more about **discovering your own capabilities** rather than adapting the given framework. In our opinion students should not be expected to jump directly into coding.

From our own experience, it is very hard to come up with good project ideas by oneself. This is why we include a third and fourth chapter that gradually builds up knowledge and student expectation on how to think about problems and slowly lays the responsibility for program design in the hands of the student.

What we want from students is to be able to understand the very core concepts of programming like control flow and branching and to be able to apply them together with more advanced concepts such as classes and modules. Ideally, students should be able to come up with solutions on their own.

After all, computer science is a very important subject having many industrial applications. Apart from that, without it we would not be able to enjoy the lovely games that we play, the apps that we use or even write an email. This wide usage of computer science makes it so compelling to study. A particularly fun application is game development. The simplest way to convey that is via the extremely widely used language `Python` and one of its libraries `PyGame`.

##Our team
We are a team of four first-year Computer Science students at University College London. All four of us have done programming in high school, either through self-study or because it was in the curriculum. Either way, it influenced our decision to study it formally.

However, to study Computer Science, it is not necessary to know programming beforehand. When we were learning programming, however, it was hard for us to start understanding the concepts. Were it not to our discipline, we probably would not have learned programming.

With the new official Computer Science A-Level curriculum, we have a similar problem: On the one hand, teachers have to find appropriate learning resources and want students to be excited about Computer Science. In order to solve this, we propose to provide resources for learning Programming in Python. Similarly, the incentive to program games (covered later in this resource), should make students interested in programming.

#Installing Python
Before we can start coding, we have to install Python first. Python can be downloaded at [https://www.python.org/downloads/](https://www.python.org/downloads/). There are multiple version available, but for this tutorial we will use *Python 2.7.11*.

If you are using *Windows*, simply click at *Download Python 2.7.11*. Once the download has finished, open your **Downloads** folder and open the file you have just downloaded. Then simply follow the instructions.

##Installing PyGame
Later through this course we will use Pygame, a Python `module` or `library` designed for writing games. Pygame allows us to create fully featured games without having to write excessive amount of code and runs almost on every system - those are the main reasons why to use it.

Pygame can be downloaded at [www.pygame.org/downloads.shtml](www.pygame.org/downloads.shtml). Again, there are multiple version available, but for the purpose of this tutorial we will use *Pygame 1.9.1*. Since we are using *Python 2.7.11*, we need download the version of Pygame compatible with our Python version, named `pygame-1.9.1.win32-py2.7.msi` (which is Pygame 1.9.1. for Python 2.7).

On *Windows*, launch the downloaded file and follow the instructions. After the installation process had ended, launch Python and type into the interactive shell:

`import pygame`.

If nothing appears on the screen after you have pressed the Enter key, it has been successfully installed!

##Installation requirements for Mac OS X
If you are using *Mac OS X, El Capitan*, you do NOT need to actually install anything - it comes with *Python 2.7* installed already. Otherwise we need to visit Python website, where we can download the installation package. Visit [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/) and find *Python 2.7.11*, which is the version we will be using for this tutorial. 

Download the *Mac OS X 32-bit i386/PPC* installer - this is the version which runs on every Mac. Afterwards open your **Downloads** folder and open the file you have just downloaded. Then simply follow the instructions.
