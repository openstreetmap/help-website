+++
type = "question"
title = "LTE RRC: how to prepare data?"
description = '''Hello! I am trying to use wireshark to decode LTE protocols data, captured from the system. It works for S1 (going to hex, then tex2pcap, then tshark -V). But, something is lost with RRC, I can not get it tunning: Maybe I should add something to RRC, like direction? Best regards, thanks, HNY Iztok e...'''
date = "2012-12-13T12:53:00Z"
lastmod = "2012-12-27T00:25:00Z"
weight = 16847
keywords = [ "asn.1", "pcap", "rrc", "lte", "s1ap" ]
aliases = [ "/questions/16847" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [LTE RRC: how to prepare data?](/questions/16847/lte-rrc-how-to-prepare-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16847-score" class="post-score" title="current number of votes">0</div><span id="post-16847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I am trying to use wireshark to decode LTE protocols data, captured from the system. It works for S1 (going to hex, then tex2pcap, then tshark -V).</p><p>But, something is lost with RRC, I can not get it tunning:</p><p>Maybe I should add something to RRC, like direction?</p><p>Best regards, thanks, HNY</p><p>Iztok</p><p>example in hex, RC_CONNECTION_REQUEST<br />
000000 58 55 95 97 74 06 zz<br />
</p><p>tshark answer:</p><pre><code>Frame 1: 6 bytes on wire (48 bits), 6 bytes captured (48 bits)  
    WTAP_ENCAP: 54  
    Arrival Time: Dec 13, 2012 21:35:02.000000000 CET  
    [Time shift for this packet: 0.000000000 seconds]  
    Epoch Time: 1355430902.000000000 seconds  
    [Time delta from previous captured frame: .000000000 seconds]  
    [Time delta from previous displayed frame: 0.000000000 seconds]  
    [Time since reference or first frame: 0.000000000 seconds]  
    Frame Number: 1  
    Frame Length: 6 bytes (48 bits)  
    Capture Length: 6 bytes (48 bits)  
    [Frame is marked: False]  
    [Frame is ignored: False]  
    [Protocols in frame: user_dlt:rlc-lte]  
DLT: 156, Payload: rlc-lte (RLC-LTE)  
RLC-LTE  
[Can&#39;t dissect LTE RLC frame because no per-frame info was attached!]</code></pre><p>S1 example:<br />
hex:<br />
000000 20 17 00 12 00 00 02 00 00 40 05 C0 01 36 FC D2 00 08 40 02 00 68 zz<br />
</p><p>tshark:</p><pre><code>Frame 15: 22 bytes on wire (176 bits), 22 bytes captured (176 bits)  
    WTAP_ENCAP: 56  
    Arrival Time: Dec 13, 2012 21:37:55.000014000 CET  
    [Time shift for this packet: 0.000000000 seconds]  
    Epoch Time: 1355431075.000014000 seconds  
    [Time delta from previous captured frame: 0.000001000 seconds]  
    [Time delta from previous displayed frame: 0.000001000 seconds]  
    [Time since reference or first frame: 0.000014000 seconds]  
    Frame Number: 15  
    Frame Length: 22 bytes (176 bits)  
    Capture Length: 22 bytes (176 bits)  
    [Frame is marked: False]
    [Frame is ignored: False]  
    [Protocols in frame: user_dlt:s1ap:s1ap:s1ap:s1ap]  
DLT: 158, Payload: s1ap (S1 Application Protocol)  
S1 Application Protocol  
    S1AP-PDU: successfulOutcome (1)  
        successfulOutcome  
            procedureCode: id-UEContextRelease (23)  
            criticality: reject (0)  
            value  
                UEContextReleaseComplete  
                    protocolIEs: 2 items  
                        Item 0: id-MME-UE-S1AP-ID  
                            ProtocolIE-Field  
                                id: id-MME-UE-S1AP-ID (0)  
                                criticality: ignore (1)  
                                value  
                                    MME-UE-S1AP-ID: 20380882  
                        Item 1: id-eNB-UE-S1AP-ID  
                            ProtocolIE-Field  
                                id: id-eNB-UE-S1AP-ID (8)  
                                criticality: ignore (1)  
                                value  
                                    ENB-UE-S1AP-ID: 104</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn.1" rel="tag" title="see questions tagged &#39;asn.1&#39;">asn.1</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-rrc" rel="tag" title="see questions tagged &#39;rrc&#39;">rrc</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span> <span class="post-tag tag-link-s1ap" rel="tag" title="see questions tagged &#39;s1ap&#39;">s1ap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/a01f024a466c4892dcf2243ce7af051f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s52d&#39;s gravatar image" /><p><span>s52d</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s52d has one accepted answer">50%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '12, 23:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></br></p></div></div><div id="comments-container-16847" class="comments-container"></div><div id="comment-tools-16847" class="comment-tools"></div><div class="clear"></div><div id="comment-16847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17250"></span>

<div id="answer-container-17250" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17250-score" class="post-score" title="current number of votes">0</div><span id="post-17250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="s52d has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello!</p><p>Solved: by using separate user_dlts, generating several hex files, and then merging tshark output files together.</p><p>my user_dlts:</p><p>"User 3 (DLT=150)","lte-rrc.bcch.bch","0","","0",""</p><p>"User 4 (DLT=151)","lte-rrc.bcch.dl.sch","0","","0",""</p><p>"User 5 (DLT=152)","lte-rrc.dl.ccch","0","","0",""</p><p>"User 6 (DLT=153)","lte-rrc.dl.dcch","0","","0",""</p><p>"User 7 (DLT=154)","lte-rrc.pcch","0","","0",""</p><p>"User 8 (DLT=155)","lte-rrc.ul.ccch","0","","0",""</p><p>"User 9 (DLT=156)","lte-rrc.ul.dcch","0","","0",""</p><p>example in hex, RC_CONNECTION_REQUEST 000000 58 55 95 97 74 06 zz</p><p>is coverted by: text2pcap -q -l 155 x.hex x.pcap and tshark -r x.pcap -V</p><p>So simple... And I learned a lot about wireshark! HNY, GL Iztok</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '12, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/a01f024a466c4892dcf2243ce7af051f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s52d&#39;s gravatar image" /><p><span>s52d</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s52d has one accepted answer">50%</span> </br></br></p></div></div><div id="comments-container-17250" class="comments-container"></div><div id="comment-tools-17250" class="comment-tools"></div><div class="clear"></div><div id="comment-17250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16851"></span>

<div id="answer-container-16851" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16851-score" class="post-score" title="current number of votes">1</div><span id="post-16851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The LTE-RLC dissector expects a structure to be attached to the frame. See packet-rlc-lte.h for details. or <a href="http://wiki.wireshark.org/RLC-LTE">http://wiki.wireshark.org/RLC-LTE</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '12, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-16851" class="comments-container"><span id="16932"></span><div id="comment-16932" class="comment"><div id="post-16932-score" class="comment-score"></div><div class="comment-text"><p>Hello! Thanks for fast answer, but I keep failing. Is it possible than hex via text2pcap does not work? maybe this works for UDP access only?</p><p>can I get working hex sample? Just to verify if I understood headers properly?</p><p>BR Iztok</p><p>example in hex, following packet-rlc-lte.h, but no succsess. it is typed manually, and at this point data might be incorect, but I fail to get header done properly.</p><p>00000000 72 6c 63 2d 6c 74 65 00 02 02 05 03 00 04 00 06 01 00 07 00 00 01 58 55 95 97 74 06 zz</p></div><div id="comment-16932-info" class="comment-info"><span class="comment-age">(15 Dec '12, 09:21)</span> <span class="comment-user userinfo">s52d</span></div></div><span id="16941"></span><div id="comment-16941" class="comment"><div id="post-16941-score" class="comment-score"></div><div class="comment-text"><p>This string:</p><p>00000000 72 6c 63 2d 6c 74 65 01 02 02 05 03 00 04 00 06 01 00 07 00 00 01 58 55 95 97 74 06 zz</p><p>At least gets it dissected by the dissector.</p><p>00000000 72 6c 63 2d 6c 74 65 01 Last byte 01 is rlcMode= RLC_TM_MODE</p></div><div id="comment-16941-info" class="comment-info"><span class="comment-age">(16 Dec '12, 07:22)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="16947"></span><div id="comment-16947" class="comment"><div id="post-16947-score" class="comment-score"></div><div class="comment-text"><p>Ups... I just wanted to get something out of it, and then to fix proper data: format first, then proper contents.</p><p>is pcap way ok? Iztok</p><p>File y.hex 00000000 72 6c 63 2d 6c 74 65 01 02 02 05 03 00 04 00 06 01 00 07 00 00 01 58 55 95 97 74 06 zz</p><p>text2pcap -q -l 156 y.hex y.pcap</p><p>tshark -r y.pcap -V<br />
</p><p>TShark 1.8.4 (cut few characters) Capture Length: 28 bytes (224 bits) [Frame is marked: False] [Frame is ignored: False] [Protocols in frame: user_dlt:rlc-lte] DLT: 156, Payload: rlc-lte (RLC-LTE) RLC-LTE [Can't dissect LTE RLC frame because no per-frame info was attached!]</p></div><div id="comment-16947-info" class="comment-info"><span class="comment-age">(16 Dec '12, 13:48)</span> <span class="comment-user userinfo">s52d</span></div></div><span id="16955"></span><div id="comment-16955" class="comment"><div id="post-16955-score" class="comment-score"></div><div class="comment-text"><p>You need to add a dummy UDP header:</p><pre><code>0000   20 52 45 43 56 00 20 53 45 4e 44 00 08 00 45 00   RECV. SEND...E.
0010   00 38 12 34 00 00 ff 11 a3 7b 01 01 01 01 02 02  .8.4.....{......
0020   02 02 00 00 00 00 00 24 e1 8d 72 6c 63 2d 6c 74  .......$..rlc-lt
0030   65 01 02 02 05 03 00 04 00 06 01 00 07 00 00 01  e...............
0040   58 55 95 97 74 06                                XU..t.</code></pre></div><div id="comment-16955-info" class="comment-info"><span class="comment-age">(16 Dec '12, 22:51)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="17244"></span><div id="comment-17244" class="comment"><div id="post-17244-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I am lost... To summarize: to get RRC decoded, we put dummy RLC around, and into dummy UDP. But I keep failing: I got <strong>something</strong> by changing settings of wireshark, but even demos from rlc_lte_logger.c and mac_pcap_sample_code.c are failing. May I ask for good RRC sample, so I can find where I got lost? Thanks!</p></div><div id="comment-17244-info" class="comment-info"><span class="comment-age">(26 Dec '12, 10:53)</span> <span class="comment-user userinfo">s52d</span></div></div><span id="17249"></span><div id="comment-17249" class="comment not_top_scorer"><div id="post-17249-score" class="comment-score"></div><div class="comment-text"><p>Managed! New look at it, by defining lte-rrc.dl.ccch in user_dlts.</p><p>So, by putting each type in own hex file, calling text2pcap for each one, it can be done. Back to coding.</p></div><div id="comment-17249-info" class="comment-info"><span class="comment-age">(26 Dec '12, 22:56)</span> <span class="comment-user userinfo">s52d</span></div></div></div><div id="comment-tools-16851" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-16851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

