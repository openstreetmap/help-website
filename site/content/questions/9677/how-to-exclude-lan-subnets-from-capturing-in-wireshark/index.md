+++
type = "question"
title = "How to exclude LAN Subnets from capturing in WireShark"
description = '''How to exclude LAN Subnets from capturing in WireShark'''
date = "2012-03-21T07:48:00Z"
lastmod = "2012-03-21T08:08:00Z"
weight = 9677
keywords = [ "exclude", "lan", "subnets" ]
aliases = [ "/questions/9677" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to exclude LAN Subnets from capturing in WireShark](/questions/9677/how-to-exclude-lan-subnets-from-capturing-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9677-score" class="post-score" title="current number of votes">0</div><span id="post-9677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to exclude LAN Subnets from capturing in WireShark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-exclude" rel="tag" title="see questions tagged &#39;exclude&#39;">exclude</span> <span class="post-tag tag-link-lan" rel="tag" title="see questions tagged &#39;lan&#39;">lan</span> <span class="post-tag tag-link-subnets" rel="tag" title="see questions tagged &#39;subnets&#39;">subnets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '12, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/31622a3bbbbf992f90124b64273c466f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fbaig&#39;s gravatar image" /><p><span>fbaig</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fbaig has no accepted answers">0%</span></p></div></div><div id="comments-container-9677" class="comments-container"></div><div id="comment-tools-9677" class="comment-tools"></div><div class="clear"></div><div id="comment-9677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9678"></span>

<div id="answer-container-9678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9678-score" class="post-score" title="current number of votes">1</div><span id="post-9678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You just have to apply a capture filter: e.g. if you don't want to capture 192.168.1.0/24 --&gt; <em>not host 192.168.1</em></p><p>just leave out the last octet(s)</p><p>or you can directly do <em>not net 192.168.1.0/24</em>, but I'm not sure if that works with older versions</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '12, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Mar '12, 08:20</strong> </span></p></div></div><div id="comments-container-9678" class="comments-container"></div><div id="comment-tools-9678" class="comment-tools"></div><div class="clear"></div><div id="comment-9678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

