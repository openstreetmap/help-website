+++
type = "question"
title = "RTP player wave graph messed up"
description = '''Hello folks!, i have a question: I work in a telecomunications company, and use to work with Wireshark making telephone call analysis. For some time now, with the latests versions of Wireshark, i have kind of a &quot;visual&quot; problem with the RTP Player. When i deploy a call in the RTP player, it seems go...'''
date = "2014-02-11T12:44:00Z"
lastmod = "2014-02-11T13:02:00Z"
weight = 29714
keywords = [ "player", "rtp", "garbage" ]
aliases = [ "/questions/29714" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP player wave graph messed up](/questions/29714/rtp-player-wave-graph-messed-up)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29714-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello folks!, i have a question: I work in a telecomunications company, and use to work with Wireshark making telephone call analysis. For some time now, with the latests versions of Wireshark, i have kind of a "visual" problem with the RTP Player. When i deploy a call in the RTP player, it seems good, but when i hit the play button, it plays, but as the time position line advances, it starts messing up the wave graph. Its not really unusable, but is kind of unconfortable, as i use the wave graph as visual reference for the analysis.</p><p>Is it something with the S.O. (WinXP) or DirectX or anything like that? I am using windows XP, and until a few versions, it worked just fine.</p><p>Below are images of how it looks at first, and after playback for some seconds. Has anybody else seen this?</p><p>Thanks a lot in advance, regards!!</p><p><strong>Before Playback:</strong> <a href="http://es.tinypic.com?ref=2d8l1c6"><img src="http://i58.tinypic.com/2d8l1c6.jpg" alt="Image and video hosting by TinyPic" /></a>,</p><p><strong>After playback:</strong> <a href="http://es.tinypic.com?ref=35b9o4p"><img src="http://i60.tinypic.com/35b9o4p.png" alt="Image and video hosting by TinyPic" /></a></p></div><div id="question-tags" class="tags-container tags">player rtp garbage</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/e3ec08a10a6d4214a8324e1f30fc2b33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnnyV&#39;s gravatar image" /><p>JohnnyV<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnnyV has no accepted answers">0%</span></p></img></div></div><div id="comments-container-29714" class="comments-container"></div><div id="comment-tools-29714" class="comment-tools"></div><div class="clear"></div><div id="comment-29714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29715"></span>

<div id="answer-container-29715" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29715-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This would appear to be the same as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7557">Bug 7557</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></img></div></div><div id="comments-container-29715" class="comments-container"><span id="29729"></span><div id="comment-29729" class="comment"><div id="post-29729-score" class="comment-score"></div><div class="comment-text"><p>And <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8007">bug 8007</a> the culprit is the switch to Cairo for witch the "XOR" function does not work. The code would have to be rewritten to work properly with Cairo possibly in the same manor as the TCPgraphs "crosshair".</p></div><div id="comment-29729-info" class="comment-info"><span class="comment-age">(11 Feb '14, 22:11)</span> Anders ♦</div></div><span id="29757"></span><div id="comment-29757" class="comment"><div id="post-29757-score" class="comment-score"></div><div class="comment-text"><p>Well thanks folks for the answers!, I knew i couldn't be the first one noticing this. I cant believe, tho, it seems to be of so unfrequent use that the bug is still there from 2012, ... is there anything i can do to fix it so i can recover full functionality? Or my best option is to switch back to Wireshark 1.6.8?</p><p>Regards!</p></div><div id="comment-29757-info" class="comment-info"><span class="comment-age">(12 Feb '14, 05:21)</span> JohnnyV</div></div><span id="29766"></span><div id="comment-29766" class="comment"><div id="post-29766-score" class="comment-score"></div><div class="comment-text"><blockquote><p>is there anything i can do to fix it so i can recover full functionality?</p></blockquote><p>Do the neccessary code changes or even better port the functionality to Qt ;-)</p><p>It seems like no one needs this bad enough to sit down and fix the code :-(</p></div><div id="comment-29766-info" class="comment-info"><span class="comment-age">(12 Feb '14, 06:49)</span> Anders ♦</div></div><span id="29810"></span><div id="comment-29810" class="comment"><div id="post-29810-score" class="comment-score"></div><div class="comment-text"><p>Well... i am not a programmer, my only trades with coding have been with... Pascal, and that was like 15 years ago, so, as much as i would like to be able to do that, i'm of no use for this one. I suppose i will revert to 1.6.8. , as long as there have been little to no improvements to the voip analysis capabilities in the latest versions...</p><p>Thanks a lot anyway!</p><p>Regards, and good luck for all!</p></div><div id="comment-29810-info" class="comment-info"><span class="comment-age">(12 Feb '14, 17:11)</span> JohnnyV</div></div></div><div id="comment-tools-29715" class="comment-tools"></div><div class="clear"></div><div id="comment-29715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

