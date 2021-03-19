+++
type = "question"
title = "Doesn&#x27;t seem to be able to capture the packets"
description = '''Hi, I&#x27;ve been trying to capture Telegram messaging application&#x27;s packets (for my class project) but I couldn&#x27;t get anything out of the punch of captured packets I got. Telegram does AES-256 encryption over the users&#x27; messages and then send it using normal-Not SSL-transportation protocols (e.g. TCP,H...'''
date = "2014-12-20T07:41:00Z"
lastmod = "2014-12-27T08:53:00Z"
weight = 38641
keywords = [ "filter", "capture", "promiscuous", "wlan", "tcp" ]
aliases = [ "/questions/38641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Doesn't seem to be able to capture the packets](/questions/38641/doesnt-seem-to-be-able-to-capture-the-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've been trying to capture Telegram messaging application's packets (for my class project) but I couldn't get anything out of the punch of captured packets I got.</p><p><a href="http://core.telegram.org/mtproto">Telegram</a> does AES-256 encryption over the users' messages and then send it using normal-Not SSL-transportation protocols (e.g. TCP,HTTP,UDP, etc..)</p><p>I tried these capturing scenario:</p><ul><li>Connecting both mobile phones (sender &amp; receiver) to the same access point that my Laptop-where wireshark is running-connected to.</li><li>making my laptop as an access point where the two phones are connected to (that's to make sure the packets go through the NIC card in case the router is not allowing packet to be broadcasted)</li></ul><p>So in my capture filter I tried many filters I assume the most relevant are :</p><ul><li>HTTP only: I got many packets, which is useless to check every single one of the 269386 packets captured. that is in the case of scenario one of the capturing trials. So I modified the filter and come up with the second filter.</li><li>HTTP with my mobile phone IP address (i.e http &amp;&amp; ip.addr) but I got no packets at all. though my phone is the sender (in both capturing scenarios).</li></ul><p>Any ideas what's wrong or what I'm missing here</p><p>P.S wireshark is set in promiscuous mode<br />
</p></div><div id="question-tags" class="tags-container tags">filter capture promiscuous wlan tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '14, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/725aa92cfc7bf87e921e124f6bae69be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="captin&#39;s gravatar image" /><p>captin<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="captin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-38641" class="comments-container"></div><div id="comment-tools-38641" class="comment-tools"></div><div class="clear"></div><div id="comment-38641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38737"></span>

<div id="answer-container-38737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38737-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any ideas what's wrong or what I'm missing here</p></blockquote><p><a href="https://core.telegram.org/mtproto">MTProto</a> supports TCP/UDP and HTTP. If you did not ensure that the client was using HTTP, you won't see anything with the filter <strong>http</strong> !!</p><p>You should better filter for the client IP address and the destionation port, based on the client protocol.</p><blockquote><p>ip.addr eq x.x.x.x and tcp.port eq yyyy</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38737" class="comments-container"></div><div id="comment-tools-38737" class="comment-tools"></div><div class="clear"></div><div id="comment-38737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

