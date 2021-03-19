+++
type = "question"
title = "Glib:Error How to analyze?"
description = '''Hi. During search period to find an video streaming error, I arrive this error: (Wireshark.exe:11980): Glib-ERROR - , gmem.c:llO: fo il•d to allocate 8388608 bytes To me, it seems to occur the same error after run this application for a while, approx- 2-5 minutes. How to analyze this, and find a sol...'''
date = "2014-09-08T18:44:00Z"
lastmod = "2014-09-09T14:17:00Z"
weight = 36090
keywords = [ "glib", "error" ]
aliases = [ "/questions/36090" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Glib:Error How to analyze?](/questions/36090/gliberror-how-to-analyze)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36090-score" class="post-score" title="current number of votes">0</div><span id="post-36090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. During search period to find an video streaming error, I arrive this error: (Wireshark.exe:11980): Glib-ERROR - , gmem.c:llO: fo il•d to allocate 8388608 bytes</p><p>To me, it seems to occur the same error after run this application for a while, approx- 2-5 minutes. How to analyze this, and find a solution to fix?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '14, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/6d89fc78202146a41f641e8c0091c6ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roof-55&#39;s gravatar image" /><p><span>Roof-55</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roof-55 has no accepted answers">0%</span></p></div></div><div id="comments-container-36090" class="comments-container"></div><div id="comment-tools-36090" class="comment-tools"></div><div class="clear"></div><div id="comment-36090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36115"></span>

<div id="answer-container-36115" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36115-score" class="post-score" title="current number of votes">0</div><span id="post-36115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is failing to allocate around 8 Gbytes of memory. That's a fairly (but not completely unreasonably) large chunk of memory. I'd say your system is running <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory</a> (rather than, say, running into a bug which is causing Wireshark to try to allocate a ridiculously large amount of memory).</p><p>You could try upgrading to the latest release if you're not already on it (1.12.0) to see if that helps, otherwise, see the linked page for some hints which can reduce Wireshark's memory usage.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '14, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36115" class="comments-container"><span id="36129"></span><div id="comment-36129" class="comment"><div id="post-36129-score" class="comment-score"></div><div class="comment-text"><p>The mainboard, Asus X79 deluxe are supplied with 64Gb DDR3 RAM. System suing at this moment 11,6Gb, stranger to me why this failure occur, thinking flush of memory available for use to Sharwire. My 6 core CPU and Intel SSD together shod make this task as easily to match. I try to check my version, but I for sure it shod be the latest one.</p></div><div id="comment-36129-info" class="comment-info"><span class="comment-age">(09 Sep '14, 13:54)</span> <span class="comment-user userinfo">Roof-55</span></div></div><span id="36130"></span><div id="comment-36130" class="comment"><div id="post-36130-score" class="comment-score"></div><div class="comment-text"><p>Are you running a 32- or 64-bit version of Wireshark? (wireshark -v or tshark -v will tell you that as well as the version)</p><p>It could be you're not running out of system memory but just process address space. You could also watch how much memory is in use <em>by Wireshark</em> at the time of the crash.</p></div><div id="comment-36130-info" class="comment-info"><span class="comment-age">(09 Sep '14, 14:17)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-36115" class="comment-tools"></div><div class="clear"></div><div id="comment-36115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

