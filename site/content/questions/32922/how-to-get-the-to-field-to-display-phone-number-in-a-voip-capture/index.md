+++
type = "question"
title = "How to get the &#x27;To&#x27; field to display phone number in a VOIP capture"
description = '''I&#x27;m capturing fax calls from our fax server going out over a SIP connection. The &#x27;From&#x27; field shows up as I would like it to &#x27;SIP:FaxServerName@company.org&#x27;, I configured this on my RightFax board server, but the &#x27;To&#x27; field just shows up as &#x27;SIP:9&#x27;. I need to see the fax number being dialed. Am I ca...'''
date = "2014-05-19T15:43:00Z"
lastmod = "2014-05-19T19:25:00Z"
weight = 32922
keywords = [ "to", "voip", "field" ]
aliases = [ "/questions/32922" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the 'To' field to display phone number in a VOIP capture](/questions/32922/how-to-get-the-to-field-to-display-phone-number-in-a-voip-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing fax calls from our fax server going out over a SIP connection. The 'From' field shows up as I would like it to 'SIP:[email protected]', I configured this on my RightFax board server, but the 'To' field just shows up as 'SIP:9'. I need to see the fax number being dialed. Am I capturing the wrong adapter? Or is there a setting where I can configure what the column displays? I see the fax number at the t.38 level when I graph it out, but I need to see it in the list of calls prior to the graph so I can select the right one to graph.</p></div><div id="question-tags" class="tags-container tags">to voip field</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '14, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/0a3cb6f8ce051498db97f39efb9bd24a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JackieB727&#39;s gravatar image" /><p>JackieB727<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JackieB727 has no accepted answers">0%</span></p></div></div><div id="comments-container-32922" class="comments-container"></div><div id="comment-tools-32922" class="comment-tools"></div><div class="clear"></div><div id="comment-32922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32924"></span>

<div id="answer-container-32924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32924-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"sip:9" indicates that the digit "9" is the only digit collected for the INVITE request. Its possible that the rest of the digits may be being sent via DTMF relay or inband DTMF if using g.711 codec. A sample trace of a completed fax setup would really help to drill down further.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '14, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-32924" class="comments-container"><span id="32935"></span><div id="comment-32935" class="comment"><div id="post-32935-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the reply. Here's a sample of the call setup. Would I need to modify Wireshark to capture the number differently? xxx-xxx-5076 is the number I'm trying to capture in the 'To' field.</p><pre><code>     |                   
|563.948  |         INVITE SDP ( g711U g711A)          |SIP From: sip:[email protected] To:sip:
|         |(5060)   ------------------&gt;  (5060)   |
|563.971  |         100 Trying|                   |SIP Status
|         |(5060)   &lt;------------------  (5060)   |
|564.303  |         180 Ringing                   |SIP Status
|         |(5060)   &lt;------------------  (5060)   |
|567.727  |         200 OK SDP ( g711U g711A)          |SIP Status
|         |(5060)   &lt;------------------  (5060)   |
|567.728  |         ACK       |                   |SIP Request
|         |(5060)   ------------------&gt;  (5060)   |
|567.742  |         RTP (g711A)                   |RTP Num packets:322  Duration:6.421s SSRC:0x18BE
|         |(56016)  ------------------&gt;  (6350)   |
|567.757  |         RTP (g711A)                   |RTP Num packets:133  Duration:2.640s SSRC:0xD2822D50
|         |(56016)  &lt;------------------  (6350)   |
|570.437  |         RTP (RTPType-103)             |RTP Num packets:183  Duration:3.640s SSRC:0xD2822D50
|         |(56016)  &lt;------------------  (6350)   |
|574.119  |         INVITE SDP ( t38)             |SIP Request
|         |(5060)   &lt;------------------  (5060)   |
|574.120  |         200 OK SDP ( t38)             |SIP Status
|         |(5060)   ------------------&gt;  (5060)   |
|574.154  |         ACK       |                   |SIP Request
|         |(5060)   &lt;------------------  (5060)   |
|574.166  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  ------------------&gt;  (6352)   |
|574.414  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  ------------------&gt;  (6352)   |
|576.897  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  &lt;------------------  (6352)   |
|579.997  |         v21-preamble                  |t38:t30 Ind:v21-preamble
|         |(56016)  &lt;------------------  (6352)   |
|581.557  |         NSF       |                   |t38:v21:HDLC:Non-Standard Facilities
|         |(56016)  &lt;------------------  (6352)   |
|582.257  |         CSI Num: xxx-xxx-5076           |t38:v21:HDLC:Called Subscriber Identification
|         |(56016)  &lt;------------------  (6352)   |
|582.697  |         DIS DSR:ITU-T V.27 ter, V.29, and V.17          |t38:v21:HDLC:Digital Identification Signal
|         |(56016)  &lt;------------------  (6352)   |
|582.758  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  ------------------&gt;  (6352)   |
|582.777  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  &lt;------------------  (6352)   |
|582.836  |         v21-preamble                  |t38:t30 Ind:v21-preamble
|         |(56016)  ------------------&gt;  (6352)   |
|583.836  |         TSI Num: companyname.ORG RFTestServer          |t38:v21:HDLC:Transmitting Subscriber Identification
|         |(56016)  ------------------&gt;  (6352)   |
|584.446  |         DCS DSR:14 400 bit/s, ITU-T V.17          |t38:v21:HDLC:Digital Command Signal
|         |(56016)  ------------------&gt;  (6352)   |
|584.633  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  ------------------&gt;  (6352)   |
|584.711  |         v17-14400-long-training          |t38:t30 Ind:v17-14400-long-training
|         |(56016)  ------------------&gt;  (6352)   |
|586.102  |         t4-non-ecm-data:v17-14400          |t38:t4-non-ecm-data:v17-14400 Duration: 1.47s No packet lost
|         |(56016)  ------------------&gt;  (6352)   |
|587.633  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  ------------------&gt;  (6352)   |
|587.711  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  ------------------&gt;  (6352)   |
|588.778  |         v21-preamble                  |t38:t30 Ind:v21-preamble
|         |(56016)  &lt;------------------  (6352)   |
|589.837  |         CFR       |                   |t38:v21:HDLC:Confirmation To Receive
|         |(56016)  &lt;------------------  (6352)   |
|589.899  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  ------------------&gt;  (6352)   |
|589.918  |         no-signal |                   |t38:t30 Ind:no-signal
|         |(56016)  &lt;------------------  (6352)   |
|589.977  |         v17-14400-short-training          |t38:t30 Ind:v17-14400-short-training
|         |(56016)  ------------------&gt;  (6352)   |
|590.368  |         FCD Frm num: 0                |t38:v17-14400:HDLC:Facsimile coded data
|         |(56016)  ------------------&gt;  (6352)   |</code></pre></div><div id="comment-32935-info" class="comment-info"><span class="comment-age">(20 May '14, 13:27)</span> JackieB727</div></div><span id="32941"></span><div id="comment-32941" class="comment"><div id="post-32941-score" class="comment-score"></div><div class="comment-text"><p>@JackieB727</p><p>Its difficult to tell exactly without seeing the actual trace, but from the summary you provided below, there are 183 dynamic RTP packets in the trace. Usually dynamic RTP indicats some type of telephony event such as DTMF. I think it is fair to say that digits are being sent in-band via dynamic RTP telephony events once the session has been established. Your devices look to be set to use/recognize RTP Payload Type 103 as DTMF. The snippet below shows the line in your sample to indicate the events I am talking about.</p><p>"570.437 RTP (RTPType-103) RTP Num packets:183 Duration:3.640s"</p><p>I have seen instances where the digits are visible in the payload. You could filter on the payload type with "rtp.p_type==103" and then create a column "rtp.payload". In the payload, look for the first instance of the byte "18". In my experience, the byte following the "18" is your DTMF digit. There will be multiple instances of this pattern in the payload depending on the length of sample size, and multiple packets of the same digit depending on the length of the DTMF tone duration.</p><p>Its very easy to see DTMF events if the UA's are using RFC2833 DTMF relay.</p><p>If you want further, more accurate analysis, you really should provide an actual trace. I really hope this helps.</p></div><div id="comment-32941-info" class="comment-info"><span class="comment-age">(20 May '14, 18:00)</span> Rooster_50</div></div></div><div id="comment-tools-32924" class="comment-tools"></div><div class="clear"></div><div id="comment-32924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

