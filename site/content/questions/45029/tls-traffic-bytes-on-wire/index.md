+++
type = "question"
title = "TLS traffic bytes on wire"
description = '''I captured a TLS Session where I&#x27;m sending my files to a Cloud Storage and have multiple entries with over 1514 bytes on wire, the biggest one is 16512Byte and the others are lower. Only the frames I&#x27;m sending are that big. Does the TLS application have some kind of buffer and then hands the buffer ...'''
date = "2015-08-12T17:50:00Z"
lastmod = "2015-08-13T03:02:00Z"
weight = 45029
keywords = [ "tls", "ssl", "bytes" ]
aliases = [ "/questions/45029" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TLS traffic bytes on wire](/questions/45029/tls-traffic-bytes-on-wire)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45029-score" class="post-score" title="current number of votes">0</div><span id="post-45029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured a TLS Session where I'm sending my files to a Cloud Storage and have multiple entries with over 1514 bytes on wire, the biggest one is 16512Byte and the others are lower. Only the frames I'm sending are that big. Does the TLS application have some kind of buffer and then hands the buffer over to the NIC which builds the segments according the MTU?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/e0a3df4142e6bf80e01f82fad9fb6fa6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gill89&#39;s gravatar image" /><p><span>gill89</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gill89 has no accepted answers">0%</span></p></div></div><div id="comments-container-45029" class="comments-container"></div><div id="comment-tools-45029" class="comment-tools"></div><div class="clear"></div><div id="comment-45029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45033"></span>

<div id="answer-container-45033" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45033-score" class="post-score" title="current number of votes">0</div><span id="post-45033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gill89 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TSO TCP send offload is probably active on the nic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 21:30</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-45033" class="comments-container"><span id="45048"></span><div id="comment-45048" class="comment"><div id="post-45048-score" class="comment-score"></div><div class="comment-text"><p>I already checked that. I'm using Windows 10 and it says Chimney is disabled. Any other suggestions?</p></div><div id="comment-45048-info" class="comment-info"><span class="comment-age">(13 Aug '15, 02:40)</span> <span class="comment-user userinfo">gill89</span></div></div><span id="45049"></span><div id="comment-45049" class="comment"><div id="post-45049-score" class="comment-score"></div><div class="comment-text"><p>Nevermind you were totally right. I thank you for your suggestion! It was enabled on the NIC. I thought i checked this option but obviously not. Thank you very much.</p></div><div id="comment-45049-info" class="comment-info"><span class="comment-age">(13 Aug '15, 03:02)</span> <span class="comment-user userinfo">gill89</span></div></div></div><div id="comment-tools-45033" class="comment-tools"></div><div class="clear"></div><div id="comment-45033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

