+++
type = "question"
title = "How to get byte value of the specified field?"
description = '''Hi, Google and Wireshark forum don’t give me exact answer on my problem that’s why decided to post this question here. I have a LUA script that parse the pcap file. In packet I have a field “gsm_map.ms.requestedInfo_element”. This field is a label and does not have the value. That’s why I would like...'''
date = "2016-04-26T01:20:00Z"
lastmod = "2016-04-26T01:20:00Z"
weight = 51951
keywords = [ "lua", "pcap", "dissector", "bytes" ]
aliases = [ "/questions/51951" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get byte value of the specified field?](/questions/51951/how-to-get-byte-value-of-the-specified-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51951-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Google and Wireshark forum don’t give me exact answer on my problem that’s why decided to post this question here. I have a LUA script that parse the pcap file. In packet I have a field “gsm_map.ms.requestedInfo_element”. This field is a label and does not have the value. That’s why I would like to get the bytes from this field. Please help me to get the bytes which are connected to this field only.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">lua pcap dissector bytes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '16, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/2d7d6eacf9c502b9188b233cb3e1d8ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="domeno&#39;s gravatar image" /><p>domeno<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="domeno has no accepted answers">0%</span></p></div></div><div id="comments-container-51951" class="comments-container"><span id="51954"></span><div id="comment-51954" class="comment"><div id="post-51954-score" class="comment-score"></div><div class="comment-text"><p>What does your LUA script have to do with the GSM map dissector? I assume you have gsm_map somehow encapsulated, and this LUA scripts takes care of that.</p><p>Furthermore the field you reference is a BER encoded sequence, handled by the GSM map dissector, see dissect_gsm_map_ms_RequestedInfo()</p></div><div id="comment-51954-info" class="comment-info"><span class="comment-age">(26 Apr '16, 03:53)</span> Jaap ♦</div></div><span id="51957"></span><div id="comment-51957" class="comment"><div id="post-51957-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/4/jaap">https://ask.wireshark.org/users/4/jaap</a></p><p>I use following: --we're intercepting SSN range 6-9 for GSM MAPlocal sccp_tbl = DissectorTable.get("sccp.ssn") -- get the TCAP dissector tcap_dissector = sccp_tbl:get_dissector(6) -- replace it with our proxy dissector, for the 6-9 range sccp_tbl:set("6-9", proxy)</p><p>"proxy" is my own proto with some fields which then i write to the file. Now I want to write to the file the all bytes of the field "gsm_map.ms.requestedInfo_element". I thought that LUA has a function that could show the bytes of the specified name of the field or may be position and length of bytes in the buf for specified field.</p></div><div id="comment-51957-info" class="comment-info"><span class="comment-age">(26 Apr '16, 04:23)</span> domeno</div></div></div><div id="comment-tools-51951" class="comment-tools"></div><div class="clear"></div><div id="comment-51951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

