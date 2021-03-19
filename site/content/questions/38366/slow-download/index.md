+++
type = "question"
title = "Slow download"
description = '''Hi, I am struggling to understand why the downloads from this server start off quickly and then suddenly  drop to a crawl. I see there are &quot;TCP windo full&quot; messages early on in the trace, but this is only in the first 100 packets and window scaling is enabled. I was testing this by downloading a 20M...'''
date = "2014-12-05T08:21:00Z"
lastmod = "2014-12-08T07:56:00Z"
weight = 38366
keywords = [ "download", "slow", "http" ]
aliases = [ "/questions/38366" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow download](/questions/38366/slow-download)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38366-score" class="post-score" title="current number of votes">0</div><span id="post-38366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am struggling to understand why the downloads from this server start off quickly and then suddenly drop to a crawl. I see there are "TCP windo full" messages early on in the trace, but this is only in the first 100 packets and window scaling is enabled. I was testing this by downloading a 20MB PDF file using "wget" from the client, I had to "ctrl-c" the capture to keep it below 1.5MB to be able to upload to cloudshark but I believe there is enough evidence of the issue in the following captures?</p><p><a href="https://www.cloudshark.org/captures/a9124b6343ce">https://www.cloudshark.org/captures/a9124b6343ce</a> - server <a href="https://www.cloudshark.org/captures/e82f6c71e0c1">https://www.cloudshark.org/captures/e82f6c71e0c1</a> - client</p><p>Regards, Elvin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '14, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/1ce649a675fca2f5c781be34d79582c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elfelvin&#39;s gravatar image" /><p><span>elfelvin</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elfelvin has no accepted answers">0%</span></p></div></div><div id="comments-container-38366" class="comments-container"></div><div id="comment-tools-38366" class="comment-tools"></div><div class="clear"></div><div id="comment-38366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38374"></span>

<div id="answer-container-38374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38374-score" class="post-score" title="current number of votes">0</div><span id="post-38374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem seems to be in the server not being able to feed the 'pipe' fast enough.<br />
The client's windowsize offering is higher than what is in flight.<br />
The communication stalls after the push bit is set by the server after 6 full sized MSS.<br />
The filter to detect those is<br />
<a href="https://www.cloudshark.org/captures/a9124b6343ce?filter=tcp.srcport%3D%3D80%20and%20tcp.flags.push%3D%3D1%20and%20tcp.analysis.bytes_in_flight%3D%3D8760">tcp.srcport==80 and tcp.flags.push==1 and tcp.analysis.bytes_in_flight==8760</a><br />
Then there is a wait of 8 ms (RTT) before it continues.</p><p>So not a network but rather a server problem - I would say...</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '14, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-38374" class="comments-container"><span id="38423"></span><div id="comment-38423" class="comment"><div id="post-38423-score" class="comment-score"></div><div class="comment-text"><p>It seems that server send limit is bound to 77380(Bytes in flight never moved beyond this),it could be due to send buffer or congestion window limitation from server end because client offered windows size is quite higher.</p></div><div id="comment-38423-info" class="comment-info"><span class="comment-age">(07 Dec '14, 23:33)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="38439"></span><div id="comment-38439" class="comment"><div id="post-38439-score" class="comment-score"></div><div class="comment-text"><p>Matthias is right, Yes in Middle it looks that server is only sending 8760 bytes/Roundtrip.</p></div><div id="comment-38439-info" class="comment-info"><span class="comment-age">(08 Dec '14, 06:55)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="38442"></span><div id="comment-38442" class="comment"><div id="post-38442-score" class="comment-score"></div><div class="comment-text"><p>So, I've looked at the "server" which is a Citrix Netscaler LB and it looks like the "MEM_TCPBUFFP" value is at 93% usage with ErrLmtFailed values incrementing, so I'm currently in contact with Citrix to get their advise on increasing this buffer (<a href="http://support.citrix.com/static/oldkc/CTX116779.html)">http://support.citrix.com/static/oldkc/CTX116779.html)</a> I'll report back on the outcome.</p><pre><code>----------------------------------------------------------------------------------------------------------------------
TotalMEM:  (2994699520/5731516416)     Allocated:  2089732480(36.46%)   ActualInUse: 958813336(16.73%)    Free:  3641783936

MEMPOOL             MaxAllowd           CurAlloc                  ErrLmtFailed   ErrAllocFailed  ErrFreeFailed
                                     Bytes (Own%)(Overall%)
----------------------------------------------------------------------------------------------------------------------
MEM_PE               62914560       1861824(2.96%  0.03%)          0                0            0
MEM_LB_SERVER     12884901885      15871488(0.12%  0.28%)          0                0            0
MEM_LB_SESSION      408944640       1575936(0.39%  0.03%)          0                0            0
MEM_LB_SERVICE    12884901885        483072(0.00%  0.01%)          0                0            0
MEM_CSWMEM           75497472        703296(0.93%  0.01%)          0                0            0
MEM_IOH              15728640             0(0.00%  0.00%)          0                0            0
MEM_LOGGING       12884901885      16785408(0.13%  0.29%)          0                0            0
MEM_CONN          12884901885    1222650368(9.49%  21.33%)          0                0            0
MEM_SNMP          12884901885       1082752(0.01%  0.02%)          0                0            0
MEM_DEBUG              786432          4608(0.59%  0.00%)          0                0            0
MEM_MISC          12884901885       9483840(0.07%  0.17%)          0                0            0
MEM_SERVMON       12884901885       3331584(0.03%  0.06%)          0                0            0
MEM_IPFRAG        12884901885             0(0.00%  0.00%)          0                0            0
MEM_URLMON           47185920             0(0.00%  0.00%)          0                0            0
MEM_TCPBUFFP         67108863      62914560(93.75%  1.10%)    1550584                0            0
MEM_DCC              31457280             0(0.00%  0.00%)          0                0            0
MEM_DNS           12884901885      25234368(0.20%  0.44%)          0                0            0
MEM_GSLB          12884901885        148416(0.00%  0.00%)          0                0            0
MEM_POLENG          402653184       3617664(0.90%  0.06%)          0                0            0
MEM_AUDITLOG        150994944       1204608(0.80%  0.02%)          0                0            0
MEM_PI_CONFIG     12884901885      41910336(0.33%  0.73%)          0                0            0</code></pre></div><div id="comment-38442-info" class="comment-info"><span class="comment-age">(08 Dec '14, 07:56)</span> <span class="comment-user userinfo">elfelvin</span></div></div></div><div id="comment-tools-38374" class="comment-tools"></div><div class="clear"></div><div id="comment-38374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

