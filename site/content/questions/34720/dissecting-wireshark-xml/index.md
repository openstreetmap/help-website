+++
type = "question"
title = "dissecting wireshark xml"
description = '''Hello I need to dissect xml through wireshark if any approaches how to dissect the contents in xml through wireshark can any body help me please with sample of code and references ...'''
date = "2014-07-17T02:51:00Z"
lastmod = "2014-07-18T05:51:00Z"
weight = 34720
keywords = [ "xml", "dissection", "wireshark" ]
aliases = [ "/questions/34720" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dissecting wireshark xml](/questions/34720/dissecting-wireshark-xml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34720-score" class="post-score" title="current number of votes">0</div><span id="post-34720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I need to dissect xml through wireshark if any approaches how to dissect the contents in xml through wireshark can any body help me please with sample of code and references ...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '14, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/7596daf4fb3556a397822344b20e2362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagar&#39;s gravatar image" /><p><span>sagar</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagar has no accepted answers">0%</span></p></div></div><div id="comments-container-34720" class="comments-container"><span id="34733"></span><div id="comment-34733" class="comment"><div id="post-34733-score" class="comment-score"></div><div class="comment-text"><p>Do I understand you correctly that you want to <em>dissect</em> XML data using Wireshark? I think shoehorning an XML parser into the Wireshark dissection engine would be a much bigger effort and development headache than it's worth in that case. Why is an actual XML parser not suitable for your application? On the other hand, if you intend to analyze XML data <em>within another protocol</em>, that might be different. Can you clarify your intent?</p></div><div id="comment-34733-info" class="comment-info"><span class="comment-age">(17 Jul '14, 11:24)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-34720" class="comment-tools"></div><div class="clear"></div><div id="comment-34720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34732"></span>

<div id="answer-container-34732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34732-score" class="post-score" title="current number of votes">0</div><span id="post-34732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the xml is transfered via a protocol using mime type such as HTTP in "Application=" you may only have to add the mime type to the list in packet-xml.c. If you have a tvb with xml data you can let the xml dissector dissectit by callng it with the tvb. packet-diameter_3gpp.c calls the xml dissector I think.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '14, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-34732" class="comments-container"><span id="34740"></span><div id="comment-34740" class="comment"><div id="post-34740-score" class="comment-score"></div><div class="comment-text"><p>Hello this my sample xml,</p><p>-&lt;message_library build_id="1.0" generated_datetime="2010-11-10T17:58IST" source_view="gstarhsc_rajat"&gt;</p><p>-&lt;pos_notify_ind id="100" type="bitStruct"&gt;</p><p>&lt;critical_escape type="bit" bitlen="1"&gt;0&lt;/critical_escape&gt;</p><p>&lt;msg_type type="bit" bitlen="2"&gt;1&lt;/msg_type&gt;</p><p>&lt;identifier type="bit" bitlen="1"&gt;1&lt;/identifier&gt;</p><p>&lt;random_ref type="bit" bitlen="20"&gt;0&lt;/random_ref&gt;</p><p>&lt;pos_accepted type="bit" bitlen="2"&gt;0&lt;/pos_accepted&gt;</p><p>&lt;plmn_present_flag type="bit" bitlen="1"&gt;1&lt;/plmn_present_flag&gt;</p><p>-&lt;plmn_info type="struct" type_name="plmn_info_s"&gt;</p><p>&lt;mcc1 type="bit" bitlen="4"&gt;8&lt;/mcc1&gt;</p><p>&lt;mcc2 type="bit" bitlen="4"&gt;7&lt;/mcc2&gt;</p><p>&lt;mcc3 type="bit" bitlen="4"&gt;6&lt;/mcc3&gt;</p><p>&lt;mnc1 type="bit" bitlen="4"&gt;5&lt;/mnc1&gt;</p><p>&lt;mnc2 type="bit" bitlen="4"&gt;4&lt;/mnc2&gt;</p><p>&lt;mnc3_flag type="bit" bitlen="1"&gt;0&lt;/mnc3_flag&gt;</p><p>&lt;/plmn_info&gt;</p><p>&lt;common_nas_info_present type="bit" bitlen="1"&gt;1&lt;/common_nas_info_present&gt;</p><p>-&lt;common_nas_info type="struct" type_name="common_nas_info_s"&gt;</p><p>&lt;nas_sys_info_count type="bit" bitlen="3"&gt;0&lt;/nas_sys_info_count&gt;</p><p>&lt;nas_sys_info type="bit" bitlen="8"&gt;0&lt;/nas_sys_info&gt;</p><p>&lt;/common_nas_info&gt;</p><p>&lt;domain_nas_info_present type="bit" bitlen="1"&gt;1&lt;/domain_nas_info_present&gt;</p><p>-&lt;domain_nas_info type="struct" type_name="domain_nas_info_s"&gt;</p><p>&lt;nas_sys_info_count type="bit" bitlen="3"&gt;0&lt;/nas_sys_info_count&gt;</p><p>&lt;nas_sys_info type="bit" bitlen="8"&gt;0&lt;/nas_sys_info&gt;</p><p>&lt;/domain_nas_info&gt;</p><p>&lt;ura_id type="bit" bitlen="16"&gt;0&lt;/ura_id&gt;</p><p>&lt;pos_updt_ind_present type="bit" bitlen="1"&gt;0&lt;/pos_updt_ind_present&gt;</p><p>&lt;rrc_conn_state type="bit" bitlen="2"&gt;0&lt;/rrc_conn_state&gt;</p><p>&lt;/pos_notify_ind&gt;</p><p>&lt;/message_library&gt;</p><p>I want to dissect the fields in this xml can any body help me..</p></div><div id="comment-34740-info" class="comment-info"><span class="comment-age">(17 Jul '14, 22:58)</span> <span class="comment-user userinfo">sagar</span></div></div><span id="34741"></span><div id="comment-34741" class="comment"><div id="post-34741-score" class="comment-score"></div><div class="comment-text"><p>Get an XML viewer application and read the file. Wireshark's XML dissector won't do much more than show you the individual XML elements, as you've already done.</p></div><div id="comment-34741-info" class="comment-info"><span class="comment-age">(17 Jul '14, 23:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34742"></span><div id="comment-34742" class="comment"><div id="post-34742-score" class="comment-score"></div><div class="comment-text"><p>Not sure to understand what you expect here. Your XML description already contains the field name, the length and the raw value. You can hardly get more. If you want an interpretation of the raw fields, Wireshark cannot help you. Those fields look like some RRC 3G info but you would need the raw data (byte stream) and the corresponding protocol dissector in Wireshark, not a pre-decoded XML data.</p></div><div id="comment-34742-info" class="comment-info"><span class="comment-age">(17 Jul '14, 23:38)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="34748"></span><div id="comment-34748" class="comment"><div id="post-34748-score" class="comment-score"></div><div class="comment-text"><p>my current requirement I need to write a code for dissecting the xml data if any approach briefly explain me and provide any screen shots or any links for how to write a code for dissecting the xml..</p></div><div id="comment-34748-info" class="comment-info"><span class="comment-age">(18 Jul '14, 02:45)</span> <span class="comment-user userinfo">sagar</span></div></div><span id="34753"></span><div id="comment-34753" class="comment"><div id="post-34753-score" class="comment-score"></div><div class="comment-text"><p>I'm really sorry but I have no idea of what you mean: what does dissecting xml means for you? If it is just to display the xml data in a tree view, use an XML viewer as Guy suggested.</p></div><div id="comment-34753-info" class="comment-info"><span class="comment-age">(18 Jul '14, 05:51)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-34732" class="comment-tools"></div><div class="clear"></div><div id="comment-34732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

