+++
type = "question"
title = "Excessive internet traffic eminating from SBS 2003 Server"
description = '''Excessive internet traffic eminating from SBS 2003 Server Our internet browsing capability at the office has slowed considerably in the last few days. I noticed our server is sending and receiving data constantly. It is running SBS 2003 and we are hosting email on it. We don&#x27;t host a website on it -...'''
date = "2010-12-08T19:19:00Z"
lastmod = "2010-12-09T09:37:00Z"
weight = 1295
keywords = [ "fragment", "sbs", "2003", "server" ]
aliases = [ "/questions/1295" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Excessive internet traffic eminating from SBS 2003 Server](/questions/1295/excessive-internet-traffic-eminating-from-sbs-2003-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1295-score" class="post-score" title="current number of votes">0</div><span id="post-1295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Excessive internet traffic eminating from SBS 2003 Server</p><p>Our internet browsing capability at the office has slowed considerably in the last few days.</p><p>I noticed our server is sending and receiving data constantly. It is running SBS 2003 and we are hosting email on it. We don't host a website on it - other than the Remote Web Workplace site that is available via the internet. Local LAN IP of SBS 2003 box is 192.168.0.254.</p><p>If I remove the server from the network, ping times are reduced and internet speeds are increased when testing from a workstation.</p><p>I installed WireShark on the server and ran a capture. I am not too good at reading the resulting data. But, there are several lines with red text on a black background. And there are many more entries listed as "Data Fragments" under the SMTP protocol - all of which have the same destination IP address (66.94.237.64)</p><p>Here are two entries:</p><p>Red text with black background:</p><p>No: 44794. Time: 245.209207. Source: 66.94.237.64. Destination: 192.168.0.254. Protocol: TCP. Info: [TCP Window Update] smtp &gt; [ACK] Seq=411 Ack=7433321 Win=61756 Len=0</p><p>Data Fragment:</p><p>No: 44795. Time: 245.209227. Source: 192.168.0.254. Destination: 66.94.237.64. Protocol: SMTP. Info: C: DATA fragment, 1452 bytes</p><p>Can anyone tell me what this is or means? Maybe a virus? Maybe a SMTP Relay situation?</p><p>Thank you for any help you may be able to offer.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragment" rel="tag" title="see questions tagged &#39;fragment&#39;">fragment</span> <span class="post-tag tag-link-sbs" rel="tag" title="see questions tagged &#39;sbs&#39;">sbs</span> <span class="post-tag tag-link-2003" rel="tag" title="see questions tagged &#39;2003&#39;">2003</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '10, 19:19</strong></p><img src="https://secure.gravatar.com/avatar/01f25b7f4ee95451e9dc70cd823d5460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coryjon&#39;s gravatar image" /><p><span>coryjon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coryjon has no accepted answers">0%</span></p></div></div><div id="comments-container-1295" class="comments-container"></div><div id="comment-tools-1295" class="comment-tools"></div><div class="clear"></div><div id="comment-1295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1299"></span>

<div id="answer-container-1299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1299-score" class="post-score" title="current number of votes">0</div><span id="post-1299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you might want to go through some of the statistics menu first. What you are looking at maybe the needle in the haystack, but if so you have lots of needles. Look at Statistics &gt; Protocol Heirarchy, Statistics &gt; Endpoints, and Statistics Conversations. Also look at statistics, packet lengths. You will want to exclude all traffic that is internal. What we are looking for is the following:</p><p>1). Is there high bw consumption (sometimes there isn't) 2). Are the packets big or small 3). Anything that surprises you 4). non tcp transport layer protocol</p><p>What you are trying to do understand from a broad perspective what your traffic looks like.</p><p>These are just a few starting points. Its really, really difficult to troubleshoot using packet analysis when you haven't had a lot of experience. Let me say that another way. It is very easy to be distracted by the unimportant when troubleshooting, if you don't regularly spend time in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '10, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1299" class="comments-container"></div><div id="comment-tools-1299" class="comment-tools"></div><div class="clear"></div><div id="comment-1299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1302"></span>

<div id="answer-container-1302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1302-score" class="post-score" title="current number of votes">0</div><span id="post-1302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The two frames that you have quoted show that your server is sending out e-Mail to a Yahoo-server.</p><p>As these are only two lines from the whole trace file it is not indication for a symptom, left alone a problem. Don't get confused by the all the colors.</p><p>As Paul pointed out the protocol hierarchy, endpoint- and conversation statistics are a good start. If Statistics -&gt; Endpoints -&gt; TCP would show that the majority of traffic is send from your SBS to the SMTP port (port 25) your server is sending out e-Mail - at least while you are capturing.</p><p>Excessive outgoing e-Mail can have a number of reasons:</p><ul><li>Some genius decides to attach the latest DVD to an e-Mail</li><li>A user (or department) is sending out e-Mail (say, a marketing department going wild)</li><li>One of your clients got infected with a trojan horse / spambot and sends out SPAM</li><li>Your mail server is not properly secured and someone is using it as a SPAM relay</li></ul><p>The general "slow surfing" experience can have a number of other reasons, including, but not limited to:</p><ul><li>One or more users downloading data / watching TV ...</li><li>A general saturation of your internet link</li><li>Introduction of a new software, that relies on an Internet service</li><li>Over subscription of the line on the provider-end</li><li>faulty hardware / cable</li></ul><p>These are just a few points to look at. The first network analysis with Wireshark is always the hardest. It get's easier once get used to it.</p><p>hth, good luck</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '10, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-1302" class="comments-container"></div><div id="comment-tools-1302" class="comment-tools"></div><div class="clear"></div><div id="comment-1302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

