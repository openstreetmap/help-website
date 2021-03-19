+++
type = "question"
title = "Weird empty blank space in capture (0x20)"
description = '''Hey guys, have any of you came across with something similar to this? What could these refer to? Why is there lots of 20 hexs, not &quot;00&quot; when they are basically empty blank space. Also, there&#x27;s a few dots in between the blank space. '''
date = "2015-08-11T01:12:00Z"
lastmod = "2015-08-11T02:10:00Z"
weight = 44956
keywords = [ "null-byte", "blank", "20", "empty", "space" ]
aliases = [ "/questions/44956" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Weird empty blank space in capture (0x20)](/questions/44956/weird-empty-blank-space-in-capture-0x20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44956-score" class="post-score" title="current number of votes">0</div><span id="post-44956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, have any of you came across with something similar to this? What could these refer to?</p><p>Why is there lots of 20 hexs, not "00" when they are basically empty blank space. Also, there's a few dots in between the blank space.</p><p><img src="http://uploadpie.com/NpP3T" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-null-byte" rel="tag" title="see questions tagged &#39;null-byte&#39;">null-byte</span> <span class="post-tag tag-link-blank" rel="tag" title="see questions tagged &#39;blank&#39;">blank</span> <span class="post-tag tag-link-20" rel="tag" title="see questions tagged &#39;20&#39;">20</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span> <span class="post-tag tag-link-space" rel="tag" title="see questions tagged &#39;space&#39;">space</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/1855020002bac3627bb6037224464140?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="albi&#39;s gravatar image" /><p><span>albi</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="albi has no accepted answers">0%</span></p></img></div></div><div id="comments-container-44956" class="comments-container"></div><div id="comment-tools-44956" class="comment-tools"></div><div class="clear"></div><div id="comment-44956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44957"></span>

<div id="answer-container-44957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44957-score" class="post-score" title="current number of votes">0</div><span id="post-44957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's text based, not binary, so empty is defined by whitespace, which is char 0x20 (among others).</p><p>The 'dots' you refer to are the end-of-line (line feed in this case) markers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '15, 02:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-44957" class="comments-container"></div><div id="comment-tools-44957" class="comment-tools"></div><div class="clear"></div><div id="comment-44957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

