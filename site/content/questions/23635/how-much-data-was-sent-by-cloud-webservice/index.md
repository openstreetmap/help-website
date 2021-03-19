+++
type = "question"
title = "How much data was sent by cloud webservice?"
description = '''Hi, I am running an HTTP restful data API) using a cloud based solution. I want to verify the data usage i.e. traffic out of the cloud (I am only charged for data sent out from the cloud. No charge you data going into the cloud). The reason I am doing this is that I do not trust the billing data fro...'''
date = "2013-08-08T04:24:00Z"
lastmod = "2013-08-16T03:19:00Z"
weight = 23635
keywords = [ "data", "cloud", "out" ]
aliases = [ "/questions/23635" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How much data was sent by cloud webservice?](/questions/23635/how-much-data-was-sent-by-cloud-webservice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23635-score" class="post-score" title="current number of votes">0</div><span id="post-23635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am running an HTTP restful data API) using a cloud based solution. I want to verify the data usage i.e. traffic out of the cloud (I am only charged for data sent out from the cloud. No charge you data going into the cloud).</p><p>The reason I am doing this is that I do not trust the billing data from the cloud provider.</p><p>So my plan is to use dumpcap to capture all traffic and then analyse the logfiles for a 24h period (the scary bit is that I have four instances serving data and each generate ~15GB of dumpcap logfiles per 24h). This is my capture command: D:\Progra~1\Wireshark\dumpcap -i \Device\NPF_{<strong><em>I/F DETAILS REMOVED</em></strong>} -b filesize:256000 -b files:600 -w c:\Wireshark\packets.cap</p><p>Apart from the quantities of data I am not quite sure how to filter out and only get the traffic going out and in the end get the total GB of data.</p><p>Any advice will be welcome!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-cloud" rel="tag" title="see questions tagged &#39;cloud&#39;">cloud</span> <span class="post-tag tag-link-out" rel="tag" title="see questions tagged &#39;out&#39;">out</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '13, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/04beaa44ff0b2ba8fd2978c3e2ef6533?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="APIshark&#39;s gravatar image" /><p><span>APIshark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="APIshark has no accepted answers">0%</span></p></div></div><div id="comments-container-23635" class="comments-container"></div><div id="comment-tools-23635" class="comment-tools"></div><div class="clear"></div><div id="comment-23635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23636"></span>

<div id="answer-container-23636" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23636-score" class="post-score" title="current number of votes">2</div><span id="post-23636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>Apart from the quantities of data</strong> I am not quite sure <strong>how to filter out and only get the traffic going out</strong> and in the end get the total GB of data.</p></blockquote><p>First of all, I'm not sure if Wireshark is the ideal tool for such an analysis (amount of data, etc.).</p><p>I would probably go a different route if I had to analyze the traffic. Maybe I would enable SNMP on the servers and poll the interface stats (in/out packets and bytes) for a first and rough overview about the amount of data. Maybe the Windows Perfmon tool is also useful.</p><p>Anyway, if you want to do it with Wireshark, you can do it like this.</p><p>Do <strong>not</strong> record the full frame, as that will generate too much data and you don't need the payload, just the information about the length of the frame. Hence, please call dumpcap with the option <code>-s 100</code> (snap length). This will only record the first 100 bytes of a frame, IP/TCP/UDP header + some payload data, just in case...</p><p>After you have finished the capture process, you need a script that walks through all file names and calls tshark with each file. Please use your preferred scripting tool on windows (perl, python, shell, poweshell, etc.).</p><blockquote><p><code>tshark -nr input_0001.pcap -q -z conv,ip &gt; output_0001.txt</code><br />
</p></blockquote><p>The <code>conv</code> module will print the amount of packets <strong>and bytes</strong> in either direction for each IP conversations. Save this output for each pcap file and then parse the output files with a second script to extract the total amount of data sent by your server(s).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23636" class="comments-container"><span id="23796"></span><div id="comment-23796" class="comment"><div id="post-23796-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thank you for the very helpful answer!</p><p>I have collected the data and done what you asked me to do with tshark. I get the following output (not included the last 3 columns and replaced some IP info with x),</p><pre><code>                           |       &lt;-      | |       -&gt;      | |
                           | Frames  Bytes | | Frames  Bytes | |</code></pre><p>168.xx.xx.xx &lt;-&gt; 10.xxx.xxx.26 20418 162450590 168380 229742169<br />
... ...</p><p>So the 10.xxx.xxx.26 address is the web service IP from where I want to calculate outgoing data (it send data to the user) and it appears in both the IP address columns. In the 1st column I look for the .26 address and wherever it appears I sum the data in the 4th (-&gt;) column. Similar for the 2nd column where it appears I sum the data in the 3rd (&lt;-) column.</p><p>Can you please confirm this is correct?</p><p>However since this is a Cloud installation there are several internal private addresses (10.) and a couple of public address where traffic is sent to. None of these count as external chargeable traffic so I am excluding all those by subtracting that data. For example the internal address 10.119.242.129 is receiving traffic from the .26 (web service) so in the 1st column I look for the 10.119.242.129 address and wherever it appears I take the data in the 3rd (&lt;-) column and subtract it from the data I calculated going out (first paragraph above). Similar for the 2nd column where it appears I take the data in the 4th (-&gt;) column.</p><p>The result is very close to what I expected.</p><p>Many thanks! Anders.</p></div><div id="comment-23796-info" class="comment-info"><span class="comment-age">(15 Aug '13, 06:05)</span> <span class="comment-user userinfo">APIshark</span></div></div><span id="23798"></span><div id="comment-23798" class="comment"><div id="post-23798-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Can you please confirm this is correct?</p></blockquote><p>The output of <strong>conv,ip</strong> looks like this (as you have shown in your example).</p><pre><code>       |       &lt;-      | |       -&gt;      | |     Total     |    Relative    |   Duration   |
       | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |
10.1.1.1            &lt;-&gt; 20.1.1.1                150    783843       100         121272     250    905115     0,000000000         9,9971</code></pre><p>So, there are 121272 bytes from 10.1.1.1 -&gt; 20.1.1.1 and 783843 bytes from 20.1.1.1 -&gt; 10.1.1.1. For that conversation, there is a total of 905115 bytes (in any direction).</p><blockquote><p>None of these count as external chargeable traffic so I am excluding all those by subtracting that data.</p></blockquote><p>correct.</p><blockquote><p>The result is very close to what I expected.</p></blockquote><p>good.</p></div><div id="comment-23798-info" class="comment-info"><span class="comment-age">(15 Aug '13, 07:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23819"></span><div id="comment-23819" class="comment"><div id="post-23819-score" class="comment-score"></div><div class="comment-text"><p>Thanks Again! This has been a very useful and interesting exercise.</p></div><div id="comment-23819-info" class="comment-info"><span class="comment-age">(16 Aug '13, 03:15)</span> <span class="comment-user userinfo">APIshark</span></div></div><span id="23820"></span><div id="comment-23820" class="comment"><div id="post-23820-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23820-info" class="comment-info"><span class="comment-age">(16 Aug '13, 03:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23636" class="comment-tools"></div><div class="clear"></div><div id="comment-23636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

