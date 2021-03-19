+++
type = "question"
title = "What does TFS() in tfs.h do?"
description = '''Ok thank you. I was only familiar with #pragma once. However from your answer I conclude, that __TFS_H__ is not a requirement for using the syntax TFS(). I could use that without the guard. What I meant in my other point is, what is the logic behind &#x27;TFS()`? Where is it declared?'''
date = "2016-04-14T02:48:00Z"
lastmod = "2016-04-22T09:58:00Z"
weight = 51664
keywords = [ "tfs" ]
aliases = [ "/questions/51664" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does TFS() in tfs.h do?](/questions/51664/what-does-tfs-in-tfsh-do)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51664-score" class="post-score" title="current number of votes">0</div><span id="post-51664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok thank you. I was only familiar with #pragma once. However from your answer I conclude, that <code>__TFS_H__</code> is not a requirement for using the syntax <code>TFS()</code>. I could use that without the guard. What I meant in my other point is, what is the logic behind 'TFS()`? Where is it declared?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tfs" rel="tag" title="see questions tagged &#39;tfs&#39;">tfs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '16, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/c288ec16e3d47bc1e1602e5b4e283949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikethebo&#39;s gravatar image" /><p><span>mikethebo</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikethebo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted <strong>14 Apr '16, 12:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-51664" class="comments-container"></div><div id="comment-tools-51664" class="comment-tools"></div><div class="clear"></div><div id="comment-51664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51677"></span>

<div id="answer-container-51677" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51677-score" class="post-score" title="current number of votes">0</div><span id="post-51677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mikethebo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Fields with an integral data type can be given a <code>value_string</code> list, which maps values of that field to descriptive strings. Fields with a Boolean data type can be given a <code>true_false_string</code> list, which maps TRUE and FALSE to descriptive strings.</p><p>If we required C99, we could make a field in the <code>header_field_info</code> structure that was a union of <code>value_string *</code> and <code>struct true_false_string *</code> and have integral fields initialize the former member and Boolean fields initialize the latter member.</p><p>However, Wireshark doesn't require C99, and C90 doesn't handle initialization of a union very well - the initializer initializes the first element of the union, with no way to initialize other members.</p><p>So we just made the field a <code>const void *</code>, and have macros <code>VALS()</code> and <code>TFS()</code> that cast <code>value_string *</code> and <code>struct true_false_string *</code> to <code>const void *</code>, which are used in initializers.</p><p><code>VALS()</code> and <code>TFS()</code> are macros, and are defined in <code>epan/proto.h</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Apr '16, 12:22</strong> </span></p></div></div><div id="comments-container-51677" class="comments-container"><span id="51879"></span><div id="comment-51879" class="comment"><div id="post-51879-score" class="comment-score"></div><div class="comment-text"><p>Oh man thank you. I was looking for this by doing multiple full text searches in the Windows Explorer. Obviously not very reliable. This almost has the dimension of RTFM, still thank you for you complete answer.</p></div><div id="comment-51879-info" class="comment-info"><span class="comment-age">(22 Apr '16, 09:58)</span> <span class="comment-user userinfo">mikethebo</span></div></div></div><div id="comment-tools-51677" class="comment-tools"></div><div class="clear"></div><div id="comment-51677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

