+++
type = "question"
title = "Only recieve win=65535 info packets"
description = '''I only want to display packets which have win=65535 in the info, how to do this as filter?'''
date = "2012-06-16T03:57:00Z"
lastmod = "2012-06-16T04:33:00Z"
weight = 11987
keywords = [ "info", "win65535" ]
aliases = [ "/questions/11987" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Only recieve win=65535 info packets](/questions/11987/only-recieve-win65535-info-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11987-score" class="post-score" title="current number of votes">0</div><span id="post-11987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I only want to display packets which have win=65535 in the info, how to do this as filter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-win65535" rel="tag" title="see questions tagged &#39;win65535&#39;">win65535</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '12, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/567b6570eeea7bfdad91a798c4e91438?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="solvapolva&#39;s gravatar image" /><p><span>solvapolva</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="solvapolva has no accepted answers">0%</span></p></div></div><div id="comments-container-11987" class="comments-container"></div><div id="comment-tools-11987" class="comment-tools"></div><div class="clear"></div><div id="comment-11987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11989"></span>

<div id="answer-container-11989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11989-score" class="post-score" title="current number of votes">1</div><span id="post-11989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the filter:</p><pre><code>tcp.window_size == 65535</code></pre><p>You can always look in the packet details for a field with it's value and then use (rightclick) Apply as filter to achieve this in an easy way :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '12, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11989" class="comments-container"></div><div id="comment-tools-11989" class="comment-tools"></div><div class="clear"></div><div id="comment-11989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

