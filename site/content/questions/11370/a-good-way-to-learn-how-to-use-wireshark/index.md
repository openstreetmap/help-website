+++
type = "question"
title = "A good way to learn how to use wireshark"
description = '''I&#x27;m new to wireshark, and I&#x27;d like to learn how to use it properly. I&#x27;m going to use wireshark to reverse-engineer communication protocols of applications, and I&#x27;d like to see an applied sample on how to do this. I&#x27;ve tried to use Wireshark to reverse engeneer communication between zynga pocker clie...'''
date = "2012-05-26T01:01:00Z"
lastmod = "2012-05-26T09:20:00Z"
weight = 11370
keywords = [ "protocol", "reverse-engineering" ]
aliases = [ "/questions/11370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [A good way to learn how to use wireshark](/questions/11370/a-good-way-to-learn-how-to-use-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to wireshark, and I'd like to learn how to use it properly.</p><p>I'm going to use wireshark to reverse-engineer communication protocols of applications, and I'd like to see an applied sample on how to do this.</p><p>I've tried to use Wireshark to reverse engeneer communication between zynga pocker client, and the server, and I run into a problem: how can I know, which packets belong to which applications?</p><p>Also, can anyone recommend/write a tutorial, which concerns itself with reverse engeneering protocols?</p></div><div id="question-tags" class="tags-container tags">protocol reverse-engineering</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '12, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/ac14814bcfc842f847af55f9b3ad55b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="menkaur&#39;s gravatar image" /><p>menkaur<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="menkaur has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 May '12, 01:01</p></div></div><div id="comments-container-11370" class="comments-container"></div><div id="comment-tools-11370" class="comment-tools"></div><div class="clear"></div><div id="comment-11370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11377"></span>

<div id="answer-container-11377" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11377-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>A good way to learn how to use wireshark</p></blockquote><p>there are several ways to start:</p><ul><li>Read the <a href="http://www.wiresharkbook.com/">wireshark book</a></li><li>Watch video tutorials. <a href="http://wiresharkdownloads.riverbed.com/video/wireshark/introduction-to-wireshark/">Tutorial #1</a> <a href="http://www.youtube.com/watch?v=NHLTa29iovU">Tutorial #2</a></li><li>Work with Wireshark</li></ul><blockquote><p>reverse engeneer communication between zynga pocker client, and the server, and I run into a problem: <strong>how can I know, which packets belong to which applications?</strong></p></blockquote><p>Reverse engineering a network protocol requires a lot of experience with other network protocols and with client-server architectures in general. You won't learn that in a simple tutorial. So, there is only the hard way, by analyzing the traffic and observing the action/reaction of the client/server.</p><p>If the protocol is unknown to wireshark it will only show the network traffic in HEX and you need to figure out if there are any recurring pattern. You can do that manually, or you can use some advanced techniques. Have a look at this video tutorial: "DEFCON 13: Reverse Engineering Network Protocols using Bioinformatics"</p><blockquote><p><code>http://www.youtube.com/watch?v=A3zP5l6TZhc</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '12, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 May '12, 13:28</p></div></div><div id="comments-container-11377" class="comments-container"></div><div id="comment-tools-11377" class="comment-tools"></div><div class="clear"></div><div id="comment-11377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

