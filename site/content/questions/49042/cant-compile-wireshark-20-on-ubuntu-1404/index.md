+++
type = "question"
title = "Can&#x27;t compile Wireshark 2.0 on Ubuntu 14.04"
description = '''Couldn&#x27;t build Wireshark 2.0 on Ubuntu 14.04 $ ./configure .... checking for GTK+ - version &amp;gt;= 3.0.0... no *** Could not run GTK+ test program, checking why... *** The test program failed to compile or link. See the file config.log for the *** exact error that occured. This usually means GTK+ is ...'''
date = "2016-01-09T20:15:00Z"
lastmod = "2016-01-10T02:51:00Z"
weight = 49042
keywords = [ "wireshark" ]
aliases = [ "/questions/49042" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't compile Wireshark 2.0 on Ubuntu 14.04](/questions/49042/cant-compile-wireshark-20-on-ubuntu-1404)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49042-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Couldn't build Wireshark 2.0 on Ubuntu 14.04</p><pre><code>$ ./configure
....
checking for GTK+ - version &gt;= 3.0.0... no
*** Could not run GTK+ test program, checking why...
*** The test program failed to compile or link. See the file config.log for the
*** exact error that occured. This usually means GTK+ is incorrectly installed.
configure: error: GTK+ 3 is not available</code></pre><p>But here is my setting</p><pre><code>apt-cache policy libgtk2.0-0 libgtk-3-0
libgtk2.0-0:
  Installed: 2.24.23-0ubuntu1.3
  Candidate: 2.24.23-0ubuntu1.3
  Version table:
 *** 2.24.23-0ubuntu1.3 0
        500 http://us.archive.ubuntu.com/ubuntu/ trusty-updates/main amd64 Packages
        100 /var/lib/dpkg/status
     2.24.23-0ubuntu1 0
        500 http://us.archive.ubuntu.com/ubuntu/ trusty/main amd64 Packages
libgtk-3-0:
  Installed: 3.10.8-0ubuntu1.6
  Candidate: 3.10.8-0ubuntu1.6
  Version table:
 *** 3.10.8-0ubuntu1.6 0
        500 http://us.archive.ubuntu.com/ubuntu/ trusty-updates/main amd64 Packages
        100 /var/lib/dpkg/status
     3.10.8-0ubuntu1.4 0
        500 http://security.ubuntu.com/ubuntu/ trusty-security/main amd64 Packages
     3.10.8-0ubuntu1 0
        500 http://us.archive.ubuntu.com/ubuntu/ trusty/main amd64 Packages</code></pre><p>Any idea why?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '16, 20:15</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-49042" class="comments-container"><span id="49044"></span><div id="comment-49044" class="comment"><div id="post-49044-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any idea why?</p></blockquote><p>Probably not without seeing the <code>config.log</code> file that the very error message you report speaks of:</p><pre><code>See the file config.log for the exact error that occurred.</code></pre><p>Please open the <code>config.log</code> file in the directory in which you ran the configure script, look for "checking for GTK+ - version &gt;= 3.0.0" in that file, and update your question to include all lines from <code>config.log</code> starting with the one that contains "checking for GTK+ - version &gt;= 3.0.0" and ending with the line that says "configure: exit 1". Put 4 spaces in front of each line, just as you did with the output that you put into the question.</p></div><div id="comment-49044-info" class="comment-info"><span class="comment-age">(09 Jan '16, 20:47)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-49042" class="comment-tools"></div><div class="clear"></div><div id="comment-49042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49047"></span>

<div id="answer-container-49047" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49047-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You probably lack the GTK-dev packages</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '16, 23:37</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-49047" class="comments-container"></div><div id="comment-tools-49047" class="comment-tools"></div><div class="clear"></div><div id="comment-49047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49048"></span>

<div id="answer-container-49048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49048-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you would like to try Wireshark 2.0, try the PPA packages published by the Debian maintainer of Wireshark: <a href="https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable">https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable</a></p><hr /><p>For compilation, the <code>libgtk-3-0</code> package is not sufficient, you need <code>libgtk-3-dev</code> on Ubuntu 14.04 as well. Rather than hunting all dependencies yourself, you can take advantage of Wireshark already being in the repositories and pull in all dependencies with:</p><pre><code>sudo apt-get build-dep wireshark</code></pre><p>Note that the default GUI toolkit for Wireshark 2.0 has changed to Qt while the version in Ubuntu 14.04 uses GTK. Therefore you might want to install the additional Qt dependencies as well:</p><pre><code>sudo apt-get install qtbase5-dev qtbase5-dev-tools qttools5-dev qttools5-dev-tools qtmultimedia5-dev libqt5svg5-dev</code></pre><p>(these dependencies can also be found in the source tree at <code>debian/control</code>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '16, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-49048" class="comments-container"></div><div id="comment-tools-49048" class="comment-tools"></div><div class="clear"></div><div id="comment-49048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

