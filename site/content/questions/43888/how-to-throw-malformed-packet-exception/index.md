+++
type = "question"
title = "How to Throw Malformed Packet Exception"
description = '''Hello, I&#x27;m writing a dissector right now, and I want it to verify that incoming packets are the right length. Is there a way I can throw a malformed packet exception once I find out that the packet isn&#x27;t the right size? I already have code that checks if the size is correct, I just don&#x27;t know how to...'''
date = "2015-07-06T06:37:00Z"
lastmod = "2015-07-06T08:37:00Z"
weight = 43888
keywords = [ "dissector", "malformedpacket", "malformed", "wireshark" ]
aliases = [ "/questions/43888" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to Throw Malformed Packet Exception](/questions/43888/how-to-throw-malformed-packet-exception)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43888-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm writing a dissector right now, and I want it to verify that incoming packets are the right length. Is there a way I can throw a malformed packet exception once I find out that the packet isn't the right size? I already have code that checks if the size is correct, I just don't know how to throw the exception, and Google has only brought me to people with questions about why their packets are being marked as malformed.</p><p>I was looking at the THROW() function but there was nothing for malformed packet exceptions. Any advice?</p></div><div id="question-tags" class="tags-container tags">dissector malformedpacket malformed wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '15, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/059a334676449782e9d927f2f79351fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="broccollirob&#39;s gravatar image" /><p>broccollirob<br />
<span class="score" title="75 reputation points">75</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="broccollirob has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jul '15, 06:38</p></div></div><div id="comments-container-43888" class="comments-container"></div><div id="comment-tools-43888" class="comment-tools"></div><div class="clear"></div><div id="comment-43888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43891"></span>

<div id="answer-container-43891" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43891-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you encounter a situation which cannot be handled by the dissector, you could use the <code>DISSECTOR_ASSERT</code> family of macros which are defined in <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/proto.h"><code>epan/proto.h</code></a>:</p><pre><code>DISSECTOR_ASSERT(size &gt;= 4);</code></pre><p>Most of the time however you want to dissect as much as possible and let the <code>proto_tree_*</code> functions (such as <code>proto_tree_add_item</code>) throw exceptions if the bounds are violated. This reduces clutter in your code.</p><p>If you can fully dissect a packet, but would like to notify the user of protocol violations, then it is recommended to use Expert Info. See <a href="https://wiki.wireshark.org/Development/ExpertInfo">https://wiki.wireshark.org/Development/ExpertInfo</a> for more information and the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/packet-PROTOABBREV.c">doc/packet-PROTOABBREV.c</a> file for an example.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-43891" class="comments-container"></div><div id="comment-tools-43891" class="comment-tools"></div><div class="clear"></div><div id="comment-43891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

