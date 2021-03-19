+++
type = "question"
title = "QOS, delivery order decoded as Traffic Class?"
description = '''Hi, I&#x27;ve question about QOS decoded message. why for Delivery order below become &quot;Streaming Class&quot; ? not Without delivery order (&#x27;no&#x27;), the number I trace subscribed with Streaming Class. GSM A-I/F DTAP - Activate PDP Context Accept  Protocol Discriminator: GPRS session management messages  1... ......'''
date = "2011-05-04T07:06:00Z"
lastmod = "2011-05-04T07:06:00Z"
weight = 3919
keywords = [ "traffic", "qos", "class" ]
aliases = [ "/questions/3919" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [QOS, delivery order decoded as Traffic Class?](/questions/3919/qos-delivery-order-decoded-as-traffic-class)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3919-score" class="post-score" title="current number of votes">0</div><span id="post-3919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've question about QOS decoded message. why for Delivery order below become "Streaming Class" ? not Without delivery order ('no'), the number I trace subscribed with Streaming Class.</p><pre><code>GSM A-I/F DTAP - Activate PDP Context Accept
    Protocol Discriminator: GPRS session management messages
        1... .... = TI flag: allocated by receiver
        .000 .... = TIO: 0
        .... 1010 = Protocol discriminator: GPRS session management messages (10)
    01.. .... = Sequence number: 1
    DTAP GPRS Session Management Message Type: Activate PDP Context Accept (0x42)
    0000 .... = Spare bit(s): 0
    .... 0011 = LLC SAPI: SAPI 3 (3)
    Quality Of Service - Negotiated QoS
        Length: 14
        00.. .... = Spare bit(s): 0
        ..00 1... = Quality of Service Delay class: Delay class 1 (1)
        .... .011 = Reliability class: Delay class 3 (3)
        1001 .... = Peak throughput: Up to 256 000 octet/s (9)
        .... 0... = Spare bit(s): 0
        .... .001 = Precedence class: High priority (1)
        000. .... = Spare bit(s): 0
        ...1 1111 = Mean throughput: Best effort (31)
        011. .... = Traffic class: Interactive class (3)
        **...1 0... = Delivery order: Streaming class (2)**
        .... ..11 = Delivery of erroneous SDUs: Erroneous SDUs are not delivered(&#39;No&#39;) (3)
        Maximum SDU size: 1500 octets (150)
        Maximum bitrate for uplink: 8640 kbps (254)
        Maximum bitrate for downlink: 8640 kbps (254)
        0111 .... = Residual Bit Error Rate (BER): 1*10-5 (7)
        .... 0100 = SDU error ratio: 1*10-4 (4)
        1000 00.. = Transfer delay: 1000 ms (32)
        .... ..01 = Traffic handling priority: Priority level 1 (1)
        Guaranteed bitrate for uplink: 0 kbps (255)
        Guaranteed bitrate for downlink: 0 kbps (255)
        000. .... = Spare bit(s): 0
        ...0 .... = Signalling indication: Not optimised for signalling traffic
        .... 0000 = Source statistics description: unknown (0)
        Maximum bitrate for downlink (extended): 21 Mbps (79)
        Guaranteed bitrate for downlink (extended): Use the value indicated by the Guaranteed bit rate for downlink (0)</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span> <span class="post-tag tag-link-class" rel="tag" title="see questions tagged &#39;class&#39;">class</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '11, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/6bdab60f4bfd3686bbbaca91a9e2fa3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ipoenkt&#39;s gravatar image" /><p><span>ipoenkt</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ipoenkt has no accepted answers">0%</span></p></div></div><div id="comments-container-3919" class="comments-container"></div><div id="comment-tools-3919" class="comment-tools"></div><div class="clear"></div><div id="comment-3919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

