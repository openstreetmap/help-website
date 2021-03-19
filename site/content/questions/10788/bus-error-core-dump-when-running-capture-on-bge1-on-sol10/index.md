+++
type = "question"
title = "bus error core dump when running capture on bge1 on sol10."
description = '''why does wireshark 1.6.4 get a bus error core dump when running capture on bge1? it does not core dump on bge0. I am running solaris 10.'''
date = "2012-05-08T12:14:00Z"
lastmod = "2012-05-09T10:06:00Z"
weight = 10788
keywords = [ "core" ]
aliases = [ "/questions/10788" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [bus error core dump when running capture on bge1 on sol10.](/questions/10788/bus-error-core-dump-when-running-capture-on-bge1-on-sol10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10788-score" class="post-score" title="current number of votes">0</div><span id="post-10788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>why does wireshark 1.6.4 get a bus error core dump when running capture on bge1? it does not core dump on bge0. I am running solaris 10.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-core" rel="tag" title="see questions tagged &#39;core&#39;">core</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '12, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/1c8bd044e036207f4c01533b4d0b4d64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="empressdawn2&#39;s gravatar image" /><p><span>empressdawn2</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="empressdawn2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 May '12, 12:15</strong> </span></p></div></div><div id="comments-container-10788" class="comments-container"></div><div id="comment-tools-10788" class="comment-tools"></div><div class="clear"></div><div id="comment-10788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10790"></span>

<div id="answer-container-10790" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10790-score" class="post-score" title="current number of votes">0</div><span id="post-10790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Chances are the problem isn't with the interface it's with what's being captured (e.g., the type of traffic). Wireshark shouldn't be getting a bus error in this case, so I'd suggest:</p><p>1) Upgrade to 1.6.7 to see if the problem persists (actually 1.6.8--which hasn't been released yet--fixes a problem which causes bus errors on SPARC).</p><p>2) If it's still a problem, <a href="https://bugs.wireshark.org">open a bug</a> and attach the capture file which causes the problem to happen. The <a href="http://www.wireshark.org/faq.html#q7.12">FAQ</a> tells you where to find the temporary capture file if it crashes during a live capture (it would be good to verify that opening this file causes the bus error). It would also be helpful if you can a) get a core file (you might need to check your "ulimit -c") and b) run pstack on it to get a backtrace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-10790" class="comments-container"><span id="10793"></span><div id="comment-10793" class="comment"><div id="post-10793-score" class="comment-score"></div><div class="comment-text"><p>the latest version I see made for oracle/solaris is the one I am running now which is 1.6.4 found on wireshark's third party link site. where do you see 1.6.7 for solaris?</p></div><div id="comment-10793-info" class="comment-info"><span class="comment-age">(08 May '12, 14:55)</span> <span class="comment-user userinfo">empressdawn2</span></div></div><span id="10794"></span><div id="comment-10794" class="comment"><div id="post-10794-score" class="comment-score"></div><div class="comment-text"><p>(I converted your Answer to a Comment--please see the FAQ.)</p><p>1.6.7 is the latest version in the 1.6 branch. I don't know if anyone supplies a package including that version (I compile my own).</p><p>Even if you can't upgrade, the pstack of a core file may lend a clue as to whether the problem has been fixed in later versions or not. A bug report with a sample capture would give a more definitive answer.</p></div><div id="comment-10794-info" class="comment-info"><span class="comment-age">(08 May '12, 15:00)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="10844"></span><div id="comment-10844" class="comment"><div id="post-10844-score" class="comment-score"></div><div class="comment-text"><p>For the record: bug 7240 was opened to track this.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7240">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7240</a></p></div><div id="comment-10844-info" class="comment-info"><span class="comment-age">(09 May '12, 10:06)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-10790" class="comment-tools"></div><div class="clear"></div><div id="comment-10790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

