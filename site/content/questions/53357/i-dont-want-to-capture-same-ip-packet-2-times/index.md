+++
type = "question"
title = "i don&#x27;t want to capture same IP packet 2 times"
description = '''I only want to capture the same ip adress packet one time but I want to always capture from the same ip how could i do this?'''
date = "2016-06-11T11:04:00Z"
lastmod = "2016-06-12T15:18:00Z"
weight = 53357
keywords = [ "packets", "capturing" ]
aliases = [ "/questions/53357" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [i don't want to capture same IP packet 2 times](/questions/53357/i-dont-want-to-capture-same-ip-packet-2-times)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53357-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I only want to capture the same ip adress packet one time but I want to always capture from the same ip</p><p>how could i do this?</p></div><div id="question-tags" class="tags-container tags">packets capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '16, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/6811fa4887f7b5041c2eb107f46b3228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allou&#39;s gravatar image" /><p>allou<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allou has no accepted answers">0%</span></p></div></div><div id="comments-container-53357" class="comments-container"><span id="53369"></span><div id="comment-53369" class="comment"><div id="post-53369-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>how could i do this?</p></blockquote></blockquote><p>I don't know. I don't understand your question at all. Can you try to rephrase? If English is not your native language, maybe post both: English and your native language and we can use google translate. Maybe that would be clearer?</p></div><div id="comment-53369-info" class="comment-info"><span class="comment-age">(12 Jun '16, 05:52)</span> Bob Jones</div></div><span id="53372"></span><div id="comment-53372" class="comment"><div id="post-53372-score" class="comment-score"></div><div class="comment-text"><p>Or you may want to give an example (a sample capture or a list of source and destination IP address pairs) of what you capture and which of the captured packets you would like to exclude.</p></div><div id="comment-53372-info" class="comment-info"><span class="comment-age">(12 Jun '16, 06:32)</span> sindy</div></div><span id="53379"></span><div id="comment-53379" class="comment"><div id="post-53379-score" class="comment-score"></div><div class="comment-text"><p>Ok for example I have an ip where I capture the trafic from and it's 192.168.84.132</p><p>I want to capture everything on the trafic BUT i don't to get the same ip 2 times. Would it be possible to group every trafic going/coming from an ip?</p><p>J'aimerai seulement être capable de regrouper le trafic d'un ip pour que ce qui découle sur wireshark soit plus clair. Je vois trop de trafic et ce n'est pas assez claire j'ai de la difficulté à trier les adresses ip entrantes et sortantes... merci.</p></div><div id="comment-53379-info" class="comment-info"><span class="comment-age">(12 Jun '16, 12:40)</span> allou</div></div></div><div id="comment-tools-53357" class="comment-tools"></div><div class="clear"></div><div id="comment-53357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53383"></span>

<div id="answer-container-53383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53383-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps Wireshark is not the best tool for this. Another option that could work, more inline with what you are asking, could be</p><p><a href="http://www.ntop.org/products/traffic-analysis/ntop/">http://www.ntop.org/products/traffic-analysis/ntop/</a></p><p>This tracks flows of data between hosts, and might be more like what you need. Wireshark is like a surgeon's scalpel: very precise, but not the right tool every time. Other tools are better for aggregating and presenting data flows, but no tool is better at packet-level analysis (this is all a matter of opinion - others may have contrasting views).<br />
</p><p>Other technologies like this are sFlow and netflow. Here is a webpage with a bunch of Linux-based bandwidth tools that might present the data in a way you need:</p><p><a href="http://dynacont.net/documentation/linux/network_monitoring/">http://dynacont.net/documentation/linux/network_monitoring/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '16, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-53383" class="comments-container"></div><div id="comment-tools-53383" class="comment-tools"></div><div class="clear"></div><div id="comment-53383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53382"></span>

<div id="answer-container-53382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53382-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot stop capturing packets to/from an IP address after the first packet to/from that address has been captured (or, more generically, Wireshark cannot actively modify the capture filter during capture).</p><p>But you can use <code>Statistics -&gt; Conversations</code> to view aggregated data at different layers depending on which tab you choose. So if you choose <code>IPv4</code> or <code>IPv6</code> in particular, you'll get a list of all (IP address A, IP address B) pairs for which at least one packet (in either direction, A-&gt;B or B-&gt;A) is present in the capture, along with the number of packets and number of bytes in each direction. And you can use this view during a running capture, so you can see the conversation list grow in real time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '16, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53382" class="comments-container"></div><div id="comment-tools-53382" class="comment-tools"></div><div class="clear"></div><div id="comment-53382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

