+++
type = "question"
title = "Wireshark save output file name Date"
description = '''I am creating an automatic routine to save pcap file. I&#x27;m having trouble saving the file with the date. Can someone help me? C:&#92;Program Files&#92;Wireshark&amp;gt;Tshark -i rpcap://[172.16.254.6]/&#92;Device&#92;NPF_{CF9CFF4 6-79FF-4A97-802A-F6CEF5896D29} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -w C:&#92; APP01%da...'''
date = "2017-06-26T18:09:00Z"
lastmod = "2017-06-27T20:49:00Z"
weight = 62313
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/62313" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark save output file name Date](/questions/62313/wireshark-save-output-file-name-date)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62313-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am creating an automatic routine to save pcap file. I'm having trouble saving the file with the date. Can someone help me?</p><pre><code>C:\Program Files\Wireshark&gt;Tshark -i rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF4
6-79FF-4A97-802A-F6CEF5896D29} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -w C:\
APP01%date:~4,2%%date:~7,2%%date%~10,4%.pcap
tshark: A capture filter was specified both with &quot;-f&quot; and with additional comman
d-line arguments.</code></pre></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '17, 18:09</strong></p><img src="https://secure.gravatar.com/avatar/a95becaa9162bc901663cdd569efda99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorgeMiguelr210&#39;s gravatar image" /><p>JorgeMiguelr210<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorgeMiguelr210 has no accepted answers">0%</span></p></div></div><div id="comments-container-62313" class="comments-container"></div><div id="comment-tools-62313" class="comment-tools"></div><div class="clear"></div><div id="comment-62313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62335"></span>

<div id="answer-container-62335" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62335-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Those date commands appear to generate a file name with spaces in it. In that case you're going to need to quote the file name so that it's passed to tshark as a single argument (rather than 2 or more). For example:</p><pre><code>C:\Program Files\Wireshark&gt;Tshark -i rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5896D29} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -w &quot;C:\APP01%date:~4,2%%date:~7,2%%date%~10,4%.pcap&quot;</code></pre><p>At least that's what would be necessary on Unix/Linux (which I'm far more familiar with...).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-62335" class="comments-container"></div><div id="comment-tools-62335" class="comment-tools"></div><div class="clear"></div><div id="comment-62335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62350"></span>

<div id="answer-container-62350" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62350-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have a 1-character typo, namely the percent (<code>%</code>) after the last <code>date</code> should be a colon (<code>:</code>), i.e. you need to change this:</p><pre><code>C:\Program Files\Wireshark&gt;Tshark -i rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5896D29} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -w C:\APP01%date:~4,2%%date:~7,2%%date%~10,4%.pcap</code></pre><p>to this:</p><pre><code>C:\Program Files\Wireshark&gt;Tshark -i rpcap://[172.16.254.6]/\Device\NPF_{CF9CFF46-79FF-4A97-802A-F6CEF5896D29} -f &quot;tcp[20:4]=0x383D4649 and tcp[24:1]=0x58&quot; -w C:\APP01%date:~4,2%%date:~7,2%%date:~10,4%.pcap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62350" class="comments-container"></div><div id="comment-tools-62350" class="comment-tools"></div><div class="clear"></div><div id="comment-62350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

