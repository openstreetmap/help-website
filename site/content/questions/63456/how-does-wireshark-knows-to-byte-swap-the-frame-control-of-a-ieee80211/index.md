+++
type = "question"
title = "How does Wireshark knows to byte swap the frame control of a IEEE80211"
description = '''I have came across some capwap packets that seems to have two bytes of IEEE80211&#x27;s frame control swapped. Wireshark successfuly detects this and displays &quot;Swapped&quot; next to the frame control frame line. I been looking through the code at epan/dissectors/packet-ieee80211.c to try to understand how doe...'''
date = "2017-08-09T12:38:00Z"
lastmod = "2017-08-09T14:10:00Z"
weight = 63456
keywords = [ "capwap", "api" ]
aliases = [ "/questions/63456" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does Wireshark knows to byte swap the frame control of a IEEE80211](/questions/63456/how-does-wireshark-knows-to-byte-swap-the-frame-control-of-a-ieee80211)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63456-score" class="post-score" title="current number of votes">0</div><span id="post-63456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have came across some capwap packets that seems to have two bytes of IEEE80211's frame control swapped.<br />
Wireshark successfuly detects this and displays "Swapped" next to the frame control frame line.<br />
I been looking through the code at <code>epan/dissectors/packet-ieee80211.c</code> to try to understand how does Wireshark know this but could not figure it out.</p><p>There seems to be a call to <code>register_dissector dissect_ieee80211_bsfc</code> but I could not understand when it is used over the other dissectors. (bsfc stands for byte-swapped frame control)</p><p>Please help me understand.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capwap" rel="tag" title="see questions tagged &#39;capwap&#39;">capwap</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '17, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/e6497f67a248956d28c81a2f3c263de5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Kroizman&#39;s gravatar image" /><p><span>Guy Kroizman</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Kroizman has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-63456" class="comments-container"></div><div id="comment-tools-63456" class="comment-tools"></div><div class="clear"></div><div id="comment-63456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63457"></span>

<div id="answer-container-63457" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63457-score" class="post-score" title="current number of votes">1</div><span id="post-63457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Guy Kroizman has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I asked the exaxt same question here:</p><p><a href="https://ask.wireshark.org/questions/55804/capwap-80111-data-header-fcf-swapped-why">https://ask.wireshark.org/questions/55804/capwap-80111-data-header-fcf-swapped-why</a></p><p>Basic Answer: if 802.11 frame control is carried over CAPWAP, bytes are simply swapped. No other indicator. It's what I do in TraceWrangler now, and it works 100% so far.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '17, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63457" class="comments-container"></div><div id="comment-tools-63457" class="comment-tools"></div><div class="clear"></div><div id="comment-63457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

