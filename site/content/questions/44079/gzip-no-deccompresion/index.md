+++
type = "question"
title = "gzip no deccompresion"
description = '''why i can&#x27;t see the decrypted text that server reply for the first post request? The seccond post is visible :/ '''
date = "2015-07-12T05:43:00Z"
lastmod = "2015-07-13T13:07:00Z"
weight = 44079
keywords = [ "gzip", "request", "wireshark" ]
aliases = [ "/questions/44079" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [gzip no deccompresion](/questions/44079/gzip-no-deccompresion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44079-score" class="post-score" title="current number of votes">0</div><span id="post-44079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>why i can't see the decrypted text that server reply for the first post request? The seccond post is visible :/</p><p><img src="http://i.imgur.com/AUFMZLE.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gzip" rel="tag" title="see questions tagged &#39;gzip&#39;">gzip</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '15, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/383254ee5dab47c3ae309133697eab20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vladimir21&#39;s gravatar image" /><p><span>Vladimir21</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vladimir21 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-44079" class="comments-container"></div><div id="comment-tools-44079" class="comment-tools"></div><div class="clear"></div><div id="comment-44079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44084"></span>

<div id="answer-container-44084" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44084-score" class="post-score" title="current number of votes">0</div><span id="post-44084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first POST resulted in a server reply consisting of many TCP segments, many of which arrive out of order, whereas the second post gets only 2 segments that arrive in order.<br />
It looks like wireshark is having trouble to reassemble the first reply.<br />
Under Edit-Preferences-Protocols-TCP you can uncheck the 'Allow dissectors to reassemble TCP streams' and wireshark will show you the segment that contains the HTTP OK message. <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-3_n0Pbzlg.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '15, 22:57</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-44084" class="comments-container"><span id="44092"></span><div id="comment-44092" class="comment"><div id="post-44092-score" class="comment-score"></div><div class="comment-text"><p>But i can't see it decompresed .. if I export the stream to C array how can i know witch order is the right one(for concatenate)?</p></div><div id="comment-44092-info" class="comment-info"><span class="comment-age">(13 Jul '15, 06:55)</span> <span class="comment-user userinfo">Vladimir21</span></div></div><span id="44098"></span><div id="comment-44098" class="comment"><div id="post-44098-score" class="comment-score"></div><div class="comment-text"><p>"Follow TCP Stream", which I believe is what you are trying, does <strong>not</strong> decompress the content!</p></div><div id="comment-44098-info" class="comment-info"><span class="comment-age">(13 Jul '15, 08:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="44101"></span><div id="comment-44101" class="comment"><div id="post-44101-score" class="comment-score"></div><div class="comment-text"><p>So this question is about decompressing the gzip-ed http content of the first POST request? As per <a href="https://en.wikipedia.org/wiki/HTTP_compression">https://en.wikipedia.org/wiki/HTTP_compression</a><br />
And the reply to the second post is also Content-Encoding: gzip ?</p></div><div id="comment-44101-info" class="comment-info"><span class="comment-age">(13 Jul '15, 10:04)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="44110"></span><div id="comment-44110" class="comment"><div id="post-44110-score" class="comment-score"></div><div class="comment-text"><p>i use "Follow TCP Stream" to export all the reply to hex array for C++ to concatenate all of them to just one(to manual inflate gzip).</p><p>Booth of the request are to the same page (diferent post value) .. first reply contain a big text and i'm unable to see it .. seccond reply i can see the un-gziped text</p></div><div id="comment-44110-info" class="comment-info"><span class="comment-age">(13 Jul '15, 13:07)</span> <span class="comment-user userinfo">Vladimir21</span></div></div></div><div id="comment-tools-44084" class="comment-tools"></div><div class="clear"></div><div id="comment-44084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

