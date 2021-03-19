+++
type = "question"
title = "Why is Wireshark Crashing when I print selected packets?"
description = '''I am trying to print a specific packet in Windows 10 using Wireshark 2.0.2 (64 bit), but every time I choose &quot;Selected packets only,&quot; or &quot;Range,&quot; Wireshark crashes. Any suggestions on how to fix this? I have uninstalled and reinstalled the program, and have rebooted, but to no avail. Thank you in ad...'''
date = "2016-03-11T16:35:00Z"
lastmod = "2016-03-11T18:53:00Z"
weight = 50837
keywords = [ "crash", "windows10", "packet" ]
aliases = [ "/questions/50837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is Wireshark Crashing when I print selected packets?](/questions/50837/why-is-wireshark-crashing-when-i-print-selected-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50837-score" class="post-score" title="current number of votes">0</div><span id="post-50837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to print a specific packet in Windows 10 using Wireshark 2.0.2 (64 bit), but every time I choose "Selected packets only," or "Range," Wireshark crashes. Any suggestions on how to fix this? I have uninstalled and reinstalled the program, and have rebooted, but to no avail. Thank you in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-windows10" rel="tag" title="see questions tagged &#39;windows10&#39;">windows10</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '16, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/02f9dacf1fab4ec921b853f98f98f010?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anakela&#39;s gravatar image" /><p><span>anakela</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anakela has no accepted answers">0%</span></p></div></div><div id="comments-container-50837" class="comments-container"></div><div id="comment-tools-50837" class="comment-tools"></div><div class="clear"></div><div id="comment-50837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50838"></span>

<div id="answer-container-50838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50838-score" class="post-score" title="current number of votes">0</div><span id="post-50838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12040">bug 12040</a>. The only ways to fix it are to wait for 2.0.3, if you can't wait, download one of the 2.0.3-rc0 builds from <a href="https://www.wireshark.org/download/automated/win64/">the Wireshark 64-bit Windows automated build area</a> and install and run that (you'll probably want to install 2.0.3 over that once it's released, as 2.0.3 will probably have more bug fixes than any of the pre-2.0.3 builds).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '16, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50838" class="comments-container"></div><div id="comment-tools-50838" class="comment-tools"></div><div class="clear"></div><div id="comment-50838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

