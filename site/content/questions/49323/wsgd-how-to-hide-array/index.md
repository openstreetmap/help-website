+++
type = "question"
title = "WSGD. How to hide array?"
description = '''Have an array of 300 values in packet. This is shown as 300 lines. I would like to print them in line if it is possible. It will be cool to have opportunity to hide an array like any struct (tree structure). Looking for this feature on the site and in example .fdesc did not give results. Is it possi...'''
date = "2016-01-18T07:42:00Z"
lastmod = "2016-01-18T08:13:00Z"
weight = 49323
keywords = [ "dissector", "wsgd" ]
aliases = [ "/questions/49323" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WSGD. How to hide array?](/questions/49323/wsgd-how-to-hide-array)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49323-score" class="post-score" title="current number of votes">0</div><span id="post-49323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Have an array of 300 values in packet. This is shown as 300 lines.<br />
I would like to print them in line if it is possible. It will be cool to have opportunity to hide an array like any struct (tree structure). Looking for this feature on the site and in example <code>.fdesc</code> did not give results.<br />
Is it possible? How to do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wsgd" rel="tag" title="see questions tagged &#39;wsgd&#39;">wsgd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '16, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/680680d82143e4d33dc569913e5ef8c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kyb&#39;s gravatar image" /><p><span>kyb</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kyb has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-49323" class="comments-container"></div><div id="comment-tools-49323" class="comment-tools"></div><div class="clear"></div><div id="comment-49323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49325"></span>

<div id="answer-container-49325" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49325-score" class="post-score" title="current number of votes">0</div><span id="post-49325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kyb has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Define an additional struct:</p><pre><code>struct T_my_array
{
  float32[300]  data;
}</code></pre><p>And use it in main struct:</p><pre><code>struct T_msg_main
{
  T_msg_header_type  Header;
  ...
  T_my_array  my_array;
}</code></pre><p>Or even:</p><pre><code>struct T_msg_main
{
  T_msg_header_type  Header;
  ...
  struct T_my_array { float32[300]  data; };
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '16, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/680680d82143e4d33dc569913e5ef8c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kyb&#39;s gravatar image" /><p><span>kyb</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kyb has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jan '16, 08:23</strong> </span></p></div></div><div id="comments-container-49325" class="comments-container"></div><div id="comment-tools-49325" class="comment-tools"></div><div class="clear"></div><div id="comment-49325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

