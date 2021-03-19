+++
type = "question"
title = "Measuring bandwidth without capture all data"
description = '''Hi,  I&#x27;m new to Wireshark and I want to be able to take the measure of our File Server bandwidth utilisation for a possible move into a remote location. So I want to capture (by port miroring) on a week my file server. For testing purpose I start a capture excluding broadcast and multicast packets, ...'''
date = "2012-06-15T12:31:00Z"
lastmod = "2012-06-16T04:51:00Z"
weight = 11971
keywords = [ "capture", "capture-filter", "data", "file" ]
aliases = [ "/questions/11971" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Measuring bandwidth without capture all data](/questions/11971/measuring-bandwidth-without-capture-all-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11971-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm new to Wireshark and I want to be able to take the measure of our File Server bandwidth utilisation for a possible move into a remote location. So I want to capture (by port miroring) on a week my file server.</p><p>For testing purpose I start a capture excluding broadcast and multicast packets, in files with a 5 minutes rotation for a couples of hour. My problem is that I will rapidly run out of disk space.<br />
</p><p>What is the best way to measure bandwidth without catching all gigabytes and terabytes data exchange on that server ?</p><p>Regards,</p><p>Patrick</p></div><div id="question-tags" class="tags-container tags">capture capture-filter data file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '12, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/7e2ee74f23d4a329dbf6b7c7015f9b55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JimToupet&#39;s gravatar image" /><p>JimToupet<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JimToupet has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11971" class="comments-container"></div><div id="comment-tools-11971" class="comment-tools"></div><div class="clear"></div><div id="comment-11971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11978"></span>

<div id="answer-container-11978" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11978-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should not capture with wireshark or tshark, as they will build internal state while dissecting data.</p><p>I suggest this:</p><ul><li><p>capture with dumpcap and options -b (ring buffer) -s 60 (snaplen set to 60 bytes - only TCP header plus some data). Also limit the capture to the ip address and the port of your file server protocol like this:</p><blockquote><p><code>dumpcap -i &lt;interface&gt; -s 60 -w fileserver.cap -b filesize:200000 -f "host 1.2.3.4 and port 8888"</code></p></blockquote></li><li>You can run this command much longer as you don't capture the payload data</li><li>If you have enough data, analyze the capture files with wireshark. Take a look at: <code>Statistics -&gt; Summary</code> , <code>Statistics -&gt; IO Graph</code> and <code>Statistics -&gt; TCP Stream Graph -&gt; Throughput Graph</code> (the later only if your file server protocol is TCP based). These will show the bandwidth consumption (especially the IO Graphs).</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '12, 01:39</p></div></div><div id="comments-container-11978" class="comments-container"><span id="11994"></span><div id="comment-11994" class="comment"><div id="post-11994-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt and SYN-bit.</p><p>Kurt : I forgot to mention that our file server it's an Novell Netware. In our final step of analysis can we say that the Novell NCP protocol load will be equivalent with the SMB Windows load ? We planned to move the server but we change it too from Netware to Windows.</p><p>SYN-bit : We already have an SNMP traffic capter setup using PRTG Network Monitor. But one of the remote location admin want a capture without "noise" (broadcast and multicast request).</p></div><div id="comment-11994-info" class="comment-info"><span class="comment-age">(16 Jun '12, 07:24)</span> JimToupet</div></div><span id="11995"></span><div id="comment-11995" class="comment"><div id="post-11995-score" class="comment-score"></div><div class="comment-text"><blockquote><p>In our final step of analysis can we say that the Novell NCP protocol load will be equivalent with the SMB Windows load</p></blockquote><p>well, you can differntiate the two protocols in wireshark <strong>however</strong> you need a different capture filter for NCP!</p><p>If you want to know if there will be the same network load after you migrated the server from NCP to SMB. Well, that's a good question. I can't tell you and I don't know a direct comparison of the two protocols regarding performance/bandwidth (which means nothing ;-))</p></div><div id="comment-11995-info" class="comment-info"><span class="comment-age">(16 Jun '12, 07:36)</span> Kurt Knochner ♦</div></div><span id="11997"></span><div id="comment-11997" class="comment"><div id="post-11997-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But one of the remote location admin want a capture without "noise" (broadcast and multicast request).</p></blockquote><p>usually netflow/sflow (whatever your switch/router supports) would help to separate protocols (using PRTG as a flow collector). However, that (possibly) won't work with NCP.</p><p>BTW: Are you using IPX or IP?</p></div><div id="comment-11997-info" class="comment-info"><span class="comment-age">(16 Jun '12, 07:47)</span> Kurt Knochner ♦</div></div><span id="11998"></span><div id="comment-11998" class="comment"><div id="post-11998-score" class="comment-score"></div><div class="comment-text"><p>Regarding the bandwitdh/performance comparison of NCP versus SMB. Maybe you can test yourself. Download a set of identical files with both protocols and compare the results in wireshark. You should at least download 3-5 large files (&gt; 10-20 MByte) and a set of small files (50 x 10-20 Kbyte) to get an idea how both protocols work in different scenarios.</p></div><div id="comment-11998-info" class="comment-info"><span class="comment-age">(16 Jun '12, 08:21)</span> Kurt Knochner ♦</div></div><span id="12020"></span><div id="comment-12020" class="comment"><div id="post-12020-score" class="comment-score"></div><div class="comment-text"><p>We using IP.</p></div><div id="comment-12020-info" class="comment-info"><span class="comment-age">(18 Jun '12, 06:45)</span> JimToupet</div></div><span id="12023"></span><div id="comment-12023" class="comment not_top_scorer"><div id="post-12023-score" class="comment-score"></div><div class="comment-text"><p>In that case, you should consider Netflows. Much easier than any analysis with wireshark!</p></div><div id="comment-12023-info" class="comment-info"><span class="comment-age">(18 Jun '12, 07:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11978" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-11978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11991"></span>

<div id="answer-container-11991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11991-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I wouldn't use wireshark for this task. I would use SNMP to read the port statistics of the switch to which the fileserver is connected (or read the WMI stats from the server itself through SNMP).</p><p>One nice little SNMP tool is <a href="http://leonidvm.chat.ru/">STG</a> (freeware)</p><p>UPDATE: I totally forgot to mention the <a href="http://www.lovemytool.com/blog/2009/12/tiny-tool-tip-1-stg-by-sake-blok.html">blogpost</a> I wrote a while ago on how to use STG.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '12, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '12, 04:53</p></div></div><div id="comments-container-11991" class="comments-container"></div><div id="comment-tools-11991" class="comment-tools"></div><div class="clear"></div><div id="comment-11991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

