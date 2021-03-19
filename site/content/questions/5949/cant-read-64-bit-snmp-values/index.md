+++
type = "question"
title = "Can&#x27;t read 64-bit SNMP values"
description = '''I can read only until 63 bits (0x7FFFFFFFFFFFFFFF) With full 64-bit values I got this error: [Dissector bug, protocol SNMP: proto.c:1317: failed assertion &quot;length &amp;lt;= 8 &amp;amp;&amp;amp; length &amp;gt;= 1&quot;] Can you help me?'''
date = "2011-08-30T03:24:00Z"
lastmod = "2011-08-30T05:32:00Z"
weight = 5949
keywords = [ "snmp", "64-bit" ]
aliases = [ "/questions/5949" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can't read 64-bit SNMP values](/questions/5949/cant-read-64-bit-snmp-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5949-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can read only until 63 bits (0x7FFFFFFFFFFFFFFF)</p><p>With full 64-bit values I got this error:</p><p>[Dissector bug, protocol SNMP: proto.c:1317: failed assertion "length &lt;= 8 &amp;&amp; length &gt;= 1"]</p><p>Can you help me?</p></div><div id="question-tags" class="tags-container tags">snmp 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '11, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/d9bc93e648d37e99509828e1116e9529?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jbit&#39;s gravatar image" /><p>Jbit<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jbit has no accepted answers">0%</span></p></div></div><div id="comments-container-5949" class="comments-container"></div><div id="comment-tools-5949" class="comment-tools"></div><div class="clear"></div><div id="comment-5949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5955"></span>

<div id="answer-container-5955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5955-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's a signed/unsigned BER encoding thing. You try to set a Counter64 [APPLICATION 6], which is an unsigned 64 bit integer. That, in BER encoding, results in an extra zero octet prefixed to the value so that it has no sign bit set. That whole value is feed into the presentation routines found in proto.c, but these are fixed size, so a zero octet prefix breaks the size check, as you've seen.</p><p>So there you have it, a mismatch between TLV encoded values (BER) and fixed size values (typed values). The SNMP dissector should convert between these worlds, obviously it doesn't do a well enough job here. You can file a bug report on this, with a sample capture, at <a href="https://bugs.wireshark.org">bugs.wireshark.org</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5955" class="comments-container"></div><div id="comment-tools-5955" class="comment-tools"></div><div class="clear"></div><div id="comment-5955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5952"></span>

<div id="answer-container-5952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5952-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I haven't done dissector coding myself, but in programming environments that kind of problem usually points to an off-by-one error, meaning that you started counting at 1 to n instead of 0 to n-1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5952" class="comments-container"></div><div id="comment-tools-5952" class="comment-tools"></div><div class="clear"></div><div id="comment-5952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

