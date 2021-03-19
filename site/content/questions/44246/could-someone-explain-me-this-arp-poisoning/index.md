+++
type = "question"
title = "Could someone explain me this arp poisoning?"
description = '''Hey guys, I have this .pcap file (download: https://goo.gl/1zqoGN) and I am a little confused. The capture file shows an arp poisoning attack, but my question is: why is the ip address 192.168.0.2 sending all these arp requests (packets 45 to 298)? Could someone explain? Thanks in advance.'''
date = "2015-07-17T08:59:00Z"
lastmod = "2015-07-17T10:46:00Z"
weight = 44246
keywords = [ "arpspoofing" ]
aliases = [ "/questions/44246" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Could someone explain me this arp poisoning?](/questions/44246/could-someone-explain-me-this-arp-poisoning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44246-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I have this .pcap file (download: <a href="https://goo.gl/1zqoGN)">https://goo.gl/1zqoGN)</a> and I am a little confused. The capture file shows an arp poisoning attack, but my question is: why is the ip address 192.168.0.2 sending all these arp requests (packets 45 to 298)? Could someone explain? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">arpspoofing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '15, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/9ac6cd419014092f44d21ec71233b1e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shad0w125&#39;s gravatar image" /><p>shad0w125<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shad0w125 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '15, 09:03</p></div></div><div id="comments-container-44246" class="comments-container"></div><div id="comment-tools-44246" class="comment-tools"></div><div class="clear"></div><div id="comment-44246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44255"></span>

<div id="answer-container-44255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44255-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The capture file shows an arp poisoning attack,</p></blockquote><p>I don't think so. Looks more like a network sweep (IP scan via <a href="http://nmap.org">nmap</a> or similar tools). If you want to scan all nodes in the local network you first need to know the MAC address of all possible addresses.</p><p>The only strange thing is that the system first seems to have IP address 192.168.0.2 (see the gap in the ARP request) and the it changes its IP address to 192.168.0.3. I have no good explanation for that, but this does not look like an ARP poisioning attack.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44255" class="comments-container"><span id="44267"></span><div id="comment-44267" class="comment"><div id="post-44267-score" class="comment-score"></div><div class="comment-text"><p>Well, this is indeed a arp poisoning attack, I got it from a hacking forum to analyse it. By the way, I thought it was a kind of sweep but I was just wondering why it was there. Thanks.</p></div><div id="comment-44267-info" class="comment-info"><span class="comment-age">(17 Jul '15, 13:18)</span> shad0w125</div></div></div><div id="comment-tools-44255" class="comment-tools"></div><div class="clear"></div><div id="comment-44255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

