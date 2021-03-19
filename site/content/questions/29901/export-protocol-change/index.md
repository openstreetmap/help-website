+++
type = "question"
title = "Export protocol change"
description = '''Hi guys, Strange one; I&#x27;ve captured a couple of packets from a windows 7 (embedded) machine, using wireshark for windows. Made an export to analyze the data on my mac, but it strangely &#x27;converts&#x27; a couple of HTTP packets to TCP and make the /GET unreadable. Is there an explanation for this, or this ...'''
date = "2014-02-16T01:01:00Z"
lastmod = "2014-02-16T08:48:00Z"
weight = 29901
keywords = [ "http", "export", "tcp" ]
aliases = [ "/questions/29901" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Export protocol change](/questions/29901/export-protocol-change)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29901-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>Strange one; I've captured a couple of packets from a windows 7 (embedded) machine, using wireshark for windows. Made an export to analyze the data on my mac, but it strangely 'converts' a couple of HTTP packets to TCP and make the /GET unreadable.</p><p>Is there an explanation for this, or this is this some sort of bug? (googled and searched here, but couldn't find related articles.)</p><p>Thanks in advance.</p><p>Regards!</p></div><div id="question-tags" class="tags-container tags">http export tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '14, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/9dd1e85aa2250705fc6ba4c612b4926b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OhNoozz&#39;s gravatar image" /><p>OhNoozz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OhNoozz has no accepted answers">0%</span></p></div></div><div id="comments-container-29901" class="comments-container"><span id="29906"></span><div id="comment-29906" class="comment"><div id="post-29906-score" class="comment-score"></div><div class="comment-text"><p>How did you 'export' the file and how did you transfer the file to your Big Mac?</p></div><div id="comment-29906-info" class="comment-info"><span class="comment-age">(16 Feb '14, 02:27)</span> Kurt Knochner ♦</div></div><span id="29911"></span><div id="comment-29911" class="comment"><div id="post-29911-score" class="comment-score"></div><div class="comment-text"><p>Saved it as pcapng file and transfered to mac fluffy with usb stick. Edit: It's exactly one package. A http /GET request. All other packets (also other HTTP) are the same. Tried multiple times; same result.</p></div><div id="comment-29911-info" class="comment-info"><span class="comment-age">(16 Feb '14, 06:37)</span> OhNoozz</div></div><span id="29912"></span><div id="comment-29912" class="comment"><div id="post-29912-score" class="comment-score"></div><div class="comment-text"><p>What are the Wireshark versions on both systems? Do you see the same on Win7 and Mac?</p></div><div id="comment-29912-info" class="comment-info"><span class="comment-age">(16 Feb '14, 06:56)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29901" class="comment-tools"></div><div class="clear"></div><div id="comment-29901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29914"></span>

<div id="answer-container-29914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29914-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe reassembly settings for http? Check the Preferences options for HTTP Reassembly (Edit | Preferences | Protocols | HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '14, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29914" class="comments-container"></div><div id="comment-tools-29914" class="comment-tools"></div><div class="clear"></div><div id="comment-29914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

