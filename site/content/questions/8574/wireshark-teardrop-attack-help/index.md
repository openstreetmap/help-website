+++
type = "question"
title = "Wireshark teardrop attack help"
description = '''How would I determine what packet is causing the direct attack of a teardrop attack. I&#x27;m using the Wireshark capture from Wireshark wiki: teardrop.cap How would I analyze this capture to determine the source IP address of the attack and the destination&#x27;s IP address?'''
date = "2012-01-23T21:00:00Z"
lastmod = "2012-01-24T04:37:00Z"
weight = 8574
keywords = [ "capture", "teardrop", "wireshark", "address" ]
aliases = [ "/questions/8574" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark teardrop attack help](/questions/8574/wireshark-teardrop-attack-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8574-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How would I determine what packet is causing the direct attack of a teardrop attack. I'm using the Wireshark capture from Wireshark wiki: <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=teardrop.cap">teardrop.cap</a></p><p>How would I analyze this capture to determine the source IP address of the attack and the destination's IP address?</p></div><div id="question-tags" class="tags-container tags">capture teardrop wireshark address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '12, 21:00</strong></p><img src="https://secure.gravatar.com/avatar/71ab82b5bab06e115acc6e046f2d97d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssams5&#39;s gravatar image" /><p>ssams5<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssams5 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jan '12, 02:24</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-8574" class="comments-container"></div><div id="comment-tools-8574" class="comment-tools"></div><div class="clear"></div><div id="comment-8574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8579"></span>

<div id="answer-container-8579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8579-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you load the referenced capture and take a look at frame 8 and 9 you'll see that frame 8 contains an IP fragment with a payload of 36 bytes long. The next fragment would, logically, be starting at offset 36. But if you look at frame 9 it says that this IP fragment starts at offset 24. This overlap is the essence of the teardrop attack.</p><p>So the question 'what packet' is causing the attack is inaccurate. It's the use of the fragmentation feature in the IP header that allows for this. In this case the combination of the IP fragment in frame 8 (the setup) and in frame 9 (the hit) are the attack.</p><p>If you are looking at the source and destination address, look at the IP header of these fragments, although the source address might be spoofed as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '12, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8579" class="comments-container"><span id="8590"></span><div id="comment-8590" class="comment"><div id="post-8590-score" class="comment-score"></div><div class="comment-text"><p>thanks for getting back to my question so quick. When I was analyzing the capture, I assumed the first 5 (loop) packets were the attack, so I guess I was wrong in this sense.</p><p>Looking for the source and destination, would I not look at the last couple of packets (the ping packets)?</p></div><div id="comment-8590-info" class="comment-info"><span class="comment-age">(24 Jan '12, 14:38)</span> ssams5</div></div><span id="8601"></span><div id="comment-8601" class="comment"><div id="post-8601-score" class="comment-score"></div><div class="comment-text"><p>Why would they be related? It could be. It could be the attacker checking for success, but there is no way to tell for sure.</p></div><div id="comment-8601-info" class="comment-info"><span class="comment-age">(25 Jan '12, 02:24)</span> Jaap ♦</div></div></div><div id="comment-tools-8579" class="comment-tools"></div><div class="clear"></div><div id="comment-8579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

