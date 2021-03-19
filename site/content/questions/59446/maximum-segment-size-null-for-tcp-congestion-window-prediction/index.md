+++
type = "question"
title = "Maximum segment size NULL for TCP congestion window prediction"
description = '''I am using the formula you see on the attached paper (link: https://drive.google.com/file/d/0B4Ajk8jGD1OxWnORG9iMG0xSEFudWcXd3X2p1Yy1FNkJr/view ) to predict a congestion window (cwnd). However, I am confused with the value of the MSS (maximum segment size) on the segments where the MSS is NULL. I am...'''
date = "2017-02-15T15:32:00Z"
lastmod = "2017-02-15T16:56:00Z"
weight = 59446
keywords = [ "congestion", "wireshark", "ask.wireshark.org", "tcp-mss-options" ]
aliases = [ "/questions/59446" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Maximum segment size NULL for TCP congestion window prediction](/questions/59446/maximum-segment-size-null-for-tcp-congestion-window-prediction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59446-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the formula you see on the attached paper (link: <a href="https://drive.google.com/file/d/0B4Ajk8jGD1OxWnORG9iMG0xSEFudWcXd3X2p1Yy1FNkJr/view">https://drive.google.com/file/d/0B4Ajk8jGD1OxWnORG9iMG0xSEFudWcXd3X2p1Yy1FNkJr/view</a> ) to predict a congestion window (cwnd). However, I am confused with the value of the MSS (maximum segment size) on the segments where the MSS is NULL. I am using iperf to generate the traffic (sending from a client to a server and capture the traffic on the edge of the network). What is causing for the value of MSS to be NULL?</p><p>Link to the full paper: <a href="https://drive.google.com/open?id=0BAjk8jGDxOVNRTGpNUVdyVnZsaGZ6ZzdOc2NUdWZELW13">https://drive.google.com/open?id=0BAjk8jGDxOVNRTGpNUVdyVnZsaGZ6ZzdOc2NUdWZELW13</a></p><p>The formula they have used in the paper is on the second column of page 2. Or is there any other formula to predict cwnd from a passive traffic?</p></div><div id="question-tags" class="tags-container tags">congestion wireshark ask.wireshark.org tcp-mss-options</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '17, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '17, 06:50</p></div></div><div id="comments-container-59446" class="comments-container"></div><div id="comment-tools-59446" class="comment-tools"></div><div class="clear"></div><div id="comment-59446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59451"></span>

<div id="answer-container-59451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59451-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MSS is a TCP option. The MSS is negotiated early in a connection, so the MSS option only appears in a few packets. The other packets don't include any MSS information.</p><p>If you need the MSS to analyze a connection, you will have to capture the initial setup of the connection, and remember the MSS value in the setup. If you don't capture the setup, you will not know the MSS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '17, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-59451" class="comments-container"><span id="59453"></span><div id="comment-59453" class="comment"><div id="post-59453-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "you will have to capture the initial setup of the connection, and remember the MSS value in the setup."? How do we do that on Wireshark?</p></div><div id="comment-59453-info" class="comment-info"><span class="comment-age">(15 Feb '17, 17:09)</span> armodes</div></div><span id="59455"></span><div id="comment-59455" class="comment"><div id="post-59455-score" class="comment-score">1</div><div class="comment-text"><p>To capture the initial setup of the connection, you will have to make sure Wireshark is doing a capture <em>before</em> iperf makes the connection. That's already being done.</p><p>To remember the MSS, you'll have to have whatever software is doing the analysis construct some data structure for each connection it sees and, if it sees an MSS option, attach that MSS value to the data structure. I.e., yes, you will have to write code.</p></div><div id="comment-59455-info" class="comment-info"><span class="comment-age">(15 Feb '17, 17:13)</span> Guy Harris ♦♦</div></div><span id="59456"></span><div id="comment-59456" class="comment"><div id="post-59456-score" class="comment-score"></div><div class="comment-text"><p>aha, OK i will do that. But the value of MSS should be 1460 all the time right? Does it have an impact on the ACK, sequence number and time stamp values?</p></div><div id="comment-59456-info" class="comment-info"><span class="comment-age">(15 Feb '17, 17:17)</span> armodes</div></div><span id="59457"></span><div id="comment-59457" class="comment"><div id="post-59457-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>But the value of MSS should be 1460 all the time right?</p></blockquote><p>Yes, once it's negotiated, it doesn't normally change. That doesn't mean that every packet will have an MSS option - the very fact that it doesn't change means that the MSS option isn't necessary once it's negotiated.</p><blockquote><p>Does it have an impact on the ACK, sequence number and time stamp values?</p></blockquote><p>No, except to the extent that it affects how big a TCP segment can be set and thus how much the sequence number (and thus the acknowledgment number) changes from packet to packet.</p></div><div id="comment-59457-info" class="comment-info"><span class="comment-age">(15 Feb '17, 17:22)</span> Guy Harris ♦♦</div></div><span id="59462"></span><div id="comment-59462" class="comment"><div id="post-59462-score" class="comment-score"></div><div class="comment-text"><p>For extra info about MSS please have a look here: <a href="https://crnetpackets.com/2016/01/27/the-relation-between-maximum-transmission-unit-mtu-and-the-maximum-segment-size-mss/">https://crnetpackets.com/2016/01/27/the-relation-between-maximum-transmission-unit-mtu-and-the-maximum-segment-size-mss/</a></p></div><div id="comment-59462-info" class="comment-info"><span class="comment-age">(15 Feb '17, 22:46)</span> Christian_R</div></div></div><div id="comment-tools-59451" class="comment-tools"></div><div class="clear"></div><div id="comment-59451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

