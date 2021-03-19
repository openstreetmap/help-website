+++
type = "question"
title = "exchange smtp auth attack ?"
description = '''hello, Recently we discovered some failed authentication requests in the Exchange Transport Logs:  In the attached screenshot you can see that the user name is editor and we receive lot&#x27;s of entries for different &quot;users&quot;. The environment is: Websense --&amp;gt; external firewall --&amp;gt;1 load balancer --...'''
date = "2016-01-12T12:48:00Z"
lastmod = "2016-01-12T13:24:00Z"
weight = 49144
keywords = [ "exchange" ]
aliases = [ "/questions/49144" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [exchange smtp auth attack ?](/questions/49144/exchange-smtp-auth-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49144-score" class="post-score" title="current number of votes">0</div><span id="post-49144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>Recently we discovered some failed authentication requests in the Exchange Transport Logs:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/snip1.PNG" alt="alt text" /></p><p>In the attached screenshot you can see that the user name is <strong>editor</strong> and we receive lot's of entries for different "users". The environment is:</p><p>Websense --&gt; external firewall --&gt;1 load balancer --&gt; encryption server --&gt; internal firewall --&gt;2 load balancer --&gt; Exchange</p><p>I believe that the connections originate from the internet because I can see failed authentication errors being reported on the encryption server because it reports that the packets are coming from the 1 load balancer's internal facing IP and because the encryption server works as a smtp proxy it passes the smtp connection towards Exchange.</p><p>What would be the post place or places to run a Wireshark capture to be sure where the requests are coming from ?</p><p>It looks to me as someone is trying to hack our Exchange, perhaps smtp auth attack ?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-exchange" rel="tag" title="see questions tagged &#39;exchange&#39;">exchange</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '16, 13:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49144" class="comments-container"></div><div id="comment-tools-49144" class="comment-tools"></div><div class="clear"></div><div id="comment-49144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49146"></span>

<div id="answer-container-49146" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49146-score" class="post-score" title="current number of votes">1</div><span id="post-49146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If I get your drawing right, the SMTP session, if coming from the internet, is encrypted all the way from the internet through to the encryption server, and the encryption server decrypts the incoming messages into plaintext SMTP?</p><p>If so, Wireshark alone may not be enough, because only the logs of the encryption server can unambiguously disclose to you the correlation between the individual encrypted SMTP sessions coming from the internet and their plaintext counterparts you can see at the "inner" side of the encryption server. Only if the traffic is not too heavy, you might be able to find this correlation based on packets' times of occurrence (or rather tcp session establishment times).</p><p>And only after you verify that you can find the mapping at the encryption server, one way or the other, it makes sense to run a Wireshark capture at both the "inner" and "outer" interfaces of the 1st load balancer simultaneously with logging or capturing at the encryption server, and use the SSL/TLS payload of the packets "after" and "before" the loadbalancer to find the correlation between the tcp session from the load balancer to the encryption server and its "source" tcp session from the attacker to the load balancer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49146" class="comments-container"></div><div id="comment-tools-49146" class="comment-tools"></div><div class="clear"></div><div id="comment-49146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

