+++
type = "question"
title = "Window update not sent"
description = '''When looking at the conversation in .pcap I can see &quot;Calculated window size&quot; is constantly growing with each packet. However there is no Window Update message is sent. Is this normal not to see it? Thanks.'''
date = "2016-11-27T04:46:00Z"
lastmod = "2016-11-27T05:01:00Z"
weight = 57659
keywords = [ "tcp_window_update", "window" ]
aliases = [ "/questions/57659" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Window update not sent](/questions/57659/window-update-not-sent)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57659-score" class="post-score" title="current number of votes">0</div><span id="post-57659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When looking at the conversation in .pcap I can see "Calculated window size" is constantly growing with each packet. However there is no Window Update message is sent. Is this normal not to see it?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_window_update" rel="tag" title="see questions tagged &#39;tcp_window_update&#39;">tcp_window_update</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '16, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/519f962e650bd3a005b302b70cb12194?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emagidso&#39;s gravatar image" /><p><span>emagidso</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emagidso has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Nov '16, 04:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-57659" class="comments-container"><span id="57660"></span><div id="comment-57660" class="comment"><div id="post-57660-score" class="comment-score"></div><div class="comment-text"><p>Can you claridy? "there is Window update message" - looks like you forgot the "no"? Otherwise the last sentence makes no sense.</p></div><div id="comment-57660-info" class="comment-info"><span class="comment-age">(27 Nov '16, 04:56)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="57661"></span><div id="comment-57661" class="comment"><div id="post-57661-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Yes I made a typo. "However there is <em>no</em> Window Update message is sent" is the correct one.</p></div><div id="comment-57661-info" class="comment-info"><span class="comment-age">(27 Nov '16, 04:57)</span> <span class="comment-user userinfo">emagidso</span></div></div><span id="57662"></span><div id="comment-57662" class="comment"><div id="post-57662-score" class="comment-score"></div><div class="comment-text"><p>Okay, I updated the question.</p></div><div id="comment-57662-info" class="comment-info"><span class="comment-age">(27 Nov '16, 04:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-57659" class="comment-tools"></div><div class="clear"></div><div id="comment-57659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57663"></span>

<div id="answer-container-57663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57663-score" class="post-score" title="current number of votes">0</div><span id="post-57663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Window Update" only happens if the receiver ACKnowledges something that has already been acknowledged but the window size value has changed. So if you're seeing growing windows while new incoming data is acknowledged it's not a window update.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '16, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-57663" class="comments-container"></div><div id="comment-tools-57663" class="comment-tools"></div><div class="clear"></div><div id="comment-57663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

