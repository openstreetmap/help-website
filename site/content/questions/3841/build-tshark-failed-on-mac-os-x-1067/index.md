+++
type = "question"
title = "build tshark failed on Mac OS X 10.6.7"
description = '''I&#x27;m build wireshark souce code with &quot;./configure --disable-wireshark&quot;, but I got errors: Making all in wsutil /bin/sh ../libtool --tag=CC --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I./.. -I/usr/local/include  &#x27;-DPLUGIN_DIR=&quot;/usr/local/lib/wireshark/plugins/1.5.2&quot;&#x27; -Werror -DINET6 -no-cpp-precomp -...'''
date = "2011-04-30T04:58:00Z"
lastmod = "2011-04-30T18:26:00Z"
weight = 3841
keywords = [ "osx", "tshark", "build" ]
aliases = [ "/questions/3841" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [build tshark failed on Mac OS X 10.6.7](/questions/3841/build-tshark-failed-on-mac-os-x-1067)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3841-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm build wireshark souce code with "./configure --disable-wireshark", but I got errors:</p><p>Making all in wsutil<br />
/bin/sh ../libtool --tag=CC --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I./.. -I/usr/local/include<br />
'-DPLUGIN_DIR="/usr/local/lib/wireshark/plugins/1.5.2"' -Werror -DINET6 -no-cpp-precomp -D_U_="<strong>attribute</strong>((unused))" -g -O2 -Wall -W -Wextra -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Wcast-align -Wformat-security -I/usr/local/include -D_REENTRANT -I/usr/local/include/glib-2.0 -I/usr/local/lib/glib-2.0/include -MT mpeg-audio.lo -MD -MP -MF .deps/mpeg-audio.Tpo -c -o mpeg-audio.lo mpeg-audio.c<br />
mv -f .deps/mpeg-audio.Tpo .deps/mpeg-audio.Plo<br />
mv: rename .deps/mpeg-audio.Tpo to .deps/mpeg-audio.Plo: No such file or directory<br />
make[2]: <strong><em>[mpeg-audio.lo] Error 1<br />
make[1]:</em></strong> [all-recursive] Error 1<br />
make: *** [all] Error 2<br />
</p><p>What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">osx tshark build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '11, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/28091c7b659fb2bf9074674937b6cd8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huubby&#39;s gravatar image" /><p>huubby<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huubby has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>retagged 30 Apr '11, 18:27</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-3841" class="comments-container"></div><div id="comment-tools-3841" class="comment-tools"></div><div class="clear"></div><div id="comment-3841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3859"></span>

<div id="answer-container-3859" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3859-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just successfully built tshark in OS X 10.6.7 using your configure options. Your problem might have to do with libtool. Check your libtool version with the command: <strong><code>libtool -V</code></strong></p><p>My libtool version is: <strong><code>Apple Computer, Inc. version cctools-782</code></strong></p><p>If you don't have libtool installed, get it from <a href="http://www.macports.org/ports.php?by=library&amp;substr=libtool">Mac Ports</a>: <strong><code>sudo port install libtool</code></strong></p><h3 id="the-commands-i-used-to-build-and-run-tshark">The commands I used to build and run tshark:</h3><pre><code>./autogen.sh
./configure --disable-wireshark
make
WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./tshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '11, 18:26</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Apr '11, 18:32</p></div></div><div id="comments-container-3859" class="comments-container"><span id="3860"></span><div id="comment-3860" class="comment"><div id="post-3860-score" class="comment-score"></div><div class="comment-text"><p>Than you very much! It worked! I'm so stupid, I have installed another libtool in /usr/local/bin, after uninstalling this libtool, I successfully built tshark. Thanks again!</p></div><div id="comment-3860-info" class="comment-info"><span class="comment-age">(30 Apr '11, 19:58)</span> huubby</div></div></div><div id="comment-tools-3859" class="comment-tools"></div><div class="clear"></div><div id="comment-3859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

