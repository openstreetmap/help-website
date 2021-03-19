+++
type = "question"
title = "Wireshark dissector support for BER OID for &quot;{itu-t(0) identified-organization(4) etsi(0) securityDomain(2)...}&quot;"
description = '''Hi, I am trying to decode ASN.1 encoded packets for BER OID for &quot;{itu-t(0) identified-organization(4) etsi(0) securityDomain(2)...}&quot; using the latest 1.8.2 but I am not able to decode it. Could someone please point if Wireshark supports this. The Dissector table list DOES NOT show up BER OID 0.4.0.2...'''
date = "2012-08-22T06:36:00Z"
lastmod = "2012-08-22T06:36:00Z"
weight = 13816
keywords = [ "lawfulintercept" ]
aliases = [ "/questions/13816" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark dissector support for BER OID for "{itu-t(0) identified-organization(4) etsi(0) securityDomain(2)...}"](/questions/13816/wireshark-dissector-support-for-ber-oid-for-itu-t0-identified-organization4-etsi0-securitydomain2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13816-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to decode ASN.1 encoded packets for BER OID for "{itu-t(0) identified-organization(4) etsi(0) securityDomain(2)...}" using the latest 1.8.2 but I am not able to decode it. Could someone please point if Wireshark supports this. The Dissector table list DOES NOT show up BER OID 0.4.0.2.x.x.x</p></div><div id="question-tags" class="tags-container tags">lawfulintercept</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '12, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/c7565e1f1798abbd82736386acf2dd60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RajanB&#39;s gravatar image" /><p>RajanB<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RajanB has no accepted answers">0%</span></p></div></div><div id="comments-container-13816" class="comments-container"><span id="13820"></span><div id="comment-13820" class="comment"><div id="post-13820-score" class="comment-score"></div><div class="comment-text"><p>I would gess not, you could raise an enhancment bug and add example traces to it.</p></div><div id="comment-13820-info" class="comment-info"><span class="comment-age">(22 Aug '12, 10:26)</span> Anders ♦</div></div><span id="13833"></span><div id="comment-13833" class="comment"><div id="post-13833-score" class="comment-score"></div><div class="comment-text"><p>I could see that the code base has the required dissector file :</p><p><a href="http://anonsvn.wireshark.org/wireshark/trunk-1.8/epan/dissectors/packet-HI2Operations.c">http://anonsvn.wireshark.org/wireshark/trunk-1.8/epan/dissectors/packet-HI2Operations.c</a></p><p>How does it translate to Dissector Table list? Could someone please help on this.</p></div><div id="comment-13833-info" class="comment-info"><span class="comment-age">(22 Aug '12, 20:40)</span> RajanB</div></div></div><div id="comment-tools-13816" class="comment-tools"></div><div class="clear"></div><div id="comment-13816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

