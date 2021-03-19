+++
type = "question"
title = "building wireshark with libpcap in /opt"
description = '''Hello, I worked on redhat and try to install wireshark from the sources. I compiled libpcap 1.8.1 with the following commands : ./configure --prefix=/opt make make install I configured wireshark 2.2.7 with the following command line : ./configure --prefix=/opt --sysconfdir=/etc --with-pcap=/opt with...'''
date = "2017-07-07T01:46:00Z"
lastmod = "2017-07-11T19:19:00Z"
weight = 62600
keywords = [ "pcap.h", "build", "libpcap", "configure" ]
aliases = [ "/questions/62600" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [building wireshark with libpcap in /opt](/questions/62600/building-wireshark-with-libpcap-in-opt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62600-score" class="post-score" title="current number of votes">0</div><span id="post-62600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I worked on redhat and try to install wireshark from the sources.</p><p>I compiled libpcap 1.8.1 with the following commands :</p><p><code>./configure --prefix=/opt make make install</code></p><p>I configured wireshark 2.2.7 with the following command line :</p><p><code>./configure --prefix=/opt --sysconfdir=/etc --with-pcap=/opt</code></p><p>with such a configuration, the make command failed several times due to the 'can't find pcap.h' failure. After correcting Makefiles on this point, the linker can't find libpcap binary ...</p><p>I had to run the following commands to compile / link the sources without error :</p><p><code>./configure --prefix=/opt --sysconfdir=/etc --with-pcap=/opt    find . -name Makefile | xargs sed 's:^\(INCLUDEDIRS .*\):\1 -I/opt/include:' -i    sed 's:^\(LDFLAGS .*\):\1 -L/opt/lib:' -i ./Makefile    make</code></p><p>Is it possible to 'correct' the configure in order not to have these failures ?</p><p>Thanks for your work.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap.h" rel="tag" title="see questions tagged &#39;pcap.h&#39;">pcap.h</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-configure" rel="tag" title="see questions tagged &#39;configure&#39;">configure</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '17, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/163586a97ea653cab990e2f83cdafd65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timy67&#39;s gravatar image" /><p><span>timy67</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timy67 has no accepted answers">0%</span></p></div></div><div id="comments-container-62600" class="comments-container"><span id="62689"></span><div id="comment-62689" class="comment"><div id="post-62689-score" class="comment-score"></div><div class="comment-text"><p>Do you have <code>pcap.h</code> in <code>/opt/include/pcap/pcap.h</code>, and the pcap library (shared or static) in <code>/opt/lib/libpcap.so</code> (shared) or <code>/opt/lib/libpcap.a</code> (static)?</p></div><div id="comment-62689-info" class="comment-info"><span class="comment-age">(11 Jul '17, 19:19)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-62600" class="comment-tools"></div><div class="clear"></div><div id="comment-62600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

