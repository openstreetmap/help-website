+++
type = "question"
title = "Source Problem"
description = '''Hey guys, I am new to wireshark and having some problems.  I am trying to capture some packets on my personal computer and i go to url and type int a web address like facebook.com and when i go to look for syn packets i cant find just the syn packet. It has syn,ack and there is non with the source a...'''
date = "2014-02-03T08:21:00Z"
lastmod = "2014-02-03T08:34:00Z"
weight = 29397
keywords = [ "source", "capture-filter", "ip" ]
aliases = [ "/questions/29397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Source Problem](/questions/29397/source-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys, I am new to wireshark and having some problems.<br />
</p><p>I am trying to capture some packets on my personal computer and i go to url and type int a web address like facebook.com and when i go to look for syn packets i cant find just the syn packet. It has syn,ack and there is non with the source as my ip. I know there has to be one. Please help.</p></div><div id="question-tags" class="tags-container tags">source capture-filter ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '14, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/4fe86e061c2d50c958e1bcc8d1a17355?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zerotolerance&#39;s gravatar image" /><p>zerotolerance<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zerotolerance has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29397" class="comments-container"><span id="29400"></span><div id="comment-29400" class="comment"><div id="post-29400-score" class="comment-score"></div><div class="comment-text"><p>Ok i fixed the problem. It was my VPN software that was blocking everything.</p></div><div id="comment-29400-info" class="comment-info"><span class="comment-age">(03 Feb '14, 09:24)</span> zerotolerance</div></div></div><div id="comment-tools-29397" class="comment-tools"></div><div class="clear"></div><div id="comment-29397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29398"></span>

<div id="answer-container-29398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29398-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i cant find just the syn packet.</p></blockquote><p>If there is <strong>really</strong> only the SYN frame, it could be due to TCP/IP offloading. See the following link.</p><blockquote><p><a href="http://ask.wireshark.org/questions/13131/wireshark-does-not-capture-packets-w-payloads">http://ask.wireshark.org/questions/13131/wireshark-does-not-capture-packets-w-payloads</a></p></blockquote><p>However, as you say that you <strong>can see</strong> SYN-ACK frames, what do you see, if you right click the SYN frame and then select "Follow TCP stream"?</p><p>Is it possible to post the capture file somewhere (google drive, dropbox, cloudshark.org)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '14, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Feb '14, 08:36</p></div></div><div id="comments-container-29398" class="comments-container"></div><div id="comment-tools-29398" class="comment-tools"></div><div class="clear"></div><div id="comment-29398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

