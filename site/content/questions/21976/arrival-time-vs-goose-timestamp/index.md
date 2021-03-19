+++
type = "question"
title = "Arrival time vs GOOSE timestamp"
description = '''I am writing a Python program to decode captured GOOSE packets and ran into a little problem. I get a perfect match between my program and Wireshark for the packet arrival time (part of the frame header). In addition, I have a match for the year, month ... down to seconds part of the GOOSE message t...'''
date = "2013-06-12T13:19:00Z"
lastmod = "2013-06-21T21:15:00Z"
weight = 21976
keywords = [ "arrival", "goose", "vs", "time" ]
aliases = [ "/questions/21976" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Arrival time vs GOOSE timestamp](/questions/21976/arrival-time-vs-goose-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21976-score" class="post-score" title="current number of votes">0</div><span id="post-21976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a Python program to decode captured GOOSE packets and ran into a little problem. I get a perfect match between my program and Wireshark for the packet arrival time (part of the frame header). In addition, I have a match for the year, month ... down to seconds part of the GOOSE message time. However, I am not getting a match for the decimal part of the time stamp.</p><p>GOOSE time in hex: 51 24 f3 bb b0 77 ab 0a</p><p>I am matching the first 8 bytes (51 24 f3 bb) perfectly (that's the year, month, ... seconds).</p><p>My translation of the rest of the time stamp (b0 77 ab) is 115649710 (my understanding is that th e last one (0a) is for time quality and not part of the time.</p><p>Wireshark displays a time of 689325988</p><p>What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arrival" rel="tag" title="see questions tagged &#39;arrival&#39;">arrival</span> <span class="post-tag tag-link-goose" rel="tag" title="see questions tagged &#39;goose&#39;">goose</span> <span class="post-tag tag-link-vs" rel="tag" title="see questions tagged &#39;vs&#39;">vs</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '13, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/4025240b8c0475c260d9cb7529e827c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecs1749&#39;s gravatar image" /><p><span>ecs1749</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecs1749 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '13, 13:19</strong> </span></p></div></div><div id="comments-container-21976" class="comments-container"><span id="22066"></span><div id="comment-22066" class="comment"><div id="post-22066-score" class="comment-score"></div><div class="comment-text"><p>May be my question wasn't clear: How does Wireshark get a value of 689325988 from 0xb077ab for the decimal portion of the GOOSE time stamp?</p></div><div id="comment-22066-info" class="comment-info"><span class="comment-age">(14 Jun '13, 08:56)</span> <span class="comment-user userinfo">ecs1749</span></div></div><span id="22242"></span><div id="comment-22242" class="comment"><div id="post-22242-score" class="comment-score"></div><div class="comment-text"><p>Maybe you could post a small capture file to <a href="http://cloudshark.org/">http://cloudshark.org/</a>?</p></div><div id="comment-22242-info" class="comment-info"><span class="comment-age">(21 Jun '13, 21:15)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-21976" class="comment-tools"></div><div class="clear"></div><div id="comment-21976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

