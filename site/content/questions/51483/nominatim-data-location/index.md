+++
type = "question"
title = "Nominatim data location"
description = '''I have a local copy of Nominatim running on a linux VM and I&#x27;m trying to find where the data is stored locally. My Nominatim copy is functioning perfectly, I&#x27;m just wondering where the ./utils/setup.php --osm-file &amp;lt;your planet file&amp;gt; --all [--osm2pgsql-cache 18000] 2&amp;gt;&amp;amp;1 | tee setup.log l...'''
date = "2016-08-17T12:39:00Z"
lastmod = "2016-08-17T13:11:00Z"
weight = 51483
keywords = [ "nominatim" ]
aliases = [ "/questions/51483" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim data location](/questions/51483/nominatim-data-location)

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
<span id="post-51483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51483-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a local copy of Nominatim running on a linux VM and I'm trying to find where the data is stored locally. My Nominatim copy is functioning perfectly, I'm just wondering where the <code>./utils/setup.php --osm-file &lt;your planet file&gt; --all [--osm2pgsql-cache 18000] 2&gt;&amp;1 | tee setup.log</code> line puts the data.</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '16, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-51483" class="comments-container">
&#10;</div>
<div id="comment-tools-51483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51483-form-container" class="comment-form-container">
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

<span id="51488"></span>

<div id="answer-container-51488" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51488-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JamesGould has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>setup.php creates and fills a postgresql database named "nominatim". In the filesystem the postgres data directory is usually /var/lib/postgresql/.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '16, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '16, 13:10</strong> </span></p>
</div>
</div>
<div id="comments-container-51488" class="comments-container">
<span id="51489"></span>
<div id="comment-51489" class="comment">
<div id="post-51489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much!</p>
</div>
<div id="comment-51489-info" class="comment-info">
<span class="comment-age">(17 Aug '16, 13:11)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
</div>
<div id="comment-tools-51488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51488-form-container" class="comment-form-container">
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

