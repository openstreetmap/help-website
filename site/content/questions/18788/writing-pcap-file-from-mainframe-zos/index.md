+++
type = "question"
title = "Writing PCAP file from mainframe ( z/os )"
description = '''I am trying to write a packet trace file in PCAP format from a packet trace I&#x27;ve captured on z/os. I am trying to mimic what IBM does with IPCS conversion to SNIFFER/PCAP format. IBM uses the following global header which in no way matches up to the PCAP format: (note: the first part of the file is ...'''
date = "2013-02-20T15:06:00Z"
lastmod = "2013-02-20T16:20:00Z"
weight = 18788
keywords = [ "mainframe" ]
aliases = [ "/questions/18788" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Writing PCAP file from mainframe ( z/os )](/questions/18788/writing-pcap-file-from-mainframe-zos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18788-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to write a packet trace file in PCAP format from a packet trace I've captured on z/os. I am trying to mimic what IBM does with IPCS conversion to SNIFFER/PCAP format.</p><p>IBM uses the following global header which in no way matches up to the PCAP format: (note: the first part of the file is 'TRSNIFF DATA' in ascii.</p><p>x01001200 (magic number?)<br />
</p><p>x00000100 (major version/minor version)<br />
</p><p>x1000CEA2 (zone)<br />
</p><p>x41420401 (sig figs)<br />
</p><p>x01050000 (max length)<br />
</p><p>x00000000 (data link type)</p><p>Can anyone make sense of this global header? I am trying to make sense of it, and even with big endian/little endian, i can make no sense of this, but it does work when i feed it into WIRESHARK.</p><p>(I have some questions about the packet header too, but first the global header).</p></div><div id="question-tags" class="tags-container tags">mainframe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/d2dc1cbc0f802ea0e3cec3a2e276e1af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbauman&#39;s gravatar image" /><p>mbauman<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbauman has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-18788" class="comments-container"></div><div id="comment-tools-18788" class="comment-tools"></div><div class="clear"></div><div id="comment-18788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18790"></span>

<div id="answer-container-18790" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18790-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a Sniffer capture file. The format is 'described' here:</p><blockquote><p><code>http://anonsvn.wireshark.org/wireshark/trunk/wiretap/ngsniffer.c</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '13, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18790" class="comments-container"><span id="18807"></span><div id="comment-18807" class="comment"><div id="post-18807-score" class="comment-score"></div><div class="comment-text"><p>I.e., that file is probably the result of converting to Sniffer format, not whatever "raw" file gets converted to Sniffer or pcap format.</p></div><div id="comment-18807-info" class="comment-info"><span class="comment-age">(21 Feb '13, 14:41)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18790" class="comment-tools"></div><div class="clear"></div><div id="comment-18790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

