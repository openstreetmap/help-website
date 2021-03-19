+++
type = "question"
title = "Problem with MMS disector"
description = '''I have captures of MMS (Manufacturer Messagges Specificatiom) messagges that wireshark can&#x27;t solve correctly (i.e., the MMS dissector doesn´t recognizes as MMS messagges). What can I do?'''
date = "2011-01-27T07:25:00Z"
lastmod = "2011-08-11T04:00:00Z"
weight = 1971
keywords = [ "mms" ]
aliases = [ "/questions/1971" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with MMS disector](/questions/1971/problem-with-mms-disector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1971-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captures of MMS (Manufacturer Messagges Specificatiom) messagges that wireshark can't solve correctly (i.e., the MMS dissector doesn´t recognizes as MMS messagges). What can I do?</p></div><div id="question-tags" class="tags-container tags">mms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '11, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/570dd5821641ca3cb3a29c2fadc867e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cgalli&#39;s gravatar image" /><p>cgalli<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cgalli has no accepted answers">0%</span></p></div></div><div id="comments-container-1971" class="comments-container"><span id="1976"></span><div id="comment-1976" class="comment"><div id="post-1976-score" class="comment-score"></div><div class="comment-text"><p>Another related question: why MMS protocol is not available in the "Decode As Dialog Box"?</p></div><div id="comment-1976-info" class="comment-info"><span class="comment-age">(27 Jan '11, 10:33)</span> cgalli</div></div><span id="2034"></span><div id="comment-2034" class="comment"><div id="post-2034-score" class="comment-score">1</div><div class="comment-text"><p>What protocol carries your MMS packets? Looking at the source code it looks like the MMS dissector runs on top of COTP or is called by OID 1.0.9506.2.3.</p></div><div id="comment-2034-info" class="comment-info"><span class="comment-age">(31 Jan '11, 04:38)</span> Anders ♦</div></div><span id="2038"></span><div id="comment-2038" class="comment"><div id="post-2038-score" class="comment-score"></div><div class="comment-text"><p>You're right. In fact, Wireshark dissects the messagges down to ISO8823 OSI Presentation Protocol, but the presentation data can't be decoded as MMS. It's pretty odd. I cant't see why.</p></div><div id="comment-2038-info" class="comment-info"><span class="comment-age">(31 Jan '11, 06:07)</span> cgalli</div></div><span id="2046"></span><div id="comment-2046" class="comment"><div id="post-2046-score" class="comment-score">1</div><div class="comment-text"><p>You could write a bug report at https://bugs.wireshark.org/bugzilla including your trace so one of the developers can take a look at it. You can mark the bug as private to limet vissiblity to core developers if yo wish.</p></div><div id="comment-2046-info" class="comment-info"><span class="comment-age">(31 Jan '11, 12:44)</span> Anders ♦</div></div><span id="2062"></span><div id="comment-2062" class="comment"><div id="post-2062-score" class="comment-score"></div><div class="comment-text"><p>thanks for your help and interest.</p></div><div id="comment-2062-info" class="comment-info"><span class="comment-age">(01 Feb '11, 04:03)</span> cgalli</div></div><span id="5640"></span><div id="comment-5640" class="comment not_top_scorer"><div id="post-5640-score" class="comment-score"></div><div class="comment-text"><p>MMS isn't available in "Decode As" because there's no general "Decode As" mechanism - "Decode As" knows about particular types of handoff, and COTP -&gt; xxx is not currently one of them.</p></div><div id="comment-5640-info" class="comment-info"><span class="comment-age">(10 Aug '11, 20:55)</span> Guy Harris ♦♦</div></div><span id="6361"></span><div id="comment-6361" class="comment not_top_scorer"><div id="post-6361-score" class="comment-score"></div><div class="comment-text"><p>what parameters "tshark" should have to get the result as setting "Context-Id = 3 Syntax Name OID = 1.0.9506.2.3" on wireshark interface?</p></div><div id="comment-6361-info" class="comment-info"><span class="comment-age">(14 Sep '11, 05:59)</span> ylda_ljm0620</div></div></div><div id="comment-tools-1971" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-1971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5635"></span>

<div id="answer-container-5635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5635-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was also having problems with this, if your capture does not contain a reference to the context, that is, if it only contains data packets, the current version of wireshark can't determine how to decode the PDU.</p><p>To force the presentation layer to decode as MMS, go to Preferences-&gt;Protocols-&gt;Presentation-&gt;User Context List and add a new element with</p><p>Context-Id = 3 Syntax Name OID = 1.0.9506.2.3</p><p>I think this is your bug , closed as worksforme by Anders.</p><p>https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5642</p><p>Not sure why his build would decode your capture properly, but mine didn't.</p><p>With this additional user context table, it looks like your file decodes properly. Full decode can be viewed, but I only printed summary decode.</p><pre><code>$ tshark  -R mms -r  ~/Downloads/d400_p132_pulseOFF.pcap 
 43   1.158915 192.168.100.5 -&gt; 192.168.100.51 MMS 122 confirmed-RequestPDU 
 45   1.177820 192.168.100.51 -&gt; 192.168.100.5 MMS 176 confirmed-ResponsePDU 
 47   1.179104 192.168.100.5 -&gt; 192.168.100.51 MMS 122 confirmed-RequestPDU 
 50   1.210306 192.168.100.51 -&gt; 192.168.100.5 MMS 584 confirmed-ResponsePDU 
120   3.324338 192.168.100.5 -&gt; 192.168.100.51 MMS 122 confirmed-RequestPDU 
122   3.344161 192.168.100.51 -&gt; 192.168.100.5 MMS 176 confirmed-ResponsePDU 
124   3.345619 192.168.100.5 -&gt; 192.168.100.51 MMS 122 confirmed-RequestPDU 
128   3.376620 192.168.100.51 -&gt; 192.168.100.5 MMS 584 confirmed-ResponsePDU 
191   5.487764 192.168.100.5 -&gt; 192.168.100.51 MMS 122 confirmed-RequestPDU 
195   5.498507 192.168.100.51 -&gt; 192.168.100.5 MMS 176 confirmed-ResponsePDU 
199   5.531221 192.168.100.5 -&gt; 192.168.100.51 MMS 122 confirmed-RequestPDU 
201   5.550969 192.168.100.51 -&gt; 192.168.100.5 MMS 584 confirmed-ResponsePDU 
243   6.521548 192.168.100.5 -&gt; 192.168.100.51 MMS 128 confirmed-RequestPDU 
248   6.540381 192.168.100.51 -&gt; 192.168.100.5 MMS 215 confirmed-ResponsePDU 
250   6.541320 192.168.100.5 -&gt; 192.168.100.51 MMS 138 confirmed-RequestPDU 
252   6.564611 192.168.100.51 -&gt; 192.168.100.5 MMS 99 confirmed-ResponsePDU 
253   6.565149 192.168.100.5 -&gt; 192.168.100.51 MMS 138 confirmed-RequestPDU 
254   6.567676 192.168.100.51 -&gt; 192.168.100.5 MMS 99 confirmed-ResponsePDU 
255   6.568880 192.168.100.5 -&gt; 192.168.100.51 MMS 318 confirmed-RequestPDU 
258   6.590589 192.168.100.51 -&gt; 192.168.100.5 MMS 106 confirmed-ResponsePDU 
259   6.592193 192.168.100.5 -&gt; 192.168.100.51 MMS 170 confirmed-RequestPDU 
261   6.614112 192.168.100.51 -&gt; 192.168.100.5 MMS 159 unconfirmed-PDU 
262   6.615719 192.168.100.51 -&gt; 192.168.100.5 MMS 97 confirmed-ResponsePDU</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '11, 17:36</strong></p><img src="https://secure.gravatar.com/avatar/55f24a02ed681bc622c509f0e4a3d9ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iondiode&#39;s gravatar image" /><p>iondiode<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iondiode has no accepted answers">0%</span></p></div></div><div id="comments-container-5635" class="comments-container"><span id="5645"></span><div id="comment-5645" class="comment"><div id="post-5645-score" class="comment-score"></div><div class="comment-text"><p>Awesome! Thanks. It´s really helpfull. All this time I had to decode de messages manually... really tedious. Again. just thanks.</p></div><div id="comment-5645-info" class="comment-info"><span class="comment-age">(11 Aug '11, 03:35)</span> cgalli</div></div></div><div id="comment-tools-5635" class="comment-tools"></div><div class="clear"></div><div id="comment-5635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5646"></span>

<div id="answer-container-5646" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5646-score" class="post-score" title="current number of votes">-2</div></div></td><td><div class="item-right"><div class="answer-body"><p>What mean WCRTESTINPUT on view trafic tcp stream</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '11, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/46d2275b0d19fdbf781e674a06c33a25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dddddddd&#39;s gravatar image" /><p>dddddddd<br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dddddddd has no accepted answers">0%</span></p></div></div><div id="comments-container-5646" class="comments-container"><span id="5648"></span><div id="comment-5648" class="comment"><div id="post-5648-score" class="comment-score"></div><div class="comment-text"><p>Please create a new (coherent) question rather than asking it in an answer to a totally different question.</p></div><div id="comment-5648-info" class="comment-info"><span class="comment-age">(11 Aug '11, 05:02)</span> grahamb ♦</div></div></div><div id="comment-tools-5646" class="comment-tools"></div><div class="clear"></div><div id="comment-5646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

