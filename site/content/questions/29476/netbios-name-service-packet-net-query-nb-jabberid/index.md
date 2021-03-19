+++
type = "question"
title = "Netbios Name Service packet - &quot;Net Query NB ##JABBERID##&quot;"
description = '''So Im having network bogging down issues. Upon capturing 30 minutes worth of packets, I have come across quite a few (afew thounsand) packets like the following: # Time Src Dest Protocol Length info &quot;5227 200.570462000 10.42.91.105 10.42.91.255 NBNS 92 Name query NB ##JABBERID##&amp;lt;00&amp;gt;&quot; Does anyo...'''
date = "2014-02-05T17:17:00Z"
lastmod = "2014-02-05T23:44:00Z"
weight = 29476
keywords = [ "services", "sniffing", "name", "packet", "netbios" ]
aliases = [ "/questions/29476" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Netbios Name Service packet - "Net Query NB \#\#JABBERID\#\#"](/questions/29476/netbios-name-service-packet-net-query-nb-jabberid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29476-score" class="post-score" title="current number of votes">0</div><span id="post-29476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So Im having network bogging down issues. Upon capturing 30 minutes worth of packets, I have come across quite a few (afew thounsand) packets like the following:</p><p># Time Src Dest Protocol Length info<br />
"5227 200.570462000 10.42.91.105 10.42.91.255 NBNS 92 Name query NB ##JABBERID##&lt;00&gt;"</p><p>Does anyone know what the ##JABBERID## means? I cant find any documentation on it anywhere...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-services" rel="tag" title="see questions tagged &#39;services&#39;">services</span> <span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-netbios" rel="tag" title="see questions tagged &#39;netbios&#39;">netbios</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '14, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/c7793b954a8b89674ae2bc2721ab6266?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m0rd3cai&#39;s gravatar image" /><p><span>m0rd3cai</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m0rd3cai has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-29476" class="comments-container"></div><div id="comment-tools-29476" class="comment-tools"></div><div class="clear"></div><div id="comment-29476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29479"></span>

<div id="answer-container-29479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29479-score" class="post-score" title="current number of votes">0</div><span id="post-29479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please check if there is a <a href="http://en.m.wikipedia.org/wiki/List_of_Jabber_client_software">Jabber/XMPP client</a> running on 10.42.91.105. If so, stop it and check again if you see those frames.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '14, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29479" class="comments-container"></div><div id="comment-tools-29479" class="comment-tools"></div><div class="clear"></div><div id="comment-29479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

