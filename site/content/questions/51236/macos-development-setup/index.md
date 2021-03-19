+++
type = "question"
title = "MacOS development setup"
description = '''Hi all, I&#x27;m trying to compile Wireshark on my Mac, but I do not want to use the provided script to install dependencies. I have my own libraries (MacPorts mostly), and they are working. The problem is: configure can&#x27;t find QT. I installed also QT5 in my home directory. it works, but Wireshark&#x27;s conf...'''
date = "2016-03-28T11:19:00Z"
lastmod = "2016-03-28T13:41:00Z"
weight = 51236
keywords = [ "compile", "macosx", "qt" ]
aliases = [ "/questions/51236" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [MacOS development setup](/questions/51236/macos-development-setup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51236-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm trying to compile Wireshark on my Mac, but I do <em>not</em> want to use the provided script to install dependencies. I have my own libraries (MacPorts mostly), and they are working.</p><p>The problem is: configure can't find QT. I installed also QT5 in my home directory. it works, but Wireshark's configure ignores it.</p><p>Any solution ?</p><p>Thanks,</p><p>T.</p></div><div id="question-tags" class="tags-container tags">compile macosx qt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '16, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/d37d57bb20ae8bf3d98ae6ff612b078a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tommaso%20Pecorella&#39;s gravatar image" /><p>Tommaso Peco...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tommaso Pecorella has no accepted answers">0%</span></p></div></div><div id="comments-container-51236" class="comments-container"><span id="51247"></span><div id="comment-51247" class="comment"><div id="post-51247-score" class="comment-score"></div><div class="comment-text"><p>Which version of Qt 5 did you install?</p></div><div id="comment-51247-info" class="comment-info"><span class="comment-age">(28 Mar '16, 19:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-51236" class="comment-tools"></div><div class="clear"></div><div id="comment-51236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51237"></span>

<div id="answer-container-51237" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51237-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What do your <code>PATH</code> and <code>PKG_CONFIG_PATH</code> environment variables look like? Assuming you have Qt 5.6 with the "clang 64-bit" components installed you should have <code>~/Qt/5.6/clang_64/bin</code> in your <code>PATH</code> and <code>~/Qt/5.6/clang_64/lib/pkgconfig</code> in your <code>PKG_CONFIG_PATH</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '16, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-51237" class="comments-container"><span id="51238"></span><div id="comment-51238" class="comment"><div id="post-51238-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>both are set (they weren't), but the result is the same.</p><p>checking if profile builds must be generated... no checking for GLIB... yes checking for Qt5Core - version &gt;= 5.0.0... no checking for QtCore - version &gt;= 4.7.0... no configure: error: Qt is not available 21:17:47:~/git/wireshark pecos$ env | grep PATH PATH=/opt/local/bin:/opt/local/sbin:/opt/local/libexec/qt4/bin/:/usr/texbin:/Users/pecos/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/usr/local/MacGPG2/bin:/Library/TeX/texbin:/Users/pecos/Qt/5.6/clang_64/bin PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/X11/lib/pkgconfig:/Users/pecos/Qt/5.6/clang_64/lib/pkgconfig/ 21:17:49:~/git/wireshark pecos$</p></div><div id="comment-51238-info" class="comment-info"><span class="comment-age">(28 Mar '16, 12:20)</span> Tommaso Peco...</div></div><span id="51239"></span><div id="comment-51239" class="comment"><div id="post-51239-score" class="comment-score"></div><div class="comment-text"><p>What does <code>qmake -query</code> print? (and what version of Qt4 is installed in /opt/local?)</p></div><div id="comment-51239-info" class="comment-info"><span class="comment-age">(28 Mar '16, 12:27)</span> Gerald Combs ♦♦</div></div><span id="51272"></span><div id="comment-51272" class="comment"><div id="post-51272-score" class="comment-score"></div><div class="comment-text"><p>For QT4 it is:</p><pre><code>01:53:17:~/git/wireshark pecos$ qmake -query
QT_INSTALL_PREFIX:/opt/local/libexec/qt4
QT_INSTALL_DATA:/opt/local/libexec/qt4/share
QT_INSTALL_DOCS:/opt/local/libexec/qt4/share/doc
QT_INSTALL_HEADERS:/opt/local/libexec/qt4/include
QT_INSTALL_LIBS:/opt/local/libexec/qt4/lib
QT_INSTALL_FRAMEWORKS:/opt/local/libexec/qt4/Library/Frameworks
QT_INSTALL_BINS:/opt/local/libexec/qt4/bin
QT_INSTALL_PLUGINS:/opt/local/libexec/qt4/share/plugins
QT_INSTALL_IMPORTS:/opt/local/libexec/qt4/share/imports
QT_INSTALL_TRANSLATIONS:/opt/local/libexec/qt4/share/translations
QT_INSTALL_CONFIGURATION:/opt/local/libexec/qt4/share/sysconf
QT_INSTALL_EXAMPLES:/opt/local/libexec/qt4/share/examples
QT_INSTALL_DEMOS:/opt/local/libexec/qt4/share/demos
QMAKE_MKSPECS:/opt/local/libexec/qt4/share/mkspecs
QMAKE_VERSION:2.01a
QT_VERSION:4.8.7</code></pre><p>For QT5:</p><pre><code>00:07:02:~/git/wireshark pecos$ ~/Qt/5.6/clang_64/bin/qmake -query
QT_SYSROOT:
QT_INSTALL_PREFIX:/Users/pecos/Qt/5.6/clang_64
QT_INSTALL_ARCHDATA:/Users/pecos/Qt/5.6/clang_64
QT_INSTALL_DATA:/Users/pecos/Qt/5.6/clang_64
QT_INSTALL_DOCS:/Users/pecos/Qt/Docs/Qt-5.6
QT_INSTALL_HEADERS:/Users/pecos/Qt/5.6/clang_64/include
QT_INSTALL_LIBS:/Users/pecos/Qt/5.6/clang_64/lib
QT_INSTALL_LIBEXECS:/Users/pecos/Qt/5.6/clang_64/libexec
QT_INSTALL_BINS:/Users/pecos/Qt/5.6/clang_64/bin
QT_INSTALL_TESTS:/Users/pecos/Qt/5.6/clang_64/tests
QT_INSTALL_PLUGINS:/Users/pecos/Qt/5.6/clang_64/plugins
QT_INSTALL_IMPORTS:/Users/pecos/Qt/5.6/clang_64/imports
QT_INSTALL_QML:/Users/pecos/Qt/5.6/clang_64/qml
QT_INSTALL_TRANSLATIONS:/Users/pecos/Qt/5.6/clang_64/translations
QT_INSTALL_CONFIGURATION:/Users/pecos/Qt/5.6/clang_64
QT_INSTALL_EXAMPLES:/Users/pecos/Qt/Examples/Qt-5.6
QT_INSTALL_DEMOS:/Users/pecos/Qt/Examples/Qt-5.6
QT_HOST_PREFIX:/Users/pecos/Qt/5.6/clang_64
QT_HOST_DATA:/Users/pecos/Qt/5.6/clang_64
QT_HOST_BINS:/Users/pecos/Qt/5.6/clang_64/bin
QT_HOST_LIBS:/Users/pecos/Qt/5.6/clang_64/lib
QMAKE_SPEC:macx-clang
QMAKE_XSPEC:macx-clang
QMAKE_VERSION:3.0
QT_VERSION:5.6.0</code></pre></div><div id="comment-51272-info" class="comment-info"><span class="comment-age">(29 Mar '16, 15:08)</span> Tommaso Peco...</div></div></div><div id="comment-tools-51237" class="comment-tools"></div><div class="clear"></div><div id="comment-51237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51243"></span>

<div id="answer-container-51243" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51243-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using cmake or autotools build? Also, if you are not running macos-setup, then take a look at the output of my script run <strong>and adapt it to your environment</strong>:</p><pre><code># From the output of macosx-setup.sh
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/Qt5.5.1/5.5/clang_64/lib/pkgconfig:/usr/X11/lib/pkgconfig
export CMAKE_PREFIX_PATH=:/usr/local/Qt5.5.1/5.5/clang_64/lib/cmake
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/Qt5.5.1/5.5/clang_64/bin</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '16, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/f1397f7833ee927f0c26a9fcb92fff11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmayer&#39;s gravatar image" /><p>jmayer<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmayer has no accepted answers">0%</span></p></div></div><div id="comments-container-51243" class="comments-container"><span id="51245"></span><div id="comment-51245" class="comment"><div id="post-51245-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I was missing the CMAKE_PREFIX_PATH... but it didn't help either.</p><p>make, yes. Autotools, yes. Script adapted, check. Still, configure doesn't find Qt (yes, I tried to run the scripts to fix the bogus QT packageconfig files)</p></div><div id="comment-51245-info" class="comment-info"><span class="comment-age">(28 Mar '16, 16:55)</span> Tommaso Peco...</div></div><span id="51274"></span><div id="comment-51274" class="comment"><div id="post-51274-score" class="comment-score"></div><div class="comment-text"><p>Well, if you are doing an autotools build then yes, adding the CMAKE_PREFIX_PATH will not resolve your problem - CMAKE is an alternative to autotools, not a helper tool or an addition. So if autotools fail for you, maybe just try the CMAKE way (look at README.cmake at the toplevel directory).</p></div><div id="comment-51274-info" class="comment-info"><span class="comment-age">(29 Mar '16, 16:45)</span> jmayer</div></div></div><div id="comment-tools-51243" class="comment-tools"></div><div class="clear"></div><div id="comment-51243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

