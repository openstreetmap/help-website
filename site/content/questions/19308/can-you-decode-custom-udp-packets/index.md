+++
type = "question"
title = "Can you decode custom UDP packets?"
description = '''I have a Xilinx board pushing out periodic UDP messages to the network with a computer running WireShark that is picking up all of the messages that the FPGA is generating. The data section of the UDP packet is not simple to decode so troubleshooting while just looking at the HEX ins&#x27;t a very easy t...'''
date = "2013-03-08T11:11:00Z"
lastmod = "2013-03-08T13:19:00Z"
weight = 19308
keywords = [ "diameter", "udp", "radius", "fpga", "decoder" ]
aliases = [ "/questions/19308" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can you decode custom UDP packets?](/questions/19308/can-you-decode-custom-udp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19308-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Xilinx board pushing out periodic UDP messages to the network with a computer running WireShark that is picking up all of the messages that the FPGA is generating. The data section of the UDP packet is not simple to decode so troubleshooting while just looking at the HEX ins't a very easy task. Is it possible to create my own decoder so that custom fields can be populated with human readable text?</p><p>If the above answer is yes then how do I create one of those decoders and where do I put it in the Wireshark directory structure?</p><p>Thank you.</p><p>Details: Computer: standard Windows XP 32bit</p></div><div id="question-tags" class="tags-container tags">diameter udp radius fpga decoder</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/fc82e692d58dbf54f004ba3251d8338f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="madscientist314&#39;s gravatar image" /><p>madscientist314<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="madscientist314 has no accepted answers">0%</span></p></div></div><div id="comments-container-19308" class="comments-container"></div><div id="comment-tools-19308" class="comment-tools"></div><div class="clear"></div><div id="comment-19308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19313"></span>

<div id="answer-container-19313" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19313-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are three main ways to create a dissector; a text based one with WSGD, a script based one in lua or python, or a c dissector.</p><p><a href="http://wsgd.free.fr">WSGD</a> is a DLL that adds dissection via a text based description. Relatively simple to start with and for simple protocols may be sufficient. Windows only.</p><p>Wireshark supports <a href="http://wiki.wireshark.org/Lua">Lua</a> and <a href="http://wiki.wireshark.org/Python">Python</a> as scripting languages for creating dissectors, lua is the most popular. Lua is available on more platforms than python.</p><p>A <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChapterDissection.html">c based dissector</a> is the traditional way to write a dissector, facilities are very comprehensive but it can be the most complicated method.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '13, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19313" class="comments-container"></div><div id="comment-tools-19313" class="comment-tools"></div><div class="clear"></div><div id="comment-19313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

