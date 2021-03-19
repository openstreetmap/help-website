+++
type = "question"
title = "how to use wireshark to capture packets from standard input"
description = '''In our program (written in Java, run on Windows), we have packets captured on our own device, and send to the Java program via a inner callback. Formerly, we decode these packet by ourselves, but there&#x27;s some performance problem. Now we want to use Wireshark instead. I&#x27;ve found that wireshark can ca...'''
date = "2013-09-28T01:47:00Z"
lastmod = "2013-09-29T09:06:00Z"
weight = 25329
keywords = [ "windows", "cmd", "java", "stdin" ]
aliases = [ "/questions/25329" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use wireshark to capture packets from standard input](/questions/25329/how-to-use-wireshark-to-capture-packets-from-standard-input)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25329-score" class="post-score" title="current number of votes">0</div><span id="post-25329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In our program (written in Java, run on Windows), we have packets captured on our own device, and send to the Java program via a inner callback. Formerly, we decode these packet by ourselves, but there's some performance problem. Now we want to use Wireshark instead. I've found that wireshark can capture packets from standard input, by using the following command line: <code>wireshark -k -i -</code>. But I have no idea how to use it in the cmd prompt in Windows 7. Suppose I have a cap file named test.cap, should I use <code>more test.cap | wireshark -k -i -</code> (just a example, I tried but failed) or something else? Of course, I also want to ask about the usage in Java. Does anyone know about it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-cmd" rel="tag" title="see questions tagged &#39;cmd&#39;">cmd</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-stdin" rel="tag" title="see questions tagged &#39;stdin&#39;">stdin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '13, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/71d3e219254ba00bc22b0a18ef5075e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonybuaa&#39;s gravatar image" /><p><span>tonybuaa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonybuaa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '13, 11:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-25329" class="comments-container"></div><div id="comment-tools-25329" class="comment-tools"></div><div class="clear"></div><div id="comment-25329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25340"></span>

<div id="answer-container-25340" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25340-score" class="post-score" title="current number of votes">0</div><span id="post-25340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>should I use more test.cap | wireshark -k -i - (just a example, I tried but failed)</p></blockquote><p><strong>more</strong> is not a good option, as it seems to modify the binary data.</p><blockquote><p>more dumpfile.pcap &gt; m1.pcap<br />
type dumpfile.pcap &gt; m2.pcap</p></blockquote><p>Then</p><blockquote><p>dir *.pcap</p></blockquote><pre><code>02.05.2012  14:28           191.140 dumpfile.pcap
29.09.2013  17:52           205.844 m1.pcap
29.09.2013  17:52           191.140 m2.pcap</code></pre><p>As you can see, the output of <strong>more</strong> is significantly larger than the original.</p><p>As <strong>type</strong> does <strong>not</strong> modify the binary data, you can pipe the capture file like this</p><blockquote><p>type dumpfile.pcap | wireshark -k -i -</p></blockquote><p>This requires wireshark.exe to be in the search PATH of your environment.</p><blockquote><p>Of course, I also want to ask about the usage in Java. Does anyone know about it?</p></blockquote><p>Spawn a Wireshark process with the parameters <code>-k -i -</code> and let your java program write the captured binary data to STDIN of that process. The data needs to be in libpcap format <strong>not</strong> pcacp-ng (see <a href="http://www.wireshark.org/docs/man-pages/wireshark.html">wireshark man page</a> for option -i).</p><p>Regarding Java, process start and writing to STDIN, please ask google: <a href="http://bit.ly/1biNFfo">java start process write STDIN</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '13, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-25340" class="comments-container"></div><div id="comment-tools-25340" class="comment-tools"></div><div class="clear"></div><div id="comment-25340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

