+++
type = "question"
title = "split netscalar large trace file"
description = '''How to split large netscalar cap file,it is showing sun snoop file type,tried editcap with no luck'''
date = "2013-07-04T06:00:00Z"
lastmod = "2013-07-04T06:29:00Z"
weight = 22648
keywords = [ "nstrace" ]
aliases = [ "/questions/22648" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [split netscalar large trace file](/questions/22648/split-netscalar-large-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22648-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to split large netscalar cap file,it is showing sun snoop file type,tried editcap with no luck</p></div><div id="question-tags" class="tags-container tags">nstrace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-22648" class="comments-container"></div><div id="comment-tools-22648" class="comment-tools"></div><div class="clear"></div><div id="comment-22648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22650"></span>

<div id="answer-container-22650" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22650-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please call editcap with the following option</p><blockquote><p>editcap <strong>-F snoop</strong></p></blockquote><p><strong>UPDATE</strong></p><p>I'm sorry, I was on the wrong track. -F is just the <strong>output</strong> file format.</p><p>The following command works with a sample snoop file. It will split the original file in pieces of 100 packets.</p><blockquote><p>editcap -c 100 input.snoop output.pcap</p></blockquote><p>Sample file:</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=genbroad.snoop">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=genbroad.snoop</a></p></blockquote><p>BTW: it also works with option -F snoop on my system (Windows XP, Wireshark 1.10.0)</p><blockquote><p>editcap -c 100 -F snoop input.snoop output.pcap</p></blockquote><p>If these commands do not work with your snoop file, please post the wireshark version (wireshark -v) and the error message.</p><p><strong>UPDATE 2</strong></p><p>O.K. I did a test with a <a href="https://bugs.wireshark.org/bugzilla/attachment.cgi?id=8051">sample nstrace file</a> and this command works.</p><blockquote><p><code>editcap -c 200 -F nstrace20  nstrace1_test.cap output.pcap</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '13, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '13, 02:15</p></div></div><div id="comments-container-22650" class="comments-container"><span id="22660"></span><div id="comment-22660" class="comment"><div id="post-22660-score" class="comment-score"></div><div class="comment-text"><p>tried it still not able to split the file,showing error "editcap: Can't open or create output.pcap: Files from that network type can't be saved in that format"</p></div><div id="comment-22660-info" class="comment-info"><span class="comment-age">(04 Jul '13, 08:16)</span> kishan pandey</div></div><span id="22661"></span><div id="comment-22661" class="comment"><div id="post-22661-score" class="comment-score"></div><div class="comment-text"><p>please see my UPDATE in the answer.</p></div><div id="comment-22661-info" class="comment-info"><span class="comment-age">(04 Jul '13, 08:32)</span> Kurt Knochner ♦</div></div><span id="22663"></span><div id="comment-22663" class="comment"><div id="post-22663-score" class="comment-score"></div><div class="comment-text"><p>Please find the capinfo output,it starts with .cap extension not snoop.Wireshark version is 1.8.4.</p><p><code> D:\ndl\Wireshark&gt;capinfos.exe nstrace9.cap File name:           nstrace9.cap File type:           NetScaler Trace (Version 2.0) File encapsulation:  NetScaler Encapsulation 2.0 of Ethernet Packet size limit:   file hdr: (not set) Number of packets:   152364 File size:           75546624 bytes Data size:           70570504 bytes Capture duration:    1 seconds Start time:          Tue Jul 02 13:47:51 2013 End time:            Tue Jul 02 13:47:51 2013 Data byte rate:      79368489.77 bytes/sec Data bit rate:       634947918.14 bits/sec Average packet size: 463.17 bytes Average packet rate: 171359.14 packets/sec SHA1:                f61908d04e1b8d46fb9e350b93a1a54bdcf8fd61 RIPEMD160:           9398681630f2bdc6c92d401ea62734f82aece3ff MD5:                 866ada08168425a3de8513d163993447 Strict time order:   False</code></p></div><div id="comment-22663-info" class="comment-info"><span class="comment-age">(04 Jul '13, 09:39)</span> kishan pandey</div></div><span id="22666"></span><div id="comment-22666" class="comment"><div id="post-22666-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it is showing sun snoop file type</p></blockquote><p>O.K. so it is not a snoop file.</p><p>So, can you please post the full error message of editcap and the parameters you used?</p></div><div id="comment-22666-info" class="comment-info"><span class="comment-age">(04 Jul '13, 11:14)</span> Kurt Knochner ♦</div></div><span id="22686"></span><div id="comment-22686" class="comment"><div id="post-22686-score" class="comment-score"></div><div class="comment-text"><p>editcap -c 50000 -F snoop nstrace9.cap output.pcap and then it shows an error "editcap: Can't open or create output.pcap: Files from that network type can't be saved in that format."</p></div><div id="comment-22686-info" class="comment-info"><span class="comment-age">(05 Jul '13, 01:52)</span> kishan pandey</div></div><span id="22693"></span><div id="comment-22693" class="comment not_top_scorer"><div id="post-22693-score" class="comment-score"></div><div class="comment-text"><p>Try splitting it with a command that does not contain the string "snoop" anywhere.</p><p>You cannot write out packets from a NetScaler file into a snoop file or a pcap file or a pcap-ng file or any other file format, because, at least inside Wireshark and its tools, packets from NetScaler files have special NetScaler metadata at the beginning, and no other file formats support that.</p><p>Try something such as</p><pre><code>editcap -c 50000 nstrace9.cap output.cap</code></pre></div><div id="comment-22693-info" class="comment-info"><span class="comment-age">(05 Jul '13, 11:59)</span> Guy Harris ♦♦</div></div><span id="22701"></span><div id="comment-22701" class="comment not_top_scorer"><div id="post-22701-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris,badluck again"editcap -c 50000 -F nstrace9.cap output.cap". "editcap: "nstrace9.cap" isn't a valid capture file type".</p></div><div id="comment-22701-info" class="comment-info"><span class="comment-age">(07 Jul '13, 05:04)</span> kishan pandey</div></div><span id="22702"></span><div id="comment-22702" class="comment not_top_scorer"><div id="post-22702-score" class="comment-score"></div><div class="comment-text"><p>Sorry, no -F flag. I've edited my comment to fix that.</p></div><div id="comment-22702-info" class="comment-info"><span class="comment-age">(07 Jul '13, 09:39)</span> Guy Harris ♦♦</div></div><span id="22713"></span><div id="comment-22713" class="comment not_top_scorer"><div id="post-22713-score" class="comment-score"></div><div class="comment-text"><p>See UPDATE 2 in my answer.</p></div><div id="comment-22713-info" class="comment-info"><span class="comment-age">(08 Jul '13, 02:14)</span> Kurt Knochner ♦</div></div><span id="22747"></span><div id="comment-22747" class="comment not_top_scorer"><div id="post-22747-score" class="comment-score"></div><div class="comment-text"><p>Great Kurt it worked this time,nothing will left unasnswered in this forum.</p></div><div id="comment-22747-info" class="comment-info"><span class="comment-age">(08 Jul '13, 22:41)</span> kishan pandey</div></div></div><div id="comment-tools-22650" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-22650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

