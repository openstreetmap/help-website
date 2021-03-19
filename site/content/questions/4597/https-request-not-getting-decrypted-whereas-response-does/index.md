+++
type = "question"
title = "HTTPS request not getting decrypted whereas response does"
description = '''Folks, I am running wireshark from the client browser machine and server service is running on another machine. I want to see what all are the request and response that are made by the client by running wireshark on client machine. I have configured the RSA key list for SSL as  &amp;lt;server-ip&amp;gt;,443...'''
date = "2011-06-16T09:52:00Z"
lastmod = "2011-06-16T10:20:00Z"
weight = 4597
keywords = [ "ssl", "svchost", "https", "missing" ]
aliases = [ "/questions/4597" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HTTPS request not getting decrypted whereas response does](/questions/4597/https-request-not-getting-decrypted-whereas-response-does)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4597-score" class="post-score" title="current number of votes">0</div><span id="post-4597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folks,</p><p>I am running wireshark from the client browser machine and server service is running on another machine. I want to see what all are the request and response that are made by the client by running wireshark on client machine.</p><p>I have configured the RSA key list for SSL as</p><p>&lt;server-ip&gt;,443,http,c:\certs\myssl.pem</p><p>Also there is a service svchost.exe which runs as local service currently i am running in as administrator though i find those requests made by svchost.exe to be missing in the capture</p><p>my capture filter is "port 443"</p><p>regards bekz</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-svchost" rel="tag" title="see questions tagged &#39;svchost&#39;">svchost</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '11, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/59b739ec2c7c9560738289f98172313a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bekz&#39;s gravatar image" /><p><span>bekz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bekz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 22:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4597" class="comments-container"></div><div id="comment-tools-4597" class="comment-tools"></div><div class="clear"></div><div id="comment-4597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4598"></span>

<div id="answer-container-4598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4598-score" class="post-score" title="current number of votes">0</div><span id="post-4598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My first thought is in order to decrypt the encrypted traffic, capture the ssl handshake 1st as a part of the traffic. ssl.record.content_type == 22 will show the handshake packets. If the handshake is successful and present, use the "Decrypted SSL data" tab which should be present at the bottom of the packet pane to display decrypted traffic.</p><p>Hope this is helpful, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '11, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4598" class="comments-container"></div><div id="comment-tools-4598" class="comment-tools"></div><div class="clear"></div><div id="comment-4598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

