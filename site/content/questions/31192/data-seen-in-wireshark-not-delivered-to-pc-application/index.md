+++
type = "question"
title = "Data seen in wireshark not delivered to PC application"
description = '''Hi, I can see the data in wireshark trace but the same is not received by application. here is the setup I am using: Access Point Detail (Router) Subnet Mask : 255.255.255.0 Default Gateway : 192.168.1.1 Device connected to Access Point:  Computer :-  IP : 192.168.1.80  Subnet Mask : 255.255.255.0  ...'''
date = "2014-03-26T10:14:00Z"
lastmod = "2014-03-27T11:46:00Z"
weight = 31192
keywords = [ "c#", "udp", "c++", "tcp" ]
aliases = [ "/questions/31192" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Data seen in wireshark not delivered to PC application](/questions/31192/data-seen-in-wireshark-not-delivered-to-pc-application)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31192-score" class="post-score" title="current number of votes">0</div><span id="post-31192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I can see the data in wireshark trace but the same is not received by application. here is the setup I am using:</p><p>Access Point Detail (Router) Subnet Mask : 255.255.255.0 Default Gateway : 192.168.1.1</p><p>Device connected to Access Point:</p><ol><li>Computer :- IP : 192.168.1.80 Subnet Mask : 255.255.255.0 Default Gateway : 192.168.1.1</li><li>Adapter 1 :- IP : 192.168.1.81(IP assigned by DHCP) Subnet Mask : 255.255.255.0 Default Gateway : 192.168.1.1</li><li>Adapter 2 :- IP : 192.168.4.32(Static IP) Subnet Mask : 255.255.255.0 Default Gateway : 192.168.4.1</li></ol><p>So my application(Devloped in c++ and C#) running on PC(UDP) can only see the data coming form Adapter 1 and do not see any data from Adapter 2, whereas wireshark can see data from both the adapter. How can my application can receive data from both the adapter like wireshark does.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/1e39d85521d9a567ab332dfa70249f80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shanky&#39;s gravatar image" /><p><span>Shanky</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shanky has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '14, 10:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-31192" class="comments-container"></div><div id="comment-tools-31192" class="comment-tools"></div><div class="clear"></div><div id="comment-31192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31193"></span>

<div id="answer-container-31193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31193-score" class="post-score" title="current number of votes">0</div><span id="post-31193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My Q+D answer:</p><p>Reading the data from the adapters depends completely on how you've coded your application so that it will get data from both adapters. That is,you have to use the proper library calls to open/read from each of the adapters.</p><p>How Wireshark reads from the adapters is not relevant with respect to your application program.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '14, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-31193" class="comments-container"><span id="31194"></span><div id="comment-31194" class="comment"><div id="post-31194-score" class="comment-score"></div><div class="comment-text"><p>To expand a little on Bill's comment, your app will need to bind to both IP's or listen on the 0.0.0.0 (all IP's) address.</p><p>But this is nothing to do with Wireshark as that uses completely different methods to capture traffic as opposed to a socket using app.</p></div><div id="comment-31194-info" class="comment-info"><span class="comment-age">(26 Mar '14, 10:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="31195"></span><div id="comment-31195" class="comment"><div id="post-31195-score" class="comment-score"></div><div class="comment-text"><p>To add my two cents...</p><p>What is the output of the following command if you run it in an elevated <del>DoS</del> DOS box (I assume Windows because of C#).</p><blockquote><p>netstat -nab</p></blockquote><p>Locate the line(s) with the port number of your application and post those lines here or draw your own conclusions from that output.</p></div><div id="comment-31195-info" class="comment-info"><span class="comment-age">(26 Mar '14, 10:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31197"></span><div id="comment-31197" class="comment"><div id="post-31197-score" class="comment-score"></div><div class="comment-text"><blockquote><p>My <strong>Q+D</strong> answer:</p></blockquote><p>Q+D ??</p></div><div id="comment-31197-info" class="comment-info"><span class="comment-age">(26 Mar '14, 10:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31200"></span><div id="comment-31200" class="comment"><div id="post-31200-score" class="comment-score"></div><div class="comment-text"><p>= Quick and Dirty</p></div><div id="comment-31200-info" class="comment-info"><span class="comment-age">(26 Mar '14, 10:56)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="31232"></span><div id="comment-31232" class="comment"><div id="post-31232-score" class="comment-score"></div><div class="comment-text"><p>obvious, now that you mention it ;-)</p></div><div id="comment-31232-info" class="comment-info"><span class="comment-age">(27 Mar '14, 11:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31193" class="comment-tools"></div><div class="clear"></div><div id="comment-31193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

