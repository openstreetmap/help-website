+++
type = "question"
title = "Wireshark Import Hex Dump always strip last byte of the packet"
description = '''I am trying to import below ICMP6 destination unreachable packet in hex dump into Wireshark but it keeps stripping last byte (34) here and then indicate checksum is invalid. I tried remove &#x27;34&#x27; and re-import again, in that case &#x27;4e&#x27; would be stripped instead... This is a Raw IPv6 packet and I import...'''
date = "2015-01-15T15:02:00Z"
lastmod = "2015-01-16T07:12:00Z"
weight = 39177
keywords = [ "hexdump" ]
aliases = [ "/questions/39177" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Import Hex Dump always strip last byte of the packet](/questions/39177/wireshark-import-hex-dump-always-strip-last-byte-of-the-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39177-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to import below ICMP6 destination unreachable packet in hex dump into Wireshark but it keeps stripping last byte (34) here and then indicate checksum is invalid. I tried remove '34' and re-import again, in that case '4e' would be stripped instead...</p><p>This is a Raw IPv6 packet and I imported it with below setting: Offsets: hexadecimal Encapsulation type: Raw IPv6</p><p>I tried import an ICMPv4 destination unreachable packet and it worked fine.</p><p>I am wondering if I am missing something here ? Any idea is well appreciated! thanks!</p><p>0000 60 00 00 00 00 24 3a 7c 00 00 00 00 00 00 00 00<br />
0010 00 c0 00 00 02 00 00 00 20 01 0d b8 00 01 ff ff<br />
0020 00 00 00 00 0a 2a 7b 64 01 04 28 9d 00 00 00 00<br />
0030 45 00 00 56 00 43 00 00 ff 11 3b 50 c0 00 00 01<br />
0040 c0 00 00 02 00 35 d1 4c 00 42 4e 34</p></div><div id="question-tags" class="tags-container tags">hexdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/5bf84cea20bbef3b33f74637c8814804?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gallon&#39;s gravatar image" /><p>Gallon<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gallon has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jan '15, 15:04</p></div></div><div id="comments-container-39177" class="comments-container"><span id="39184"></span><div id="comment-39184" class="comment"><div id="post-39184-score" class="comment-score"></div><div class="comment-text"><p>What version of wireshark do you use? It sounds like an old bug</p></div><div id="comment-39184-info" class="comment-info"><span class="comment-age">(15 Jan '15, 21:33)</span> Anders ♦</div></div><span id="39188"></span><div id="comment-39188" class="comment"><div id="post-39188-score" class="comment-score"></div><div class="comment-text"><p>...and if it's an old bug, there's no reason to submit it on the Wireshark Bugzilla.</p></div><div id="comment-39188-info" class="comment-info"><span class="comment-age">(15 Jan '15, 23:35)</span> Guy Harris ♦♦</div></div><span id="39189"></span><div id="comment-39189" class="comment"><div id="post-39189-score" class="comment-score"></div><div class="comment-text"><p>I can't reproduce this with the version of Wireshark on the tip of the main branch, so this might be an old bug.</p></div><div id="comment-39189-info" class="comment-info"><span class="comment-age">(15 Jan '15, 23:38)</span> Guy Harris ♦♦</div></div><span id="39190"></span><div id="comment-39190" class="comment"><div id="post-39190-score" class="comment-score"></div><div class="comment-text"><p>(By the way, why does an ICMPv6 Destination Unreachable packet have an IPv<em>4</em> packet as the packet sent to the unreachable destination?)</p></div><div id="comment-39190-info" class="comment-info"><span class="comment-age">(15 Jan '15, 23:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-39177" class="comment-tools"></div><div class="clear"></div><div id="comment-39177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39209"></span>

<div id="answer-container-39209" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39209-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This function is derived from text2pcap, and</p><blockquote>Text2pcap understands a hexdump of the form generated by od -Ax -tx1 -v. In other words, each byte is individually displayed and surrounded with a space.</blockquote><p>It that 'surrounded with a space' that's tripping you up. Add a trailing space and you should be fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '15, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-39209" class="comments-container"><span id="39213"></span><div id="comment-39213" class="comment"><div id="post-39213-score" class="comment-score"></div><div class="comment-text"><p>thanks. That helps!</p></div><div id="comment-39213-info" class="comment-info"><span class="comment-age">(16 Jan '15, 09:41)</span> Gallon</div></div><span id="39218"></span><div id="comment-39218" class="comment"><div id="post-39218-score" class="comment-score"></div><div class="comment-text"><p>As indicated, the trunk's "import from a text file" doesn't require the trailing space; the trunk's text2pcap doesn't, either. The requirement for a trailing space was a bug, and was apparently fixed at some point. I've updated the text2pcap man page to reflect that.</p></div><div id="comment-39218-info" class="comment-info"><span class="comment-age">(16 Jan '15, 10:42)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-39209" class="comment-tools"></div><div class="clear"></div><div id="comment-39209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

