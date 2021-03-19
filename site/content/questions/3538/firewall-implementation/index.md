+++
type = "question"
title = "FireWall Implementation."
description = '''I want to build a firewall(Packet Filter Mechanism). How WireShark can help me in this regard? Is there any function available in WireShark by which i can discard an abnormally detected packet?'''
date = "2011-04-17T11:10:00Z"
lastmod = "2011-04-18T23:54:00Z"
weight = 3538
keywords = [ "firewall" ]
aliases = [ "/questions/3538" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FireWall Implementation.](/questions/3538/firewall-implementation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3538-score" class="post-score" title="current number of votes">0</div><span id="post-3538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to build a firewall(Packet Filter Mechanism). How WireShark can help me in this regard? Is there any function available in WireShark by which i can discard an abnormally detected packet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall" rel="tag" title="see questions tagged &#39;firewall&#39;">firewall</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '11, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/3b365869f80105499ecd964e9642ba37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Avik&#39;s gravatar image" /><p><span>Avik</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Avik has no accepted answers">0%</span></p></div></div><div id="comments-container-3538" class="comments-container"></div><div id="comment-tools-3538" class="comment-tools"></div><div class="clear"></div><div id="comment-3538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3539"></span>

<div id="answer-container-3539" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3539-score" class="post-score" title="current number of votes">2</div><span id="post-3539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark was not made to interfere with traffic, it is made to record and analyze traffic. You can't influence traffic flows with wireshark. You will need to look for another tool to do that.</p><p>Some suggestions that might get you what you need:</p><ul><li>pfSense, an open source firewall</li><li>m0n0wall, another open source firewall</li><li>snort, an open source Intrusion Detection and Prevention system (which might be what your looking for since you seek to filter abnormal packets)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '11, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '11, 23:57</strong> </span></p></div></div><div id="comments-container-3539" class="comments-container"><span id="3600"></span><div id="comment-3600" class="comment"><div id="post-3600-score" class="comment-score"></div><div class="comment-text"><p>oh! thank you.. The resources you provided are awesome.</p></div><div id="comment-3600-info" class="comment-info"><span class="comment-age">(18 Apr '11, 23:54)</span> <span class="comment-user userinfo">Avik</span></div></div></div><div id="comment-tools-3539" class="comment-tools"></div><div class="clear"></div><div id="comment-3539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

