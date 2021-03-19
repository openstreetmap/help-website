+++
type = "question"
title = "Make Error."
description = '''Hello All ,  I am new to Wireshark and also linux env .  I am trying to install on ubuntu 12.04 LTS . I checked out from the version repository trying to install . ./autogen.sh ./configure Both work fine . However , in the next step. when I try to make .  It gives me below error .  yash@pc-video2:~/...'''
date = "2012-05-25T03:54:00Z"
lastmod = "2012-05-25T04:08:00Z"
weight = 11326
keywords = [ "make", "build" ]
aliases = [ "/questions/11326" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Make Error.](/questions/11326/make-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All ,</p><p>I am new to Wireshark and also linux env . I am trying to install on ubuntu 12.04 LTS . I checked out from the version repository trying to install . ./autogen.sh ./configure</p><p>Both work fine . However , in the next step. when I try to make .</p><p>It gives me below error .</p><pre><code>[email protected]:~/wireshark$ sudo make
/usr/bin/perl ./make-version.pl .
Version configuration file version.conf not found.  Using defaults.
svnversion.h unchanged.
make  all-recursive
make[1]: Entering directory `/home/yash/wireshark&#39;
Making all in tools
make[2]: Entering directory `/home/yash/wireshark/tools&#39;
Making all in lemon
make[3]: Entering directory `/home/yash/wireshark/tools/lemon&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/yash/wireshark/tools/lemon&#39;
make[3]: Entering directory `/home/yash/wireshark/tools&#39;
sed \
        -e &#39;s,@BIN_PREFIX\@,/usr/local/bin,&#39; \
        -e &#39;s,@TSHARK_BIN\@,tshark,&#39; \
        -e &#39;s,@DUMPCAP_BIN\@,dumpcap,&#39; \
        &lt; ./setuid-root.pl.in &gt; setuid-root.pl
chmod +x setuid-root.pl
make[3]: Leaving directory `/home/yash/wireshark/tools&#39;
make[2]: Leaving directory `/home/yash/wireshark/tools&#39;
Making all in wsutil
make[2]: Entering directory `/home/yash/wireshark/wsutil&#39;
/bin/bash ../libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I. -I.. -I./..  -DINET6 -DG_DISABLE_DEPRECATED -DG_DISABLE_SINGLE_INCLUDES -DGSEAL_ENABLE -DGTK_DISABLE_DEPRECATED -DGTK_DISABLE_SINGLE_INCLUDES -D_FORTIFY_SOURCE=2 -D_U_=&quot;__attribute__((unused))&quot;  -I/usr/local/include -I/usr/include &#39;-DPLUGIN_DIR=&quot;/usr/local/lib/wireshark/plugins/1.7.2&quot;&#39; -Werror -g -O2 -Wall -W -Wextra -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Warray-bounds -Wcast-align -Wformat-security -Wold-style-definition -Wno-error=unused-but-set-variable -fexcess-precision=fast -pthread -I/usr/include/gtk-2.0 -I/usr/lib/x86_64-linux-gnu/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/pango-1.0 -I/usr/include/gio-unix-2.0/ -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12   -MT airpdcap_wep.lo -MD -MP -MF .deps/airpdcap_wep.Tpo -c -o airpdcap_wep.lo airpdcap_wep.c
mv -f .deps/airpdcap_wep.Tpo .deps/airpdcap_wep.Plo
mv: cannot stat `.deps/airpdcap_wep.Tpo&#39;: No such file or directory
make[2]: *** [airpdcap_wep.lo] Error 1
make[2]: Leaving directory `/home/yash/wireshark/wsutil&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/yash/wireshark&#39;
make: *** [all] Error 2</code></pre><p>Any ideas on this ?</p><p>Best Regards, yash</p></div><div id="question-tags" class="tags-container tags">make build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '12, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/5dc8192968061e7ff0475f55dc94802f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yash&#39;s gravatar image" /><p>yash<br />
<span class="score" title="2 reputation points">2</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yash has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 May '12, 04:51</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-11326" class="comments-container"></div><div id="comment-tools-11326" class="comment-tools"></div><div class="clear"></div><div id="comment-11326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11329"></span>

<div id="answer-container-11329" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11329-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Some suggestions:</p><ol><li>run this command prior to compiling the code: <strong><code>apt-get build-dep wireshark</code></strong></li><li>Fetch the source code *.tgz instead of the current SVN trunk and try to compile that. <a href="http://wiresharkdownloads.riverbed.com/wireshark/src/wireshark-1.7.1.tar.bz2">http://wiresharkdownloads.riverbed.com/wireshark/src/wireshark-1.7.1.tar.bz2</a></li></ol><p><strong>EDIT</strong>: I was able to build the current SVN trunk on Ubuntu 12.04, after I ran: <strong><code>apt-get build-dep wireshark</code></strong></p><p>BTW: There is no reason to run <strong>make</strong> as root (<code>sudo make</code>)! Only <strong>make install</strong> requires root privileges (<code>sudo make install</code>).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '12, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 May '12, 06:14</p></div></div><div id="comments-container-11329" class="comments-container"></div><div id="comment-tools-11329" class="comment-tools"></div><div class="clear"></div><div id="comment-11329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

