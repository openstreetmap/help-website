+++
type = "question"
title = "IGMP in wirshark"
description = '''have two devices that communicate over Ethernet/IP - cannot get them conncted so found a Hub and connected them and my PC running Wireshark - what I see is the Client (192.168.144.11) device making a connection to the Server device (192.168.144.130) but then the Client goes to following: 239.192.17....'''
date = "2011-03-17T18:12:00Z"
lastmod = "2011-03-18T07:43:00Z"
weight = 2916
keywords = [ "industrial-network", "igmp" ]
aliases = [ "/questions/2916" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IGMP in wirshark](/questions/2916/igmp-in-wirshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2916-score" class="post-score" title="current number of votes">0</div><span id="post-2916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>have two devices that communicate over Ethernet/IP - cannot get them conncted so found a Hub and connected them and my PC running Wireshark - what I see is the Client (192.168.144.11) device making a connection to the Server device (192.168.144.130) but then the Client goes to following:</p><p>239.192.17.32 IGMP V2 Membership Report Join group 239.192.17.32</p><p>when it should simply continue talking to the Server device - consequently the connection between my devices' fails</p><p>Can anyone help me understand where this could come from</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-industrial-network" rel="tag" title="see questions tagged &#39;industrial-network&#39;">industrial-network</span> <span class="post-tag tag-link-igmp" rel="tag" title="see questions tagged &#39;igmp&#39;">igmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '11, 18:12</strong></p><img src="https://secure.gravatar.com/avatar/485e1e3e7c6833bc8bca5a4e445dbc53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonyh110&#39;s gravatar image" /><p><span>tonyh110</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonyh110 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>18 Mar '11, 09:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span></p></div></div><div id="comments-container-2916" class="comments-container"><span id="2918"></span><div id="comment-2918" class="comment"><div id="post-2918-score" class="comment-score"></div><div class="comment-text"><p>I'm not familiar with Ethernet/IP (by which I'm assuming you mean Industrial Protocol) so I'll just note the following:</p><p>IGMP is a protocol in it's own right completely separate from TCP (which is presumably the protocol being used in "making a connection").</p><p>The IGMP message is merely the client requesting to receive multicast messages from group 239.192.17.32 so I suspect "consequently the connection between my devices' fails" is not really correct.</p><p>What do you mean by "cannot get them connected" ? Does the TCP 3-way handshake complete ?</p></div><div id="comment-2918-info" class="comment-info"><span class="comment-age">(17 Mar '11, 19:28)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-2916" class="comment-tools"></div><div class="clear"></div><div id="comment-2916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2921"></span>

<div id="answer-container-2921" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2921-score" class="post-score" title="current number of votes">0</div><span id="post-2921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Bill, thanks for your reply - yes its industrial CAN bus over TCP/IP - once the Client device makes a connection then a CIP CM transaction opens - because the Client starts this IGMP request the Server device stops responding at the CIP level I have the Client device vendor working on the problem - but your answer helps me understand this much better - thing is Industrial Networks are deterministic and wont suffer timeouts (which begs why do they put such critical stuff through a non-deterministic transport layer)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '11, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/485e1e3e7c6833bc8bca5a4e445dbc53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonyh110&#39;s gravatar image" /><p><span>tonyh110</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonyh110 has no accepted answers">0%</span></p></div></div><div id="comments-container-2921" class="comments-container"></div><div id="comment-tools-2921" class="comment-tools"></div><div class="clear"></div><div id="comment-2921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

