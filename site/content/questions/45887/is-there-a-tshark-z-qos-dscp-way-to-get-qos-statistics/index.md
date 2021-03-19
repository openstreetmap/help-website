+++
type = "question"
title = "Is there a tshark -z QOS | DSCP  way to get QOS statistics?"
description = '''Basically i&#x27;m looking to answer the following question on many large, tracefiles:  what value did the ip.dsfield.dscp have for each packet, so i can answer questions as , what percentage of the traffic was in Expedited Forwarding and what in other classes etc. tshark -z would be great to gather thes...'''
date = "2015-09-16T12:32:00Z"
lastmod = "2015-09-17T08:15:00Z"
weight = 45887
keywords = [ "ip.dsfield.dscp", "qos", "tshark", "dscp", "-z" ]
aliases = [ "/questions/45887" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a tshark -z QOS | DSCP way to get QOS statistics?](/questions/45887/is-there-a-tshark-z-qos-dscp-way-to-get-qos-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45887-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Basically i'm looking to answer the following question on many large, tracefiles: what value did the <code>ip.dsfield.dscp</code> have for each packet, so i can answer questions as , what percentage of the traffic was in Expedited Forwarding and what in other classes etc. <code>tshark -z</code> would be great to gather these, would it not? Or is there a way to count a certain field in tshark?</p></div><div id="question-tags" class="tags-container tags">ip.dsfield.dscp qos tshark dscp -z</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '15, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-45887" class="comments-container"></div><div id="comment-tools-45887" class="comment-tools"></div><div class="clear"></div><div id="comment-45887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45922"></span>

<div id="answer-container-45922" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45922-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>By now , i've read up on some of Sake's Blok and Joke Snelders' work and this looks promising:</p><p><code>tshark -r test.pkt -q -z io,stat,300,COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==48",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==46",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==34",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==32",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==26",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==24",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==18",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==16",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==10",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==8",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==4",COUNT"(ip.dsfield.dscp)ip.dsfield.dscp&amp;&amp;ip.dsfield.dscp==0"</code></p><p><img src="https://osqa-ask.wireshark.org/upfiles/dscpfields_QKRCLnn.png" alt="alt text" /></p><p>now lets check if the values found are the right amounts ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '15, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></img></div></div><div id="comments-container-45922" class="comments-container"><span id="45941"></span><div id="comment-45941" class="comment"><div id="post-45941-score" class="comment-score"></div><div class="comment-text"><p>Right, so the values check out, now i've worked it over &gt; 580 traces, got a substantial txt doc,</p><p><code>0.0 &lt;&gt; 118.9 |  5602 |  4024 |  9096 |     0 |  7162 |     0 |    56 |     0 |     0 |     0 |     0 | 1814545 |</code></p><p>did a FIND for <code>0.0 &lt;&gt;</code> then a copy results to new file in PSPAD, use the <code>|</code> as a delimiter to work it in a spreadsheet .. .. hmm , i might just start marking my own comment as an answer ..</p></div><div id="comment-45941-info" class="comment-info"><span class="comment-age">(18 Sep '15, 01:03)</span> Marc</div></div></div><div id="comment-tools-45922" class="comment-tools"></div><div class="clear"></div><div id="comment-45922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

