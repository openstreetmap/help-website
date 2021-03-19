+++
type = "question"
title = "how to add custom protocol dissector for layer 1 (ethernet) protcol"
description = '''Hi, I uses a custom protocol format to save packets, the full ethernet frame(eth-&amp;gt;ip-&amp;gt;tcp..) is prepended by my custom protocol header, I want to add plugin in wireshark that displays My custom header and its subfields &amp;amp; then the actual protcol hierarchy like in order  MyProtcolName -subhe...'''
date = "2013-04-03T06:38:00Z"
lastmod = "2013-04-03T07:15:00Z"
weight = 20052
keywords = [ "layer1", "dissector", "protocol", "custom" ]
aliases = [ "/questions/20052" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to add custom protocol dissector for layer 1 (ethernet) protcol](/questions/20052/how-to-add-custom-protocol-dissector-for-layer-1-ethernet-protcol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20052-score" class="post-score" title="current number of votes">0</div><span id="post-20052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I uses a custom protocol format to save packets, the full ethernet frame(eth-&gt;ip-&gt;tcp..) is prepended by my custom protocol header,</p><p>I want to add plugin in wireshark that displays My custom header and its subfields &amp; then the actual protcol hierarchy like in order</p><p>MyProtcolName</p><p>-subheaderinfo1</p><p>-subheaderinfo2</p><p>Ethernet</p><p>ip</p><p>&amp; so on,</p><p>Is it possible in wireshark to add protocol over layer1 protocols? If it is, then kindly suggest a way to implement it. A sample would be appreciable..</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-layer1" rel="tag" title="see questions tagged &#39;layer1&#39;">layer1</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/a1ba2dae9d8121c073a393c58b73938a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vipul%20Pal&#39;s gravatar image" /><p><span>Vipul Pal</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vipul Pal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Apr '13, 07:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20052" class="comments-container"></div><div id="comment-tools-20052" class="comment-tools"></div><div class="clear"></div><div id="comment-20052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20055"></span>

<div id="answer-container-20055" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20055-score" class="post-score" title="current number of votes">0</div><span id="post-20055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is possible. You will need to register for a new Link Layer header type value (see: <a href="http://www.tcpdump.org/linktypes.html)">http://www.tcpdump.org/linktypes.html)</a> or you can use one of the types reserved for private use (if you don't plan to distribute your specific capture files and dissector).</p><p>Then you will need to write a dissector that registers to the "wtap_encap" dissector list to get your dissector called based on the encapsulation type in the pcap file (which should match the requested Link Layer Header type). Your dissector will dissect your protocol headers and then will call the ethernet dissector to dissect the eth,ip,etc layers.</p><p>Have a look at <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.8/epan/dissectors/packet-juniper.c?revision=43119&amp;view=markup">epan/dissectors/packet-juniper.c</a> for an example...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '13, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20055" class="comments-container"></div><div id="comment-tools-20055" class="comment-tools"></div><div class="clear"></div><div id="comment-20055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

