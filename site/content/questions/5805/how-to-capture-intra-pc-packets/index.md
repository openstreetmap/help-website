+++
type = "question"
title = "How to capture intra-PC packets"
description = '''Running Wireshark 1.6.1 on Win 7 x64. I have a webserver running on my PC, and would like to capture packets from applications accessing the webserver, from the same PC. Attempting to capture packets on the usual port don&#x27;t seem to work. Is this even possible? Thanks for any pointers.'''
date = "2011-08-22T07:16:00Z"
lastmod = "2011-08-22T13:39:00Z"
weight = 5805
keywords = [ "capture", "internal", "intra-pc", "wireshark" ]
aliases = [ "/questions/5805" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture intra-PC packets](/questions/5805/how-to-capture-intra-pc-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5805-score" class="post-score" title="current number of votes">0</div><span id="post-5805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running Wireshark 1.6.1 on Win 7 x64.</p><p>I have a webserver running on my PC, and would like to capture packets from applications accessing the webserver, from the same PC. Attempting to capture packets on the usual port don't seem to work. Is this even possible? Thanks for any pointers.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-internal" rel="tag" title="see questions tagged &#39;internal&#39;">internal</span> <span class="post-tag tag-link-intra-pc" rel="tag" title="see questions tagged &#39;intra-pc&#39;">intra-pc</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '11, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/1dc0914cda671a1f86527ad799b1ff3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cgtyoder&#39;s gravatar image" /><p><span>cgtyoder</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cgtyoder has no accepted answers">0%</span></p></div></div><div id="comments-container-5805" class="comments-container"></div><div id="comment-tools-5805" class="comment-tools"></div><div class="clear"></div><div id="comment-5805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5806"></span>

<div id="answer-container-5806" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5806-score" class="post-score" title="current number of votes">0</div><span id="post-5806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cgtyoder has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it is, because the packets are not going out to the network and winpcap will not be able to pick them up. For that kind of scenario I usually put application and server on two different PCs to be able to see what is going back and forth - it's a pain to do that, but IMHO the easiest way to see what is really happening.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '11, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5806" class="comments-container"></div><div id="comment-tools-5806" class="comment-tools"></div><div class="clear"></div><div id="comment-5806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5807"></span>

<div id="answer-container-5807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5807-score" class="post-score" title="current number of votes">2</div><span id="post-5807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately on Windows intra-PC packets (loopback) don't surface at a level that WinPCap can capture them.</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">THIS</a> page on the Wireshark Wiki for more info about loopback capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '11, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5807" class="comments-container"><span id="5808"></span><div id="comment-5808" class="comment"><div id="post-5808-score" class="comment-score"></div><div class="comment-text"><p>grahamb, thanks for the pointer. RawCap looks like a great deal, but the traffic I am after is SSL-encrypted, and it would be way too much work to manually decrypt. I ended up re-creating the sending env on another computer, and quickly found the problem I was after. Thanks much for the pointers.</p></div><div id="comment-5808-info" class="comment-info"><span class="comment-age">(22 Aug '11, 11:53)</span> <span class="comment-user userinfo">cgtyoder</span></div></div><span id="5809"></span><div id="comment-5809" class="comment"><div id="post-5809-score" class="comment-score"></div><div class="comment-text"><p>Have a look at <a href="http://www.fiddler2.com/fiddler2/">Fiddler</a> as well, it's an HTTP(S) proxy that logs all traffic in plain text.</p></div><div id="comment-5809-info" class="comment-info"><span class="comment-age">(22 Aug '11, 13:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-5807" class="comment-tools"></div><div class="clear"></div><div id="comment-5807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

