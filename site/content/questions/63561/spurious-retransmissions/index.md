+++
type = "question"
title = "Spurious retransmissions."
description = '''Hi I have some employees that use a remote application launched by a rdp file that opens a remote chrome application on the client side, I have been noticing a delay when clicking and typing on the remote app, and after making many changes on Computers I started debugging on my firewall a USG-300 Zy...'''
date = "2017-09-04T14:00:00Z"
lastmod = "2017-09-06T07:23:00Z"
weight = 63561
keywords = [ "spurious", "wireshark" ]
aliases = [ "/questions/63561" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Spurious retransmissions.](/questions/63561/spurious-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63561-score" class="post-score" title="current number of votes">0</div><span id="post-63561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I have some employees that use a remote application launched by a rdp file that opens a remote chrome application on the client side, I have been noticing a delay when clicking and typing on the remote app, and after making many changes on Computers I started debugging on my firewall a USG-300 Zywall.</p><p>Packet captures shows a lot of Spurious retransmissions and the behavior is recurrent and always happening, pretty much 99% of this spurious retransmissions are sent by the remote host 50.201.127.20 and I cannot see any change with many tests I have made no luck or service enhancement, So I think must be something on the server application.</p><p>Has anybody fixed this? or now how to,? thanks a lot <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_IZ5a38E.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-spurious" rel="tag" title="see questions tagged &#39;spurious&#39;">spurious</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '17, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/812fe573bf9fbc2fb3cb8370ca32b97d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Josue56&#39;s gravatar image" /><p><span>Josue56</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Josue56 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Sep '17, 10:23</strong> </span></p></div></div><div id="comments-container-63561" class="comments-container"><span id="63562"></span><div id="comment-63562" class="comment"><div id="post-63562-score" class="comment-score"></div><div class="comment-text"><p>The screenshot doesn't seem to show spurious retransmissions, just normal fast retransmissions after packet loss (indicated by the DUP ACK chain). And what is "host 50"? Do you mean 50.201.127.20?</p></div><div id="comment-63562-info" class="comment-info"><span class="comment-age">(04 Sep '17, 23:58)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="63565"></span><div id="comment-63565" class="comment"><div id="post-63565-score" class="comment-score"></div><div class="comment-text"><p>I updated the picture is so weird I just receive same spurious transmission but no see any packet loss on my side.</p></div><div id="comment-63565-info" class="comment-info"><span class="comment-age">(05 Sep '17, 10:32)</span> <span class="comment-user userinfo">Josue56</span></div></div></div><div id="comment-tools-63561" class="comment-tools"></div><div class="clear"></div><div id="comment-63561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63569"></span>

<div id="answer-container-63569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63569-score" class="post-score" title="current number of votes">0</div><span id="post-63569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Spurious retransmissions are packets that are sent again even though their content has already been ACKed. That usually means that you're capturing on the receiving end of the connection, seeing data arrive twice and most likely means that the acknowledge packets for those data packets have been lost on the way to the sender. That way the sender thinks the data never arrived and sends it again.</p><p>If possible, capture on both ends to compare what packets are seen on each of the locations, and determine to point of packet loss from there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '17, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63569" class="comments-container"></div><div id="comment-tools-63569" class="comment-tools"></div><div class="clear"></div><div id="comment-63569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

