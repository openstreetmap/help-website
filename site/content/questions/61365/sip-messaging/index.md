+++
type = "question"
title = "SIP Messaging"
description = '''I&#x27;m running a monitor session on a Cisco 7609, source gi1/1 to destination gi 1/13. My computer is connected to int gi1/13. I want to capture SIP messaging from this interface but can&#x27;t see it. I get DHCP, UDP, etc packets, but no SIP. What am I doing wrong'''
date = "2017-05-12T06:19:00Z"
lastmod = "2017-05-15T07:27:00Z"
weight = 61365
keywords = [ "sipcapture" ]
aliases = [ "/questions/61365" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SIP Messaging](/questions/61365/sip-messaging)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61365-score" class="post-score" title="current number of votes">0</div><span id="post-61365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running a monitor session on a Cisco 7609, source gi1/1 to destination gi 1/13. My computer is connected to int gi1/13. I want to capture SIP messaging from this interface but can't see it. I get DHCP, UDP, etc packets, but no SIP. What am I doing wrong</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sipcapture" rel="tag" title="see questions tagged &#39;sipcapture&#39;">sipcapture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '17, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/9a519eae13c270d27bce4d4a81891417?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blangham&#39;s gravatar image" /><p><span>blangham</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blangham has no accepted answers">0%</span></p></div></div><div id="comments-container-61365" class="comments-container"></div><div id="comment-tools-61365" class="comment-tools"></div><div class="clear"></div><div id="comment-61365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61366"></span>

<div id="answer-container-61366" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61366-score" class="post-score" title="current number of votes">0</div><span id="post-61366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Many SIP implementations use UDP/5060 but it is possible the SIP you are trying to capture is using a non-standard port. SIP can also run over TCP (typically only used in enterprises, and even then seldom) or TLS. If it's in TLS you won't be able to decode it unless you can get the keys.</p><p>Do you have a trace???</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '17, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/efd6c87b3ea03d76a316e1bc5cf19a07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbAtAffirmed&#39;s gravatar image" /><p><span>dbAtAffirmed</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbAtAffirmed has no accepted answers">0%</span></p></div></div><div id="comments-container-61366" class="comments-container"><span id="61405"></span><div id="comment-61405" class="comment"><div id="post-61405-score" class="comment-score"></div><div class="comment-text"><p>This ended up being a NIC card issue. My PC has a Realtek PCIe Gbe Family controller. My laptop has Broadcom NetLink Gigabit. There must be some settings int the Realtek that need changed to pass this traffic.</p></div><div id="comment-61405-info" class="comment-info"><span class="comment-age">(15 May '17, 07:27)</span> <span class="comment-user userinfo">blangham</span></div></div></div><div id="comment-tools-61366" class="comment-tools"></div><div class="clear"></div><div id="comment-61366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

