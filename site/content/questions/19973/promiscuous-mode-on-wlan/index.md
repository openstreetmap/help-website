+++
type = "question"
title = "promiscuous mode on WLAN"
description = '''Dear all, I&#x27;m encountering the following problem. I&#x27;m trying to run promiscuous mode on the standard network adapter on the macbook air running Mountain Lion. As you well know, MBAir does not have a LAN input thus the capture mode should always work over wifi. The issue is that I ONLY capture the pa...'''
date = "2013-03-31T10:39:00Z"
lastmod = "2013-03-31T11:42:00Z"
weight = 19973
keywords = [ "capture", "promiscuous", "wlan", "mode", "monitor" ]
aliases = [ "/questions/19973" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [promiscuous mode on WLAN](/questions/19973/promiscuous-mode-on-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19973-score" class="post-score" title="current number of votes">0</div><span id="post-19973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>I'm encountering the following problem. I'm trying to run promiscuous mode on the standard network adapter on the macbook air running Mountain Lion. As you well know, MBAir does not have a LAN input thus the capture mode should always work over wifi. The issue is that I ONLY capture the packets from the localhost and thus none of the packets of the rest of IPs from the same network. I tried to run on "monitor mode" but I cannot properly check none of the HTTP.REQUESTS nor I can I do appropriate cookie analysis. I'm testing a web service in a MAMP server installed in the same network but can't see the none of the interaction.</p><p>Does anyone know what may be the issue here?</p><p>Thank you and best regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '13, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/9a7b3d90ed1b30fa51b052416705e80d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monkey&#39;s gravatar image" /><p><span>monkey</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monkey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Mar '13, 11:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19973" class="comments-container"></div><div id="comment-tools-19973" class="comment-tools"></div><div class="clear"></div><div id="comment-19973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19974"></span>

<div id="answer-container-19974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19974-score" class="post-score" title="current number of votes">1</div><span id="post-19974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The issues is that you're probably on a "protected", i.e. encrypted, Wi-Fi network.</p><p>On a wired LAN, there's normally no link-layer encryption, so if you can capture the traffic (which might involve more than just promiscuous mode, e.g. a "mirrored port" on a switch), the network analyzer can dissect it past the link layer.</p><p>On a wireless LAN, there's often link-layer encryption, i.e. WEP or WPA/WPA2, so, even if you could capture the traffic, you would, at best, only be able to dissect traffic to and from your own machine without having the password for the WLAN <em>and</em>, if WPA or WPA2 is being used, the initial setup packets for the other machines. See the <a href="http://wiki.wireshark.org/HowToDecrypt802.11">how to decrypt 802.11</a> page on the Wireshark Wiki for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '13, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19974" class="comments-container"></div><div id="comment-tools-19974" class="comment-tools"></div><div class="clear"></div><div id="comment-19974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

