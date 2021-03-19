+++
type = "question"
title = "What is the problem with reassembling in this pcap?"
description = '''I&#x27;m developing a subdissector under SSL. When I test it, I found that most of the packets are dissected properly where some of them are dissected as &quot;Ignored Unknown Record&quot;. I noticed these cases get (always) properly dissected: a single PDU embedded in a single SSL frame or multiple PDUs embedded ...'''
date = "2015-08-04T09:18:00Z"
lastmod = "2015-08-04T09:18:00Z"
weight = 44826
keywords = [ "ssl", "subdissector", "reassembling" ]
aliases = [ "/questions/44826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the problem with reassembling in this pcap?](/questions/44826/what-is-the-problem-with-reassembling-in-this-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm developing a subdissector under SSL. When I test it, I found that most of the packets are dissected properly where some of them are dissected as "Ignored Unknown Record". I noticed these cases get (always) properly dissected: a single PDU embedded in a single SSL frame or multiple PDUs embedded in a single SSL frame. However, the case where a single PDU is a crosse multiple SSL frames is not (attached screenshot)! Dissection works fine if the next involved frame is a reassembled one (looks as "Application Data" in the Info column) but fails when it is a "[TCP segment of a reassembled PDU]".</p><p>W]hen I tried to dissect the same dump without the related decryption keys, I found that the packets which appear as "[TCP segment of a reassembled PDU]" are the ones which dissected as"Ignored Unknown Record" when I use the keys.</p><p>Based on that, I can only think there is something wrong with the reassembling but I'm not sure where?</p><p>Here is my <a href="https://www.cloudshark.org/captures?_message=BAh7BjoLbm90aWNlSSIaV2VsY29tZSB0byBDbG91ZFNoYXJrBjoGRVQ%3D%0A#">relate dump</a> (no keys provided!)</p><p><strong>Part of My ssl_debug_file</strong></p><pre><code> avialble =548 
 required = 514 
 Yes we have enough bytes for #310 
 done dissecting 
 avialble =34 
 required = 514 
No enough bytes for #310 we need 480 more

dissect_ssl enter frame #312 (first time)
packet_from_server: is from server - TRUE
  conversation = 0x7fb399607058, ssl_session = 0x7fb3721867e0
  record: offset = 0, reported_length_remaining = 1368
Unknown Record because of the session version is 3 and the returned type is 206

dissect_ssl enter frame #313 (first time)
packet_from_server: is from server - TRUE
 conversation = 0x7fb399607058, ssl_session = 0x7fb3721867e0
 record: offset = 0, reported_length_remaining = 1368
 Unknown Record because of the session version is 3 and the returned type is 133</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/improper_case.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ssl subdissector reassembling</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '15, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 05 Aug '15, 05:54</p></div></div><div id="comments-container-44826" class="comments-container"></div><div id="comment-tools-44826" class="comment-tools"></div><div class="clear"></div><div id="comment-44826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

