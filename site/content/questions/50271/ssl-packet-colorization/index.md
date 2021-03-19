+++
type = "question"
title = "SSL Packet Colorization"
description = '''SSL and TLS v2 are both supported protocols, but I cannot create a packet colorization rule to highlight either of these. Is there an update to fix this, or is it not possible?'''
date = "2016-02-17T07:58:00Z"
lastmod = "2016-02-20T11:51:00Z"
weight = 50271
keywords = [ "tls", "ssl", "colorization503" ]
aliases = [ "/questions/50271" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Packet Colorization](/questions/50271/ssl-packet-colorization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50271-score" class="post-score" title="current number of votes">0</div><span id="post-50271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>SSL and TLS v2 are both supported protocols, but I cannot create a packet colorization rule to highlight either of these. Is there an update to fix this, or is it not possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-colorization503" rel="tag" title="see questions tagged &#39;colorization503&#39;">colorization503</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '16, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/b5cfc0cb11e9fe8a78d6d5cc137559cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="banjoguru&#39;s gravatar image" /><p><span>banjoguru</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="banjoguru has no accepted answers">0%</span></p></div></div><div id="comments-container-50271" class="comments-container"><span id="50342"></span><div id="comment-50342" class="comment"><div id="post-50342-score" class="comment-score"></div><div class="comment-text"><p>How are you attempting to add colorization? What version are you using? I just tried adding a coloring rule for "ssl" and it worked just fine.</p></div><div id="comment-50342-info" class="comment-info"><span class="comment-age">(19 Feb '16, 06:42)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-50271" class="comment-tools"></div><div class="clear"></div><div id="comment-50271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50374"></span>

<div id="answer-container-50374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50374-score" class="post-score" title="current number of votes">0</div><span id="post-50374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the question is about how to use a coloring rule that indicates whether an SSL Record is SSL3.0 vs. TLS (1.0 1.1 1.2) these filters might do what you're seeking (even if wireshark has not recognized the data as SSL)</p><p>They will check whether the first data bytes after the TCP header (and after timestamp options if they exist) are x1403vv x1503vv x1603vv or x1703vv<br />
If vv is 00 then chances are good that this is a SSLv30 record If vv is between 1 and 3 it "might" be a TLS1.0, TLS1.1 or TLS1.2 record</p><p>(tcp[12,21]==5003 &amp;&amp; tcp[20]&gt;13&amp;&amp;tcp[20]&lt;18&amp;&amp; tcp[22]&lt;1)||((tcp[12,33]==8003 &amp;&amp; tcp[32]&gt;13 &amp;&amp; tcp[32]&lt;18 &amp;&amp; tcp[34]&lt;1))</p><p>(tcp[12,21]==5003 &amp;&amp; tcp[20]&gt;13&amp;&amp;tcp[20]&lt;18&amp;&amp; tcp[22]&lt;4)||((tcp[12,33]==8003 &amp;&amp; tcp[32]&gt;13 &amp;&amp; tcp[32]&lt;18 &amp;&amp; tcp[34]&lt;4))</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_664.png" alt="alt text" /></p><p>Hope this answers (part of) your question.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '16, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-50374" class="comments-container"></div><div id="comment-tools-50374" class="comment-tools"></div><div class="clear"></div><div id="comment-50374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

