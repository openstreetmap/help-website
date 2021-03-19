+++
type = "question"
title = "wireshark with proxy?"
description = '''Basically i want to use wireshark to grab ips in skype but i can&#x27;t figure out how to get it to do it since i have a proxy and all my skype packets are sent threw the proxy. Anyone know how to do this? Thanks'''
date = "2014-11-16T12:42:00Z"
lastmod = "2014-12-27T11:10:00Z"
weight = 37886
keywords = [ "sniffing", "skype", "proxy", "packet", "wireshark" ]
aliases = [ "/questions/37886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark with proxy?](/questions/37886/wireshark-with-proxy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37886-score" class="post-score" title="current number of votes">0</div><span id="post-37886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Basically i want to use wireshark to grab ips in skype but i can't figure out how to get it to do it since i have a proxy and all my skype packets are sent threw the proxy. Anyone know how to do this? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-skype" rel="tag" title="see questions tagged &#39;skype&#39;">skype</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '14, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/72205730dcae6ac9111816e31b79dd9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bdoug101&#39;s gravatar image" /><p><span>bdoug101</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bdoug101 has no accepted answers">0%</span></p></div></div><div id="comments-container-37886" class="comments-container"><span id="38740"></span><div id="comment-38740" class="comment"><div id="post-38740-score" class="comment-score"></div><div class="comment-text"><p>Hello, I am having the same problem ... has a special command to find the exact header? like udp.srcport...</p></div><div id="comment-38740-info" class="comment-info"><span class="comment-age">(27 Dec '14, 10:38)</span> <span class="comment-user userinfo">Anon741</span></div></div><span id="38744"></span><div id="comment-38744" class="comment"><div id="post-38744-score" class="comment-score"></div><div class="comment-text"><p>see my answer. It contains everything you need.</p></div><div id="comment-38744-info" class="comment-info"><span class="comment-age">(27 Dec '14, 11:10)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37886" class="comment-tools"></div><div class="clear"></div><div id="comment-37886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37921"></span>

<div id="answer-container-37921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37921-score" class="post-score" title="current number of votes">1</div><span id="post-37921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Skype seems to be using "skype" in the <strong>User-Agent:</strong> header (HTTP) when talking to a proxy, so you could (probably) identify Skype traffic by looking at that header in a capture file.</p><blockquote><p>http.user_agent contains "kype"</p></blockquote><p>This will match lower case and upper case sSkype.</p><p>If you've identified those frame, simply look at the <strong>Host:</strong> Header and or the URL to identify the servers Skype is try to communicate with.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37921" class="comments-container"></div><div id="comment-tools-37921" class="comment-tools"></div><div class="clear"></div><div id="comment-37921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

