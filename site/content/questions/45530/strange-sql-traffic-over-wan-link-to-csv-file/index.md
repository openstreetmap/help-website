+++
type = "question"
title = "Strange SQL traffic over WAN (link to csv file)"
description = '''I&#x27;d like some opinions on a wireshark capture between a web server and SQL database server that takes place over our WAN. This is east coast to west coast. We are trying to troubleshoot issues with slow performance on this web application. It was developed in house. We already know we have some issu...'''
date = "2015-08-30T13:44:00Z"
lastmod = "2015-08-30T15:30:00Z"
weight = 45530
keywords = [ "reassembly", "slow", "sql", "wan" ]
aliases = [ "/questions/45530" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strange SQL traffic over WAN (link to csv file)](/questions/45530/strange-sql-traffic-over-wan-link-to-csv-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45530-score" class="post-score" title="current number of votes">0</div><span id="post-45530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like some opinions on a wireshark capture between a web server and SQL database server that takes place over our WAN. This is east coast to west coast. We are trying to troubleshoot issues with slow performance on this web application. It was developed in house. We already know we have some issues with our WAN connection to this location from time to time and also looking into that. I haven't found in issues on the LAN yet. Also, there are other dependencies but this seems to be the main bottleneck since it's the only one cross-country.</p><p>I'm not a packet guru, I do know the fundamentals of TCP. I'm seeing a lot of ACK's with no SYN's and multiple ACK's in a row. Is this a bad capture? Also, it's saturated with reassembled PDUs. The average MS for this connection is 90-100, which I know might be out of the range of tolerance for SQL and could be causing the problem. Can anyone take look at this capture and shed some light on what they're seeing?</p><p><a href="https://drive.google.com/file/d/0By8V5doQZvoWR1k1VUN4Q0tJRG8/view?usp=sharing">https://drive.google.com/file/d/0By8V5doQZvoWR1k1VUN4Q0tJRG8/view?usp=sharing</a></p><p>web-srvr==10.10.10.200, db-srvr==10.0.0.50</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span> <span class="post-tag tag-link-wan" rel="tag" title="see questions tagged &#39;wan&#39;">wan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '15, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/f89758e8d8469083ddf1d9b54e32302a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vontech615&#39;s gravatar image" /><p><span>Vontech615</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vontech615 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Aug '15, 13:45</strong> </span></p></div></div><div id="comments-container-45530" class="comments-container"><span id="45539"></span><div id="comment-45539" class="comment"><div id="post-45539-score" class="comment-score"></div><div class="comment-text"><p>If you want to look behind the Reassembled PDUs, then you could do the following:</p><pre><code>On the Packet pane Select the tcp Header then click right mouse button.
Context Menu -&gt; Protocol preferences -&gt; Deselect &quot;Allow subdissectors to reasemble...&quot; </code></pre></div><div id="comment-45539-info" class="comment-info"><span class="comment-age">(30 Aug '15, 14:46)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-45530" class="comment-tools"></div><div class="clear"></div><div id="comment-45530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45534"></span>

<div id="answer-container-45534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45534-score" class="post-score" title="current number of votes">2</div><span id="post-45534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>We are trying to <strong>troubleshoot issues with slow performance</strong> on this web application. It was developed in house.</p></blockquote><p>To me it looks like your application is not well designed to work over a WAN. Take a look at TCP stream 9 (the only one with some data to transmit). The client sends a SELECT and gets the answer pretty fast. But then it waits for ~ 2.5 seconds before it sends the next SELECT. These seconds wait time add up to a lot of "dead wait time" with the result, that the whole communication takes longer than it should.</p><p>Example:</p><pre><code>frame #1462, 50.174: SELECT 
frame #1469, 50.461: last ACK for that request

~2.2 seconds wait time

frame #1480, 52.693: SELECT
frame #1487, 52.977: last ACK for that request

~2.6 seconds wait time

frame #1488, 55.562: SELECT
frame #1495, 55.821: last ACK for that request</code></pre><p>As you can see. Between the SELECT and the last ACK for that request, there is a time delta of a few 100 ms, which is O.K. for a WAN link, especially as the <strong>SELECT statement is pretty large (~ 6KB)</strong>.</p><p><strong>However</strong> between the last ACK and the next SELECT, there is a <strong>pause of ~2.5 seconds!!</strong></p><p>You can see that in the TCP Stream graph as well.</p><p>Please ask your developers why there is a pause of n seconds between the SELECT statements, as that's causing the whole problem!</p><p><strong>++ UPDATE ++</strong><br />
BTW: A database application that uses a lot of SELECT statements might work well on a local network (or on localhost of the developers laptop) as there is almost no latency, but it won't work well on a WAN link with high latency (RTT &gt; 50ms). I've seen this particular problem quite often, because developers usually run everything on their laptop or on the local lan (client, web server, database server) and don't realize, that latency might be a problem while they write and test the code. So, what a good programmer usually does to solve this kind of problem:</p><ul><li>have an application server next to the database server (same lan) and send a request to the application server to retrieve the whole data in one step (JSON, XML, whatever)</li><li>write a stored procedure on the SQL server and call that, instead of sending 20-30 SELECT statements over a low latency network</li></ul><p>;-))</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcp_stream.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '15, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Aug '15, 14:25</strong> </span></p></div></div><div id="comments-container-45534" class="comments-container"><span id="45535"></span><div id="comment-45535" class="comment"><div id="post-45535-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, that makes sense. As I said there are some other dependencies so it's possible, the web server is contacting those in these pauses and that's adding time. I'm not a developer, just a network guy, but this analysis helps. The full capture file actually has the traffic to those other dependencies as well and they are on the same lan as the web server. This DB server is the only one across the WAN.</p></div><div id="comment-45535-info" class="comment-info"><span class="comment-age">(30 Aug '15, 14:17)</span> <span class="comment-user userinfo">Vontech615</span></div></div><span id="45536"></span><div id="comment-45536" class="comment"><div id="post-45536-score" class="comment-score"></div><div class="comment-text"><p>see my updates above how to solve the problem.</p></div><div id="comment-45536-info" class="comment-info"><span class="comment-age">(30 Aug '15, 14:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45537"></span><div id="comment-45537" class="comment"><div id="post-45537-score" class="comment-score"></div><div class="comment-text"><p>Awesome, that gives me some ammunition when I meet with these people tomorrow.</p></div><div id="comment-45537-info" class="comment-info"><span class="comment-age">(30 Aug '15, 14:32)</span> <span class="comment-user userinfo">Vontech615</span></div></div><span id="45538"></span><div id="comment-45538" class="comment"><div id="post-45538-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Awesome, that gives me some ammunition when I meet with these people tomorrow.</p></blockquote><p>Good luck!</p><p>Maybe there are more problems to find in the whole capture file, but looking at that is beyond the scope of this site. I suggest to hire a network troubleshooting professional to analyze your application performance problems, in case the problem mentioned above is not the only one ;-)</p><p>I dare to bet that there are other problems as well, because as I said: developers often forget about latency when they develop and test applications on the local network and/or in virtual machines running on their laptop!</p><p>They get bitten in the a.. only when it's to late and the release date is due next monday :-))</p></div><div id="comment-45538-info" class="comment-info"><span class="comment-age">(30 Aug '15, 14:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45540"></span><div id="comment-45540" class="comment"><div id="post-45540-score" class="comment-score"></div><div class="comment-text"><p>1 last question... Why so many ACK's without a SYN or 3 way handshake? When I reveal what's underneath the reassembled PDU's it's mostly uknown packets (not last buffer). I'm reading that can be normal if WS doesn't understand the DB language?</p></div><div id="comment-45540-info" class="comment-info"><span class="comment-age">(30 Aug '15, 15:02)</span> <span class="comment-user userinfo">Vontech615</span></div></div><span id="45541"></span><div id="comment-45541" class="comment not_top_scorer"><div id="post-45541-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Why so many ACK's <strong>without a SYN</strong> or 3 way handshake?</p></blockquote><p>because you've (apparently) captured TCP streams that were already established when you started Wireshark.</p><blockquote><p>Why so many ACK's</p></blockquote><p>You can spot frames that are larger than ~1500 bytes in the capture file. That's because you've captured on the web server which has TCP offloading enabled. Those large TCP segements will be split into several smaller IP frames, according to the MTU size, by the NIC driver. As a result, you will see a lot more ACKs than you've expected.</p><blockquote><p>When I reveal what's underneath the reassembled PDU's it's mostly uknown packets (not last buffer).</p></blockquote><p>without the full pcap file (not anonymized), it's hard to tell what you are actually seeing....</p></div><div id="comment-45541-info" class="comment-info"><span class="comment-age">(30 Aug '15, 15:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45534" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-45534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

