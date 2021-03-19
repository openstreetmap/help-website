+++
type = "question"
title = "tcp options  ( how to make a separate DLL )"
description = '''HI, I have written few lines of code to dissect tcp options ( ORBITAL_META_OPTION 0x18 Citrix-BR add this option) and it is working perfectly. I modified packet-tcp.c (wireshark&#92;epan&#92;dissectors&#92;packet-tcp.c)  first i added required information in static  const ip_tcp_opt tcpopts[] and static hf_regi...'''
date = "2011-08-29T23:32:00Z"
lastmod = "2011-08-30T00:36:00Z"
weight = 5940
keywords = [ "development", "dissector", "tcp" ]
aliases = [ "/questions/5940" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp options ( how to make a separate DLL )](/questions/5940/tcp-options-how-to-make-a-separate-dll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5940-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI,</p><p>I have written few lines of code to dissect tcp options ( ORBITAL_META_OPTION 0x18 Citrix-BR add this option) and it is working perfectly.</p><p>I modified <strong>packet-tcp.c</strong> (wireshark\epan\dissectors\packet-tcp.c)</p><ul><li>first i added required information in <strong>static const ip_tcp_opt tcpopts[]</strong> and <strong>static hf_register_info hf[]</strong></li><li>then my own dissector function to dissect ORBITAL_META_OPTION ( 0x18)</li></ul><p>But the problem is, if someone want to see these feature he has to use my Wireshark ( compiled by me ).</p><p>Now my manager suggested me to write a separate dissector and then <strong>DLL</strong> ( because DLL can be distributed easily).</p><p>Now my final aim is to make a DLL. How should i do ???</p><p>Regards,</p></div><div id="question-tags" class="tags-container tags">development dissector tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/53c5d806ca95207e95aa3287052d708d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vikas&#39;s gravatar image" /><p>Vikas<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vikas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '11, 12:57</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5940" class="comments-container"><span id="5969"></span><div id="comment-5969" class="comment"><div id="post-5969-score" class="comment-score"></div><div class="comment-text"><p>Distributing a DLL is easier than a customized Wireshark build, but maintaining a DLL release could be somewhat painful. DLLs must be compiled against a specific Wireshark version. So, a DLL for 1.4.6 won't necessarily run on 1.6.1 (or vice versa), and this version mismatch can cause Wireshark to fail. Every time Wireshark releases a new version, you have to recompile your DLL to ensure compatibility.</p><p>Consider writing a dissector with the <a href="http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html">Wireshark Lua API</a>, which does not have this problem.</p></div><div id="comment-5969-info" class="comment-info"><span class="comment-age">(30 Aug '11, 12:56)</span> helloworld</div></div></div><div id="comment-tools-5940" class="comment-tools"></div><div class="clear"></div><div id="comment-5940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5946"></span>

<div id="answer-container-5946" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5946-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>packet-tcp is a built in dissector and can't be replaced with a DLL.</p><p>To get your changes included in Wireshark for general distribution see the Developers Guide section 3.9.2 <a href="http://www.wireshark.org/docs/wsdg_html/#ChSrcSend">HERE</a> which basically asks you to raise an enhancement request on Bugzilla and attach your changes as a patch for review.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5946" class="comments-container"></div><div id="comment-tools-5946" class="comment-tools"></div><div class="clear"></div><div id="comment-5946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

