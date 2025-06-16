+++
type = "question"
title = "How to configure id editor on own server without Oauth"
description = '''I&#x27;m newer in Web mapping, I need web map editor. I found ID Editor but I couldn&#x27;t configure to my osm server! I don&#x27;t know how working with API and Oauth. How to configure id editor on own server without Oauth. And how to create API. Thanks.'''
date = "2016-02-01T05:16:00Z"
lastmod = "2016-02-01T13:11:00Z"
weight = 47774
keywords = [ "ideditor", "oauth", "api", "osm", "mapping" ]
aliases = [ "/questions/47774" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure id editor on own server without Oauth](/questions/47774/how-to-configure-id-editor-on-own-server-without-oauth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47774-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm newer in Web mapping, I need web map editor. I found ID Editor but I couldn't configure to my osm server! I don't know how working with API and Oauth. How to configure id editor on own server without Oauth. And how to create API. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '16, 05:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f54945518479ca3573bf3e268ccd4f24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fizmasoft&#39;s gravatar image" />
<p><span>fizmasoft</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fizmasoft has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47774" class="comments-container">
<span id="47789"></span>
<div id="comment-47789" class="comment">
<div id="post-47789-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/35127317/how-to-configure-id-editor-in-my-server-without-oauth">https://stackoverflow.com/questions/35127317/how-to-configure-id-editor-in-my-server-without-oauth</a></p>
</div>
<div id="comment-47789-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 12:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="47791"></span>
<div id="comment-47791" class="comment">
<div id="post-47791-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You'll probably need to provide a lot more details of what you've done so far and what you're actually trying to achieve.</p>
<p>Your question contains the sentence "And how to create API." so it's really unclear what you have done, and what you're trying to do.</p>
<p>Try adding information such as "I'm trying to create a website that allows users to edit X data in Y area; I expect user account details to be held in Z and to acheive that so far I've installed A, B and C".</p>
</div>
<div id="comment-47791-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 12:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47794"></span>
<div id="comment-47794" class="comment">
<div id="post-47794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have installed PostgreSQL-9.3, osm2pgsql, apache2-mod_tile, renderd, mapnik, mapnik-python, and eth. I have created my osm server and I want to edit and draw map. Just I need map id editor!</p>
</div>
<div id="comment-47794-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 13:08)</span> <span class="comment-user userinfo">fizmasoft</span>
</div>
</div>
<span id="47795"></span>
<div id="comment-47795" class="comment">
<div id="post-47795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Those packages suggest that you've set up a rendering server, not an API that people can use for map editing. You still haven't explained what your ultimate goal is.</p>
<p>Just checking - have you read <a href="https://wiki.openstreetmap.org/wiki/The_Rails_Port">https://wiki.openstreetmap.org/wiki/The_Rails_Port</a> and the various links from it?</p>
</div>
<div id="comment-47795-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 13:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47774-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

