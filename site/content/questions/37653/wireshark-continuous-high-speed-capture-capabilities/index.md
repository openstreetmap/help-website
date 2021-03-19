+++
type = "question"
title = "Wireshark continuous high speed capture capabilities?"
description = '''Hi, I have a requirement to monitor a 1GBps data stream and would like to further understand Wireshark&#x27;s monitoring capabilities. Is the GUI display responsive to continuous capture at 1GBps i.e can you still scroll/read the display during continuous high speed data capture? Is there a limit to the ...'''
date = "2014-11-07T07:50:00Z"
lastmod = "2014-11-11T08:04:00Z"
weight = 37653
keywords = [ "high", "responsive", "speed" ]
aliases = [ "/questions/37653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark continuous high speed capture capabilities?](/questions/37653/wireshark-continuous-high-speed-capture-capabilities)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37653-score" class="post-score" title="current number of votes">0</div><span id="post-37653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a requirement to monitor a 1GBps data stream and would like to further understand Wireshark's monitoring capabilities.</p><p>Is the GUI display responsive to continuous capture at 1GBps i.e can you still scroll/read the display during continuous high speed data capture?</p><p>Is there a limit to the amount of data Wireshark can comfortably handle?</p><p>Thanks Andy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-high" rel="tag" title="see questions tagged &#39;high&#39;">high</span> <span class="post-tag tag-link-responsive" rel="tag" title="see questions tagged &#39;responsive&#39;">responsive</span> <span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '14, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/b6f0b9cf8fbd07c11186bdeed9f0e3a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awl&#39;s gravatar image" /><p><span>awl</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awl has no accepted answers">0%</span></p></div></div><div id="comments-container-37653" class="comments-container"><span id="37655"></span><div id="comment-37655" class="comment"><div id="post-37655-score" class="comment-score"></div><div class="comment-text"><p>Can you read the data on the screen if it's coming in at 1GBps?</p><p>Wireshark (and tshark) will run out of memory at some point because of all the conversation tracking they do. The faster it comes in, the faster it will happen. If you want to capture in such situations for post-analysis then use dumpcap.</p></div><div id="comment-37655-info" class="comment-info"><span class="comment-age">(07 Nov '14, 09:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37754"></span><div id="comment-37754" class="comment"><div id="post-37754-score" class="comment-score"></div><div class="comment-text"><p>I'd can only imagine that if Wireshark had a virtual display it could display just enough capture data on screen according to the user positioning the slider, but it appears it does not.</p><p>Do you know what data capture size Wireshark can support? I vaguely recall reading Wireshark handling 100MB of data but struggles beyond that amount.</p></div><div id="comment-37754-info" class="comment-info"><span class="comment-age">(11 Nov '14, 07:38)</span> <span class="comment-user userinfo">awl</span></div></div><span id="37755"></span><div id="comment-37755" class="comment"><div id="post-37755-score" class="comment-score"></div><div class="comment-text"><p>The supported capture size is very hard to answer, it depends on the data in the capture and how much extra memory is consumed for conversations, synthesised data etc.</p><p>I've opened files of 2GB before, but they're not fun to work with as any filter op takes a long time.</p><p>The memory problem is normally circumvented by using dumpcap to capture to multiple files. <span>@Jasper</span> has blog entry about it <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">here</a>.</p></div><div id="comment-37755-info" class="comment-info"><span class="comment-age">(11 Nov '14, 08:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37653" class="comment-tools"></div><div class="clear"></div><div id="comment-37653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37664"></span>

<div id="answer-container-37664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37664-score" class="post-score" title="current number of votes">1</div><span id="post-37664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark can't handle 1GBps unless you capture it with specialized hardware, e.g. <a href="http://www.napatech.com/">Napatech</a> or <a href="http://www.fiberblaze.com/">Fiberblaze</a> cards (at least Napatech does not sell to retail though). Normal NICs will fail to capture consistently at about 200-300 MBit at the most.</p><p>And forget scrolling - it's not going to work well at anything above a couple of MBit because it is not going to show much except for a slide show (if it moves at all). It also leads to dropped frames because it puts additional stress on the capture machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37664" class="comments-container"></div><div id="comment-tools-37664" class="comment-tools"></div><div class="clear"></div><div id="comment-37664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

