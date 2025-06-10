+++
type = "question"
title = "How to get number of Lane from OSM?"
description = '''Hello, I am using OSM for my project, I have downloaded data from http://download.geofabrik.de/ in the OSM file and imported the data in POSTGIS, In the planet_osm_roads, I am not able to see any key realted to lanes. Can you please help me get the information about the number of lanes from OSM?'''
date = "2019-05-15T18:54:00Z"
lastmod = "2019-05-15T21:07:00Z"
weight = 69198
keywords = [ "osm", "osm2pgsql", "postgis" ]
aliases = [ "/questions/69198" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get number of Lane from OSM?](/questions/69198/how-to-get-number-of-lane-from-osm)

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
<span id="post-69198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am using OSM for my project, I have downloaded data from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> in the OSM file and imported the data in POSTGIS, In the planet_osm_roads, I am not able to see any key realted to lanes.</p>
<p>Can you please help me get the information about the number of lanes from OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '19, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/aed8449bff24f11ecd4dc2062f00d060?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gautamshahi&#39;s gravatar image" />
<p><span>gautamshahi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gautamshahi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69198" class="comments-container">
&#10;</div>
<div id="comment-tools-69198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69198-form-container" class="comment-form-container">
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

<span id="69201"></span>

<div id="answer-container-69201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69201-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>By default osm2pgsql will not create a "lanes" column. You can either provide a modified .style file that contains the "lanes" attribute when running osm2pgsl (with the <code>-S</code> option), or you can run osm2pgsql with the <code>--hstore</code> option which will result in a "tags" column that has <em>all</em> tags that don't have extra columns to themselves. You will then be able to access the lanes tag with the syntax <code>tags-&gt;'lanes'</code> in your SQL query.</p>
<p>Of course, less than 10% of all <code>highway</code> objects in OSM have a lane tag so you won't find it everywhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '19, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69201" class="comments-container">
&#10;</div>
<div id="comment-tools-69201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69201-form-container" class="comment-form-container">
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

