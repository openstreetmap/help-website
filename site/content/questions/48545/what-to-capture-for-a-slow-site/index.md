+++
type = "question"
title = "What To capture for a slow site?"
description = '''I apologise in advance but i&#x27;m just learning about Wireshark. I&#x27;m an engineer who works for company that does the IT for medical centres. I was asked to investigate a strange issue that has been affecting the site for the last 7 months. Every four weeks on a wednesday, without fail, the entire site ...'''
date = "2015-12-15T13:40:00Z"
lastmod = "2015-12-15T13:52:00Z"
weight = 48545
keywords = [ "slowness" ]
aliases = [ "/questions/48545" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What To capture for a slow site?](/questions/48545/what-to-capture-for-a-slow-site)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I apologise in advance but i'm just learning about Wireshark. I'm an engineer who works for company that does the IT for medical centres. I was asked to investigate a strange issue that has been affecting the site for the last 7 months. Every four weeks on a wednesday, without fail, the entire site grinds to a crawl. There has been investigations by the tech team, and BT, but they cannot seem to find where the problem is coming from. They asked me to run a Wireshark capture. I did this on a day that the site was running fine, and on a day it was crawling. Someone else will get to look at this, but it interests me as well. Would there be anything specific you'd be looking for if you were in this situation? Kind regards. Darren</p></div><div id="question-tags" class="tags-container tags">slowness</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/24611aafc99d31e9761b15a41bb2fb29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="1470&#39;s gravatar image" /><p>1470<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="1470 has no accepted answers">0%</span></p></div></div><div id="comments-container-48545" class="comments-container"></div><div id="comment-tools-48545" class="comment-tools"></div><div class="clear"></div><div id="comment-48545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48546"></span>

<div id="answer-container-48546" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48546-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would start from looking at the following things:</p><ul><li><p>unusually high volume of traffic (go <code>Statistics -&gt; Conversations</code>, sort by number of packets and by number of bytes by clicking the column header), aka "someone is downloading films" or "something is doing a monthly backup"</p></li><li><p>unusually high number of tcp retransmissions, aka "something is wrong on the uplink connection" (display filter <code>tcp.analysis.retransmission</code>).</p></li></ul><p>The two may be related together, as if there is a traffic shaping policy on the uplink (which is quite likely), attempts to transfer high volumes of data will cause packets to be dropped and thus retransmitted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '15, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48546" class="comments-container"><span id="48549"></span><div id="comment-48549" class="comment"><div id="post-48549-score" class="comment-score"></div><div class="comment-text"><p>Thank you Sindy. Very kind of you to answer so soon.</p></div><div id="comment-48549-info" class="comment-info"><span class="comment-age">(15 Dec '15, 14:07)</span> 1470</div></div></div><div id="comment-tools-48546" class="comment-tools"></div><div class="clear"></div><div id="comment-48546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

