+++
type = "question"
title = "HEX string to payload text"
description = '''Hi,  i have a hex string which is S1AP/X2AP/RRC payload. I need to covert it to text for example : HEX STRING : 401D004C5DD80000 OUT PUT : UL-CCCH-Message message: c1 (0)   c1: rrcConnectionRequest (1)   rrcConnectionRequest   criticalExtensions: rrcConnectionRequest-r8 (0)   rrcConnectionRequest-r8...'''
date = "2013-11-16T02:42:00Z"
lastmod = "2013-11-16T02:42:00Z"
weight = 27045
keywords = [ "x2ap", "lte", "s1ap" ]
aliases = [ "/questions/27045" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HEX string to payload text](/questions/27045/hex-string-to-payload-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27045-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have a hex string which is S1AP/X2AP/RRC payload. I need to covert it to text for example :</p><p>HEX STRING : 401D004C5DD80000</p><p>OUT PUT : UL-CCCH-Message</p><pre><code>message: c1 (0)

    c1: rrcConnectionRequest (1)

        rrcConnectionRequest

            criticalExtensions: rrcConnectionRequest-r8 (0)

                rrcConnectionRequest-r8

                    ue-Identity: s-TMSI (0)

                        s-TMSI

                            mmec: 01 [bit length 8, 0000 0001 decimal value 1]

                            m-TMSI: d004c5dd [bit length 32, 1101 0000  0000 0100  1100 0101  1101 1101 decimal value 3489973725]

                    establishmentCause: mo-Data (4)

                    spare: 00 [bit length 1, 7 LSB pad bits, 0... .... decimal value 0]</code></pre><p>3GPPdecoder only suport RRC for LTE. Is is possible to do it using wireshark/tshark ?</p><p>Thanks &amp; Regards, SM</p></div><div id="question-tags" class="tags-container tags">x2ap lte s1ap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '13, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/276dd2e60fd9f342b8fc2d3bd102886e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Surajitm&#39;s gravatar image" /><p>Surajitm<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Surajitm has no accepted answers">0%</span></p></div></div><div id="comments-container-27045" class="comments-container"></div><div id="comment-tools-27045" class="comment-tools"></div><div class="clear"></div><div id="comment-27045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

