+++
type = "question"
title = "file can not be opened using version 1.6.4 (64 bit) on Windows 7"
description = '''I am running Wireshark 1.6.4 (64 Bit) on Windows 7. When I tried to open files, it failed with following errors. &quot;The capture file appears to be damaged or corrupt. (pcap: File has 771751936 byte packet, bigger than maximum of 65535)&quot;. The same file can be opened fine on wireshark on MacOS so I am a...'''
date = "2012-01-03T14:56:00Z"
lastmod = "2012-01-03T14:56:00Z"
weight = 8209
keywords = [ "wireshark" ]
aliases = [ "/questions/8209" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [file can not be opened using version 1.6.4 (64 bit) on Windows 7](/questions/8209/file-can-not-be-opened-using-version-164-64-bit-on-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8209-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark 1.6.4 (64 Bit) on Windows 7.</p><p>When I tried to open files, it failed with following errors.</p><p>"The capture file appears to be damaged or corrupt. (pcap: File has 771751936 byte packet, bigger than maximum of 65535)".</p><p>The same file can be opened fine on wireshark on MacOS so I am assuming file is fine it is just some kind of bug is causing problem on Windows 7.</p><p>Does anyone experience this problem? Any insight?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '12, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/cad9cb543f4c8ca0f46d461015d1f9b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ABC&#39;s gravatar image" /><p>ABC<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ABC has no accepted answers">0%</span></p></div></div><div id="comments-container-8209" class="comments-container"><span id="8212"></span><div id="comment-8212" class="comment"><div id="post-8212-score" class="comment-score"></div><div class="comment-text"><p>64 or 32 bit MacOS?</p></div><div id="comment-8212-info" class="comment-info"><span class="comment-age">(03 Jan '12, 17:00)</span> cmaynard ♦♦</div></div><span id="8340"></span><div id="comment-8340" class="comment"><div id="post-8340-score" class="comment-score"></div><div class="comment-text"><p>The standard first question: :)</p><p>How was the file copied ? IOW: was the copy a binary copy ?</p></div><div id="comment-8340-info" class="comment-info"><span class="comment-age">(12 Jan '12, 08:36)</span> Bill Meier ♦♦</div></div><span id="8354"></span><div id="comment-8354" class="comment"><div id="post-8354-score" class="comment-score"></div><div class="comment-text"><p>In particular, was it captured on Mac OS X, or some other UN*X, and then copied over to the Windows machine? If the copy was done in a fashion that tries to compensate for the difference between the UN*X text file format (lines with LF at the end of the line) and the DOS/Windows text file format (lines with CR-LF at the end of the line), that would damage the capture file (pcap files are binary files, not text files) and make it not readable.</p></div><div id="comment-8354-info" class="comment-info"><span class="comment-age">(12 Jan '12, 12:03)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-8209" class="comment-tools"></div><div class="clear"></div><div id="comment-8209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

