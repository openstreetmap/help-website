+++
type = "question"
title = "Help with &quot;NOT&quot; display filter"
description = '''Hello,  Sorry I&#x27;m a bit rusty and have tried a few expressions but I need to filter traffic on these 2 subnets but exclude IPs 192.168.138.33 and 192.168.138.34 ip.addr==192.168.138.0/24 || ip.addr==192.168.115.0/24 not ip.addr eq 192.168.138.34 not ip.addr eq 192.168.138.33 This above isn&#x27;t working...'''
date = "2015-09-22T04:22:00Z"
lastmod = "2015-09-22T15:01:00Z"
weight = 46048
keywords = [ "not", "display-filter" ]
aliases = [ "/questions/46048" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help with "NOT" display filter](/questions/46048/help-with-not-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46048-score" class="post-score" title="current number of votes">0</div><span id="post-46048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Sorry I'm a bit rusty and have tried a few expressions but I need to filter traffic on these 2 subnets but exclude IPs 192.168.138.33 and 192.168.138.34</p><p>ip.addr==192.168.138.0/24 || ip.addr==192.168.115.0/24 not ip.addr eq 192.168.138.34 not ip.addr eq 192.168.138.33</p><p>This above isn't working, what have I missed?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '15, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/09e8dc62bc7c0b2a6d62edf9aebb8707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gonzo&#39;s gravatar image" /><p><span>gonzo</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gonzo has no accepted answers">0%</span></p></div></div><div id="comments-container-46048" class="comments-container"><span id="46068"></span><div id="comment-46068" class="comment"><div id="post-46068-score" class="comment-score"></div><div class="comment-text"><p>The <code>&amp;&amp;</code> operator (and some parentheses) as per Jim Aragon's answer.</p></div><div id="comment-46068-info" class="comment-info"><span class="comment-age">(22 Sep '15, 15:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-46048" class="comment-tools"></div><div class="clear"></div><div id="comment-46048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46049"></span>

<div id="answer-container-46049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46049-score" class="post-score" title="current number of votes">1</div><span id="post-46049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(ip.addr==192.168.138.0/24 || ip.addr==192.168.115.0/24) &amp;&amp; (not ip.addr==192.168.138.34 &amp;&amp; not ip.addr==192.168.138.33)</p><p>The change from "eq" to "==" in the second part of the filter is strictly cosmetic, to agree with your use in the first part. Either version of the operator can be used interchangeably.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '15, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-46049" class="comments-container"></div><div id="comment-tools-46049" class="comment-tools"></div><div class="clear"></div><div id="comment-46049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

