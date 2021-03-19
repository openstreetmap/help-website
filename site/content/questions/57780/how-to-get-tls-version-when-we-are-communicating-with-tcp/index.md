+++
type = "question"
title = "how to get TLS version when we are communicating with TCP"
description = '''Hi,  i am looking for configuration changes required to see TLS(version 1.2) when we are communicating with TCP. Is it possible on wireshark??? thanks Bhuvnesh'''
date = "2016-12-02T02:23:00Z"
lastmod = "2016-12-02T03:38:00Z"
weight = 57780
keywords = [ "tls", "version", "with", "tcp" ]
aliases = [ "/questions/57780" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to get TLS version when we are communicating with TCP](/questions/57780/how-to-get-tls-version-when-we-are-communicating-with-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57780-score" class="post-score" title="current number of votes">0</div><span id="post-57780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i am looking for configuration changes required to see TLS(version 1.2) when we are communicating with TCP. Is it possible on wireshark???</p><p>thanks Bhuvnesh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-with" rel="tag" title="see questions tagged &#39;with&#39;">with</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '16, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/bdaab301d47d057eedf81801d90990d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhuvnesh&#39;s gravatar image" /><p><span>bhuvnesh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhuvnesh has no accepted answers">0%</span></p></div></div><div id="comments-container-57780" class="comments-container"></div><div id="comment-tools-57780" class="comment-tools"></div><div class="clear"></div><div id="comment-57780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57784"></span>

<div id="answer-container-57784" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57784-score" class="post-score" title="current number of votes">0</div><span id="post-57784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark quite happily spots TLS 1.2, there should be no configuration required, unless the traffic is on a non-default port. In that case either use "Decode As ..." or set the preferences for the protocol carried in the TLS tunnel, e.g. for HTTP the "SSL/TLS Ports" preference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '16, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57784" class="comments-container"><span id="57786"></span><div id="comment-57786" class="comment"><div id="post-57786-score" class="comment-score"></div><div class="comment-text"><p>I know about HTTP settings "HTTP the "SSL/TLS Ports" preference." but we are working communicating on TCP layer. for TCP i don't see any option in wireshark.</p></div><div id="comment-57786-info" class="comment-info"><span class="comment-age">(02 Dec '16, 03:34)</span> <span class="comment-user userinfo">bhuvnesh</span></div></div><span id="57787"></span><div id="comment-57787" class="comment"><div id="post-57787-score" class="comment-score"></div><div class="comment-text"><p>Is there a dissector for the protocol you are using in the TLS tunnel? If so, then configure that dissector, else you'll have to try "Decode As .."</p></div><div id="comment-57787-info" class="comment-info"><span class="comment-age">(02 Dec '16, 03:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-57784" class="comment-tools"></div><div class="clear"></div><div id="comment-57784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

