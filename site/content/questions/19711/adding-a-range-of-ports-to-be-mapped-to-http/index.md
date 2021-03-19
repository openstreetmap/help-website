+++
type = "question"
title = "Adding a range of ports to be mapped to http"
description = '''Hi, So this is similar to http://ask.wireshark.org/questions/6294/using-wireshark-to-debug-http-traffic-on-a-non-standard-port and http://ask.wireshark.org/questions/12360/mapping-a-well-known-protocol-to-a-custom-port.  The difference is, I don&#x27;t have one or two ports that I would like to add as HT...'''
date = "2013-03-21T08:53:00Z"
lastmod = "2013-03-21T08:57:00Z"
weight = 19711
keywords = [ "http", "mapping", "port" ]
aliases = [ "/questions/19711" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding a range of ports to be mapped to http](/questions/19711/adding-a-range-of-ports-to-be-mapped-to-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19711-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>So this is similar to <a href="http://ask.wireshark.org/questions/6294/using-wireshark-to-debug-http-traffic-on-a-non-standard-port">http://ask.wireshark.org/questions/6294/using-wireshark-to-debug-http-traffic-on-a-non-standard-port</a> and <a href="http://ask.wireshark.org/questions/12360/mapping-a-well-known-protocol-to-a-custom-port.">http://ask.wireshark.org/questions/12360/mapping-a-well-known-protocol-to-a-custom-port.</a></p><p>The difference is, I don't have one or two ports that I would like to add as HTTP. I need to add a range, something like 8000-26000.</p><p>Is this possible?</p></div><div id="question-tags" class="tags-container tags">http mapping port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/e407c0930a3a245340b42199b02a2c8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pattimus-prime&#39;s gravatar image" /><p>pattimus-prime<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pattimus-prime has one accepted answer">100%</span></p></div></div><div id="comments-container-19711" class="comments-container"></div><div id="comment-tools-19711" class="comment-tools"></div><div class="clear"></div><div id="comment-19711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19712"></span>

<div id="answer-container-19712" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19712-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just tried and it works.</p><p>To answer my own question:</p><p>In Wireshark do:</p><p>Edit -&gt; Preferences -&gt; Protocols -&gt; HTTP</p><p>TCP Ports:</p><p>80,3128,3132,5985,11371,1900,2869,2710,8000-26000</p><p>And now for example, a request sent to my webserver on port 19620 is properly marked as HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/e407c0930a3a245340b42199b02a2c8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pattimus-prime&#39;s gravatar image" /><p>pattimus-prime<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pattimus-prime has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '13, 08:57</p></div></div><div id="comments-container-19712" class="comments-container"></div><div id="comment-tools-19712" class="comment-tools"></div><div class="clear"></div><div id="comment-19712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

