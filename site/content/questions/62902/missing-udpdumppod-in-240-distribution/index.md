+++
type = "question"
title = "Missing UDPDUMP.POD in 2.4.0 distribution"
description = '''Hi guys -  the 2.4.0 build includes references to udpdump.pod but this isn&#x27;t included. I&#x27;ve manually added it to my build from the git sources but a bit of a weird one.'''
date = "2017-07-19T21:50:00Z"
lastmod = "2017-07-20T06:40:00Z"
weight = 62902
keywords = [ "udpdump", "build_error" ]
aliases = [ "/questions/62902" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Missing UDPDUMP.POD in 2.4.0 distribution](/questions/62902/missing-udpdumppod-in-240-distribution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62902-score" class="post-score" title="current number of votes">0</div><span id="post-62902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys -</p><p>the 2.4.0 build includes references to udpdump.pod but this isn't included. I've manually added it to my build from the git sources but a bit of a weird one.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udpdump" rel="tag" title="see questions tagged &#39;udpdump&#39;">udpdump</span> <span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '17, 21:50</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p><span>Scott Harman</span><br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-62902" class="comments-container"></div><div id="comment-tools-62902" class="comment-tools"></div><div class="clear"></div><div id="comment-62902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62904"></span>

<div id="answer-container-62904" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62904-score" class="post-score" title="current number of votes">0</div><span id="post-62904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Scott Harman has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This should go into a <a href="https://bugs.wireshark.org/bugzilla/">bug report</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '17, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62904" class="comments-container"><span id="62905"></span><div id="comment-62905" class="comment"><div id="post-62905-score" class="comment-score"></div><div class="comment-text"><p>Yup - done now bug number: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13903">13903</a></p></div><div id="comment-62905-info" class="comment-info"><span class="comment-age">(19 Jul '17, 23:11)</span> <span class="comment-user userinfo">Scott Harman</span></div></div><span id="62928"></span><div id="comment-62928" class="comment"><div id="post-62928-score" class="comment-score"></div><div class="comment-text"><p>And 'instantly' fixed. Therefore note to All: Bugs have to be reported in <a href="https://bugs.wireshark.org/bugzilla/">bugzilla</a>, not here.</p></div><div id="comment-62928-info" class="comment-info"><span class="comment-age">(20 Jul '17, 06:40)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-62904" class="comment-tools"></div><div class="clear"></div><div id="comment-62904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

