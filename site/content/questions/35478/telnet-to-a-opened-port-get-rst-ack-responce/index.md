+++
type = "question"
title = "Telnet to a opened port, get [RST, ACK] responce"
description = '''Hi All, I have been googleing for 3 days, still couldn&#x27;t find correct answer yet for this issue. hopeing someone would help me out here. I have 2 windows2008R2 servers running in the same subnet, actually they are cable connected to each other directly. Both have firewall disabled. Server A can ping...'''
date = "2014-08-14T03:42:00Z"
lastmod = "2014-08-15T09:01:00Z"
weight = 35478
keywords = [ "rst", "ack", "telnet", "windows2008" ]
aliases = [ "/questions/35478" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Telnet to a opened port, get \[RST, ACK\] responce](/questions/35478/telnet-to-a-opened-port-get-rst-ack-responce)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35478-score" class="post-score" title="current number of votes">0</div><span id="post-35478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have been googleing for 3 days, still couldn't find correct answer yet for this issue. hopeing someone would help me out here.</p><p>I have 2 windows2008R2 servers running in the same subnet, actually they are cable connected to each other directly. Both have firewall disabled. Server A can ping Server B successfully, but when i tried to telnet from Server A to a certain port on Server B, it fails. this port is on listening state, and the port local address is 0.0.0.0:1234 (not bind to 127.0.0.1).</p><p>The wireshark captured data on Server B says that the TCP [SYN] packet was received by ServerB, and ServerB responced with a TCP [RST,ACK] packet instade of a [SYN, ACK]. which seems exactly same as the port is not listening.</p><p>Appreciate for any comments.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span> <span class="post-tag tag-link-windows2008" rel="tag" title="see questions tagged &#39;windows2008&#39;">windows2008</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '14, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/ab27b29d43311d8eb9b8d8544b41f044?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ckliu&#39;s gravatar image" /><p><span>ckliu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ckliu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Aug '14, 03:51</strong> </span></p></div></div><div id="comments-container-35478" class="comments-container"></div><div id="comment-tools-35478" class="comment-tools"></div><div class="clear"></div><div id="comment-35478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35479"></span>

<div id="answer-container-35479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35479-score" class="post-score" title="current number of votes">0</div><span id="post-35479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>are you also telnetting to port 1234? or are you trying to connect to the standard port 23? you should be able to see what port your client is using in the trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '14, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35479" class="comments-container"><span id="35480"></span><div id="comment-35480" class="comment"><div id="post-35480-score" class="comment-score"></div><div class="comment-text"><p>not port23, it is a certain port used by a certain software. i just assum it is 1234. when i type "netstat -nba" in ServerB , i can see the port is listening.</p></div><div id="comment-35480-info" class="comment-info"><span class="comment-age">(14 Aug '14, 04:32)</span> <span class="comment-user userinfo">ckliu</span></div></div><span id="35482"></span><div id="comment-35482" class="comment"><div id="post-35482-score" class="comment-score"></div><div class="comment-text"><p>I don't know how you run your telnet client, but you need to specify the port you want to connect to if it is not 23. So normally you'd run it like this: "telnet IPADDRESS 1234".</p></div><div id="comment-35482-info" class="comment-info"><span class="comment-age">(14 Aug '14, 08:27)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="35501"></span><div id="comment-35501" class="comment"><div id="post-35501-score" class="comment-score"></div><div class="comment-text"><p>yes, I did telnet IPADDRESS 1234, and in the destination server wireshark dump data, we can see there was a [syn] packet coming in, but the destination server responded with a [rst, ack] packet while it has port 1234 listening.</p></div><div id="comment-35501-info" class="comment-info"><span class="comment-age">(15 Aug '14, 03:08)</span> <span class="comment-user userinfo">ckliu</span></div></div></div><div id="comment-tools-35479" class="comment-tools"></div><div class="clear"></div><div id="comment-35479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35481"></span>

<div id="answer-container-35481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35481-score" class="post-score" title="current number of votes">0</div><span id="post-35481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The wireshark captured data on Server B says that the TCP [SYN] packet was received by ServerB, and ServerB responced with a TCP [RST,ACK] packet instade of a [SYN, ACK]. which seems exactly same as the port is not listening.</p></blockquote><p>sounds like the socket is <strong>not in LISTEN mode</strong>, although you say it is.</p><p>Please post:</p><ul><li>the output of <strong>netstat -nab</strong> on server B (only the lines related to port 1234)</li><li>the output of <strong>ipconfig /all</strong> on both servers</li><li>the capture file that shows the TCP reset (you can publish it on google drive, dropbox, or cloudshark.org and post the link here)</li></ul><p>Furthermore:</p><ul><li>is there any security software installed on server B, like Endpoint Security, AV, IDS/IPS, etc.?</li><li>what happens if you telnet from server B to its own address (not localhost!)?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '14, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Aug '14, 07:01</strong> </span></p></div></div><div id="comments-container-35481" class="comments-container"><span id="35502"></span><div id="comment-35502" class="comment"><div id="post-35502-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>yes seems exactly same as the port is not in listen mode,</p><p>the output of netstat -nba on server B is TCP 0.0.0.0:1234 0.0.0.0:0 LISTENING</p></div><div id="comment-35502-info" class="comment-info"><span class="comment-age">(15 Aug '14, 03:27)</span> <span class="comment-user userinfo">ckliu</span></div></div><span id="35506"></span><div id="comment-35506" class="comment"><div id="post-35506-score" class="comment-score"></div><div class="comment-text"><p>what about the rest of the information I requested?</p></div><div id="comment-35506-info" class="comment-info"><span class="comment-age">(15 Aug '14, 09:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35481" class="comment-tools"></div><div class="clear"></div><div id="comment-35481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

