+++
type = "question"
title = "RTP Player does not show progress in selected stream(s)"
description = '''Using the latest version of Wireshark (Version 1.12.1 (v1.12.1-0-g01b65bf from master-1.12)), the VoIP (RTP) player no longer shows the progress line and does not update progress during the call. Neither does it reset the control buttons once the RTP stream has ended (you have to manually click the ...'''
date = "2014-10-30T07:06:00Z"
lastmod = "2014-10-30T11:06:00Z"
weight = 37460
keywords = [ "player", "rtp", "voip" ]
aliases = [ "/questions/37460" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Player does not show progress in selected stream(s)](/questions/37460/rtp-player-does-not-show-progress-in-selected-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37460-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using the latest version of Wireshark (Version 1.12.1 (v1.12.1-0-g01b65bf from master-1.12)), the VoIP (RTP) player no longer shows the progress line and does not update progress during the call. Neither does it reset the control buttons once the RTP stream has ended (you have to manually click the Stop button). I know Wireshark used to show progress when playing VoIP calls.</p></div><div id="question-tags" class="tags-container tags">player rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/e8a2fffd463507c000c10e5b0e3bca8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Icon&#39;s gravatar image" /><p>Icon<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Icon has no accepted answers">0%</span></p></div></div><div id="comments-container-37460" class="comments-container"></div><div id="comment-tools-37460" class="comment-tools"></div><div class="clear"></div><div id="comment-37460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37471"></span>

<div id="answer-container-37471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37471-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds a lot like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10307">bug 10307</a> which was supposed to be fixed in 1.12.1.</p><p>What version of glib do you have installed (assuming this isn't Windows)? The fix (well, the hack around a PortAudio bug) for that bug will only work if you have glib 2.28 or greater; I'm guessing you don't have 2.28 or later.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '14, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37471" class="comments-container"></div><div id="comment-tools-37471" class="comment-tools"></div><div class="clear"></div><div id="comment-37471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

