+++
type = "question"
title = "RTP flow is not associated with SIP call"
description = '''I have a basic SIP call via G711u codec. (here&#x27;s CAP) Somehow my switch doesn&#x27;t see the incoming RTP flow from 188.92.162.85 to 109.201.138.144.  Moreover Wireshark 2.0.3 doesn&#x27;t associate it either (yes, you can play the missing stream)    On the other hand when I use Wireshark 1.12.11 the media ma...'''
date = "2016-05-25T09:02:00Z"
lastmod = "2016-05-26T03:34:00Z"
weight = 52922
keywords = [ "sip", "rtp" ]
aliases = [ "/questions/52922" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP flow is not associated with SIP call](/questions/52922/rtp-flow-is-not-associated-with-sip-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a basic SIP call via G711u codec. <a href="http://78.47.220.147/kea/3.pcapng">(here's CAP)</a></p><p>Somehow my switch doesn't see the incoming RTP flow from 188.92.162.85 to 109.201.138.144. Moreover Wireshark 2.0.3 doesn't associate it either (yes, you can play the missing stream)</p><hr /><p><img src="https://i.imgur.com/h13SThd.png" alt="alt text" /></p><hr /><p>On the other hand when I use Wireshark 1.12.11 the media magically appears in SIP flow:</p><hr /><p><img src="https://i.imgur.com/6J1Vg4O.png" alt="alt text" /></p><hr /><p>Can anyone tell me what has changed in VoIP processing in the new Wireshark so I can overcome my problem with 1-way-voice. Thanks</p></div><div id="question-tags" class="tags-container tags">sip rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '16, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/edcbd91a6646415652791302627a3370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ky4k0b&#39;s gravatar image" /><p>ky4k0b<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ky4k0b has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 May '16, 09:16</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></img></div></div><div id="comments-container-52922" class="comments-container"><span id="52935"></span><div id="comment-52935" class="comment"><div id="post-52935-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can anyone tell me what has changed in VoIP processing in the new Wireshark so I can overcome my problem with 1-way-voice.</p></blockquote><p>I'm afraid the issues of VoIP analyis which still exist in Qt (new) Wireshark are not related to the reason why Yevgeniy could not hear the other party in the field, so identifying what has changed in Wireshark would not help you identify the real life issue.</p><p>The VoIP analysis is still Work in Progress in Qt Wireshark, and in 2.0.3 (and even in 2.1.0-2945-g66bea39 snapshot), e.g. the SSRC is wrongly displayed if you go <code>Telephony -&gt; RTP -&gt; RTP Streams -&gt; Analyze</code> - the SSRC for "reversed" direction is shown the same as the (correct) one for "forward" direction, the "setup packet" number for one of the streams is a huge number not matching any frame in the capture, ...</p><p>The RTP stream from Yevgeniy (109.201... -&gt; 188.92...) doesn't have the Mark bit set in the first packet which might cause issues with some over-sensitive RTP stacks, but if this was the reason of your trouble, it would be the other party who would not hear Yevgeniy, not vice versa. So this is also not the explanation.</p><p>Nor have I found anything wrong about the SDP contents. So further analysis steps should answer the following:</p><ul><li><p>whether the issue exists only for PCMU streams and/or only for streams coming from 188.92.... to 109.201...,</p></li><li><p>whether 109.201... is a gateway to TDM or audio itself or it forwards the RTP further,</p></li><li><p>whether no "leftover" RTP stream from previous call, possibly from a different source IP, was coming to 109.201....'s UDP port during this call (I don't know what capture filters you have used).</p></li></ul></div><div id="comment-52935-info" class="comment-info"><span class="comment-age">(25 May '16, 13:15)</span> sindy</div></div><span id="52943"></span><div id="comment-52943" class="comment"><div id="post-52943-score" class="comment-score"></div><div class="comment-text"><p>Am I missing a sendrecv SDP attribute from 188.92.162.85?</p></div><div id="comment-52943-info" class="comment-info"><span class="comment-age">(26 May '16, 01:05)</span> Jaap ♦</div></div><span id="52944"></span><div id="comment-52944" class="comment"><div id="post-52944-score" class="comment-score"></div><div class="comment-text"><p>Jaap,</p><p>If the offerer wishes to both send and receive media with its peer, it MAY include an "a=sendrecv" attribute, or it MAY omit it, since sendrecv is the default.</p><p>rfc3264 (c)</p></div><div id="comment-52944-info" class="comment-info"><span class="comment-age">(26 May '16, 01:12)</span> ky4k0b</div></div><span id="52945"></span><div id="comment-52945" class="comment"><div id="post-52945-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, @ky4k0b was faster to react. Even if this would be a reason for Wireshark to (incorrectly) treat one of the streams in a special way, it still wouldn't explain why in real life the 109.201... doesn't play the received RTP, as its own SDP does contain the sendrecv attribute.</p><p>@ku4k0b, will you file the bugs noticed? If not, may I use your pcap as the mandatory attachment?</p></div><div id="comment-52945-info" class="comment-info"><span class="comment-age">(26 May '16, 01:21)</span> sindy</div></div><span id="52946"></span><div id="comment-52946" class="comment"><div id="post-52946-score" class="comment-score"></div><div class="comment-text"><p>@sindy ye, sure, use it if you need.</p><p>ps: switched to G.729 codec and still no change. Keep investigating</p></div><div id="comment-52946-info" class="comment-info"><span class="comment-age">(26 May '16, 01:28)</span> ky4k0b</div></div><span id="52956"></span><div id="comment-52956" class="comment not_top_scorer"><div id="post-52956-score" class="comment-score"></div><div class="comment-text"><p>@ky4k0b oke, so it's optional to have this attribute. It's been too long I've worked in detail with that.</p></div><div id="comment-52956-info" class="comment-info"><span class="comment-age">(26 May '16, 04:52)</span> Jaap ♦</div></div></div><div id="comment-tools-52922" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-52922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52952"></span>

<div id="answer-container-52952" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52952-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It tool me couple days to find these lines I've added 2 years ago in iptables:</p><p>#voip-spammers</p><p>-A INPUT -s 188.92.162.85 -j REJECT --reject-with icmp-net-unreachable</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '16, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/edcbd91a6646415652791302627a3370?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ky4k0b&#39;s gravatar image" /><p>ky4k0b<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ky4k0b has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 May '16, 03:35</p></div></div><div id="comments-container-52952" class="comments-container"></div><div id="comment-tools-52952" class="comment-tools"></div><div class="clear"></div><div id="comment-52952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

