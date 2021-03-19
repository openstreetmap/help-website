+++
type = "question"
title = "Malformed Packet for ICMPv6 Redirect Message"
description = '''Hi! I always get a &quot;Malformed Packet&quot; for ICMP Redirect Message. Does anyone have an idea why or what the problem is? Screenshot: http://postimg.org/image/6a27pizr1/ BR DarkEye'''
date = "2013-04-01T05:55:00Z"
lastmod = "2013-04-01T11:22:00Z"
weight = 19988
keywords = [ "redirect", "icmpv6", "icmp", "ipv6" ]
aliases = [ "/questions/19988" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Malformed Packet for ICMPv6 Redirect Message](/questions/19988/malformed-packet-for-icmpv6-redirect-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I always get a "Malformed Packet" for ICMP Redirect Message. Does anyone have an idea why or what the problem is?</p><p>Screenshot: <a href="http://postimg.org/image/6a27pizr1/">http://postimg.org/image/6a27pizr1/</a></p><p>BR DarkEye</p></div><div id="question-tags" class="tags-container tags">redirect icmpv6 icmp ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '13, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/a392786bd1d998d453645e0d55c8aeae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheDarkEye&#39;s gravatar image" /><p>TheDarkEye<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheDarkEye has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '13, 06:01</p></div></div><div id="comments-container-19988" class="comments-container"></div><div id="comment-tools-19988" class="comment-tools"></div><div class="clear"></div><div id="comment-19988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19992"></span>

<div id="answer-container-19992" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's not the Redirect that gives you the error, it's the Echo inside the redirected header ICMP field that gets the dissector spooked when it's cut short. Not an error in this case.</p><p>You could file this nicely documented error on <a href="https://bugs.wireshark.org">bugs.wireshark.org</a> (don't forget to attach this sample capture) for it to be fixed in an upcoming release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '13, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19992" class="comments-container"><span id="19993"></span><div id="comment-19993" class="comment"><div id="post-19993-score" class="comment-score"></div><div class="comment-text"><p>Thx a lot.</p><p>I also have issues that the redirect has no effect on the receiving host, so I thought this "malformed packet" is the reason. Now I have to look somewhere else ... :-)</p><p>Thank you very much.</p></div><div id="comment-19993-info" class="comment-info"><span class="comment-age">(01 Apr '13, 12:56)</span> TheDarkEye</div></div></div><div id="comment-tools-19992" class="comment-tools"></div><div class="clear"></div><div id="comment-19992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

