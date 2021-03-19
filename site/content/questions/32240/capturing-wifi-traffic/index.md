+++
type = "question"
title = "capturing wifi traffic"
description = '''Hello i captured wifi traffic with that tutorial: http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version. But now when i try to use filter http.request, I get &quot;loading&quot; window, and when it&#x27;s done, I don&#x27;t see any traffic. What have i done w...'''
date = "2014-04-28T03:11:00Z"
lastmod = "2014-04-28T08:11:00Z"
weight = 32240
keywords = [ "http.request", "wifi" ]
aliases = [ "/questions/32240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capturing wifi traffic](/questions/32240/capturing-wifi-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>i captured wifi traffic with that tutorial: <a href="http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version">http://ask.wireshark.org/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version.</a></p><p>But now when i try to use filter <strong>http.request</strong>, I get "loading" window, and when it's done, I don't see any traffic. What have i done wrong. I tried to see what sites are users in our network visiting, and also i figured out that wireshark is not so good for sniffing for a long time, but now its to late :) . I have a question, how to see what sites were visited</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">http.request wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/02bfcf9ef119a526e187ef0550113711?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beginer&#39;s gravatar image" /><p>Beginer<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beginer has no accepted answers">0%</span></p></div></div><div id="comments-container-32240" class="comments-container"></div><div id="comment-tools-32240" class="comment-tools"></div><div class="clear"></div><div id="comment-32240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32255"></span>

<div id="answer-container-32255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32255-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I don't see any traffic. What have i done wrong.</p></blockquote><p>The traffic is most certainly encrypted. Please search for EAPOL frames to verify my assumption. Display filter: <strong>eapol</strong>.</p><p>If that is the case, please read the Wifi Decryption Wiki.</p><blockquote><p><a href="http://wiki.wireshark.org/HowToDecrypt802.11">http://wiki.wireshark.org/HowToDecrypt802.11</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32255" class="comments-container"></div><div id="comment-tools-32255" class="comment-tools"></div><div class="clear"></div><div id="comment-32255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

