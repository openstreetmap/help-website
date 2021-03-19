+++
type = "question"
title = "1st packet"
description = '''Hello, I would like to know when your looking at a packet if it&#x27;s the very first packet. I know how to do this when its TCP but when I am looking at other protocols how do I find this info?  Thanks,'''
date = "2015-09-02T05:21:00Z"
lastmod = "2015-09-07T16:49:00Z"
weight = 45594
keywords = [ "firstpacket" ]
aliases = [ "/questions/45594" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [1st packet](/questions/45594/1st-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45594-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to know when your looking at a packet if it's the very first packet. I know how to do this when its TCP but when I am looking at other protocols how do I find this info?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">firstpacket</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '15, 05:21</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p>rock90<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-45594" class="comments-container"><span id="45604"></span><div id="comment-45604" class="comment"><div id="post-45604-score" class="comment-score"></div><div class="comment-text"><p>"First packet" in what sense? First packet of some protocol exchange?</p></div><div id="comment-45604-info" class="comment-info"><span class="comment-age">(02 Sep '15, 14:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-45594" class="comment-tools"></div><div class="clear"></div><div id="comment-45594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45680"></span>

<div id="answer-container-45680" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45680-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Identifying the first packet in a session oriented protocol (like TCP) is easy, as there is a defined session start (like TCP SYN) and a defined session end (like TCP FIN/RESET). <strong>However</strong> for session-less protocols (like UDP) there is no common definition of a first packet. All you can say, that it's the first/last packet within a certain time window. So, to find the first packet of "other protocols", you'll have to define the time window you're interested in and then simply find the frist protocol frame in that time period.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45680" class="comments-container"></div><div id="comment-tools-45680" class="comment-tools"></div><div class="clear"></div><div id="comment-45680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

