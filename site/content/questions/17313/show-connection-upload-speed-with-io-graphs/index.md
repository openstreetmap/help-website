+++
type = "question"
title = "Show connection upload speed with IO Graphs"
description = '''hi, im looking for a way to graph only the upload or download traffic for one connection, is this possible? what ive found: how fast a connection is at the moment(probably up+download speed combined): http://ask.wireshark.org/questions/1242/speed-of-sending-and-receiving-packets selecting a filter A...'''
date = "2012-12-29T06:02:00Z"
lastmod = "2012-12-29T06:53:00Z"
weight = 17313
keywords = [ "connection.speed" ]
aliases = [ "/questions/17313" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show connection upload speed with IO Graphs](/questions/17313/show-connection-upload-speed-with-io-graphs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17313-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>im looking for a way to graph only the upload or download traffic for one connection, is this possible?</p><p>what ive found:</p><p>how fast a connection is at the moment(probably up+download speed combined): <a href="http://ask.wireshark.org/questions/1242/speed-of-sending-and-receiving-packets">http://ask.wireshark.org/questions/1242/speed-of-sending-and-receiving-packets</a> selecting a filter A-&gt;B or B-&gt;A both showed the same value for my test application.</p><p>or how much data was downloaded by conversation x <a href="http://ask.wireshark.org/questions/82/can-wireshark-monitor-bandwidth-usage-per-applicationprocess">http://ask.wireshark.org/questions/82/can-wireshark-monitor-bandwidth-usage-per-applicationprocess</a></p></div><div id="question-tags" class="tags-container tags">connection.speed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '12, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/e73d763dd0b04d5354d00d4ba3247441?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiste_Becks&#39;s gravatar image" /><p>Kiste_Becks<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiste_Becks has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Dec '12, 06:24</p></div></div><div id="comments-container-17313" class="comments-container"></div><div id="comment-tools-17313" class="comment-tools"></div><div class="clear"></div><div id="comment-17313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17314"></span>

<div id="answer-container-17314" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17314-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use a filter in the IO graph for one of the colors, which would lead to a graph of that color being painted for just the packets that pass the filter. For example you could filter on something like "(ip.addr eq 192.168.1.1 and ip.addr eq 10.0.0.1) and (tcp.port eq 1025 and tcp.port eq 80)", assuming that these IPs and ports are used for the connection you want to graph. Don't forget to activate the graph by pushing the according button in front of the filter box.</p><p>If you only want one direction - lets say, just the packets coming back from the server (a download for example), you can filter on "ip.src eq 10.0.0.1 and tcp.srcport eq 80". That filter forces Wireshark to only graph for packets that come from the server. Problem with this is - if you have multiple connection to that server on that port you'll graph all of them. You can circumvent this problem by adding the stream index as well, for example "ip.src eq 10.0.0.1 and tcp.srcport eq 80 and tcp.stream==5" (assuming 5 is the connection that you want to graph).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '12, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Dec '12, 06:55</p></div></div><div id="comments-container-17314" class="comments-container"><span id="17315"></span><div id="comment-17315" class="comment"><div id="post-17315-score" class="comment-score"></div><div class="comment-text"><p>thx, will experiment with that.</p><p>[Answer converted to a comment as per the style for <a href="http://bugs.wireahrk.org">bugs.wireahrk.org</a>; Please see the FAQ]</p></div><div id="comment-17315-info" class="comment-info"><span class="comment-age">(29 Dec '12, 12:34)</span> Kiste_Becks</div></div><span id="17316"></span><div id="comment-17316" class="comment"><div id="post-17316-score" class="comment-score"></div><div class="comment-text"><p>If you're going to use the stream index, which is a good idea, I think you can drop the "tcp.srcport" and simplify your filter to "ip.src == 10.0.0.1 and tcp.stream == 5" since the entire stream will be between one pair of ports that won't change during that particular TCP connection.</p></div><div id="comment-17316-info" class="comment-info"><span class="comment-age">(29 Dec '12, 16:50)</span> Jim Aragon</div></div><span id="17361"></span><div id="comment-17361" class="comment"><div id="post-17361-score" class="comment-score"></div><div class="comment-text"><p>True. I added the paragraph about the stream index when I realized that without it you'd see all connections on that port. In that Edit, I forgot that I could now deprecate the port. It doesn't hurt to have it, so I didn't edit the answer again :-)</p></div><div id="comment-17361-info" class="comment-info"><span class="comment-age">(31 Dec '12, 10:17)</span> Jasper ♦♦</div></div></div><div id="comment-tools-17314" class="comment-tools"></div><div class="clear"></div><div id="comment-17314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

