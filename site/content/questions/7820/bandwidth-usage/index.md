+++
type = "question"
title = "Bandwidth usage"
description = '''Hi there, I´m pretty new to Wireshark. So maybe you can answer me a question about sniffing my LAN. Is there a possibility to see which IP address is using a high level of bandwidth? The best thing would be a new column in the capture pane, like MBit/s. I didn´t find anything in the wiki, so maybe y...'''
date = "2011-12-07T07:23:00Z"
lastmod = "2011-12-07T07:30:00Z"
weight = 7820
keywords = [ "capturing" ]
aliases = [ "/questions/7820" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Bandwidth usage](/questions/7820/bandwidth-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7820-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I´m pretty new to Wireshark. So maybe you can answer me a question about sniffing my LAN.</p><p>Is there a possibility to see which IP address is using a high level of bandwidth? The best thing would be a new column in the capture pane, like MBit/s. I didn´t find anything in the wiki, so maybe you know even if it´s possible.</p><p>I was thinking of something like this:</p><p>No. Time Source Destination [Usage in MBit/s] Information ^ | This would be my new column.</p><p>I´m not a native english speaker, so my English is poor. Hopefully you understand what I´m trying ti do.</p><p>Kind regards Martin</p></div><div id="question-tags" class="tags-container tags">capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '11, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/1abac6d3cfb3dbc3096ed6b420ca256f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin&#39;s gravatar image" /><p>Martin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin has no accepted answers">0%</span></p></div></div><div id="comments-container-7820" class="comments-container"></div><div id="comment-tools-7820" class="comment-tools"></div><div class="clear"></div><div id="comment-7820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7821"></span>

<div id="answer-container-7821" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7821-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go for statistics -&gt; conversations and there you check the tab labeled "IPv4". The two rightmost coloumns give you bits per second in each direction between those IP addresses. If you want to have them sorted, simply click on the coloumn's label.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-7821" class="comments-container"><span id="7823"></span><div id="comment-7823" class="comment"><div id="post-7823-score" class="comment-score"></div><div class="comment-text"><p>Hi Landi,</p><p>thanks for your quick reply.</p><p>Is there any way I can personalize the capture pane the way I wanted to do?</p><p>I found this option on my own, but it´s not exactly what I was looking for.</p><p>Kind regards Martin</p></div><div id="comment-7823-info" class="comment-info"><span class="comment-age">(07 Dec '11, 07:43)</span> Martin</div></div><span id="7845"></span><div id="comment-7845" class="comment"><div id="post-7845-score" class="comment-score">1</div><div class="comment-text"><p>Sorry, but wireshark treats the packets independently in the packet list -&gt; what you would need is a custom column that supports math operations like ((cumulative bytes / relative time) * 8 / 10^6)</p><p>So either you export your trace to e.g. excel and do it there or like already suggested you go for statistics, which IMO is perfectly fine for your needs because of the ability to directly sort for the top talkers</p></div><div id="comment-7845-info" class="comment-info"><span class="comment-age">(08 Dec '11, 03:31)</span> Landi</div></div><span id="7864"></span><div id="comment-7864" class="comment"><div id="post-7864-score" class="comment-score"></div><div class="comment-text"><p>Thanks Landi for your support.</p><p>I´m going to use statistics to find the top talkers.</p><p>Topic may be closed.</p><p>Kind regards Martin</p></div><div id="comment-7864-info" class="comment-info"><span class="comment-age">(09 Dec '11, 00:12)</span> Martin</div></div><span id="7866"></span><div id="comment-7866" class="comment"><div id="post-7866-score" class="comment-score"></div><div class="comment-text"><p>Martin, I converted your answer to a comment, as that's the way this site works best, please see the FAQ. Regarding "closing" this topic, you can do that by "accepting" the answer that answered your question best (duh, there is only one answer this time) by clicking on the checkmark (little 'v') next to it.</p></div><div id="comment-7866-info" class="comment-info"><span class="comment-age">(09 Dec '11, 00:35)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-7821" class="comment-tools"></div><div class="clear"></div><div id="comment-7821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

