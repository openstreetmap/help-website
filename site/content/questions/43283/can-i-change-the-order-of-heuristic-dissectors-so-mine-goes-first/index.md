+++
type = "question"
title = "Can I change the order of heuristic dissectors so mine goes first?"
description = '''There is another heuristic dissector that gets in the way and erroneously claims packets for its protocol. There is a change of protocols in the middle of my TCP session. So I&#x27;d rather use mine lua heuristic dissector first, and then pass whatever doesn&#x27;t belong to it down to another built-in dissec...'''
date = "2015-06-17T14:01:00Z"
lastmod = "2015-06-27T17:12:00Z"
weight = 43283
keywords = [ "heuristic", "dissector", "order", "lua" ]
aliases = [ "/questions/43283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I change the order of heuristic dissectors so mine goes first?](/questions/43283/can-i-change-the-order-of-heuristic-dissectors-so-mine-goes-first)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43283-score" class="post-score" title="current number of votes">0</div><span id="post-43283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is another heuristic dissector that gets in the way and erroneously claims packets for its protocol. There is a change of protocols in the middle of my TCP session. So I'd rather use mine lua heuristic dissector first, and then pass whatever doesn't belong to it down to another built-in dissector.</p><p>Update... it looks like the other dissector does something with TCP sequence and overrides things. If I claim everything as mine (by returning true), then I'm not getting the dissector from libwireshark.dll in the way. So I guess nothing can be done.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-heuristic" rel="tag" title="see questions tagged &#39;heuristic&#39;">heuristic</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/f50a845aca7585dfa8bff6358258eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mlt&#39;s gravatar image" /><p><span>mlt</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mlt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jun '15, 14:13</strong> </span></p></div></div><div id="comments-container-43283" class="comments-container"></div><div id="comment-tools-43283" class="comment-tools"></div><div class="clear"></div><div id="comment-43283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43300"></span>

<div id="answer-container-43300" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43300-score" class="post-score" title="current number of votes">0</div><span id="post-43300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could disable to dissector that causes problems.</p><blockquote><p>Analyze -&gt; Enabled Protocols</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 23:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43300" class="comments-container"><span id="43335"></span><div id="comment-43335" class="comment"><div id="post-43335-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, I do need that another protocol. The actual problem is that BitTorrent dissector claims other packets before handshake as its own, whereas I would like to have <a href="https://geti2p.net/en/docs/api/samv3">I2P SAM</a> dissector. Same port is being used, but the conversation starts with SAM and then switches over to BT. It is probably a bug for BT dissector. It shouldn't claim anything before the handshake.</p></div><div id="comment-43335-info" class="comment-info"><span class="comment-age">(18 Jun '15, 09:39)</span> <span class="comment-user userinfo">mlt</span></div></div><span id="43610"></span><div id="comment-43610" class="comment"><div id="post-43610-score" class="comment-score"></div><div class="comment-text"><p>I haven't tried to do it before, but I think you could disable the BitTorrent one in the GUI, but then still call/invoke the BitTorrent dissector from within your Lua-based I2P dissector. (i.e., using <code>Dissector.get()</code> and <code>dissector:call()</code>)</p></div><div id="comment-43610-info" class="comment-info"><span class="comment-age">(27 Jun '15, 17:12)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-43300" class="comment-tools"></div><div class="clear"></div><div id="comment-43300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

