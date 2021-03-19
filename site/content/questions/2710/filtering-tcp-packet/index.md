+++
type = "question"
title = "filtering tcp packet"
description = '''I want to open an static web page and run wireshark. How can I filter the last packet which comes form that page? Is it true to use tcp.flag.fin?'''
date = "2011-03-07T23:12:00Z"
lastmod = "2011-03-08T15:44:00Z"
weight = 2710
keywords = [ "flag" ]
aliases = [ "/questions/2710" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filtering tcp packet](/questions/2710/filtering-tcp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2710-score" class="post-score" title="current number of votes">0</div><span id="post-2710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to open an static web page and run wireshark. How can I filter the last packet which comes form that page? Is it true to use tcp.flag.fin?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flag" rel="tag" title="see questions tagged &#39;flag&#39;">flag</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '11, 23:12</strong></p><img src="https://secure.gravatar.com/avatar/0d1f835bfa8cc91838057ef65fc4d1c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A%20B&#39;s gravatar image" /><p><span>A B</span><br />
<span class="score" title="1 reputation points">1</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A B has no accepted answers">0%</span></p></div></div><div id="comments-container-2710" class="comments-container"></div><div id="comment-tools-2710" class="comment-tools"></div><div class="clear"></div><div id="comment-2710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2714"></span>

<div id="answer-container-2714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2714-score" class="post-score" title="current number of votes">3</div><span id="post-2714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It could be using the fin bit, in which case you'd filter for <code>tcp.flags.fin==1</code>. Or it might use a reset flag, which would be filtered using <code>tcp.flags.reset==1</code>. Or both together, just to be sure: <code>tcp.flags.fin==1 or tcp.flags.reset==1</code>.</p><p>My approach would be slightly different than yours though: I'd search for the URL of the "GET" request (if it's not easy to spot right away), and then use the popup menu "Conversation Filter -&gt; TCP". That way you get the whole communication, including the last packet, which is very easy to jump to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '11, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2714" class="comments-container"><span id="2716"></span><div id="comment-2716" class="comment"><div id="post-2716-score" class="comment-score"></div><div class="comment-text"><p>Thanks,so helpful answer.</p></div><div id="comment-2716-info" class="comment-info"><span class="comment-age">(08 Mar '11, 15:44)</span> <span class="comment-user userinfo">A B</span></div></div></div><div id="comment-tools-2714" class="comment-tools"></div><div class="clear"></div><div id="comment-2714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

