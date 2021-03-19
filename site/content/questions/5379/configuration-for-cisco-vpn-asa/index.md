+++
type = "question"
title = "Configuration for Cisco VPN ASA"
description = '''I&#x27;m trying to configure WireShark to pickup the inbound traffic on my Cisco ASA Concentrator. When i launch Wireshark it automatically picks up my local adapters. How can I configure WireShark to pickup the traffic on my ASA&#x27;s adapter?'''
date = "2011-08-01T11:55:00Z"
lastmod = "2011-08-03T01:18:00Z"
weight = 5379
keywords = [ "asa" ]
aliases = [ "/questions/5379" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Configuration for Cisco VPN ASA](/questions/5379/configuration-for-cisco-vpn-asa)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5379-score" class="post-score" title="current number of votes">0</div><span id="post-5379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to configure WireShark to pickup the inbound traffic on my Cisco ASA Concentrator. When i launch Wireshark it automatically picks up my local adapters. How can I configure WireShark to pickup the traffic on my ASA's adapter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asa" rel="tag" title="see questions tagged &#39;asa&#39;">asa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '11, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/2249d51b1332af4f4742e937ca9a6394?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c1n29&#39;s gravatar image" /><p><span>c1n29</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c1n29 has no accepted answers">0%</span></p></div></div><div id="comments-container-5379" class="comments-container"></div><div id="comment-tools-5379" class="comment-tools"></div><div class="clear"></div><div id="comment-5379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5387"></span>

<div id="answer-container-5387" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5387-score" class="post-score" title="current number of votes">1</div><span id="post-5387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '11, 19:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5387" class="comments-container"></div><div id="comment-tools-5387" class="comment-tools"></div><div class="clear"></div><div id="comment-5387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5417"></span>

<div id="answer-container-5417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5417-score" class="post-score" title="current number of votes">1</div><span id="post-5417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can not capture directly from a Cisco ASA. You can either capture packets on the ASA and then export them to a file for Wireshark to read. Or you will need to capture the packets inline, have a look at the <a href="http://wiki.wireshark.org/CaptureSetup">link</a> in the other answer to see how that can be done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5417" class="comments-container"></div><div id="comment-tools-5417" class="comment-tools"></div><div class="clear"></div><div id="comment-5417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

