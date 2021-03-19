+++
type = "question"
title = "Need help interpreting extra ACK package from Win 8 to SQL Server"
description = '''Hi! I&#x27;ve got a slightly duplicate of this post on http://social.technet.microsoft.com/Forums/windows/en-US/558553e7-d602-4584-a5dc-97f813890edc/extra-ack-packet-delaying-each-query-with-500-ms-on-windows-8, but I&#x27;m hoping some of you guys have some valuable input on this problem. Thing is, my box wi...'''
date = "2013-08-22T04:29:00Z"
lastmod = "2013-08-28T02:52:00Z"
weight = 23948
keywords = [ "ack", "delay", "ms-sql-s", "tds", "tcp" ]
aliases = [ "/questions/23948" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Need help interpreting extra ACK package from Win 8 to SQL Server](/questions/23948/need-help-interpreting-extra-ack-package-from-win-8-to-sql-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23948-score" class="post-score" title="current number of votes">0</div><span id="post-23948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I've got a slightly duplicate of this post on <a href="http://social.technet.microsoft.com/Forums/windows/en-US/558553e7-d602-4584-a5dc-97f813890edc/extra-ack-packet-delaying-each-query-with-500-ms-on-windows-8,">http://social.technet.microsoft.com/Forums/windows/en-US/558553e7-d602-4584-a5dc-97f813890edc/extra-ack-packet-delaying-each-query-with-500-ms-on-windows-8,</a> but I'm hoping some of you guys have some valuable input on this problem.</p><p>Thing is, my box with Win8 apparently sends an extra ACK package when I run SQL queries, and it seems like that package is creating a ~500 ms delay. Here's a short snippet of logs from my box and a Win 7 Box. (mine has multiboot and doesn't have the problem when booted with Win7)</p><p>Other box:</p><pre><code>&quot;20&quot;,&quot;0.286775000&quot;,&quot;10.29.84.125&quot;,&quot;172.18.166.116&quot;,&quot;TDS&quot;,&quot;116&quot;,&quot;SQL batch&quot;
&quot;21&quot;,&quot;0.311569000&quot;,&quot;172.18.166.116&quot;,&quot;10.29.84.125&quot;,&quot;TDS&quot;,&quot;480&quot;,&quot;Response&quot;
-- 22 is ack for 21, no delay
&quot;22&quot;,&quot;0.312462000&quot;,&quot;10.29.84.125&quot;,&quot;172.18.166.116&quot;,&quot;TDS&quot;,&quot;116&quot;,&quot;SQL batch&quot;
&quot;23&quot;,&quot;0.337217000&quot;,&quot;172.18.166.116&quot;,&quot;10.29.84.125&quot;,&quot;TDS&quot;,&quot;480&quot;,&quot;Response&quot;</code></pre><p>My box:</p><pre><code>&quot;19&quot;,&quot;2.949616000&quot;,&quot;10.29.84.127&quot;,&quot;172.18.166.116&quot;,&quot;TDS&quot;,&quot;116&quot;,&quot;SQL batch&quot;
&quot;20&quot;,&quot;2.974706000&quot;,&quot;172.18.166.116&quot;,&quot;10.29.84.127&quot;,&quot;TDS&quot;,&quot;480&quot;,&quot;Response&quot;
&quot;21&quot;,&quot;2.974793000&quot;,&quot;10.29.84.127&quot;,&quot;172.18.166.116&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;50457 &gt; sslp [ACK] Seq=775 Ack=1955 Win=65792 Len=0&quot;
-- 21 is ack for 20
-- 22 is not ack for 20, although ack bit is set
-- 500 ms delay before each new SQL batch 
&quot;22&quot;,&quot;3.494747000&quot;,&quot;10.29.84.127&quot;,&quot;172.18.166.116&quot;,&quot;TDS&quot;,&quot;116&quot;,&quot;SQL batch&quot;
&quot;23&quot;,&quot;3.520266000&quot;,&quot;172.18.166.116&quot;,&quot;10.29.84.127&quot;,&quot;TDS&quot;,&quot;480&quot;,&quot;Response&quot;
&quot;24&quot;,&quot;3.520363000&quot;,&quot;10.29.84.127&quot;,&quot;172.18.166.116&quot;,&quot;TCP&quot;,&quot;54&quot;,&quot;50457 &gt; sslp [ACK] Seq=837 Ack=2381 Win=65280 Len=0&quot;</code></pre><p>Hope someone has seen this before and know exactly what setting I can change or command I can run. ;)</p><p>[edit] Reason ACK packet is on SSLP instead of MS-SQL-S is that SQL Server in question runs on port 1750 instead of 1433. Same behavior on other servers though, so never mind it.</p><p>Lars-Erik</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-ms-sql-s" rel="tag" title="see questions tagged &#39;ms-sql-s&#39;">ms-sql-s</span> <span class="post-tag tag-link-tds" rel="tag" title="see questions tagged &#39;tds&#39;">tds</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '13, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/e01edb3cfd7c95926be8c85a0ea75bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lars-Erik&#39;s gravatar image" /><p><span>Lars-Erik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lars-Erik has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Aug '13, 05:18</strong> </span></p></div></div><div id="comments-container-23948" class="comments-container"></div><div id="comment-tools-23948" class="comment-tools"></div><div class="clear"></div><div id="comment-23948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24120"></span>

<div id="answer-container-24120" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24120-score" class="post-score" title="current number of votes">0</div><span id="post-24120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lars-Erik has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Purp identified.</p><p>It was Trend Micro Worry Free (!) Business Security.</p><p>Upgraded it, and problem gone.</p><p>Lars-Erik</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/e01edb3cfd7c95926be8c85a0ea75bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lars-Erik&#39;s gravatar image" /><p><span>Lars-Erik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lars-Erik has one accepted answer">100%</span></p></div></div><div id="comments-container-24120" class="comments-container"></div><div id="comment-tools-24120" class="comment-tools"></div><div class="clear"></div><div id="comment-24120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23949"></span>

<div id="answer-container-23949" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23949-score" class="post-score" title="current number of votes">0</div><span id="post-23949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hm, the packet that is sent out is just 62 bytes in length. So this may be the Nagle algorithm that is slowing you down here. This <a href="http://windows7themes.net/how-to-improve-latency-in-wow-in-windows-7.html">blog</a> suggests to turn it off</p><p>"To disable TCP packet batching, we set TcpNoDelay to 1, so all packets will be send no matter what size they have (normally TCP sends out batched packages)."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '13, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-23949" class="comments-container"><span id="23950"></span><div id="comment-23950" class="comment"><div id="post-23950-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I've tried setting both TcpNoDelay and TcpAckFrequency to 1 and AckFreq to 2, neither has any effect what-so-ever.</p><p>Although I'm not entirely sure I put it in the right key. I used HKLM\SYSTEM\ControlSet001\Microsoft\Services\tcpip\Parameters\Interfaces\[the one that has my ip in a setting].</p><p>I'll try nodelay once more with a restart just to be sure I've tried properly.</p><p>[edit] Tried TcpNoDelay = 1 on all adapters for good measure, restart, no effect. :(</p><p>Lars-Erik</p></div><div id="comment-23950-info" class="comment-info"><span class="comment-age">(22 Aug '13, 05:06)</span> <span class="comment-user userinfo">Lars-Erik</span></div></div></div><div id="comment-tools-23949" class="comment-tools"></div><div class="clear"></div><div id="comment-23949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

