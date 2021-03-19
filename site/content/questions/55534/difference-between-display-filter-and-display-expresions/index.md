+++
type = "question"
title = "Difference between Display filter and Display expresions"
description = '''I have searched and don&#x27;t really see the difference between these. I have always used expressions to filter out local machine etc. and had a button. I have been playing with Display filters in the drop down list on the left and have a whole list I gathered that look for certain traffic.'''
date = "2016-09-13T14:19:00Z"
lastmod = "2016-09-14T02:05:00Z"
weight = 55534
keywords = [ "filter", "expresions", "display" ]
aliases = [ "/questions/55534" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between Display filter and Display expresions](/questions/55534/difference-between-display-filter-and-display-expresions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55534-score" class="post-score" title="current number of votes">0</div><span id="post-55534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have searched and don't really see the difference between these. I have always used expressions to filter out local machine etc. and had a button. I have been playing with Display filters in the drop down list on the left and have a whole list I gathered that look for certain traffic.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-expresions" rel="tag" title="see questions tagged &#39;expresions&#39;">expresions</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '16, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/0833f7ef8618ac6b7842265fbaa39861?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itsme0k&#39;s gravatar image" /><p><span>itsme0k</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itsme0k has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Sep '16, 14:23</strong> </span></p></div></div><div id="comments-container-55534" class="comments-container"></div><div id="comment-tools-55534" class="comment-tools"></div><div class="clear"></div><div id="comment-55534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55543"></span>

<div id="answer-container-55543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55543-score" class="post-score" title="current number of votes">0</div><span id="post-55543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I did a Google search for "display expression" on all wireshark.org sites and found <a href="https://www.wireshark.org/lists/ethereal-users/200604/msg00221.html">only one reference in a mail message</a> - unlike "display filter", which shows a lot of references.</p><p>So I'm not sure what a "display expression" is - it doesn't seem to be used, but if by "I have always used expressions to filter out local machine etc." you mean that you've captured traffic and then, in that capture, added a filter that only matched traffic other than local machine traffic, that's the exact same thing as a "display filter". I.e., a display filter is an expression that involves field names, values, comparison and matching operations, and Boolean operators ("and", "or", and "not") to combine multiple such operations.</p><p>So, in that sense, a "display filter", a "display expression", and a "display filter expression" are all different names for the same thing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '16, 19:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55543" class="comments-container"></div><div id="comment-tools-55543" class="comment-tools"></div><div class="clear"></div><div id="comment-55543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55549"></span>

<div id="answer-container-55549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55549-score" class="post-score" title="current number of votes">0</div><span id="post-55549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>Expression</code> button next to the display filter field opens a tool assisting you in putting together display filter primitives which you may use to create more complex display filter expressions. To compose a display filter primitive using this tool, you first select the protocol (meta)field from a tree containing all available fields provided by all active dissectors. By choosing a field, you get a list of comparison operators available for the chosen field which depends on field type and properties, and a list of possible values to compare with if a fixed list of values exists for the chosen field.</p><p>I.e. use of the <code>Expression</code> button is yet another way how to compose a display filter (which is, in this context, a common abbreviation of the precise term "display filter expression" - you may "use" a display filter but you describe the behaviour of that filter using an expression which consists of one or more primitives), the others being freehand typing and use of the dissection pane's context menu items like <code>Apply as Filter</code> and <code>Prepare as Filter</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '16, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55549" class="comments-container"></div><div id="comment-tools-55549" class="comment-tools"></div><div class="clear"></div><div id="comment-55549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

