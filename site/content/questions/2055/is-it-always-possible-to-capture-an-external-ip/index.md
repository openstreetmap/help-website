+++
type = "question"
title = "Is it always possible to capture an external IP?"
description = '''Hello everybody! My question is: How do I capture an external IP of a machine I have a transmission with? Or is it not always possible (depending on the structure of internal network). All I was able to find were internal IPs of my machine and another. They&#x27;re useless. The only thing I need is an ex...'''
date = "2011-01-31T17:30:00Z"
lastmod = "2011-02-01T18:27:00Z"
weight = 2055
keywords = [ "ip", "external" ]
aliases = [ "/questions/2055" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it always possible to capture an external IP?](/questions/2055/is-it-always-possible-to-capture-an-external-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2055-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody! My question is: How do I capture an external IP of a machine I have a transmission with? Or is it not always possible (depending on the structure of internal network). All I was able to find were internal IPs of my machine and another. They're useless. The only thing I need is an external IP. May be I need to adjust capture options?</p><p>P.S. Sorry if my question sounds stupid - I'm just a beginner...</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">ip external</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '11, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/3f50ccf3ddf0e1631e0e49e9eef02cdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_KLblK&#39;s gravatar image" /><p>_KLblK<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_KLblK has no accepted answers">0%</span></p></div></div><div id="comments-container-2055" class="comments-container"></div><div id="comment-tools-2055" class="comment-tools"></div><div class="clear"></div><div id="comment-2055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2057"></span>

<div id="answer-container-2057" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2057-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a detail that Network Address Translation (NAT) is designed to hide from you. Therefore it won't show up on your computers network interface and in captures.</p><p>There are some other options to get it, STUN, maybe even uPNP, but neither have to do with packet capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 22:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2057" class="comments-container"><span id="2081"></span><div id="comment-2081" class="comment"><div id="post-2081-score" class="comment-score"></div><div class="comment-text"><p>thank you so much for your help. I really appreciate it :)</p></div><div id="comment-2081-info" class="comment-info"><span class="comment-age">(01 Feb '11, 11:35)</span> _KLblK</div></div></div><div id="comment-tools-2057" class="comment-tools"></div><div class="clear"></div><div id="comment-2057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2089"></span>

<div id="answer-container-2089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2089-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will need to capture in front of the NAT device. You could capture on the device with one Wireshark instance, then plug another pc with Wireshark in front of the NAT process. Then you can use the protocol, destination IP address, port and IP Identification field to correllate the two. You can't tell the public address from behind the NAT device because Wireshark just looks at the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '11, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-2089" class="comments-container"></div><div id="comment-tools-2089" class="comment-tools"></div><div class="clear"></div><div id="comment-2089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

