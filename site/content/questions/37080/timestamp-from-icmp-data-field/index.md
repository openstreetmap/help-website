+++
type = "question"
title = "Timestamp from icmp data field"
description = '''Why don&#x27;t Windows pings ever show this field in Wireshark: Timestamp from icmp data field (icmp.data_time)? A Linux ping always has this field right after the Sequence Number (and it&#x27;s actually the first 8 bytes of the data section), but when I ping with Windows, I NEVER see this field. Furthermore,...'''
date = "2014-10-15T10:55:00Z"
lastmod = "2014-10-20T14:17:00Z"
weight = 37080
keywords = [ "icmp.data_time" ]
aliases = [ "/questions/37080" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Timestamp from icmp data field](/questions/37080/timestamp-from-icmp-data-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37080-score" class="post-score" title="current number of votes">0</div><span id="post-37080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why don't Windows pings ever show this field in Wireshark: Timestamp from icmp data field (icmp.data_time)?</p><p>A Linux ping always has this field right after the Sequence Number (and it's actually the first 8 bytes of the data section), but when I ping with Windows, I NEVER see this field.</p><p>Furthermore, when I open up a Linux ping capture in Windows, I CAN see this field.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp.data_time" rel="tag" title="see questions tagged &#39;icmp.data_time&#39;">icmp.data_time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '14, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/3ce10f364ce411160730097943414b09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sniffer52&#39;s gravatar image" /><p><span>Sniffer52</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sniffer52 has no accepted answers">0%</span></p></div></div><div id="comments-container-37080" class="comments-container"></div><div id="comment-tools-37080" class="comment-tools"></div><div class="clear"></div><div id="comment-37080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37156"></span>

<div id="answer-container-37156" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37156-score" class="post-score" title="current number of votes">2</div><span id="post-37156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sniffer52 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The payload of an ICMP ping is entirely implementation dependant. The Windows ping utility does not carry a timestamp in the payload, instead it's the ASCII characters a-w (on Win 8.1 at least). See <a href="http://tools.ietf.org/html/rfc792">RFC 792</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '14, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37156" class="comments-container"></div><div id="comment-tools-37156" class="comment-tools"></div><div class="clear"></div><div id="comment-37156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37105"></span>

<div id="answer-container-37105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37105-score" class="post-score" title="current number of votes">0</div><span id="post-37105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ICMP dissector makes an attempt to interpret the timestamp, but is <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-icmp.c;hb=HEAD#l1566">not flawless</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '14, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-37105" class="comments-container"><span id="37155"></span><div id="comment-37155" class="comment"><div id="post-37155-score" class="comment-score"></div><div class="comment-text"><p>This does NOT answer my question.</p><p>The field is missing in Windows (Between the sequence number and data), but shows up in Linux. It's not a dissector issue.</p></div><div id="comment-37155-info" class="comment-info"><span class="comment-age">(18 Oct '14, 16:45)</span> <span class="comment-user userinfo">Sniffer52</span></div></div><span id="37203"></span><div id="comment-37203" class="comment"><div id="post-37203-score" class="comment-score"></div><div class="comment-text"><p>This does answer your question. If you read the code comments carefully you'll see that the dissector tries its best to make something of the data in the packet where a timestamp could be. There may be timestamp formats the dissector doesn't understand, or there may be no timestamp at all. That is what the dissector author is unsure about.</p><p>If your question really is: "why doesn't Windows fill in a timestamp in the ICMP data field", then I suggest you consult a Windows networking support site, which this is not.</p></div><div id="comment-37203-info" class="comment-info"><span class="comment-age">(20 Oct '14, 08:39)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="37209"></span><div id="comment-37209" class="comment"><div id="post-37209-score" class="comment-score"></div><div class="comment-text"><p>No, grahamb answered my question.</p><p>Your answer has nothing to do with my question (to which I wrote "This does NOT answer my question").</p><p>The answer is that Windows doesn't include a timestamp in the data field, not "the ICMP dissector makes an attempt but is not flawless."</p><p>Your reply to my reply is nothing but backtracking and revising history in terms of what you wrote (...or there may be no timestamp at all) :-)</p></div><div id="comment-37209-info" class="comment-info"><span class="comment-age">(20 Oct '14, 14:00)</span> <span class="comment-user userinfo">Sniffer52</span></div></div><span id="37210"></span><div id="comment-37210" class="comment"><div id="post-37210-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-37210-info" class="comment-info"><span class="comment-age">(20 Oct '14, 14:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37105" class="comment-tools"></div><div class="clear"></div><div id="comment-37105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

