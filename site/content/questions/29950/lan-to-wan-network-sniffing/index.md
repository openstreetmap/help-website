+++
type = "question"
title = "LAN TO WAN Network Sniffing"
description = '''So I&#x27;m fairly new to packet sniffing, I am tech savvy to an extent. What I am trying to do is monitor all network traffic between my router and the WAN. (specifically I&#x27;m trying to see if I can sniff iMessage Data off my iPhone when connected to my home wifi) can I use wireshark connect to the LAN o...'''
date = "2014-02-17T22:08:00Z"
lastmod = "2014-02-18T04:01:00Z"
weight = 29950
keywords = [ "wan", "lan", "imessage", "wireshark" ]
aliases = [ "/questions/29950" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LAN TO WAN Network Sniffing](/questions/29950/lan-to-wan-network-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29950-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I'm fairly new to packet sniffing, I am tech savvy to an extent.</p><p>What I am trying to do is monitor all network traffic between my router and the WAN.</p><p>(specifically I'm trying to see if I can sniff iMessage Data off my iPhone when connected to my home wifi)</p><p>can I use wireshark connect to the LAN or do I have to route LAN traffic through my computer running wire shark then to the WAN?</p><p>any insight and guidance is appreciated<br />
</p></div><div id="question-tags" class="tags-container tags">wan lan imessage wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '14, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/d658e8b5888211d1950270e9fc582ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dpopeofdope&#39;s gravatar image" /><p>dpopeofdope<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dpopeofdope has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29950" class="comments-container"><span id="29989"></span><div id="comment-29989" class="comment"><div id="post-29989-score" class="comment-score"></div><div class="comment-text"><p>What is on the WAN side of your router, ATM or ethernet? i.e., do you have a CAT5 running from your router's WAN port to a bridged modem which has an ATM (phone) connection?</p></div><div id="comment-29989-info" class="comment-info"><span class="comment-age">(18 Feb '14, 15:53)</span> randyp</div></div></div><div id="comment-tools-29950" class="comment-tools"></div><div class="clear"></div><div id="comment-29950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29963"></span>

<div id="answer-container-29963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29963-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It should capture those packets if you running the program on the same PC as Wireshark. If it is a different PC you will likely not see that traffic because of the way an Ethernet switch works. You may want to review <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '14, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-29963" class="comments-container"></div><div id="comment-tools-29963" class="comment-tools"></div><div class="clear"></div><div id="comment-29963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

