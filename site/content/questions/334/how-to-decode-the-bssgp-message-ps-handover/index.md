+++
type = "question"
title = "how to decode the BSSGP message PS-Handover"
description = '''Hi, the BSSGP messages related to PS-Handover are displayed as unknown pdu type, such as PS-HANDOVER-REQUIRED (0x59), PS-HANDOVER-REQUIRED-ACK(0x5a) etc. how to set to decode them?  Thanks.'''
date = "2010-09-27T00:52:00Z"
lastmod = "2011-03-14T23:06:00Z"
weight = 334
keywords = [ "bssgp", "ps-handover" ]
aliases = [ "/questions/334" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to decode the BSSGP message PS-Handover](/questions/334/how-to-decode-the-bssgp-message-ps-handover)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-334-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, the BSSGP messages related to PS-Handover are displayed as unknown pdu type, such as PS-HANDOVER-REQUIRED (0x59), PS-HANDOVER-REQUIRED-ACK(0x5a) etc. how to set to decode them? Thanks.</p></div><div id="question-tags" class="tags-container tags">bssgp ps-handover</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '10, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/c349400ef8f34293fba92ce86a62fa90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hill%20Hou&#39;s gravatar image" /><p>Hill Hou<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hill Hou has no accepted answers">0%</span></p></div></div><div id="comments-container-334" class="comments-container"></div><div id="comment-tools-334" class="comment-tools"></div><div class="clear"></div><div id="comment-334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="341"></span>

<div id="answer-container-341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-341-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, It looks like decoding of those PDUs are missing, you could add a feature request over at https://bugs.wireshark.org/bugzilla/ enclosing a trace(pcap) file with tose PDUs. Regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '10, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-341" class="comments-container"><span id="1913"></span><div id="comment-1913" class="comment"><div id="post-1913-score" class="comment-score"></div><div class="comment-text"><p>I'm updating the dissector, if you have some traces to share that would help the verification. If so you could add it to a bugreport in bugzilla https://bugs.wireshark.org/bugzilla/ by marking it as private only the core developers will be able to see the trace.</p></div><div id="comment-1913-info" class="comment-info"><span class="comment-age">(25 Jan '11, 00:50)</span> Anders ♦</div></div></div><div id="comment-tools-341" class="comment-tools"></div><div class="clear"></div><div id="comment-341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2816"></span>

<div id="answer-container-2816" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2816-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Dissection of those PDUs Committed revision 36195.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '11, 23:06</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-2816" class="comments-container"></div><div id="comment-tools-2816" class="comment-tools"></div><div class="clear"></div><div id="comment-2816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

