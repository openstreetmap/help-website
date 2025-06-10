+++
type = "question"
title = "Possible to use one DB for Nominatim and Tile-Server"
description = '''Hello guys, it is possible to use only 1 database for a tile-server (mod_tile) and nominatim? Or I need to create a seperate one for the nominatim-search? thanks in advance'''
date = "2016-11-16T15:06:00Z"
lastmod = "2018-06-04T12:07:00Z"
weight = 52978
keywords = [ "nominatim", "tileserver" ]
aliases = [ "/questions/52978" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Possible to use one DB for Nominatim and Tile-Server](/questions/52978/possible-to-use-one-db-for-nominatim-and-tile-server)

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
<span id="post-52978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52978-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys,</p>
<p>it is possible to use only 1 database for a tile-server (mod_tile) and nominatim? Or I need to create a seperate one for the nominatim-search?</p>
<p>thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '16, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad332fb85ece95d8d53ae63eea5d534f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hevilp&#39;s gravatar image" />
<p><span>hevilp</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hevilp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52978" class="comments-container">
&#10;</div>
<div id="comment-tools-52978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52978-form-container" class="comment-form-container">
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

<span id="52980"></span>

<div id="answer-container-52980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52980-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-52980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will currently need two database instances (which naturally can be created in the same "database" you will likely have to change the default name of one of them).</p>
<p>PS: this only makes sense if we are talking about a small extract of OSM data and yes some of the information is duplicate in such a setup.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '16, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '16, 15:10</strong> </span></p>
</div>
</div>
<div id="comments-container-52980" class="comments-container">
<span id="64015"></span>
<div id="comment-64015" class="comment">
<div id="post-64015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it still valid in 2018? Why can't both services use the same schema in DB? What data is different and what is duplicated?</p>
</div>
<div id="comment-64015-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 11:22)</span> <span class="comment-user userinfo">Defozo</span>
</div>
</div>
<span id="64017"></span>
<div id="comment-64017" class="comment">
<div id="post-64017-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Major parts of the database schema are different (as the use case is very different).</p>
</div>
<div id="comment-64017-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 12:07)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52980-form-container" class="comment-form-container">
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

