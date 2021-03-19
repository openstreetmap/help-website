+++
type = "question"
title = "Use Wireshark as a decoder"
description = '''Hi Everyone,  I have a task to write an application that would take an encoded RRC (3GPP protocol) message, translate it to some human readable format(text, xml, etc) and store it in the database. The question is can Wireshark be used by a 3rd party application as a protocol decoder? Does it have an...'''
date = "2015-01-10T09:56:00Z"
lastmod = "2015-01-10T10:17:00Z"
weight = 39027
keywords = [ "wireshark" ]
aliases = [ "/questions/39027" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Use Wireshark as a decoder](/questions/39027/use-wireshark-as-a-decoder)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39027-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone,</p><p>I have a task to write an application that would take an encoded RRC (3GPP protocol) message, translate it to some human readable format(text, xml, etc) and store it in the database.</p><p>The question is can Wireshark be used by a 3rd party application as a protocol decoder? Does it have any kind of API that can be used by external application?</p><p>If that is possible can you please direct me to the right source of information?</p><p>/Alex<br />
</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '15, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/986dff787b6f19aeab2d4fe0cb5c8cfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander&#39;s gravatar image" /><p>Alexander<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39027" class="comments-container"></div><div id="comment-tools-39027" class="comment-tools"></div><div class="clear"></div><div id="comment-39027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39028"></span>

<div id="answer-container-39028" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39028-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes you can use text2pcap + tshark to achieve this. Look at <a href="https://ask.wireshark.org/questions/28735/decode-sms-bearer-data-hex-string">this thread</a> for details.</p><p>For RRC protocol, here is the list of applicable payload protocols:</p><pre><code>rrc.dl.dcch, rrc.ul.dcch, rrc.dl.ccch, rrc.ul.ccch, rrc.pcch, rrc.dl.shcch, rrc.ul.shcch, rrc.bcch.fach, rrc.bcch.bch, rrc.mcch, rrc.msch, rrc.sysinfo, rrc.sysinfo.cont, rrc.si.mib, rrc.si.sib1, rrc.si.sib2, rrc.si.sib3, rrc.si.sib4, rrc.si.sib5, rrc.si.sib5bis, rrc.si.sib6, rrc.si.sib7, rrc.si.sib8, rrc.si.sib9, rrc.si.sib10, rrc.si.sib11, rrc.si.sib11bis, rrc.si.sib12, rrc.si.sib13, rrc.si.sib13-1, rrc.si.sib13-2, rrc.si.sib13-3, rrc.si.sib13-4, rrc.si.sib14, rrc.si.sib15, rrc.si.sib15bis, rrc.si.sib15-1, rrc.si.sib15-1bis, rrc.si.sib15-2, rrc.si.sib15-2bis, rrc.si.sib15-2ter, rrc.si.sib15-3, rrc.si.sib15-3bis, rrc.si.sib15-4, rrc.si.sib15-5, rrc.si.sib15-6, rrc.si.sib15-7, rrc.si.sib15-8, rrc.si.sib16, rrc.si.sib17, rrc.si.sib18, rrc.si.sib19, rrc.si.sib20, rrc.si.sib21, rrc.si.sib22, rrc.si.sb1, rrc.si.sb2, rrc.irat.ho_to_utran_cmd, rrc.irat.irat_ho_info, rrc.ue_radio_access_cap_info</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '15, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39028" class="comments-container"><span id="39033"></span><div id="comment-39033" class="comment"><div id="post-39033-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thanks for the idea. It looks like an option but I assume it will have performance problems for a large amount of messages since at least two intermediate files need to be created. Is there any library that would provide the functionality you described above in the form of API functions calls?</p><p>Thanks</p><p>A</p></div><div id="comment-39033-info" class="comment-info"><span class="comment-age">(10 Jan '15, 14:45)</span> Alexander</div></div><span id="39034"></span><div id="comment-39034" class="comment"><div id="post-39034-score" class="comment-score"></div><div class="comment-text"><p>No there is no official API. You will need to link directly libwireshark.dll (meaning that your program will now be GPL) and dive in the source code to find the entry points are they are not documented (other than the comments).</p></div><div id="comment-39034-info" class="comment-info"><span class="comment-age">(10 Jan '15, 15:02)</span> Pascal Quantin</div></div><span id="39040"></span><div id="comment-39040" class="comment"><div id="post-39040-score" class="comment-score"></div><div class="comment-text"><p>One more question. How to find the right protocol decoder(you listed above) having the RRC message type name (e.g. RRCConnectionRequest)? Can wireshark some how help with such mapping?</p><p>Thanks!</p></div><div id="comment-39040-info" class="comment-info"><span class="comment-age">(11 Jan '15, 04:23)</span> Alexander</div></div><span id="39045"></span><div id="comment-39045" class="comment"><div id="post-39045-score" class="comment-score"></div><div class="comment-text"><p>The mapping is given in 3GPP 25.331 ASN.1 definition. For example a RRC Connection Request is a rrc.ul.ccch message. You can also find a copy of the ASN.1 description used by Wireshark here: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=asn1/rrc/Class-definitions.asn;hb=refs/heads/master">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=asn1/rrc/Class-definitions.asn;hb=refs/heads/master</a></p><p>By the way, you are referring to the 3G RRC right? Not the LTE version? Because if it's the LTE version you are interested in, the payload protocols are different.</p></div><div id="comment-39045-info" class="comment-info"><span class="comment-age">(11 Jan '15, 07:34)</span> Pascal Quantin</div></div><span id="39046"></span><div id="comment-39046" class="comment"><div id="post-39046-score" class="comment-score"></div><div class="comment-text"><p>LTE for now, 3G I will need as well but a bit later. So need both.</p></div><div id="comment-39046-info" class="comment-info"><span class="comment-age">(11 Jan '15, 07:53)</span> Alexander</div></div><span id="39048"></span><div id="comment-39048" class="comment not_top_scorer"><div id="post-39048-score" class="comment-score"></div><div class="comment-text"><p>Then the protocol payloads are: lte-rrc.bcch.bch, lte-rrc.bcch.dl.sch, lte-rrc.pcch, lte-rrc.dl.ccch, lte-rrc.dl.dcch, lte-rrc.ul.ccch, lte-rrc.ul.dcch, lte-rrc.mcch. Those are the top levels PDUs as found in the ASN.1 description.</p><p>The ASN.1 description can be found in 3GPP 36.331. The one used by Wireshark development builds is: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=asn1/lte-rrc/EUTRA-RRC-Definitions.asn;hb=refs/heads/master">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=asn1/lte-rrc/EUTRA-RRC-Definitions.asn;hb=refs/heads/master</a></p></div><div id="comment-39048-info" class="comment-info"><span class="comment-age">(11 Jan '15, 08:44)</span> Pascal Quantin</div></div><span id="39056"></span><div id="comment-39056" class="comment not_top_scorer"><div id="post-39056-score" class="comment-score"></div><div class="comment-text"><p>Pascal, Thanks a lot!</p></div><div id="comment-39056-info" class="comment-info"><span class="comment-age">(11 Jan '15, 10:26)</span> Alexander</div></div></div><div id="comment-tools-39028" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-39028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

