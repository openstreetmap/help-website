+++
type = "question"
title = "Building 1.12 from source fails with QT problem on Xubuntu"
description = '''Hi, does anybody know what kind of QT packages I have to install on Xubuntu 14.04 to compile Wireshark 1.12 from source? ./configure went through okay, but I got a couple of QT related error messages which I was partially able to clear by installing &quot;qt4-qtconfig&quot;. Now the final lines of the &quot;make&quot; ...'''
date = "2014-08-26T08:34:00Z"
lastmod = "2014-08-26T08:56:00Z"
weight = 35757
keywords = [ "qt", "build", "ubuntu" ]
aliases = [ "/questions/35757" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Building 1.12 from source fails with QT problem on Xubuntu](/questions/35757/building-112-from-source-fails-with-qt-problem-on-xubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35757-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>does anybody know what kind of QT packages I have to install on Xubuntu 14.04 to compile Wireshark 1.12 from source? ./configure went through okay, but I got a couple of QT related error messages which I was partially able to clear by installing "qt4-qtconfig".</p><p>Now the final lines of the "make" output are</p><pre><code>Making all in ui/qt
make[2]: Entering directory `/usr/src/wireshark/wireshark-1.12.0/ui/qt&#39;
  CXX      about_dialog.o
In file included from about_dialog.cpp:25:0:
ui_about_dialog.h:13:25: fatal error: QtGui/QAction: No such file or directory
 #include &lt;qtgui qaction=&quot;&quot;&gt;
                         ^
compilation terminated.
make[2]: *** [about_dialog.o] Error 1
make[2]: Leaving directory `/usr/src/wireshark/wireshark-1.12.0/ui/qt&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/usr/src/wireshark/wireshark-1.12.0&#39;
make: *** [all] Error 2</code></pre><p>I have no idea what I need to prepare to allow "make" to do its job :-) Any help appreciated.</p></div><div id="question-tags" class="tags-container tags">qt build ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '14, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35757" class="comments-container"></div><div id="comment-tools-35757" class="comment-tools"></div><div class="clear"></div><div id="comment-35757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35760"></span>

<div id="answer-container-35760" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35760-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.qt;h=967dc41cbb97d1e5a000b083b284d9a02b41c039;hb=HEAD">README.qt</a> in the doc directory, although I think it could do with an update.</p><p>It suggests installing the qt-sdk package, and using CMake to build.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35760" class="comments-container"><span id="35771"></span><div id="comment-35771" class="comment"><div id="post-35771-score" class="comment-score"></div><div class="comment-text"><p>thx Graham, forgot to check the readme indeed. Will try to get the packages installed tomorrow when I have a faster line for downloading them.</p></div><div id="comment-35771-info" class="comment-info"><span class="comment-age">(26 Aug '14, 12:42)</span> Jasper ♦♦</div></div><span id="35786"></span><div id="comment-35786" class="comment"><div id="post-35786-score" class="comment-score"></div><div class="comment-text"><p>there was no README.qt in the doc directory of the source package 1.12.0, but even with the online version I got stuck after installing the missing QT packages since cmake doesn't run without errors (the normal "make" fails, too). What I get for cmake is</p><pre><code>-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
CAP NOT FOUND
CMake Error at cmake/modules/FindCARES.cmake:15 (INCLUDE):
  include could not find load file:

    FindWSWinLibs
Call Stack (most recent call first):
  CMakeLists.txt:587 (find_package)

CMake Error at cmake/modules/FindCARES.cmake:16 (FindWSWinLibs):
  Unknown CMake command &quot;FindWSWinLibs&quot;.
Call Stack (most recent call first):
  CMakeLists.txt:587 (find_package)

-- Configuring incomplete, errors occurred!</code></pre><p>My build skills are quite limited so I have no idea how to fix this. Maybe I should just exclude the QT version from the build process, but I have no clue how to do that, either :D</p></div><div id="comment-35786-info" class="comment-info"><span class="comment-age">(27 Aug '14, 00:24)</span> Jasper ♦♦</div></div><span id="35789"></span><div id="comment-35789" class="comment"><div id="post-35789-score" class="comment-score"></div><div class="comment-text"><p>TBH I think trying to build QT using a 1.12 source package isn't a great idea (i.e. likely to be broken), much better to use a git clone of master if you want QT</p><p>To not build QT, you'll need to pass the appropriate magic into confgure which is out of my area I'm afraid. Usually ./configure --help will give you the config options.</p></div><div id="comment-35789-info" class="comment-info"><span class="comment-age">(27 Aug '14, 02:45)</span> grahamb ♦</div></div><span id="36131"></span><div id="comment-36131" class="comment"><div id="post-36131-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham, didn't see your new comment until now. Will try to build without QT when I have the chance to try again.</p></div><div id="comment-36131-info" class="comment-info"><span class="comment-age">(09 Sep '14, 15:44)</span> Jasper ♦♦</div></div><span id="37397"></span><div id="comment-37397" class="comment"><div id="post-37397-score" class="comment-score"></div><div class="comment-text"><p>For all those who are still looking: I solved my build problem by following a hint from Robert Cragie on the developer mailing list. This is what he said:</p><pre><code>sudo apt-get install &lt;tool&gt;

git
autoconf
automake
libtool
libtool-bin
bison
flex
qt-sdk
qttools5-dev-tools
libgtk-3-dev
libpcap-dev

Then (sudoing may be required as well):

git clone https://code.wireshark.org/review/wireshark
cd wireshark
./autogen.sh
./configure
make</code></pre><p>If you want to install Wireshark, do this as well:</p><pre><code>make install
sudo ldconfig</code></pre></div><div id="comment-37397-info" class="comment-info"><span class="comment-age">(28 Oct '14, 08:06)</span> Jasper ♦♦</div></div></div><div id="comment-tools-35760" class="comment-tools"></div><div class="clear"></div><div id="comment-35760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

