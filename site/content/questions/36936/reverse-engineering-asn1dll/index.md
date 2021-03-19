+++
type = "question"
title = "reverse engineering asn1.dll"
description = '''Hi  iam developing a dissector similar to already developed dissector.Earlier they have used asn1 file and compiled. they have asn1.dll in plugin folder. (i do have asn1 file withe me) But i have used my own code starting from scratch. i have almost finished 90 % and could not complete as some part ...'''
date = "2014-10-09T02:24:00Z"
lastmod = "2014-10-09T05:29:00Z"
weight = 36936
keywords = [ "engineering", "reverse", "asn1" ]
aliases = [ "/questions/36936" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [reverse engineering asn1.dll](/questions/36936/reverse-engineering-asn1dll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36936-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>iam developing a dissector similar to already developed dissector.Earlier they have used asn1 file and compiled. they have asn1.dll in plugin folder. (i do have asn1 file withe me)</p><p>But i have used my own code starting from scratch. i have almost finished 90 % and could not complete as some part is very difficult.I have 3 different layers connection, control and adaption layer.</p><p>is it possible for me to reverse engineering and get the code? please suggest.</p></div><div id="question-tags" class="tags-container tags">engineering reverse asn1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '14, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div></div><div id="comments-container-36936" class="comments-container"></div><div id="comment-tools-36936" class="comment-tools"></div><div class="clear"></div><div id="comment-36936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36937"></span>

<div id="answer-container-36937" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36937-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you aware of the <a href="http://wiki.wireshark.org/Asn2wrs">asn2wrs</a> tool that can produce a dissector from an asn1 description (along with some helper files)?</p><p>Reverse engineering the DLL might be possible, but to get back to anything like the originating C code for the dissector would be a monumental task.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '14, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36937" class="comments-container"><span id="36938"></span><div id="comment-36938" class="comment"><div id="post-36938-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb!</p><p>Thanks for the reply. I have 3 different layers each come with 100s of payload types which is in the asn1 code.</p><p>But how do i create dissector using this asn1 i have gone through some of the examples here using asn2wrs (Toyasn1 ). i have 4 asn1 files all are link to each other .</p><p>i have control layer connecion layer and adaption layer. I have heder contains the information on which payload followed by. How do i do this ? please help. Thanks</p></div><div id="comment-36938-info" class="comment-info"><span class="comment-age">(09 Oct '14, 03:37)</span> umar</div></div><span id="36939"></span><div id="comment-36939" class="comment"><div id="post-36939-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure if this is possible with ASN1 dissectors and\or plugins, but normal dissectors can work in layers such as you describe, for instance the http dissector hands off websocket data to the websocket dissector. When the http dissector registers, it looks for the websocket dissector using find_dissector("websocket"), and then calls that dissector using call_dissector() when it determines that the data is websocket type.</p></div><div id="comment-36939-info" class="comment-info"><span class="comment-age">(09 Oct '14, 03:47)</span> grahamb ♦</div></div><span id="36940"></span><div id="comment-36940" class="comment"><div id="post-36940-score" class="comment-score"></div><div class="comment-text"><p>ADAP_PDU DEFINITIONS AUTOMATIC TAGS ::= BEGIN</p><p>-- <strong><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em>*</strong></p><p>-- Value References</p><p>-- <strong><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em>*</strong></p><p>maxCdomain INTEGER ::= 4</p><p>maxKeySize INTEGER ::= 8192</p><p>maxPGAlgoType INTEGER ::= 8</p><p>maxRCPacketSizes INTEGER ::= 16</p><p>maxRCProfile INTEGER ::= 16</p><p>maxRB INTEGER ::= 16</p><p>-- <strong><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em>*</strong></p><p>-- Type Definitions</p><p>-- <strong><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em><em>*</em>*</strong></p><p>AdaptationLayerAVP ::= CHOICE { al-short-avp ALShortAVP, al-standard-avp ALStandardAVP }</p><p>AdaptationLayerAVPList ::= SEQUENCE { adaptation-layer-avp AdaptationLayerAVP }</p><p>AdaptationLayerAVPListLengthAVP ::= BCnAVP</p><p>AdaptationLayerAVPListLengthParam ::= INTEGER (0..255)</p><p>ALMsgSeqNumber ::= INTEGER (0..15)</p><p>ALShortAVP ::= SEQUENCE { length-control BOOLEAN, --{encode as FALSE} al-short-avp-type ALShortAVPType, al-short-avp-length INTEGER(1..8), -- encode as minimum bits from lowest bound param-value CHOICE { -- as appropriate to value of al-short-avp-type .. .. .. .. ..</p><p>} }</p></div><div id="comment-36940-info" class="comment-info"><span class="comment-age">(09 Oct '14, 03:54)</span> umar</div></div><span id="36941"></span><div id="comment-36941" class="comment"><div id="post-36941-score" class="comment-score">1</div><div class="comment-text"><p>I've had a quick look at the asn1 dissectors in Wireshark and there are quite a few of them that use call_dissector to hand off data to another dissector, e.g. tcap calls ansi_tcap. Have a look there to see how it is handled and adapt it to your situation.</p></div><div id="comment-36941-info" class="comment-info"><span class="comment-age">(09 Oct '14, 04:10)</span> grahamb ♦</div></div></div><div id="comment-tools-36937" class="comment-tools"></div><div class="clear"></div><div id="comment-36937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36942"></span>

<div id="answer-container-36942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36942-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>iam developing a dissector similar to already developed dissector.Earlier they have used asn1 file and &gt; compiled. they have asn1.dll in plugin folder. (i do have asn1 file withe me)</p><p>is it possible for me to reverse engineering and get the code? please suggest</p></blockquote><p>A comment:</p><p>If you have a Wireshark "asn1.dll" that suggests that the creator of same has made it publicly available in some manner.</p><p>If so, since Wireshark is GPLv2 licensed, the creator of the plugin is obliged to provide the plugin source upon request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '14, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-36942" class="comments-container"></div><div id="comment-tools-36942" class="comment-tools"></div><div class="clear"></div><div id="comment-36942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

