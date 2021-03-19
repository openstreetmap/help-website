+++
type = "question"
title = "export .pcap file in readable format"
description = '''i open with wireshark a .pcap file , so what i need is to somehow export all the data of the specific protocol , i see the data when i expand the tree inside the program but when using the File-&amp;gt; export packet Dissections on csv format i can not see the actual data but only the data of the column...'''
date = "2017-02-28T23:41:00Z"
lastmod = "2017-03-01T03:45:00Z"
weight = 59752
keywords = [ "pcap", "export" ]
aliases = [ "/questions/59752" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [export .pcap file in readable format](/questions/59752/export-pcap-file-in-readable-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59752-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i open with wireshark a .pcap file , so what i need is to somehow export all the data of the specific protocol , i see the data when i expand the tree inside the program but when using the File-&gt; export packet Dissections on csv format i can not see the actual data but only the data of the columns (No ,Time,Source,.....0 ) is there a way to export the actual data of the spesific protocol in a readable format , for example csv ????</p></div><div id="question-tags" class="tags-container tags">pcap export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/afa543678e40d3f4ab9b53bebf9fc679?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chriskaza81&#39;s gravatar image" /><p>chriskaza81<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chriskaza81 has no accepted answers">0%</span></p></div></div><div id="comments-container-59752" class="comments-container"></div><div id="comment-tools-59752" class="comment-tools"></div><div class="clear"></div><div id="comment-59752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59756"></span>

<div id="answer-container-59756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59756-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are some options to export payload data.</p><p>For example you can export objects (e.g. SMB files, TFTP files, HTTP objects...) or you can save the payload of a TCP or UDP stream (Follow TCP Stream -&gt; Save as ASCII, C Array...).</p><p>It depends on your requirement and your protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-59756" class="comments-container"><span id="59759"></span><div id="comment-59759" class="comment"><div id="post-59759-score" class="comment-score"></div><div class="comment-text"><p>And don't forget about tshark -T fields</p></div><div id="comment-59759-info" class="comment-info"><span class="comment-age">(01 Mar '17, 05:39)</span> Jaap ♦</div></div><span id="59767"></span><div id="comment-59767" class="comment"><div id="post-59767-score" class="comment-score"></div><div class="comment-text"><p>the protocol is sr15 it is a radar which sends some coordinates and i need somehow to read them from the packet contents . Unfortunately i tried the above you suggested but with no luck. There must me some way to do it i also tried with tshark commands but still can not achieve any results</p></div><div id="comment-59767-info" class="comment-info"><span class="comment-age">(01 Mar '17, 09:47)</span> chriskaza81</div></div><span id="59772"></span><div id="comment-59772" class="comment"><div id="post-59772-score" class="comment-score"></div><div class="comment-text"><blockquote><p>the protocol is sr15 it is a radar which sends some coordinates</p></blockquote><p>Presumably you either have your own dissector or somebody's plugin; Wireshark doesn't include a dissector for it.</p><blockquote><p>i also tried with tshark commands but still can not achieve any results</p></blockquote><p>If the dissector gives those coordinates names, i.e. treats them as named fields, <code>tshark -T fields</code> should work - use <code>-e</code> flags, and specify the names of the fields as arguments to the <code>-e</code> flags. If it <em>doesn't</em> give those coordinates names, it should be improved so that it does so.</p></div><div id="comment-59772-info" class="comment-info"><span class="comment-age">(01 Mar '17, 10:24)</span> Guy Harris ♦♦</div></div><span id="59844"></span><div id="comment-59844" class="comment"><div id="post-59844-score" class="comment-score"></div><div class="comment-text"><p>Acctually managed to extract the payload running the above command: tshark -r c:\myFile.pcap -x -R frame.number==1&gt;outpout.txt For now this is the only way i found out ..</p><p>Also i am looking into the PcapDotNet library , i see the PayloadLayer class but can not see any data in ascii format</p></div><div id="comment-59844-info" class="comment-info"><span class="comment-age">(04 Mar '17, 10:10)</span> chriskaza81</div></div></div><div id="comment-tools-59756" class="comment-tools"></div><div class="clear"></div><div id="comment-59756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

