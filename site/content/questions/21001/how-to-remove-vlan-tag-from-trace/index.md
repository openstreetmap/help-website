+++
type = "question"
title = "How to remove vlan tag from trace?"
description = '''Hello, I have a H248 pcap trace with double vlan tag: 802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 999 802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 473 And my question if there any way to remove one vlan tag, or both tags from the trace?. Thanks beforehand for your answer.'''
date = "2013-05-07T04:34:00Z"
lastmod = "2013-05-07T06:08:00Z"
weight = 21001
keywords = [ "h248", "vlan", "tag", "remove" ]
aliases = [ "/questions/21001" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to remove vlan tag from trace?](/questions/21001/how-to-remove-vlan-tag-from-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21001-score" class="post-score" title="current number of votes">0</div><span id="post-21001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a H248 pcap trace with double vlan tag:</p><p>802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 999</p><p>802.1Q Virtual LAN, PRI: 0, CFI: 0, ID: 473</p><p>And my question if there any way to remove one vlan tag, or both tags from the trace?.</p><p>Thanks beforehand for your answer.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-h248" rel="tag" title="see questions tagged &#39;h248&#39;">h248</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '13, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/beced2d25419ada1b1879cb55d8da7a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rubik001&#39;s gravatar image" /><p><span>rubik001</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rubik001 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '13, 05:01</strong> </span></p></div></div><div id="comments-container-21001" class="comments-container"></div><div id="comment-tools-21001" class="comment-tools"></div><div class="clear"></div><div id="comment-21001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21003"></span>

<div id="answer-container-21003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21003-score" class="post-score" title="current number of votes">1</div><span id="post-21003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please take a look at tcprewrite. It is able to add/remove VLAN tags.</p><blockquote><p><code>http://tcpreplay.synfin.net/wiki/tcprewrite</code><br />
</p></blockquote><p>Run it like this:</p><blockquote><p><code>tcprewrite --enet-vlan=del --infile=vlan.cap --outfile=novlan.cap</code><br />
</p></blockquote><p>Please read the man page for more options.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '13, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '13, 06:14</strong> </span></p></div></div><div id="comments-container-21003" class="comments-container"></div><div id="comment-tools-21003" class="comment-tools"></div><div class="clear"></div><div id="comment-21003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

