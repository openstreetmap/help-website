+++
type = "question"
title = "asn2wrs: how to handle import definitions with the same definition name? Use tags?"
description = '''Hi, I am trying to create a ASN.1 dissector using asn2wrs. To do so, I need a asn file.  The asn protocol requires IMPORTS of definitions from several other asn files.  Unfortunately the naming of some definitions is identical. Resulting in a &#x27;Duplicate type&#x27; error This problem could be circumvented...'''
date = "2012-07-11T05:13:00Z"
lastmod = "2012-07-11T05:13:00Z"
weight = 12619
keywords = [ "asn2wrs", "wireshark", "dissector", "asn1" ]
aliases = [ "/questions/12619" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [asn2wrs: how to handle import definitions with the same definition name? Use tags?](/questions/12619/asn2wrs-how-to-handle-import-definitions-with-the-same-definition-name-use-tags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12619-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to create a ASN.1 dissector using asn2wrs. To do so, I need a asn file. The asn protocol requires IMPORTS of definitions from several other asn files. Unfortunately the naming of some definitions is identical. Resulting in a 'Duplicate type' error</p><p>This problem could be circumvented using tags. eg. filename1.parameters filename2.parameters</p><p>Has anyone an idea how to deal with this? Can I rename parameters from filename1 to let's say 'parameters1' using the .cnf file? There is something like #.FIELD RENAME and #.TYPE RENAME</p><p>By the way, any additional documentation (next to <a href="http://wiki.wireshark.org/Asn2wrsAuxiliary)">http://wiki.wireshark.org/Asn2wrsAuxiliary)</a> on how to modify cnf files is welcome :-)</p></div><div id="question-tags" class="tags-container tags">asn2wrs wireshark dissector asn1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '12, 05:13</strong></p><img src="https://secure.gravatar.com/avatar/f7b86af5c2a0a5df465eb1203761ce1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michel&#39;s gravatar image" /><p>Michel<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michel has no accepted answers">0%</span></p></div></div><div id="comments-container-12619" class="comments-container"><span id="12627"></span><div id="comment-12627" class="comment"><div id="post-12627-score" class="comment-score"></div><div class="comment-text"><p>That sounds weird - using the same name for different definitions? Perhaps you need to break it up into more than one dissector? You may need to comment out duplicated IMPORTS when using multiple ASN1 files however. Is this for a standard protcol for which you will offer the dissector back to Wireshark? If so you could open up an enhancement bug report in bugzilla and get help there.</p></div><div id="comment-12627-info" class="comment-info"><span class="comment-age">(11 Jul '12, 06:04)</span> Anders ♦</div></div><span id="12656"></span><div id="comment-12656" class="comment"><div id="post-12656-score" class="comment-score"></div><div class="comment-text"><p>Weird? Its the new ETSI standard! :-) Anyway, the use of imports did not help me in the end, because when including the packet that was created by asn2wrs in the Wireshark build I end up with Undeclared Identifier errors. I fixed this by copying and paste all asn protocols into a single asn file, while renaming duplicate definitions. FYI: I need to build Wireshark because I am working on a reader and a packet encapsulation.</p></div><div id="comment-12656-info" class="comment-info"><span class="comment-age">(12 Jul '12, 05:19)</span> Michel</div></div></div><div id="comment-tools-12619" class="comment-tools"></div><div class="clear"></div><div id="comment-12619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

