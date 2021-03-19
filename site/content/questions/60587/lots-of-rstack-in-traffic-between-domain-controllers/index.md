+++
type = "question"
title = "Lots of RST,ACK in traffic between Domain Controllers"
description = '''Is this normal behaviour?  '''
date = "2017-04-05T07:18:00Z"
lastmod = "2017-04-05T11:00:00Z"
weight = 60587
keywords = [ "rst+ack" ]
aliases = [ "/questions/60587" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Lots of RST,ACK in traffic between Domain Controllers](/questions/60587/lots-of-rstack-in-traffic-between-domain-controllers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60587-score" class="post-score" title="current number of votes">0</div><span id="post-60587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is this normal behaviour?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/RST_ACK1_G9fC1bp.JPG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/RST_ACK2_2cgeWoW.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst+ack" rel="tag" title="see questions tagged &#39;rst+ack&#39;">rst+ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '17, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/1b11873ac7fe8613629b5fbd0a2edb9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincebaat&#39;s gravatar image" /><p><span>Vincebaat</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincebaat has no accepted answers">0%</span></p></img></div></div><div id="comments-container-60587" class="comments-container"></div><div id="comment-tools-60587" class="comment-tools"></div><div class="clear"></div><div id="comment-60587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60588"></span>

<div id="answer-container-60588" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60588-score" class="post-score" title="current number of votes">2</div><span id="post-60588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vincebaat has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks pretty normal to me - some clients or servers terminate connections with a reset packet, because it's faster and needs less resources than the "normal" FIN-ACK teardown. So unless the reset appears before all the data is exchanged, it's nothing to worry about.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '17, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-60588" class="comments-container"></div><div id="comment-tools-60588" class="comment-tools"></div><div class="clear"></div><div id="comment-60588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60592"></span>

<div id="answer-container-60592" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60592-score" class="post-score" title="current number of votes">1</div><span id="post-60592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your capture looks very normal to me.</p><p>Just to add up - It's probably something you don't want to hear - but whenever possible, do baselines !</p><ul><li>You will be able to know what's going on in the network while everything runs OK</li><li>You will be able to know exactly how works a specific protocol / app in Wireshark, and when it fails, you'll be able to check any differences.</li></ul><p>I often have co-workers asking : '' Hey, is that normal I have this in Wireshark for X specific thing '', and I'm unable to tell them if it's normal or not because it's something too specific I never see / no baseline.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '17, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/21cfa2071214d5dacbb6d0cd9769a6d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jerioux&#39;s gravatar image" /><p><span>jerioux</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jerioux has no accepted answers">0%</span></p></div></div><div id="comments-container-60592" class="comments-container"></div><div id="comment-tools-60592" class="comment-tools"></div><div class="clear"></div><div id="comment-60592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

