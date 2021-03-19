+++
type = "question"
title = "Wireshark error with &quot;TCP Acked unseen segment&quot;?"
description = '''Hey, I&#x27;ve got a question about the message &quot;TCP Acked unseen segment&quot;. We made a trace and we&#x27;ve got this message, but the segment was traced also. So could there be a bug with Wireshark? The trace is saved on cloudshark: http://www.cloudshark.org/captures/a47e3794dd1a Thanks for your help! Best reg...'''
date = "2013-02-26T04:36:00Z"
lastmod = "2013-02-27T00:03:00Z"
weight = 18877
keywords = [ "unseen_segment", "bug" ]
aliases = [ "/questions/18877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark error with "TCP Acked unseen segment"?](/questions/18877/wireshark-error-with-tcp-acked-unseen-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18877-score" class="post-score" title="current number of votes">0</div><span id="post-18877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I've got a question about the message "TCP Acked unseen segment". We made a trace and we've got this message, but the segment was traced also. So could there be a bug with Wireshark?</p><p>The trace is saved on cloudshark: <a href="http://www.cloudshark.org/captures/a47e3794dd1a">http://www.cloudshark.org/captures/a47e3794dd1a</a></p><p>Thanks for your help!</p><p>Best regards, dranigl</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unseen_segment" rel="tag" title="see questions tagged &#39;unseen_segment&#39;">unseen_segment</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '13, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/128b142c3a9292444f555b1aad741960?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dranigl&#39;s gravatar image" /><p><span>dranigl</span><br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dranigl has no accepted answers">0%</span></p></div></div><div id="comments-container-18877" class="comments-container"></div><div id="comment-tools-18877" class="comment-tools"></div><div class="clear"></div><div id="comment-18877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18878"></span>

<div id="answer-container-18878" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18878-score" class="post-score" title="current number of votes">1</div><span id="post-18878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like a wireshark bug indeed. Frame 9 is a retransmission of frame 8, but with new data atached to it. It looks like wireshark does not update its pointers correctly in this case.</p><p>You can see this more clearly when you "ignore" frame 8 (Edit -&gt; Ignore packet), then the ACK acks all received data and there is no expert message.</p><p>Could you file a bug report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '13, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18878" class="comments-container"><span id="18911"></span><div id="comment-18911" class="comment"><div id="post-18911-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer! Yes I'll file a bug report</p></div><div id="comment-18911-info" class="comment-info"><span class="comment-age">(27 Feb '13, 00:03)</span> <span class="comment-user userinfo">dranigl</span></div></div></div><div id="comment-tools-18878" class="comment-tools"></div><div class="clear"></div><div id="comment-18878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

