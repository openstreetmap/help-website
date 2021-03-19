+++
type = "question"
title = "Can see SIP/SDP; m = audio RTP/AVP but no RTP packets or sessions."
description = '''In my captured file (pcap) I can see SIP/SDP packets. But No RTP. I tried decoding UDP as RTP, but still wireshark cannot see RTP sessions. Here is one of the SIP/SDP packet data. What can be the reason ? Any possible solutions ? I will post more pictures if need more to find the problem. Any sugges...'''
date = "2015-05-11T03:57:00Z"
lastmod = "2015-05-11T03:57:00Z"
weight = 42297
keywords = [ "sip", "sdp", "rtp", "voip" ]
aliases = [ "/questions/42297" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can see SIP/SDP; m = audio RTP/AVP but no RTP packets or sessions.](/questions/42297/can-see-sipsdp-m-audio-rtpavp-but-no-rtp-packets-or-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42297-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my captured file (pcap) I can see SIP/SDP packets. But No RTP. I tried decoding UDP as RTP, but still wireshark cannot see RTP sessions. Here is one of the SIP/SDP packet data.</p><p>What can be the reason ? Any possible solutions ? I will post more pictures if need more to find the problem. Any suggestions Please. Thanks</p><p><strong>UPDATE:</strong> I have uploaded the file in cloudshark. This is the link: <a href="https://www.cloudshark.org/captures/8dc9fe0edaeb">https://www.cloudshark.org/captures/8dc9fe0edaeb</a></p></div><div id="question-tags" class="tags-container tags">sip sdp rtp voip</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '15, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/4ec917e3556fb6d9c03cc0e39ec7732a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shas&#39;s gravatar image" /><p>Shas<br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '15, 04:46</p></div></div><div id="comments-container-42297" class="comments-container"><span id="42300"></span><div id="comment-42300" class="comment"><div id="post-42300-score" class="comment-score"></div><div class="comment-text"><p>ANNOUNCEMENT TO ANYONE: DON"T POST PICTURES! These are useless for analysis. Supply capture files through a file share service or cloudshark.</p></div><div id="comment-42300-info" class="comment-info"><span class="comment-age">(11 May '15, 04:25)</span> Jaap ♦</div></div><span id="42308"></span><div id="comment-42308" class="comment"><div id="post-42308-score" class="comment-score"></div><div class="comment-text"><p>Yep, this capture sure helps to understand what's going on.</p><ol><li>There's SIP REGISTERs and OKs and these OKs from you have SDP, but where is the INVITE?</li><li>There's unidentified UDP traffic to the same box happening, is that call related?</li></ol><p>There's HTTPS traffic to the same box. I assume for management/monitoring? Or is it call related?</p><p>Does the installation support Compressed RTP? I can't see that packet capture as such.</p><p>You're connecting to facebook as well. I guess this is not part of your problem at hand? Might try to clean up your network traffic as good as possible when investigating a problem, this 'noise' makes it harder for you to get a feel for what's happening with your protocol.</p></div><div id="comment-42308-info" class="comment-info"><span class="comment-age">(11 May '15, 08:39)</span> Jaap ♦</div></div><span id="42322"></span><div id="comment-42322" class="comment"><div id="post-42322-score" class="comment-score"></div><div class="comment-text"><p>I see you are using CSipSimple on your Samsung Android smartphone and registering to your Asterisk PBX, but this capture does not include any Call setup (INVITE) that shows any SDP negotiation.....only SDP information pertaining to OPTIONS requests.</p><p>Try starting a capture BEFORE your attempted call, and then stopping the capture AFTER the call attempt is terminated.....then repost the new capture.</p><p>As far as NOISE goes, that can be filtered out with display filters. Its always good to have to full capture, in case this is an issue at L2.</p></div><div id="comment-42322-info" class="comment-info"><span class="comment-age">(11 May '15, 20:13)</span> Rooster_50</div></div><span id="42328"></span><div id="comment-42328" class="comment"><div id="post-42328-score" class="comment-score"></div><div class="comment-text"><p>@Rooster_50, @Jaap, I tried to capture the session with same application, with same kind of network connection (from the beginning). But now it seems I dont have any SIP/SDP packets. Just UDPs.</p></div><div id="comment-42328-info" class="comment-info"><span class="comment-age">(12 May '15, 06:21)</span> Shas</div></div></div><div id="comment-tools-42297" class="comment-tools"></div><div class="clear"></div><div id="comment-42297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

