+++
type = "question"
title = "How to capture port 25 traffic on Internet address?"
description = '''Could someone please advise me on capturing outgoing port 25 traffic on our Internet IP address? We were placed on a couple of block lists, mostly cleared except for Outlook.com/Microsoft services. I have been capturing internal port 25 traffic just fine, where we look clean. I&#x27;d like to look at it ...'''
date = "2014-05-18T20:22:00Z"
lastmod = "2014-05-18T23:53:00Z"
weight = 32874
keywords = [ "capture", "side", "internet" ]
aliases = [ "/questions/32874" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture port 25 traffic on Internet address?](/questions/32874/how-to-capture-port-25-traffic-on-internet-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32874-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could someone please advise me on capturing outgoing port 25 traffic on our Internet IP address?</p><p>We were placed on a couple of block lists, mostly cleared except for Outlook.com/Microsoft services. I have been capturing internal port 25 traffic just fine, where we look clean.</p><p>I'd like to look at it from the "Internet side." I guess I need to do this remotely? Any assistance and with an example most appreciated.</p><p>Thanks to the very helpful documentation and examples already out there I have been able to capture internal traffic, now just need the view from "outside."</p></div><div id="question-tags" class="tags-container tags">capture side internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '14, 20:22</strong></p><img src="https://secure.gravatar.com/avatar/890f18d56a845a73a04e9f52f75a0dba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Neilrahc&#39;s gravatar image" /><p>Neilrahc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Neilrahc has no accepted answers">0%</span></p></div></div><div id="comments-container-32874" class="comments-container"></div><div id="comment-tools-32874" class="comment-tools"></div><div class="clear"></div><div id="comment-32874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32877"></span>

<div id="answer-container-32877" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32877-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Inside or outside is usually just a difference in where you capture the data. If you need to capture packets on the outside you need to place your capture device on the port that connects you to your ISP. In most cases this is at the ISP router or on the outside of your own Firewall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '14, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32877" class="comments-container"><span id="32886"></span><div id="comment-32886" class="comment"><div id="post-32886-score" class="comment-score"></div><div class="comment-text"><p>Ok, thanks, that helps clarify. I wonder if I could do this remotely? I can at least ping that address.</p><p>Otherwise I could maybe put a switch between the company router and the ISP connection.</p></div><div id="comment-32886-info" class="comment-info"><span class="comment-age">(19 May '14, 05:45)</span> Neilrahc</div></div><span id="32887"></span><div id="comment-32887" class="comment"><div id="post-32887-score" class="comment-score"></div><div class="comment-text"><p>No you cannot do that remotely, because the outside packets will not be seen at the remote site - except for the answer packets of anything you sent (if you get an answer at all, depending on the firewall rules). My advice would be to put a switch between your company router and the ISP connection (if it is Ethernet, of course) and capture at the switch.</p></div><div id="comment-32887-info" class="comment-info"><span class="comment-age">(19 May '14, 05:48)</span> Jasper ♦♦</div></div></div><div id="comment-tools-32877" class="comment-tools"></div><div class="clear"></div><div id="comment-32877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

