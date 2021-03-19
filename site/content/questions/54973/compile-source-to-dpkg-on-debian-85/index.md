+++
type = "question"
title = "Compile source to dpkg on Debian 8.5"
description = '''Hi, I am trying to get 2.05 to compile on Debian 8.5. I have had a bit of a ride, but I got all of it working (command line from compile directory with sudo runs wireshark fine) $ WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark I am now trying to compile as a dpkg.. Had a few errors which I have ma...'''
date = "2016-08-19T03:28:00Z"
lastmod = "2016-08-19T15:06:00Z"
weight = 54973
keywords = [ "compile", "debian" ]
aliases = [ "/questions/54973" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Compile source to dpkg on Debian 8.5](/questions/54973/compile-source-to-dpkg-on-debian-85)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54973-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to get 2.05 to compile on Debian 8.5. I have had a bit of a ride, but I got all of it working (command line from compile directory with sudo runs wireshark fine)</p><p><code>$ WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark</code></p><p>I am now trying to compile as a dpkg.. Had a few errors which I have managed to workaround / fix (libcap version changed etc) but I am really stuck on:</p><pre><code>77% Building CXX object ui/qt/CMakeFiles/qtui.dir/bluetooth_hci_summary_dialog.cpp.o
In file included from /home/steve/Downloads/wireshark-2.0.5/ui/qt/bluetooth_hci_summary_dialog.cpp:23:0:
/home/steve/Downloads/wireshark-2.0.5/ui/qt/ui_bluetooth_hci_summary_dialog.h:13:25: fatal error: QtGui/QAction: No such file or directory
 #include &lt;QtGui/QAction&gt;
                     ^
compilation terminated.
ui/qt/CMakeFiles/qtui.dir/build.make:1451: recipe for target &#39;ui/qt/CMakeFiles/qtui.dir/bluetooth_hci_summary_dialog.cpp.o&#39; failed
make[4]: *** [ui/qt/CMakeFiles/qtui.dir/bluetooth_hci_summary_dialog.cpp.o] Error 1
make[4]: Leaving directory &#39;/home/steve/Downloads/wireshark-2.0.5/obj-x86_64-linux-gnu&#39;
CMakeFiles/Makefile2:8448: recipe for target &#39;ui/qt/CMakeFiles/qtui.dir/all&#39; failed
make[3]: *** [ui/qt/CMakeFiles/qtui.dir/all] Error 2
make[3]: Leaving directory &#39;/home/steve/Downloads/wireshark-2.0.5/obj-x86_64-linux-gnu&#39;
Makefile:140: recipe for target &#39;all&#39; failed
make[2]: *** [all] Error 2
make[2]: Leaving directory &#39;/home/steve/Downloads/wireshark-2.0.5/obj-x86_64-linux-gnu&#39;
dh_auto_build: make -j1 returned exit code 2
debian/rules:34: recipe for target &#39;override_dh_auto_build&#39; failed
make[1]: *** [override_dh_auto_build] Error 2
make[1]: Leaving directory &#39;/home/steve/Downloads/wireshark-2.0.5&#39;
debian/rules:27: recipe for target &#39;build&#39; failed
make: *** [build] Error 2
dpkg-buildpackage: error: debian/rules build gave error exit status 2
&gt;</code></pre><p>The directory is in /usr/include/..., I have installed QTWidgets etc. Any ideas anyone?</p></div><div id="question-tags" class="tags-container tags">compile debian</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '16, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '16, 03:52</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54973" class="comments-container"><span id="54990"></span><div id="comment-54990" class="comment"><div id="post-54990-score" class="comment-score"></div><div class="comment-text"><p>Hmm. According to QT Docs: In Qt5, QAction header is in QtWidgets include sub-directory, not in QtGui (that's true for Qt4).</p><p>Soo. Updated the ui_bluetooth_hci_summary_dialog.h to QTWidget instead of QTGui, now I have new problems :/</p><p>/home/steve/Downloads/wireshark-2.0.5/ui/qt/ui_bluetooth_hci_summary_dialog.h:146:132: error: ‘UnicodeUTF8’ is not a member of ‘QApplication’ BluetoothHciSummaryDialog-&gt;setWindowTitle(QApplication::translate("BluetoothHciSummaryDialog", "Bluetooth HCI Summary", 0, QApplication::UnicodeUTF8</p><p>Stupid question: Should Wireshark be built on QT4 or QT5??</p></div><div id="comment-54990-info" class="comment-info"><span class="comment-age">(19 Aug '16, 09:31)</span> DarrenWright</div></div></div><div id="comment-tools-54973" class="comment-tools"></div><div class="clear"></div><div id="comment-54973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54995"></span>

<div id="answer-container-54995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54995-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Updated the <code>ui_bluetooth_hci_summary_dialog.h</code></p></blockquote><p>The beginning of that file, on my machine, says:</p><pre><code>/********************************************************************************
** Form generated from reading UI file &#39;bluetooth_hci_summary_dialog.ui&#39;
**
** Created by: Qt User Interface Compiler version 5.5.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/</code></pre><p>so it's not <em>our</em> file, it's a file generated by "Qt User Interface Compiler", i.e. the <code>uic</code> command.</p><p>"Qt User Interface Compiler version 5.5.0" means it's the version of <code>uic</code> that comes with Qt 5.5; if you're building with Qt 4, you need to use the version of <code>uic</code> that comes with Qt 4, and if you're building with Qt 5, you need to use the version of <code>uic</code> that comes with Qt 5.</p><blockquote><p>/home/steve/Downloads/wireshark-2.0.5/ui/qt/ui_bluetooth_hci_summary_dialog.h:146:132: error: ‘UnicodeUTF8’ is not a member of ‘Application’</p></blockquote><p>It's a member in Qt 4, but not in Qt 5.</p><blockquote><p>Should Wireshark be built on QT4 or QT5??</p></blockquote><p>The answer to that question is "yes, because the GTK+ UI is deprecated, we don't support Qt 3 or earlier, and there is no Qt 6, so you should either build it on Qt 4 or Qt 5."</p><p>If you build it on Qt 4, you should make sure you have <em>all</em> the Qt build tools for Qt 4 installed, including <code>uic</code>.</p><p>If you build it on Qt 5, you should make sure you have <em>all</em> the Qt build tools for Qt 5 installed, including <code>uic</code>.</p><p>If you have both of them installed, the wrong one might be used. There's a comment in the <code>acinclude.m4</code> script that says:</p><pre><code>    #
    # At least in some versions of Debian/Ubuntu, and perhaps
    # other OSes, the Qt build tools are just links to a
    # program called &quot;qtchooser&quot;, and even if you want to
    # build with Qt 5, running the tool might give you the
    # Qt 4 version of the tool unless you run the tool with
    # a -qt=5 argument.
    #
    # So we look for qtchooser and, if we find it, use the
    # -qt={version} argument, otherwise we look for particular
    # tool versions using tool name suffixes.</code></pre><p>so the configure script at least <em>tries</em> to make sure the right version is used.</p><p>For CMake, we may rely on Qt to set up the right "find Qt and its tools" stuff, and that might be failing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '16, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-54995" class="comments-container"></div><div id="comment-tools-54995" class="comment-tools"></div><div class="clear"></div><div id="comment-54995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

