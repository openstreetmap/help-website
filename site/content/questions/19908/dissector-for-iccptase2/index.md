+++
type = "question"
title = "Dissector for ICCP/TASE.2"
description = '''I&#x27;m looking for a way to read ICCP/TASE.2 packets. I&#x27;ve seen anecdotal evidence that Wireshark supports this protocol, but can&#x27;t find anything concrete from Wireshark&#x27;s documentation or Q&amp;amp;A.  When I view pcaps with ICCP packets through Wireshark, they&#x27;re displayed down to the MMS protocol, which...'''
date = "2013-03-28T11:30:00Z"
lastmod = "2013-04-15T10:16:00Z"
weight = 19908
keywords = [ "protocol", "dissector", "tase.2", "iccp" ]
aliases = [ "/questions/19908" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector for ICCP/TASE.2](/questions/19908/dissector-for-iccptase2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19908-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for a way to read ICCP/TASE.2 packets. I've seen anecdotal evidence that Wireshark supports this protocol, but can't find anything concrete from Wireshark's documentation or Q&amp;A.</p><p>When I view pcaps with ICCP packets through Wireshark, they're displayed down to the MMS protocol, which is shown full of various errors (primarily "BER Error: Wrong field in SEQUENCE"). We've tried Wireshark versions up to 1.8.3, but the release notes for later versions don't indicate the addition of ICCP/TASE.2 support.</p><p>We are investigating the possibility of writing a custom ICCP dissector, but this has a number of problems, primarily that we don't have a C++ programmer or anyone with experience dissecting protocols.</p><p><strong>Is there an ICCP/TASE.2 dissector, either built-in or as a plugin, available for Wireshark? If not, what other tools are available to read ICCP/TASE.2 packets?</strong></p></div><div id="question-tags" class="tags-container tags">protocol dissector tase.2 iccp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '13, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/f86b2ae7e8b2f4351ff2d64ee077e0f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alisha&#39;s gravatar image" /><p>alisha<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alisha has no accepted answers">0%</span></p></div></div><div id="comments-container-19908" class="comments-container"></div><div id="comment-tools-19908" class="comment-tools"></div><div class="clear"></div><div id="comment-19908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20427"></span>

<div id="answer-container-20427" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20427-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For what I have seen myself from the TASE.2 specification, TASE.2 is just a way to use MMS. There's a mapping to the MMS data model and no extra layer is added (from a networking point of view).</p><p>MF</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 10:16</strong></p><img src="https://secure.gravatar.com/avatar/12bc430f55a4862ae9556a694858bd28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="splinux&#39;s gravatar image" /><p>splinux<br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="splinux has one accepted answer">100%</span></p></div></div><div id="comments-container-20427" class="comments-container"><span id="20428"></span><div id="comment-20428" class="comment"><div id="post-20428-score" class="comment-score"></div><div class="comment-text"><p>@splinux It's not that simple, unfortunately. TASE.2 packets show up as malformed MMS packets when we try to view them (usually the BER error I mentioned in the question). So whatever TASE.2 is doing, Wireshark can't dissect it correctly, and we can't see the contents of the packet.</p></div><div id="comment-20428-info" class="comment-info"><span class="comment-age">(15 Apr '13, 10:21)</span> alisha</div></div><span id="20438"></span><div id="comment-20438" class="comment"><div id="post-20438-score" class="comment-score"></div><div class="comment-text"><p>Then there might be a bug in the MMS dissector, or the ASN.1 specification it implements might not include all the stuff used by TASE.2. Please file a bug on this at <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, and include, if possible, a sample packet capture that demonstrates the problem.</p></div><div id="comment-20438-info" class="comment-info"><span class="comment-age">(15 Apr '13, 15:11)</span> Guy Harris ♦♦</div></div><span id="20455"></span><div id="comment-20455" class="comment"><div id="post-20455-score" class="comment-score"></div><div class="comment-text"><p>@alisha can you upload your traces somewhere like pcapr(DOT)net/home beside Bugzilla?</p></div><div id="comment-20455-info" class="comment-info"><span class="comment-age">(16 Apr '13, 01:41)</span> splinux</div></div><span id="20468"></span><div id="comment-20468" class="comment"><div id="post-20468-score" class="comment-score"></div><div class="comment-text"><p>@splinux I'll find out, but I know we're very restricted on where and how we can share our pcaps, so it might not be possible. I'm going to see if I can scrub the IP addresses &amp; other identifying data, and maybe upload then.</p></div><div id="comment-20468-info" class="comment-info"><span class="comment-age">(16 Apr '13, 08:19)</span> alisha</div></div><span id="21381"></span><div id="comment-21381" class="comment"><div id="post-21381-score" class="comment-score"></div><div class="comment-text"><p>Marking this as the answer since it's the closest we can get without being able to upload our data files. I'll file a bug report as suggested and see where it goes.</p></div><div id="comment-21381-info" class="comment-info"><span class="comment-age">(22 May '13, 15:22)</span> alisha</div></div></div><div id="comment-tools-20427" class="comment-tools"></div><div class="clear"></div><div id="comment-20427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

