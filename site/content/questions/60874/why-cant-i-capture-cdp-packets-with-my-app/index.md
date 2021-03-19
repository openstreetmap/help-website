+++
type = "question"
title = "Why can&#x27;t I capture CDP Packets with my app?"
description = '''So I&#x27;m having a strange issue trying to capture CDP packets. I wrote my own light weight application utilizing the wpcap.dll and built a filter and a parser everything was working fine until I started testing with other computers. It was then I figured out that my application will NOT capture CDP pa...'''
date = "2017-04-18T06:29:00Z"
lastmod = "2017-04-18T06:43:00Z"
weight = 60874
keywords = [ "winpcap", "vbscript", "wireshark" ]
aliases = [ "/questions/60874" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why can't I capture CDP Packets with my app?](/questions/60874/why-cant-i-capture-cdp-packets-with-my-app)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60874-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I'm having a strange issue trying to capture CDP packets. I wrote my own light weight application utilizing the wpcap.dll and built a filter and a parser everything was working fine until I started testing with other computers. It was then I figured out that my application will NOT capture CDP packets if wire shark is not running.</p><p>It is capturing an parsing packets fine I can see them scrolling by but I never get a CDP hit. My switches are set to advertise every 60 seconds but I can leave my program open for 10 mins and then open wireshark and get a CDP packet. If I close Wireshark I no longer see the CDP packets.</p><p>I'm using the filter 'ether[20:2] == 0x2000' looking for type '0x01E3'</p></div><div id="question-tags" class="tags-container tags">winpcap vbscript wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '17, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/acd062a2d7758deff611f41a289625b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlman12&#39;s gravatar image" /><p>tlman12<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlman12 has no accepted answers">0%</span></p></div></div><div id="comments-container-60874" class="comments-container"></div><div id="comment-tools-60874" class="comment-tools"></div><div class="clear"></div><div id="comment-60874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60875"></span>

<div id="answer-container-60875" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60875-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Destination MAC address of a CDP packet is a multicast address. Therefore to be able to get such a packet to the application layer your network card has to accept it.</p><p>This can be achieved by setting the network card to promiscuous mode (which does Wireshark resp. the WINpcap driver). Or another way is to join this multicast address at the OS level.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '17, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Apr '17, 06:49</p></div></div><div id="comments-container-60875" class="comments-container"><span id="60877"></span><div id="comment-60877" class="comment"><div id="post-60877-score" class="comment-score"></div><div class="comment-text"><p>-Facepalm- I've been messing with this for hours wondering why I could only capture with wireshark running.</p><p>Set my program to put the card in promiscuous mode and bam packet captured. Thank you!</p></div><div id="comment-60877-info" class="comment-info"><span class="comment-age">(18 Apr '17, 07:18)</span> tlman12</div></div><span id="60878"></span><div id="comment-60878" class="comment"><div id="post-60878-score" class="comment-score">1</div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-60878-info" class="comment-info"><span class="comment-age">(18 Apr '17, 07:49)</span> grahamb ♦</div></div></div><div id="comment-tools-60875" class="comment-tools"></div><div class="clear"></div><div id="comment-60875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

