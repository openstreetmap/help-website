+++
type = "question"
title = "Do not see SIP or G711 calls in VOIP Calls tab"
description = '''I recently discovered (because of this forum) that G729 calls will not display in the VOIP Calls tab. I would however expect to see G711 and SIP calls in the VOIP Calls tab. I do not. Am I missing a setting change? I am able to save the RTP streams and covert the files to PCM and play with Audacity....'''
date = "2015-07-14T10:30:00Z"
lastmod = "2015-07-14T11:00:00Z"
weight = 44143
keywords = [ "voipcalls", "voip" ]
aliases = [ "/questions/44143" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Do not see SIP or G711 calls in VOIP Calls tab](/questions/44143/do-not-see-sip-or-g711-calls-in-voip-calls-tab)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44143-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently discovered (because of this forum) that G729 calls will not display in the VOIP Calls tab. I would however expect to see G711 and SIP calls in the VOIP Calls tab. I do not. Am I missing a setting change? I am able to save the RTP streams and covert the files to PCM and play with Audacity. Just wondering why I never see VOIP Calls.</p></div><div id="question-tags" class="tags-container tags">voipcalls voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/7680a2a610d43f1161f289dd85b76a30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kenny70&#39;s gravatar image" /><p>Kenny70<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kenny70 has no accepted answers">0%</span></p></div></div><div id="comments-container-44143" class="comments-container"></div><div id="comment-tools-44143" class="comment-tools"></div><div class="clear"></div><div id="comment-44143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44144"></span>

<div id="answer-container-44144" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44144-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not whether they're G.729, or G.711, or any codec. The problem is the VOIP Calls feature analyzes a VoIP <em>call</em>, meaning the the signaling (SIP, H.323, etc.) as well as the RTP media. In your capture files, Wireshark cannot see the SIP signaling, because SIP is running over TLS, and is thus encrypted.</p><p>The only reason you even see the RTP packets decoded as <em>RTP</em> is because you have the preference for RTP called "<code>Try to decode RTP outside of conversations</code>" enabled. (in <code>Edit-&gt;Preferences-&gt;Protocols-&gt;RTP</code>) That preference setting makes Wireshark try to decode any/every UDP packet as an RTP packet using a heuristic, unless some other protocol matched the packet first. If you disable that preference, you won't even see RTP packets. You'll just see them as UDP packets with unknown data payload.</p><p>So basically Wireshark is guessing that the UDP packets are RTP - it happens to be guessing correctly in your case. It guessed incorrectly in <a href="https://ask.wireshark.org/questions/44136/cannot-playback-audio-from-rtp-stream-using-g711">Amato_C's question</a>, because those UDP packets are probably SRTP not RTP - unfortunately SRTP is almost indistinguishable from RTP - Wireshark would need to decode the SIP signaling's SDP to figure out the RTP is actually SRTP, but since SIP is running over TLS, it can't decode SIP.</p><p>So, since all Wireshark en decode in your capture is RTP, without any VoIP signaling protocol, nothing shows up in the "VOIP Calls" dialog. But if you click <code>Telephony-&gt;RTP-&gt;Show All Streams</code>, then you'll see the RTP streams.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '15, 11:07</p></div></div><div id="comments-container-44144" class="comments-container"><span id="44152"></span><div id="comment-44152" class="comment"><div id="post-44152-score" class="comment-score"></div><div class="comment-text"><p>The strange thing is that I disabled TLS on the media stream of the IPBX system. I still do not see SIP calls in the VOIP Calls tab.</p></div><div id="comment-44152-info" class="comment-info"><span class="comment-age">(14 Jul '15, 13:27)</span> Kenny70</div></div><span id="44153"></span><div id="comment-44153" class="comment"><div id="post-44153-score" class="comment-score"></div><div class="comment-text"><p>Type in "<code>sip</code>" in the display filter box and press the "Apply" button - if no packets showed up, then Wireshark doesn't see any SIP. Then type in "<code>tcp.port == 5061</code>" in the display filter box and press Apply - if you see packets, then it's still using SIP over TLS.</p></div><div id="comment-44153-info" class="comment-info"><span class="comment-age">(14 Jul '15, 13:31)</span> Hadriel</div></div><span id="44154"></span><div id="comment-44154" class="comment"><div id="post-44154-score" class="comment-score"></div><div class="comment-text"><p>Display filter is empty when I filter for SIP. I guess I need to figure out why SIP on this IPBX is still running over TLS even though I disable TLS on the media stream.</p></div><div id="comment-44154-info" class="comment-info"><span class="comment-age">(14 Jul '15, 13:35)</span> Kenny70</div></div><span id="44155"></span><div id="comment-44155" class="comment"><div id="post-44155-score" class="comment-score"></div><div class="comment-text"><p>@Kenny70</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-44155-info" class="comment-info"><span class="comment-age">(14 Jul '15, 13:49)</span> grahamb ♦</div></div></div><div id="comment-tools-44144" class="comment-tools"></div><div class="clear"></div><div id="comment-44144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

