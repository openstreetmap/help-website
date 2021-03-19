+++
type = "question"
title = "ICMP Checksum."
description = '''Hi all, I need your help, I&#x27;m trying to calculate checksum on icmp packet type 8 ( Ping ) but I can&#x27;t obtain checksum value, how i can do it? what is the value of data field? I have this values, you can check the print, I hope you can help me. type 8--8_bits; codigo 0--8_bits; id_be 1 --- 16 bits; i...'''
date = "2012-05-16T12:18:00Z"
lastmod = "2012-05-16T13:34:00Z"
weight = 11061
keywords = [ "checksum" ]
aliases = [ "/questions/11061" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [ICMP Checksum.](/questions/11061/icmp-checksum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11061-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I need your help, I'm trying to calculate checksum on icmp packet type 8 ( Ping ) but I can't obtain checksum value, how i can do it? what is the value of data field?</p><p>I have this values, you can check the print, I hope you can help me.</p><p>type 8--8_bits; codigo 0--8_bits; id_be 1 --- 16 bits; id_le 256 --16bits; Se_be 4104---16 bits; Se_le 2064 16 bits data ?????<br />
checksum is 0x3d53</p><p>0000</p><p>0001<br />
0256<br />
2064<br />
4104<br />
2064<br />
---&gt; data value????? then complement 1.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/icmp_checksum.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">checksum</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/917f6c4ca3412b5be65c51e4b90a2be5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blackfredy&#39;s gravatar image" /><p>blackfredy<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blackfredy has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-11061" class="comments-container"></div><div id="comment-tools-11061" class="comment-tools"></div><div class="clear"></div><div id="comment-11061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11063"></span>

<div id="answer-container-11063" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11063-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://tools.ietf.org/html/rfc792">RFC 792</a>:</p><pre><code>Checksum

  The checksum is the 16-bit ones&#39;s complement of the one&#39;s
  complement sum of the ICMP message starting with the ICMP Type.
  For computing the checksum , the checksum field should be zero.
  If the total length is odd, the received data is padded with one
  octet of zeros for computing the checksum.  This checksum may be
  replaced in the future.</code></pre><p>So you have to split the ICMP header + payload (data) into 16 bit words (using 0x0000 for the checksum field) like this:</p><pre><code>0x0800
0x0000
0x0001
0x1008
0x6162
0x6364
0x6566
0x6768
0x696a
0x6b6c
0x6d6e
0x6f70
0x7172
0x7374
0x7576
0x7761
0x6263
0x6465
0x6667
0x6869</code></pre><p>Then calculate the <a href="http://en.wikipedia.org/wiki/Ones%27_complement">one's complement sum</a> of the first two words and then repeatedly calculate the one's complement sum of the result and the next 16 bit word until you reach 0x6869. At last, calculate the one's complement by inverting all bits.</p><p>(Also have a look at <a href="http://www.ietf.org/rfc/rfc1071.txt">RFC 1071: Computing the Internet Checksum</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-11063" class="comments-container"><span id="11067"></span><div id="comment-11067" class="comment"><div id="post-11067-score" class="comment-score"></div><div class="comment-text"><p>Hey!!!</p><p>You go it!!! i calculate and the result is 49836, i do the complement ( 65535-49836 = 15699 ) and get the answer!!!!, I have to calculate using more types on icmp, if a need help a will write again.</p><p>Thanks thanks in advance!!!</p><p>Bye.</p></div><div id="comment-11067-info" class="comment-info"><span class="comment-age">(16 May '12, 14:56)</span> blackfredy</div></div><span id="11069"></span><div id="comment-11069" class="comment"><div id="post-11069-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", as that's the way this site works best, please see the FAQ)</p></div><div id="comment-11069-info" class="comment-info"><span class="comment-age">(16 May '12, 14:59)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-11063" class="comment-tools"></div><div class="clear"></div><div id="comment-11063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

