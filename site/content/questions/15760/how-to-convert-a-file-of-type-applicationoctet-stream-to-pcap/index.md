+++
type = "question"
title = "How to convert a file of type application/octet-stream to .pcap?"
description = '''I want to convert a file of type application/octet-stream to .pcap. I tried using text2pcap but its output on terminal is &quot;Read 0 potential packets, wrote 0 packets&quot;'''
date = "2012-11-09T01:23:00Z"
lastmod = "2012-11-09T02:25:00Z"
weight = 15760
keywords = [ "pcap" ]
aliases = [ "/questions/15760" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert a file of type application/octet-stream to .pcap?](/questions/15760/how-to-convert-a-file-of-type-applicationoctet-stream-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15760-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to convert a file of type application/octet-stream to .pcap. I tried using text2pcap but its output on terminal is "Read 0 potential packets, wrote 0 packets"</p></div><div id="question-tags" class="tags-container tags">pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '12, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p>Akhil<br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '12, 01:23</p></div></div><div id="comments-container-15760" class="comments-container"></div><div id="comment-tools-15760" class="comment-tools"></div><div class="clear"></div><div id="comment-15760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15765"></span>

<div id="answer-container-15765" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15765-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>without further information you can't, because application/octet-stream is just a MIME type to encode data in several protocols.</p><p>Unless the encoded data is already in pcap format, there is no way to create a <strong>meaningful</strong> pcap file from that data. Think about it yourself:</p><ul><li>Should the encoded data be the payload of one/two/three packets?</li><li>If so, what protocol would you use for that packet (TCP/UDP/HTTP/Telnet)?</li><li>Which addresses would you use (IP, Ethernet, etc.)</li><li>etc.</li></ul><p>As you did not explain anything about the nature of your encoded data, the circumstances and the reason why you need to convert that data to a pcap file, nobody will be able to give a helpful/meaningful answer.</p><p>Please consider to be more specific in your questions. It will help yourself and it will help others to help you. I suggest you add at least these things to your questions</p><ul><li>Wireshark version</li><li>OS version</li><li>An exact description of what you want to do</li><li>Sample data</li><li>Expected result and possibly what you got instead, if you tried yourself</li><li>Any (error) messages of Wireshark and/or the OS, if there are any</li></ul><p>BTW: text2pcap accepts only data in the format defined in the following link</p><blockquote><p><code>http://www.wireshark.org/docs/wsug_html_chunked/AppToolstext2pcap.html</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '12, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '12, 02:27</p></div></div><div id="comments-container-15765" class="comments-container"><span id="15767"></span><div id="comment-15767" class="comment"><div id="post-15767-score" class="comment-score"></div><div class="comment-text"><p>Wireshark version:1.7.0 OS Ubuntu 10.04</p><p>I have a file which contains amf packet but i can't open it in wireshark. So i am converting it into .pcap.</p><p>Error message of Wireshark :isn't a capture file in a format Wireshark understands.</p></div><div id="comment-15767-info" class="comment-info"><span class="comment-age">(09 Nov '12, 03:02)</span> Akhil</div></div><span id="15768"></span><div id="comment-15768" class="comment"><div id="post-15768-score" class="comment-score"></div><div class="comment-text"><p>I opened the file in Bless Hex Editor and copied the hex values in a text document and executed the following command: text2pcap amf1 outfile. The output for this is Read 0 potential packets, wrote 0 packets</p></div><div id="comment-15768-info" class="comment-info"><span class="comment-age">(09 Nov '12, 03:05)</span> Akhil</div></div><span id="15769"></span><div id="comment-15769" class="comment"><div id="post-15769-score" class="comment-score"></div><div class="comment-text"><p>O.K. now we need a sample of the data. Please post the amf packet here (or at <a href="http://pastebin.com">pastebin.com</a>).</p><ul><li>How did you generate that packet?</li><li>is it a full packet with all layers (Ethernet, IP, TCP, etc.)?</li></ul></div><div id="comment-15769-info" class="comment-info"><span class="comment-age">(09 Nov '12, 03:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15765" class="comment-tools"></div><div class="clear"></div><div id="comment-15765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

