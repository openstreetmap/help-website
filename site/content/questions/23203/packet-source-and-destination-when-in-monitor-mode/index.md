+++
type = "question"
title = "Packet Source and Destination when in Monitor Mode"
description = '''Hi, probably a n00b question, but I can&#x27;t find an answer to it. I have my Wireshark instaled on Ubuntu within VmWare Workstation. I activated the monitor mode on mon0 with airmon-ng. When I&#x27;m listening on that interface (mon0) all I can see is 802.11 protocol and Source/Destination addresses are not...'''
date = "2013-07-21T02:25:00Z"
lastmod = "2013-07-21T12:43:00Z"
weight = 23203
keywords = [ "monitor", "monitor-mode" ]
aliases = [ "/questions/23203" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Source and Destination when in Monitor Mode](/questions/23203/packet-source-and-destination-when-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23203-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, probably a n00b question, but I can't find an answer to it.</p><p>I have my Wireshark instaled on Ubuntu within VmWare Workstation. I activated the monitor mode on mon0 with airmon-ng. When I'm listening on that interface (mon0) all I can see is 802.11 protocol and Source/Destination addresses are not displayed as regular IP addresses so I can't figure out where does traffic originated from and where is it going (no IP information).</p><p>Is it possible to somehow get frames with their source and destination IP addresses?</p><p>Thanks for any help.</p></div><div id="question-tags" class="tags-container tags">monitor monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/8c1d2e18fd109856aeeb39970ea92e87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mate%20Strgacic&#39;s gravatar image" /><p>Mate Strgacic<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mate Strgacic has no accepted answers">0%</span></p></div></div><div id="comments-container-23203" class="comments-container"></div><div id="comment-tools-23203" class="comment-tools"></div><div class="clear"></div><div id="comment-23203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23214"></span>

<div id="answer-container-23214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23214-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On a protected network (one using WEP or WPA/WPA2), the packets are encrypted (the whole <em>point</em> of protected networks is to make it hard to sniff traffic on them!), and, when captured in monitor mode, what's captured is the encrypted data. You will have to <a href="http://wiki.wireshark.org/HowToDecrypt802.11">configure Wireshark to decrypt the traffic</a> and, for WPA/WPA2 networks, for each machine whose traffic you want to decrypt, you will need to capture the initial handshake done when the machine joins the network (so you might have to turn your own, and other machines', Wi-FI interfaces off and on again, or put them to sleep and wake them up again, to force them to re-join the network).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '13, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23214" class="comments-container"><span id="23233"></span><div id="comment-23233" class="comment"><div id="post-23233-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. That's exactly the info I was looking for.</p></div><div id="comment-23233-info" class="comment-info"><span class="comment-age">(22 Jul '13, 07:58)</span> Mate Strgacic</div></div><span id="23234"></span><div id="comment-23234" class="comment"><div id="post-23234-score" class="comment-score"></div><div class="comment-text"><p>@ Mate Strgacic Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>Also, if an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. The FAQ also has more information on this.</p></div><div id="comment-23234-info" class="comment-info"><span class="comment-age">(22 Jul '13, 08:08)</span> grahamb ♦</div></div></div><div id="comment-tools-23214" class="comment-tools"></div><div class="clear"></div><div id="comment-23214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

