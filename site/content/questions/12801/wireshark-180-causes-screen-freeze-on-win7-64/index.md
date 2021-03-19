+++
type = "question"
title = "Wireshark 1.8.0 causes screen freeze on Win7 64"
description = '''Since installing 1.8.0 I find that almost every time I move or resize a Wireshark window, my screen freezes: the mouse cursor moves but clicking does nothing. I can recover by using control-alt-del, then clicking Cancel, after which the screen repaints and normal mouse operations resume, until I nex...'''
date = "2012-07-17T10:00:00Z"
lastmod = "2012-07-17T13:59:00Z"
weight = 12801
keywords = [ "mouse", "freeze" ]
aliases = [ "/questions/12801" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 1.8.0 causes screen freeze on Win7 64](/questions/12801/wireshark-180-causes-screen-freeze-on-win7-64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12801-score" class="post-score" title="current number of votes">0</div><span id="post-12801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Since installing 1.8.0 I find that almost every time I move or resize a Wireshark window, my screen freezes: the mouse cursor moves but clicking does nothing. I can recover by using control-alt-del, then clicking Cancel, after which the screen repaints and normal mouse operations resume, until I next move a window. Reverting to 1.6.8 has restored sanity.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mouse" rel="tag" title="see questions tagged &#39;mouse&#39;">mouse</span> <span class="post-tag tag-link-freeze" rel="tag" title="see questions tagged &#39;freeze&#39;">freeze</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '12, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/4d15cd03db763ce238278a08c4967aa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frogb&#39;s gravatar image" /><p><span>frogb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frogb has no accepted answers">0%</span></p></div></div><div id="comments-container-12801" class="comments-container"></div><div id="comment-tools-12801" class="comment-tools"></div><div class="clear"></div><div id="comment-12801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12802"></span>

<div id="answer-container-12802" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12802-score" class="post-score" title="current number of votes">0</div><span id="post-12802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="frogb has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think this is one for the bug tracker at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a>. After finding out if there is already an open bug for this you should include details information about your system, because I know tons of 1.8 installations that run just fine on Win7 x64 (for me, it's working fine on two of my Workstations and on my Laptop at least). So it is probably something in relation to your hardware/driver specs.</p><p>You can also try to update your graphics card drivers to the latest version, maybe it helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12802" class="comments-container"><span id="12809"></span><div id="comment-12809" class="comment"><div id="post-12809-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the link. It is a reported bug (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7305">7305</a>).</p></div><div id="comment-12809-info" class="comment-info"><span class="comment-age">(17 Jul '12, 13:59)</span> <span class="comment-user userinfo">frogb</span></div></div></div><div id="comment-tools-12802" class="comment-tools"></div><div class="clear"></div><div id="comment-12802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

