+++
type = "question"
title = "Building on Solaris 8"
description = '''I&#x27;ve been trying to build wireshark 1.4.1 for Solaris 8 on sparc. I haven&#x27;t had much luck. My first problem was that I had an older gtk than what is required so I had to try and build it without much luck. I have ended up building cairo, pango, libiconv, GNU m4, GNU sed, glib, flex, and pkgconfig. A...'''
date = "2010-11-03T20:37:00Z"
lastmod = "2010-11-04T12:46:00Z"
weight = 812
keywords = [ "solaris" ]
aliases = [ "/questions/812" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Building on Solaris 8](/questions/812/building-on-solaris-8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-812-score" class="post-score" title="current number of votes">0</div><span id="post-812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to build wireshark 1.4.1 for Solaris 8 on sparc. I haven't had much luck. My first problem was that I had an older gtk than what is required so I had to try and build it without much luck. I have ended up building cairo, pango, libiconv, GNU m4, GNU sed, glib, flex, and pkgconfig. At every stage I seen to have a problem. I had to have a couple of empty shell scripts for pod2html and pod2man.</p><p>Has anyone succeeded in building wireshark on Solaris 8? I am just as happy to give up but someone here wanted to use it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-solaris" rel="tag" title="see questions tagged &#39;solaris&#39;">solaris</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '10, 20:37</strong></p><img src="https://secure.gravatar.com/avatar/873f0c07a86cb00a3a5b957ef002b0ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TV1&#39;s gravatar image" /><p><span>TV1</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TV1 has no accepted answers">0%</span></p></div></div><div id="comments-container-812" class="comments-container"></div><div id="comment-tools-812" class="comment-tools"></div><div class="clear"></div><div id="comment-812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="814"></span>

<div id="answer-container-814" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-814-score" class="post-score" title="current number of votes">0</div><span id="post-814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I haven't tried a build on Solaris, but I note that you can download Solaris 8 binaries (SPARC or x86) for Wireshark 1.2.10 from <a href="http://www.sunfreeware.com">http://www.sunfreeware.com</a>. If you don't need features specific to later releases, that might be the easiest path for you...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '10, 20:44</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-814" class="comments-container"><span id="815"></span><div id="comment-815" class="comment"><div id="post-815-score" class="comment-score"></div><div class="comment-text"><p>Actually I want the 1.4.0 version of wireshark that is why I am trying to build it from the source. I found the 1.2.10 version but I want to be able to decode the DIS (Distributed Interactive Simulation) protocol and the early version just didn't decode enough of the messages that I am interested.</p></div><div id="comment-815-info" class="comment-info"><span class="comment-age">(03 Nov '10, 20:47)</span> <span class="comment-user userinfo">TV1</span></div></div><span id="822"></span><div id="comment-822" class="comment"><div id="post-822-score" class="comment-score"></div><div class="comment-text"><p>I'm not able to check at the moment, but does sunfreeware have recent packages for gtk?</p></div><div id="comment-822-info" class="comment-info"><span class="comment-age">(04 Nov '10, 12:46)</span> <span class="comment-user userinfo">GeonJay</span></div></div></div><div id="comment-tools-814" class="comment-tools"></div><div class="clear"></div><div id="comment-814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="821"></span>

<div id="answer-container-821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-821-score" class="post-score" title="current number of votes">0</div><span id="post-821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We <a href="http://buildbot.wireshark.org/trunk/waterfall">build Wireshark all day long</a> on Solaris 10. I'm not aware of any issue that would prevent a build on Solaris 8. If there is, that's a bug and should be fixed. The Solaris 10 builder uses support packages and libraries from <a href="http://www.blastwave.org/">Blastwave</a>. They also have Wireshark packages but the latest is 1.2.2.</p><p>An alternative might be to use SSH to pipe the capture data from the Solaris 8 machine to a machine running Wireshark 1.4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '10, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-821" class="comments-container"></div><div id="comment-tools-821" class="comment-tools"></div><div class="clear"></div><div id="comment-821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

