+++
type = "question"
title = "Dropbox using a lot of bandwidth even when fully synced"
description = '''Hi all, Have an interesting problem.  Dropbox client: even when fully synced (green tick), it continues uses a substantial amount of bandwidth (20GB UPLOAD across a few days). Upgraded Dropbox to a new version (just to make sure Dropbox executable is not compromised), but the issue remains. Reboots,...'''
date = "2015-11-11T19:44:00Z"
lastmod = "2015-11-12T02:47:00Z"
weight = 47528
keywords = [ "dropbox", "amazon", "retransmissions" ]
aliases = [ "/questions/47528" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dropbox using a lot of bandwidth even when fully synced](/questions/47528/dropbox-using-a-lot-of-bandwidth-even-when-fully-synced)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47528-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Have an interesting problem.</p><p>Dropbox client: even when fully synced (green tick), it continues uses a substantial amount of bandwidth (20GB UPLOAD across a few days). Upgraded Dropbox to a new version (just to make sure Dropbox executable is not compromised), but the issue remains. Reboots, restarts of client, etc. all do not help. This happens on only one PC, others are fine. As soon as Dropbox client is live, the traffic resumes, even though it's fully synced already.</p><p>Capture shows lots of retransmissions and other things, mainly to IP 52.20.119.195 which seems to be Amazon, and googling shows that Dropbox uses Amazon. Previous capture was to IP 52.3.199.155, also Amazon.</p><p>Any ideas what is going on here?</p><p>Capture: <a href="https://www.cloudshark.org/captures/fc93850bcba3">https://www.cloudshark.org/captures/fc93850bcba3</a></p></div><div id="question-tags" class="tags-container tags">dropbox amazon retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '15, 19:44</strong></p><img src="https://secure.gravatar.com/avatar/0a725291807794b43970ceb7d02f0174?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcw&#39;s gravatar image" /><p>pcw<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcw has no accepted answers">0%</span></p></div></div><div id="comments-container-47528" class="comments-container"><span id="47539"></span><div id="comment-47539" class="comment"><div id="post-47539-score" class="comment-score"></div><div class="comment-text"><p>the connection to the dropbox servers is <strong>encrypted</strong>, so nobody will be able to tell you <strong>what</strong> kind of data your dropbox client is transmitting to the NSA. Please ask the Dropbox support team. See also the answer of @grahamb.</p></div><div id="comment-47539-info" class="comment-info"><span class="comment-age">(12 Nov '15, 02:52)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47528" class="comment-tools"></div><div class="clear"></div><div id="comment-47528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47538"></span>

<div id="answer-container-47538" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47538-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Seems to me that this is a question for DropBox support. While Wireshark can show the traffic being sent, it can't tell you <strong>why</strong> it's being sent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47538" class="comments-container"></div><div id="comment-tools-47538" class="comment-tools"></div><div class="clear"></div><div id="comment-47538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

