+++
type = "question"
title = "tshark commands -e and -T"
description = '''I want to print the information that I need of a PCAP file. I know that I can use the command &quot;tshark -e&quot;: tshark -r rdpcap.pcap -e ip.src -e ip.dst -e data -e frame.number -T fields  My question is: How can I display the &quot;id source port&quot;, &quot;id destination port&quot;? And for &quot;-e data&quot;, is it possible to ...'''
date = "2012-05-02T08:32:00Z"
lastmod = "2012-05-03T03:59:00Z"
weight = 10605
keywords = [ "tshark" ]
aliases = [ "/questions/10605" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark commands -e and -T](/questions/10605/tshark-commands-e-and-t)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10605-score" class="post-score" title="current number of votes">0</div><span id="post-10605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to print the information that I need of a PCAP file. I know that I can use the command "tshark -e":</p><pre><code>tshark -r rdpcap.pcap -e ip.src -e ip.dst -e data -e frame.number -T fields</code></pre><p>My question is: How can I display the "id source port", "id destination port"?</p><p>And for "-e data", is it possible to display just the first 8 bytes?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '12, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/4ffb36ec4ee25beb69f3e0fa8969c8b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alice&#39;s gravatar image" /><p><span>Alice</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alice has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '12, 14:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10605" class="comments-container"></div><div id="comment-tools-10605" class="comment-tools"></div><div class="clear"></div><div id="comment-10605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10611"></span>

<div id="answer-container-10611" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10611-score" class="post-score" title="current number of votes">1</div><span id="post-10611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you are interested in <code>tcp.srcport</code> and <code>tcp.dstport</code>, so please use this:</p><pre><code>tshark -i 1 -n -e frame.number -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e data -T fields</code></pre><p>If you need the UDP source port, replace <code>tcp</code> with <code>udp</code>, e.g. <code>udp.srcport</code>.</p><blockquote><p>And for "-e data", is it possible to display juste the first 8 bytes?</p></blockquote><p>Unfortunately, this is not possible. However, you can limit the total packet size with editcap, effectively getting only 8 bytes of data, at least in the most cases.</p><h3 id="capture">Capture<br />
</h3><pre><code>tshark -i 1 -n -w http.pcap</code></pre><h3 id="truncate">Truncate<br />
</h3><pre><code>editcap.exe -s62  http.pcap http_truncated.pcap</code></pre><h3 id="print">Print<br />
</h3><pre><code>tshark -i 1 -n -e frame.number -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e data -T fields -r http_truncated.pcap</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '12, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 May '12, 15:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-10611" class="comments-container"><span id="10623"></span><div id="comment-10623" class="comment"><div id="post-10623-score" class="comment-score"></div><div class="comment-text"><p>Thanks you. I tried "-e udp.srcport", that works!! I have another question, that will be so nice if you can help me again. If i want to print the ID, is there something like "-e id.src, -e id.dst" ? I tried this command, but it doesn't work. And for "-e frame.time", i just want to display "Mai 3, 2012 10:00:00", not like "Mai 3, 2012 10:00:00:958252000", can I?</p><p>Regards</p></div><div id="comment-10623-info" class="comment-info"><span class="comment-age">(03 May '12, 00:59)</span> <span class="comment-user userinfo">Alice</span></div></div><span id="10624"></span><div id="comment-10624" class="comment"><div id="post-10624-score" class="comment-score"></div><div class="comment-text"><p>What is the element you are calling "id"? To see (most) of the element names that you can supply to <code>-e</code> open the capture in the Wireshark GUI click on the field you are interested in in the packet tree and the status bar will show you the field name.</p><p>There are a number of other frame.timeXXX fields, you could use but they all display fractional seconds. The format you require doesn't appear to be supported, and the <code>-t</code> and <code>-u</code> parameters don't affect field values.</p></div><div id="comment-10624-info" class="comment-info"><span class="comment-age">(03 May '12, 02:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="10627"></span><div id="comment-10627" class="comment"><div id="post-10627-score" class="comment-score"></div><div class="comment-text"><p>what do you meand by "ID"? Is it the IP ID? If yes, please use -e <a href="http://ip.id">ip.id</a>"</p></div><div id="comment-10627-info" class="comment-info"><span class="comment-age">(03 May '12, 03:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-10611" class="comment-tools"></div><div class="clear"></div><div id="comment-10611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

