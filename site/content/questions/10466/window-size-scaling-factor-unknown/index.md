+++
type = "question"
title = "Window size scaling factor unknown?"
description = '''I have noticed some strange packets with the &quot;Window size scaling factor: -1 (unknown)&quot;. Is this a buffer full problem? I am seeing this on both the source and destination intermittently. Thanks for your help in advance,'''
date = "2012-04-26T11:30:00Z"
lastmod = "2012-04-26T11:40:00Z"
weight = 10466
keywords = [ "scaling", "factor" ]
aliases = [ "/questions/10466" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Window size scaling factor unknown?](/questions/10466/window-size-scaling-factor-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10466-score" class="post-score" title="current number of votes">0</div><span id="post-10466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have noticed some strange packets with the "Window size scaling factor: -1 (unknown)". Is this a buffer full problem? I am seeing this on both the source and destination intermittently.</p><p>Thanks for your help in advance,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-scaling" rel="tag" title="see questions tagged &#39;scaling&#39;">scaling</span> <span class="post-tag tag-link-factor" rel="tag" title="see questions tagged &#39;factor&#39;">factor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '12, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/a8c012ef0ff5075fe9f6e7484d3bba0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arpsalot&#39;s gravatar image" /><p><span>arpsalot</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arpsalot has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '12, 14:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-10466" class="comments-container"></div><div id="comment-tools-10466" class="comment-tools"></div><div class="clear"></div><div id="comment-10466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10467"></span>

<div id="answer-container-10467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10467-score" class="post-score" title="current number of votes">1</div><span id="post-10467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It just means that Wireshark doesn't KNOW the scale factor, most likely because it hasn't seen the SYN / SYN/ACK packets (where the options are negotiated). -1 is an artifical value meaning "unknown". So no, it is not a buffer full problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '12, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10467" class="comments-container"></div><div id="comment-tools-10467" class="comment-tools"></div><div class="clear"></div><div id="comment-10467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

