+++
type = "question"
title = "filter unanswered diameter queries through tshark"
description = '''Hi experts, While using following filter through wireshark GUI application it gives me desired results i.e. diameter requests that didn&#x27;t receieve response. diameter.flags.request == 1 and !diameter.answer_in But when I tried to execute same filter using tshark -R syntax it simply shows me entire li...'''
date = "2017-03-13T10:01:00Z"
lastmod = "2017-03-13T10:28:00Z"
weight = 60035
keywords = [ "diameter", "tshark" ]
aliases = [ "/questions/60035" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filter unanswered diameter queries through tshark](/questions/60035/filter-unanswered-diameter-queries-through-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60035-score" class="post-score" title="current number of votes">0</div><span id="post-60035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi experts,</p><p>While using following filter through wireshark GUI application it gives me desired results i.e. diameter requests that didn't receieve response.</p><p>diameter.flags.request == 1 and !diameter.answer_in</p><p>But when I tried to execute same filter using tshark -R syntax it simply shows me entire list of diameter request packets irrespective of their answer status.</p><p>I want to know how to execute this specific filter using tshark command ?</p><p>Thanks in advance !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '17, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-60035" class="comments-container"></div><div id="comment-tools-60035" class="comment-tools"></div><div class="clear"></div><div id="comment-60035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60037"></span>

<div id="answer-container-60037" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60037-score" class="post-score" title="current number of votes">1</div><span id="post-60037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>-R</code> is a <em>read</em> filter option that limits what packets are loaded from the capture, and as such it won't work for filter elements that require a 2nd pass.</p><p>In this case use the <code>-Y</code> display filter option that corresponds to the display filter in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '17, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60037" class="comments-container"><span id="60038"></span><div id="comment-60038" class="comment"><div id="post-60038-score" class="comment-score"></div><div class="comment-text"><p>Wow..that was superfast. Thanks ! I will definitely check this and will confirm. I presume no dependency on tshark version, correct ?</p></div><div id="comment-60038-info" class="comment-info"><span class="comment-age">(13 Mar '17, 10:16)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="60039"></span><div id="comment-60039" class="comment"><div id="post-60039-score" class="comment-score">1</div><div class="comment-text"><p><code>-Y</code> was added in March 2013, see the bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8223">here</a>.</p><p>I leave it as an exercise for the reader to determine what version that was then released in.</p></div><div id="comment-60039-info" class="comment-info"><span class="comment-age">(13 Mar '17, 10:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-60037" class="comment-tools"></div><div class="clear"></div><div id="comment-60037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

