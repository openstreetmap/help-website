+++
type = "question"
title = "Exchanging TileMill (Mapnik) datasource: static data / PostGIS"
description = '''I have the following use case: A graphic designer is assigned to design a map style. This style should later be deployed on a PostGIS (osm2pgsql) / Mapnik / Tirex based tile server stack. So far I found TileMill to be a great tool for designing the map. While on the production server, the OSM data w...'''
date = "2013-03-26T20:55:00Z"
lastmod = "2013-03-27T17:32:00Z"
weight = 21010
keywords = [ "shp", "tilemill", "design", "mapnik", "postgis" ]
aliases = [ "/questions/21010" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Exchanging TileMill (Mapnik) datasource: static data / PostGIS](/questions/21010/exchanging-tilemill-mapnik-datasource-static-data-postgis)

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
<span id="post-21010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21010-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the following use case:</p>
<p>A graphic designer is assigned to design a map style. This style should later be deployed on a PostGIS (osm2pgsql) / Mapnik / Tirex based tile server stack.</p>
<p>So far I found TileMill to be a great tool for designing the map.</p>
<p>While on the production server, the OSM data would be served from PostGIS, on the designers computer I want to avoid the PostGIS setup. I even want to avoid to run the PostGIS server before the design is finished.</p>
<p><strong>Is it possible to design a map using TileMill on base of a simple OSM export (SHP File?) and to directly use the same style on a PostGIS based server?</strong></p>
<p>I guess I could change all the data source settings in the tilemill definition by hand - but the process should be as automatic as possible so the design could be continuously improved and applied again.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shp" rel="tag" title="see questions tagged &#39;shp&#39;">shp</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-design" rel="tag" title="see questions tagged &#39;design&#39;">design</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '13, 20:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Mar '13, 21:01</strong> </span></p>
</div>
</div>
<div id="comments-container-21010" class="comments-container">
&#10;</div>
<div id="comment-tools-21010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21010-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="21012"></span>

<div id="answer-container-21012" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21012-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could potentially do an osm2pgsql or imposm import, then export all tables into shape files, and let the designer work on those; that could then be changed by a simple script if you go into production. However shapefile sources are less flexible than database sources; you cannot do WHERE clauses or ORDER BY (for example, when drawing city labels you might want to draw those with larger population first). The lack of WHERE clauses can be compensated by filter rules but that will lead to a less efficient style.</p>
<p>Having direct access to a database (through a port forward if necessary) will make things more complex during design but will also give a more efficient result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '13, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21012" class="comments-container">
<span id="21029"></span>
<div id="comment-21029" class="comment">
<div id="post-21029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, it's an answer to the question, and pretty much what I would have said too.</p>
</div>
<div id="comment-21029-info" class="comment-info">
<span class="comment-age">(27 Mar '13, 17:09)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="21030"></span>
<div id="comment-21030" class="comment">
<div id="post-21030-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not really familiar with this, so perhaps it is a silly comment. But would potentially using a sqlite db work on the designers computer? Hopefully that would be much easier to set up than the full postgis / postgresql and gives similar functionality.</p>
<p>Otherwise, yes, I'd agree, giving the designer access to a remote postgis db over the network (or via a VM) probably seems like the most appropriate solution in this situation</p>
</div>
<div id="comment-21030-info" class="comment-info">
<span class="comment-age">(27 Mar '13, 17:32)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-21012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21012-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21011"></span>

<div id="answer-container-21011" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21011-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>self-answer - but I hope for simpler ones:</em></p>
<p>One pragmatic solution would be to provide the designer with a PostGIS installation, for example in a Virtual machine to do the designing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '13, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21011" class="comments-container">
&#10;</div>
<div id="comment-tools-21011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21011-form-container" class="comment-form-container">
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

