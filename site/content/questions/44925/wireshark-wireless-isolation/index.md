+++
type = "question"
title = "wireshark wireless isolation"
description = '''I want to find out if wireshark can be used to confirm if wireless isolation has been implemented on a router or acess point.'''
date = "2015-08-07T09:34:00Z"
lastmod = "2015-08-07T10:36:00Z"
weight = 44925
keywords = [ "wireless", "isolation" ]
aliases = [ "/questions/44925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark wireless isolation](/questions/44925/wireshark-wireless-isolation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44925-score" class="post-score" title="current number of votes">0</div><span id="post-44925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to find out if wireshark can be used to confirm if wireless isolation has been implemented on a router or acess point.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-isolation" rel="tag" title="see questions tagged &#39;isolation&#39;">isolation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '15, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/e9c4aae7a45293db913d0493c1211dbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kofi%20Ntim&#39;s gravatar image" /><p><span>Kofi Ntim</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kofi Ntim has no accepted answers">0%</span></p></div></div><div id="comments-container-44925" class="comments-container"></div><div id="comment-tools-44925" class="comment-tools"></div><div class="clear"></div><div id="comment-44925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44926"></span>

<div id="answer-container-44926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44926-score" class="post-score" title="current number of votes">0</div><span id="post-44926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireless isolation typically stops two computers on the wireless network from seeing each other, but still allows the wireless clients to access the wired network. This is done within the AP or wireless router, similar to a firewall rule. NOTE I said similar to a firewall rule.</p><p>The process works something like this:</p><ol><li>Packet is received by AP over the wireless interface</li><li>Bridging subsystem examines packet for destination MAC</li><li>If destination MAC exists on wireless interface, then drop</li><li>Otherwise forward the packet via wired interface</li></ol><p>Since all wireless clients have to connect to the AP for communication, the AP's switching table is aware of all the client's MAC address. Therefore the logic of whether to drop a frame exists within the AP.</p><p>The AP/wireless router does not advertise this "feature" in any WiFi frames (such as Beacons). However, you can try to ping another wireless client. Just make sure that all firewalls are disabled on both clients. Windows likes to block ping requests.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '15, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44926" class="comments-container"></div><div id="comment-tools-44926" class="comment-tools"></div><div class="clear"></div><div id="comment-44926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

