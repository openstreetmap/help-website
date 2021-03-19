+++
type = "question"
title = "Is UDP-Lite checksum correct (IPv6) ?"
description = '''the packet 00 50 56 c0 00 01 //dst mac 00 0c 29 fb 59 a8 //src mac 86 dd  60 00 00 00 //ipv6 00 28 //payload length 88 //next header UDP-Lite 80 //hop limit 20 01 00 00 00 00 00 00 00 00 00 00 00 00 00 01 //src ip 20 01 00 00 00 00 00 00 00 00 00 00 00 00 00 02 //dst ip 80 00 //src port 94 90 //dst ...'''
date = "2012-06-10T09:26:00Z"
lastmod = "2012-06-10T12:52:00Z"
weight = 11798
keywords = [ "checksum", "udp-lite", "ipv6" ]
aliases = [ "/questions/11798" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is UDP-Lite checksum correct (IPv6) ?](/questions/11798/is-udp-lite-checksum-correct-ipv6)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11798-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>the packet<br />
00 50 56 c0 00 01 //dst mac<br />
00 0c 29 fb 59 a8 //src mac<br />
86 dd<br />
60 00 00 00 //ipv6<br />
00 28 //payload length<br />
88 //next header UDP-Lite<br />
80 //hop limit<br />
20 01 00 00 00 00 00 00 00 00 00 00 00 00 00 01 //src ip<br />
20 01 00 00 00 00 00 00 00 00 00 00 00 00 00 02 //dst ip<br />
80 00 //src port<br />
94 90 //dst port<br />
00 08 //checksum coverage<br />
aa b1 //checksum<br />
61 62 //data<br />
63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72<br />
73 74 75 76 77 61 62 63 64 65 66 67 68 69<br />
//end<br />
when I open the packet with wireshark 1.6.0, the checksum is correct. But wireshark 1.6.8 tells me that the checksum is incorrect, it should be 0xaa89. Does payload length include IPv6 header length(40 bytes) when check UDP-Lite checksum?</p></div><div id="question-tags" class="tags-container tags">checksum udp-lite ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '12, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/297bbf4b2b131bc6f3a564f10f029f23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wolf%20Wong&#39;s gravatar image" /><p>Wolf Wong<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wolf Wong has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jun '12, 09:36</p></div></div><div id="comments-container-11798" class="comments-container"></div><div id="comment-tools-11798" class="comment-tools"></div><div class="clear"></div><div id="comment-11798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11801"></span>

<div id="answer-container-11801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11801-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The checksum is correct. A bug was introduced in <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;amp;revision=40387">r40387</a>, which was made to fix <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6711">bug 6711</a>. However, at the time, I didn't realize the slight difference in the pseudo header between UDP and UDP-Lite, as pointed out in <a href="http://tools.ietf.org/html/rfc3828#section-3.2">RFC 3828</a>. I have committed a change in <a href="http://anonsvn.wireshark.org/viewvc?revision=43187&amp;view=revision">r43187</a> to fix this and <a href="http://wiki.wireshark.org/Development/Roadmap">I scheduled it</a> to be backported to 1.8.0.rc2, 1.6.9 and 1.4.14.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '12, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-11801" class="comments-container"></div><div id="comment-tools-11801" class="comment-tools"></div><div class="clear"></div><div id="comment-11801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

