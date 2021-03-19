+++
type = "question"
title = "There are no interfaces on which a capture can be done."
description = '''I&#x27;ve made all steps described in wiki.wireshark.org/CaptureSetup/CapturePrivileges, but I still get next error message  There are no interfaces on which a capture can be done.  Where I&#x27;ve made a mistake? $ groups dima lp wheel games video audio optical storage power wireshark users $ ls -l /usr/bin/...'''
date = "2012-08-15T03:11:00Z"
lastmod = "2012-08-15T04:15:00Z"
weight = 13649
keywords = [ "captureerror", "error" ]
aliases = [ "/questions/13649" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [There are no interfaces on which a capture can be done.](/questions/13649/there-are-no-interfaces-on-which-a-capture-can-be-done)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13649-score" class="post-score" title="current number of votes">1</div><span id="post-13649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've made all steps described in <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">wiki.wireshark.org/CaptureSetup/CapturePrivileges</a>, but I still get next error message</p><blockquote><p>There are no interfaces on which a capture can be done.</p></blockquote><p>Where I've made a mistake?</p><pre><code>$ groups dima
lp wheel games video audio optical storage power wireshark users
$ ls -l /usr/bin/dumpcap 
-rwxr-xr-- 1 root wireshark 77000 Jul 29 12:07 /usr/bin/dumpcap
$ getcap /usr/bin/dumpcap 
/usr/bin/dumpcap = cap_net_admin,cap_net_raw+eip</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-captureerror" rel="tag" title="see questions tagged &#39;captureerror&#39;">captureerror</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '12, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/5dd277c40ada2b417b3c832997b0729f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jofsey&#39;s gravatar image" /><p><span>Jofsey</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jofsey has no accepted answers">0%</span></p></div></div><div id="comments-container-13649" class="comments-container"></div><div id="comment-tools-13649" class="comment-tools"></div><div class="clear"></div><div id="comment-13649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13654"></span>

<div id="answer-container-13654" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13654-score" class="post-score" title="current number of votes">2</div><span id="post-13654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jofsey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capabilities and group seems in order. You may have to login again to make it effective.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '12, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-13654" class="comments-container"></div><div id="comment-tools-13654" class="comment-tools"></div><div class="clear"></div><div id="comment-13654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13650"></span>

<div id="answer-container-13650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13650-score" class="post-score" title="current number of votes">1</div><span id="post-13650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have no idea if this helps but the wiki page states the capabilities required are:</p><pre><code>CAP_NET_RAW+eip CAP_NET_ADMIN+eip</code></pre><p>You seem to be missing the <code>+eip</code> from <code>CAP_NET_ADMIN</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '12, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13650" class="comments-container"><span id="13651"></span><div id="comment-13651" class="comment"><div id="post-13651-score" class="comment-score"></div><div class="comment-text"><p>I can't.</p><pre><code>$ setcap &#39;CAP_NET_RAW+eip CAP_NET_ADMIN+eip&#39; /usr/bin/dumpcap
$ getcap /usr/bin/dumpcap 
/usr/bin/dumpcap = cap_net_admin,cap_net_raw+eip</code></pre></div><div id="comment-13651-info" class="comment-info"><span class="comment-age">(15 Aug '12, 03:23)</span> <span class="comment-user userinfo">Jofsey</span></div></div><span id="13653"></span><div id="comment-13653" class="comment"><div id="post-13653-score" class="comment-score"></div><div class="comment-text"><p>OK, what OS are you using?</p></div><div id="comment-13653-info" class="comment-info"><span class="comment-age">(15 Aug '12, 04:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-13650" class="comment-tools"></div><div class="clear"></div><div id="comment-13650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

