+++
type = "question"
title = "Time Machine to Network drive doesn&#x27;t finish"
description = '''Hi Guys, We are trying to backup a macbook air to a Synology diskstation over wireless using Time Machine. We are able to backup on a wired connection but on wireless the Mac says &quot;Preparing backup&quot; and never starts the backup. I took a capture from our router and saw that there are a lot of &quot;TCP Re...'''
date = "2013-11-08T10:56:00Z"
lastmod = "2013-11-12T04:18:00Z"
weight = 26783
keywords = [ "wireless", "nas", "mac", "afp" ]
aliases = [ "/questions/26783" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Time Machine to Network drive doesn't finish](/questions/26783/time-machine-to-network-drive-doesnt-finish)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26783-score" class="post-score" title="current number of votes">0</div><span id="post-26783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>We are trying to backup a macbook air to a Synology diskstation over wireless using Time Machine. We are able to backup on a wired connection but on wireless the Mac says "Preparing backup" and never starts the backup. I took a capture from our router and saw that there are a lot of "TCP Retransmission" and "TCP Out of Order" packets. From what it looks like packets are first being transmitted to the router and the router is retransmitting them to the Synology. I am wondering if this is normal since the Macbook is connected through a wireless access point to a switch then to the router or if there is a problem in the routing.</p><p>Capture file can be found <a href="http://www.cloudshark.org/captures/418e1909c587">here.</a></p><p>Thank you in advance!!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-nas" rel="tag" title="see questions tagged &#39;nas&#39;">nas</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-afp" rel="tag" title="see questions tagged &#39;afp&#39;">afp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '13, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/dae23d56e1def8b3ca2023c7fb7e6258?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clarsen&#39;s gravatar image" /><p><span>clarsen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clarsen has no accepted answers">0%</span></p></div></div><div id="comments-container-26783" class="comments-container"></div><div id="comment-tools-26783" class="comment-tools"></div><div class="clear"></div><div id="comment-26783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26819"></span>

<div id="answer-container-26819" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26819-score" class="post-score" title="current number of votes">2</div><span id="post-26819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That one's indeed tricky. An yes, the router (where the trace was taken) initially seems to be in the path even though we are within the same sub-net and so the ARP table in the MacBook should contain the the NAS's MAC address. Instead the packets are sent to the SonicWall router's MAC address, who forwards them to the Synology NAS. Why this happens - still - is a mystery to me as I'm not an WLAN expert. Here some more observations which might provide some hints as to why this is happening:</p><ul><li>The Sonicwall router adjusts the MSS option of the syn packets from 1460 to 1452</li><li>The router does not decrement the ip.ttl</li><li>The dest-MAC of the NAS changes 360s into the trace (Synology:20:59:f7 -&gt; Synology:20:59:f9)</li><li>Before (298s-360s into the trace)there were 3823153 not traced in the router (in both directions)</li></ul><p>As for the problem you are investigating, I'd say the NAS server is closing the session unexpectedly with a 'server shutting down' indication.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/afp.PNG" alt="alt text" /></p><p>There was a discussion about <a href="http://forum.synology.com/enu/viewtopic.php?f=159&amp;t=49914">wireless Time Machine backup not supported</a> in a Synology forum which might lead you to the right experts.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '13, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-26819" class="comments-container"><span id="26846"></span><div id="comment-26846" class="comment"><div id="post-26846-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your insight, it has been extremely helpful. How did you configure wireshark to show DSI_Type, DSI req/rply and the associated flags? I'm still figuring out how to get the most out of wireshark. Thanks!!</p></div><div id="comment-26846-info" class="comment-info"><span class="comment-age">(11 Nov '13, 08:24)</span> <span class="comment-user userinfo">clarsen</span></div></div><span id="26863"></span><div id="comment-26863" class="comment"><div id="post-26863-score" class="comment-score">1</div><div class="comment-text"><p>The easiest way to add any field to the packet list is to go to the packet details, right-click on the desired field and 'Apply as Column'. As an owner of a question, don't forget to 'accept' an answer when you're satisfied.</p></div><div id="comment-26863-info" class="comment-info"><span class="comment-age">(11 Nov '13, 21:39)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-26819" class="comment-tools"></div><div class="clear"></div><div id="comment-26819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26827"></span>

<div id="answer-container-26827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26827-score" class="post-score" title="current number of votes">1</div><span id="post-26827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As <span><span>@mrEEde</span></span> mentioned, the frames are first forwarded to the router (SonicWall) and then probably forwarded by the SonicWall to the Synology.</p><blockquote><p>I am wondering if this is normal since the Macbook is connected through a wireless access point to a switch then to the router or if there is a problem in the routing.</p></blockquote><p>The only plausible explanation I can think of (besides a bug somewhere): The Mac gets a wrong netmask while connected via the AP, i.e. /25 instead of /24. In that case 10.250.212.145 is <strong>not</strong> in the same subnet from the Macs perspective (10.250.212.0/25 == 10.250.212.1 - 10.250.212.127) and thus it forwards the traffic to its default gateway (SonicWall - maybe 10.250.212.1). As the SonicWall has a subnet mask of (probably) /24 it knows it can forward the frames directly to the Synology device (10.250.212.145).</p><p><strong>Possible solution:</strong> Please check if the netmask of the Mac is set to a different value than it should be on your network (i.e. /25 versus /24).</p><p>BTW: This does <strong>not</strong> explain why the MAC address of the Synology changes from 00:11:32:20:59:f7 to 00:11:32:20:59:<strong>f9</strong> in frame 1186!?! Maybe there is a second Synology with the same IP address and you did not capture the ARP update, or maybe the same Synology has two interfaces connected to the LAN (for redundancy).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '13, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '13, 15:34</strong> </span></p></div></div><div id="comments-container-26827" class="comments-container"><span id="26847"></span><div id="comment-26847" class="comment"><div id="post-26847-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much Kurt, the subnet mask is /20 which is what our internal subnet mask is so that's good but I still think there is an issue from the AP to the router. You are correct about the Synology having multiple interfaces connected to the LAN, the first MAC listed is two bonded LAN interfaces and the second is not bonded. There are 4 total LAN interfaces.</p></div><div id="comment-26847-info" class="comment-info"><span class="comment-age">(11 Nov '13, 08:30)</span> <span class="comment-user userinfo">clarsen</span></div></div><span id="26883"></span><div id="comment-26883" class="comment"><div id="post-26883-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but I still think there is an issue from the AP to the router.</p></blockquote><p>Maybe. Can you please add some information about the AP (brand, model) and who you attached it to the network. Is the 'AP' working as a AP or as a wireless router (based on the MAC addresses in the capture file, I guess it's a pure AP, but you never know until you check ;-))</p></div><div id="comment-26883-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26827" class="comment-tools"></div><div class="clear"></div><div id="comment-26827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

