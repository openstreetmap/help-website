+++
type = "question"
title = "RTP player voice playback problem"
description = '''hi, I would like to ask a question about RTP streams playback. When I finished rtp packet capture and perform voice packet playback, I can not hear any sound. I found Sample Rate (Hz) field shows zero, instead of 8000 (as shown below). How do I resolve this issue ?Is there a correlation between this...'''
date = "2016-03-06T20:40:00Z"
lastmod = "2016-03-06T23:07:00Z"
weight = 50731
keywords = [ "udp", "codecs", "rtp", "voip", "rtp.payload" ]
aliases = [ "/questions/50731" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP player voice playback problem](/questions/50731/rtp-player-voice-playback-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50731-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>I would like to ask a question about RTP streams playback. When I finished rtp packet capture and perform voice packet playback, I can not hear any sound. I found Sample Rate (Hz) field shows zero, instead of 8000 (as shown below). How do I resolve this issue ?Is there a correlation between this issue and the Sample Rate(Hz)?</p><p>Thank you in advance.</p><p>eric</p><p><img src="https://osqa-ask.wireshark.org/upfiles/rtp_player_problem_2Gq2cZo.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">udp codecs rtp voip rtp.payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '16, 20:40</strong></p><img src="https://secure.gravatar.com/avatar/a85b1956247ff17c75abad585211cf3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eric%20hou&#39;s gravatar image" /><p>eric hou<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eric hou has no accepted answers">0%</span></p></img></div></div><div id="comments-container-50731" class="comments-container"></div><div id="comment-tools-50731" class="comment-tools"></div><div class="clear"></div><div id="comment-50731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50734"></span>

<div id="answer-container-50734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50734-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not embed a G.729 decoder because it's not patent free.</p><p>You can follow the procedure described on this <a href="https://wiki.wireshark.org/HowToDecodeG729">wiki page</a> to manually decode the stream.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '16, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-50734" class="comments-container"></div><div id="comment-tools-50734" class="comment-tools"></div><div class="clear"></div><div id="comment-50734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

