+++
type = "question"
title = "wireshark in rpm"
description = '''dear expert,  please help our issue on installing and running wireshark.rpm i&#x27;ve install wireshark with : rpm -ivh wireshark then it had installed, but how to running this application ? i&#x27;ve type wireshark on root#wireshark , but it cannot running please advice :( '''
date = "2012-05-25T02:25:00Z"
lastmod = "2012-05-25T02:51:00Z"
weight = 11323
keywords = [ "rpm", "wireshark" ]
aliases = [ "/questions/11323" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark in rpm](/questions/11323/wireshark-in-rpm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11323-score" class="post-score" title="current number of votes">0</div><span id="post-11323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>dear expert,</p><p>please help our issue on installing and running wireshark.rpm</p><p>i've install wireshark with : rpm -ivh wireshark</p><p>then it had installed, but how to running this application ?</p><p>i've type wireshark on root#wireshark ,</p><p>but it cannot running</p><p>please advice :(</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpm" rel="tag" title="see questions tagged &#39;rpm&#39;">rpm</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '12, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/42ceab67e7b30b09adfcdaba88883837?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chipset83&#39;s gravatar image" /><p><span>chipset83</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chipset83 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '12, 03:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-11323" class="comments-container"></div><div id="comment-tools-11323" class="comment-tools"></div><div class="clear"></div><div id="comment-11323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11324"></span>

<div id="answer-container-11324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11324-score" class="post-score" title="current number of votes">0</div><span id="post-11324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>sounds like you installed only the non-gui version of wireshark. Try to run <strong>tshark</strong> to verify that.</p><p>HOWEVER, without ANY information about the system you're on (Linux distribution, release version, etc.), nobody will be to help.</p><p>Futhermore I suggest:</p><ol><li><p>don't use rpm to install wireshark. You're better off with the package manager of your system (yum, yast, whatever it may be).</p></li><li><p>better don't run wireshark as root (security reasons).</p></li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '12, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '12, 03:23</strong> </span></p></div></div><div id="comments-container-11324" class="comments-container"></div><div id="comment-tools-11324" class="comment-tools"></div><div class="clear"></div><div id="comment-11324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

