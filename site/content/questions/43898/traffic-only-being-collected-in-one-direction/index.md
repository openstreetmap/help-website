+++
type = "question"
title = "Traffic only being collected in one direction"
description = '''I have Wireshark running on a client PC and it is only collected traffic in one direction. I see responses from the remote device but not the client Wireshark is running on. I am using a host filter: host xxx.xxx.xxx.xxx or host xxx.xxx.xxx.xxx. I have promiscuous mode enabled and don&#x27;t have anythin...'''
date = "2015-07-06T11:37:00Z"
lastmod = "2015-07-07T12:03:00Z"
weight = 43898
keywords = [ "filter", "capture", "unidirectional" ]
aliases = [ "/questions/43898" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Traffic only being collected in one direction](/questions/43898/traffic-only-being-collected-in-one-direction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43898-score" class="post-score" title="current number of votes">0</div><span id="post-43898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark running on a client PC and it is only collected traffic in one direction. I see responses from the remote device but not the client Wireshark is running on. I am using a host filter: host xxx.xxx.xxx.xxx or host xxx.xxx.xxx.xxx. I have promiscuous mode enabled and don't have anything enabled which would block the traffic from the WS client. Any help you can provide would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-unidirectional" rel="tag" title="see questions tagged &#39;unidirectional&#39;">unidirectional</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '15, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/6d5eef8b4584208fd32aa2281ba38481?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snifferguy&#39;s gravatar image" /><p><span>snifferguy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snifferguy has no accepted answers">0%</span></p></div></div><div id="comments-container-43898" class="comments-container"></div><div id="comment-tools-43898" class="comment-tools"></div><div class="clear"></div><div id="comment-43898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43905"></span>

<div id="answer-container-43905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43905-score" class="post-score" title="current number of votes">0</div><span id="post-43905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the past this issue has been found to be due to AV, firewall or VPN endpoint software. Are you sure you don't have anything like that installed?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43905" class="comments-container"><span id="43935"></span><div id="comment-43935" class="comment"><div id="post-43935-score" class="comment-score"></div><div class="comment-text"><p>I'm checking and will get back to you. Thanks!</p></div><div id="comment-43935-info" class="comment-info"><span class="comment-age">(07 Jul '15, 08:02)</span> <span class="comment-user userinfo">snifferguy</span></div></div><span id="43937"></span><div id="comment-43937" class="comment"><div id="post-43937-score" class="comment-score"></div><div class="comment-text"><p>We tried it on a different machine and were able to get bi-directional data. We're still looking into why the other machine only captures one way. Thanks for your help.</p></div><div id="comment-43937-info" class="comment-info"><span class="comment-age">(07 Jul '15, 11:54)</span> <span class="comment-user userinfo">snifferguy</span></div></div><span id="43939"></span><div id="comment-43939" class="comment"><div id="post-43939-score" class="comment-score"></div><div class="comment-text"><p>Would be nice if you could post your final finding. So we all can learn from that.</p></div><div id="comment-43939-info" class="comment-info"><span class="comment-age">(07 Jul '15, 12:03)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-43905" class="comment-tools"></div><div class="clear"></div><div id="comment-43905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

