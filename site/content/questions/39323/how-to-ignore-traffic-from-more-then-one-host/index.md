+++
type = "question"
title = "how to ignore traffic from more then one host."
description = '''I am trying to capture data but am getting a flood of data from a replicating server that i need to filter out. Basically i would like to filter out any traffic between 192.168.1.1 and 192.168.1.2 as well as ignore traffic that has a source address of 192.168.1.3 to either 192.168.1.1 and 192.168.1....'''
date = "2015-01-20T14:34:00Z"
lastmod = "2015-01-21T12:32:00Z"
weight = 39323
keywords = [ "host", "filtering" ]
aliases = [ "/questions/39323" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to ignore traffic from more then one host.](/questions/39323/how-to-ignore-traffic-from-more-then-one-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39323-score" class="post-score" title="current number of votes">0</div><span id="post-39323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture data but am getting a flood of data from a replicating server that i need to filter out. Basically i would like to filter out any traffic between 192.168.1.1 and 192.168.1.2 as well as ignore traffic that has a source address of 192.168.1.3 to either 192.168.1.1 and 192.168.1.2.</p><p>I have tried these captures and the only one that seems to work the way i need it is the first one:</p><p>tshark not host 192.168.1.1 and not host 192.168.1.2</p><p>When I have tried to filter out the src ip to the dst ip I noticed i was filtering all traffic:</p><p>tshark not src 192.168.1.3 and not dst 192.168.1.1</p><p>Also, how would I join the filters into one line?</p><p>tshark not host 192.168.1.1 and not host 192.168.1.2 and not src 192.168.1.3 and not dst 192.168.1.1</p><p>Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-host" rel="tag" title="see questions tagged &#39;host&#39;">host</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '15, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/9b4c8d50d3e1d194842afff70318c410?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhorse&#39;s gravatar image" /><p><span>dhorse</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhorse has no accepted answers">0%</span></p></div></div><div id="comments-container-39323" class="comments-container"></div><div id="comment-tools-39323" class="comment-tools"></div><div class="clear"></div><div id="comment-39323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39329"></span>

<div id="answer-container-39329" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39329-score" class="post-score" title="current number of votes">1</div><span id="post-39329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dhorse has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From your post:</p><blockquote><p>any traffic between 192.168.1.1 and 192.168.1.2</p></blockquote><p>This would create a filter like:</p><pre><code>host 192.168.1.1 and host 192.168.1.2</code></pre><p>And:</p><blockquote><p>a source address of 192.168.1.3 to either 192.168.1.1 and 192.168.1.2.</p></blockquote><p>This would create a filter like:</p><pre><code>src host 192.168.1.3 and (dst host 192.168.1.1 or 192.168.1.2)</code></pre><p>Combined it makes:</p><pre><code>(host 192.168.1.1 and host 192.168.1.2) or (src host 192.168.1.3 and (dst host 192.168.1.1 or 192.168.1.2))</code></pre><p>And then you don't want to see this traffic, so it becomes:</p><pre><code>not ( (host 192.168.1.1 and host 192.168.1.2) or (src host 192.168.1.3 and (dst host 192.168.1.1 or 192.168.1.2)) )</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '15, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39329" class="comments-container"><span id="39341"></span><div id="comment-39341" class="comment"><div id="post-39341-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply, but when ever i try to add the parenthesis, I get a message saying, "-bash: syntax error near unexpected token `('"</p></div><div id="comment-39341-info" class="comment-info"><span class="comment-age">(21 Jan '15, 12:13)</span> <span class="comment-user userinfo">dhorse</span></div></div><span id="39342"></span><div id="comment-39342" class="comment"><div id="post-39342-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ)</p><p>That is because the parenthesis are also used by bash, to make sure they are not interpreted by bash, you need to put the whole capture filter in quotes so that bash sees it as a string and passes the whole filter to tshark.</p></div><div id="comment-39342-info" class="comment-info"><span class="comment-age">(21 Jan '15, 12:27)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="39343"></span><div id="comment-39343" class="comment"><div id="post-39343-score" class="comment-score"></div><div class="comment-text"><p>That works great, thanks for the help.</p></div><div id="comment-39343-info" class="comment-info"><span class="comment-age">(21 Jan '15, 12:32)</span> <span class="comment-user userinfo">dhorse</span></div></div></div><div id="comment-tools-39329" class="comment-tools"></div><div class="clear"></div><div id="comment-39329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

