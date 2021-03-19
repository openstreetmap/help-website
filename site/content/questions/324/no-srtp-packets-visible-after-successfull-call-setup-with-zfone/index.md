+++
type = "question"
title = "No SRTP packets visible after successfull call setup with zfone"
description = '''Hi, I have 2 PCs each running X-Lite 4.O softphones in combination with ZFONE v0.92 build 218.  Both are connected to an Asterix Softswitch. A PC is running Fedora with Wireshark 1.4 able to decode SRTP packets(In preferences, &quot;Try to decode RTP outside of conversation&quot; etc..) with filter applied fo...'''
date = "2010-09-25T14:46:00Z"
lastmod = "2010-09-25T22:53:00Z"
weight = 324
keywords = [ "zfone", "srtp", "zrtp" ]
aliases = [ "/questions/324" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No SRTP packets visible after successfull call setup with zfone](/questions/324/no-srtp-packets-visible-after-successfull-call-setup-with-zfone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-324-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have 2 PCs each running X-Lite 4.O softphones in combination with ZFONE v0.92 build 218. Both are connected to an Asterix Softswitch. A PC is running Fedora with Wireshark 1.4 able to decode SRTP packets(In preferences, "Try to decode RTP outside of conversation" etc..) with filter applied for SIP, RTP and SRTP. This PC is connected in bridge mode between the Asterix and one of the softphone PC.</p><p>I have the following strange behaviour: As per ZFONE Displays, secure connection can be established between both parties. The call flow reported by Wireshark is inline with ZRTP IETF specs BUT no SRTP packets are visible (only RTP packets are exchanged between the parties.)</p><p>I first though that wireshark is not able to decode SRTP packets at all. Hence, I replaced the X-lite phones with eyeBeam: in fact, SRTP is not supported natively by X-lite and I wanted to force SRTP traffic to be exchanged (eyeBeam does support TLS/SRTP) I deactivated ZFONE and initated a call: SRTP packets were reported.</p><p>Who can help ? the ZFONE is intended to generate a shared secret which is then used to generate keys and salt for a Secure RTP (SRTP)</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">zfone srtp zrtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '10, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/2819aa4c2ab18ec7c515a47c3d36a2a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aspirin&#39;s gravatar image" /><p>Aspirin<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aspirin has no accepted answers">0%</span></p></div></div><div id="comments-container-324" class="comments-container"></div><div id="comment-tools-324" class="comment-tools"></div><div class="clear"></div><div id="comment-324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="329"></span>

<div id="answer-container-329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-329-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look closely at the initial RTP packets in the ZFONE session, you'll see they're odd. You have to set the preferences for the RTP dissector to see these type 0 packets as ZRTP packets.</p><p>Furthermore the RTP dissector can't really see that RTP packets are really SRTP packets when looking at the packets themselves, it has to be taken from the session signaling. This is done from the SIP/SDP dissector, but not from the ZRTP dissector.</p><p>You could file an enhancement bug, with sample captures of your ZRTP session, so this can be added to Wireshark. (I would love to see some captures <strong>:-)</strong> )</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '10, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-329" class="comments-container"><span id="336"></span><div id="comment-336" class="comment"><div id="post-336-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap. I can forward you the traces. Please just advise how to proceed (Size of the File is 260 KB)</p><p>Not sure in my case, that, when using Zfone, the session signaling can help to determine if the RTP packet is in fact an SRTP packet.</p><p>The only difference I have noticed is the size of the RTP packets: 180 bytes prior ZRTP session is established and 184 byte after the Conf2Ack message.</p><p>I am (very) happy for any related info</p><p>Cheers</p></div><div id="comment-336-info" class="comment-info"><span class="comment-age">(27 Sep '10, 06:24)</span> Aspirin</div></div><span id="340"></span><div id="comment-340" class="comment"><div id="post-340-score" class="comment-score"></div><div class="comment-text"><p>You can: - File a bug at https://bugs.wireshark.org - You can send it straight to me, see my profile</p><p>Indeed, one has to look in the RTP packets to see ZRTP session establishment, which is done in-band.</p><p>Those 4 extra bytes look like the 32bit authentication tag</p></div><div id="comment-340-info" class="comment-info"><span class="comment-age">(27 Sep '10, 08:30)</span> Jaap ♦</div></div><span id="720"></span><div id="comment-720" class="comment"><div id="post-720-score" class="comment-score"></div><div class="comment-text"><p>This feature was added in revision 34277, see http://www.wireshark.org/lists/wireshark-commits/201009/msg00241.html</p></div><div id="comment-720-info" class="comment-info"><span class="comment-age">(28 Oct '10, 04:06)</span> Jaap ♦</div></div></div><div id="comment-tools-329" class="comment-tools"></div><div class="clear"></div><div id="comment-329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

