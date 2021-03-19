+++
type = "question"
title = "ISDN HEX capture analyze"
description = '''I have a Hex Dump of ISDN messages and I wonder if Wireshark can be used to decode those messages. Here an example of what I have: 0000 02 01 01 a5  0000 02 01 01 b9  0000 02 01 01 a5  0000 02 01 01 b9  0000 00 01 a4 b8 08 02 00 3e 05 04 03 80 90 a2 18 03  0010 a9 83 85 6c 0c 21 80 38 30 31 38 30 32...'''
date = "2011-09-23T09:01:00Z"
lastmod = "2011-09-23T10:01:00Z"
weight = 6516
keywords = [ "decode", "hexdump", "messages", "isdn" ]
aliases = [ "/questions/6516" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [ISDN HEX capture analyze](/questions/6516/isdn-hex-capture-analyze)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6516-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Hex Dump of ISDN messages and I wonder if Wireshark can be used to decode those messages. Here an example of what I have:</p><pre><code>0000  02 01 01 a5                                          
0000  02 01 01 b9                                          
0000  02 01 01 a5                                          
0000  02 01 01 b9                                          
0000  00 01 a4 b8 08 02 00 3e 05 04 03 80 90 a2 18 03   
0010  a9 83 85 6c 0c 21 80 38 30 31 38 30 32 33 30 30   
0020  30 70 08 c1 33 37 33 39 31 32 30                   
0000  00 01 01 a6                                          
0000  02 01 b8 a6 08 02 80 3e 02 18 03 a9 83 85         
0000  02 01 01 ba                                          
0000  02 01 ba a6 08 02 80 3e 01 1e 02 82 88            
0000  02 01 01 bc                                          
0000  02 01 bc a6 08 02 80 3e 07                         
0000  02 01 01 be                                          
0000  00 01 a6 be 08 02 00 3e 0f                         
0000  00 01 01 a8                                          
0000  00 01 a8 be 08 02 00 3e 45 08 02 8a 90            
0000  00 01 01 aa                                          
0000  02 01 be aa 08 02 80 3e 4d                         
0000  02 01 01 c0                                          
0000  00 01 aa c0 08 02 00 3e 5a                         
0000  00 01 01 ac                                          
0000  02 01 01 ad                                          
0000  02 01 01 c1                                          
0000  02 01 01 ad                                          
0000  02 01 01 c1</code></pre><p>I've try to use text2cap command but wireshark couldn't decode the ISDN messages. The command used was text2pcap.exe -s 273,819,1 TXT.file CAP.file<br />
</p><p>Is there a way to make it work ?</p><p>Thank you</p><p>Marcelo</p></div><div id="question-tags" class="tags-container tags">decode hexdump messages isdn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '11, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/674fc356c92d4c00c0089d9b3a104e67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MOVnet&#39;s gravatar image" /><p>MOVnet<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MOVnet has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-6516" class="comments-container"></div><div id="comment-tools-6516" class="comment-tools"></div><div class="clear"></div><div id="comment-6516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6518"></span>

<div id="answer-container-6518" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6518-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to specify a data link type of 203 (see <a href="https://github.com/mcr/libpcap/blob/master/pcap/bpf.h">pcap/bpf.h</a>). Try <code>text2pcap -l 203 file.txt file.pcap</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6518" class="comments-container"><span id="6522"></span><div id="comment-6522" class="comment"><div id="post-6522-score" class="comment-score"></div><div class="comment-text"><p>Great! Problem solved! <strong>Thank you very much !</strong></p></div><div id="comment-6522-info" class="comment-info"><span class="comment-age">(23 Sep '11, 11:46)</span> MOVnet</div></div></div><div id="comment-tools-6518" class="comment-tools"></div><div class="clear"></div><div id="comment-6518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

