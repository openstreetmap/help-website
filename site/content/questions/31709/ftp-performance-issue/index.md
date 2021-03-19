+++
type = "question"
title = "FTP performance issue"
description = '''Hi! (Sorry its about Window Size thing and many answers available but please answer for my explanation. Thanks) I am working on issues that my FTP takes longer time to download and upload files.  I did a capture on FTP server. The client is downloading a file in this scenario. Server OS = win 2003 N...'''
date = "2014-04-10T07:16:00Z"
lastmod = "2014-04-14T02:46:00Z"
weight = 31709
keywords = [ "ftp", "issue", "performance" ]
aliases = [ "/questions/31709" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FTP performance issue](/questions/31709/ftp-performance-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31709-score" class="post-score" title="current number of votes">0</div><span id="post-31709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! (Sorry its about Window Size thing and many answers available but please answer for my explanation. Thanks)</p><p>I am working on issues that my FTP takes longer time to download and upload files. I did a capture on FTP server. The client is downloading a file in this scenario. Server OS = win 2003 No high delta time. I can see line lines [TCP Window full]</p><p>Client to server: 14119 &gt; ftp-data [ACK] Seq=1 Ack=196609 Win=64860 Len=0 I have window size of 64860 and i am sending 0 packet</p><p>Server to Client 14119 FTP-DATA [TCP Window Full] FTP Data: 4140 bytes</p><p>Server is telling client that I am sending 4140bytes and my buffer size is full ???</p><p>Any help to check where the problem is so that we can reduce the transfer time.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '14, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/4da86d80e318819f883001822857d369?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="capricorn800&#39;s gravatar image" /><p><span>capricorn800</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="capricorn800 has no accepted answers">0%</span></p></div></div><div id="comments-container-31709" class="comments-container"></div><div id="comment-tools-31709" class="comment-tools"></div><div class="clear"></div><div id="comment-31709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31721"></span>

<div id="answer-container-31721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31721-score" class="post-score" title="current number of votes">0</div><span id="post-31721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would start with a tcp.analysis.flags filter and look at the Statistics -&gt; Flow Graph. If you see lots of window_full conditions then it's the client's tcp receive buffer that is too small to fill the pipe. See Bandwidth Delay Product and RFC1323: <a href="http://lmgtfy.com/?q=rfc1323+bdp">http://lmgtfy.com/?q=rfc1323+bdp</a></p><p>Without seeing a portion of the capture it is hard to help through this forum. Any chance you could put a snippet to <a href="http://cloudshark.org"></a><a href="http://cloudshark.org">http://cloudshark.org</a> ? You can use <code>editcap -s 100 infile outfile</code> to chop the full packets to just the header information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '14, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-31721" class="comments-container"><span id="31749"></span><div id="comment-31749" class="comment"><div id="post-31749-score" class="comment-score"></div><div class="comment-text"><p>Hi!</p><p>Thanks for you reply.</p><p>As I am filtering on specific source IP i use the following filter: ip.addr==Client IP address &amp;&amp; tcp.analysis.window_full and just found 27 line out of 100+ lines. If server sending information to client with Tcp window full then its server window which is full??</p><p>I cant post the capture due to restriction.</p><p>can you explain this:</p><p>Server to Client FTP-DATA [TCP Window Full] FTP Data: 4140 bytes</p><p>Server to Client FTP-DATA [TCP Window Full] FTP Data: 2760 bytes</p><p>Thanks,</p></div><div id="comment-31749-info" class="comment-info"><span class="comment-age">(11 Apr '14, 03:04)</span> <span class="comment-user userinfo">capricorn800</span></div></div><span id="31750"></span><div id="comment-31750" class="comment"><div id="post-31750-score" class="comment-score"></div><div class="comment-text"><p>"just" 27 out of 100+ is more than 20% ! I tink you need to enable WindowScaling on your client in order to get a better throughput. it your client is running Windows as the offered windowsize suggests then you need to set Tcp1323Opts to "1" (or "3" if you also want TIMESTAMP option)</p><p>The "FTP Data: 4140/2760 bytes" indicate that LargeSendOffload or TCP Segmentation Offload is enabled on the server's interface and the MSS is 1380 bytes</p></div><div id="comment-31750-info" class="comment-info"><span class="comment-age">(11 Apr '14, 04:45)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="31751"></span><div id="comment-31751" class="comment"><div id="post-31751-score" class="comment-score"></div><div class="comment-text"><p>(Answer converted to a comment in keeping with the way ask.wireshark.org works; Please see the FAQ).</p><p>But the problem is on Server side (ftp server). Its not just one client its more client that are seeing sluggish effect while downloading and uploading files. Can i check something more to troubleshoot the slowness?</p></div><div id="comment-31751-info" class="comment-info"><span class="comment-age">(11 Apr '14, 06:46)</span> <span class="comment-user userinfo">capricorn800</span></div></div><span id="31756"></span><div id="comment-31756" class="comment"><div id="post-31756-score" class="comment-score"></div><div class="comment-text"><p>I think you are misinterpreting the INFO line. It is not the server telling the client that the Window is full, it is wireshark that detected that the server has sent as many bytes as the client's windowsize offered and now needs to wait until the client opens its window again - which might take a while - depending on the RTT of the connection. With the information you offered that's all I can advice - sorry.</p></div><div id="comment-31756-info" class="comment-info"><span class="comment-age">(11 Apr '14, 09:19)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="31781"></span><div id="comment-31781" class="comment"><div id="post-31781-score" class="comment-score"></div><div class="comment-text"><p>Thanks mrEEde. Can i upload excel format file as i need to change the info?</p></div><div id="comment-31781-info" class="comment-info"><span class="comment-age">(14 Apr '14, 02:46)</span> <span class="comment-user userinfo">capricorn800</span></div></div></div><div id="comment-tools-31721" class="comment-tools"></div><div class="clear"></div><div id="comment-31721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

