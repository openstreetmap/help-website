+++
type = "question"
title = "Syntax for Multiple Ports In Filter"
description = '''I am trying look for all the ports used by Fifa 12. I am using https://help.ea.com/article/fifa-12-online-ports for the information. Is this the best way look for the information for a PC communications as follows? (udp.port==9565)||(udp.port==9570)||(udp.port==6000)||(tcp.port==9946)||(tcp.port==99...'''
date = "2012-05-07T17:56:00Z"
lastmod = "2012-05-08T01:56:00Z"
weight = 10759
keywords = [ "fifa12" ]
aliases = [ "/questions/10759" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Syntax for Multiple Ports In Filter](/questions/10759/syntax-for-multiple-ports-in-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10759-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying look for all the ports used by Fifa 12. I am using <a href="https://help.ea.com/article/fifa-12-online-ports">https://help.ea.com/article/fifa-12-online-ports</a> for the information. Is this the best way look for the information for a PC communications as follows?</p><p>(udp.port==9565)||(udp.port==9570)||(udp.port==6000)||(tcp.port==9946)||(tcp.port==9988)||(tcp.port==42124)||(tcp.port&gt;=10000)||(tcp.port&lt;=20000)</p></div><div id="question-tags" class="tags-container tags">fifa12</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/b47fc9ff10b938b2c04a2f791094637b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Perceptus&#39;s gravatar image" /><p>Perceptus<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Perceptus has no accepted answers">0%</span></p></div></div><div id="comments-container-10759" class="comments-container"></div><div id="comment-tools-10759" class="comment-tools"></div><div class="clear"></div><div id="comment-10759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10769"></span>

<div id="answer-container-10769" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10769-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If one uses tcp.port, then both source and destination port will match, which makes it impossible to define a valid range, as the source port will be random and might match as well (and possibly more often than the intended destination port)</p><p>This rather long filter will match better (tested on the sample below):</p><blockquote><p><code>udp.port==9565 or udp.port==9570 or udp.port==6000 or tcp.port==9946 or tcp.port==9988 or tcp.port==42124 or</code> <strong><code>((tcp.dstport&gt;=10000 and tcp.dstport&lt;=20000) or (tcp.srcport&gt;=10000 and tcp.srcport&lt;=20000))</code></strong><br />
</p></blockquote><p>BEWARE: You need both tcp.dstport and tcp.srcport, to get packets of both directions.</p><p>This filter will also match for source ports in that range. However, you can't prevent that without further scripting.</p><p>EDIT: Test file: <strong><a href="http://cloudshark.org/captures/bd90209e690f">http://cloudshark.org/captures/bd90209e690f</a></strong><br />
</p><p>The display filter can be tested within cloudshark ;-) If you apply the filter, you won't see packets with port 30000, which appear first in frame 87. With the filter 'tcp.flags eq 0x02' you will see the ports used in that capture file.</p><p><strong>EDIT2</strong>: As <strong>Jasper</strong> already mentioned above, this filter will do as well :-))</p><blockquote><p><code>udp.port==9565 or udp.port==9570 or udp.port==6000 or tcp.port==9946 or tcp.port==9988 or tcp.port==42124 or (tcp.port&gt;=10000 and tcp.port&lt;=20000)</code><br />
</p></blockquote><p>as it's equivalent to my much longer filter! Sorry for any confusion ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '12, 03:28</p></div></div><div id="comments-container-10769" class="comments-container"><span id="10787"></span><div id="comment-10787" class="comment"><div id="post-10787-score" class="comment-score"></div><div class="comment-text"><p>That is excellent information. Can I use that also for a capture filter?</p></div><div id="comment-10787-info" class="comment-info"><span class="comment-age">(08 May '12, 11:34)</span> Perceptus</div></div><span id="10801"></span><div id="comment-10801" class="comment"><div id="post-10801-score" class="comment-score"></div><div class="comment-text"><p>Yes, but the syntax is different.</p><blockquote><p><code>udp port 9565 or udp port 9570 or udp port 6000 or tcp port 9946 or tcp port 9988 or tcp port 42124 or tcp portrange 10000-20000</code><br />
</p></blockquote><p><strong>portrange</strong> works at least with 1.7.1. (just tested). If it does not work with an earlier versions (not checked), please upgrade.</p></div><div id="comment-10801-info" class="comment-info"><span class="comment-age">(08 May '12, 22:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10769" class="comment-tools"></div><div class="clear"></div><div id="comment-10769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10767"></span>

<div id="answer-container-10767" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10767-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That last bit "(tcp.port&gt;=10000)||(tcp.port&lt;=20000)" just opens up the filter to all TCP ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-10767" class="comments-container"><span id="10768"></span><div id="comment-10768" class="comment"><div id="post-10768-score" class="comment-score"></div><div class="comment-text"><p>probably the "or" should be an "and", but then the range needs to be put in additional brackets.</p></div><div id="comment-10768-info" class="comment-info"><span class="comment-age">(08 May '12, 01:15)</span> Jasper ♦♦</div></div></div><div id="comment-tools-10767" class="comment-tools"></div><div class="clear"></div><div id="comment-10767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

