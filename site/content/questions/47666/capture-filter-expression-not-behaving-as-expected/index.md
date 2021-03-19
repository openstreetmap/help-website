+++
type = "question"
title = "Capture filter expression not behaving as expected"
description = '''I&#x27;m trying to capture TCP packets related to some type of bug I&#x27;m finding when using a Wiznet W5300. It seems to freeze up sometimes when the TCP sequence number is near the rollover point of 0xFFFFFFFF. I&#x27;m trying to capture packets near the rollover only, say within 5000 bytes before or after, bec...'''
date = "2015-11-17T07:56:00Z"
lastmod = "2015-11-17T10:03:00Z"
weight = 47666
keywords = [ "filter", "capture", "tcp", "sequence" ]
aliases = [ "/questions/47666" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter expression not behaving as expected](/questions/47666/capture-filter-expression-not-behaving-as-expected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47666-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture TCP packets related to some type of bug I'm finding when using a Wiznet W5300. It seems to freeze up sometimes when the TCP sequence number is near the rollover point of 0xFFFFFFFF.</p><p>I'm trying to capture packets near the rollover only, say within 5000 bytes before or after, because the total amount of data that moves before the bug hits is way too much.</p><p>I have 4 units running with IP addresses of .52 through .55</p><p>When I use this filter expression:</p><p>((ip[15] &gt;= 52 and ip[15] &lt;= 55) or (ip[19] &gt;= 52 and ip[19] &lt;= 55)) and ((tcp[4:4] &lt; 0x00001388))</p><p>it shows the following compilation:</p><p>(000) ldh [12]</p><p>(001) jeq #0x800 jt 2 jf 16</p><p>(002) ldb [29]</p><p>(003) jge #0x34 jt 4 jf 5</p><p>(004) jgt #0x37 jt 5 jf 8</p><p>(005) ldb [33]</p><p>(006) jge #0x34 jt 7 jf 16</p><p>(007) jgt #0x37 jt 16 jf 8</p><p>(008) ldb [23]</p><p>(009) jeq #0x6 jt 10 jf 16</p><p>(010) ldh [20]</p><p>(011) jset #0x1fff jt 16 jf 12</p><p>(012) ldxb 4*([14]&amp;0xf)</p><p>(013) ld [x + 18]</p><p>(014) jge #0x1388 jt 16 jf 15</p><p>(015) ret #65535</p><p>(016) ret #0</p><p>and it seems to correctly filter out the typical messages that do not have sequence numbers from 0 to 5000. However, when I use the filter I actually want with the additional constraint to get the high end of the sequence numbers as well:</p><p>((ip[15] &gt;= 52 and ip[15] &lt;= 55) or (ip[19] &gt;= 52 and ip[19] &lt;= 55)) and ((tcp[4:4] &lt; 0x00001388) or (tcp[4:4] &gt; 0xFFFFEC77))</p><p>I get the following compilation:</p><p>(000) ldh [12]</p><p>(001) jeq #0x800 jt 2 jf 17</p><p>(002) ldb [29]</p><p>(003) jge #0x34 jt 4 jf 5</p><p>(004) jgt #0x37 jt 5 jf 8</p><p>(005) ldb [33]</p><p>(006) jge #0x34 jt 7 jf 17</p><p>(007) jgt #0x37 jt 17 jf 8</p><p>(008) ldb [23]</p><p>(009) jeq #0x6 jt 10 jf 17</p><p>(010) ldh [20]</p><p>(011) jset #0x1fff jt 17 jf 12</p><p>(012) ldxb 4*([14]&amp;0xf)</p><p>(013) ld [x + 18]</p><p>(014) jge #0x1388 jt 15 jf 16</p><p>(015) jgt #0xffffec77 jt 16 jf 17</p><p>(016) ret #65535</p><p>(017) ret #0</p><p>which seems reasonable, but it doesn't work. It captures all packets that are not in the sequence number range I want.</p><p>Does anyone see a logic error or a numeric/sign type error? Wireshark is pretty new for me. Thanks.</p></div><div id="question-tags" class="tags-container tags">filter capture tcp sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/9386555acbf992085f85ada045a6bbec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eeabe&#39;s gravatar image" /><p>eeabe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eeabe has no accepted answers">0%</span></p></div></div><div id="comments-container-47666" class="comments-container"><span id="47667"></span><div id="comment-47667" class="comment"><div id="post-47667-score" class="comment-score">1</div><div class="comment-text"><p>I don't dare to call it an Answer (yet), but in order to check whether it is a sign issue, please try to split <code>tcp[4:4] &gt; 0xFFFFEC77</code> into <code>tcp[4:2] = 0xFFFF and tcp[6:2] &gt; 0x7fff</code> (you should get slightly more packets than with your original value of 0xec77 but you'll be sure whether the highest bit is evaluated as sign bit or not).</p></div><div id="comment-47667-info" class="comment-info"><span class="comment-age">(17 Nov '15, 08:09)</span> sindy</div></div><span id="47669"></span><div id="comment-47669" class="comment"><div id="post-47669-score" class="comment-score"></div><div class="comment-text"><p>Smart idea. I tried it and it still captures undesired packets. I should have also noted that the high end constraint, (tcp[4:4] &gt; 0xFFFFEC77), seems to work fine by itself. It's only when I try to "or" the low and high end constraints together that everything gets through the filter.</p></div><div id="comment-47669-info" class="comment-info"><span class="comment-age">(17 Nov '15, 08:25)</span> eeabe</div></div><span id="47670"></span><div id="comment-47670" class="comment"><div id="post-47670-score" class="comment-score"></div><div class="comment-text"><p>I also just tried: ((ip[15] &gt;= 52 and ip[15] &lt;= 55) or (ip[19] &gt;= 52 and ip[19] &lt;= 55)) and ((tcp[4:4] &lt; 0x00001388) or (tcp[4:2] == 0xFFFF))</p><p>Just adding the or (tcp[4:2] == 0xFFFF) term causes all the packets to be let through. Again, the compilation seems logical but doesn't seem to work.</p></div><div id="comment-47670-info" class="comment-info"><span class="comment-age">(17 Nov '15, 08:34)</span> eeabe</div></div></div><div id="comment-tools-47666" class="comment-tools"></div><div class="clear"></div><div id="comment-47666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47673"></span>

<div id="answer-container-47673" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47673-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to get it working by switching to 16 bit comparisons, and using &lt; and &gt;:</p><p>((ip[15] &gt;= 52 and ip[15] &lt;= 55) or (ip[19] &gt;= 52 and ip[19] &lt;= 55)) and ((tcp[4:2] &lt; 0x0001) or (tcp[4:2] &gt; 0xFFFE) or (tcp[8:2] &lt; 0x0001) or (tcp[8:2] &gt; 0xFFFE))</p><p>Maybe there is a bug with 32 bit comparisons, or with the &gt;= or &lt;=. I'm up and running for now. Thank you for the great hint sindy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/9386555acbf992085f85ada045a6bbec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eeabe&#39;s gravatar image" /><p>eeabe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eeabe has no accepted answers">0%</span></p></div></div><div id="comments-container-47673" class="comments-container"></div><div id="comment-tools-47673" class="comment-tools"></div><div class="clear"></div><div id="comment-47673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

