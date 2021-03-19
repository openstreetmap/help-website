+++
type = "question"
title = "Empty pcap file from converting a syslog server text file to pcap"
description = '''There are many discussions on converting PCAP to TXT but nothing on TXT to PCAP. Let&#x27;s establish the scenario. Discussion is based on Windows Platform. Router is a NETGEAR FVS318N. The logs can be sent to a &quot;syslog server&quot;. Two examples are &quot;Kiwi Syslog Server&quot; and &quot;TFTpd32 Syslog Server&quot; Out of all...'''
date = "2014-11-17T01:14:00Z"
lastmod = "2014-11-17T01:31:00Z"
weight = 37892
keywords = [ "syslog", "convert", "txt", "pcap" ]
aliases = [ "/questions/37892" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Empty pcap file from converting a syslog server text file to pcap](/questions/37892/empty-pcap-file-from-converting-a-syslog-server-text-file-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37892-score" class="post-score" title="current number of votes">0</div><span id="post-37892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There are many discussions on converting PCAP to TXT but nothing on TXT to PCAP. Let's establish the scenario. Discussion is based on Windows Platform. Router is a NETGEAR FVS318N. The logs can be sent to a "syslog server". Two examples are "Kiwi Syslog Server" and "TFTpd32 Syslog Server" Out of all the variations and preferences that the Syslog Server community may offer, the question is focused on how to get the information to "WireShark". So first we need to establish that the information that is captured from the Router to the Syslog Server is placed in a log folder that is in the form of "File.txt". There is nothing special about it. It is a simple "File.txt". It can be opened with a simple notepad. Here is where it gets difficult. It is said, that you should convert the "txt" file to a "pcap" file. So CMD is: text2pcap.exe file.txt file.pcap - resulting in the following:<br />
<strong>Input from: file.txt<br />
Output to: file.pcap<br />
Output format: PCAP<br />
Read 4 potential packets, wrote 0 packets (24 bytes)</strong><br />
The goal is to take the captured data that is in a .txt format and get it into a .pcap format so that the captured data can be opened in WireShark. What is the process?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syslog" rel="tag" title="see questions tagged &#39;syslog&#39;">syslog</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-txt" rel="tag" title="see questions tagged &#39;txt&#39;">txt</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/c2bd39086ec6f0bbc6837d0b1a30104e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SJISP&#39;s gravatar image" /><p><span>SJISP</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SJISP has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Aug '16, 21:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></br></p></div></div><div id="comments-container-37892" class="comments-container"></div><div id="comment-tools-37892" class="comment-tools"></div><div class="clear"></div><div id="comment-37892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37893"></span>

<div id="answer-container-37893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37893-score" class="post-score" title="current number of votes">0</div><span id="post-37893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This will only work (and make sense) if the text you have contains the hex bytes of the actual packet content. SysLog is usually text based stuff, like "port eth0 blocked packet from ip w.x.y.z" - Wireshark is not made for analyzing that kind of thing. You'd better be using logging systems like Splunk to store and search through those kinds of messages (they have filters that slightly remind of Wireshark display filters, too).</p><p>So unless your text file contains the packet bytes you're not going to have much luck with text2pcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-37893" class="comments-container"><span id="37894"></span><div id="comment-37894" class="comment"><div id="post-37894-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. I have just warmed up to WireShark and like how you can search for specifics. I'll give Splunk a shot.</p></div><div id="comment-37894-info" class="comment-info"><span class="comment-age">(17 Nov '14, 01:31)</span> <span class="comment-user userinfo">SJISP</span></div></div></div><div id="comment-tools-37893" class="comment-tools"></div><div class="clear"></div><div id="comment-37893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

