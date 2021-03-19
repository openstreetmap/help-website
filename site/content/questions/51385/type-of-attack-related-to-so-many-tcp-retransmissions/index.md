+++
type = "question"
title = "Type of attack related to so many TCP Retransmissions"
description = '''I am analysing an attack capture with Wireshark and am having some trouble identifying the type of attack that this one is. I am guessing it may be a DDoS attack since there are many TCP Retransmissions but I am not quite sure. Can someone with more experience clarify me? '''
date = "2016-04-03T10:40:00Z"
lastmod = "2016-04-03T15:25:00Z"
weight = 51385
keywords = [ "attack", "tcp-retransmit" ]
aliases = [ "/questions/51385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Type of attack related to so many TCP Retransmissions](/questions/51385/type-of-attack-related-to-so-many-tcp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51385-score" class="post-score" title="current number of votes">0</div><span id="post-51385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analysing an attack capture with Wireshark and am having some trouble identifying the type of attack that this one is.</p><p>I am guessing it may be a DDoS attack since there are many TCP Retransmissions but I am not quite sure.</p><p>Can someone with more experience clarify me?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/fdgfhgfh_AnRsSBR.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-attack" rel="tag" title="see questions tagged &#39;attack&#39;">attack</span> <span class="post-tag tag-link-tcp-retransmit" rel="tag" title="see questions tagged &#39;tcp-retransmit&#39;">tcp-retransmit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '16, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/0638835dc95bc1f5f9435471815300bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twistedx&#39;s gravatar image" /><p><span>twistedx</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twistedx has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51385" class="comments-container"></div><div id="comment-tools-51385" class="comment-tools"></div><div class="clear"></div><div id="comment-51385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51387"></span>

<div id="answer-container-51387" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51387-score" class="post-score" title="current number of votes">1</div><span id="post-51387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks pretty normal to me, except for the duplicate frames in the trace. You'll need to deduplicate the file first, see <a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '16, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-51387" class="comments-container"><span id="51388"></span><div id="comment-51388" class="comment"><div id="post-51388-score" class="comment-score"></div><div class="comment-text"><p>I will take a look at that. But now I was thinking that this can have something to do with a SMB Flow attack. What do you think about that?</p></div><div id="comment-51388-info" class="comment-info"><span class="comment-age">(03 Apr '16, 15:25)</span> <span class="comment-user userinfo">twistedx</span></div></div></div><div id="comment-tools-51387" class="comment-tools"></div><div class="clear"></div><div id="comment-51387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

