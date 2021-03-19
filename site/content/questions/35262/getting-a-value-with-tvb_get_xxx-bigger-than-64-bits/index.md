+++
type = "question"
title = "Getting a value (with tvb_get_XXX) bigger than 64 bits"
description = '''Hi, I want to get a value but i don&#x27;t know its size till i dissect the previous field. I &#x27;m thinking of using tvb_get_ntoh_64(), but what if value&#x27;s size is bigger than 64 bits? Also i want to ask how to get a value of an IPv6? i don&#x27;t want to use tvb_get_ip6 (it is void anyway). Any ideas???'''
date = "2014-08-06T05:02:00Z"
lastmod = "2014-08-07T04:35:00Z"
weight = 35262
keywords = [ "tvb_get" ]
aliases = [ "/questions/35262" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Getting a value (with tvb\_get\_XXX) bigger than 64 bits](/questions/35262/getting-a-value-with-tvb_get_xxx-bigger-than-64-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35262-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I want to get a value but i don't know its size till i dissect the previous field. I 'm thinking of using tvb_get_ntoh_64(), but what if value's size is bigger than 64 bits? Also i want to ask how to get a value of an IPv6? i don't want to use tvb_get_ip6 (it is void anyway). Any ideas???</p></div><div id="question-tags" class="tags-container tags">tvb_get</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '14, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/8ee003c9042bb54a75a39046704e8d5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miltos%20Patsiouras&#39;s gravatar image" /><p>Miltos Patsi...<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miltos Patsiouras has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '14, 06:13</p></div></div><div id="comments-container-35262" class="comments-container"><span id="35282"></span><div id="comment-35282" class="comment"><div id="post-35282-score" class="comment-score"></div><div class="comment-text"><p>What type of value do you want to get? Integral? Floating-point? Character string? Raw bytes with no interpretation? Something else?</p></div><div id="comment-35282-info" class="comment-info"><span class="comment-age">(06 Aug '14, 21:59)</span> Guy Harris ♦♦</div></div><span id="35288"></span><div id="comment-35288" class="comment"><div id="post-35288-score" class="comment-score"></div><div class="comment-text"><p>It is an endpoint ID so i assume that it is an integer. Also can you tell me how to get a value of an IPv6? I just need to print the value in a proto_tree_add_text function and i see that for IPv4 tvb_get_ntohl is used as it returns a 32 bit unsigned integer, so what about IPv6?</p></div><div id="comment-35288-info" class="comment-info"><span class="comment-age">(07 Aug '14, 02:41)</span> Miltos Patsi...</div></div><span id="35291"></span><div id="comment-35291" class="comment"><div id="post-35291-score" class="comment-score"></div><div class="comment-text"><p>Whether it's an integer depends on the protocol. What protocol is this?</p></div><div id="comment-35291-info" class="comment-info"><span class="comment-age">(07 Aug '14, 03:57)</span> Guy Harris ♦♦</div></div><span id="35292"></span><div id="comment-35292" class="comment"><div id="post-35292-score" class="comment-score"></div><div class="comment-text"><p>The protocol is rsvp and i'm trying to add a new object(call atributes object) which contains the endpoint ID in a tlv.</p></div><div id="comment-35292-info" class="comment-info"><span class="comment-age">(07 Aug '14, 04:03)</span> Miltos Patsi...</div></div></div><div id="comment-tools-35262" class="comment-tools"></div><div class="clear"></div><div id="comment-35262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="35273"></span>

<div id="answer-container-35273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35273-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want a raw buffer containing whatever size you want, you can use tvb_memdup(). But then you will need to know how to interpret its content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '14, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-35273" class="comments-container"></div><div id="comment-tools-35273" class="comment-tools"></div><div class="clear"></div><div id="comment-35273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35289"></span>

<div id="answer-container-35289" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35289-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To answer your supplementary question:</p><blockquote>Also can you tell me how to get a value of an IPv6? I just need to print the value in a proto_tree_add_text function and i see that for IPv4 tvb_get_ntohl is used as it returns a 32 bit unsigned integer, so what about IPv6?</blockquote><p>Generally you should be using <code>proto_tree_add_item()</code> calls rather than getting the data yourself and adding it to the tree with <code>proto_tree_add_text()</code>, this then gives you filterable fields as well. See README.dissector for more info.</p><p>If you must get the values for purposes other than displaying in the tree then use <code>tvb_get_ipv4()</code> and <code>tvb_get_ipv6()</code>, again all detailed in README.dissector, read the note concerning ipv4. There are also ip address to string functions, <code>tvb_ip_to_str()</code> and <code>tvb_ip6_to_str()</code>, again all detailed in README.dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '14, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35289" class="comments-container"></div><div id="comment-tools-35289" class="comment-tools"></div><div class="clear"></div><div id="comment-35289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35293"></span>

<div id="answer-container-35293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35293-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So if the TLV containing the endpoint ID is the one described in <a href="http://tools.ietf.org/html/rfc6004#section-2.1">RFC 6004 section 2.1</a>, the endpoint ID is "defined in [G.8011] and [MEF10.1]".</p><p>The second of those references is Metro Ethernet Forum Technical Specification 10.1, which has been superseded by 10.1.1, which has been suspended by <a href="http://www.metroethernetforum.org/Assets/Technical_Specifications/PDF/MEF10.2.pdf">10.2</a>. It also doesn't define anything it calls an "endpoint ID", but it does define an "Ethernet Virtual Connection ID" or "EVC ID" in section 6.2 "EVC ID Service Attribute". That section says</p><blockquote><p>The EVC ID is an arbitrary string administered by the Service Provider that is used to identify an EVC within the MEN. The EVC ID <strong>MUST</strong> be unique across all EVCs in the MEN. It is intended for management and control purposes. The EVC ID is not carried in any field in the Service Frame. As an example, the AcmethService Provider might use “EVC-0001898-ACME- MEGAMART” to represent the 1898th EVC in the MEN and the customer for the EVC is MegaMart.</p></blockquote><p>so if that's the "endpoint ID", it's an "arbitrary string", not a number. I infer from section 8.3 "Service Attribute Parameters" that "string" would mean "character string".</p><p>The first of those references is <a href="http://www.itu.int/rec/T-REC-G.8011-201210-I">ITU-T Recommendation G.8011/Y.1307</a>, and doesn't seem to define anything it calls an "endpoint ID". However, section 7.1 "Ethernet virtual connection (EVC)" of that document says:</p><blockquote><p>This clause describes Ethernet virtual connection (EVC) attributes that characterize a particular instance of an Ethernet service. The area of applicability of these EVC attributes is identified in Figure 6-1 as being equivalent to the ETH connection or ETH connectivity (per clause 6.6 of [ITU-T G.8010]). The base set of ITU-T G.8011 EVC attributes is the same as the Ethernet virtual connection (EVC) attributes defined in Table 13 of [MEF 10.2] and they are summarized in Table 7-1.</p></blockquote><p>so it sounds as if an "endpoint ID" might be an "EVC ID", in which case it would be a string, not a number.</p><p>And, in fact, RFC 6004 section 2.1 says</p><blockquote><p>Specifically, the Ethernet endpoint identifiers are character based as opposed to the GMPLS norm of being IP address based.</p></blockquote><p>So it's not a number, it's a string, and you'd get it with <code>tvb_get_string_enc()</code>; I don't know what the right encoding would be for the string, but you might want to start with ENC_ASCII. Or, if you just want that value to be displayed in the dissection and be filterable, just add it with <code>proto_tree_add_item()</code>, as per grahamb's reply to your other question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '14, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35293" class="comments-container"></div><div id="comment-tools-35293" class="comment-tools"></div><div class="clear"></div><div id="comment-35293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

