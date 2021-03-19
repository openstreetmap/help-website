+++
type = "question"
title = "Will enumeration string allow to range the enum value with the string"
description = '''Hi I have a requirement in which enums are defined from 1 to 225, but the problem of here is 1 to 10 enum strings are different and from 11 to 225 are same. const value_string Fields_Emun_validate_Errors[] = { { 0, &quot;Port_Error&quot; }, { 1, &quot;IP_Error&quot; }, { 2, &quot;Stack_Error&quot; }, { 3, &quot;Val_Error&quot; }, { 4, &quot;ra...'''
date = "2016-05-17T06:07:00Z"
lastmod = "2016-05-17T07:16:00Z"
weight = 52670
keywords = [ "reassembly", "value_string", "enumeration", "wireshark" ]
aliases = [ "/questions/52670" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Will enumeration string allow to range the enum value with the string](/questions/52670/will-enumeration-string-allow-to-range-the-enum-value-with-the-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52670-score" class="post-score" title="current number of votes">0</div><span id="post-52670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a requirement in which enums are defined from 1 to 225, but the problem of here is 1 to 10 enum strings are different and from 11 to 225 are same.</p><pre><code>const value_string Fields_Emun_validate_Errors[] = { { 0, &quot;Port_Error&quot; }, { 1, &quot;IP_Error&quot; }, { 2, &quot;Stack_Error&quot; }, { 3, &quot;Val_Error&quot; }, { 4, &quot;range_Error&quot; },.. .. .. { 11, &quot;Field Error&quot; },.. .. .. { 225, &quot;Field Erro&quot; }, };</code></pre><p>Should we need to write for 11 to 225 or else any range is allowed ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-value_string" rel="tag" title="see questions tagged &#39;value_string&#39;">value_string</span> <span class="post-tag tag-link-enumeration" rel="tag" title="see questions tagged &#39;enumeration&#39;">enumeration</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '16, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/04334c27cb629065a13d61a61b611038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinesh%20Babu%20Sadu&#39;s gravatar image" /><p><span>Dinesh Babu ...</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinesh Babu Sadu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '16, 07:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-52670" class="comments-container"></div><div id="comment-tools-52670" class="comment-tools"></div><div class="clear"></div><div id="comment-52670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52671"></span>

<div id="answer-container-52671" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52671-score" class="post-score" title="current number of votes">0</div><span id="post-52671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dinesh Babu Sadu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>given your description you should use a range_string array instead of value_string array. Please have a look at doc/README.dissector document, more specifically the chapter 1.5 and "ranges" section.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '16, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-52671" class="comments-container"><span id="52673"></span><div id="comment-52673" class="comment"><div id="post-52673-score" class="comment-score"></div><div class="comment-text"><p>Thanks Pascal, It worked for me.</p></div><div id="comment-52673-info" class="comment-info"><span class="comment-age">(17 May '16, 07:16)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div></div><div id="comment-tools-52671" class="comment-tools"></div><div class="clear"></div><div id="comment-52671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

