+++
type = "question"
title = "Understanding two pass analysis with tshark"
description = '''I am trying to understand 2 pass analysis with tshark using the latest 1.10.2 (TShark 1.10.2 (SVN Rev 51377 from /trunk-1.10)) The first example starts with a single pass. I use the &quot;-c 1&quot; option to only display a single packet. I am also using a display filter to see packets with frame numbers &amp;gt;...'''
date = "2013-08-15T10:22:00Z"
lastmod = "2013-08-15T13:10:00Z"
weight = 23804
keywords = [ "tshark" ]
aliases = [ "/questions/23804" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Understanding two pass analysis with tshark](/questions/23804/understanding-two-pass-analysis-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23804-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to understand 2 pass analysis with tshark using the latest 1.10.2 (TShark 1.10.2 (SVN Rev 51377 from /trunk-1.10))</p><p>The first example starts with a single pass. I use the "-c 1" option to only display a single packet. I am also using a display filter to see packets with frame numbers &gt; 1. The result makes sense. I see frame #2.</p><pre><code>[email protected]:~/lab2/wireshark-1.10-trunk$ ./tshark -r dns.cap -c 1 -Y &quot;frame.number&gt;1&quot;
  2   0.000269   172.16.1.1 -&gt; 172.16.1.198 DNS 84 Standard query response 0xc576  A 10.0.0.101</code></pre><p>However, once I switch this to a two pass using "-2", I don't see any packets displayed.</p><pre><code>[email protected]:~/lab2/wireshark-1.10-trunk$ ./tshark -r dns.cap -2 -c 1 -Y &quot;frame.number&gt;1&quot;
[email protected]:~/lab2/wireshark-1.10-trunk$ </code></pre><p>I would not expect the results to change when I switch to a two pass decode. I suspect this is a bug, but I want to confirm the expected behavior.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '13, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/9681c8a3b1c4620c300ab9e3fdce439b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joemc&#39;s gravatar image" /><p>joemc<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joemc has no accepted answers">0%</span></p></div></div><div id="comments-container-23804" class="comments-container"></div><div id="comment-tools-23804" class="comment-tools"></div><div class="clear"></div><div id="comment-23804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23805"></span>

<div id="answer-container-23805" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23805-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>AFAICT (without looking at the source code), both '-c' and '-R' work on the first pass. During the first pass all packets are read and full dissection is done to calculate all the fields. Only frames that pass the filter in the '-R' option will be kept for the second pass. When the amount of packets that pass the filter in the '-R' option reach the number in the '-c' option, reading of the capture file is stopped.</p><p>Then on the second pass, only packets that matched the first pass are examined (with their full dissection intact) and matched against the filter in the '-Y' option. Matching packets will be printed.</p><p>It looks like frame numbers are re-calculated on the second run:</p><pre><code>[email protected]:~$ tshark -r ~/Wireshark/pcap/http.cap -c 2 -Y &#39;tcp.len&gt;0&#39;
  4   0.056589 192.168.1.43 -&gt; 66.102.13.103 HTTP 715 GET / HTTP/1.1 
  6   0.122335 66.102.13.103 -&gt; 192.168.1.43 TCP 1278 [TCP segment of a reassembled PDU]
[email protected]:~$ tshark -r ~/Wireshark/pcap/http.cap -c 2 -2 -Y &#39;tcp.len&gt;0&#39;
[email protected]:~$ tshark -r ~/Wireshark/pcap/http.cap -c 2 -2 -R &#39;tcp.len&gt;0&#39; -Y &#39;tcp.len&gt;0&#39;
  1   0.056589 192.168.1.43 -&gt; 66.102.13.103 HTTP 715 GET / HTTP/1.1 
  2   0.122335 66.102.13.103 -&gt; 192.168.1.43 TCP 1278 [TCP segment of a reassembled PDU]
[email protected]:~$</code></pre><p>Which I would consider a bug. Could you file a bug report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> with a link to this question?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '13, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23805" class="comments-container"><span id="23822"></span><div id="comment-23822" class="comment"><div id="post-23822-score" class="comment-score"></div><div class="comment-text"><p>This has been filed as wireshark bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9048">9048</a>.</p></div><div id="comment-23822-info" class="comment-info"><span class="comment-age">(16 Aug '13, 09:32)</span> joemc</div></div></div><div id="comment-tools-23805" class="comment-tools"></div><div class="clear"></div><div id="comment-23805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

