+++
type = "question"
title = "Wireshark crashing"
description = '''Hi all, thanks for being here. I&#x27;m running Wireshark 1.6.7 on Ubuntu 12.04.Total newbie.Left side of screen &quot;capture&quot; box says &quot;no interface can be used for capturing in this system with the current configuration&quot;. Striking 1st top left icon for &quot;listing available capture interfaces&quot; gives me a pop-...'''
date = "2012-10-11T00:13:00Z"
lastmod = "2012-10-11T00:23:00Z"
weight = 14914
keywords = [ "maybe", "monitor", "mode" ]
aliases = [ "/questions/14914" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashing](/questions/14914/wireshark-crashing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14914-score" class="post-score" title="current number of votes">0</div><span id="post-14914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, thanks for being here. I'm running Wireshark 1.6.7 on Ubuntu 12.04.Total newbie.Left side of screen "capture" box says "no interface can be used for capturing in this system with the current configuration". Striking 1st top left icon for "listing available capture interfaces" gives me a pop-up box with a red circle w/ white bar inside stating "There are no interfaces on which a capture can be done." striking 2nd icon from top left "show capture options" gives me a "capture" config type box. After entering the 1st letter of my interface name wireshark crashes,shuts down, gone. What the hey ? Right ? I have set the described permissions for non super users to capture packets.Now have a new "red circle box", sez "Couldn't run /usr/bin/dumpcap in child process: Permission denied". after removing those permissions again, i now am seeing the original "no interface can be used for capturing in this system with the current configuration". Hand up to the new guy ? thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-maybe" rel="tag" title="see questions tagged &#39;maybe&#39;">maybe</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/2c674f92ab74d0e088f156a1993f6a90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tooler512&#39;s gravatar image" /><p><span>tooler512</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tooler512 has no accepted answers">0%</span></p></div></div><div id="comments-container-14914" class="comments-container"></div><div id="comment-tools-14914" class="comment-tools"></div><div class="clear"></div><div id="comment-14914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14915"></span>

<div id="answer-container-14915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14915-score" class="post-score" title="current number of votes">0</div><span id="post-14915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please run this command in a terminal window. That should solve the problem:</p><blockquote><p><code>sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap</code><br />
</p></blockquote><p>See here: <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '12, 00:23</strong> </span></p></div></div><div id="comments-container-14915" class="comments-container"></div><div id="comment-tools-14915" class="comment-tools"></div><div class="clear"></div><div id="comment-14915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

