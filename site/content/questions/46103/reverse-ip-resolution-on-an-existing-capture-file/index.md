+++
type = "question"
title = "Reverse IP resolution on an existing capture file"
description = '''Is it possible for Wireshark to resolve IP to hostname using external DNS server on an existing capture file? &quot;show address resolution&quot; is empty for this IP I&#x27;ve set &quot;Resolve IP address&quot; &amp;amp; &quot;Use an external network name resolver&quot; I open the trace, but don&#x27;t see any DNS requests going out on the n...'''
date = "2015-09-24T04:20:00Z"
lastmod = "2015-09-24T09:52:00Z"
weight = 46103
keywords = [ "dns" ]
aliases = [ "/questions/46103" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse IP resolution on an existing capture file](/questions/46103/reverse-ip-resolution-on-an-existing-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46103-score" class="post-score" title="current number of votes">0</div><span id="post-46103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible for Wireshark to resolve IP to hostname using external DNS server on an existing capture file?</p><p>"show address resolution" is empty for this IP I've set "Resolve IP address" &amp; "Use an external network name resolver"</p><p>I open the trace, but don't see any DNS requests going out on the network to try to resolve all IPs of this file.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-46103" class="comments-container"><span id="46108"></span><div id="comment-46108" class="comment"><div id="post-46108-score" class="comment-score">1</div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version?</p></div><div id="comment-46108-info" class="comment-info"><span class="comment-age">(24 Sep '15, 08:35)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="46112"></span><div id="comment-46112" class="comment"><div id="post-46112-score" class="comment-score"></div><div class="comment-text"><p>OS X - Wireshark 1.12.3</p></div><div id="comment-46112-info" class="comment-info"><span class="comment-age">(24 Sep '15, 09:26)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div></div><div id="comment-tools-46103" class="comment-tools"></div><div class="clear"></div><div id="comment-46103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46114"></span>

<div id="answer-container-46114" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46114-score" class="post-score" title="current number of votes">0</div><span id="post-46114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TomLaBaude has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Oups... Solution was to upgrade from 1.12.3 to 1.12.7 Thanks <span>@Jaap</span> for the hint</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-46114" class="comments-container"></div><div id="comment-tools-46114" class="comment-tools"></div><div class="clear"></div><div id="comment-46114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

