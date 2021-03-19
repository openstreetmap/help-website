+++
type = "question"
title = "PDU fails to re-assemble after lost packet."
description = '''I have created a dissector for meteorological messages under a specific interface designated COREMET which consists of GRIB messages and METAR messages. These messages are sent across TCP/IP from one unix box to another. The GRIB messages are in excess of 1.0 Mbyte and are split over many messages. ...'''
date = "2013-02-26T06:24:00Z"
lastmod = "2013-02-27T03:26:00Z"
weight = 18879
keywords = [ "pdu", "dissector" ]
aliases = [ "/questions/18879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PDU fails to re-assemble after lost packet.](/questions/18879/pdu-fails-to-re-assemble-after-lost-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18879-score" class="post-score" title="current number of votes">0</div><span id="post-18879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created a dissector for meteorological messages under a specific interface designated COREMET which consists of GRIB messages and METAR messages. These messages are sent across TCP/IP from one unix box to another. The GRIB messages are in excess of 1.0 Mbyte and are split over many messages. MTU is around 1500. When everything is correct the dissector works fine. However we have an issue where a packet was lost during transmission. (not sure why yet and I am trying to remotely debug using a wireshark capture). Wireshark marks every packet as [TCP segment of reassmbled PDU]. However the final dissection never occurs, presumably due to the fact that the received bytes do not exceed/equal the required bytes to call the dissector from tcp_dissect_pdus(). I under stand that the message will never decode correctly if it is missing any part however it would be nice to have some sort of indication that the message was caught by never dissected due to the fact that all the data was not received. The next message on that interface is a METAR message which is 420 bytes and will dissect in one go and works fine however there is no indication that the first message failed. I have looked at the pinfo-&gt;noreassembly_reason but it contains nothing. short of writing my own tcp_dissect_pdus() which will cope with the missing packet with some sort of timeout has anyone had this problem and found a solution.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '13, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/d64d9a4ffe16338d4c65598b82424d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spotthemaniac&#39;s gravatar image" /><p><span>spotthemaniac</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spotthemaniac has no accepted answers">0%</span></p></div></div><div id="comments-container-18879" class="comments-container"></div><div id="comment-tools-18879" class="comment-tools"></div><div class="clear"></div><div id="comment-18879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18905"></span>

<div id="answer-container-18905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18905-score" class="post-score" title="current number of votes">1</div><span id="post-18905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Cope" in what sense?</p><p>There are at least three reasons why this could be happening:</p><ol><li>a TCP segment that <em>doesn't</em> contain the first part of a higher-level message got lost, but the first part of the message wasn't lost, so reassembly was started, but couldn't finish because the data required isn't available;</li><li>a TCP segment that <em>does</em> contain the first part of a higher-level message got lost, and Wireshark found what appears to be the beginning of a higher-level message, but is really stuff in the middle of a message, in a later TCP segment, and is trying to reassemble based on the probably-bogus length field value it got from what it thought was the beginning of that message</li><li>a snapshot length was used when capturing, so that not all the data in the TCP segments are necessarily available, and some of the data necessary to reassemble the message was discarded due to the snapshot length.</li></ol><p>Fixing the first problem would require that the TCP reassembly code recognize the absence of the segment (it must not, of course, assume that all segments are being delivered in order when doing that!) and, once it either has all the data necessary to complete the packet <em>or</em> has recognized enough absent segments such that, if present, it would have all the data necessary to complete the packet, construct the reassembled packet, perhaps with an indication that some of the data is missing (currently, tvbuffs don't support that).</p><p>Fixing the second problem has to be done by the dissector - it would have to check whether the header "looks reasonable" and, if not either scan the segment looking for something that "looks reasonable" or not bother trying to dissect the data in the segment as anything other than raw bytes.</p><p>Fixing the third problem would require some work similar to the work required to fix the first problem.</p><p>The simplest workaround might be to turn off TCP reassembly - turn off "Allow subdissector to reassemble TCP streams" in the TCP preferences. That will disable reassembly of the GRIB messages, but it will prevent Wireshark from trying to "reassemble" a packet based on, for example, something in the missing segment that's <em>not</em> the beginning of a packet but that Wireshark interprets as a packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '13, 18:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18905" class="comments-container"><span id="18912"></span><div id="comment-18912" class="comment"><div id="post-18912-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick answer:</p><p>so from analysis of the capture we lost a packet in the middle of the transmission. Dont know why yet. (worrying)</p><p>Hence tcp_dissect_pdus never calls my dissector. I assume due to the fact that there is not enough data to fully reconstruct.</p><p>five minutes later another message is sent on the same port which is passed straight to the dissector (which decodes fine) as it fits in one packet so I am assuming the tcp_dissect_pdus has a way to differentiate between messages.</p></div><div id="comment-18912-info" class="comment-info"><span class="comment-age">(27 Feb '13, 00:21)</span> <span class="comment-user userinfo">spotthemaniac</span></div></div><span id="18913"></span><div id="comment-18913" class="comment"><div id="post-18913-score" class="comment-score"></div><div class="comment-text"><p>I have started looking at the tcp_dissect_pdu code but i am new to some of this. Do you know if wireshark has a structure that holds the partially reconstructed message information?</p><p>What I am looking for is a way to interrogate the timestamps of the packet and timeout after x secs and label the first part(packet) of the message as BAD GRIB with only header dissection. (if possible) Regards</p><p>Wayne</p></div><div id="comment-18913-info" class="comment-info"><span class="comment-age">(27 Feb '13, 00:21)</span> <span class="comment-user userinfo">spotthemaniac</span></div></div><span id="18925"></span><div id="comment-18925" class="comment"><div id="post-18925-score" class="comment-score"></div><div class="comment-text"><p>oh and the get message length code does some form of syntax check before it returns a value from the header of the size of the message. There are specific bytes at specific palces in the header!</p></div><div id="comment-18925-info" class="comment-info"><span class="comment-age">(27 Feb '13, 03:26)</span> <span class="comment-user userinfo">spotthemaniac</span></div></div></div><div id="comment-tools-18905" class="comment-tools"></div><div class="clear"></div><div id="comment-18905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

