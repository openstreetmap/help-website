+++
type = "question"
title = "60 Who has 192.168.1.2? Tell 192.168.X.XX Any idea what this means?"
description = '''Hi, First post here, when I try to use wireshark 1.12.3, it keeps showing this message, though I can use internet without any issue, just curious about what this actually means? And after restarting my system, it will show 60 192.168.X.X is as XX:XX:XX:XX:XX, I guess this is more like normal, right?...'''
date = "2015-03-05T01:38:00Z"
lastmod = "2015-03-05T01:48:00Z"
weight = 40267
keywords = [ "message" ]
aliases = [ "/questions/40267" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [60 Who has 192.168.1.2? Tell 192.168.X.XX Any idea what this means?](/questions/40267/60-who-has-19216812-tell-192168xxx-any-idea-what-this-means)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40267-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>First post here, when I try to use wireshark 1.12.3, it keeps showing this message, though I can use internet without any issue, just curious about what this actually means? And after restarting my system, it will show 60 192.168.X.X is as XX:XX:XX:XX:XX, I guess this is more like normal, right? Is there anything wrong? Any help would be appreciated.</p><p>BR, Kai</p></div><div id="question-tags" class="tags-container tags">message</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/ed43b7356b2d83058e78a31ee9883fb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kai&#39;s gravatar image" /><p>Kai<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kai has no accepted answers">0%</span></p></div></div><div id="comments-container-40267" class="comments-container"></div><div id="comment-tools-40267" class="comment-tools"></div><div class="clear"></div><div id="comment-40267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40270"></span>

<div id="answer-container-40270" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40270-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is an <a href="http://en.wikipedia.org/wiki/Address_Resolution_Protocol">ARP</a> conversation, and is perfectly normal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40270" class="comments-container"><span id="40273"></span><div id="comment-40273" class="comment"><div id="post-40273-score" class="comment-score"></div><div class="comment-text"><p>Thanks for quick reply.</p><p>What message I keep having is "60 Who has 192.168.1.2? Tell 192.168.X.XX", I won't get "60 192.168.X.X is as XX:XX:XX:XX:XX" until I restart my system, otherwise it just keeps coming out "60 Who has 192.168.1.2? Tell 192.168.X.XX"...Is it also normal that they need to keep communicating with "60 Who has 192.168.1.2? Tell 192.168.X.XX"? Again, thank you very much.</p></div><div id="comment-40273-info" class="comment-info"><span class="comment-age">(05 Mar '15, 02:27)</span> Kai</div></div><span id="40278"></span><div id="comment-40278" class="comment"><div id="post-40278-score" class="comment-score"></div><div class="comment-text"><p>Standard ARP behaviour, the machine at 192.68.x.x is asking if anyone has IP 192.168.1.2 as either:</p><p>a. It wants to send a message to that IP and needs to know the MAC address. b. It's using <a href="http://wiki.wireshark.org/Gratuitous_ARP">gratuitous ARP</a> for various other reasons.</p></div><div id="comment-40278-info" class="comment-info"><span class="comment-age">(05 Mar '15, 04:18)</span> grahamb ♦</div></div><span id="40291"></span><div id="comment-40291" class="comment"><div id="post-40291-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-40291-info" class="comment-info"><span class="comment-age">(05 Mar '15, 08:17)</span> Jaap ♦</div></div></div><div id="comment-tools-40270" class="comment-tools"></div><div class="clear"></div><div id="comment-40270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

