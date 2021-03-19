+++
type = "question"
title = "Observing the Round Trip Time Graph"
description = '''Hi everybody, I am trying to figure out how to find the most common RTT for a packets from sender and receiver and back. From what I observed from the RTT graph (Statistics | TCP StreamGraph | RTT graph), there is a horizontal straight line in the bottom of the graph, so is that the one called &quot;the ...'''
date = "2015-09-22T18:57:00Z"
lastmod = "2015-09-22T18:57:00Z"
weight = 46069
keywords = [ "rtt" ]
aliases = [ "/questions/46069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Observing the Round Trip Time Graph](/questions/46069/observing-the-round-trip-time-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>I am trying to figure out how to find the most common RTT for a packets from sender and receiver and back.</p><p>From what I observed from the RTT graph (Statistics | TCP StreamGraph | RTT graph), there is a horizontal straight line in the bottom of the graph, so is that the one called "the most common RTT" ?</p><p>Also I am not sure why some of the packet will have a much higher RTT value in a specific sequence number, what would cause this happen ? <strong>Updated:</strong> Just realized that those who have higher RTT value packets (outside the horizontal straight line) are all have a [ACK] flag...why a packets with a [ACK] flag would have a higher RTT ?</p><p>Thank you!</p><p>Here's the RTT graph of the trace file: <img src="https://osqa-ask.wireshark.org/upfiles/RTT_oKc8Irx.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">rtt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '15, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/e6ff2184109221c8715a8ede1bf5eacc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phantomcy&#39;s gravatar image" /><p>phantomcy<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phantomcy has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '15, 19:12</p></div></div><div id="comments-container-46069" class="comments-container"><span id="46090"></span><div id="comment-46090" class="comment"><div id="post-46090-score" class="comment-score"></div><div class="comment-text"><p>can you upload a sample capture file somewhere and post the link here? If the file contains sensitive information, please use TraceWrangler (tracewrangler.com) to anonymize it.</p></div><div id="comment-46090-info" class="comment-info"><span class="comment-age">(23 Sep '15, 14:21)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46069" class="comment-tools"></div><div class="clear"></div><div id="comment-46069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

