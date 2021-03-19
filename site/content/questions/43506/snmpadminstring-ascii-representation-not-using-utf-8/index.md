+++
type = "question"
title = "SnmpAdminString ascii representation not using UTF-8"
description = '''We are sending a SnmpAdminString in a SNMP trap. The SNMP-FRAMEWORK mib describes SnmpAdminString as  &quot;An octet string containing administrative information, preferably in human-readable form. To facilitate internationalization, this information is represented using the ISO/IEC IS 10646-1 character ...'''
date = "2015-06-24T08:49:00Z"
lastmod = "2015-06-24T15:09:00Z"
weight = 43506
keywords = [ "snmpadminstring" ]
aliases = [ "/questions/43506" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SnmpAdminString ascii representation not using UTF-8](/questions/43506/snmpadminstring-ascii-representation-not-using-utf-8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43506-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are sending a SnmpAdminString in a SNMP trap. The SNMP-FRAMEWORK mib describes SnmpAdminString as</p><p><em>"An octet string containing administrative information, preferably in human-readable form. To facilitate internationalization, this information is represented using the ISO/IEC IS 10646-1 character set, encoded as an octet string using the UTF-8 transformation format described in [RFC2279].</em></p><p>However, the string representation for this OctetString appears to not be using the UTF-8 character set. For example sending the string 'IQTV-ö05':<br />
Receiving octets: - 495154562dc3b63035<br />
String rep: IQTV-Ã¶05<br />
<br />
In UTF-8, the character ö = 0xc3b6, but in 8-bit extended ascii 0xc3b6 is Ã¶ which is what is being displayed. Is there something that I have misconfigured?</p></div><div id="question-tags" class="tags-container tags">snmpadminstring</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '15, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/9ac0c174ead4b6b2a78d925dc913ff68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ccrotty&#39;s gravatar image" /><p>ccrotty<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ccrotty has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-43506" class="comments-container"></div><div id="comment-tools-43506" class="comment-tools"></div><div class="clear"></div><div id="comment-43506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43524"></span>

<div id="answer-container-43524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43524-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>After a lot of searching in the source code, it appears that the snmp dissector in Wireshark doesn't make any use of the DISPLAY-HINT associated with the SnmpAdminString of "255t" that indicates a UTF-8 encoded string. Currently the snmp dissector treats all OCTET STRING values as ASCII.</p><p>I <em>think</em> that libsmi (the library Wireshark uses for parsing Mibs) makes the DISPLAY-HINT available so it could be used, but I'm not certain as the docs don't really indicate much about that.</p><p>You could raise a bug\enhancement item on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> to at least track this, if you do so please add a capture with an snmp packet showing the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '15, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '15, 15:09</p></div></div><div id="comments-container-43524" class="comments-container"></div><div id="comment-tools-43524" class="comment-tools"></div><div class="clear"></div><div id="comment-43524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

