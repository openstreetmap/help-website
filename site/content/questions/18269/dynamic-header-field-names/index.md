+++
type = "question"
title = "Dynamic Header field names"
description = '''Is there any way to change the header names in a dissector depending on the data that&#x27;s dissected? or to have the header names extracted from a pre-initialized array? example: array[]={&quot;NewHeading1&quot;,&quot;NewHeading2&quot;}; OLD DISPLAY: -Frame 17300........ -Ethernet II,....... -MYPROTOCOL -Heading1 -SubHead...'''
date = "2013-02-03T17:54:00Z"
lastmod = "2013-02-05T19:44:00Z"
weight = 18269
keywords = [ "header", "dynamic" ]
aliases = [ "/questions/18269" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dynamic Header field names](/questions/18269/dynamic-header-field-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18269-score" class="post-score" title="current number of votes">0</div><span id="post-18269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to change the header names in a dissector depending on the data that's dissected? or to have the header names extracted from a pre-initialized array?</p><p>example: array[]={"NewHeading1","NewHeading2"};</p><p><strong><em>OLD DISPLAY:</em></strong></p><p>-Frame 17300........</p><p>-Ethernet II,.......</p><p>-MYPROTOCOL</p><p>-Heading1</p><pre><code>-SubHeading1

-SubHeading2</code></pre><p>-Heading2</p><pre><code>-SubHeading1

-SubHeading2</code></pre><p><strong><em>NEW DISPLAY:</em></strong></p><p>-Frame 17300........</p><p>-Ethernet II,.......</p><p>-MYPROTOCOL</p><p>-NewHeading1</p><pre><code>-SubHeading1

-SubHeading2</code></pre><p>-NewHeading2</p><pre><code>-SubHeading1

-SubHeading2</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '13, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/024c038a84faf77c618cfe43ee97ed64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StealthUE&#39;s gravatar image" /><p><span>StealthUE</span><br />
<span class="score" title="66 reputation points">66</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StealthUE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '13, 17:57</strong> </span></p></div></div><div id="comments-container-18269" class="comments-container"></div><div id="comment-tools-18269" class="comment-tools"></div><div class="clear"></div><div id="comment-18269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18345"></span>

<div id="answer-container-18345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18345-score" class="post-score" title="current number of votes">0</div><span id="post-18345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No. A particular field should always represent the same thing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '13, 19:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18345" class="comments-container"></div><div id="comment-tools-18345" class="comment-tools"></div><div class="clear"></div><div id="comment-18345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

