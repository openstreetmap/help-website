+++
type = "question"
title = "Boolean preference change bypasses callback?"
description = '''I&#x27;ve registered a number of preferences using a common call back which needs to perform some combinational assessment of preferences. Everything seems to work fine EXCEPT for when I change a boolean field using the right click menu directly (e.g. toggling checkmark). Under these circumstances it see...'''
date = "2017-06-13T14:37:00Z"
lastmod = "2017-06-14T07:10:00Z"
weight = 61992
keywords = [ "prefs", "preferences" ]
aliases = [ "/questions/61992" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Boolean preference change bypasses callback?](/questions/61992/boolean-preference-change-bypasses-callback)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61992-score" class="post-score" title="current number of votes">0</div><span id="post-61992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've registered a number of preferences using a common call back which needs to perform some combinational assessment of preferences. Everything seems to work fine EXCEPT for when I change a boolean field using the right click menu directly (e.g. toggling checkmark). Under these circumstances it seems the value is being changed, and the packets are being re-dissected, but the callback routine is bypassed. I can manipulate the same variable using regular preferences window (even launching it from the right click menu) and everything works just fine.</p><p>It's as if the shortcut method for changing booleans neglects to call the callback.. Is this a (QT) GUI Bug?</p><p>EDIT: This behavior may be limited to windows... Linux plugin in built from same code seems to act properly.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-prefs" rel="tag" title="see questions tagged &#39;prefs&#39;">prefs</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '17, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/f5a6a32440657fdf63b9db18f3922c70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wittynickname&#39;s gravatar image" /><p><span>wittynickname</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wittynickname has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '17, 15:17</strong> </span></p></div></div><div id="comments-container-61992" class="comments-container"></div><div id="comment-tools-61992" class="comment-tools"></div><div class="clear"></div><div id="comment-61992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62007"></span>

<div id="answer-container-62007" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62007-score" class="post-score" title="current number of votes">0</div><span id="post-62007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wittynickname has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you've encountered <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13536">Bug 13536</a>, which has been fixed as of <a href="https://www.wireshark.org/docs/relnotes/wireshark-2.2.6.html">Wireshark 2.2.6</a> and <a href="https://www.wireshark.org/docs/relnotes/wireshark-2.0.12.html">Wireshark 2.0.12</a>. If you're using an older version of Wireshark, you should upgrade to at least one of these versions to resolve this bug, but I recommend upgrading to the latest available version (currently 2.2.7, with <a href="https://wiki.wireshark.org/Development/LifeCycle">2.4.0 coming soon</a>) if you can.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '17, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62007" class="comments-container"><span id="62012"></span><div id="comment-62012" class="comment"><div id="post-62012-score" class="comment-score"></div><div class="comment-text"><p>That solves it! Linux build is 2.2.6 but my Windows testbed is 2.2.5.</p></div><div id="comment-62012-info" class="comment-info"><span class="comment-age">(14 Jun '17, 07:08)</span> <span class="comment-user userinfo">wittynickname</span></div></div><span id="62013"></span><div id="comment-62013" class="comment"><div id="post-62013-score" class="comment-score">1</div><div class="comment-text"><p>also THANKS!</p></div><div id="comment-62013-info" class="comment-info"><span class="comment-age">(14 Jun '17, 07:10)</span> <span class="comment-user userinfo">wittynickname</span></div></div></div><div id="comment-tools-62007" class="comment-tools"></div><div class="clear"></div><div id="comment-62007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

