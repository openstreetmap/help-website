+++
type = "question"
title = "Port statistics"
description = '''Hello, I&#x27;m looking for syntax in Wireshark/tshark or any other tool for pcap analyzing for port statistics. I don&#x27;t know if its possible, but I need to make statistics of port in pcap file.  Show statistics by port and display in descending order by occurrence.  Calculation will be performed only on...'''
date = "2015-04-06T12:56:00Z"
lastmod = "2015-04-08T10:31:00Z"
weight = 41231
keywords = [ "wireshark", "statistics", "tshark", "port" ]
aliases = [ "/questions/41231" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Port statistics](/questions/41231/port-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41231-score" class="post-score" title="current number of votes">0</div><span id="post-41231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm looking for syntax in Wireshark/tshark or any other tool for pcap analyzing for port statistics. I don't know if its possible, but I need to make statistics of port in pcap file. Show statistics by port and display in descending order by occurrence. Calculation will be performed only on Well known ports (0-1023).</p><p>Output should be something like:</p><ul><li>PORT NAME COUNT</li><li>80 HTTP 5000</li><li>443 HTTPS 500</li><li>25 SMTP 80</li><li>143 IMAP 70 ....</li></ul><p>Thanks a lot<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '15, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/d0cb734898132ce703ea326a1d7c6354?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eduard%20Woidig&#39;s gravatar image" /><p><span>Eduard Woidig</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eduard Woidig has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '15, 12:59</strong> </span></p></div></div><div id="comments-container-41231" class="comments-container"><span id="41251"></span><div id="comment-41251" class="comment"><div id="post-41251-score" class="comment-score"></div><div class="comment-text"><p>Hi Eduard - Did you try the Statistics function within Wireshark? In Wireshark, select Statistics from the top menu. Then select Conversations. A window pop-up will be displayed with multiple tabs. You can select TCP. In the TCP tab, you can arrange the amount of traffic in descending order by either bytes or packets. The only limitation on this approach is that each TCP stream (IP-address:TCP-port) is treated separately.</p></div><div id="comment-41251-info" class="comment-info"><span class="comment-age">(07 Apr '15, 07:37)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-41231" class="comment-tools"></div><div class="clear"></div><div id="comment-41231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41298"></span>

<div id="answer-container-41298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41298-score" class="post-score" title="current number of votes">1</div><span id="post-41298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>C:\Program Files\Wireshark&gt;tshark -i 1 -qz io,stat,5,http,smtp,imap

Capturing on &#39;Local Area Connection&#39;
4866 packets captured

===============================================================
| IO Statistics                                               |
|                                                             |
| Duration: 29. 30456 secs                                    |
| Interval:  5 secs                                           |
|                                                             |
| Col 1: http                                                 |
|     2: smtp                                                 |
|     3: imap                                                 |
|-------------------------------------------------------------|
|          |1               |2               |3               |
| Interval | Frames | Bytes | Frames | Bytes | Frames | Bytes |
|-------------------------------------------------------------|
|  0 &lt;&gt;  5 |      3 |   525 |      0 |     0 |      0 |     0 |
|  5 &lt;&gt; 10 |      2 |   350 |      0 |     0 |      0 |     0 |
| 10 &lt;&gt; 15 |     11 |  4610 |      0 |     0 |      0 |     0 |
| 15 &lt;&gt; 20 |     75 | 47906 |      0 |     0 |      0 |     0 |
| 20 &lt;&gt; 25 |    137 | 69147 |      0 |     0 |      0 |     0 |
| 25 &lt;&gt; Dur|     28 | 20001 |      0 |     0 |      0 |     0 |
===============================================================

C:\Program Files\Wireshark&gt;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '15, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '15, 10:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41298" class="comments-container"></div><div id="comment-tools-41298" class="comment-tools"></div><div class="clear"></div><div id="comment-41298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

