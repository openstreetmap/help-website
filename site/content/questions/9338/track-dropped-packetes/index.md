+++
type = "question"
title = "Track dropped packetes"
description = '''I have two pcaps taken one at the ingress of the device and the other at the egress. The device seems to be dropping the udp packets. The packets have an identification of all 0s Is there a way I can track what packets are missing in the packets at the output.'''
date = "2012-03-03T22:31:00Z"
lastmod = "2012-03-04T03:15:00Z"
weight = 9338
keywords = [ "identification", "packet" ]
aliases = [ "/questions/9338" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Track dropped packetes](/questions/9338/track-dropped-packetes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9338-score" class="post-score" title="current number of votes">0</div><span id="post-9338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two pcaps taken one at the ingress of the device and the other at the egress. The device seems to be dropping the udp packets. The packets have an identification of all 0s Is there a way I can track what packets are missing in the packets at the output.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-identification" rel="tag" title="see questions tagged &#39;identification&#39;">identification</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '12, 22:31</strong></p><img src="https://secure.gravatar.com/avatar/6151b7c8c2a16f622de7c8c7edfda74a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet&#39;s gravatar image" /><p><span>Packet</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet has no accepted answers">0%</span></p></div></div><div id="comments-container-9338" class="comments-container"></div><div id="comment-tools-9338" class="comment-tools"></div><div class="clear"></div><div id="comment-9338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9340"></span>

<div id="answer-container-9340" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9340-score" class="post-score" title="current number of votes">0</div><span id="post-9340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on the way the device alters the packets.</p><ul><li>If it just switches the packets at Layer-2, then the frames will be exactly the same on the ingress and the egress port. In this case you can use wireshark to generate a MD5 hash on each packet and compare those.</li><li>When the packets are routed and or natted, then you can compare the length of the packets and maybe the first couple of bytes from the payload. This will work well when there is no packet re-ordering in the device</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '12, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9340" class="comments-container"></div><div id="comment-tools-9340" class="comment-tools"></div><div class="clear"></div><div id="comment-9340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

