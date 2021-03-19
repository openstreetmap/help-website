+++
type = "question"
title = "Expert information field"
description = '''Hello, I&#x27;ve updated tshark to actual version, i.e. 1.12. Unfortunately, in this version field filter -e expert is not working.  (process:31133): WARNING : &#x27;expert&#x27; isn&#x27;t a valid field! tshark: Some fields aren&#x27;t valid How to resolve this issue? Many thanks in advance!'''
date = "2014-08-20T03:51:00Z"
lastmod = "2014-08-20T06:46:00Z"
weight = 35615
keywords = [ "filter", "linux" ]
aliases = [ "/questions/35615" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Expert information field](/questions/35615/expert-information-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35615-score" class="post-score" title="current number of votes">0</div><span id="post-35615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I've updated tshark to actual version, i.e. 1.12. Unfortunately, in this version field filter <strong>-e expert</strong> is not working. <code> (process:31133): WARNING : 'expert' isn't a valid field! tshark: Some fields aren't valid</code></p><p>How to resolve this issue?</p><p>Many thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '14, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc9b7ddbee4ec657351cff07ace3ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrav&#39;s gravatar image" /><p><span>mrav</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrav has no accepted answers">0%</span></p></div></div><div id="comments-container-35615" class="comments-container"></div><div id="comment-tools-35615" class="comment-tools"></div><div class="clear"></div><div id="comment-35615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35624"></span>

<div id="answer-container-35624" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35624-score" class="post-score" title="current number of votes">2</div><span id="post-35624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrav has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Starting with Wireshark 1.12, you need to specify, <code>-e _ws.expert</code>. The <code>_ws.</code> prefix was added to make it clear that this is a Wireshark-generated field and not an actual field that's part of any particular protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35624" class="comments-container"></div><div id="comment-tools-35624" class="comment-tools"></div><div class="clear"></div><div id="comment-35624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

