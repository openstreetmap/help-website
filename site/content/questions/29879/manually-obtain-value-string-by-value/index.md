+++
type = "question"
title = "Manually obtain value string by value"
description = '''I would like to obtain the value string for a specific value manually (to display it in the COL_INFO column) by it&#x27;s value. I could manually iterate over my value string mapping, however I think there might also be an official API for this task.'''
date = "2014-02-14T21:08:00Z"
lastmod = "2014-02-15T02:34:00Z"
weight = 29879
keywords = [ "dissector", "value_string" ]
aliases = [ "/questions/29879" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Manually obtain value string by value](/questions/29879/manually-obtain-value-string-by-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29879-score" class="post-score" title="current number of votes">0</div><span id="post-29879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to obtain the value string for a specific value manually (to display it in the <code>COL_INFO</code> column) by it's value. I could manually iterate over my value string mapping, however I think there might also be an official API for this task.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-value_string" rel="tag" title="see questions tagged &#39;value_string&#39;">value_string</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '14, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/81b4919fa0947bab71a147c436c9e9b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="athre0z&#39;s gravatar image" /><p><span>athre0z</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="athre0z has no accepted answers">0%</span></p></div></div><div id="comments-container-29879" class="comments-container"></div><div id="comment-tools-29879" class="comment-tools"></div><div class="clear"></div><div id="comment-29879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29882"></span>

<div id="answer-container-29882" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29882-score" class="post-score" title="current number of votes">1</div><span id="post-29882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="athre0z has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are several functions doing the dirty work for you. Look at the content of epan/value_strings.h and pick the one fitting your needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '14, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-29882" class="comments-container"></div><div id="comment-tools-29882" class="comment-tools"></div><div class="clear"></div><div id="comment-29882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

