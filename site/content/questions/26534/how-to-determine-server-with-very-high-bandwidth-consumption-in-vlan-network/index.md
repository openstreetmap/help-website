+++
type = "question"
title = "How to determine server with very high bandwidth consumption in VLAN network."
description = '''Wireshark is very helpful in terms of troubleshooting network. I have encountered one time an intermittent connection over my network. I begin troubleshooting from top to toe but I can not find the source of problem. We&#x27;re using fortigate firewall and I trace the source of problem by looking to fort...'''
date = "2013-10-30T04:51:00Z"
lastmod = "2013-10-31T03:47:00Z"
weight = 26534
keywords = [ "bandwidth", "vlan", "wireshark" ]
aliases = [ "/questions/26534" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to determine server with very high bandwidth consumption in VLAN network.](/questions/26534/how-to-determine-server-with-very-high-bandwidth-consumption-in-vlan-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26534-score" class="post-score" title="current number of votes">0</div><span id="post-26534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark is very helpful in terms of troubleshooting network. I have encountered one time an intermittent connection over my network. I begin troubleshooting from top to toe but I can not find the source of problem. We're using fortigate firewall and I trace the source of problem by looking to fortigate monitoring where you can view server with more bandwidth used. I wonder why wireshark can't trace other activity in vlan network. I run wireshark in a server that connected in Vlan 12 (192.168.12.x)and other server is connected in Vlan 16 (192.168.16.x) with high bandwidth consumption. Why is it that wireshark can't monitor or sniff other vlan's and show only results that connected in vlan 12(192.168.12.x)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '13, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/a42962da254360f0bfc5fd52402789f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rayden&#39;s gravatar image" /><p><span>rayden</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rayden has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Oct '13, 07:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-26534" class="comments-container"></div><div id="comment-tools-26534" class="comment-tools"></div><div class="clear"></div><div id="comment-26534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26573"></span>

<div id="answer-container-26573" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26573-score" class="post-score" title="current number of votes">0</div><span id="post-26573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why is it that wireshark can't monitor or sniff other vlan's and show only results that connected in vlan 12(192.168.12.x)?</p></blockquote><p>because the purpose of VLANs is to <strong>separate networks</strong> from each other!?!</p><p>So, it's not Wireshark that is unable to capture the traffic, it's your switch that does not send any VLAN16 traffic into VLAN12!</p><p>You need to <strong>activate port mirroring</strong> on your switch and mirror the traffic of VLAN16 to the port of your Wireshark system (should <strong>not</strong> be a productive system, as it might get flooded with that traffic!!).</p><p>Here is a brief overview how to enable port mirroring for some switches: <a href="http://wiki.wireshark.org/SwitchReference">http://wiki.wireshark.org/SwitchReference</a><br />
</p><p>Please also read this: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch</a></p><p>BTW: Besides capturing (and analyzing) the traffic with Wireshark, you can simply check the port statistics of your switch to identify the system with 'very high bandwidth consumption'. If you just need to find the system, that's the way to go. If you need to know <strong>what</strong> that system sends and receives, you need Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '13, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Oct '13, 04:06</strong> </span></p></div></div><div id="comments-container-26573" class="comments-container"></div><div id="comment-tools-26573" class="comment-tools"></div><div class="clear"></div><div id="comment-26573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

