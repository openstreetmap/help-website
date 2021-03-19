+++
type = "question"
title = "Is it possible to disable &quot;check for updates&quot;?"
description = '''I am trying to package and deploy Wireshark 1.10.9 and I must have the &quot;check for updates&quot; under the Help icon, disabled, greyed out, or removed. Can someone furnish an answer on how this can be accomplished? Thanks'''
date = "2014-08-11T10:22:00Z"
lastmod = "2014-08-11T14:02:00Z"
weight = 35416
keywords = [ "packaging", "disable", "updates" ]
aliases = [ "/questions/35416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to disable "check for updates"?](/questions/35416/is-it-possible-to-disable-check-for-updates)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35416-score" class="post-score" title="current number of votes">0</div><span id="post-35416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to package and deploy Wireshark 1.10.9 and I must have the "check for updates" under the Help icon, disabled, greyed out, or removed. Can someone furnish an answer on how this can be accomplished?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packaging" rel="tag" title="see questions tagged &#39;packaging&#39;">packaging</span> <span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '14, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/1874987e18cf7e801e283b02809de418?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irishbug&#39;s gravatar image" /><p><span>Irishbug</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irishbug has no accepted answers">0%</span></p></div></div><div id="comments-container-35416" class="comments-container"></div><div id="comment-tools-35416" class="comment-tools"></div><div class="clear"></div><div id="comment-35416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35422"></span>

<div id="answer-container-35422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35422-score" class="post-score" title="current number of votes">2</div><span id="post-35422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is an item in the preferences "Check for Updates" (gui.update.enabled in the preferences file) that you could preset to be disabled, but users could easily enable that again.</p><p>It sounds like you really want to restrict your users, and to do that you'll have to compile your own version and in config.nmake comment out the entries for <code>WINSPARKLE_PKG</code> to build without the version updates.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '14, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '14, 20:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-35422" class="comments-container"></div><div id="comment-tools-35422" class="comment-tools"></div><div class="clear"></div><div id="comment-35422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

