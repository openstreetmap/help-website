+++
type = "question"
title = "how do i capture packets of two hosts"
description = '''how do i capture packets between two hosts? once packets are captured, how do i know the cause of the problem? like email alerts sent from Oracle server to Exchange server sometimes fail. is there something like a reference that i can compare against my captured packets?'''
date = "2014-02-26T00:51:00Z"
lastmod = "2014-02-27T05:23:00Z"
weight = 30198
keywords = [ "oracle", "exchange" ]
aliases = [ "/questions/30198" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how do i capture packets of two hosts](/questions/30198/how-do-i-capture-packets-of-two-hosts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30198-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how do i capture packets between two hosts?</p><p>once packets are captured, how do i know the cause of the problem? like email alerts sent from Oracle server to Exchange server sometimes fail. is there something like a reference that i can compare against my captured packets?</p></div><div id="question-tags" class="tags-container tags">oracle exchange</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '14, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/3e2476d65272d249cef41ccd62720b8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rino19ny&#39;s gravatar image" /><p>rino19ny<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rino19ny has no accepted answers">0%</span></p></div></div><div id="comments-container-30198" class="comments-container"></div><div id="comment-tools-30198" class="comment-tools"></div><div class="clear"></div><div id="comment-30198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30230"></span>

<div id="answer-container-30230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30230-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how do i capture packets between two hosts?</p></blockquote><p>by following the steps described here: <strong><a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></strong></p><p>and here: <strong><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></strong> or <strong><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></strong> whatever applies in your environment.</p><blockquote><p>once packets are captured, how do i know the cause of the problem?</p></blockquote><p>by analyzing the problem description, then 'mapping' that description to involved protocols (http, smtp, whatever) and finally by looking at the matching connections between the involved systems (Oracle and/or mail sever).</p><blockquote><p>is there something like a reference that i can compare against my captured packets?</p></blockquote><p>Most certainly no, as every network is different. However, you should learn something about the basic protocols (IP, TCP, UDP, http, smtp, etc.). With that knowledge (and some experience), you should be able to figure out if the connection you are analyzing shows any problem.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30230" class="comments-container"></div><div id="comment-tools-30230" class="comment-tools"></div><div class="clear"></div><div id="comment-30230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

