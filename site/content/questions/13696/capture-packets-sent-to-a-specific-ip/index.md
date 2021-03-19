+++
type = "question"
title = "Capture packets sent to a specific IP"
description = '''I am playing around with the wireshark for a while now, but I&#x27;m still not sure if this is possible. Is it possible to capture packets sent to a specific IP, not from my computer? Obviously outside of a local network, let&#x27;s say www.google.com as a brutal example.'''
date = "2012-08-16T21:09:00Z"
lastmod = "2012-08-16T22:40:00Z"
weight = 13696
keywords = [ "wireshark" ]
aliases = [ "/questions/13696" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture packets sent to a specific IP](/questions/13696/capture-packets-sent-to-a-specific-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am playing around with the wireshark for a while now, but I'm still not sure if this is possible.</p><p>Is it possible to capture packets sent to a specific IP, not from my computer? Obviously outside of a local network, let's say <a href="http://www.google.com">www.google.com</a> as a brutal example.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '12, 21:09</strong></p><img src="https://secure.gravatar.com/avatar/fe66fa20bcc8f8f408938b8b4eb91753?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trfvbg&#39;s gravatar image" /><p>Trfvbg<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trfvbg has no accepted answers">0%</span></p></div></div><div id="comments-container-13696" class="comments-container"></div><div id="comment-tools-13696" class="comment-tools"></div><div class="clear"></div><div id="comment-13696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13697"></span>

<div id="answer-container-13697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13697-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can only capture traffic that is visible on the interface on which it captures. So the answer is yes, but only if you are capturing within the google datacenter on a spot in the network where you know all traffic for <a href="http://www.google.com">www.google.com</a> is passing. You can then set up capture filtering to only capture the traffic in which you are interested.</p><p>Have a look at the following wiki pages:</p><ul><li><a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></li><li><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></li><li><a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '12, 22:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13697" class="comments-container"></div><div id="comment-tools-13697" class="comment-tools"></div><div class="clear"></div><div id="comment-13697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

