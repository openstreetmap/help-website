+++
type = "question"
title = "Issue about crawl HTTP"
description = '''I met a problem while using wireshark, which was that i only wanted to crawl the data package of HTTP by setting a filter, but when i input HTTP in filtering condition as setting the network card, why it showed red meaning the setting was wrong, but input TCP etc. , it showed right. please tell me w...'''
date = "2012-12-20T22:52:00Z"
lastmod = "2012-12-20T23:23:00Z"
weight = 17118
keywords = [ "http" ]
aliases = [ "/questions/17118" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Issue about crawl HTTP](/questions/17118/issue-about-crawl-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17118-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I met a problem while using wireshark, which was that i only wanted to crawl the data package of HTTP by setting a filter, but when i input HTTP in filtering condition as setting the network card, why it showed red meaning the setting was wrong, but input TCP etc. , it showed right. please tell me what is the reason. Though filtering condition can be set to be tcp port 80, it can only crawl the HTTP passed the 80 port. If some HTTP do not pass the 80 part, how to crawl it?</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '12, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/52c284b06d387ac702f48ee644e6f442?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jun&#39;s gravatar image" /><p>jun<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Dec '12, 23:07</p></div></div><div id="comments-container-17118" class="comments-container"></div><div id="comment-tools-17118" class="comment-tools"></div><div class="clear"></div><div id="comment-17118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17120"></span>

<div id="answer-container-17120" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17120-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it showed right. please tell me what is the reason.</p></blockquote><p>the reason is already explained in your <a href="http://ask.wireshark.org/questions/17001/crawl-http-protocol-http">other question</a> with the same content. I'll repeat it for you:</p><p>You cannot use <strong>http</strong> as a capture filter, as that is not valid libpcap filter syntax. whereas <strong>tcp</strong> is a valid filter.</p><p>See here: <a href="http://www.manpagez.com/man/7/pcap-filter/">http://www.manpagez.com/man/7/pcap-filter/</a></p><p>Please use this filter instead: <strong><code>tcp port 80</code></strong></p><blockquote><p>Though filtering condition can be set to be tcp port 80, it can only gain the HTTP protocol passed the 80 port. If some HTTP protocol do not pass the 80 part, how to gain it?</p></blockquote><p>Wireshark needs a criteria to identify a protocol <strong>during the capture phase</strong>. That criteria is usually the protocol and the port (80, 3128, 8080, etc.). So, if you want to capture HTTP with libpcap, regardless of the port, you can only try to identify the usual HTTP request commands in the tcp payload.</p><p>Looking for 'GET ' in the payload:<br />
</p><blockquote><p><code>tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420</code><br />
</p></blockquote><p>Looking for 'POST' in the payload:<br />
</p><blockquote><p><code>tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x504F5354</code><br />
</p></blockquote><p>Explanation:</p><ul><li>((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) represents the length of the tcp header</li><li>tcp[header_length:4] = 0x47455420 looks for 4 bytes in the tcp packet, beginning at the end of the header. Those 4 bytes are compared to the ASCII representation of 'GET '.</li></ul><p>So, if you want to look for all HTTP commands, you need to combine several of these filters.</p><blockquote><p><code>tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420 or tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x504F5354 or xxxxx</code></p></blockquote><p>Replace <strong>xxxxx</strong> with the filters for HEAD and other HTTP commands.</p><p><strong>IMPORTANT</strong>: There are some problems</p><p>the <strong>most important</strong> problem<br />
</p><ul><li>with the filters shown above, you will <strong>only</strong> capture packets that contain the HTTP requests. As your are interested in the HTTP payload, this method does not work for you.</li></ul><p>other problems<br />
</p><ul><li>Some HTTP implementations accept 'get' or 'Get' instead of 'GET', so you will probably miss some HTTP requests, unless you add filters for all possible lowercase/uppercase combinations.</li><li>You will get false positives, if the strings 'GET', 'POST', 'HEAD', etc. happen to be at the beginning of the TCP payload (e.g. as part of a text file that is transferred via ftp).</li><li>You may get performance problems, if you need to capture at high packet rates</li></ul><p>So, if you need the whole HTTP payload for all HTTP connections, regardless of the port, you cannot do that with libpcap filters (Wireshark capture filters). So, you can only capture all data and later use display filters to extract only HTTP sessions.</p><p>A possible alternative would be one of these commands:</p><blockquote><p><code>tshark -ni 0 -R "http" -V</code><br />
<code>tshark -ni 0 -R "http" -T pdml</code><br />
</p></blockquote><p>However, you cannot write that data into a pcap file (-w not supported together with -R), so you need to analyze the output of tshark with other tools than Wireshark.</p><p><strong>HINT</strong>: tshark will also <strong>not detect</strong> HTTP on ports other than the default port list of the HTTP dissector: 80,3128,3132,5985,8080,8088,11371,1900,2869 !!</p><p>If you tell us more about your plans (why do you need to capture HTTP payload (regardless of the port), we might be find a different solution.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '12, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Dec '12, 10:45</p></div></div><div id="comments-container-17120" class="comments-container"></div><div id="comment-tools-17120" class="comment-tools"></div><div class="clear"></div><div id="comment-17120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

