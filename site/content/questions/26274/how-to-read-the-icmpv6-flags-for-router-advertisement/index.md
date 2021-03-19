+++
type = "question"
title = "how to read the icmpv6 flags for router advertisement"
description = '''Hi, I am running a wireshark capture on the LAN cape side i.e 192.168.0.x router side. I am looking for Router advertisement packets . I am running a display filter &quot;icmpv6.type == 134&quot;. I want to read the &#x27;M&#x27;(managed address configuration) bit, &#x27;O&#x27;(other stateful configuration) bit, &#x27;L&#x27; bit and &#x27;A&#x27;...'''
date = "2013-10-21T21:42:00Z"
lastmod = "2013-10-28T07:53:00Z"
weight = 26274
keywords = [ "tshark" ]
aliases = [ "/questions/26274" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to read the icmpv6 flags for router advertisement](/questions/26274/how-to-read-the-icmpv6-flags-for-router-advertisement)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26274-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am running a wireshark capture on the LAN cape side i.e 192.168.0.x router side. I am looking for Router advertisement packets . I am running a display filter "icmpv6.type == 134". I want to read the 'M'(managed address configuration) bit, 'O'(other stateful configuration) bit, 'L' bit and 'A' bit from the captured file.</p><p>I am using Tshark command line as i am doing this for automation and cannot use wireshark GUI for reading these flags.I want to read these flags from the capture file , I am currently using ;</p><p>tshark -r &lt;capturedfile&gt; -R "icmpv6.type == 134" -w &lt;newcapturedfile&gt;</p><p>but it only gives the RA packets but I need to read the boolean flag bits.</p><p>-Gourab Majumdar.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '13, 21:42</strong></p><img src="https://secure.gravatar.com/avatar/35103890f2be63f3116eee2c058265a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gourab%20Majumdar&#39;s gravatar image" /><p>Gourab Majumdar<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gourab Majumdar has no accepted answers">0%</span></p></div></div><div id="comments-container-26274" class="comments-container"></div><div id="comment-tools-26274" class="comment-tools"></div><div class="clear"></div><div id="comment-26274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26465"></span>

<div id="answer-container-26465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26465-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but it only gives the RA packets but I need to read the boolean flag bits.</p></blockquote><p>That's because you wrote the frames (option -w) that matched your filter into a new pcap file.</p><blockquote><p>I want to read the 'M'(managed address configuration) bit, 'O'(other stateful configuration) bit, 'L' bit and 'A' bit from the captured file.</p></blockquote><p>Please try this:</p><blockquote><p>thsark -nr input.pcap -R "icmpv6.type == 134" -T fields -e frame.number -e ipv6.src -e ipv6.dst -e icmpv6.mip6.flag.m -e icmpv6.mip6.flag.o -E header=y -E separator=;</p></blockquote><p>If you need more/other fields (flags), please try to find them here:</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/i/icmpv6.html">http://www.wireshark.org/docs/dfref/i/icmpv6.html</a><br />
<a href="http://www.wireshark.org/docs/dfref/">http://www.wireshark.org/docs/dfref/</a><br />
tshark -G<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26465" class="comments-container"><span id="26497"></span><div id="comment-26497" class="comment"><div id="post-26497-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for the detailed filter. with the filter I am now getting the RA packets with the "M" and "O" flags/bits actually i want to display/read only those packets which are having M=1 and O=1 and not any others. right now I am getting all captures which are having those bits in the flags. I mean all RA packets. i tried the following :</p><p>tshark -nr Ra.pcap -R "icmpv6.type == 134" -T fields -e frame.number -e ipv6.src -e ipv6.dst -e icmpv6.mip6.flag.m==1 -e icmpv6.mip6.flag.o==1 -E header=y -E separator=;</p><p>but it did not work. how can we set the filter so that it reads only those packets which are having the bits SET and not others.</p></div><div id="comment-26497-info" class="comment-info"><span class="comment-age">(28 Oct '13, 19:56)</span> Koushik Gane...</div></div><span id="26500"></span><div id="comment-26500" class="comment"><div id="post-26500-score" class="comment-score"></div><div class="comment-text"><p>The <code>-e</code> switches indicate which fields to include in the output, they aren't filters. To only output those packets with the required flags you'll need to adjust the filter following the <code>-R</code> switch. You should be able to use the expressions you have (incorrectly) used in the <code>-e</code> switches.</p></div><div id="comment-26500-info" class="comment-info"><span class="comment-age">(29 Oct '13, 02:50)</span> grahamb ♦</div></div><span id="26503"></span><div id="comment-26503" class="comment"><div id="post-26503-score" class="comment-score"></div><div class="comment-text"><p>as @grahamb said, please use the following tshark command</p><blockquote><p>thsark -nr input.pcap <strong>-R "icmpv6.mip6.flag.m == 1 or icmpv6.mip6.flag.o == 1"</strong> -T fields -e frame.number -e ipv6.src -e ipv6.dst -e icmpv6.mip6.flag.m -e icmpv6.mip6.flag.o -E header=y -E separator=;</p></blockquote></div><div id="comment-26503-info" class="comment-info"><span class="comment-age">(29 Oct '13, 04:04)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26465" class="comment-tools"></div><div class="clear"></div><div id="comment-26465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

