+++
type = "question"
title = "Dropping packet detection"
description = '''We are hosting equipment in our data center and finding packet loss between customers and our servers. Can wireshark identify where those packets are dropped? Connection involves customer network, internet, our data center network. If it can, what help is available to determine wireshark setup and a...'''
date = "2015-04-08T05:49:00Z"
lastmod = "2015-04-08T06:25:00Z"
weight = 41278
keywords = [ "packetloss" ]
aliases = [ "/questions/41278" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dropping packet detection](/questions/41278/dropping-packet-detection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41278-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are hosting equipment in our data center and finding packet loss between customers and our servers. Can wireshark identify where those packets are dropped? Connection involves customer network, internet, our data center network. If it can, what help is available to determine wireshark setup and analysis?</p></div><div id="question-tags" class="tags-container tags">packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '15, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/7db23ba4791b8e18e46f27ae58a51d4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hholinger&#39;s gravatar image" /><p>hholinger<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hholinger has no accepted answers">0%</span></p></div></div><div id="comments-container-41278" class="comments-container"></div><div id="comment-tools-41278" class="comment-tools"></div><div class="clear"></div><div id="comment-41278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41282"></span>

<div id="answer-container-41282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41282-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That would involve setting up mirror ports at applicable interfaces, make traces at the same time and then start comparing these traces. I guess it could be problematic to get at the mirror ports, and maybe even handle the amount of data going through. If you can define controlled test scenarios, you may be able to create capture filters to limit the amount of data you collect, to ease the analysis. So, it very much depends on the specifics of your situation.</p><p>Furthermore, depending on the size of the system / problem, you could think about investing in CFM (ETH-LM).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '15, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41282" class="comments-container"></div><div id="comment-tools-41282" class="comment-tools"></div><div class="clear"></div><div id="comment-41282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

