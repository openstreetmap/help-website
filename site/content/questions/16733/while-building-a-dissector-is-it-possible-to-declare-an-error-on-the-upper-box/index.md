+++
type = "question"
title = "while building a dissector, Is it possible to declare an error on the upper box?"
description = '''Hey, I&#x27;m building a dissector and wanted to know if it is possible declare an error on the upper box, where all the packets are (tcp ...) By declaring I mean to get the color of the column red... I know it is possible to declare and color the column in red on the middle box (where the description of...'''
date = "2012-12-09T02:24:00Z"
lastmod = "2012-12-14T23:58:00Z"
weight = 16733
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/16733" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [while building a dissector, Is it possible to declare an error on the upper box?](/questions/16733/while-building-a-dissector-is-it-possible-to-declare-an-error-on-the-upper-box)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16733-score" class="post-score" title="current number of votes">0</div><span id="post-16733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I'm building a dissector and wanted to know if it is possible declare an error on the upper box, where all the packets are (tcp ...)</p><p>By declaring I mean to get the color of the column red...</p><p>I know it is possible to declare and color the column in red on the middle box (where the description of the packets is found), but I want to see if it is also possible to the upper box...</p><p>Or, the only way to do it is to make it by the hand with view&gt;&gt;coloring rules and create some error flag which will be up in an error, and then I'll color it ?</p><p>thanks ahead</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '12, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p><span>hudac</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div></div><div id="comments-container-16733" class="comments-container"></div><div id="comment-tools-16733" class="comment-tools"></div><div class="clear"></div><div id="comment-16733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16924"></span>

<div id="answer-container-16924" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16924-score" class="post-score" title="current number of votes">1</div><span id="post-16924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hudac has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use <code>expert_add_info_format()</code> to add an error flag to the packet, which will make the row in the middle pane red, and then add a coloring rule with a filter expression of</p><pre><code>expert.severity == &quot;Error&quot;</code></pre><p>(exactly like that, complete with the quotes around Error) and with your choice of background color (red, presumably - #FF5C5C is probably closes to the red used in the packet detail pane). Put that rule at the beginning of the list of coloring rules, so that it overrides all rules below it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16924" class="comments-container"></div><div id="comment-tools-16924" class="comment-tools"></div><div class="clear"></div><div id="comment-16924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16736"></span>

<div id="answer-container-16736" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16736-score" class="post-score" title="current number of votes">0</div><span id="post-16736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://ask.wireshark.org/questions/9511/is-it-possible-to-set-the-coloring-of-a-packet-from-a-dissector">http://ask.wireshark.org/questions/9511/is-it-possible-to-set-the-coloring-of-a-packet-from-a-dissector</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '12, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p><span>hudac</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div></div><div id="comments-container-16736" class="comments-container"></div><div id="comment-tools-16736" class="comment-tools"></div><div class="clear"></div><div id="comment-16736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

