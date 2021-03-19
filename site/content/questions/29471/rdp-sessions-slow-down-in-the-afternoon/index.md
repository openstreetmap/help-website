+++
type = "question"
title = "RDP Sessions Slow down in the afternoon"
description = '''Hello - this one has been puzzling me for some time. I frequently RDP to the office from home via 3 different methods: site to site VPN, client VPN, and Citrix RDP. There is no difference in behavior between the three methods, nor is there a difference in behavior if I RDP from different home machin...'''
date = "2014-02-05T13:14:00Z"
lastmod = "2015-04-18T11:53:00Z"
weight = 29471
keywords = [ "ack", "duplicate", "session", "tpkt", "rdp" ]
aliases = [ "/questions/29471" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RDP Sessions Slow down in the afternoon](/questions/29471/rdp-sessions-slow-down-in-the-afternoon)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29471-score" class="post-score" title="current number of votes">0</div><span id="post-29471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello - this one has been puzzling me for some time. I frequently RDP to the office from home via 3 different methods: site to site VPN, client VPN, and Citrix RDP. There is no difference in behavior between the three methods, nor is there a difference in behavior if I RDP from different home machines, or target different machines at the office (even on different subnets.</p><p>What happens is the latency substantially increases in the afternoon, however only via RDP. Users in the office do not see this, there is no bandwidth issue at the office. Nor is there anything that runs in the afternoon. This has been going on for months.</p><p>Wireshark reveals on the destination that the source is constantly sending duplicate ACKs, perhpas 6-10 of them in response to a TPKT continuation packet. The ACKs are in rapid succession, time differences are in the 10000th of a second.</p><p>These happen every 1/2 to 1 second.<br />
</p><p>Anyone have any ideas? I've updated NIC drives on both ends and again, only happens via RDP. If I'm in the office, I can run WS all day and don't see these, same thing from my home machine to any other destination.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-tpkt" rel="tag" title="see questions tagged &#39;tpkt&#39;">tpkt</span> <span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '14, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/092c1c399b449f3be26551a98dcafff9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DB13&#39;s gravatar image" /><p><span>DB13</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DB13 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29471" class="comments-container"><span id="29472"></span><div id="comment-29472" class="comment"><div id="post-29472-score" class="comment-score"></div><div class="comment-text"><p>Do those ACKs have the same IP ID?</p></div><div id="comment-29472-info" class="comment-info"><span class="comment-age">(05 Feb '14, 13:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29473"></span><div id="comment-29473" class="comment"><div id="post-29473-score" class="comment-score"></div><div class="comment-text"><p>I'm trying to find out how to see that info, but do not see it in the break down. Is that exclusive to WS?</p></div><div id="comment-29473-info" class="comment-info"><span class="comment-age">(05 Feb '14, 13:45)</span> <span class="comment-user userinfo">DB13</span></div></div><span id="29474"></span><div id="comment-29474" class="comment"><div id="post-29474-score" class="comment-score"></div><div class="comment-text"><p>Just open the IP layer in Wireshark. The IP ID is one of the fields.</p></div><div id="comment-29474-info" class="comment-info"><span class="comment-age">(05 Feb '14, 14:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29477"></span><div id="comment-29477" class="comment"><div id="post-29477-score" class="comment-score"></div><div class="comment-text"><p>Got it. No, each one is sequentially increasing in value. What does that indicate?</p></div><div id="comment-29477-info" class="comment-info"><span class="comment-age">(05 Feb '14, 17:26)</span> <span class="comment-user userinfo">DB13</span></div></div><span id="29478"></span><div id="comment-29478" class="comment"><div id="post-29478-score" class="comment-score"></div><div class="comment-text"><p>Consecutive frames with the same IP ID could have indicated a loop somewhere.</p><p>Is it possible to post the capture file (Google drive, dropbox, cloudshark.org)?</p></div><div id="comment-29478-info" class="comment-info"><span class="comment-age">(05 Feb '14, 23:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29493"></span><div id="comment-29493" class="comment not_top_scorer"><div id="post-29493-score" class="comment-score"></div><div class="comment-text"><p>Sure, here it is. <a href="http://www.cloudshark.org/captures/f4383a0d23cd">http://www.cloudshark.org/captures/f4383a0d23cd</a></p><p>A loop would extremely surprising. Also note that going the other way, from work to home, I do not see this behavior on either side - no duplicate ACKs...</p></div><div id="comment-29493-info" class="comment-info"><span class="comment-age">(06 Feb '14, 10:49)</span> <span class="comment-user userinfo">DB13</span></div></div></div><div id="comment-tools-29471" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-29471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29513"></span>

<div id="answer-container-29513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29513-score" class="post-score" title="current number of votes">0</div><span id="post-29513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP session is using SACK and your client is reporting gaps indicating packets are dropped in the network. The amount of traffic is certainly not something to cause those packet losses so it must be something else going on here. Segmentation Offload is also enabled at the server side.<br />
</p><p>filter: <code>tcp.analysis.retransmission or tcp.options.sack.count &gt; 0</code></p><p>As this only occurs over the WAN in the afternoon and other protocols (non-RDP but also TCP?) are ok at the same time I suspect some kind of traffic shaping occurring here. Maybe you talk to your network folks and have them bump up the priority (ip.dsfield) of your tcp 3389 traffic before the packets enter the VPN. Maybe also disabling TSO at the server side might be of help here .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '14, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-29513" class="comments-container"><span id="29533"></span><div id="comment-29533" class="comment"><div id="post-29533-score" class="comment-score"></div><div class="comment-text"><p>Hi - thanks for the reply. We do not have any QoS policies in place, so there is no traffic shaping occurring. I have a 50 Mbps line at home, and we have a 200 Mbps line at the office, typically we don't have any bandwidth issues. I've checked the circuits during the problem times and they are not maxing out. Just not sure why there would be packet loss at all.</p></div><div id="comment-29533-info" class="comment-info"><span class="comment-age">(07 Feb '14, 07:11)</span> <span class="comment-user userinfo">DB13</span></div></div><span id="29535"></span><div id="comment-29535" class="comment"><div id="post-29535-score" class="comment-score"></div><div class="comment-text"><p>"...why there would be packet loss at all" is the question indeed.</p><p>You need to identify where the packets are lost by tracing at multiple points simultaneously.</p></div><div id="comment-29535-info" class="comment-info"><span class="comment-age">(07 Feb '14, 07:22)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="41563"></span><div id="comment-41563" class="comment"><div id="post-41563-score" class="comment-score"></div><div class="comment-text"><p>sometimes packet loss could happen on a line which uses only 1% of the bandwith. Watch out for microburst.</p></div><div id="comment-41563-info" class="comment-info"><span class="comment-age">(18 Apr '15, 11:53)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-29513" class="comment-tools"></div><div class="clear"></div><div id="comment-29513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

