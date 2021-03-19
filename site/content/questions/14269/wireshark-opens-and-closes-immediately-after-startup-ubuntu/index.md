+++
type = "question"
title = "wireshark opens and closes immediately after startup (ubuntu)"
description = '''wireshark opens and closes immediately after startup when started as sudo. When started as a root user in ubuntu, additionally a segmentation fault appears. This happens when building from source code as well as installing using synaptic package manager. Any comments appreciated'''
date = "2012-09-14T10:20:00Z"
lastmod = "2012-09-14T16:03:00Z"
weight = 14269
keywords = [ "startup" ]
aliases = [ "/questions/14269" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark opens and closes immediately after startup (ubuntu)](/questions/14269/wireshark-opens-and-closes-immediately-after-startup-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14269-score" class="post-score" title="current number of votes">0</div><span id="post-14269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>wireshark opens and closes immediately after startup when started as sudo. When started as a root user in ubuntu, additionally a segmentation fault appears. This happens when building from source code as well as installing using synaptic package manager. Any comments appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/e8b5da154262a5aca7f544fc3651cba3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mna&#39;s gravatar image" /><p><span>mna</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mna has no accepted answers">0%</span></p></div></div><div id="comments-container-14269" class="comments-container"><span id="14275"></span><div id="comment-14275" class="comment"><div id="post-14275-score" class="comment-score"></div><div class="comment-text"><p>can you please post the seg fault message?</p></div><div id="comment-14275-info" class="comment-info"><span class="comment-age">(14 Sep '12, 13:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14276"></span><div id="comment-14276" class="comment"><div id="post-14276-score" class="comment-score"></div><div class="comment-text"><p>Sep 14 13:05:48 meena-HP-Z400-Workstation kernel: [150343.041124] wireshark[19063]: segfault at 8 ip 00007fccb15fcf53 sp 00007fff67564130 error 4 in libsmi.so.2.0.27[7fccb15f0000+59000] Sep 14 13:06:50 meena-HP-Z400-Workstation kernel: [150404.353829] wireshark[19074]: segfault at 8 ip 00007f5d93e14f53 sp 00007fff149f35e0 error 4 in libsmi.so.2.0.27[7f5d93e08000+59000]</p></div><div id="comment-14276-info" class="comment-info"><span class="comment-age">(14 Sep '12, 14:13)</span> <span class="comment-user userinfo">mna</span></div></div></div><div id="comment-tools-14269" class="comment-tools"></div><div class="clear"></div><div id="comment-14269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14282"></span>

<div id="answer-container-14282" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14282-score" class="post-score" title="current number of votes">0</div><span id="post-14282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I fixed it by installing snmp-mibs-downloader</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/e8b5da154262a5aca7f544fc3651cba3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mna&#39;s gravatar image" /><p><span>mna</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mna has no accepted answers">0%</span></p></div></div><div id="comments-container-14282" class="comments-container"></div><div id="comment-tools-14282" class="comment-tools"></div><div class="clear"></div><div id="comment-14282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

