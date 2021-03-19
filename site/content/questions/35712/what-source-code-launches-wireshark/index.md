+++
type = "question"
title = "What source code launches Wireshark?"
description = '''What is the main file in the source code which launches the wireshark application after the build?'''
date = "2014-08-25T11:34:00Z"
lastmod = "2014-08-26T13:05:00Z"
weight = 35712
keywords = [ "source-code" ]
aliases = [ "/questions/35712" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What source code launches Wireshark?](/questions/35712/what-source-code-launches-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35712-score" class="post-score" title="current number of votes">0</div><span id="post-35712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the main file in the source code which launches the wireshark application after the build?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source-code" rel="tag" title="see questions tagged &#39;source-code&#39;">source-code</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '14, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/6faea3eba9bf10d1e5dd9cc5b58e4fcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssayed1&#39;s gravatar image" /><p><span>ssayed1</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssayed1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>25 Aug '14, 11:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35712" class="comments-container"><span id="35775"></span><div id="comment-35775" class="comment"><div id="post-35775-score" class="comment-score"></div><div class="comment-text"><p>Please refrain from asking the <a href="https://ask.wireshark.org/questions/35715/source-code-main-file-of-wireshark">same question</a> more than once.</p></div><div id="comment-35775-info" class="comment-info"><span class="comment-age">(26 Aug '14, 13:05)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-35712" class="comment-tools"></div><div class="clear"></div><div id="comment-35712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35718"></span>

<div id="answer-container-35718" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35718-score" class="post-score" title="current number of votes">1</div><span id="post-35718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean "what source file contains the <code>main()</code> function for Wireshark?", it's <code>ui/gtk/main.c</code> in the GTK+ version and <code>ui/qt/main.cpp</code> in the Qt version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '14, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '14, 11:58</strong> </span></p></div></div><div id="comments-container-35718" class="comments-container"></div><div id="comment-tools-35718" class="comment-tools"></div><div class="clear"></div><div id="comment-35718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

