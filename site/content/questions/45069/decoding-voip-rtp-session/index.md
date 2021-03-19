+++
type = "question"
title = "Decoding VOIP RTP session"
description = '''Hello, When I try decode raw audio data of RTP stream by va_g729_decoder- got NOISE instead normal audio.(This issue only when few RTP streams in the one session) As you can see Session has few RTP stream on the same SRC DST ports and all stream has same SSRC. Total audio duration was 30 sec = why w...'''
date = "2015-08-13T12:24:00Z"
lastmod = "2015-08-14T10:23:00Z"
weight = 45069
keywords = [ "rtp", "voip" ]
aliases = [ "/questions/45069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding VOIP RTP session](/questions/45069/decoding-voip-rtp-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45069-score" class="post-score" title="current number of votes">0</div><span id="post-45069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, When I try decode raw audio data of RTP stream by <strong>va_g729_decoder</strong>- got NOISE instead normal audio.(This issue only when few RTP streams in the one session) As you can see Session has few RTP stream on the same SRC DST ports and all stream has same SSRC. Total audio duration was 30 sec = why wireshark show RTP1=33sec RTP2=24sec RTP=12sec <strong>SDP</strong></p><pre><code>Via: 
From: 
To: 
Call-ID: 
CSeq: 1 INVITE
Contact: 
Content-Type: application/sdp
Server: MERA MVTS3G v.4.3.0-40
Content-Length:   260
v=0
o=- 1439471899 1439471899 IN IP4 
s=-
c=IN IP4 
t=0 0
m=audio 24130 RTP/AVP 18 101
a=rtpmap:18 G729/8000
a=fmtp:18 annexb=no
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=ptime:20
a=sendrecv
a=silenceSupp:off - - - -</code></pre><pre><code>Version 1.12.7 (v1.12.7-0-g7fc8978 from master-1.12)
Running on 64-bit Windows 7 Service Pack 1, build 7601,
with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980),
based on libpcap version 1.0 branch 1_0_rel0b (20091008),
GnuTLS 3.2.15, Gcrypt 1.6.2, without AirPcap.
Intel(R) Core(TM) i5-2520M CPU @ 2.50GHz, with 12063MB of physical memory.</code></pre><p><img src="https://www.cubbyusercontent.com/pl/call.png/_c9fd34598d1d47efb6727d621156f433" alt="Call" /></p><p><a href="https://www.cubbyusercontent.com/pl/call.wav/_d271e9ec315f4eb6946fc50ed72a720d">LINK to the Wav file with result of decoding</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '15, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/0319823751d2656828f8f21f22b90b05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sindar&#39;s gravatar image" /><p><span>Sindar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sindar has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Aug '15, 12:25</strong> </span></p></div></div><div id="comments-container-45069" class="comments-container"><span id="45114"></span><div id="comment-45114" class="comment"><div id="post-45114-score" class="comment-score"></div><div class="comment-text"><p>Is SRTP (Secure Real-time Transport Protocol) being used?</p></div><div id="comment-45114-info" class="comment-info"><span class="comment-age">(14 Aug '15, 08:35)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="45117"></span><div id="comment-45117" class="comment"><div id="post-45117-score" class="comment-score"></div><div class="comment-text"><p>No, only pure RTP</p></div><div id="comment-45117-info" class="comment-info"><span class="comment-age">(14 Aug '15, 10:23)</span> <span class="comment-user userinfo">Sindar</span></div></div></div><div id="comment-tools-45069" class="comment-tools"></div><div class="clear"></div><div id="comment-45069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

