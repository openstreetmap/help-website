+++
type = "question"
title = "Capturing packets and extracting files from pcap"
description = '''Hello everybody! I am attempting to capture the packets on my own computer, in the hopes of being able to extract any files downloaded from the resulting pcap file. From what I understand this should be possible, but I am having no success in doing so. When in wireshark after the capture, I understa...'''
date = "2015-10-07T05:39:00Z"
lastmod = "2015-10-07T08:30:00Z"
weight = 46389
keywords = [ "capture", "pcap", "http", "stream" ]
aliases = [ "/questions/46389" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing packets and extracting files from pcap](/questions/46389/capturing-packets-and-extracting-files-from-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody! I am attempting to capture the packets on my own computer, in the hopes of being able to extract any files downloaded from the resulting pcap file. From what I understand this should be possible, but I am having no success in doing so. When in wireshark after the capture, I understand that doing file&gt;export objects&gt;HTTP should extract the files from the capture session, but I do not see either of the two .exe files that I downloaded during my session when using this method. I am not using any filters, and I am sniffing on the ethernet that my computer is connected to.</p><p>Help is appreciated!</p></div><div id="question-tags" class="tags-container tags">capture pcap http stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '15, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/9282595526ace3f9b2189a726505b4c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="surfing123&#39;s gravatar image" /><p>surfing123<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="surfing123 has no accepted answers">0%</span></p></div></div><div id="comments-container-46389" class="comments-container"><span id="46395"></span><div id="comment-46395" class="comment"><div id="post-46395-score" class="comment-score"></div><div class="comment-text"><p>Show us the capture file, just put it on CloudShark.</p></div><div id="comment-46395-info" class="comment-info"><span class="comment-age">(07 Oct '15, 07:34)</span> Jaap ♦</div></div><span id="46396"></span><div id="comment-46396" class="comment"><div id="post-46396-score" class="comment-score"></div><div class="comment-text"><p>If the download was through HTTPS, you won't see anything!</p></div><div id="comment-46396-info" class="comment-info"><span class="comment-age">(07 Oct '15, 07:42)</span> Kurt Knochner ♦</div></div><span id="46397"></span><div id="comment-46397" class="comment"><div id="post-46397-score" class="comment-score"></div><div class="comment-text"><p>Ok. Here is the link. The pcap should contain a single exe file, which I am attempting to extract. <a href="https://www.cloudshark.org/captures/d6503563cbc6">https://www.cloudshark.org/captures/d6503563cbc6</a></p></div><div id="comment-46397-info" class="comment-info"><span class="comment-age">(07 Oct '15, 07:56)</span> surfing123</div></div><span id="46398"></span><div id="comment-46398" class="comment"><div id="post-46398-score" class="comment-score"></div><div class="comment-text"><p>Ok, so it appears that when I used networkminer to extract files from the pcap I just posted, I was able to grab the file. The difference between this pcap and the original one is that the original pcap contained larger exe files. Could this be the reason I was originally unable to extra the exe files? Is there some sort of size limitation in play? I was unable to upload the original pcap because cloudshark limits to 2mb.</p></div><div id="comment-46398-info" class="comment-info"><span class="comment-age">(07 Oct '15, 08:00)</span> surfing123</div></div><span id="46399"></span><div id="comment-46399" class="comment"><div id="post-46399-score" class="comment-score"></div><div class="comment-text"><p>Kurt, is there no way to extract a file downloaded over an HTTPS connection?</p></div><div id="comment-46399-info" class="comment-info"><span class="comment-age">(07 Oct '15, 08:03)</span> surfing123</div></div></div><div id="comment-tools-46389" class="comment-tools"></div><div class="clear"></div><div id="comment-46389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46401"></span>

<div id="answer-container-46401" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46401-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to extract and run the file PortRptr.exe from the trace you posted on Cloudshark.</p><p>Go to Edit &gt; Preferences &gt; Protocols &gt; TCP and enable "Allow subdissector to reassemble TCP streams." Then go to File &gt; Export Objects &gt; HTTP. Find and highlight the file and click "Save As."</p><p>If you normally have "Allow subdissector to reassemble streams" off, then turn it back off when you're done saving the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '15, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-46401" class="comments-container"></div><div id="comment-tools-46401" class="comment-tools"></div><div class="clear"></div><div id="comment-46401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

