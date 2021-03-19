+++
type = "question"
title = "tshark output refining"
description = '''Hello, I&#x27;m using this command to see DNS requests: tshark -pni fxp0 -f &#x27;dst port 53&#x27; -T fields -e dns.qry.name  And the output looks like this: livejournal.com 1 www.youtube.com apis.google.com platform.twitter.com connect.facebook.net 5 cnt.sup.com 6 l-api.livejournal.com l-stat.livejournal.net  I ...'''
date = "2014-04-06T02:04:00Z"
lastmod = "2014-04-07T09:37:00Z"
weight = 31564
keywords = [ "tshark" ]
aliases = [ "/questions/31564" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark output refining](/questions/31564/tshark-output-refining)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31564-score" class="post-score" title="current number of votes">0</div><span id="post-31564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using this command to see DNS requests:</p><pre><code>tshark -pni fxp0 -f &#39;dst port 53&#39; -T fields -e dns.qry.name</code></pre><p>And the output looks like this:</p><pre><code>livejournal.com
1 www.youtube.com
apis.google.com
platform.twitter.com
connect.facebook.net
5 cnt.sup.com
6 l-api.livejournal.com
l-stat.livejournal.net</code></pre><p>I don't understand where those numbers come from (1, 5, 6). And how to suppress those?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '14, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/f87c8f60a3162f616b939a56dcedf780?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tesuto&#39;s gravatar image" /><p><span>tesuto</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tesuto has no accepted answers">0%</span></p></div></div><div id="comments-container-31564" class="comments-container"></div><div id="comment-tools-31564" class="comment-tools"></div><div class="clear"></div><div id="comment-31564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31596"></span>

<div id="answer-container-31596" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31596-score" class="post-score" title="current number of votes">3</div><span id="post-31596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tesuto has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Those numbers are the packet counts.</p><p>Which version of Wireshark are you using? Because this was fixed with Guy's <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=51227">r51227</a> (or <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=5c0baee2a96f752ec093646002f7cdd677e38eb8">r51227</a>) commit on August 9, 2013. It doesn't appear that that fix was backported to the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=history;f=tshark.c;h=618e905e4230814ba4b4d30754ef63a40d12ce10;hb=refs/heads/master-1.10">1.10</a> trunk, so you would need to either:</p><ul><li>Use a development version of Wireshark released after that date, such as <a href="http://www.wireshark.org/download.html#development-rel">1.11.2</a> released on <a href="http://www.wireshark.org/news/20131118.html">November 18, 2013</a> (which is incorrectly indicated as being the 1.11.0 release, but 1.11.0 was released on <a href="http://www.wireshark.org/news/20131015.html">October 15, 2013</a>. Incidentally, 1.11.1 released on <a href="http://www.wireshark.org/news/20131115.html">November 15, 2013</a> is also incorrectly indicated as 1.11.0)</li><li>Download and run a recent <a href="http://www.wireshark.org/download/automated/">automated</a> build.</li><li>Download the Wireshark source code and build your own version with the fix. See <a href="http://www.wireshark.org/develop.html">http://www.wireshark.org/develop.html</a>.</li><li><a href="https://bugs.wireshark.org/bugzilla/">Submit a bug report</a> asking for this fix to be backported to the 1.10 branch (if that's what you're running and want to continue to run it) and then wait for the next 1.10 release with the fix.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '14, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-31596" class="comments-container"><span id="31597"></span><div id="comment-31597" class="comment"><div id="post-31597-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply! I'm using wireshark 1.10.5. Looks like I have to wait until 1.11 version will be available on FreeBSD ports.</p></div><div id="comment-31597-info" class="comment-info"><span class="comment-age">(07 Apr '14, 09:37)</span> <span class="comment-user userinfo">tesuto</span></div></div></div><div id="comment-tools-31596" class="comment-tools"></div><div class="clear"></div><div id="comment-31596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

