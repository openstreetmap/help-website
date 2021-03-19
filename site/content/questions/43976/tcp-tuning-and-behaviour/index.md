+++
type = "question"
title = "TCP Tuning and Behaviour"
description = '''I have the following questions about TCP:  Regarding the following two parameters related to TCP connection in sysctl in Linux. Which one of them does the Linux TCP stack consider for the receive window when it establishes a connection:  I. net.ipv4.tcp_rmem II. net.core.rmem_max The first parameter...'''
date = "2015-07-08T10:49:00Z"
lastmod = "2015-07-08T12:27:00Z"
weight = 43976
keywords = [ "tcp", "linux" ]
aliases = [ "/questions/43976" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Tuning and Behaviour](/questions/43976/tcp-tuning-and-behaviour)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43976-score" class="post-score" title="current number of votes">0</div><span id="post-43976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following questions about TCP:</p><ol><li>Regarding the following two parameters related to TCP connection in sysctl in Linux. Which one of them does the Linux TCP stack consider for the receive window when it establishes a connection:</li></ol><p>I. net.ipv4.tcp_rmem</p><p>II. net.core.rmem_max</p><p>The first parameter contains 3 values (Min, Default and Max). Whereas the second one contains only one value.</p><ol><li><p>Additionally how does TCP calculate the initial MSS during the Handshake? My initial guess is TCP considers the MTU and it subtracts the TCP/IP/LLC Headers Length, is it correct?</p></li><li><p>Does the two ends agree on one MSS to use during the handshake? Or each side can his own MSS?</p></li><li><p>What would be the reason behind having only one congestion control in the Linux Kernel? i.e when I execute the following command:</p><p>sysctl .net.ipv4.tcp_available_congestion_control</p></li></ol><p>I only get reno. Even-though I have Linux Kernel 3.14.0 , should not I get Cubic too? Or do I need to have specific configuration while compiling the Kernel?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '15, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/566cfe38b17a31f0dc825c86538cf3d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hany%20Assasa&#39;s gravatar image" /><p><span>Hany Assasa</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hany Assasa has no accepted answers">0%</span></p></div></div><div id="comments-container-43976" class="comments-container"></div><div id="comment-tools-43976" class="comment-tools"></div><div class="clear"></div><div id="comment-43976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43978"></span>

<div id="answer-container-43978" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43978-score" class="post-score" title="current number of votes">3</div><span id="post-43978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hany Assasa has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.psc.edu/index.php/networking/641-tcp-tune">http://www.psc.edu/index.php/networking/641-tcp-tune</a> explains that TCP Autotuning automatically adjusts socket buffer sizes as needed to optimally balance TCP performance and memory usage... Autotuning is now enabled by default in current Linux releases (after 2.6.6 and 2.4.16).</p><p>net.core.rmem_max defines the TCP max buffer size that and application can set using setsockopt()</p><p>net.ipv4.tcp_rmem define the Linux autotuning TCP buffer limits min, default, and max number of bytes</p><hr /><p>Let me start with 3)</p><p>If the desired algorithm is not yet available the following command can be used to see which algorithms are installed:</p><pre><code>ls /lib/modules/`uname -r`/kernel/net/ipv4/tcp_*.ko</code></pre><p>and you can issue a modprobe command to activate those</p><pre><code>sudo modprobe tcp_westwood</code></pre><hr /><p>2) Does the two ends agree on one MSS to use during the handshake? Or each side can his own MSS?</p><p>Each side has has its own MSS that it offers in its SYN packet, it is based on the MTU size of the route towards the destination and tries to avoid ip fragmentation by substracting 40 bytes.<br />
The sender remembers the incoming SYN's MSS and should not exceed the segment size when sending data. Not necessarily do both MSS values have to match but they better do ...</p><hr /><p>1) As per <a href="http://www.cdnplanet.com/blog/tune-tcp-initcwnd-for-optimum-performance/">http://www.cdnplanet.com/blog/tune-tcp-initcwnd-for-optimum-performance/</a><br />
Linux kernel 2.6 offers 3xMSS typically 5840 bytes in its initial rwin offering<br />
Linux kernel 3.0 offers 10xMSS typically 14600 bytes.</p><p>If TCP timestamp option was negotiated you will see 10X1448 or 3X1448 bytes ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '15, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '15, 12:14</strong> </span></p></div></div><div id="comments-container-43978" class="comments-container"><span id="43980"></span><div id="comment-43980" class="comment"><div id="post-43980-score" class="comment-score"></div><div class="comment-text"><p>Valueable links, thanks <span></span><span>@mrEEde</span></p></div><div id="comment-43980-info" class="comment-info"><span class="comment-age">(08 Jul '15, 12:27)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-43978" class="comment-tools"></div><div class="clear"></div><div id="comment-43978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

