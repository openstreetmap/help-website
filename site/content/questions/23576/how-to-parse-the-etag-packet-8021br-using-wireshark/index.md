+++
type = "question"
title = "how to parse the Etag packet (802.1br) using wireshark?"
description = '''hi all, I want to use the wireshark to parse/identify the Etag packets, but the wireshark cannot do it, i want to know if the tool can support etag/802.1br packets? if support, how should i do ? thanks a lot'''
date = "2013-08-06T01:39:00Z"
lastmod = "2013-08-08T06:12:00Z"
weight = 23576
keywords = [ "parse", "etag", "802.1br" ]
aliases = [ "/questions/23576" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to parse the Etag packet (802.1br) using wireshark?](/questions/23576/how-to-parse-the-etag-packet-8021br-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23576-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>I want to use the wireshark to parse/identify the Etag packets, but the wireshark cannot do it, i want to know if the tool can support etag/802.1br packets? if support, how should i do ? thanks a lot</p></div><div id="question-tags" class="tags-container tags">parse etag 802.1br</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '13, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/8ab61bb30d5effb9eb07247fb3516504?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="python1983&#39;s gravatar image" /><p>python1983<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="python1983 has no accepted answers">0%</span></p></div></div><div id="comments-container-23576" class="comments-container"></div><div id="comment-tools-23576" class="comment-tools"></div><div class="clear"></div><div id="comment-23576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23641"></span>

<div id="answer-container-23641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23641-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Currently there is no 802.1br support in Wireshark. You will be able to <strong>capture</strong> that traffic, but Wireshark will not know how to decode 802.1br packets.</p><p>BTW: is it possible to post a sample capture file somewhere (google docs, dropbox, cloudshark.org)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23641" class="comments-container"><span id="23642"></span><div id="comment-23642" class="comment"><div id="post-23642-score" class="comment-score"></div><div class="comment-text"><p>Or add a enhancement request in our bug tracker attaching a sample trace.</p></div><div id="comment-23642-info" class="comment-info"><span class="comment-age">(08 Aug '13, 06:16)</span> Anders ♦</div></div></div><div id="comment-tools-23641" class="comment-tools"></div><div class="clear"></div><div id="comment-23641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

