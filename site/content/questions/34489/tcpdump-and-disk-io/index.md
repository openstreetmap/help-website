+++
type = "question"
title = "tcpdump and disk I/O"
description = '''hello, I am using tcpdump on Linux and going to know how tcpdump write to disk ? Raw mode or cook mode ? It means tcpdump write to disk or Linux write to disk ?  Thank you '''
date = "2014-07-08T20:55:00Z"
lastmod = "2014-07-08T21:49:00Z"
weight = 34489
keywords = [ "tcpdump" ]
aliases = [ "/questions/34489" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tcpdump and disk I/O](/questions/34489/tcpdump-and-disk-io)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34489-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, I am using tcpdump on Linux and going to know how tcpdump write to disk ? Raw mode or cook mode ? It means tcpdump write to disk or Linux write to disk ? Thank you</p></div><div id="question-tags" class="tags-container tags">tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '14, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/d4b0725fbcdc688d55ded6e98ca5e35f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mhch&#39;s gravatar image" /><p>mhch<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mhch has no accepted answers">0%</span></p></div></div><div id="comments-container-34489" class="comments-container"><span id="34494"></span><div id="comment-34494" class="comment"><div id="post-34494-score" class="comment-score"></div><div class="comment-text"><p>Hm.. you could have answered that question yourself by applying logical reasoning.</p><p>Does tcpdump create a <strong>file</strong> (in a filesystem) if you use it with option -w?</p><p>If yes, <strong>raw</strong> disk mode does not sound like a reasonable option, does it ;-))</p></div><div id="comment-34494-info" class="comment-info"><span class="comment-age">(09 Jul '14, 01:24)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34489" class="comment-tools"></div><div class="clear"></div><div id="comment-34489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34490"></span>

<div id="answer-container-34490" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34490-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Tcpdump, like Wireshark and the programs that are part of it, and almost all programs running on Windows, Linux, OS X, Solaris, *BSD, and all other UN*Xes (and most <em>other</em> operating systems on the planet), write files out through the file system.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 21:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34490" class="comments-container"></div><div id="comment-tools-34490" class="comment-tools"></div><div class="clear"></div><div id="comment-34490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

