+++
type = "question"
title = "ISDN (LAPD) Trace"
description = '''In an ISDN trace the hex value is different in the summary and within the hex dump The control field shows 0xEA01, the hex value in the storage dump showa 01ea Why? Wolfgang Schulte woschul at t-online.de'''
date = "2016-09-24T02:30:00Z"
lastmod = "2016-09-24T02:30:00Z"
weight = 55781
keywords = [ "lapd", "isdn" ]
aliases = [ "/questions/55781" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ISDN (LAPD) Trace](/questions/55781/isdn-lapd-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55781-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In an ISDN trace the hex value is different in the summary and within the hex dump The control field shows 0xEA01, the hex value in the storage dump showa 01ea</p><p>Why?</p><p>Wolfgang Schulte woschul at t-online.de</p></div><div id="question-tags" class="tags-container tags">lapd isdn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '16, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/5ac2dd2eb7881d91b22d4e7ec4c0482d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schulte&#39;s gravatar image" /><p>schulte<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schulte has no accepted answers">0%</span></p></div></div><div id="comments-container-55781" class="comments-container"><span id="55790"></span><div id="comment-55790" class="comment"><div id="post-55790-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid the only person who can really answer the question is the author of the dissector.</p><p>None of the subfields of the control field is split between the octets, so there is no objective reason why one of the octets should be deemed "LSB" and the other one "MSB". Nor anything in Q.921 implies a particular LSB/MSB role of the octets within the field.</p><p>So my speculation is that because in some cases the control field has two octets and in other cases only one, it seemed logical to treat the 4th octet of the frame, which is, depending on the case, either the first one of the two or the only one to be transmitted, as a LSB when displaying the control field as a whole. Because normally you suppress the leading zeroes when printing an integer, not the trailing ones. But doing so causes the endianness of the control field in the dissector to be reverted as compared to the address field.</p><p>Does it cause you any practical issue? You can always <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">file a bug at Wireshark bugzilla</a>, and the presence or absence of a practical issue would determine its severity.</p></div><div id="comment-55790-info" class="comment-info"><span class="comment-age">(24 Sep '16, 04:05)</span> sindy</div></div></div><div id="comment-tools-55781" class="comment-tools"></div><div class="clear"></div><div id="comment-55781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

