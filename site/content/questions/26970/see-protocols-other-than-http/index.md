+++
type = "question"
title = "See protocols other than http"
description = '''I am looking to view the https from other computers connected to my network through an ethernet connection. It is showing other protocols such as udp, ssdp, and other random ones. I can view my https though. Anyone know how to fix this?'''
date = "2013-11-13T15:02:00Z"
lastmod = "2013-11-13T18:08:00Z"
weight = 26970
keywords = [ "ethernet", "http", "protocol" ]
aliases = [ "/questions/26970" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [See protocols other than http](/questions/26970/see-protocols-other-than-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26970-score" class="post-score" title="current number of votes">0</div><span id="post-26970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking to view the https from other computers connected to my network through an ethernet connection. It is showing other protocols such as udp, ssdp, and other random ones. I can view my https though. Anyone know how to fix this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '13, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/9837943c9432cc23c03847de491ab816?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brad&#39;s gravatar image" /><p><span>brad</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brad has no accepted answers">0%</span></p></div></div><div id="comments-container-26970" class="comments-container"></div><div id="comment-tools-26970" class="comment-tools"></div><div class="clear"></div><div id="comment-26970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26973"></span>

<div id="answer-container-26973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26973-score" class="post-score" title="current number of votes">0</div><span id="post-26973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume "other computers connected to my network through an ethernet connection" means your network is an Ethernet network rather than a Wi-Fi network.</p><p>If so, then you would need to capture in promiscuous mode, <em>and</em>, if you have a switched network, follow <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">the Wireshark Wiki directions for setting up the switch to see all traffic flowing through it</a>, <em>if</em> your switch supports that. (If it doesn't, you're out of luck.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '13, 17:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26973" class="comments-container"><span id="26974"></span><div id="comment-26974" class="comment"><div id="post-26974-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry I'm confused how to set up this switch. I don't see where it explains that anywhere. If you could explain to me how to set up the switch I would appreciate it.</p></div><div id="comment-26974-info" class="comment-info"><span class="comment-age">(13 Nov '13, 18:03)</span> <span class="comment-user userinfo">brad</span></div></div><span id="26975"></span><div id="comment-26975" class="comment"><div id="post-26975-score" class="comment-score"></div><div class="comment-text"><p>Whether you can set it up at all, and how it would be done if it's possible, would depend on the switch. See <a href="http://wiki.wireshark.org/SwitchReference">the Wireshark Wiki switch reference</a> for some models of switch.</p></div><div id="comment-26975-info" class="comment-info"><span class="comment-age">(13 Nov '13, 18:08)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-26973" class="comment-tools"></div><div class="clear"></div><div id="comment-26973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

