+++
type = "question"
title = "instalation tile server OSM on ubuntu 14.04"
description = '''hai all, i am a beginner, i try to follow step by step from https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/ , to build a tile server but in step &quot;Run the pre-processor and then carto: &quot; ... ./make.py cd ../OSMBright/ carto project.mml &amp;gt; OSMBright.xml i am not yet under...'''
date = "2015-06-28T20:18:00Z"
lastmod = "2015-07-25T07:58:00Z"
weight = 43829
keywords = [ "ubuntu", "osm", "tileserver" ]
aliases = [ "/questions/43829" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [instalation tile server OSM on ubuntu 14.04](/questions/43829/instalation-tile-server-osm-on-ubuntu-1404)

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
<span id="post-43829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43829-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hai all, i am a beginner,</p>
<p>i try to follow step by step from <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> , to build a tile server</p>
<p>but in step "Run the pre-processor and then carto: " ...</p>
<p>./make.py cd ../OSMBright/ carto project.mml &gt; OSMBright.xml</p>
<p>i am not yet understand about how to build "OSMBright" folder,where i have to start with? please help, thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '15, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f3b7015e787942201843bb38d2f89cc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grenfajr&#39;s gravatar image" />
<p><span>grenfajr</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grenfajr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43829" class="comments-container">
&#10;</div>
<div id="comment-tools-43829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43829-form-container" class="comment-form-container">
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

<span id="44418"></span>

<div id="answer-container-44418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44418-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. I am a beginner too and I am working on the same. I have problems in next stages but this ran pretty smoothly for me. Its specified there in the tutorial itself. When you change the path and dbname in configure.py file of osm-bright-master and build it by ./make.py, a folder OSMBright gets generated. cd.. goes back a folder and there you will have OSMBright folder. To convert the project.mml file in that folder to xml you gotta give the command - carto project.mml &gt; OSMBright.xml</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '15, 07:58</strong></p>
<img src="https://secure.gravatar.com/avatar/8dd67b802a9670a2c48a10ef79d718b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmnw15&#39;s gravatar image" />
<p><span>dmnw15</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmnw15 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44418" class="comments-container">
&#10;</div>
<div id="comment-tools-44418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44418-form-container" class="comment-form-container">
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

