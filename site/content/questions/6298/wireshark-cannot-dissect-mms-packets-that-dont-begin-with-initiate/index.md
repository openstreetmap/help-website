+++
type = "question"
title = "Wireshark cannot dissect MMS packets that don&#x27;t begin with Initiate"
description = '''If Wireshark captures packets after Initiate Service (such as Initiate-Request and Initiate-Response), Wireshark dissects the message down to ISO8823 OSI Presentation Protocol, but the presentation data can&#x27;t be decoded as MMS. How do I get the MMS portion to decode properly? Network packet: 0000 aa...'''
date = "2011-09-12T19:21:00Z"
lastmod = "2011-09-12T21:28:00Z"
weight = 6298
keywords = [ "capture", "mms" ]
aliases = [ "/questions/6298" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark cannot dissect MMS packets that don't begin with Initiate](/questions/6298/wireshark-cannot-dissect-mms-packets-that-dont-begin-with-initiate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6298-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If Wireshark captures packets after Initiate Service (such as <em>Initiate-Request</em> and <em>Initiate-Response</em>), Wireshark dissects the message down to ISO8823 OSI Presentation Protocol, but the presentation data can't be decoded as MMS. How do I get the MMS portion to decode properly?</p><p><strong>Network packet:</strong></p><pre><code>0000   aa c0 a8 06 c8 aa 00 21 70 6b 0c 67 08 00 45 00  .......!pk.g..E.
0010   00 67 2f bc 40 00 80 06 42 88 c0 a8 03 34 c0 a8  .g/[email protected]
0020   03 c8 0f 75 00 66 2c 00 28 24 ad d8 00 da 50 18  ...u.f,.($....P.
0030   fa e3 88 a6 00 00 03 00 00 3f 02 f0 80 01 00 01  .........?......
0040   00 61 32 30 30 02 01 03 a0 2b a0 29 02 02 01 b5  .a200....+.)....
0050   a4 23 a1 21 a0 1f 30 1d a0 1b a1 19 1a 09 44 45  .#.!..0.......DE
0060   50 35 30 30 4e 53 52 1a 0c 4c 4c 4e 30 24 53 50  P500NSR..LLN0$SP
0070   24 53 47 43 42                                   $SGCB</code></pre><p><strong>Dissection result from Wireshark 1.2.9:</strong></p><pre><code>ISO 8823 OSI Presentation Protocol
  user-data: fully-encoded-data (1)
    fully-encoded-data: 1 item
      PDV-list
        presentation-context-identifier: 3
      presentation-data-values: single-ASN1-type (0)
        dissector is not available
          Expert Info (Warn/Undecoded): Dissector is not available
            Message: Dissector is not available
            Severity level: Warn
            Group: Undecoded
          single-ASN1-type: A029020201B5A423A121A01F301DA01BA1191A0944455035...</code></pre></div><div id="question-tags" class="tags-container tags">capture mms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '11, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p>ylda_ljm0620<br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '11, 23:28</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6298" class="comments-container"></div><div id="comment-tools-6298" class="comment-tools"></div><div class="clear"></div><div id="comment-6298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6299"></span>

<div id="answer-container-6299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6299-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, That is because there is nothing in that packet saying what the data is except the presentation-context-identifier, to know what the presentation-context is the setup information is needed. It might be possible to create "decode as" functionality but no one has written code to do that yet. Regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '11, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-6299" class="comments-container"><span id="6301"></span><div id="comment-6301" class="comment"><div id="post-6301-score" class="comment-score"></div><div class="comment-text"><p>re:to know what the presentation-context is the setup information is needed</p><p>thanks, but what is your mean? about what setup information?</p><p>additonally, mms-ethereal can dissect that packet the same as before. why wireshark (any version) can not?</p></div><div id="comment-6301-info" class="comment-info"><span class="comment-age">(12 Sep '11, 21:56)</span> ylda_ljm0620</div></div><span id="6302"></span><div id="comment-6302" class="comment"><div id="post-6302-score" class="comment-score"></div><div class="comment-text"><p>The information in "initiate-request and initiate-response" is needed to know what the presentation conext is. I would guess that it worked earlier at the expence of some other protocol, missinterpreating someting as MMS.</p></div><div id="comment-6302-info" class="comment-info"><span class="comment-age">(12 Sep '11, 22:28)</span> Anders ♦</div></div><span id="6303"></span><div id="comment-6303" class="comment"><div id="post-6303-score" class="comment-score"></div><div class="comment-text"><p>(please use "add a comment" instead of adding a new answer when responding, see the FAQ for details)</p></div><div id="comment-6303-info" class="comment-info"><span class="comment-age">(12 Sep '11, 22:36)</span> SYN-bit ♦♦</div></div><span id="6309"></span><div id="comment-6309" class="comment"><div id="post-6309-score" class="comment-score"></div><div class="comment-text"><p>sorry, i will add a comment.</p><p>initiate-request and initiate-response" means Initiate-RequestPDU and Initiate-ResponsePDU in ISO/FDIS 9506-2.</p></div><div id="comment-6309-info" class="comment-info"><span class="comment-age">(12 Sep '11, 23:50)</span> ylda_ljm0620</div></div><span id="6311"></span><div id="comment-6311" class="comment not_top_scorer"><div id="post-6311-score" class="comment-score"></div><div class="comment-text"><p>when 61850 server associates to 61850 client, they have MMS packets, just Initiate-RequestPDU and Initiate-ResponsePDU.</p><p>if wireshar is started and captures firstly, and then 61850 server associates to 61850 client, the presentation data can be decoded as MMS.</p><p>if 61850 server associates to 61850 client firstly, and then wireshar is started and captures, the presentation data can't be decoded as MMS.</p></div><div id="comment-6311-info" class="comment-info"><span class="comment-age">(12 Sep '11, 23:50)</span> ylda_ljm0620</div></div><span id="6314"></span><div id="comment-6314" class="comment not_top_scorer"><div id="post-6314-score" class="comment-score"></div><div class="comment-text"><p>I am sorry. "add a comment" can not let me write follows. so i answer again.</p><p><strong>mms-ethereal disscets as :</strong></p><pre><code>ISO 8823 OSI Presentation Protocol
  user-data: fully-encoded-data (1)
    fully-encoded-data: 1 item
      Item
        presentation-context-identifier: 3
        presentation-data-values: single-ASN1-type (0)
ISO/IEC 9506 MMS
  Conf Request (0)
  Read (4)
  InvokeID: InvokeID:  437
  Read
        List of Variable
                VariableSpecification
                          Object Name
                                      Domain Specific 
                DomainName:  
                  DomainName: DEP500NSR
                ItemName:  
                  ItemName: LLN0$SP$SGCB

**but wireshark1.2.9 dissects as before.**</code></pre></div><div id="comment-6314-info" class="comment-info"><span class="comment-age">(13 Sep '11, 00:01)</span> ylda_ljm0620</div></div><span id="6317"></span><div id="comment-6317" class="comment not_top_scorer"><div id="post-6317-score" class="comment-score"></div><div class="comment-text"><p>Sonds lik eyou should open up a bug report and attach the two examples e.g the one working and the one when it's not working</p></div><div id="comment-6317-info" class="comment-info"><span class="comment-age">(13 Sep '11, 05:45)</span> Anders ♦</div></div><span id="6318"></span><div id="comment-6318" class="comment"><div id="post-6318-score" class="comment-score">3</div><div class="comment-text"><p>Hi, Go to Edit-&gt;preferences-&gt;protocol-&gt;PRES and edit the users context tale</p><p>enter context = 3 and OID = 1.0.9506.2.3 and your trace will be dissected as MMS.</p></div><div id="comment-6318-info" class="comment-info"><span class="comment-age">(13 Sep '11, 06:39)</span> Anders ♦</div></div><span id="6348"></span><div id="comment-6348" class="comment not_top_scorer"><div id="post-6348-score" class="comment-score"></div><div class="comment-text"><p>Thanks. it works in wireshark interface.</p><p>but how to set parameters of "tshark" if i hope to use thark to convert mms packet as before to text.(like the result of 'enter context = 3 and OID = 1.0.9506.2.3')</p><p>if enter "tshark -r d:sg1.pcap -V -T text &gt; d:sg1.txt", it will appear "single-ASN1-type: A029020201B5A423A121A01F301DA01BA1191A0944455035..." in text.</p></div><div id="comment-6348-info" class="comment-info"><span class="comment-age">(14 Sep '11, 01:42)</span> ylda_ljm0620</div></div><span id="6367"></span><div id="comment-6367" class="comment not_top_scorer"><div id="post-6367-score" class="comment-score"></div><div class="comment-text"><p>I think once you set the setting in the wireshark gui, the tshark interface will pick up those changes, as long as you are the same user. I'm on linux and that is what happens for me. But i think you should be able to access that table from tshark directly, but I don't know the syntax</p></div><div id="comment-6367-info" class="comment-info"><span class="comment-age">(14 Sep '11, 12:57)</span> iondiode</div></div></div><div id="comment-tools-6299" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-6299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

