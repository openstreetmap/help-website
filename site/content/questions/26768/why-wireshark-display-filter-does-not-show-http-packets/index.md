+++
type = "question"
title = "Why Wireshark display filter does not show http packets?"
description = '''Hi, When I use display filter for HTTP it shows only HTTP packets when HTTP message is on standard port i.e. on port 80. But, when message is not using standard port, then display filter not works for HTTP and I need to filter for TCP and then need to find out HTTP packets manually. I want to know w...'''
date = "2013-11-07T22:22:00Z"
lastmod = "2013-11-07T23:16:00Z"
weight = 26768
keywords = [ "filter", "packet-display", "display", "tcp", "display-filter" ]
aliases = [ "/questions/26768" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why Wireshark display filter does not show http packets?](/questions/26768/why-wireshark-display-filter-does-not-show-http-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26768-score" class="post-score" title="current number of votes">2</div><span id="post-26768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When I use display filter for HTTP it shows only HTTP packets when HTTP message is on standard port i.e. on port 80. But, when message is not using standard port, then display filter not works for HTTP and I need to filter for TCP and then need to find out HTTP packets manually.</p><p>I want to know why this happen? Is it standard behavior or I am doing (or expecting) it wrongly.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-packet-display" rel="tag" title="see questions tagged &#39;packet-display&#39;">packet-display</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/4d5a1d4ba48122bcddd239a84b8bf3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pranitkothari&#39;s gravatar image" /><p><span>pranitkothari</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pranitkothari has one accepted answer">100%</span></p></div></div><div id="comments-container-26768" class="comments-container"></div><div id="comment-tools-26768" class="comment-tools"></div><div class="clear"></div><div id="comment-26768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26769"></span>

<div id="answer-container-26769" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26769-score" class="post-score" title="current number of votes">3</div><span id="post-26769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pranitkothari has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is normal behavior. If you want to be able to use the "http" filter for HTTP traffic on non-standard ports you need to tell Wireshark that it IS in fact http on that port. You can do that in the preferences of the HTTP protocol decoder (there's a list of ports that you can edit).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '13, 03:17</strong> </span></p></div></div><div id="comments-container-26769" class="comments-container"></div><div id="comment-tools-26769" class="comment-tools"></div><div class="clear"></div><div id="comment-26769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

