+++
type = "question"
title = "Is my computer being attacked?"
description = '''Would anyway be able to have a look in the pcap of my computer as I am thinking my computer get attacked by a process keep sending out packet from my computer to DoS my network.  I get errors in DNS very often and I simply cannot use the internet.  pcap'''
date = "2016-04-10T18:31:00Z"
lastmod = "2016-04-19T06:50:00Z"
weight = 51548
keywords = [ "dos" ]
aliases = [ "/questions/51548" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is my computer being attacked?](/questions/51548/is-my-computer-being-attacked)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51548-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would anyway be able to have a look in the pcap of my computer as I am thinking my computer get attacked by a process keep sending out packet from my computer to DoS my network. I get errors in DNS very often and I simply cannot use the internet.<br />
</p><p><a href="https://www.dropbox.com/s/s3dycoupemrv9sa/MyComputerIsGone_anon.pcapng?dl=0">pcap</a></p></div><div id="question-tags" class="tags-container tags">dos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '16, 18:31</strong></p><img src="https://secure.gravatar.com/avatar/73e25bdfef6a24bfbf1c2357c1d70637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Henrylalala&#39;s gravatar image" /><p>Henrylalala<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Henrylalala has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '16, 18:33</p></div></div><div id="comments-container-51548" class="comments-container"><span id="51559"></span><div id="comment-51559" class="comment"><div id="post-51559-score" class="comment-score"></div><div class="comment-text"><p>To help with this one you'd atleast have to posts the part(s) of the pcap you are concerned with.</p></div><div id="comment-51559-info" class="comment-info"><span class="comment-age">(11 Apr '16, 10:29)</span> msmorten</div></div><span id="51739"></span><div id="comment-51739" class="comment"><div id="post-51739-score" class="comment-score"></div><div class="comment-text"><p>As msmorten points out we could do with some indication of which packets you are concerned about.</p><p>Did you choose to capture the layer 4 headers only as none of the packets appear to have any data?</p><p>From the PCAP provided it certainly appears like something isn't working properly as there is no data in what appears to be DNS packets (It's UDP to port 53), or any packets for that matter.</p></div><div id="comment-51739-info" class="comment-info"><span class="comment-age">(17 Apr '16, 19:05)</span> sludge3000</div></div></div><div id="comment-tools-51548" class="comment-tools"></div><div class="clear"></div><div id="comment-51548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51787"></span>

<div id="answer-container-51787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51787-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have limited the frame size during the capturing phase, so it's impossible to do any (deeper) analysis.</p><p>From what I can see in the pcap: Your client (172.23.72.15) is sending a lot more requests to your DNS resolver (192.168.159.250) thaen it receives responses. That could be a sign for DNS problems. As I said: You've limited the frame size during the capturing phase, so any further analysis is not possible.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-51787" class="comments-container"></div><div id="comment-tools-51787" class="comment-tools"></div><div class="clear"></div><div id="comment-51787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

