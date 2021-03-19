+++
type = "question"
title = "Criteria for decoding UDP to RTP"
description = '''Hello, I&#x27;m writing a VoIP application and trying to verify correct RTP behavior with Wireshark. Unfortunately, Wireshark sees my packets as UDP only, it does not recognize them as RTP packets. What criteria does Wireshark use to determine RTP packets? Thanks.'''
date = "2011-02-13T10:15:00Z"
lastmod = "2011-02-14T14:36:00Z"
weight = 2305
keywords = [ "udp", "rtp" ]
aliases = [ "/questions/2305" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Criteria for decoding UDP to RTP](/questions/2305/criteria-for-decoding-udp-to-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2305-score" class="post-score" title="current number of votes">0</div><span id="post-2305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm writing a VoIP application and trying to verify correct RTP behavior with Wireshark. Unfortunately, Wireshark sees my packets as UDP only, it does not recognize them as RTP packets. What criteria does Wireshark use to determine RTP packets? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '11, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/2a6cf43ccd6b1ab3634d72f17ebdb980?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbwest&#39;s gravatar image" /><p><span>cbwest</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbwest has no accepted answers">0%</span></p></div></div><div id="comments-container-2305" class="comments-container"></div><div id="comment-tools-2305" class="comment-tools"></div><div class="clear"></div><div id="comment-2305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2307"></span>

<div id="answer-container-2307" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2307-score" class="post-score" title="current number of votes">1</div><span id="post-2307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Open the preferences, scroll down in the list of protocols, select RTP, check "Try to decode RTP outside of conversations".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2307" class="comments-container"></div><div id="comment-tools-2307" class="comment-tools"></div><div class="clear"></div><div id="comment-2307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2329"></span>

<div id="answer-container-2329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2329-score" class="post-score" title="current number of votes">0</div><span id="post-2329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark needs to see the signaling (SIP, MGCP, H.248, etc) associated with the VoIP call in order to determine which UDP packets are RTP. The signaling packets contain Session Description Protocol data, which tells the endpoints which IPs/ports to send RTP to. Wireshark in turn uses this SDP info to decode UDP packets matching those IP/port pairs as RTP.</p><p>It sounds like you either the signaling is not in the PCAP file or your signaling is being sent on a non-standard port. You can use the preferences setting in Jaap's answer to get around the former, or you can select a signaling packet and set a user specific decode via right-click -&gt; Decode As -&gt; Transport -&gt; Both for the latter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '11, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/e458b44fd60b4064eb73fc42e67b3897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grossman&#39;s gravatar image" /><p><span>grossman</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grossman has no accepted answers">0%</span></p></div></div><div id="comments-container-2329" class="comments-container"></div><div id="comment-tools-2329" class="comment-tools"></div><div class="clear"></div><div id="comment-2329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2332"></span>

<div id="answer-container-2332" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2332-score" class="post-score" title="current number of votes">0</div><span id="post-2332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please note that:</p><ol><li>Wireshark doesn't <strong>need</strong> signaling, but can <strong>use</strong> signaling to tag UDP packet flows as possible RTP packet flows.</li><li>Session Description Protocol (SDP) is just one of the possible signaling protocols to describe the media session. This is usually related to SIP and MGCP. Another media description protocols is H.245 f.i.</li><li>Wireshark use the <strong>hint</strong> derived from the media description protocol to try to dissect the UDP packets as RTP. RTP is hard to heuristically discriminate from other UDP payloads, therefore the media description protocol dissection is helpful, while the RTP dissector preference helps out in other cases.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2332" class="comments-container"></div><div id="comment-tools-2332" class="comment-tools"></div><div class="clear"></div><div id="comment-2332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

