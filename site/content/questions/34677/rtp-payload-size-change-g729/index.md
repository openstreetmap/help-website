+++
type = "question"
title = "Rtp payload Size change G729"
description = '''By observing a VoIP connection I realized that the payload size is varying size. When the value is 60 is a comfort noise, when the value is 74 has voice. But what if the value is 66? '''
date = "2014-07-15T12:24:00Z"
lastmod = "2014-07-15T14:06:00Z"
weight = 34677
keywords = [ "g729", "rtp", "payload" ]
aliases = [ "/questions/34677" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rtp payload Size change G729](/questions/34677/rtp-payload-size-change-g729)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34677-score" class="post-score" title="current number of votes">0</div><span id="post-34677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>By observing a VoIP connection I realized that the payload size is varying size. When the value is 60 is a comfort noise, when the value is 74 has voice. But what if the value is 66? <img src="https://osqa-ask.wireshark.org/upfiles/rtp_payload.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g729" rel="tag" title="see questions tagged &#39;g729&#39;">g729</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/a79d778ac3ee711846e97e458ffa6964?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="julius&#39;s gravatar image" /><p><span>julius</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="julius has no accepted answers">0%</span></p></img></div></div><div id="comments-container-34677" class="comments-container"><span id="34686"></span><div id="comment-34686" class="comment"><div id="post-34686-score" class="comment-score"></div><div class="comment-text"><p>You'd probably need to read the g.729 specification to find out.</p></div><div id="comment-34686-info" class="comment-info"><span class="comment-age">(15 Jul '14, 12:58)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="34689"></span><div id="comment-34689" class="comment"><div id="post-34689-score" class="comment-score"></div><div class="comment-text"><p>Anders i read the rfc but it says that the payload can be 10 20 30 40 bytes.</p></div><div id="comment-34689-info" class="comment-info"><span class="comment-age">(15 Jul '14, 13:07)</span> <span class="comment-user userinfo">julius</span></div></div><span id="34692"></span><div id="comment-34692" class="comment"><div id="post-34692-score" class="comment-score"></div><div class="comment-text"><p>The sizes in the codec specs (which G.729 is) are usually the codec payload size, not including the headers for RTP, UDP, IP, etc. Also, are you sure it isn't specifying 10/20/30/40 packetization audio sample size (i.e., ptime in milliseconds, instead of encoded packet length)?</p></div><div id="comment-34692-info" class="comment-info"><span class="comment-age">(15 Jul '14, 14:06)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-34677" class="comment-tools"></div><div class="clear"></div><div id="comment-34677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

