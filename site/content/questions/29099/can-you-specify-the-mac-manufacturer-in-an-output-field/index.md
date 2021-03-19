+++
type = "question"
title = "Can you specify the MAC manufacturer in an output field ?"
description = '''I&#x27;m outputting MAC addresses and other fields using the -T option: -T fields -e wlan.sa that works fine, but in addition I&#x27;d like the manufacturer information e.g. e0:f5:c6:12:34 Intel'''
date = "2014-01-22T08:21:00Z"
lastmod = "2014-01-22T08:53:00Z"
weight = 29099
keywords = [ "manuf", "mac-address" ]
aliases = [ "/questions/29099" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can you specify the MAC manufacturer in an output field ?](/questions/29099/can-you-specify-the-mac-manufacturer-in-an-output-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29099-score" class="post-score" title="current number of votes">0</div><span id="post-29099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm outputting MAC addresses and other fields using the -T option:</p><p>-T fields -e wlan.sa</p><p>that works fine, but in addition I'd like the manufacturer information e.g.</p><p>e0:f5:c6:12:34 Intel</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-manuf" rel="tag" title="see questions tagged &#39;manuf&#39;">manuf</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/869cf11edc0cc880cc04931d386f4321?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikerr&#39;s gravatar image" /><p><span>mikerr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikerr has no accepted answers">0%</span></p></div></div><div id="comments-container-29099" class="comments-container"></div><div id="comment-tools-29099" class="comment-tools"></div><div class="clear"></div><div id="comment-29099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29100"></span>

<div id="answer-container-29100" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29100-score" class="post-score" title="current number of votes">1</div><span id="post-29100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try the field name <code>wlan.sa_resolved</code>. You might also need to enable MAC name resolution with a <code>-N m</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '14, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29100" class="comments-container"><span id="29101"></span><div id="comment-29101" class="comment"><div id="post-29101-score" class="comment-score"></div><div class="comment-text"><p>Looks good, but after some digging I've found the Raspberry Pi has an older version 1.8.2 which doesn't support that</p></div><div id="comment-29101-info" class="comment-info"><span class="comment-age">(22 Jan '14, 08:53)</span> <span class="comment-user userinfo">mikerr</span></div></div></div><div id="comment-tools-29100" class="comment-tools"></div><div class="clear"></div><div id="comment-29100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

