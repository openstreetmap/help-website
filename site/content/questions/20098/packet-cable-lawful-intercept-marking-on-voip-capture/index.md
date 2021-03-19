+++
type = "question"
title = "Packet Cable Lawful Intercept marking on VoIP capture"
description = '''While running a pcap on a Samsung VoIP set, I saw that packets that I know were part of an audio stream were simply identified as UDP and not rtp. A closer look showed 2 IP headers, the first one was in the usual place and the second was sandwiched between the data portion and another part of the he...'''
date = "2013-04-04T23:11:00Z"
lastmod = "2013-04-05T07:07:00Z"
weight = 20098
keywords = [ "pcli", "voip" ]
aliases = [ "/questions/20098" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Cable Lawful Intercept marking on VoIP capture](/questions/20098/packet-cable-lawful-intercept-marking-on-voip-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20098-score" class="post-score" title="current number of votes">0</div><span id="post-20098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While running a pcap on a Samsung VoIP set, I saw that packets that I know were part of an audio stream were simply identified as UDP and not rtp. A closer look showed 2 IP headers, the first one was in the usual place and the second was sandwiched between the data portion and another part of the header shown as "Packet Cable Lawful Intercept" with a CCCID of 2147499140 (reminded me of a phone number). Ports involved were udp 9000 &amp; 30004. I know that 30000 through 300083 are being used for the rtp/rtcp and I also saw that WS will dissect 9000 as pcli but will it also put in a specific WAN and CCID number as well? Occasionally the second IP header would have a public address and other times a normal broadcast address.</p><p>Has anyone else run into this and Is this what I think it is? [play scary/dramatic music here .....]</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcli" rel="tag" title="see questions tagged &#39;pcli&#39;">pcli</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '13, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-20098" class="comments-container"></div><div id="comment-tools-20098" class="comment-tools"></div><div class="clear"></div><div id="comment-20098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20103"></span>

<div id="answer-container-20103" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20103-score" class="post-score" title="current number of votes">1</div><span id="post-20103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Packet Cable Lawful Intercept is a protocol that runs on port 9000 and therefor Wireshark interprets the packets as PCLI. Select one of the packets and rightclick on the "PCLI" header in the packet details pane. You can then choose "Disable Prototol".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '13, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20103" class="comments-container"></div><div id="comment-tools-20103" class="comment-tools"></div><div class="clear"></div><div id="comment-20103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20101"></span>

<div id="answer-container-20101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20101-score" class="post-score" title="current number of votes">0</div><span id="post-20101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to preferences, look for the RTP dissector settings and check 'Try to decode RTP outside of conversations'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '13, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20101" class="comments-container"><span id="20117"></span><div id="comment-20117" class="comment"><div id="post-20117-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys - I did all that already and WS will still not read it as an rtp stream. I've looked at a lot of SIP pcaps (NEC, Astrisk, Shoretel, Panasonic, hosted SIP, etc) and have not seen this before. Normally it's 5060 (or something close to it) and the then the media streams on higher ports. Here, it's 6000 for their signaling (which still does not decode as SIP even though I put it in preferences) and then 9000 for one side and 30000 to 30083 for the other side with two IP headers embedded in the packet as described earlier. If WS were simply interpreting this as a default, then why am I seeing the pcli fields filled in with a value not in brackets - eg "[CCID: 2147499133 ]"? And what's with the second IP address that actually resolves to something and appears in the Source/Destination field in the packet list screen instead of the first IP header (this happens just as the supposed rtp stream starts btw)? My concern is that the manufacturer has defaulted to this port (9000) in order to be compliant with some of the federal gov. access laws started in 2007 which would allow the traffic to be siphoned off to a surveillance group that is not necessarily .... friendly or secure. Just seems fishy to me.</p></div><div id="comment-20117-info" class="comment-info"><span class="comment-age">(05 Apr '13, 07:07)</span> <span class="comment-user userinfo">EricKnaus</span></div></div></div><div id="comment-tools-20101" class="comment-tools"></div><div class="clear"></div><div id="comment-20101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

