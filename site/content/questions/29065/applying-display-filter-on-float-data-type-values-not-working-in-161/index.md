+++
type = "question"
title = "Applying display filter on float data type values not working in 1.6.1"
description = '''I have a pcap which contains messages having data of type float. I tried applying display filter on this field, but it is not working, not able to see the messages being filtered. Wanted to know whether Wireshark supports display filter option on float data type values. I am using Wireshark version ...'''
date = "2014-01-21T10:21:00Z"
lastmod = "2014-01-21T11:52:00Z"
weight = 29065
keywords = [ "display-filter" ]
aliases = [ "/questions/29065" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Applying display filter on float data type values not working in 1.6.1](/questions/29065/applying-display-filter-on-float-data-type-values-not-working-in-161)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29065-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap which contains messages having data of type float. I tried applying display filter on this field, but it is not working, not able to see the messages being filtered.</p><p>Wanted to know whether Wireshark supports display filter option on float data type values. I am using Wireshark version 1.6.1.</p><p>Thanks in advance. Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '14, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p>Kiran Kumar G<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '14, 12:03</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-29065" class="comments-container"><span id="29066"></span><div id="comment-29066" class="comment"><div id="post-29066-score" class="comment-score"></div><div class="comment-text"><p>Which protocol? What was the display filter you tried?</p></div><div id="comment-29066-info" class="comment-info"><span class="comment-age">(21 Jan '14, 11:14)</span> grahamb ♦</div></div></div><div id="comment-tools-29065" class="comment-tools"></div><div class="clear"></div><div id="comment-29065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29071"></span>

<div id="answer-container-29071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29071-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Wanted to know whether Wireshark supports display filter option on float data type values.</p></blockquote><p>yes, in general that's supported, at least in the versions I tested (1.10.x and 1.11.x).</p><p>I did a test with DTLS, where the sequence number was (strangely) defined as a double value up until 1.11.x</p><p>Test File: <a href="http://wiki.wireshark.org/SampleCaptures#DTLS_with_decryption_keys">http://wiki.wireshark.org/SampleCaptures#DTLS_with_decryption_keys</a></p><p>In Wireshark 1.10.x I was able to use the following filters</p><ul><li>dtls.record.sequence_number == 1.0</li><li>dtls.record.sequence_number == 1</li></ul><p>They both work.</p><p>In 1.11.x that field was redefined as UINT64, hence it does not work in 1.11.x.</p><p>Now, for 1.6.x: The field is defined as DOUBLE there as well, <strong>however</strong> filtering for a double value (1.0, see above), does <strong>not</strong> work in 1.6.8. I get an error message, but I did not check the reason for it in the code!</p><p>So, to answer you question in more details:</p><p>Yes, filtering for float/double values works, if</p><ul><li>the Wireshark release supports it (at least in 1.10.x, maybe earlier - <strong>however</strong> not in 1.6.8)</li><li>there is a float/double field for the protocol you are analyzing</li></ul><p><strong>-- UPDATE --</strong></p><p>Filters for float/double values <strong>do work</strong> for 1.6.11 and upwards, so maybe that's a bug in 1.6.x that has been fixed. Please update or upgrade your version of Wireshark and it should work (again) ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '14, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '14, 12:23</p></div></div><div id="comments-container-29071" class="comments-container"><span id="29136"></span><div id="comment-29136" class="comment"><div id="post-29136-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for your answer, it clarified many of my questions.</p><p>I did further analysis and below are my observations. I took a PCAP of a protocol which had float values, i selected CIGI protocol as it is supported by default in Wireshark. I opened this in both Wireshark 1.6.1 and Wireshark 1.10.2 and 1.10.5 (latest version) and tried applying filter on the float field. Observed that it is the same behaviour with both the versions.</p><p>I am not sure if the problem still there in the latest version or am i missing something.</p><p>HF declaration and the code to display this field in CIGI code is as below.</p><p>---HF declaration---</p><p>&amp;hf_cigi2_line_of_sight_range_request_max_range, { "Maximum Range (m)", "cigi.los_range_request.max_range", FT_FLOAT, BASE_NONE, NULL, 0x0, "Specifies the maximum extent from the source position specified in this data packet to a point along the LOS vector where intersection testing will end", HFILL } },</p><p>---Code snippet---</p><p>proto_tree_add_item(tree, hf_cigi2_line_of_sight_range_request_max_range, tvb, offset, 4, ENC_BIG_ENDIAN); offset += 4;</p><p>---Applied filter string is as below---</p><p>cigi.los_range_request.max_range</p><p>---PCAP for the CIGI protocol is obtained from the below link---</p><p><a href="http://wiki.wireshark.org/CIGI">http://wiki.wireshark.org/CIGI</a></p><p>Request you suggestion on the same.</p><p>Thanks, Kiran</p></div><div id="comment-29136-info" class="comment-info"><span class="comment-age">(24 Jan '14, 04:29)</span> Kiran Kumar G</div></div><span id="29137"></span><div id="comment-29137" class="comment"><div id="post-29137-score" class="comment-score"></div><div class="comment-text"><p>O.K. I believe this is a <strong>bug</strong> related to 'localization/internationalization' settings of the OS, where either '.' or ',' is used to separate the fraction of a number, similar to a problem reported in another question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/26084/time-shift-feature">http://ask.wireshark.org/questions/26084/time-shift-feature</a></p></blockquote><p>If I apply <code>cigi.los_range_request.max_range</code> as a filter on my system (right click the field in frame 1), Wireshark 1.10.5 creates the following filter on a german localized system.</p><blockquote><p>cigi.los_range_request.max_range == 336,921</p></blockquote><p>However, that filter is not accepted (certainly due to the comma)</p><p>If I used the following filter</p><blockquote><p>cigi.los_range_request.max_range == 336.921</p></blockquote><p>The filter itself is accepted (green), but it <strong>does not match any frame</strong>.</p><p>So, please open a bug request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and describe your problem as detailed as possible. Please also add the link to this question.</p></div><div id="comment-29137-info" class="comment-info"><span class="comment-age">(24 Jan '14, 05:31)</span> Kurt Knochner ♦</div></div><span id="29215"></span><div id="comment-29215" class="comment"><div id="post-29215-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for your reply, i will be raising a bug as suggested.</p></div><div id="comment-29215-info" class="comment-info"><span class="comment-age">(27 Jan '14, 23:19)</span> Kiran Kumar G</div></div></div><div id="comment-tools-29071" class="comment-tools"></div><div class="clear"></div><div id="comment-29071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

