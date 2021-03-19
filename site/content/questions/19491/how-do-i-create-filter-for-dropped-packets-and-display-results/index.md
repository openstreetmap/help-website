+++
type = "question"
title = "How do I create filter for dropped packets and display results"
description = '''I am trying to isolate faulty equipment in a network. My idea is that if I can measure dropped packets between various components on the network I can ultimately isolate the bad component by narrowing the beginning and end points of the analysis. What I don&#x27;t understand is how to &quot;append a filter to...'''
date = "2013-03-14T02:04:00Z"
lastmod = "2013-03-14T02:30:00Z"
weight = 19491
keywords = [ "missing_packets" ]
aliases = [ "/questions/19491" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I create filter for dropped packets and display results](/questions/19491/how-do-i-create-filter-for-dropped-packets-and-display-results)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19491-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to isolate faulty equipment in a network. My idea is that if I can measure dropped packets between various components on the network I can ultimately isolate the bad component by narrowing the beginning and end points of the analysis.</p><p>What I don't understand is how to "append a filter to a conversation". There is an answered question about how to create the filter in your database but I can't figure out how to append a filter to a particular conversation.</p><p>Example: I create a filter on the conversations that shows me the traffic between a given computer and my router(one conversion). What I think I want to do is then apply the tcp.analysis.lost_segment filter to that particular conversation. Don't know how to do that. If this is something I can do then how would I view the results once the filter is in place?</p><p>Thanks for any help you can provide.</p></div><div id="question-tags" class="tags-container tags">missing_packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/fac7670ad51ab3bf0cd317a70b5e28af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrBub&#39;s gravatar image" /><p>MrBub<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrBub has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '13, 02:06</p></div></div><div id="comments-container-19491" class="comments-container"></div><div id="comment-tools-19491" class="comment-tools"></div><div class="clear"></div><div id="comment-19491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19492"></span>

<div id="answer-container-19492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19492-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if you already have a conversation filter in place, you could just put that filter in brackets and add " and tcp.analysis.lost_segment". That will show all packets that are from that conversation as well as having the "lost segment" symptom.</p><p>The result will be all packets where Wireshark has determined that there was at least one (or more) segments lost <strong>before</strong> the frame that is marked with the symptom. If you need to determine how many packets it actually were it may be useful to look for the retransmissions instead. A "lost segment" gap can be more than one packets wide, but each packet has to be retransmitted, so count these instead.</p><p>All this works if you are sure that you have no drops, meaning that you capture all packets that have been on the wire. If you have drops (at the capture PC or SPAN port) your calculations will be off.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '13, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '13, 02:31</p></div></div><div id="comments-container-19492" class="comments-container"></div><div id="comment-tools-19492" class="comment-tools"></div><div class="clear"></div><div id="comment-19492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

