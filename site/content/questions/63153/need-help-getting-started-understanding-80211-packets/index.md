+++
type = "question"
title = "Need help getting started understanding 802.11 packets"
description = '''All, I am trying to debug a custom device and I followed the very helpful instructions here http://www.algissalys.com/network-security/passive-packet-sniffing-on-wifi-connections to get going. I now have several capture files, but am struggling to figure out what they mean.  What I have figured out ...'''
date = "2017-07-26T16:43:00Z"
lastmod = "2017-07-27T02:41:00Z"
weight = 63153
keywords = [ "802.11", "packets" ]
aliases = [ "/questions/63153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need help getting started understanding 802.11 packets](/questions/63153/need-help-getting-started-understanding-80211-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63153-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All,</p><p>I am trying to debug a custom device and I followed the very helpful instructions here <a href="http://www.algissalys.com/network-security/passive-packet-sniffing-on-wifi-connections">http://www.algissalys.com/network-security/passive-packet-sniffing-on-wifi-connections</a> to get going. I now have several capture files, but am struggling to figure out what they mean.</p><p>What I have figured out is that the data from my device to the cloud is probably encapsulated in QoS Data packets but I am having a hard time figuring out all of the intricacies of how these packets (and groups of packets) are to be interpreted.</p><p>Can you please point me to a good primer that will help me learn how to interpret these packets?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">802.11 packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '17, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/efb7a1f078cc0924d400ddc530222272?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="groston&#39;s gravatar image" /><p>groston<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="groston has no accepted answers">0%</span></p></div></div><div id="comments-container-63153" class="comments-container"></div><div id="comment-tools-63153" class="comment-tools"></div><div class="clear"></div><div id="comment-63153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63165"></span>

<div id="answer-container-63165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63165-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd start here: <a href="http://shop.oreilly.com/product/9780596100520.do">http://shop.oreilly.com/product/9780596100520.do</a></p><p>This is Gast's 802.11 book and it is pretty good. It will describe in some detail 802.11 and the protocols in use. For Wireshark analysis, you could probably skip some of the real low level stuff about modulation as you are looking at 802.11 frames and how they interact.</p><p>Of course, the 802.11 specification is useful as well but I find it a tough read. It's available for free from IEEE. It can be found here: <a href="https://standards.ieee.org/about/get/802/802.11.html">https://standards.ieee.org/about/get/802/802.11.html</a> You probably want to have it at least for a reference.</p><p>Analysis comes up here on this site, but it is usually very detailed when someone posts a trace or something so certainly search here for 802.11 questions and answers, but it is not a tutorial.</p><p>I am not sure if some of the Wireshark training that is available publicly (<a href="https://www.chappellu.com/online.html">Laura Chappell</a> et al) includes 802.11 or not, but it is worth asking. Maybe they can make a class for you or something.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '17, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-63165" class="comments-container"><span id="63177"></span><div id="comment-63177" class="comment"><div id="post-63177-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/112/bob-jones">@Bob Jones</a> = I have that same book! It is a great book for WiFi! Not so great on the latest technologies (like 11ac), but as you indicated, that is what the specs are for. :)</p></div><div id="comment-63177-info" class="comment-info"><span class="comment-age">(27 Jul '17, 06:49)</span> Amato_C</div></div><span id="63180"></span><div id="comment-63180" class="comment"><div id="post-63180-score" class="comment-score"></div><div class="comment-text"><p>There's a <a href="http://shop.oreilly.com/product/0636920052760.do">3rd edition</a> due out in March next year, and the same author has an <a href="http://shop.oreilly.com/product/0636920027768.do">802.11ac book</a> as well (I don't have any of the books :-( but might have to buy one soon).</p></div><div id="comment-63180-info" class="comment-info"><span class="comment-age">(27 Jul '17, 07:02)</span> grahamb ♦</div></div></div><div id="comment-tools-63165" class="comment-tools"></div><div class="clear"></div><div id="comment-63165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

