+++
type = "question"
title = "missing transmitted packets"
description = '''I collected the tftp traces at the source network interface using wireshark while downloading a software to destination. When I analysed the TFTP traces I could see missing transmitted packets from the source but could see acknowledgement from the destination. Why is that? Why it couldn&#x27;t capture th...'''
date = "2013-09-12T20:59:00Z"
lastmod = "2013-09-19T11:19:00Z"
weight = 24621
keywords = [ "tftp", "missing" ]
aliases = [ "/questions/24621" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [missing transmitted packets](/questions/24621/missing-transmitted-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24621-score" class="post-score" title="current number of votes">0</div><span id="post-24621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I collected the tftp traces at the source network interface using wireshark while downloading a software to destination. When I analysed the TFTP traces I could see missing transmitted packets from the source but could see acknowledgement from the destination. Why is that? Why it couldn't capture the transmitted packets? Is there any thing wrong in the setting? Are the transmitted packets too fast to capture? If so is it possible to capture these packets by modifying any parameters on the wireshark?Please reply.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tftp" rel="tag" title="see questions tagged &#39;tftp&#39;">tftp</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '13, 20:59</strong></p><img src="https://secure.gravatar.com/avatar/31cf42af6fe0b3d1e1d900e619cbf9c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nsrikant&#39;s gravatar image" /><p><span>nsrikant</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nsrikant has no accepted answers">0%</span></p></div></div><div id="comments-container-24621" class="comments-container"><span id="24625"></span><div id="comment-24625" class="comment"><div id="post-24625-score" class="comment-score"></div><div class="comment-text"><p>Is this a wired or wireless connection?</p></div><div id="comment-24625-info" class="comment-info"><span class="comment-age">(13 Sep '13, 00:16)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-24621" class="comment-tools"></div><div class="clear"></div><div id="comment-24621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24963"></span>

<div id="answer-container-24963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24963-score" class="post-score" title="current number of votes">0</div><span id="post-24963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>Why is that?</em> If the ACK is present, then the capture machine must have dropped packets (or the missing packets were sent on another interface, but that's unlikely).</p><p><em>Why it couldn't capture the transmitted packets?</em> Could be several reasons.</p><p><em>Is there any thing wrong in the setting?</em> What setting?</p><p><em>Are the transmitted packets too fast to capture?</em> Probably not, since each block is acknowledged so the round-trip latency dictates the transmission rate. But how fast is the sender transmitting?</p><p><em>If so is it possible to capture these packets by modifying any parameters on the wireshark?</em> Try taking a look at the information provided at the <a href="http://wiki.wireshark.org/Performance">Wireshark Performance wiki page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '13, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24963" class="comments-container"></div><div id="comment-tools-24963" class="comment-tools"></div><div class="clear"></div><div id="comment-24963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

