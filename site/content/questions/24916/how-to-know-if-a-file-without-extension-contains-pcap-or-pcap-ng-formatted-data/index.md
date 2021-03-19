+++
type = "question"
title = "how to know if a file without extension contains PCAP or PCAP-NG formatted data?"
description = '''Hi, i have a trace file which is in either PCAP or PCAP-NG format, but it has no extension. With a drag-and-drop i can load/open it in Wireshark. The columns (&#x27;No.&#x27;, &#x27;Time&#x27;, &#x27;Source&#x27;, &#x27;Destination&#x27;, &#x27;Protocol&#x27;, &#x27;Length&#x27;, &#x27;Info&#x27;) and the data look fine, but how can i know in which format (PCAP or PCA...'''
date = "2013-09-18T07:25:00Z"
lastmod = "2013-09-22T05:33:00Z"
weight = 24916
keywords = [ "ntartest", "pcap-ng", "pcap" ]
aliases = [ "/questions/24916" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to know if a file without extension contains PCAP or PCAP-NG formatted data?](/questions/24916/how-to-know-if-a-file-without-extension-contains-pcap-or-pcap-ng-formatted-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24916-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i have a trace file which is in either PCAP or PCAP-NG format, but it has no extension.</p><p>With a drag-and-drop i can load/open it in Wireshark. The columns ('No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info') and the data look fine, but how can i know in which format (PCAP or PCAP-NG) the file contents is written?</p><p>My question more precisely:</p><ul><li>when i load into Wireshark a PCAP-NG file, can i see anything that i cannot see when i load a PCAP file?</li><li>if there's nothing to distinguish PCAP-formatted data from PCAP-NG-formatted data in Wireshark, what's the best tool on Windows to distinguish PCAP contents from PCAP-NG contents?</li><li>ntartest, the simplistic PCAP-NG reader (as mentioned on the Wireshark Wiki's Development/PcapNg page) does this job, somehow: when launched with a PCAP file as argument, it crashes! Sadly, it doesn't show the contents of the Section Header Block or of the Interface Description Blocks. So, any better suggestion?</li></ul></div><div id="question-tags" class="tags-container tags">ntartest pcap-ng pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '13, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/0c4a0d3634bb05bf810ee1b5fe13ec54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ime-braun&#39;s gravatar image" /><p>ime-braun<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ime-braun has no accepted answers">0%</span></p></div></div><div id="comments-container-24916" class="comments-container"><span id="24925"></span><div id="comment-24925" class="comment"><div id="post-24925-score" class="comment-score"></div><div class="comment-text"><blockquote><p>when i load into Wireshark a PCAP-NG file, can i see anything that i cannot see when i load a PCAP file?</p></blockquote><p>Do you mean "is there information that can be stored in a pcap-ng file that can't be stored in a pcap file, so that captures in pcap-ng files are more informative?" or do you mean "in Wireshark, does something show up for pcap-ng files that doesn't show up for pcap files, so that I can distinguish between pcap-ng files and pcap files that way?"</p></div><div id="comment-24925-info" class="comment-info"><span class="comment-age">(18 Sep '13, 11:59)</span> Guy Harris ♦♦</div></div><span id="25067"></span><div id="comment-25067" class="comment"><div id="post-25067-score" class="comment-score"></div><div class="comment-text"><p>the second meaning: "does something in Wireshark show up". cmaynard gave an answer, and I found another one: when I capture traffic with Wireshark or when I open a PCAP-NG dump file, I can click on each line in the upper sub-window and in the middle sub-window (which gives an analytical description of the selected packet), the second line gives the interface id on which the packet was captured. I don't get this piece of information when I open a PCAP dump file.</p></div><div id="comment-25067-info" class="comment-info"><span class="comment-age">(22 Sep '13, 04:14)</span> ime-braun</div></div></div><div id="comment-tools-24916" class="comment-tools"></div><div class="clear"></div><div id="comment-24916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="24917"></span>

<div id="answer-container-24917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24917-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark, you can look at: <code>Statistics -&gt; Summary -&gt; Format</code>.</p><p>Alternatively, you can use the Wireshark command-line <a href="http://www.wireshark.org/docs/man-pages/capinfos.html">capinfos</a> companion tool to find this out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24917" class="comments-container"></div><div id="comment-tools-24917" class="comment-tools"></div><div class="clear"></div><div id="comment-24917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25069"></span>

<div id="answer-container-25069" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25069-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>if there's nothing to distinguish PCAP-formatted data from PCAP-NG-formatted data</p></blockquote><p>The difference between pcap and pcapng is the magic bytes used at the beginning of the file.</p><p><strong>pcap</strong>: D4C3B2A1 or A1B2C3D4 (depends on byte order)<br />
<strong>pcapng</strong>: 0A0D0D0A + (4 bytes length) + 4D3C2B1A or 1A2B3C4D (depends on byte order)</p><blockquote><p><strong>what's the best tool on Windows</strong> to distinguish PCAP contents from PCAP-NG contents?</p></blockquote><p>Please check the following tool</p><p><strong>TrID</strong> - File Identifier<br />
<a href="http://mark0.net/soft-trid.html">http://mark0.net/soft-trid.html</a></p><p>If contains a list of several thousand file types, including <strong>pcap</strong> and <strong>pcapng</strong> (it checks the byte pattern mentioned above).</p><p>Sample output for a <strong>pcapng</strong> file</p><pre><code>Z:&gt;trid file.pcapng
TrID/32 - File Identifier v2.10 - (C) 2003-11 By M.Pontello
Definitions found:  5128
Analyzing...
Collecting data from file: file.pcapng
 79.9% (.PCAPNG) Wireshark PCAP Next Generation Dump File Format (Little Endian) (4004/2)
 20.0% (.PCX) ZSoft PCX bitmap (1002/3)</code></pre><p>Sample output for a <strong>pcap</strong> file</p><pre><code>Z:&gt;trid file.pcap
TrID/32 - File Identifier v2.10 - (C) 2003-11 By M.Pontello
Definitions found:  5128
Analyzing...
Collecting data from file: file.pcap
100.0% (.ACP/PCAP) TCPDUMP&#39;s style capture (4000/1)</code></pre><p>There is also a tool called <strong>TriDScan</strong> which allows to extend the file type database by scanning several similar files. The tool tries to find similar byte strings on all files and then creates an XML file.</p><p><strong>TrIDScan</strong> - Patterns scanner<br />
<a href="http://mark0.net/soft-tridscan.html">http://mark0.net/soft-tridscan.html</a></p><p>With another tool (TrIDDefsPack - on the same page as TriDScan), you can pack the XML file into the definition file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '13, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '13, 16:14</p></div></div><div id="comments-container-25069" class="comments-container"></div><div id="comment-tools-25069" class="comment-tools"></div><div class="clear"></div><div id="comment-25069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24926"></span>

<div id="answer-container-24926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24926-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>ntartest, the simplistic PCAP-NG reader (as mentioned on the Wireshark Wiki's Development/PcapNg page) does this job, somehow: when launched with a PCAP file as argument, it crashes!</p></blockquote><p>I couldn't get it to crash with a pcap file, but it reported errors, which is not surprising, as it's not checking to make sure the file <em>is</em> a pcap-ng file, it's just <em>assuming</em> it is. It's presumably crashing for you for the same reason.</p><blockquote><p>Sadly, it doesn't show the contents of the Section Header Block or of the Interface Description Blocks.</p></blockquote><p>Presumably, you mean it doesn't show the contents of the Section Header Block or of the Interface Description Blocks of pcap-ng files, because pcap files don't <em>have</em> Section Header Blocks or Interface Description Blocks.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-24926" class="comments-container"></div><div id="comment-tools-24926" class="comment-tools"></div><div class="clear"></div><div id="comment-24926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

