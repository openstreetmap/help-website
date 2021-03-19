+++
type = "question"
title = "Detecting UDP packets on simplex channel of a tap using SW API"
description = '''Background. Have a lab setup involving multiple PC&#x27;s with add-in 4-slot NIC cards, and a manufactured box with static IP addresses, all connected using Ethernet cable. Our plan was to insert a tap (Black Box 10/100 Aggregate Copper Tap) into one of the data connections between the box and PC#1, with...'''
date = "2015-09-30T12:25:00Z"
lastmod = "2015-10-01T06:14:00Z"
weight = 46286
keywords = [ "udp", "tap" ]
aliases = [ "/questions/46286" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Detecting UDP packets on simplex channel of a tap using SW API](/questions/46286/detecting-udp-packets-on-simplex-channel-of-a-tap-using-sw-api)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46286-score" class="post-score" title="current number of votes">0</div><span id="post-46286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Background. Have a lab setup involving multiple PC's with add-in 4-slot NIC cards, and a manufactured box with static IP addresses, all connected using Ethernet cable. Our plan was to insert a tap (Black Box 10/100 Aggregate Copper Tap) into one of the data connections between the box and PC#1, with the straight-thru connection going to PC#1, and a second Ethernet cable connecting to PC#2 from the tap's "A" output; ie we want the traffic going from the box to PC#1. The PC's are on a company network using their system board NIC and the usual dynamic IP address allocation, while the static IP addresses are on the add-in cards (1 add-in card per PC).</p><p>Problem. Wireshark seems to be in agreement on both PC's, as to traffic info. Most important, it can see the uni-directional traffic on the tap output line. But my software app cannot seem to do so.</p><p>Question: Can high-level network socket SW API's recognize UDP packets on this type of tap output line? For now, I just want to know if it's possible or not. I'm attempting to use MS Visual Studio C#'s socket API set, since the rest of the app is in C#. We have C++ apps that do this, but they all use the WinPCap API interface to do so. So, before I switch over to use the WinPCap API, I'm wondering if I'm screwing up somewhere in the C# socket initialization code.</p><p>Thanks for any insights.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '15, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/3ab83edb8bd57136e5d7459848963025?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StevenSperling&#39;s gravatar image" /><p><span>StevenSperling</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StevenSperling has no accepted answers">0%</span></p></div></div><div id="comments-container-46286" class="comments-container"></div><div id="comment-tools-46286" class="comment-tools"></div><div class="clear"></div><div id="comment-46286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46301"></span>

<div id="answer-container-46301" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46301-score" class="post-score" title="current number of votes">0</div><span id="post-46301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="StevenSperling has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should look into WHY these C++ apps all use the WinPcap API instead of the high-level network socket API. They can't all be wrong in choosing that over the 'normal' network socket API?</p><p>Fact is, you need low level access to the network. Since the high level sockets are not involved in a connection they will not present you with the tap line traffic. You may be able to tweak the options of a specific type of socket to get at this, but then you basically are reinventing parts of WinPcap. Might be worth to look at HOW these C++ apps use the WinPcap API. As for porting that to C# I've got no clue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '15, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46301" class="comments-container"><span id="46307"></span><div id="comment-46307" class="comment"><div id="post-46307-score" class="comment-score"></div><div class="comment-text"><p>Is it that by using the WinPCap interface they can put the NIC into promiscuous mode?</p></div><div id="comment-46307-info" class="comment-info"><span class="comment-age">(01 Oct '15, 03:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="46310"></span><div id="comment-46310" class="comment"><div id="post-46310-score" class="comment-score"></div><div class="comment-text"><p>To Jaap: Thanks for the input. And you are correct I believe with the tweak option; saw a post that indicated a raw packet socket option that would probably see the data at least. To Grahamb: Correct.</p></div><div id="comment-46310-info" class="comment-info"><span class="comment-age">(01 Oct '15, 06:14)</span> <span class="comment-user userinfo">StevenSperling</span></div></div></div><div id="comment-tools-46301" class="comment-tools"></div><div class="clear"></div><div id="comment-46301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

