+++
type = "question"
title = "How can I find the correct dissector programmatically?"
description = '''I am developing an application in C# using wireshark and I need to find the right dissector programmatically. By now I can dissect a LTE message but I need to put the dissector manually everytime. I would like to know how I can do that with the program finding the correct dissector by itself. Also, ...'''
date = "2014-10-16T06:13:00Z"
lastmod = "2014-10-16T07:59:00Z"
weight = 37108
keywords = [ "wcdma", "dissector", "gsm", "lte", "wireshark" ]
aliases = [ "/questions/37108" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I find the correct dissector programmatically?](/questions/37108/how-can-i-find-the-correct-dissector-programmatically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37108-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing an application in C# using wireshark and I need to find the right dissector programmatically. By now I can dissect a LTE message but I need to put the dissector manually everytime. I would like to know how I can do that with the program finding the correct dissector by itself. Also, is there any list of LTE, WCDMA and GSM wireshark dissectors?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">wcdma dissector gsm lte wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '14, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/4de92f5cbacdafb96fdad81319ad4341?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lsilva&#39;s gravatar image" /><p>lsilva<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lsilva has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '14, 06:13</p></div></div><div id="comments-container-37108" class="comments-container"></div><div id="comment-tools-37108" class="comment-tools"></div><div class="clear"></div><div id="comment-37108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37112"></span>

<div id="answer-container-37112" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37112-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot deduce which dissector you need from the message dump itself: there is nothing at the beginning of the payload giving you the protocol to be used. Instead you need to know it from some meta data or proprietary information.</p><p>Regarding the list of 2G/3G/4G dissectors, it is quite long.</p><p>For LTE: mac-lte (needs meta data that can be provided through UDP framing protocol, see <a href="http://wiki.wireshark.org/MAC-LTE),">http://wiki.wireshark.org/MAC-LTE),</a> rlc-lte (needs meta data that can be provided through UDP framing protocol, see <a href="http://wiki.wireshark.org/RLC-LTE),">http://wiki.wireshark.org/RLC-LTE),</a> pdcp-lte (needs meta data that can be provided through UDP framing protocol, see <a href="http://wiki.wireshark.org/PDCP-LTE),">http://wiki.wireshark.org/PDCP-LTE),</a> lte-rrc.bcch.bch, lte-rrc.bcch.dl.sch, lte-rrc.pcch, lte-rrc.dl.ccch, lte-rrc.dl.dcch, lte-rrc.ul.ccch, lte-rrc.ul.dcch, lte-rrc.mcch, nas-eps, nas-eps_plain</p><p>For UMTS: mac.fdd.rach, mac.fdd.fach, mac.fdd.pch, mac.fdd.dch, mac.fdd.edch, mac.fdd.edch.type2, mac.fdd.hsdsch, rlc.bcch, rlc.pcch, rlc.ccch, rlc.ctch, rlc.dcch, rlc.ps_dtch, rlc.dch_unknown, rrc.dl.dcch, rrc.ul.dcch, rrc.dl.ccch, rrc.pcch, rrc.dl.shcch, rrc.ul.shcch, rrc.bcch.fach, rrc.bcch.bch, rrc.mcch, rrc.msch, rrc.irat.ho_to_utran_cmd, rrc.irat.irat_ho_info, rrc.sysinfo, rrc.sysinfo.cont, rrc.ue_radio_access_cap_info, rrc.si.mib, rrc.si.sib1, rrc.si.sib2, rrc.si.sib3, rrc.si.sib4, rrc.si.sib5, rrc.si.sib5bis, rrc.si.sib6, rrc.si.sib7, rrc.si.sib8, rrc.si.sib9, rrc.si.sib10, rrc.si.sib11, rrc.si.sib11bis, rrc.si.sib12, rrc.si.sib13, rrc.si.sib13-1, rrc.si.sib13-2, rrc.si.sib13-3, rrc.si.sib13-4, rrc.si.sib14, rrc.si.sib15, rrc.si.sib15bis, rrc.si.sib15-1, rrc.si.sib15-1bis, rrc.si.sib15-2, rrc.si.sib15-2bis, rrc.si.sib15-2ter, rrc.si.sib15-3, rrc.si.sib15-3bis, rrc.si.sib15-4, rrc.si.sib15-5, rrc.si.sib15-6, rrc.si.sib15-7, rrc.si.sib15-8, rrc.si.sib16, rrc.si.sib17, rrc.si.sib18, rrc.si.sib19, rrc.si.sib20, rrc.si.sib21, rrc.si.sib22, rrc.si.sb1, rrc.si.sb2, gsm_a_dtap</p><p>For GSM/GPRS: lapdm, gsm_a_sacch, gsm_a_dtap, gsm_rlcmac_dl, gsm_rlcmac_ul, llcgprs, sndcp, sndcpxid</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '14, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-37112" class="comments-container"><span id="37317"></span><div id="comment-37317" class="comment"><div id="post-37317-score" class="comment-score"></div><div class="comment-text"><p>When you say from meta data, what does that mean? I've seen in one of the topics here that you can find the correct LTE dissector based on the link direction and channel type. Is there anything like that to GSM and WCDMA?</p></div><div id="comment-37317-info" class="comment-info"><span class="comment-age">(23 Oct '14, 12:12)</span> lsilva</div></div><span id="37319"></span><div id="comment-37319" class="comment"><div id="post-37319-score" class="comment-score"></div><div class="comment-text"><p>For WCDMA RRC you will need to know the channel type, for GPRS you will need the direction, etc. By metadata I mean the information specific to each layer allowing you to identify which dissector is required (as you cannot deduce it from the payload). Wireshark cannot do that for you. You need to add I your own application whatever logic is required to select the dissector depending on your input file or data.</p></div><div id="comment-37319-info" class="comment-info"><span class="comment-age">(23 Oct '14, 13:08)</span> Pascal Quantin</div></div></div><div id="comment-tools-37112" class="comment-tools"></div><div class="clear"></div><div id="comment-37112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

