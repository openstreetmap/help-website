+++
type = "question"
title = "I can&#x27;t get Odessa (Ukraine) node with overpass API"
description = '''Hi! I&#x27;m wrote a small tool that make a request to a overpass server and returns a list of ways and POIs of concrete city (e.g. Odessa). Early all works fine, but several weeks ago I&#x27;m checked work of my tools and received a message that &quot;city is not found&quot;. What can I do in this case? If I understoo...'''
date = "2012-05-04T11:15:00Z"
lastmod = "2012-05-06T19:35:00Z"
weight = 12543
keywords = [ "overpass", "api" ]
aliases = [ "/questions/12543" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I can't get Odessa (Ukraine) node with overpass API](/questions/12543/i-cant-get-odessa-ukraine-node-with-overpass-api)

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
<span id="post-12543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12543-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I'm wrote a small tool that make a request to a overpass server and returns a list of ways and POIs of concrete city (e.g. Odessa). Early all works fine, but several weeks ago I'm checked work of my tools and received a message that <em>"city is not found"</em>. What can I do in this case? If I understood correctly, <strong>Odessa node was deleted from OSM database</strong>... Please answer on my question. Thanks a lot!</p>
<p><a href="http://overpass.osm.rambler.ru/cgi/interpreter?data=%5Bout:json%5D;node%5B%22name:en%22=%22Odesa%22%5D;relation(around:1000)%5B%22admin_level%22=%228%22%5D;foreach-%3E.a((way(r.a);node(w);););out;">This is my request...</a></p>
<p><strong>Honestly regards Nikolay Druchaty. Mail: druchaty@gmail.com</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '12, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a20a11b76f1df6d361de226d4bc7c12d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikolay%20Druchaty&#39;s gravatar image" />
<p><span>Nikolay Druc...</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikolay Druchaty has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 May '12, 11:20</strong> </span></p>
</div>
</div>
<div id="comments-container-12543" class="comments-container">
<span id="12581"></span>
<div id="comment-12581" class="comment">
<div id="post-12581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My request is not working again. Please check it out. Thanks!</p>
</div>
<div id="comment-12581-info" class="comment-info">
<span class="comment-age">(06 May '12, 19:35)</span> <span class="comment-user userinfo">Nikolay Druc...</span>
</div>
</div>
</div>
<div id="comment-tools-12543" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12543-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12558"></span>

<div id="answer-container-12558" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12558-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I <a href="http://www.openstreetmap.org/browse/changeset/11506004">restored</a> the deleted place node. After the Overpass server gets the update, you should be fine again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '12, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '12, 19:34</strong> </span></p>
</div>
</div>
<div id="comments-container-12558" class="comments-container">
<span id="12572"></span>
<div id="comment-12572" class="comment">
<div id="post-12572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for your change!</p>
</div>
<div id="comment-12572-info" class="comment-info">
<span class="comment-age">(05 May '12, 22:15)</span> <span class="comment-user userinfo">Nikolay Druc...</span>
</div>
</div>
<span id="12574"></span>
<div id="comment-12574" class="comment">
<div id="post-12574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are welcome</p>
<p>If you are satisfied with the answer you received, mark this question as closed, please.</p>
</div>
<div id="comment-12574-info" class="comment-info">
<span class="comment-age">(06 May '12, 00:46)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-12558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12558-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

