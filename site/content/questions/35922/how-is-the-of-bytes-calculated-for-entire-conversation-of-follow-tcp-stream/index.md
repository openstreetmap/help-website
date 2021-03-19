+++
type = "question"
title = "How is the # of bytes calculated for &quot;Entire Conversation&quot; of &quot;Follow TCP Stream&quot;"
description = '''I tried to analyze a specific TCP stream with filter like &quot;tcp.stream eq 16&quot;, which then show me all the packets in this stream. Then I select one of the packet, and select &quot;Follow TCP Stream&quot;, a window was popped up. And below the Stream Content, it shows &quot;Entire conversation (6817 bytes)&quot;. However...'''
date = "2014-09-02T00:10:00Z"
lastmod = "2014-09-02T15:40:00Z"
weight = 35922
keywords = [ "entirecoversation", "followtcpstream" ]
aliases = [ "/questions/35922" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How is the \# of bytes calculated for "Entire Conversation" of "Follow TCP Stream"](/questions/35922/how-is-the-of-bytes-calculated-for-entire-conversation-of-follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35922-score" class="post-score" title="current number of votes">0</div><span id="post-35922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to analyze a specific TCP stream with filter like "tcp.stream eq 16", which then show me all the packets in this stream. Then I select one of the packet, and select "Follow TCP Stream", a window was popped up. And below the Stream Content, it shows "Entire conversation (<strong>6817 byte</strong>s)". However, if I add up the value in the "Length" column for all packets in the stream, the sum is <strong>8575</strong>, which is a lot larger than <strong>6817</strong>. I'm just wondering how the value "6817" was calculated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-entirecoversation" rel="tag" title="see questions tagged &#39;entirecoversation&#39;">entirecoversation</span> <span class="post-tag tag-link-followtcpstream" rel="tag" title="see questions tagged &#39;followtcpstream&#39;">followtcpstream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '14, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/066d4ecc00f7a2f618cbca55561331de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zeal&#39;s gravatar image" /><p><span>zeal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zeal has no accepted answers">0%</span></p></div></div><div id="comments-container-35922" class="comments-container"></div><div id="comment-tools-35922" class="comment-tools"></div><div class="clear"></div><div id="comment-35922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35926"></span>

<div id="answer-container-35926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35926-score" class="post-score" title="current number of votes">2</div><span id="post-35926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "Follow TCP Stream" probably calculates the TCP <strong>payload</strong> size, while the length column also contains the overhead of the protocol headers for Ethernet, IP and TCP. So it should be larger.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '14, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35926" class="comments-container"><span id="35940"></span><div id="comment-35940" class="comment"><div id="post-35940-score" class="comment-score">1</div><div class="comment-text"><p>As Jasper said, "Follow TCP Stream" does not include the headers, while the Length column does. If you want the numbers to match, you can add the tcp.len field as a custom column. That is the length of the TCP data segment, not including any headers.</p></div><div id="comment-35940-info" class="comment-info"><span class="comment-age">(02 Sep '14, 15:40)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-35926" class="comment-tools"></div><div class="clear"></div><div id="comment-35926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

