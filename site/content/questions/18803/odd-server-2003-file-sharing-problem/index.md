+++
type = "question"
title = "Odd Server 2003 File Sharing Problem"
description = '''Hi, We are having a very weird issue that has been going on for a number of months on our network. We currently have a 3 Windows Server 2003 servers that have connectivity issues between them. We have a .Net app that monitors a folder via a network share on another server and the .net app seems to h...'''
date = "2013-02-21T10:59:00Z"
lastmod = "2013-02-21T13:13:00Z"
weight = 18803
keywords = [ "windows", "2003" ]
aliases = [ "/questions/18803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Odd Server 2003 File Sharing Problem](/questions/18803/odd-server-2003-file-sharing-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are having a very weird issue that has been going on for a number of months on our network. We currently have a 3 Windows Server 2003 servers that have connectivity issues between them.</p><p>We have a .Net app that monitors a folder via a network share on another server and the .net app seems to hang periodically for about 33 seconds.</p><p>I've downloaded and installed Wireshark and I can find what I believe the problem packets however I can't understand why this is happening. Here is a copy/paste from our wireshark capture:</p><p>44133 2013-02-21 10:27:34.948610000 408.427221000 53.248.98.58 53.248.98.60 TCP 54 appworxsrv &gt; microsoft-ds [ACK] Seq=18552 Ack=39734 Win=65077 Len=0</p><p>44693 2013-02-21 10:28:08.416593000 441.895204000 53.248.98.58 53.248.98.60 TCP 54 appworxsrv &gt; microsoft-ds [FIN, ACK] Seq=18552 Ack=39734 Win=65077 Len=0</p><p>44694 2013-02-21 10:28:08.416658000 441.895269000 53.248.98.60 53.248.98.58 TCP 60 microsoft-ds &gt; appworxsrv [FIN, ACK] Seq=39734 Ack=18553 Win=65283 Len=0</p><p>44695 2013-02-21 10:28:08.416670000 441.895281000 53.248.98.58 53.248.98.60 TCP 54 appworxsrv &gt; microsoft-ds [ACK] Seq=18553 Ack=39735 Win=65077 Len=0</p><p>If you look at the time between 44133 and 44693 this is where the time delay is occuring but I don't know why.</p><p>Any ideas or help would be appreciated.</p><p>Kevin</p></div><div id="question-tags" class="tags-container tags">windows 2003</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '13, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/0e65e537256654384be2035887749f42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KPMoore&#39;s gravatar image" /><p>KPMoore<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KPMoore has no accepted answers">0%</span></p></div></div><div id="comments-container-18803" class="comments-container"></div><div id="comment-tools-18803" class="comment-tools"></div><div class="clear"></div><div id="comment-18803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18805"></span>

<div id="answer-container-18805" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18805-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt that the packets you have quoted are a cause for your delay. What you have is a packet coming from 53.248.98.58 with no payload (Len=0), so there is no need for 53.248.98.60 to acknowledge it. Then, we again see a packet from 53.248.98.58, which is about 34 seconds late, but it is a FIN packet, tearing down the connection from this side. That ususally happens when a node realizes that the TCP session is not needed for any more data transfers and torn down - a typical and quite normal time out trigger. The rest is just the usualy FIN-ACK-FIN-ACK procedure, so nothing special there, either. By that time, the application has to have all the data it needs, otherwise there would not be a FIN-ACK teardown.</p><p>I agree that the delay of 34 seconds is curious since you said that it is about the time your transfer hangs, but you should probably look for the reason in another place. What you need to look for are data packets that are either sent out with a delay instead of right away, or the same for late arrival of acknowledges that slow down the sender's performance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '13, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18805" class="comments-container"><span id="18806"></span><div id="comment-18806" class="comment"><div id="post-18806-score" class="comment-score"></div><div class="comment-text"><p>Jasper,</p><p>Thank you for your analysis. This issue has me quite stumped and I'll go back and review the wireshark log to see if there are any other packets that could indicate a problem and I'll post a follow up in a bit.</p><p>Thanks, Kevin</p></div><div id="comment-18806-info" class="comment-info"><span class="comment-age">(21 Feb '13, 13:52)</span> KPMoore</div></div></div><div id="comment-tools-18805" class="comment-tools"></div><div class="clear"></div><div id="comment-18805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

