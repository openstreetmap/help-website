+++
type = "question"
title = "How do I use filter on the command line"
description = '''I am trying use filter like this. But it return error on -R options? It looks like it doesn&#x27;t like brackets any clues how the syntax should be? &quot;C:&#92;Program files&#92;Wireshark&#92;wireshark&quot; -r &quot;2012-07-27_154856_10.36.1.210_4.pcap&quot; -R &quot;(ip.addr==x.x.x.x and gtp) || ( ranap.gTP_TEI == 0x000059ca or sctp.por...'''
date = "2012-08-01T01:52:00Z"
lastmod = "2012-08-01T02:17:00Z"
weight = 13212
keywords = [ "line", "command", "filters" ]
aliases = [ "/questions/13212" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I use filter on the command line](/questions/13212/how-do-i-use-filter-on-the-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying use filter like this. But it return error on -R options? It looks like it doesn't like brackets any clues how the syntax should be?</p><p>"C:\Program files\Wireshark\wireshark" -r "2012-07-27_154856_10.36.1.210_4.pcap" -R "(ip.addr==x.x.x.x and gtp) || ( ranap.gTP_TEI == 0x000059ca or sctp.port==xxxxxx and (frame.time &gt; "Jul 27, 2012 16:36:00" and frame.time &lt; "July 27, 2012 16:38:00"))"</p></div><div id="question-tags" class="tags-container tags">line command filters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '12, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/e0e2dc23842e8a3a3b6437eafa10cdfd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dees&#39;s gravatar image" /><p>Dees<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dees has no accepted answers">0%</span></p></div></div><div id="comments-container-13212" class="comments-container"></div><div id="comment-tools-13212" class="comment-tools"></div><div class="clear"></div><div id="comment-13212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13214"></span>

<div id="answer-container-13214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13214-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is the use of quotes, not the brackets. You need to escape the inner quotes with \", otherwise the DOS commandline get's confused. Please try this:</p><blockquote><p><code>"C:\Program files\Wireshark\wireshark" -r "2012-07-27_154856_10.36.1.210_4.pcap" -R "(ip.addr==x.x.x.x and gtp) || ( ranap.gTP_TEI == 0x000059ca or sctp.port==xxxx and (frame.time &gt; \"Jul 27, 2012 16:36:00\" and frame.time &lt; \"July 27, 2012 16:38:00\"))"</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13214" class="comments-container"><span id="13216"></span><div id="comment-13216" class="comment"><div id="post-13216-score" class="comment-score"></div><div class="comment-text"><p>Its still giving same error.</p><p>Unexpected end of filter string</p><p>The filter expression "(ip.addr=192.168.0.1 and gtp) || (" isn't a valid display filter.</p></div><div id="comment-13216-info" class="comment-info"><span class="comment-age">(01 Aug '12, 02:23)</span> Dees</div></div><span id="13220"></span><div id="comment-13220" class="comment"><div id="post-13220-score" class="comment-score"></div><div class="comment-text"><p>it works on my Win 7 system. What is your OS? Maybe you should use OR instead of ||.</p></div><div id="comment-13220-info" class="comment-info"><span class="comment-age">(01 Aug '12, 02:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13214" class="comment-tools"></div><div class="clear"></div><div id="comment-13214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

