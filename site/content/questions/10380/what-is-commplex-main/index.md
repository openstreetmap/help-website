+++
type = "question"
title = "What is commplex-main"
description = '''I am learning computer networking. When I started using Wireshark to capture packets on my wireless card, I noticed the following entries: 39 15.453128 169.254.1.127 169.254.1.255 UDP Source port: 43292 Destination port: commplex-main 40 16.989062 169.254.1.107 169.254.1.255 UDP Source port: intecom...'''
date = "2012-04-21T18:33:00Z"
lastmod = "2012-04-21T20:42:00Z"
weight = 10380
keywords = [ "commplex-main" ]
aliases = [ "/questions/10380" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is commplex-main](/questions/10380/what-is-commplex-main)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10380-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am learning computer networking. When I started using Wireshark to capture packets on my wireless card, I noticed the following entries:</p><pre><code>39 15.453128 169.254.1.127 169.254.1.255 UDP Source port: 43292  Destination port: commplex-main
40 16.989062 169.254.1.107 169.254.1.255 UDP Source port: intecom-ps1  Destination port: commplex-main
41 20.070231 169.254.1.107  255.255.255.255 UDP Source port: 21302  Destination port: 21302</code></pre><p>What do the above entries resemble?</p></div><div id="question-tags" class="tags-container tags">commplex-main</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '12, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/05914f22e83d9089efa4d4a1e5035ce5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tech2010&#39;s gravatar image" /><p>Tech2010<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tech2010 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Apr '12, 23:34</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10380" class="comments-container"></div><div id="comment-tools-10380" class="comment-tools"></div><div class="clear"></div><div id="comment-10380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10381"></span>

<div id="answer-container-10381" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10381-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is port 5000. You have transport name resolution turned on, so Wireshark is displaying a service name instead of port number. For example "http" instead of "80", or in this case "commplex-main" instead of "5000". The port-number-to-service-name mappings are found in Wireshark's <em>services</em> file. I did some Googling, but was unable to find out exactly what commplex-main is. However, there are actually multiple services that commonly run over port 5000. "commplex-main" is the service name associated with port 5000 in the <em>services</em> file, but this traffic could be some other service; all this tells you is that it's running on port 5000. If this is a Windows computer, the traffic is more likely to be UPnP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '12, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-10381" class="comments-container"></div><div id="comment-tools-10381" class="comment-tools"></div><div class="clear"></div><div id="comment-10381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

