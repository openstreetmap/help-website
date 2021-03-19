+++
type = "question"
title = "Sniffing Multiple Switches"
description = '''I have a client who has a network that has a FIOS router that uplinks into their main switch. this main switch has two other switches plugged into it that are in different parts of the office. Each of the remote switches have anywhere from 6 to 8 users plugged into each and the main one has about 10...'''
date = "2014-06-23T06:04:00Z"
lastmod = "2014-06-26T07:07:00Z"
weight = 34072
keywords = [ "switchednetwork", "switch", "multiple", "sniff", "hub" ]
aliases = [ "/questions/34072" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffing Multiple Switches](/questions/34072/sniffing-multiple-switches)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34072-score" class="post-score" title="current number of votes">0</div><span id="post-34072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a client who has a network that has a FIOS router that uplinks into their main switch. this main switch has two other switches plugged into it that are in different parts of the office. Each of the remote switches have anywhere from 6 to 8 users plugged into each and the main one has about 10 connections plugged into it plus the 2 other switches. i know i need a hub to be able to sniff the traffic on the switches. i was planning on connecting the fios to the switchable uplink port on the hub and use a crossover cable to hook the main switch (with the other 2 switches plugged into it) to the hub also, then connect my laptop to the same hub. My question is would the laptop be able to sniff the traffic from all the switches in that configuration. it would be very difficult to run crossover cable to each of the 2 remote switches and i am hoping that i wont need to.</p><p>please inform me as i am not sure as i never had to sniff more than one switch before....</p><p>thank you</p><p>andy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-switchednetwork" rel="tag" title="see questions tagged &#39;switchednetwork&#39;">switchednetwork</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-sniff" rel="tag" title="see questions tagged &#39;sniff&#39;">sniff</span> <span class="post-tag tag-link-hub" rel="tag" title="see questions tagged &#39;hub&#39;">hub</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/211b7427028098641110de9231d79c5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="medusanyc&#39;s gravatar image" /><p><span>medusanyc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="medusanyc has no accepted answers">0%</span></p></div></div><div id="comments-container-34072" class="comments-container"></div><div id="comment-tools-34072" class="comment-tools"></div><div class="clear"></div><div id="comment-34072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34094"></span>

<div id="answer-container-34094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34094-score" class="post-score" title="current number of votes">0</div><span id="post-34094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you just looking at the office traffic via the FIOS router, or also internal traffic? If the first then any decent switch should be able to give you a monitor port to look at that traffic. Or get a <a href="http://wiki.wireshark.org/SwitchReference">small one</a> and stick that in between the FIOS router and the main switch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '14, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-34094" class="comments-container"><span id="34100"></span><div id="comment-34100" class="comment"><div id="post-34100-score" class="comment-score"></div><div class="comment-text"><p>i want to monitor the traffic of the workstations across the network. i dont have a monitor port on my switches nor do i have a managed switch.<br />
</p><p>will i be able to use a hub on my network to sniff the traffic across all the switches,i am more interested in the traffic across the internal network than the traffic to the internet</p></div><div id="comment-34100-info" class="comment-info"><span class="comment-age">(23 Jun '14, 18:43)</span> <span class="comment-user userinfo">medusanyc</span></div></div><span id="34108"></span><div id="comment-34108" class="comment"><div id="post-34108-score" class="comment-score"></div><div class="comment-text"><p>What does a switch do? It tries to get the frames to the right destination. So, two machines on a remote switch exchanging frames will have their frames confined to that switch. That means that you'll end up exchanging every switch with a hub to get all traffic on the core hub, which you want to monitor. This will do no good for your network performance, going from full duplex to half duplex and all traffic flushing out of every network port.</p><p>Wanting to see <em>all</em> traffic on a network leads me to believe that you've no idea where to look for the thing you're looking for. I would suggest working different angles to the problem and see if you can narrow down the amount of traffic <em>you</em> need to analyze.</p></div><div id="comment-34108-info" class="comment-info"><span class="comment-age">(24 Jun '14, 00:17)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="34111"></span><div id="comment-34111" class="comment"><div id="post-34111-score" class="comment-score"></div><div class="comment-text"><p>i found there are crossover adapters. if i connect each switch to the hub independantly then connect my laptop to the hub would that allow me to see the traffic on all three switches?</p></div><div id="comment-34111-info" class="comment-info"><span class="comment-age">(24 Jun '14, 04:28)</span> <span class="comment-user userinfo">medusanyc</span></div></div><span id="34112"></span><div id="comment-34112" class="comment"><div id="post-34112-score" class="comment-score"></div><div class="comment-text"><p><span>@medusanyc</span> Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>I think you're still missing the point. If two machines are connected to the same switch, traffic between the two will never leave the switch (and will be confined to their respective switch ports apart from broadcast traffic) and you'll never see it with you hub connected to the switch.</p><p>That's how a switch works, hence the need for managed switches that can span or mirror a port to another port so you can capture the traffic <em>internal</em> to the switch.</p><p>You could insert the hub between the switch and a machine of interest, but then you'll still only be able to monitor one machine at a time and will need to move the hub to monitor another machine.</p></div><div id="comment-34112-info" class="comment-info"><span class="comment-age">(24 Jun '14, 04:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="34215"></span><div id="comment-34215" class="comment"><div id="post-34215-score" class="comment-score"></div><div class="comment-text"><p>i think i got it now. i should plug our server into the hub along with the switch that all the traffic goes through, then plug my laptop into the hub and i should be able to monitor all the traffice between the workstations and the servers.</p><p>we have 2 servers can i plug both into the hub and monitor traffic from both?</p></div><div id="comment-34215-info" class="comment-info"><span class="comment-age">(26 Jun '14, 07:07)</span> <span class="comment-user userinfo">medusanyc</span></div></div></div><div id="comment-tools-34094" class="comment-tools"></div><div class="clear"></div><div id="comment-34094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

