+++
type = "question"
title = "Generating TSHARK decoded output from TCPDUMP PCAP file ? without tshark"
description = '''Hello, I would like to convert tcpdump output into tshark standard decoded output. As you know tcpdump don&#x27;t summarize gathered data just like tshark does it.  That&#x27;s too bad, because there are so many doubled values in the pcap file: for example: ipsrc,port,ipdest,port,data_sent 10.38.39.245,1267,1...'''
date = "2012-09-19T05:36:00Z"
lastmod = "2012-09-20T23:35:00Z"
weight = 14376
keywords = [ "decoded", "parsing", "tcpdump", "tshark", "perl" ]
aliases = [ "/questions/14376" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Generating TSHARK decoded output from TCPDUMP PCAP file ? without tshark](/questions/14376/generating-tshark-decoded-output-from-tcpdump-pcap-file-without-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14376-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to convert tcpdump output into tshark standard decoded output. As you know tcpdump don't summarize gathered data just like tshark does it. That's too bad, because there are so many doubled values in the pcap file: for example:<br />
ipsrc,port,ipdest,port,data_sent<br />
10.38.39.245,1267,10.238.125.83,9999,0<br />
10.38.39.245,1267,10.238.125.83,9999,116<br />
10.227.40.61,2491,10.238.125.83,9999,0<br />
</p><p>I would like to have decoded output, similiar to this from t-shark<br />
TSHARK:<br />
10.238.125.83:9999 &lt;-&gt; 10.197.118.246:4412 276 29298 0 0 276 29298 42.208780000 1755.1373<br />
10.39.0.144:55296 &lt;-&gt; 10.238.125.83:9999 0 0 205 22974 205 22974 40.616219000 1746.5140<br />
10.238.125.83:9999 &lt;-&gt; 10.99.156.29:1075 199 20184 0 0 199 20184 2.779606000 1784.9520<br />
10.238.125.83:9999 &lt;-&gt; 10.99.176.220:1226 198 20412 0 0 198 20412 14.735165000 1781.4088<br />
<br />
I've found some information on this site: <a href="http://hype-free.blogspot.fr/2010/03/parsing-pcap-files-with-perl.html">http://hype-free.blogspot.fr/2010/03/parsing-pcap-files-with-perl.html</a><br />
</p><p>It does job well, however i'm having doubled lines, however it's the same connection:<br />
10.197.191.250:445 10.197.191.50:47766 778663<br />
10.197.191.50:47766 10.197.191.250:445 739008<br />
<br />
Have you ever managed to do this correctly in Perl?<br />
</p></div><div id="question-tags" class="tags-container tags">decoded parsing tcpdump tshark perl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '12, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/3cb8c867874b2dc19c6ef111d9458b08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cps86&#39;s gravatar image" /><p>cps86<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cps86 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-14376" class="comments-container"></div><div id="comment-tools-14376" class="comment-tools"></div><div class="clear"></div><div id="comment-14376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14416"></span>

<div id="answer-container-14416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14416-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The beauty of writing a script to do some work for you is that you can make it do exactly what YOU want. It is quite easy to extend the script that you are referring to, to make is combine both flows of the TCP session into one output line. I have done so in the past...</p><p>Hmmm... looking at the script you are referring to, it should not produce the output you are showing. Did you alter the script to your needs already? You can use a conversation index based on IP addresses and ports, and determine the direction of traffic by swapping the src and dst if the dst port is higher than the src port. Just a suggestion...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '12, 23:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-14416" class="comments-container"></div><div id="comment-tools-14416" class="comment-tools"></div><div class="clear"></div><div id="comment-14416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

