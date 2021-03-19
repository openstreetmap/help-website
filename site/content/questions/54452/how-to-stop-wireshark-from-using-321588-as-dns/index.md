+++
type = "question"
title = "How to stop Wireshark from using 32.1.5.88 as DNS?"
description = '''How do I stop Wireshark from using 32.1.5.88 as a Domain Name Server? It never receives a response from that IP, and until it switches over to using the system&#x27;s DNS addresses, all the domain names are unresolved.'''
date = "2016-07-29T14:21:00Z"
lastmod = "2016-07-30T19:46:00Z"
weight = 54452
keywords = [ "dns" ]
aliases = [ "/questions/54452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to stop Wireshark from using 32.1.5.88 as DNS?](/questions/54452/how-to-stop-wireshark-from-using-321588-as-dns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54452-score" class="post-score" title="current number of votes">0</div><span id="post-54452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I stop Wireshark from using 32.1.5.88 as a Domain Name Server? It never receives a response from that IP, and until it switches over to using the system's DNS addresses, all the domain names are unresolved.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '16, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/6249379fb0f05126b574b84c81f36e32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CElliott&#39;s gravatar image" /><p><span>CElliott</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CElliott has no accepted answers">0%</span></p></div></div><div id="comments-container-54452" class="comments-container"><span id="54453"></span><div id="comment-54453" class="comment"><div id="post-54453-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure what you mean. Wireshark <strong>always</strong> uses the system's DNS addresses.</p></div><div id="comment-54453-info" class="comment-info"><span class="comment-age">(29 Jul '16, 18:45)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-54452" class="comment-tools"></div><div class="clear"></div><div id="comment-54452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54467"></span>

<div id="answer-container-54467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54467-score" class="post-score" title="current number of votes">0</div><span id="post-54467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Under Wireshark Capture Options, deselect the [Use external network name resolver].</p><p>FWIW</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '16, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-54467" class="comments-container"></div><div id="comment-tools-54467" class="comment-tools"></div><div class="clear"></div><div id="comment-54467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

