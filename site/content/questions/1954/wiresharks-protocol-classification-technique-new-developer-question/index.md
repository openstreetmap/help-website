+++
type = "question"
title = "Wireshark&#x27;s protocol classification technique (new developer question)"
description = '''I working with a small team to develop a wireshark plugin for a new protocol. The protocol has no header, so it is difficult (impossible maybe) to identify weather or not a packet contains this protocol. Also the protocol is state dependent, so it is important our plugin not receive packets containi...'''
date = "2011-01-26T14:08:00Z"
lastmod = "2011-01-26T19:28:00Z"
weight = 1954
keywords = [ "protocol", "plugins" ]
aliases = [ "/questions/1954" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark's protocol classification technique (new developer question)](/questions/1954/wiresharks-protocol-classification-technique-new-developer-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1954-score" class="post-score" title="current number of votes">0</div><span id="post-1954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I working with a small team to develop a wireshark plugin for a new protocol.</p><p>The protocol has no header, so it is difficult (impossible maybe) to identify weather or not a packet contains this protocol.</p><p>Also the protocol is state dependent, so it is important our plugin not receive packets containing other protocols.</p><p>Currently our plugin works by assuming everything on a given UDP port is our protocol.</p><p>Is there some way to identify other protocols sent on our port, or at least tell wireshark to check all other protocols first before handing packets off to our plugin?</p><p>Thanks much for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '11, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/b30c40f0577a6846075787f369d26d01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drjohnso&#39;s gravatar image" /><p><span>drjohnso</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drjohnso has no accepted answers">0%</span></p></div></div><div id="comments-container-1954" class="comments-container"></div><div id="comment-tools-1954" class="comment-tools"></div><div class="clear"></div><div id="comment-1954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1956"></span>

<div id="answer-container-1956" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1956-score" class="post-score" title="current number of votes">1</div><span id="post-1956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="drjohnso has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The best you can do is enable the UDP preference: "Try heuristic sub-dissectors first".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '11, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1956" class="comments-container"><span id="1959"></span><div id="comment-1959" class="comment"><div id="post-1959-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help.</p><p>I am guessing that "Try heuristic sub-dissectors first" will do something like I stated "tell wireshark to check all other protocols first before handing packets off to our plugin"</p><p>Am I right? Do you know where I could find any documentation on this?</p></div><div id="comment-1959-info" class="comment-info"><span class="comment-age">(26 Jan '11, 14:55)</span> <span class="comment-user userinfo">drjohnso</span></div></div><span id="1964"></span><div id="comment-1964" class="comment"><div id="post-1964-score" class="comment-score">1</div><div class="comment-text"><p>There are two types of dissectors for UDP-based protocols - dissectors called for specific port numbers, and dissectors called for all packets that can accept or reject a packet. The latter are called "heuristic" dissectors; "Try heuristic sub-dissectors first" means those will be called before dissectors for specific port numbers are called.</p></div><div id="comment-1964-info" class="comment-info"><span class="comment-age">(26 Jan '11, 19:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1956" class="comment-tools"></div><div class="clear"></div><div id="comment-1956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

