+++
type = "question"
title = "wireshark Ethernet conversation statistics"
description = '''Can somebody help me out in understanding the statistics for the conversation for Ethernet in Wireshark. I have a Cisco_2d:fa:22 as Address A and Cisco_4d:f3:11 as Address B. So it looks like it is the ID for the Cisco device. I see their MAC addresses in the Ethernet section in Wireshark. But in th...'''
date = "2014-02-26T20:18:00Z"
lastmod = "2014-02-27T00:43:00Z"
weight = 30223
keywords = [ "conversation", "statistics" ]
aliases = [ "/questions/30223" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark Ethernet conversation statistics](/questions/30223/wireshark-ethernet-conversation-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30223-score" class="post-score" title="current number of votes">0</div><span id="post-30223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can somebody help me out in understanding the statistics for the conversation for Ethernet in Wireshark. I have a Cisco_2d:fa:22 as Address A and Cisco_4d:f3:11 as Address B. So it looks like it is the ID for the Cisco device. I see their MAC addresses in the Ethernet section in Wireshark. But in the IP section, the source and destination IP addresses keep changing from one packet to another. I'm not sure I understand that. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '14, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/4bf9a4681570406f873b404a912f2a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="character9&#39;s gravatar image" /><p><span>character9</span><br />
<span class="score" title="16 reputation points">16</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="character9 has no accepted answers">0%</span></p></div></div><div id="comments-container-30223" class="comments-container"></div><div id="comment-tools-30223" class="comment-tools"></div><div class="clear"></div><div id="comment-30223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30226"></span>

<div id="answer-container-30226" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30226-score" class="post-score" title="current number of votes">0</div><span id="post-30226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The two Cisco addresses <strong>are</strong> their MAC addresses; Wireshark just replaces the first three bytes (the vendor specific ones) with the vendor name. The names are taken from the "manuf" file found in the Wireshark installation directory.</p><p>Regarding the IP addresses: both devices are probably routers, which means that they forward IP packets for other systems. The IPs that you observe are the end node IP addresses, and it is quite typical that you see a lot of different IP addresses. You should probably read up a bit about how routing works ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30226" class="comments-container"></div><div id="comment-tools-30226" class="comment-tools"></div><div class="clear"></div><div id="comment-30226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

