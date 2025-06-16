+++
type = "question"
title = "how to import .osm files to postGIS?"
description = '''maybe it&#x27;s a simple question for most of you ,but it really confused me,does it have to use commend line tools to open it since i&#x27;ve seen somebody open the osm file by simple dragging? i can&#x27;t remember the tool,can someone give me some clues?'''
date = "2014-03-03T02:02:00Z"
lastmod = "2014-03-03T11:00:00Z"
weight = 31199
keywords = [ "osm", "postgis" ]
aliases = [ "/questions/31199" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to import .osm files to postGIS?](/questions/31199/how-to-import-osm-files-to-postgis)

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
<span id="post-31199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31199-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>maybe it's a simple question for most of you ,but it really confused me,does it have to use commend line tools to open it since i've seen somebody open the osm file by simple dragging? i can't remember the tool,can someone give me some clues?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '14, 02:02</strong></p>
<img src="https://secure.gravatar.com/avatar/dc5cc6c6e5f35c966c1dccf8493f2dce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="post_cs&#39;s gravatar image" />
<p><span>post_cs</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="post_cs has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '14, 02:02</strong> </span></p>
</div>
</div>
<div id="comments-container-31199" class="comments-container">
&#10;</div>
<div id="comment-tools-31199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31199-form-container" class="comment-form-container">
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

<span id="31202"></span>

<div id="answer-container-31202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31202-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a few tools to load osm data into a postgis db, the most commons being <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a>, <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a>, and <a href="https://wiki.openstreetmap.org/wiki/Imposm">imposm</a>. There are many different use cases; what tool and which options you use really depends on <em>what you are trying to achieve</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '14, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-31202" class="comments-container">
&#10;</div>
<div id="comment-tools-31202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31202-form-container" class="comment-form-container">
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

