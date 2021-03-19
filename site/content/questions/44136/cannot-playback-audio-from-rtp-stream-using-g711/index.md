+++
type = "question"
title = "Cannot playback audio from RTP stream using G.711"
description = '''I have captured a VoIP call using RTP with G.711 codec. I have tried using Wireshark to playback the audio, but all I hear is static. Here is a link to the capture file: https://drive.google.com/file/d/0B80gG9wZvGF0X0NPb2dnemtYMzA/view?usp=sharing At first, I thought SRTP was being used, but Wiresha...'''
date = "2015-07-14T07:06:00Z"
lastmod = "2015-07-14T11:21:00Z"
weight = 44136
keywords = [ "decode", "audio" ]
aliases = [ "/questions/44136" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot playback audio from RTP stream using G.711](/questions/44136/cannot-playback-audio-from-rtp-stream-using-g711)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44136-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured a VoIP call using RTP with G.711 codec. I have tried using Wireshark to playback the audio, but all I hear is static.</p><p>Here is a link to the capture file:</p><p><a href="https://drive.google.com/file/d/0B80gG9wZvGF0X0NPb2dnemtYMzA/view?usp=sharing">https://drive.google.com/file/d/0B80gG9wZvGF0X0NPb2dnemtYMzA/view?usp=sharing</a></p><p>At first, I thought SRTP was being used, but Wireshark's RTP dissector does not detect SRTP and the encryption method (AES). I have done the following in Wireshark:</p><ol><li>Telephony -&gt; RTP -&gt; Show All Streams, then I save the Payload as a .AU file</li><li>Tried decoding with a G.729 codec (in case the codec shown by Wireshark was incorrect)</li><li>Saved the file as a .RAW file and used a sound processing program (SoX) to create an audio file</li></ol><p>Any recommendations?</p></div><div id="question-tags" class="tags-container tags">decode audio</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44136" class="comments-container"></div><div id="comment-tools-44136" class="comment-tools"></div><div class="clear"></div><div id="comment-44136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44146"></span>

<div id="answer-container-44146" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44146-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure there really is a general rule for that - at my previous job we sometimes used SIP/TLS with plain RTP, and at other places we used unencrypted SIP (over UDP or TCP) with SRTP.</p><p>One way to tell your capture actually contains SRTP is that the RTP payload was too big - normal G.711 is encoded in multiples of 80 bytes (each 80 bytes representing 10ms of audio time). Since your "RTP" packet payload was 164 bytes, there were 4 extra bytes - which are likely a 32-bit SRTP authentication hash tag (i.e., HMAC_SHA1_32).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44146" class="comments-container"><span id="44156"></span><div id="comment-44156" class="comment"><div id="post-44156-score" class="comment-score"></div><div class="comment-text"><p>Just for completeness:</p><p>G.711 frame size = multiple of 80 bytes</p><p>G.729 frame size = multiple of 10 bytes</p></div><div id="comment-44156-info" class="comment-info"><span class="comment-age">(14 Jul '15, 14:07)</span> Amato_C</div></div></div><div id="comment-tools-44146" class="comment-tools"></div><div class="clear"></div><div id="comment-44146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44138"></span>

<div id="answer-container-44138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44138-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The fact that the preceeding TCP stream goes to port 5061 leads me to believe this is SRTP encrypted G.711 encoded speech. Unless you can decrypt the call setup in the TCP stream, you won't be able to get the required keys for the SRTP session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '15, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44138" class="comments-container"><span id="44141"></span><div id="comment-44141" class="comment"><div id="post-44141-score" class="comment-score"></div><div class="comment-text"><p>@Jaap - Would it be fair to say that whenever encrypted SIP is used (SIP-TLS), then SRTP is also used? I am trying to find a general rule.</p></div><div id="comment-44141-info" class="comment-info"><span class="comment-age">(14 Jul '15, 10:21)</span> Amato_C</div></div><span id="44150"></span><div id="comment-44150" class="comment"><div id="post-44150-score" class="comment-score"></div><div class="comment-text"><p>@Hadriel - So I reexamined my RTP captures using G.711 codec and noticed that your answer provides a great way to determine if SRTP is being used when G.711 coded is implemented:</p><p>if &lt;rtp-payload&gt; mod 80 != 0, then SRTP</p><p>Can you change your comment to an answer so I can select it as the answer?</p><p>Thanks again!</p></div><div id="comment-44150-info" class="comment-info"><span class="comment-age">(14 Jul '15, 12:56)</span> Amato_C</div></div><span id="44163"></span><div id="comment-44163" class="comment"><div id="post-44163-score" class="comment-score"></div><div class="comment-text"><p>It's a common combination. There's little use doing one, but not the other, other than for testing maybe.</p><p>As for the rule: that works ... unless the optional authentication tag is not included. (SDES: UNAUTHENTICATEDS_SRTP). So there's no other definitive way to tell unless you look at the SDP (which is encrypted in your SIP/TLS stream)</p></div><div id="comment-44163-info" class="comment-info"><span class="comment-age">(14 Jul '15, 22:50)</span> Jaap ♦</div></div></div><div id="comment-tools-44138" class="comment-tools"></div><div class="clear"></div><div id="comment-44138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

