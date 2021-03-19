+++
type = "question"
title = "Find Behavior when searching for HEX sequence"
description = '''I&#x27;ve just noticed the following while playing with a wireshark trace: http contains &quot;&#92;x89&#92;x50&#92;x4E&#92;x47&quot; finds the correct packet with png signature in the http content. On the contrary, a CTRL + F for Find, then selecting the HEX options and typing 89 50 4E 47 (no case sensitive), only finds a differ...'''
date = "2015-03-06T09:10:00Z"
lastmod = "2015-03-18T10:39:00Z"
weight = 40328
keywords = [ "hex", "find" ]
aliases = [ "/questions/40328" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find Behavior when searching for HEX sequence](/questions/40328/find-behavior-when-searching-for-hex-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40328-score" class="post-score" title="current number of votes">0</div><span id="post-40328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've just noticed the following while playing with a wireshark trace: http contains "\x89\x50\x4E\x47" finds the correct packet with png signature in the http content. On the contrary, a CTRL + F for Find, then selecting the HEX options and typing 89 50 4E 47 (no case sensitive), only finds a different packet with that hex sequence in the tcp segment data. Basically, it finds the sequence in a TCP packet but seems to ignore packets categorized as HTTP and the http content. By any chance, do you know if it's a bug or by design in wireshark?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-find" rel="tag" title="see questions tagged &#39;find&#39;">find</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '15, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/95f6b6d3f469cb96f0e8806273d0b2e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="halfluke&#39;s gravatar image" /><p><span>halfluke</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="halfluke has no accepted answers">0%</span></p></div></div><div id="comments-container-40328" class="comments-container"><span id="40342"></span><div id="comment-40342" class="comment"><div id="post-40342-score" class="comment-score"></div><div class="comment-text"><p>Did you verify that it does not highlight the TCP segment that contains a part of the HTTP payload that is later reassembled so as to be decoded by the HTTP dissector? If you could share the pcap file, it would allow to verify this hypothesis.</p></div><div id="comment-40342-info" class="comment-info"><span class="comment-age">(06 Mar '15, 22:28)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="40666"></span><div id="comment-40666" class="comment"><div id="post-40666-score" class="comment-score"></div><div class="comment-text"><p>sorry I've just seen your reply. I cannot find the trace where I experienced that behaviour. I have a new one now and the Find seems to be able to find both in "tcp" and "http" packets. I will try to reproduce as soon as I have some time But thank you!</p></div><div id="comment-40666-info" class="comment-info"><span class="comment-age">(18 Mar '15, 10:39)</span> <span class="comment-user userinfo">halfluke</span></div></div></div><div id="comment-tools-40328" class="comment-tools"></div><div class="clear"></div><div id="comment-40328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

