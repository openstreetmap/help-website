+++
type = "question"
title = "Only seeing broadcast and arp traffic on a mirrored port"
description = '''I have a Network Video Recorder connected to an IP camera on a Cisco 3750 switch. I wanted to sniff the traffic between the recorder and the camera so I mirrored (using SPAN) the camera port (FA1/0/23) to my PC port (FA1/0/9). Then I run wireshark on my PC in promiscuous mode expected to capture all...'''
date = "2015-10-13T10:28:00Z"
lastmod = "2015-10-13T10:55:00Z"
weight = 46502
keywords = [ "port", "mirroring" ]
aliases = [ "/questions/46502" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Only seeing broadcast and arp traffic on a mirrored port](/questions/46502/only-seeing-broadcast-and-arp-traffic-on-a-mirrored-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46502-score" class="post-score" title="current number of votes">0</div><span id="post-46502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Network Video Recorder connected to an IP camera on a Cisco 3750 switch. I wanted to sniff the traffic between the recorder and the camera so I mirrored (using SPAN) the camera port (FA1/0/23) to my PC port (FA1/0/9). Then I run wireshark on my PC in promiscuous mode expected to capture all packets between the recorder and the camera but all I see is arp and broadcast traffic!! Based on the activity led, there's lot of traffic on the mirrored port but nothing is being captured by wireshark. What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-mirroring" rel="tag" title="see questions tagged &#39;mirroring&#39;">mirroring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/1fa50f89ad089605082159ef07806f43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dyue&#39;s gravatar image" /><p><span>dyue</span><br />
<span class="score" title="45 reputation points">45</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dyue has one accepted answer">100%</span></p></div></div><div id="comments-container-46502" class="comments-container"></div><div id="comment-tools-46502" class="comment-tools"></div><div class="clear"></div><div id="comment-46502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46503"></span>

<div id="answer-container-46503" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46503-score" class="post-score" title="current number of votes">1</div><span id="post-46503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kurt Knochner has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you for those who viewed this question but I found the answer within these thousands of posted answers. It turned out that I had left my antivirus and firewall on the PC I was using. Disable Bitdefender and now I am seeing everything.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/1fa50f89ad089605082159ef07806f43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dyue&#39;s gravatar image" /><p><span>dyue</span><br />
<span class="score" title="45 reputation points">45</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dyue has one accepted answer">100%</span></p></div></div><div id="comments-container-46503" class="comments-container"></div><div id="comment-tools-46503" class="comment-tools"></div><div class="clear"></div><div id="comment-46503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

