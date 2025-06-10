+++
type = "question"
title = "duplicate key value violates unique constraint &quot;relations_pkey&quot;"
description = '''When i use osmosis command to import data into the openstreetmap database, some error appears, such as duplicate key value violates unique constraint &quot;relations_pkey&quot;. The command that i used is ./osmosis-latest/bin/osmosis --read-pbf file=&quot;planet/chengdu_china.osm.pbf&quot; --write-apidb host=&quot;localhost...'''
date = "2016-09-12T05:15:00Z"
lastmod = "2016-09-12T12:44:00Z"
weight = 51995
keywords = [ "postgresql", "osmosis", "railsport" ]
aliases = [ "/questions/51995" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [duplicate key value violates unique constraint "relations_pkey"](/questions/51995/duplicate-key-value-violates-unique-constraint-relations_pkey)

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
<span id="post-51995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51995-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When i use osmosis command to import data into the openstreetmap database, some error appears, such as duplicate key value violates unique constraint "relations_pkey". The command that i used is <strong>./osmosis-latest/bin/osmosis --read-pbf file="planet/chengdu_china.osm.pbf" --write-apidb host="localhost" database="openstreetmap" user="osm" password="buaanlp" validateSchemaVersion=no</strong>. I have used the lastest osmosis tool and the version of osmosis is 0.45, but the problem still arise, how can i sovle this problem?</p>
<p>If this problem can't be solved, then how can i add .pdf data file into the apidb?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '16, 05:15</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-51995" class="comments-container">
&#10;</div>
<div id="comment-tools-51995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51995-form-container" class="comment-form-container">
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

<span id="52001"></span>

<div id="answer-container-52001" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52001-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yuyy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The key to the answer is in your last sentence: you are adding data to an existing datanase, which already contains an entry for the objects in question.</p>
<p>AFAIK you cannot directly merge into an existing APIDB with osmosis, you can however merge two datasources into one, see <strong>--merge</strong>. With other words you should pre-merge and then import (if you have modified data in your APIDB likely export, merge, re-import).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '16, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-52001" class="comments-container">
<span id="52003"></span>
<div id="comment-52003" class="comment">
<div id="post-52003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok,thanks to your reply, so the osmosis command only can use once when import .pbf data file because the apidb must keep empty, this is so unconvenient and unreasonable.</p>
</div>
<div id="comment-52003-info" class="comment-info">
<span class="comment-age">(12 Sep '16, 12:44)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-52001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52001-form-container" class="comment-form-container">
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

