+++
type = "question"
title = "How to cut short the packet size when capturing using Tshark"
description = '''Hi, I have a question regarding cutting the bigger packet length to desired value when using tshark for capture.  We run very high traffic tests and the packet size would be 16k,8K. I want to know is there is any flag available to cut the payload of a big wireless packet using Tshark. Thank you for ...'''
date = "2014-09-19T14:30:00Z"
lastmod = "2014-09-19T16:58:00Z"
weight = 36472
keywords = [ "tshark" ]
aliases = [ "/questions/36472" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to cut short the packet size when capturing using Tshark](/questions/36472/how-to-cut-short-the-packet-size-when-capturing-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36472-score" class="post-score" title="current number of votes">0</div><span id="post-36472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a question regarding cutting the bigger packet length to desired value when using tshark for capture. We run very high traffic tests and the packet size would be 16k,8K. I want to know is there is any flag available to cut the payload of a big wireless packet using Tshark. Thank you for answering my question.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '14, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/effe6282f37b078757e6044218fa2a4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mukkapati9&#39;s gravatar image" /><p><span>mukkapati9</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mukkapati9 has no accepted answers">0%</span></p></div></div><div id="comments-container-36472" class="comments-container"></div><div id="comment-tools-36472" class="comment-tools"></div><div class="clear"></div><div id="comment-36472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36474"></span>

<div id="answer-container-36474" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36474-score" class="post-score" title="current number of votes">0</div><span id="post-36474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the -s (snap length) parameter to limit the amount of bytes you want to store to disk per packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '14, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36474" class="comments-container"><span id="36475"></span><div id="comment-36475" class="comment"><div id="post-36475-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply. I will try it.</p></div><div id="comment-36475-info" class="comment-info"><span class="comment-age">(19 Sep '14, 16:58)</span> <span class="comment-user userinfo">mukkapati9</span></div></div></div><div id="comment-tools-36474" class="comment-tools"></div><div class="clear"></div><div id="comment-36474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

