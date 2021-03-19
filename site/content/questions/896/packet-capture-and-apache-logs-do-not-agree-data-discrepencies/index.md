+++
type = "question"
title = "Packet capture and Apache logs do not agree - data discrepencies"
description = '''I recently started to see a burst of HTTP &#x27;400&#x27; response codes in our Apache logs running on RHEL5 servers. According to our logs we are serving up a &#x27;400&#x27; every few seconds. When I manually cut/paste the URL receiving a &#x27;400&#x27; in a browser it works without any problems. What&#x27;s odd is that Apache is ...'''
date = "2010-11-10T08:46:00Z"
lastmod = "2012-09-13T10:57:00Z"
weight = 896
keywords = [ "apache", "tshark", "capture", "log", "wireshark" ]
aliases = [ "/questions/896" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Packet capture and Apache logs do not agree - data discrepencies](/questions/896/packet-capture-and-apache-logs-do-not-agree-data-discrepencies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-896-score" class="post-score" title="current number of votes">0</div><span id="post-896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently started to see a burst of HTTP '400' response codes in our Apache logs running on RHEL5 servers. According to our logs we are serving up a '400' every few seconds. When I manually cut/paste the URL receiving a '400' in a browser it works without any problems. What's odd is that Apache is showing those responses taking 1 second to complete.<br />
</p><p>To debug I ran tshark on one of the RHEL5 web servers. I didn't enter in any abnormal packet capture. Here was my syntax: tshark -i bond0 -f "host port 80" -w ~/test.cap</p><p>I am unable to find the '400' errors that I see in the Apache logs in the capture. What is odd is there are '400' errors for queries that I am unable to find in the Apache logs, for another URI entirely. The number of '400' errors I see in the capture for URI X and the number I see in the Apache logs for URI Y do not line up directly. We also do not have any sort of rewrite rules or proxies in place that would account for a URL being altered.<br />
</p><p>I ran a wide open packet capture (i.e. not using 'host port 80') on our border router and see the same behavior. What is odd is that I do not see the web server's '400' error ever leaving our network.<br />
</p><p>I have run subsequent captures wide open, capturing all traffic just in case something was out of whack with the filter. I also ran captures against every interface on the servers in case something might be wrong or misconfigured with the bonded interface but that isn't the case.<br />
</p><p>I have always been able to directly correlate entries in wireshark to log entries. This is a first for me. Has anyone run into this problem before?<br />
</p><p>All servers are 64 bit running RHEL5, wireshark version wireshark-1.0.15-1.el5_5.1. I also analyzed the capture on a 64 bit windows laptop running the 64 bit 1.4.1 wireshark version.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '10, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/c72ae7a46acbddf07e3c2ba755b19a4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devrick0&#39;s gravatar image" /><p><span>devrick0</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devrick0 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-896" class="comments-container"></div><div id="comment-tools-896" class="comment-tools"></div><div class="clear"></div><div id="comment-896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="922"></span>

<div id="answer-container-922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-922-score" class="post-score" title="current number of votes">0</div><span id="post-922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That capture filter isn't valide - "host port 80." You should have seen an error message though.</p><p>Can you open the "wide open" traces you captured and apply a display filter for <code>http.response.code == 400</code> - there is a chance you might not be able to 'see' the 400 errors in the packet list if the TCP preferences are set to "allow subdissector to reassemble TCP streams." I usually set that off on standard HTTP communications so I can see the response codes clearly in the list.</p><p>If the 400 errors are being sent and Wireshark can see them, so should you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 17:10</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span> </br></br></p></div></div><div id="comments-container-922" class="comments-container"><span id="930"></span><div id="comment-930" class="comment"><div id="post-930-score" class="comment-score"></div><div class="comment-text"><p>Yes, my mistake, it was "tcp port 80" when I tried the filter.<br />
</p><p>I was able to have the inbound requests that were generating the '400' errors corrected so those are gone. I checked the load balancer and confirmed the errors are not leaving the server. I checked all the interfaces again and I don't see the '400' errors. My next thought is to look at wireshark and see if I can track down inbound requests that didn't receive a response from the web server.<br />
</p><p>I realize that I am lacking in wireshark skills so I ordered "Wireshark Network Analysis" yesterday on amazon.</p></div><div id="comment-930-info" class="comment-info"><span class="comment-age">(12 Nov '10, 07:25)</span> <span class="comment-user userinfo">devrick0</span></div></div><span id="933"></span><div id="comment-933" class="comment"><div id="post-933-score" class="comment-score"></div><div class="comment-text"><p>One nice feature of Wireshark is Statistics &gt; HTTP &gt; Packet Counter that will list the response types by number group (1xx, 2xx, 3xx, etc.). Check that out as well.</p></div><div id="comment-933-info" class="comment-info"><span class="comment-age">(12 Nov '10, 11:06)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-922" class="comment-tools"></div><div class="clear"></div><div id="comment-922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6385"></span>

<div id="answer-container-6385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6385-score" class="post-score" title="current number of votes">0</div><span id="post-6385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://justniffer.sourceforge.net/">justniffer</a> for logging http traffic</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '11, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/748d970388f03add061a45634d5608e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Augustyn&#39;s gravatar image" /><p><span>Augustyn</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Augustyn has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-6385" class="comments-container"></div><div id="comment-tools-6385" class="comment-tools"></div><div class="clear"></div><div id="comment-6385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14241"></span>

<div id="answer-container-14241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14241-score" class="post-score" title="current number of votes">0</div><span id="post-14241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We had similar symptoms and the problem was that 2 HTTP requests seemed to be intermingled within the same TCP communication left open because of the keep-alive directive. In our case a proxy is talking to the apache, not the browsers directly. Because the queries are intermingled our proxy only detects the 400 response on one of the requests, I assume the other is considered to have timed out. Apache actually doesn't log anything at all in the access_log.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '12, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/60f0f4bd86ee7e3788f53ae8c53d495e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adamloopkin&#39;s gravatar image" /><p><span>adamloopkin</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adamloopkin has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-14241" class="comments-container"></div><div id="comment-tools-14241" class="comment-tools"></div><div class="clear"></div><div id="comment-14241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

