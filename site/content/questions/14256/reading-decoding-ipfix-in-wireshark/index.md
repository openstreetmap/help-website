+++
type = "question"
title = "reading (decoding?) IPFIX in wireshark"
description = '''Hey, I can detect CFLOW messages in wireshark and they have the information I need,like the src address, dest address etc but when I do Follow UDP Stream the output in ASCII are characters like these &quot;.J.B......2........&quot; for example. So does anyone know if there is a way to decode these characters ...'''
date = "2012-09-13T23:08:00Z"
lastmod = "2012-11-01T12:08:00Z"
weight = 14256
keywords = [ "netflow" ]
aliases = [ "/questions/14256" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [reading (decoding?) IPFIX in wireshark](/questions/14256/reading-decoding-ipfix-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14256-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I can detect CFLOW messages in wireshark and they have the information I need,like the src address, dest address etc but when I do Follow UDP Stream the output in ASCII are characters like these ".J.B......2........" for example. So does anyone know if there is a way to decode these characters to get something useful out of them.</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">netflow</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '12, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/d5cbfa5e042d44586040d1d76c6d9f89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="remit&#39;s gravatar image" /><p>remit<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="remit has no accepted answers">0%</span></p></div></div><div id="comments-container-14256" class="comments-container"><span id="15473"></span><div id="comment-15473" class="comment"><div id="post-15473-score" class="comment-score"></div><div class="comment-text"><p>If you find out, <em>I</em> would love to know as well!</p></div><div id="comment-15473-info" class="comment-info"><span class="comment-age">(01 Nov '12, 09:57)</span> BWB8771</div></div></div><div id="comment-tools-14256" class="comment-tools"></div><div class="clear"></div><div id="comment-14256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15475"></span>

<div id="answer-container-15475" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15475-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Follow TCP Stream" and "Follow UDP Stream" serve two purposes. The main purpose is to show a simple display of <em>text-based</em> protocols; a secondary purpose is that they also filter the display to show the packets in a given TCP or UDP conversation.</p><p>The first of those purposes is <em>not</em> useful for non-text-based protocols. For non-text-based protocols, you just use the packet dissection, as shown in the packet summary and packet details pane. The ASCII characters - or rather the raw bytes corresponding to them - are decoded by the Wireshark dissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15475" class="comments-container"></div><div id="comment-tools-15475" class="comment-tools"></div><div class="clear"></div><div id="comment-15475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

