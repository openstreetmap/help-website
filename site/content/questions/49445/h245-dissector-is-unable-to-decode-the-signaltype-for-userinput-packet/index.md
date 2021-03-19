+++
type = "question"
title = "H245 dissector is unable to decode the signalType for userInput packet"
description = '''H245 dissector is unable to decode the signalType for userInput packet. Currently we are using Version 2.0.1 (v2.0.1-0-g59ea380 from master-2.0). Is there any way updated H245 dissector for this issue?? please find the snapshot of traces below for reference Frame 1576: 87 bytes on wire (696 bits), 8...'''
date = "2016-01-21T23:48:00Z"
lastmod = "2016-01-21T23:51:00Z"
weight = 49445
keywords = [ "h245" ]
aliases = [ "/questions/49445" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [H245 dissector is unable to decode the signalType for userInput packet](/questions/49445/h245-dissector-is-unable-to-decode-the-signaltype-for-userinput-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49445-score" class="post-score" title="current number of votes">0</div><span id="post-49445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>H245 dissector is unable to decode the signalType for userInput packet. Currently we are using Version 2.0.1 (v2.0.1-0-g59ea380 from master-2.0).</p><p>Is there any way updated H245 dissector for this issue??</p><p>please find the snapshot of traces below for reference</p><p>Frame 1576: 87 bytes on wire (696 bits), 87 bytes captured (696 bits) Ethernet II, Src: SonusNet_02:0b:c6 (00:10:6b:02:0b:c6), Dst: HewlettP_b8:2f:00 (00:19:bb:b8:2f:00) Internet Protocol Version 4, Src: 10.54.144.144, Dst: 10.70.52.116 Transmission Control Protocol, Src Port: 1034 (1034), Dst Port: 1720 (1720), Seq: 522, Ack: 908, Len: 33 TPKT, Version: 3, Length: 33 Q.931 H.225.0 CS H323-UserInformation h323-uu-pdu h323-message-body: empty (8) empty: NULL 1... .... h245Tunnelling: True h245Control: 1 item Item 0 H245Control item: 7 octets H.245 PDU Type: indication (3) indication: userInput (13) userInput: signal (3) signal signalType: ? ---&gt; unable to decode duration: 150</p><p>Thanks, Satish</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-h245" rel="tag" title="see questions tagged &#39;h245&#39;">h245</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '16, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/3d57766b184497779844072b83a4ed3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="satish&#39;s gravatar image" /><p><span>satish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="satish has no accepted answers">0%</span></p></div></div><div id="comments-container-49445" class="comments-container"></div><div id="comment-tools-49445" class="comment-tools"></div><div class="clear"></div><div id="comment-49445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49446"></span>

<div id="answer-container-49446" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49446-score" class="post-score" title="current number of votes">0</div><span id="post-49446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Open a <a href="https://bugs.wireshark.org">bug report</a> and attach a pcap file with the messages in question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '16, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '16, 04:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-49446" class="comments-container"></div><div id="comment-tools-49446" class="comment-tools"></div><div class="clear"></div><div id="comment-49446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

