+++
type = "question"
title = "Where can I find a list of all possible fields for the Tshark -e commandline argument?"
description = '''In Tshark CLI, we can use the commandline argument -T fields, and then follow it with -e argument, whose value has to be the name of the field I want to print.  But where are my options? What values can I use for -e? Where can I find all the fields that I can choose from? How do you get to know what...'''
date = "2016-08-20T07:31:00Z"
lastmod = "2016-08-20T12:14:00Z"
weight = 55000
keywords = [ "fields", "tshark", "field" ]
aliases = [ "/questions/55000" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Where can I find a list of all possible fields for the Tshark -e commandline argument?](/questions/55000/where-can-i-find-a-list-of-all-possible-fields-for-the-tshark-e-commandline-argument)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55000-score" class="post-score" title="current number of votes">1</div><span id="post-55000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>In Tshark CLI, we can use the commandline argument <strong><code>-T fields</code></strong>, and then follow it with <strong><code>-e</code></strong> argument, whose value has to be the name of the field I want to print.</p><p>But where are my options? What values can I use for <code>-e</code>?</p><p>Where can I find all the fields that I can choose from? How do you get to know what field you need to use?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '16, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p><span>Jesss</span><br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div></div><div id="comments-container-55000" class="comments-container"></div><div id="comment-tools-55000" class="comment-tools"></div><div class="clear"></div><div id="comment-55000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55001"></span>

<div id="answer-container-55001" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55001-score" class="post-score" title="current number of votes">2</div><span id="post-55001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jesss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The protocol fields that can be used for display filter can also be used as values to <code>-e</code> in tshark. So you have three possibilities how to find the ones you need:</p><ul><li><p>in the relevant <a href="https://www.wireshark.org/docs/dfref/">Wireshark documentation</a></p></li><li><p>by running Wireshark and using the <code>Expression...</code> button next to the display filter form field to open a tree with all protocols and their fields.</p></li><li><p>by starting to type a protocol name into the display filter and using the context completion.</p></li></ul><p>On top of the actual protocol fields, you can use also column headers from packet list as arguments to <code>-e</code> if you put <code>_ws.col.</code> in front of the column name. An example would be <code>-e _ws.col.Info</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '16, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55001" class="comments-container"></div><div id="comment-tools-55001" class="comment-tools"></div><div class="clear"></div><div id="comment-55001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55005"></span>

<div id="answer-container-55005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55005-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55005-score" class="post-score" title="current number of votes">4</div><span id="post-55005-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Or by using the command <code>tshark -G fields</code> that dumps all the registered fields</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '16, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Aug '16, 23:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55005" class="comments-container"></div><div id="comment-tools-55005" class="comment-tools"></div><div class="clear"></div><div id="comment-55005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

