+++
type = "question"
title = "TCP Stream output in Pdml format"
description = '''Hi, I use tshark to get tcp stream in ascii format by using tshark -r read.pcap -z follow,tcp,stream,1 -q I want to output the the http request and response in pdml format. (or in xml format) like &amp;lt;conn srcip=&quot;0.0.0.0&quot; dstip=&quot;0.0.0.0&quot;/&amp;gt;&amp;lt;msg proto=&quot;http&quot;&amp;gt;&amp;lt;field method=&quot;&quot;&amp;gt; and so on....'''
date = "2012-12-05T06:42:00Z"
lastmod = "2012-12-05T11:59:00Z"
weight = 16592
keywords = [ "follow", "tcp.stream", "follow.tcp.stream", "pdml" ]
aliases = [ "/questions/16592" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Stream output in Pdml format](/questions/16592/tcp-stream-output-in-pdml-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16592-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I use tshark to get tcp stream in ascii format by using tshark -r read.pcap -z follow,tcp,stream,1 -q I want to output the the http request and response in pdml format. (or in xml format) like &lt;conn srcip="0.0.0.0" dstip="0.0.0.0"/&gt;&lt;msg proto="http"&gt;&lt;field method=""&gt; and so on.</p><p>Can any one help me how to access the code of tshark to output the protocol tree while following the tcp stream?<br />
</p></div><div id="question-tags" class="tags-container tags">follow tcp.stream follow.tcp.stream pdml</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/678147d096482ad76cd3350a3b9c7367?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leaguer&#39;s gravatar image" /><p>Leaguer<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leaguer has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-16592" class="comments-container"></div><div id="comment-tools-16592" class="comment-tools"></div><div class="clear"></div><div id="comment-16592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16610"></span>

<div id="answer-container-16610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16610-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can any one help me how to access the code of tshark to output the protocol tree while following the tcp stream?</p></blockquote><p>By using the option <code>-z follow,tcp,hex,1</code> tshark will just walk trough the capture file and it will collect the whole payload data of the given stream (using a TAP function). At the end of the capture file, tshark will output the collected data in a predefined form. So, there is no PDML involved while using the follow stats option. If you add the option <code>-q</code> it will not even show the packet summary for each packet it processes.</p><p>So, if you need PDML output of stream 1, I suggest to use this:</p><blockquote><p><code>tshark -nr input.cap -T pdml -R "tcp.stream == 1"</code><br />
</p></blockquote><p>This will output every packet of that stream #1 in PDML format, <strong>including</strong> the payload data (field name="tcp.data"). So, you will get the PDML output, <strong>and</strong> if you need the same output that <code>follow,tcp</code> produces, you can have that as well, by extracting the payload data from the "tcp.data" field (unless, there is packet reordering).</p><p>Does that help?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16610" class="comments-container"><span id="16859"></span><div id="comment-16859" class="comment"><div id="post-16859-score" class="comment-score"></div><div class="comment-text"><p>Following the above discussion. It is not helpful in case of chunked http response (e.g., executable in data). From pdml it requires to do all the reordering and reassembly. I was wondering if I can have full protocol request and response (with one data) in pdml format, for one stream. It seems with current configuration it is not possible. Any suggestions for assembling the tcp stream from pdml output? Thanks</p></div><div id="comment-16859-info" class="comment-info"><span class="comment-age">(13 Dec '12, 21:33)</span> Leaguer</div></div><span id="16879"></span><div id="comment-16879" class="comment"><div id="post-16879-score" class="comment-score"></div><div class="comment-text"><p>Well, then I suggest to use another tool, like tcpflow. See my answers to the following questions. The output is not in PDML, but easy to parse.</p><blockquote><p><code>http://ask.wireshark.org/questions/14811/follow-tcp-stream-with-tshark-still-can-not-in-batch-mode</code><br />
<code>http://ask.wireshark.org/questions/16690/split-pcap-file-into-smaller-pcap-file-according-to-tcp-flow</code></p></blockquote></div><div id="comment-16879-info" class="comment-info"><span class="comment-age">(14 Dec '12, 06:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16610" class="comment-tools"></div><div class="clear"></div><div id="comment-16610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

