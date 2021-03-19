+++
type = "question"
title = "Decode GTPv2 TEID as Decimal or Hex?"
description = '''Hello, When I check GTPv2 message with expanding subtree, it is found that TEID is decoded as decimal as below.  TEID/GRE Key: 34604084  But in top of subtree it is decoded as hex as below.  Fully Qualified Tunnel Endpoint Identifier (F-TEID) : S11 MME GTP-C interface, TEID/GRE Key: 0x02100434, IPv4...'''
date = "2013-08-31T00:41:00Z"
lastmod = "2013-08-31T07:52:00Z"
weight = 24221
keywords = [ "gtpv2c" ]
aliases = [ "/questions/24221" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode GTPv2 TEID as Decimal or Hex?](/questions/24221/decode-gtpv2-teid-as-decimal-or-hex)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24221-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>When I check GTPv2 message with expanding subtree, it is found that TEID is decoded as decimal as below.</p><hr /><p>TEID/GRE Key: <strong>34604084</strong></p><hr /><p><br />
But in top of subtree it is decoded as hex as below.</p><hr /><p>Fully Qualified Tunnel Endpoint Identifier (F-TEID) : S11 MME GTP-C interface, TEID/GRE Key: <strong>0x02100434</strong>, IPv4 10.64.194.1</p><hr /><p><br />
I'm wondering both should be hex but is there anyone who knows reason of this?</p></div><div id="question-tags" class="tags-container tags">gtpv2c</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '13, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/0a70735248ce1ad24a7034e389496f61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kaz&#39;s gravatar image" /><p>Kaz<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kaz has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '13, 07:44</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-24221" class="comments-container"></div><div id="comment-tools-24221" class="comment-tools"></div><div class="clear"></div><div id="comment-24221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24229"></span>

<div id="answer-container-24229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24229-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>is there anyone who knows reason of this?</em></p><p>Yes. That's how <a href="http://ask.wireshark.org/users/42/anders">Anders Broman</a> coded it when he committed the change in <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-gtpv2.c?r1=35362&amp;r2=35378">r35378</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24229" class="comments-container"><span id="24236"></span><div id="comment-24236" class="comment"><div id="post-24236-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment! Do you know any intention? I also re-checked other pcap files and as long as I check GTP version 1 and S1AP seem to decode as Hex as below.</p><p>S1AP</p><p>gTP-TEID: 052c2201</p><p>GTP version1</p><p>TEID: 0x22000db5</p><p>So for me, unifying to hex looks beautiful rather than mix hex and decimal. But there might be some purpose for the future use. Do you know any reason?</p></div><div id="comment-24236-info" class="comment-info"><span class="comment-age">(31 Aug '13, 09:43)</span> Kaz</div></div><span id="24307"></span><div id="comment-24307" class="comment"><div id="post-24307-score" class="comment-score"></div><div class="comment-text"><p>Well, it'd probably be better if the representation was consistent, but whether it should be displayed as hexadecimal, decimal, or both may be subjective. What does the GTPv2 specification say about how this field should be represented?</p><p>In any case, feel free to open a <a href="https://bugs.wireshark.org/bugzilla/">bug report</a> asking for the value to be consistently displayed.</p></div><div id="comment-24307-info" class="comment-info"><span class="comment-age">(03 Sep '13, 07:46)</span> cmaynard ♦♦</div></div><span id="24365"></span><div id="comment-24365" class="comment"><div id="post-24365-score" class="comment-score"></div><div class="comment-text"><p>In 3GPP TS 36.444, it seems saying TEID type is octets string. But overall there seems no clear definition...</p><p>I also think it is not right or wrong answer to display as whether hexadecimal or decimal in the current situation.</p><p>Well, let's see if bug report would help to get conclusion about this question. :)</p></div><div id="comment-24365-info" class="comment-info"><span class="comment-age">(04 Sep '13, 17:33)</span> Kaz</div></div><span id="24392"></span><div id="comment-24392" class="comment"><div id="post-24392-score" class="comment-score"></div><div class="comment-text"><p>Since it's an octet string, I think the right thing to do is to display it in hexadecimal. I committed a change in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=51789">r51789</a> to do that and scheduled the change to the <a href="http://wiki.wireshark.org/Development/Roadmap">roadmap</a> for 1.10.2 and 1.8.10<a href="http://wiki.wireshark.org/Development/Roadmap">2</a>.</p></div><div id="comment-24392-info" class="comment-info"><span class="comment-age">(05 Sep '13, 11:59)</span> cmaynard ♦♦</div></div><span id="24599"></span><div id="comment-24599" class="comment"><div id="post-24599-score" class="comment-score"></div><div class="comment-text"><p>Sorry, for late response. Thanks a lot for help!</p></div><div id="comment-24599-info" class="comment-info"><span class="comment-age">(11 Sep '13, 23:45)</span> Kaz</div></div><span id="37564"></span><div id="comment-37564" class="comment not_top_scorer"><div id="post-37564-score" class="comment-score"></div><div class="comment-text"><p>Hi, Have been a wireshark + GTP user for quite some time now. Just realized that teid displayed value is in decimal for gtpv2.teid however hex for gtpv2.f_teid_gre_key.</p><p>This is again inconvenient while trying to analyse /observe GTP flows. Can we please make the gtpv2.teid as HEX.</p><p>5345 { &amp;hf_gtpv2_t, 5346 {"TEID flag (T)", "gtpv2.t", 5347 FT_UINT8, BASE_DEC, NULL, 0x08, 5348 "If TEID field is present or not", HFILL} 5349 }, 5350 { &amp;hf_gtpv2_message_type,</p></div><div id="comment-37564-info" class="comment-info"><span class="comment-age">(03 Nov '14, 22:32)</span> PKR</div></div><span id="37568"></span><div id="comment-37568" class="comment not_top_scorer"><div id="post-37568-score" class="comment-score"></div><div class="comment-text"><p>Wireshark development releases already dump the gtpv2.teid as HEX and DEC. You just need to upgrade to a nightly build as found here: <a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p></div><div id="comment-37568-info" class="comment-info"><span class="comment-age">(04 Nov '14, 05:46)</span> Pascal Quantin</div></div><span id="46390"></span><div id="comment-46390" class="comment not_top_scorer"><div id="post-46390-score" class="comment-score"></div><div class="comment-text"><p>Hi, Was this issue ever solved? I have WS 1.12.7 and still see GTPv2 pkts TEID and SQN in decimal but not Hexa.</p><p>Thanks a lot</p><p>Br, Bulphi</p></div><div id="comment-46390-info" class="comment-info"><span class="comment-age">(07 Oct '15, 06:33)</span> 109</div></div><span id="46392"></span><div id="comment-46392" class="comment not_top_scorer"><div id="post-46392-score" class="comment-score"></div><div class="comment-text"><p>This change is part of the upcoming Wireshark 2.0. In the meantime you can already download the 1.99.9 development preview from Wireshark download page.</p></div><div id="comment-46392-info" class="comment-info"><span class="comment-age">(07 Oct '15, 07:01)</span> Pascal Quantin</div></div><span id="46394"></span><div id="comment-46394" class="comment not_top_scorer"><div id="post-46394-score" class="comment-score"></div><div class="comment-text"><p>From the comment of @cmaynard from Sept 5, 2013(!) I would expect it to be in the 1.12 branch already. And backported to 1.10. and 1.8 as per comment on r51789. Did this make it into the git repo?</p></div><div id="comment-46394-info" class="comment-info"><span class="comment-age">(07 Oct '15, 07:32)</span> Jaap ♦</div></div><span id="46402"></span><div id="comment-46402" class="comment not_top_scorer"><div id="post-46402-score" class="comment-score"></div><div class="comment-text"><p>This was done for the gtpv2.f_teid_gre_key field, not for the gtpv2.teid field. This one is changed in 2.0 branch.</p></div><div id="comment-46402-info" class="comment-info"><span class="comment-age">(07 Oct '15, 08:57)</span> Pascal Quantin</div></div></div><div id="comment-tools-24229" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-24229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

