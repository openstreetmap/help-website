+++
type = "question"
title = "Capturing all traffic from one IP"
description = '''I would like to capture all traffic leaving and arriving to a specific on my netowrk. Unfortunately the &quot;host IP&quot; command does not work both ways. Only when I initiate traffic, so I know I am missing a step. Can you help me out?'''
date = "2014-05-28T10:56:00Z"
lastmod = "2014-05-28T18:52:00Z"
weight = 33140
keywords = [ "ip", "traffic", "capturing" ]
aliases = [ "/questions/33140" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing all traffic from one IP](/questions/33140/capturing-all-traffic-from-one-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33140-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to capture all traffic leaving and arriving to a specific on my netowrk. Unfortunately the "host IP" command does not work both ways. Only when I initiate traffic, so I know I am missing a step. Can you help me out?</p></div><div id="question-tags" class="tags-container tags">ip traffic capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/7d265b804c113ade8c794311b7272681?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itteche&#39;s gravatar image" /><p>itteche<br />
<span class="score" title="20 reputation points">20</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itteche has no accepted answers">0%</span></p></div></div><div id="comments-container-33140" class="comments-container"></div><div id="comment-tools-33140" class="comment-tools"></div><div class="clear"></div><div id="comment-33140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33141"></span>

<div id="answer-container-33141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33141-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are talking about a Capture filter, then the "host [ip address]" filter will capture all traffic to/from that specific address.</p><p>If you are talking about a display filter, then the "ip.addr==[ip address]" filter will display all traffic to/from the specified IP address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '14, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-33141" class="comments-container"><span id="33161"></span><div id="comment-33161" class="comment"><div id="post-33161-score" class="comment-score"></div><div class="comment-text"><p>I've tried the host ip, did not work. I will try the next option to see if that works.</p></div><div id="comment-33161-info" class="comment-info"><span class="comment-age">(29 May '14, 04:57)</span> itteche</div></div></div><div id="comment-tools-33141" class="comment-tools"></div><div class="clear"></div><div id="comment-33141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33144"></span>

<div id="answer-container-33144" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33144-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try "(vlan and ip host [ip address]) or (ip host [ip address])" without the quotes. If you're capturing two legs where one has a vlan tag, that will prevent it from matching that type of IP display filter.</p><p>Having said that, the plain 'ip host [address]' filter should be valid for two-way traffic to that one IP. Are you certain that you are capturing traffic in a place where you should be able to see both directions? If so, is this pure IP traffic over Ethernet we're talking about here?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '14, 18:52</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 May '14, 20:48</p></div></div><div id="comments-container-33144" class="comments-container"><span id="33162"></span><div id="comment-33162" class="comment"><div id="post-33162-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by in the place it should be?</p></div><div id="comment-33162-info" class="comment-info"><span class="comment-age">(29 May '14, 05:09)</span> itteche</div></div><span id="33163"></span><div id="comment-33163" class="comment"><div id="post-33163-score" class="comment-score"></div><div class="comment-text"><p>@itteche</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-33163-info" class="comment-info"><span class="comment-age">(29 May '14, 05:32)</span> grahamb ♦</div></div><span id="33182"></span><div id="comment-33182" class="comment"><div id="post-33182-score" class="comment-score"></div><div class="comment-text"><p>What I mean is, when you are running Wireshark you need to make sure you are running it on a system that is receiving the traffic you want to capture. Where are you runnning Wireshark as it relates to the traffic you are capturing in your network?</p></div><div id="comment-33182-info" class="comment-info"><span class="comment-age">(29 May '14, 16:00)</span> Quadratic</div></div></div><div id="comment-tools-33144" class="comment-tools"></div><div class="clear"></div><div id="comment-33144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

