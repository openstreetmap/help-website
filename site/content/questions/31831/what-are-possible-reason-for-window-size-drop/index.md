+++
type = "question"
title = "What are possible reason for window size drop"
description = '''hi ,  I am seeing data dips in my device . When i analyse from wireshark i can see that there is a drop in the tcp window frequently . What are the possible reason for the tcp window size dropped ? My set up and results :  1. I am using android JB and testing in private network :   In Browser (Chrom...'''
date = "2014-04-15T01:48:00Z"
lastmod = "2014-04-15T03:27:00Z"
weight = 31831
keywords = [ "android", "throughput", "dropped", "tcpwindowsize" ]
aliases = [ "/questions/31831" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What are possible reason for window size drop](/questions/31831/what-are-possible-reason-for-window-size-drop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31831-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi ,<br />
I am seeing <strong>data dips</strong> in my device . When i analyse from wireshark i can see that there is a <strong>drop in the tcp window</strong> frequently . What are the possible <strong>reason for the tcp window size dropped</strong> ?<br />
<br />
<br />
My set up and results :<br />
1. I am using android JB and testing in private network :</p><ul><li>In Browser (Chrome and android native browser) i find window size being dropped</li><li>In iperf (running my device as server ie iperf -s to make it download data) there is no size drop .<br />
</li></ul>2. In Kitkat There is a drop . But <strong>not as much as that of JB</strong> os .<p>Regards, Madhan</p></div><div id="question-tags" class="tags-container tags">android throughput dropped tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '14, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/5cc66aa833a55d252d14fcafde02af36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madhan&#39;s gravatar image" /><p>Madhan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madhan has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '14, 01:49</p></div></div><div id="comments-container-31831" class="comments-container"></div><div id="comment-tools-31831" class="comment-tools"></div><div class="clear"></div><div id="comment-31831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31836"></span>

<div id="answer-container-31836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31836-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What are the possible reason for the tcp window size dropped ?</p></blockquote><p>to sum it up</p><ul><li>packet loss</li><li>inability of the receiver to process the data fast enough</li><li>bug in the software</li><li>other things (like solar particles flipping the wrong bit in the TCP header)</li></ul><p>If those <strong>tcp window drops</strong> are a problem in your environment, depends on</p><ul><li>how large the window size gets changed and how fast</li><li>how often it appears</li></ul><p>If there is a clear difference between JB and KitKat, I tend to say: Could be a bug in android ...</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-31836" class="comments-container"><span id="31837"></span><div id="comment-31837" class="comment"><div id="post-31837-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply . But if that is the case i must be seein the problem in perf also . But iperf i dont see any issue . (may be it uses fixed window size or set some max value)</p><blockquote><blockquote><p>how large the window size gets changed and how fast <strong>can u tell me the kernel parameter which would increase the window size ?</strong> so that i can check from the JB and KK kernel .</p><p>how often it appears ? it is in regular interval . when i draw a I/O grap using tcp.window_size i get a graph similar to sin curve(kinda)</p></blockquote></blockquote></div><div id="comment-31837-info" class="comment-info"><span class="comment-age">(15 Apr '14, 04:35)</span> Madhan</div></div><span id="31841"></span><div id="comment-31841" class="comment"><div id="post-31841-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But if that is the case i must be seein the problem in perf</p></blockquote><p>if you run iperf on the same Android device, then it could be a problem within the web client 'library' (the part that is used by the browser/os to create/send/receive HTTP requests). If that is the case, iperf would not be affected, as iperf is calling the kernels socket api directly. However, that's all just speculation, as it's only one possible cause for the problem.</p><blockquote><p>can u tell me the kernel parameter which would increase the window size ?</p></blockquote><p>I have no knowledge about the android TCP/IP stack internals. So, there might or might not be such a parameter. Please ask google.</p><blockquote><p>when i draw a I/O grap using tcp.window_size i get a graph similar to sin curve(kinda)</p></blockquote><p>can you post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-31841-info" class="comment-info"><span class="comment-age">(15 Apr '14, 06:58)</span> Kurt Knochner ♦</div></div><span id="32046"></span><div id="comment-32046" class="comment"><div id="post-32046-score" class="comment-score"></div><div class="comment-text"><p>web client 'library'<br />
<strong>Can u tell me exactly which library would be impacting ? so that i can check that .</strong></p></div><div id="comment-32046-info" class="comment-info"><span class="comment-age">(21 Apr '14, 22:50)</span> Madhan</div></div><span id="32047"></span><div id="comment-32047" class="comment"><div id="post-32047-score" class="comment-score"></div><div class="comment-text"><p>I don't know, maybe HttpClient. Please ask the Android folks.</p><blockquote><p><a href="http://developer.android.com/reference/org/apache/http/client/HttpClient.html">http://developer.android.com/reference/org/apache/http/client/HttpClient.html</a></p></blockquote></div><div id="comment-32047-info" class="comment-info"><span class="comment-age">(22 Apr '14, 01:15)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31836" class="comment-tools"></div><div class="clear"></div><div id="comment-31836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

