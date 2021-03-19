+++
type = "question"
title = "Is there a more complete example about how to add a new capture type to libpcap?"
description = '''In the Wireshark Developer&#x27;s Guide, section 8 (http://www.wireshark.org/docs/wsdg_html/#ChCaptureAddLibpcap) briefly describes &quot;How to add a new capture type to libpcap&quot;. I am developing a dissector for a unique protocol whose traffic has been captured into a pcap file. Is there a more complete exam...'''
date = "2013-12-20T10:12:00Z"
lastmod = "2014-01-02T09:33:00Z"
weight = 28308
keywords = [ "dlt_user", "dissector", "libpcap" ]
aliases = [ "/questions/28308" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a more complete example about how to add a new capture type to libpcap?](/questions/28308/is-there-a-more-complete-example-about-how-to-add-a-new-capture-type-to-libpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28308-score" class="post-score" title="current number of votes">0</div><span id="post-28308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the Wireshark Developer's Guide, section 8 (<a href="http://www.wireshark.org/docs/wsdg_html/#ChCaptureAddLibpcap)">http://www.wireshark.org/docs/wsdg_html/#ChCaptureAddLibpcap)</a> briefly describes "How to add a new capture type to libpcap". I am developing a dissector for a unique protocol whose traffic has been captured into a pcap file. Is there a more complete example on how to determine a DLT_ value (DLT_user?), modify the wtap.h and .c files, and call the dissector_add_uint function appropriately?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dlt_user" rel="tag" title="see questions tagged &#39;dlt_user&#39;">dlt_user</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '13, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/5616ea3bb0508befa40fd66a768acc65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tinker&#39;s gravatar image" /><p><span>Tinker</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tinker has one accepted answer">100%</span></p></div></div><div id="comments-container-28308" class="comments-container"></div><div id="comment-tools-28308" class="comment-tools"></div><div class="clear"></div><div id="comment-28308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28527"></span>

<div id="answer-container-28527" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28527-score" class="post-score" title="current number of votes">0</div><span id="post-28527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tinker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you. This response led me to a solution. The dissector I am developing for a unique protocol will not be used externally so it is acceptable and easy for me to use one of the DLT_user slots.</p><p>First, I had already built the PCAP file with network data link type of DLT_USER User15 (i.e., 162) in the PCAP header.</p><p>Next, the link <a href="http://wiki.wireshark.org/HowToDissectAnything">http://wiki.wireshark.org/HowToDissectAnything</a> that is referenced in the above answer link of <a href="http://ask.wireshark.org/questions/27279/encapsulation-type-value">http://ask.wireshark.org/questions/27279/encapsulation-type-value</a> had the information I needed to complete the dissector plugin. That link describes a plugin for an http-type protocol. I needed to "overload" the handling of an existing protocol, preferably some generic type of protocol. I see that the standard Wireshark-supported protocols (Internals -&gt; Supported protocols), includes one named "collectd", which sounds about as generic as one could get. So: a) following the example in the HowToDissectAnything webpage, I enabled User15, in the DLT_USER table, to payload_prototype of "collectd"</p><p>b) using the information described in link <a href="http://ask.wireshark.org/questions/8823/error-in-column-payload-protocol-dissector-not-found,">http://ask.wireshark.org/questions/8823/error-in-column-payload-protocol-dissector-not-found,</a> I changed my plugin prototype to use register_dissector("collectd",dissect_foo,proto_foo) in function proto_register_foo in place of the invocation of proto_register_protocol as described in section 9 of <a href="http://www.wireshark.org/docs/wsdg_html_chunked,">http://www.wireshark.org/docs/wsdg_html_chunked,</a> and I deleted the invocation of dissector_add_uint as described in function proto_reg_handoff_foo of that same section 9.</p><p>Now my plugin dissects the unique protocol PCAP file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '14, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/5616ea3bb0508befa40fd66a768acc65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tinker&#39;s gravatar image" /><p><span>Tinker</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tinker has one accepted answer">100%</span></p></div></div><div id="comments-container-28527" class="comments-container"></div><div id="comment-tools-28527" class="comment-tools"></div><div class="clear"></div><div id="comment-28527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28342"></span>

<div id="answer-container-28342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28342-score" class="post-score" title="current number of votes">1</div><span id="post-28342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>If you want to add a new DLT_value look at this link : <a href="http://ask.wireshark.org/questions/27279/encapsulation-type-value">http://ask.wireshark.org/questions/27279/encapsulation-type-value</a></p><p>You can also force a file to an existing encap value by using editcap with -T option, see : <a href="http://www.wireshark.org/docs/man-pages/editcap.html">http://www.wireshark.org/docs/man-pages/editcap.html</a></p><p>Read the note of the -T option, I'm not sure that's what you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '13, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p><span>Afrim</span><br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-28342" class="comments-container"></div><div id="comment-tools-28342" class="comment-tools"></div><div class="clear"></div><div id="comment-28342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

