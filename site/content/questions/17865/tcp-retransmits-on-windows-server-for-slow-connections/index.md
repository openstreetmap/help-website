+++
type = "question"
title = "TCP Retransmits on Windows Server for slow connections"
description = '''I&#x27;m trying to understand why there are seemingly &#x27;aggressive&#x27; TCP retransmits seen in the capture below: The server is a Windows 2008 R2 server, the client is connecting over a &quot;slow&quot; GPRS or 3G connection. Notice how the server will retransmit packet number 5 after 0.36s and then again after 0.6 se...'''
date = "2013-01-22T12:08:00Z"
lastmod = "2013-01-23T13:21:00Z"
weight = 17865
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/17865" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmits on Windows Server for slow connections](/questions/17865/tcp-retransmits-on-windows-server-for-slow-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17865-score" class="post-score" title="current number of votes">0</div><span id="post-17865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to understand why there are seemingly 'aggressive' TCP retransmits seen in the capture below:</p><p>The server is a Windows 2008 R2 server, the client is connecting over a "slow" GPRS or 3G connection. Notice how the server will retransmit packet number 5 after 0.36s and then again after 0.6 seconds. Doubling the timeout (this seems to be consistent with some logic built into how TCP calculates the retry timeout).</p><p>It's almost as if the server "thinks" the connection is faster then it really is. This pattern continues throughout the session.</p><p>Any thoughts or comments appreciated.</p><p><img src="http://s8.postimage.org/i3f9w4m37/capture2.png" alt="alt text" /></p><p><a href="http://s8.postimage.org/i3f9w4m37/capture2.png" title="Direct link to image">Direct link to image</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/fd4e4f3ad1cfaaa0a05ab88a2589d5fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dodgyrabbit&#39;s gravatar image" /><p><span>Dodgyrabbit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dodgyrabbit has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '13, 08:22</strong> </span></p></div></div><div id="comments-container-17865" class="comments-container"></div><div id="comment-tools-17865" class="comment-tools"></div><div class="clear"></div><div id="comment-17865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="17907"></span>

<div id="answer-container-17907" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17907-score" class="post-score" title="current number of votes">0</div><span id="post-17907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dodgyrabbit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We have found the solution. Windows 2008 R2 has an issue where the RTT is not recalculated under some specific conditions related to SACK and high latency networks. We have confirmed that enabling this setting fixes the problem and RTT is correctly updated, therefore stopping the premature retries:</p><pre><code>netsh interface tcp set global nonsackrttresiliency=enabled</code></pre><blockquote><p>TCP packets sent from Windows Server 2008 R2 are retransmitted when SACK is disabled on the client computer</p></blockquote><p><a href="http://support.microsoft.com/kb/2764305">KB 2764305</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '13, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/fd4e4f3ad1cfaaa0a05ab88a2589d5fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dodgyrabbit&#39;s gravatar image" /><p><span>Dodgyrabbit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dodgyrabbit has one accepted answer">100%</span></p></div></div><div id="comments-container-17907" class="comments-container"></div><div id="comment-tools-17907" class="comment-tools"></div><div class="clear"></div><div id="comment-17907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17866"></span>

<div id="answer-container-17866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17866-score" class="post-score" title="current number of votes">0</div><span id="post-17866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Slow connection" is a bit of a nice way putting it... it is crawling with hands and knees on a floor pasted with sticky tar - the RTT is almost 1 (in words: one) second :-)</p><p>I guess the server really gets impatient after a while in packet 6, and while it should have noticed that the three way handshake was indeed almost taking one second it retransmitted faster than that. The initial Retransmission Timeout for Windows Server 2k8R2 is 3000 milliseconds, for SYN and the first data segment. So I think it should have waited longer, but it is possible that packet number 4 (arriving quite soon after packet number 3) fooled the stack into believing that there is now a much better RTT. Or it is just refusing to believe that a connection could be THIS slow :-)</p><p>On a sidenote... there is a ongoing quest for my coworker <span>@landi</span> and me to track down a Microsoft engineer to find out what the Windows stack really does, and why. So far, no technical personal was ever able to answer questions like that, so unless we find the guy who writes the stack code we'll keep guessing... :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17866" class="comments-container"><span id="17874"></span><div id="comment-17874" class="comment"><div id="post-17874-score" class="comment-score"></div><div class="comment-text"><blockquote><p>On a sidenote... there is a ongoing quest for my coworker <span>@landi</span> and me to track down a Microsoft engineer to find out what the Windows stack really does, and why.</p></blockquote><p>hahaha... funny ;-)) I'll donate a bottle of champagne, if you ever find a single person who is able to give really detailed insight into the internal workings of the stack of a certain patch level.</p></div><div id="comment-17874-info" class="comment-info"><span class="comment-age">(22 Jan '13, 15:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17866" class="comment-tools"></div><div class="clear"></div><div id="comment-17866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17875"></span>

<div id="answer-container-17875" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17875-score" class="post-score" title="current number of votes">0</div><span id="post-17875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>It's almost as if the server "thinks" the connection is faster then it really is. This pattern continues throughout the session.</p></blockquote><p>maybe it's not the 2008 R2 stack, but the TCP offloading code of the NIC driver, who is a bit 'optimistic' while calculating the RTO ;-) Please check if TCP offloading (<strong>chimney</strong>) is enabled. If so, please disable it and retry..</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Offloading#TCP_Chimney</code><br />
<code>http://blogs.technet.com/b/brad_rutkowski/archive/2007/08/10/how-to-know-if-tcp-offload-is-working.aspx</code><br />
<code>http://support.microsoft.com/kb/951037</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 16:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-17875" class="comments-container"><span id="17895"></span><div id="comment-17895" class="comment"><div id="post-17895-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt - didn't think of that. I had a look and the TCP offloading is set to automatic. However, there are no connections that are in the offloaded state.</p></div><div id="comment-17895-info" class="comment-info"><span class="comment-age">(23 Jan '13, 05:58)</span> <span class="comment-user userinfo">Dodgyrabbit</span></div></div><span id="17901"></span><div id="comment-17901" class="comment"><div id="post-17901-score" class="comment-score"></div><div class="comment-text"><p>Never trust any stats ;-) Did you try to disable it?</p></div><div id="comment-17901-info" class="comment-info"><span class="comment-age">(23 Jan '13, 10:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17875" class="comment-tools"></div><div class="clear"></div><div id="comment-17875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

