+++
type = "question"
title = "response time - single src ip, multiple dst ip addresses"
description = '''I have a trace with a single source ip address talking to several destination ip addresses. I need a report or graph that shows the http response times for the source going to each dest ip. I need to know who the fastest and slowest servers are when communicating with this ip address. How can I do t...'''
date = "2012-02-22T22:11:00Z"
lastmod = "2012-02-23T02:58:00Z"
weight = 9178
keywords = [ "multiple", "addresses", "http", "response", "ip" ]
aliases = [ "/questions/9178" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [response time - single src ip, multiple dst ip addresses](/questions/9178/response-time-single-src-ip-multiple-dst-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9178-score" class="post-score" title="current number of votes">0</div><span id="post-9178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace with a single source ip address talking to several destination ip addresses. I need a report or graph that shows the http response times for the source going to each dest ip. I need to know who the fastest and slowest servers are when communicating with this ip address. How can I do this? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '12, 22:11</strong></p><img src="https://secure.gravatar.com/avatar/a921639d21f1c40d3e70cf3d7489053d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jacob600&#39;s gravatar image" /><p><span>jacob600</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jacob600 has no accepted answers">0%</span></p></div></div><div id="comments-container-9178" class="comments-container"></div><div id="comment-tools-9178" class="comment-tools"></div><div class="clear"></div><div id="comment-9178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9182"></span>

<div id="answer-container-9182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9182-score" class="post-score" title="current number of votes">2</div><span id="post-9182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It isn't very easy but it can be done.</p><p>You need to divide up your HTTP traffic into separate TCP streams and then report on each of them. This is because we are are going to use the ability for wireshark to calculate and display times (deltas) between displayed packets. This only works if you have a single TCP stream in the display.</p><ol><li>Identify all of the HTTP conservations. You could use just the "http" display filter, but if you want to specific, you could use <code>http.host == "the.host.com"</code>. (Of course this will be the host in the HTTP headers of the request - which may or may not be the same as the URL of the initial HTTP fetch). To be more general you can use a filter like "<code>http.host contains bbc"</code></li><li><p>Then use the Statistics-&gt;Conversations-&gt;TCP, and check limit to display filter, to see all of the conversation to the TCP host.</p></li><li><p>Then select a TCP stream of interest and follow it, or apply as a display filter. You then need to append a "<code>&amp;&amp; http</code>" again to that particular stream. This way you will only see http requests and responses - not individual frames. <a href="https://docs.google.com/open?id=0Bwx8XaFad3_MODQ2NTQ5N2MtYmY2Mi00ZTE2LWEzMTktNzlmMGEyMWM1MTMw">HTTP requests and responses</a></p></li><li><p>You then will want to use that display filter (copy it) in the IO Graphs. In the IO Graph Filter, use the TCP stream filter anded with the http.response. For instance "tcp.stream eq 155 &amp;&amp; ( http.response)". In the Y axis Unit, select Advanced... Then the Calc: field select MAX (or AVG or MIN), and the field will be <code>'frame.time_delta_displayed'</code>. You may also want to change the Tick Interval.<a href="https://docs.google.com/open?id=0Bwx8XaFad3_MMjQ4YjdhNDctYWM0NC00ODBhLWI2YWUtNDliMTM2Yzg4OTZj">Setting up graph</a></p></li><li><p>As the response times are quite discrete, I would change the Style to FBar.</p></li></ol><p>Note that because by default Wireshark will reassemble multiple TCP segments, displaying the last frame in the response, your default response graph will show the Response Time for the last byte (or at least the last frame). If you want the response time for the first byte (which gives you a better idea of the server processing time, and doesn't include the delay in streaming the whole response), you may want to go into your Preferences-&gt;Protocols-&gt;HTTP and turn off reassembly. Note that if you do this you should use the filter "http.request &amp;&amp; http.response" rather than just "http" to avoid seeing all the in-between frames.</p><p>You can see the difference here in the following two graphs (from Australia to the BBC web site for images)</p><p><a href="https://docs.google.com/open?id=0Bwx8XaFad3_MMWYzYTU5MjAtMGE1Ni00MmJiLTkyNjUtY2MxMDI2ZDRiOTQy">BBC - Response Time to Last Byte</a></p><p><a href="https://docs.google.com/open?id=0Bwx8XaFad3_MMDRiMGFiZjMtM2U0NS00NDNmLWE4ODQtZDcyY2EwZjk0OGYx5.5.4.4.4.4.4.">BBC - Response Time to First Byte</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '12, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '12, 03:11</strong> </span></p></div></div><div id="comments-container-9182" class="comments-container"></div><div id="comment-tools-9182" class="comment-tools"></div><div class="clear"></div><div id="comment-9182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

