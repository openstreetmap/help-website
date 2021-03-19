+++
type = "question"
title = "the filter ip.addr is not the sum of the two filters ip.src ip.dst"
description = '''Well, I was trying to compare some capture and I did find a strange, to me, condition. If I sum the number of packets of the filter ip.src and the number of packets of the filter ip.dst I&#x27;m not getting the same packet number of the filter ip.addr. After a deep analysis I&#x27;ve found that the filter ip....'''
date = "2012-02-07T00:13:00Z"
lastmod = "2012-02-08T13:35:00Z"
weight = 8868
keywords = [ "filter", "ip.addr", "ip.dst", "ip.src", "sum" ]
aliases = [ "/questions/8868" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [the filter ip.addr is not the sum of the two filters ip.src ip.dst](/questions/8868/the-filter-ipaddr-is-not-the-sum-of-the-two-filters-ipsrc-ipdst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8868-score" class="post-score" title="current number of votes">0</div><span id="post-8868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Well, I was trying to compare some capture and I did find a strange, to me, condition. If I sum the number of packets of the filter ip.src and the number of packets of the filter ip.dst I'm not getting the same packet number of the filter ip.addr. After a deep analysis I've found that the filter ip.src is including the icmp unreachable directed to the source (and not from!!) because in their payload the orginal source is really the ip.src. So far, I can't compare efficiently upstream and downstream packet number, because they're overlapping...any idea?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip.addr" rel="tag" title="see questions tagged &#39;ip.addr&#39;">ip.addr</span> <span class="post-tag tag-link-ip.dst" rel="tag" title="see questions tagged &#39;ip.dst&#39;">ip.dst</span> <span class="post-tag tag-link-ip.src" rel="tag" title="see questions tagged &#39;ip.src&#39;">ip.src</span> <span class="post-tag tag-link-sum" rel="tag" title="see questions tagged &#39;sum&#39;">sum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '12, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/04033cce5ba97ed6c1571ef7d9da092c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stefanor&#39;s gravatar image" /><p><span>stefanor</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stefanor has no accepted answers">0%</span></p></div></div><div id="comments-container-8868" class="comments-container"></div><div id="comment-tools-8868" class="comment-tools"></div><div class="clear"></div><div id="comment-8868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8869"></span>

<div id="answer-container-8869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8869-score" class="post-score" title="current number of votes">0</div><span id="post-8869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There you found a common problem, because even in statistics, that gets interesting when there are more packets in the different conversations compared to total packets in the trace file ;)</p><p>As a workaround I'd always specifically filter out certain ICMP types, because the ICMP "quotes" have that issue or go for filtering ip.src and MAC src/dst address in parallel, making sure you're only looking at packets from or to a certain workstation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '12, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Feb '12, 00:36</strong> </span></p></div></div><div id="comments-container-8869" class="comments-container"><span id="8911"></span><div id="comment-8911" class="comment"><div id="post-8911-score" class="comment-score"></div><div class="comment-text"><p>thanks Landi, I'm already filtering out all the ICMP for this reason... Maybe I'm too easy, but I'm not seeing the right behavior implementation as a hard task..</p></div><div id="comment-8911-info" class="comment-info"><span class="comment-age">(08 Feb '12, 13:35)</span> <span class="comment-user userinfo">stefanor</span></div></div></div><div id="comment-tools-8869" class="comment-tools"></div><div class="clear"></div><div id="comment-8869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

