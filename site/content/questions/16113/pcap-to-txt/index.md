+++
type = "question"
title = "pcap to txt"
description = '''Hi !  If pcap can be converted to txt by using: &quot;tshark -V -r original.pcap &amp;gt; file_to_convert.txt&quot; and pcap can be converted to txt: &quot;text2pcap.exe -e 0x800 file_to_convert.txt result.pcap&quot;, why does the resulted file have a different dimension from the original one? Is there something that I cou...'''
date = "2012-11-20T06:19:00Z"
lastmod = "2012-11-20T06:33:00Z"
weight = 16113
keywords = [ "convert", "txt", "pcap", "conversion", "wireshark" ]
aliases = [ "/questions/16113" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pcap to txt](/questions/16113/pcap-to-txt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16113-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi !</p><p>If pcap can be converted to txt by using: "tshark -V -r original.pcap &gt; <a href="http://file_to_convert.txt">file_to_convert.txt</a>" and pcap can be converted to txt: "text2pcap.exe -e 0x800 <a href="http://file_to_convert.txt">file_to_convert.txt</a> result.pcap", why does the resulted file have a different dimension from the original one?</p><p>Is there something that I could change in order to make it right ?</p><p>Thank you !</p></div><div id="question-tags" class="tags-container tags">convert txt pcap conversion wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '12, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/31a0ef3c5f2c7aa1802925dccaad3f20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AvL&#39;s gravatar image" /><p>AvL<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AvL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '12, 06:30</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-16113" class="comments-container"></div><div id="comment-tools-16113" class="comment-tools"></div><div class="clear"></div><div id="comment-16113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16116"></span>

<div id="answer-container-16116" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16116-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because the output of tshark -V is not the input format of text2pcap. See the <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">manual</a> of text2pcap for the format requirements. These programs are not each others opposite.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '12, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16116" class="comments-container"><span id="16118"></span><div id="comment-16118" class="comment"><div id="post-16118-score" class="comment-score"></div><div class="comment-text"><p>Thank you !!</p><p>Is there a combination of programs that would result a file the same with the original ?</p></div><div id="comment-16118-info" class="comment-info"><span class="comment-age">(20 Nov '12, 06:44)</span> AvL</div></div><span id="16119"></span><div id="comment-16119" class="comment"><div id="post-16119-score" class="comment-score"></div><div class="comment-text"><p>I've changed the commands , but i still don't get the expected result . Is it possible to get the original as final output ? Or am I searching something that can't be done ?</p><p>Thanks !</p></div><div id="comment-16119-info" class="comment-info"><span class="comment-age">(20 Nov '12, 07:45)</span> AvL</div></div><span id="16150"></span><div id="comment-16150" class="comment"><div id="post-16150-score" class="comment-score"></div><div class="comment-text"><p>Sure. od the pcap file, run it through a Perl script to filter out the PCAP headers and construct a text dump file in the specified format. Better yet, have the Perl script <a href="http://hype-free.blogspot.nl/2010/03/parsing-pcap-files-with-perl.html">read the PCAP file directly</a>, using NET::TcpDumpLog. The Perl script you'll have to write though.</p></div><div id="comment-16150-info" class="comment-info"><span class="comment-age">(21 Nov '12, 04:17)</span> Jaap ♦</div></div><span id="16156"></span><div id="comment-16156" class="comment"><div id="post-16156-score" class="comment-score"></div><div class="comment-text"><p>Thanks ! I'll try that .</p></div><div id="comment-16156-info" class="comment-info"><span class="comment-age">(21 Nov '12, 05:35)</span> AvL</div></div></div><div id="comment-tools-16116" class="comment-tools"></div><div class="clear"></div><div id="comment-16116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

