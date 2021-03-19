+++
type = "question"
title = "wireshark hsts"
description = '''Hi, how can I use Wireshark to see if a particular web site, web app is using HSTS?  Thanks '''
date = "2017-02-17T05:35:00Z"
lastmod = "2017-02-18T02:04:00Z"
weight = 59495
keywords = [ "hsts" ]
aliases = [ "/questions/59495" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark hsts](/questions/59495/wireshark-hsts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59495-score" class="post-score" title="current number of votes">0</div><span id="post-59495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>how can I use Wireshark to see if a particular web site, web app is using HSTS?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hsts" rel="tag" title="see questions tagged &#39;hsts&#39;">hsts</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '17, 05:35</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-59495" class="comments-container"></div><div id="comment-tools-59495" class="comment-tools"></div><div class="clear"></div><div id="comment-59495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59502"></span>

<div id="answer-container-59502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59502-score" class="post-score" title="current number of votes">0</div><span id="post-59502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>IF you can decrypt the HTTP exchange between server and client, you can check to see if the HSTS header is present in the HTTP response from the server. IF NOT then you can't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '17, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59502" class="comments-container"></div><div id="comment-tools-59502" class="comment-tools"></div><div class="clear"></div><div id="comment-59502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59510"></span>

<div id="answer-container-59510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59510-score" class="post-score" title="current number of votes">0</div><span id="post-59510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jaap said: If you can decrypt the traffic you will be able to see the HSTS header.</p><p>If not you can use the Web Developer tools in your browser (available in/for Chrome, Safari, Firefox, Internet Explorer) or you can configure a proxy like <a href="http://www.telerik.com/fiddler">Fiddler</a> to see the headers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '17, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-59510" class="comments-container"><span id="59513"></span><div id="comment-59513" class="comment"><div id="post-59513-score" class="comment-score"></div><div class="comment-text"><p>cURL does it without acting as a proxy and without having to decrypt the payload:</p><p><a href="https://www.owasp.org/index.php/Test_HTTP_Strict_Transport_Security_(OTG-CONFIG-007)">https://www.owasp.org/index.php/Test_HTTP_Strict_Transport_Security_(OTG-CONFIG-007)</a></p></div><div id="comment-59513-info" class="comment-info"><span class="comment-age">(17 Feb '17, 11:58)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="59523"></span><div id="comment-59523" class="comment"><div id="post-59523-score" class="comment-score"></div><div class="comment-text"><p>cURL does receive the plain text payload though, the library it uses for the TLS connection does the decryption for it.</p><p>Wireshark does not originate any connections so do not have access to the key, and hence the plain text payload unless the user provides the keying material.</p></div><div id="comment-59523-info" class="comment-info"><span class="comment-age">(18 Feb '17, 02:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-59510" class="comment-tools"></div><div class="clear"></div><div id="comment-59510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

