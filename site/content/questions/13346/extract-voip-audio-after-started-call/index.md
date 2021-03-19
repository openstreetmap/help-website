+++
type = "question"
title = "Extract VoIP audio AFTER started call"
description = '''Excuse me for my not perfect english. I have recorded some Calls becouse my ISP and I have problems (tech). But I cant extract any audio from VoIP calls. I have asked google, and I found the problem. I must start Wireshark recording, then do any Call via VoIP. And I started a Call, then started Wire...'''
date = "2012-08-03T05:03:00Z"
lastmod = "2012-08-03T05:54:00Z"
weight = 13346
keywords = [ "audio", "call", "fritzbox", "voip", "wireshark" ]
aliases = [ "/questions/13346" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Extract VoIP audio AFTER started call](/questions/13346/extract-voip-audio-after-started-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13346-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Excuse me for my not perfect english. I have recorded some Calls becouse my ISP and I have problems (tech).</p><p>But I cant extract any audio from VoIP calls. I have asked google, and I found the problem.</p><p>I must start Wireshark recording, then do any Call via VoIP. And I started a Call, then started Wireshark recording.</p><p>Have I any chance to get Audio from the Wireshark recordings with my fault?</p></div><div id="question-tags" class="tags-container tags">audio call fritzbox voip wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '12, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/3fb42e0205518410ee559cfc17415eaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Danni&#39;s gravatar image" /><p>Danni<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Danni has no accepted answers">0%</span></p></div></div><div id="comments-container-13346" class="comments-container"></div><div id="comment-tools-13346" class="comment-tools"></div><div class="clear"></div><div id="comment-13346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13348"></span>

<div id="answer-container-13348" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13348-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try setting the RTP preference (Edit-&gt;Preferences-&gt;Protocols-&gt;RTP) "Try to decode RTP outside of conversations". This will make the RTP dissector try to heuristically recognize UDP packets as RTP instead of relying on signaling (e.g., SIP) to tell it which UDP packets to look at.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '12, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-13348" class="comments-container"><span id="13349"></span><div id="comment-13349" class="comment"><div id="post-13349-score" class="comment-score"></div><div class="comment-text"><p>Thank you. That helps. Thank you very much! :D</p></div><div id="comment-13349-info" class="comment-info"><span class="comment-age">(03 Aug '12, 06:42)</span> Danni</div></div></div><div id="comment-tools-13348" class="comment-tools"></div><div class="clear"></div><div id="comment-13348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

