+++
type = "question"
title = "Providing each packet to wireshark using command line"
description = '''Hello All, I am right now writing a pcap file to save all packets, as soon as I receive. Then I am opening that pcap into wireshark using wireshark -k -i ${FILE}. Instead of that I want to provide each packet to wireshark? Is that possible? Also when I provide the pcap file, and after running the co...'''
date = "2013-07-24T10:07:00Z"
lastmod = "2013-07-25T11:23:00Z"
weight = 23333
keywords = [ "packets", "pdu", "pcap", "wireshark" ]
aliases = [ "/questions/23333" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Providing each packet to wireshark using command line](/questions/23333/providing-each-packet-to-wireshark-using-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23333-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I am right now writing a pcap file to save all packets, as soon as I receive. Then I am opening that pcap into wireshark using <code>wireshark -k -i ${FILE}</code>. Instead of that I want to provide each packet to wireshark? Is that possible?</p><p>Also when I provide the pcap file, and after running the command if I append packets in the file would wireshark analyse them also?</p><p>Thank you very much.</p></div><div id="question-tags" class="tags-container tags">packets pdu pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '13, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/b0df273d0b1e4325420a40aa1a00664e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WiData&#39;s gravatar image" /><p>WiData<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WiData has no accepted answers">0%</span></p></div></div><div id="comments-container-23333" class="comments-container"></div><div id="comment-tools-23333" class="comment-tools"></div><div class="clear"></div><div id="comment-23333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23364"></span>

<div id="answer-container-23364" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23364-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Quick follow up, I am creating pcap headers in a c++ files and in the same file I want to execute dumpcap from the same c++ file to save those pcap headers, so that I can open the pcap file written by dumpcap in wireshark later on. What should I use as -i interface option?</p></blockquote><p>Well, you don't have to call dumpcap, as that's just the capturing process to generate a pcap data stream, that is piped to Wireshark. So, basically what you need to do in your program is similar to this.</p><blockquote><p><code>tcpdump -ni eth0 -w - | wireshark -k -i -</code><br />
</p></blockquote><p>tcpdump writes a data stream (pcap data structure) to STDOUT (-w -). That output is piped to STDIN of Wireshark (-i -).</p><p>So, in your c++ program the part of tcpdump is obsolete, as you create the packets yourself. So here is the way to go.</p><p><strong>First option:</strong></p><ul><li>spawn a Wireshark process in your code: <code>wireshark -k -i -</code></li><li>write your generated packets to STDOUT. That data needs to be in <strong>pcap format</strong> as Wireshark will only understand that. If you cannot write pcap format, you could use text2pcap as an intermediate tool: <code>your_application -&gt; STDOUT | text2pcap - - | wireshark -k -i -</code></li><li>as soon as you are ready, kill the spawned wireshark process</li></ul><p><strong>Second option:</strong></p><ul><li>create a named pipe (please check your OS manual how to do that). Also here: <a href="http://wiki.wireshark.org/CaptureSetup/Pipes">http://wiki.wireshark.org/CaptureSetup/Pipes</a> for some example code</li><li>spawn a wireshark process, that <strong>reads</strong> from that named pipe: wireshark -nr \.\pipe\wireshark</li><li>write <strong>pcap formated</strong> data to that pipe in your application</li><li>as soon as you are ready, kill the spawned wireshark process</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '13, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23364" class="comments-container"><span id="23392"></span><div id="comment-23392" class="comment"><div id="post-23392-score" class="comment-score"></div><div class="comment-text"><p>@kurt: thanks a lot for your feedback and it is very useful. I appreciate giving a detailed answer. I am just confused over one thing, I dont want to kill the wireshark process. As the packet are being created I just want them to pass to the wireshark application? I hope I am clear enough in asking this.</p></div><div id="comment-23392-info" class="comment-info"><span class="comment-age">(26 Jul '13, 14:55)</span> WiData</div></div><span id="23399"></span><div id="comment-23399" class="comment"><div id="post-23399-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I dont want to kill the wireshark process.</p></blockquote><p>That was just in case you want to end the whole workflow within your c++ application (at the end). If you don't want to that, don't kill the process and let the user end Wireshark by closing the GUI window.</p></div><div id="comment-23399-info" class="comment-info"><span class="comment-age">(27 Jul '13, 00:14)</span> Kurt Knochner ♦</div></div><span id="23433"></span><div id="comment-23433" class="comment"><div id="post-23433-score" class="comment-score"></div><div class="comment-text"><p>@kurt: thanks a lot for your help. I tried it and it seems it almost worked except the same error like the post in <a href="http://ask.wireshark.org/questions/14773/end-of-file-on-pipe-magic-during-open">http://ask.wireshark.org/questions/14773/end-of-file-on-pipe-magic-during-open</a> I am using this code <a href="http://pastie.org/8188169">http://pastie.org/8188169</a> Am I doing something wrong with the pipe? The d_msg is the pcap header which I want to pass to the wireshark.</p></div><div id="comment-23433-info" class="comment-info"><span class="comment-age">(29 Jul '13, 15:43)</span> WiData</div></div><span id="23434"></span><div id="comment-23434" class="comment"><div id="post-23434-score" class="comment-score"></div><div class="comment-text"><p>And when I use this <a href="http://pastie.org/8188232">http://pastie.org/8188232</a> I get this error <code>The file "/tmp/wireshark_mine.pcap_20130730012654_ndbFzk" is a capture for a network type that Wireshark doesn't support</code> Not sure where I am going wrong.</p></div><div id="comment-23434-info" class="comment-info"><span class="comment-age">(29 Jul '13, 16:29)</span> WiData</div></div><span id="23436"></span><div id="comment-23436" class="comment"><div id="post-23436-score" class="comment-score"></div><div class="comment-text"><blockquote><p>system("mkfifo /tmp/mine.pcap");</p></blockquote><p>What is your OS?</p></div><div id="comment-23436-info" class="comment-info"><span class="comment-age">(29 Jul '13, 19:30)</span> Kurt Knochner ♦</div></div><span id="23438"></span><div id="comment-23438" class="comment not_top_scorer"><div id="post-23438-score" class="comment-score"></div><div class="comment-text"><p>Linux-Ubuntu 12.04</p></div><div id="comment-23438-info" class="comment-info"><span class="comment-age">(29 Jul '13, 23:09)</span> WiData</div></div><span id="23453"></span><div id="comment-23453" class="comment not_top_scorer"><div id="post-23453-score" class="comment-score"></div><div class="comment-text"><p>I also tried with the mkfifo() function. No Change with it. Its like I am almost there and then I can not resolve it. Should I be using netcat? I am not much familiar with it but I think it may be useful.</p></div><div id="comment-23453-info" class="comment-info"><span class="comment-age">(30 Jul '13, 14:22)</span> WiData</div></div></div><div id="comment-tools-23364" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-23364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23334"></span>

<div id="answer-container-23334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23334-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>When running a live capture, Wireshark actually runs dumpcap to do the capturing which then pipes the packets into the Wireshark process, maybe you could use that technique.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23334" class="comments-container"><span id="23347"></span><div id="comment-23347" class="comment"><div id="post-23347-score" class="comment-score"></div><div class="comment-text"><p>Grahamb: Quick follow up, I am creating pcap headers in a c++ files and in the same file I want to execute <code>dumpcap</code> from the same c++ file to save those pcap headers, so that I can open the pcap file written by dumpcap in wireshark later on. What should I use as <code>-i</code> interface option?</p></div><div id="comment-23347-info" class="comment-info"><span class="comment-age">(24 Jul '13, 15:23)</span> WiData</div></div><span id="23356"></span><div id="comment-23356" class="comment"><div id="post-23356-score" class="comment-score">1</div><div class="comment-text"><p>I'm afraid that's out of my knowledge zone.</p></div><div id="comment-23356-info" class="comment-info"><span class="comment-age">(25 Jul '13, 02:38)</span> grahamb ♦</div></div></div><div id="comment-tools-23334" class="comment-tools"></div><div class="clear"></div><div id="comment-23334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

