+++
type = "question"
title = "How does wireshark dissect a PDCP-LTE header?"
description = '''How does wireshark dissect a PDCP-LTE header? I mean what should be the initial bytes in a raw packet data for it be identified as a PDCP-LTE packet by wireshark'''
date = "2011-09-07T04:16:00Z"
lastmod = "2011-09-07T04:16:00Z"
weight = 6174
keywords = [ "pdcp-lte" ]
aliases = [ "/questions/6174" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does wireshark dissect a PDCP-LTE header?](/questions/6174/how-does-wireshark-dissect-a-pdcp-lte-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6174-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does wireshark dissect a PDCP-LTE header? I mean what should be the initial bytes in a raw packet data for it be identified as a PDCP-LTE packet by wireshark</p></div><div id="question-tags" class="tags-container tags">pdcp-lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '11, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/17531e510285b905a76d4f993fe65975?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chaitanya%20Pratapa&#39;s gravatar image" /><p>Chaitanya Pr...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chaitanya Pratapa has no accepted answers">0%</span></p></div></div><div id="comments-container-6174" class="comments-container"><span id="6193"></span><div id="comment-6193" class="comment"><div id="post-6193-score" class="comment-score"></div><div class="comment-text"><p>Is this helpful? http://wiki.wireshark.org/PDCP-LTE</p></div><div id="comment-6193-info" class="comment-info"><span class="comment-age">(07 Sep '11, 10:09)</span> Anders ♦</div></div><span id="6194"></span><div id="comment-6194" class="comment"><div id="post-6194-score" class="comment-score"></div><div class="comment-text"><p>PDCP is not a protocol that can just be passed to the dissector, you need to give it some context (see struct pdcp_lte_info in packet-pdcp-lte.h - there is a link on the wiki page).</p><p>The available options are: - use a log file format that has this information and can be read (currently only IxCatapult .out files) - log from your PDCP application code by sending UDP frames whose headers contain the info (again see wiki page) and capture those frames in Wireshark - configure RLC to call it. Until a couple of days ago, it would only call the PDCP dissector for complete SDUs, but now basic re-assembly is supported).</p></div><div id="comment-6194-info" class="comment-info"><span class="comment-age">(07 Sep '11, 10:34)</span> MartinM</div></div></div><div id="comment-tools-6174" class="comment-tools"></div><div class="clear"></div><div id="comment-6174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

