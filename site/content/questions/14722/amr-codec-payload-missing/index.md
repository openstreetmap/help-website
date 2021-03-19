+++
type = "question"
title = "AMR codec payload missing"
description = '''Hi, I am trying to capture an AMR codec generated using Navtel. When I decode it to RTP, the trace shows &quot;RTP EVENT&quot; instead of &quot;RTP&quot; and the payload is missing in all of those packets. I have used the same setup for various other codecs like PCMU, PCMA, AMR-WB, etc which are captured fine. What cou...'''
date = "2012-10-04T13:58:00Z"
lastmod = "2012-10-04T23:05:00Z"
weight = 14722
keywords = [ "captureerror", "codec", "payload", "rtp" ]
aliases = [ "/questions/14722" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [AMR codec payload missing](/questions/14722/amr-codec-payload-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14722-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to capture an AMR codec generated using Navtel. When I decode it to RTP, the trace shows "RTP EVENT" instead of "RTP" and the payload is missing in all of those packets.</p><p>I have used the same setup for various other codecs like PCMU, PCMA, AMR-WB, etc which are captured fine. What could be the cause and a possible solution?</p><p>P.S.: I have just started off as an intern, so I am quite new to Wireshark!</p></div><div id="question-tags" class="tags-container tags">captureerror codec payload rtp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '12, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/9b8b471264a9caa8487e86e8a71f2db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Newbie_Acme&#39;s gravatar image" /><p>Newbie_Acme<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Newbie_Acme has no accepted answers">0%</span></p></div></div><div id="comments-container-14722" class="comments-container"></div><div id="comment-tools-14722" class="comment-tools"></div><div class="clear"></div><div id="comment-14722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14728"></span>

<div id="answer-container-14728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want RTP event out of the way you should look at the preference settings for the RTP Event protocol. There's probably a payload type set that the Navtel uses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '12, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14728" class="comments-container"></div><div id="comment-tools-14728" class="comment-tools"></div><div class="clear"></div><div id="comment-14728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

