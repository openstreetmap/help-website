+++
type = "question"
title = "How to capture http-alt package?"
description = '''Hi, i need some help here. i have to capture traffic using http-alt port. how can i configure wireshark filter ?. Thanks'''
date = "2015-10-13T08:58:00Z"
lastmod = "2015-10-13T11:33:00Z"
weight = 46501
keywords = [ "http-alt" ]
aliases = [ "/questions/46501" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture http-alt package?](/questions/46501/how-to-capture-http-alt-package)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46501-score" class="post-score" title="current number of votes">0</div><span id="post-46501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i need some help here. i have to capture traffic using http-alt port. how can i configure wireshark filter ?. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http-alt" rel="tag" title="see questions tagged &#39;http-alt&#39;">http-alt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/22190e87da4221754fd631ce34fced2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhaa11&#39;s gravatar image" /><p><span>buddhaa11</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhaa11 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '15, 11:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-46501" class="comments-container"></div><div id="comment-tools-46501" class="comment-tools"></div><div class="clear"></div><div id="comment-46501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46505"></span>

<div id="answer-container-46505" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46505-score" class="post-score" title="current number of votes">2</div><span id="post-46505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="buddhaa11 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark <em>services</em> file identifies ports 591, 8008, and 8080 as http-alt. So, the capture filter would be "port 591 or port 8008 or port 8080". You could further restrict the filter by putting "tcp" or "udp" in front of "port". Wireshark identifies both TCP and UPD traffic over those ports as http-alt.</p><p>The display filter would be "tcp.port==591 or tcp.port== 8008 or tcp.port==8080". This is for http-alt traffic over TCP only. You could also add expressions for UDP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-46505" class="comments-container"></div><div id="comment-tools-46505" class="comment-tools"></div><div class="clear"></div><div id="comment-46505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

