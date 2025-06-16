+++
type = "question"
title = "How can I create an OSM Relation Area if it doesn&#x27;t exist?"
description = '''I&#x27;m working on a project where I need to collect the streets within cities (for various definitions of &#x27;city&#x27;). I&#x27;m running into trouble when a city does not have an OSM Relation ID (I understand this as it does not have its Administrative Boundary mapped out, but I might be misunderstanding this as...'''
date = "2014-02-15T23:15:00Z"
lastmod = "2014-03-30T02:22:00Z"
weight = 30758
keywords = [ "osm", "editing", "admin_boundary", "relations", "city" ]
aliases = [ "/questions/30758" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I create an OSM Relation Area if it doesn't exist?](/questions/30758/how-can-i-create-an-osm-relation-area-if-it-doesnt-exist)

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
<span id="post-30758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30758-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on a project where I need to collect the streets within cities (for various definitions of 'city'). I'm running into trouble when a city does not have an OSM Relation ID (I understand this as it does not have its Administrative Boundary mapped out, but I might be misunderstanding this as well).</p>
<p>For example, <a href="http://nominatim.openstreetmap.org/details.php?place_id=97822449">Holyoke</a> has its area mapped out so it has an OSM Relation ID ... whereas <a href="http://nominatim.openstreetmap.org/details.php?place_id=497336">Tolland</a> does not have its area mapped out yet. For cities without the OSM Relation ID, I've been using <a href="http://extract.bbbike.org/">http://extract.bbbike.org/</a> to trace the city's border by hand, and then export that traced region to OSM file.</p>
<p>That works well enough, but if I knew how to actually create the Relation IDs for city areas I could be helpful to OpenStreetMap while working through my project. I could generate the OSM Relation IDs by tracing the city's Administrative Boundary - I'm doing the tracing anyway ... it might as well be put to use.</p>
<p>Can someone either point me to articles/videos that explain this, or explain how to edit OpenStreetMap (with iD, presumably) to add this data?</p>
<p>It seems like I should 'Edit with iD', click the 'Area' button, map out the city's border to create a closed area (going with the assumption that it is a simple city border, not something like <a href="http://nominatim.openstreetmap.org/details.php?place_id=97418351">Austin</a>), and then ... ??? ... Do I set the feature type to 'Area', name it whatever the city's name is, and do something else to associate it with the actual city? When I navigate around a city that has an OSM Relation ID, I see that it is surrounded by an 'Administrative Boundary' feature type. It doesn't seem like I can create those, though.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '14, 23:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-30758" class="comments-container">
<span id="30759"></span>
<div id="comment-30759" class="comment">
<div id="post-30759-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A boundary is typically not mapped as an area, but as a relation. The relation contains a collection of (OSM) ways (not highways, roads) that form the boundary. Those ways can be shared with neighboring cities, counties, etc. I created quite a few boundaries, but used JOSM, so I cannot help you on describing how it should be done in iD. I read a few statements about iD not really supporting relations, but maybe that has changed recently.</p>
</div>
<div id="comment-30759-info" class="comment-info">
<span class="comment-age">(16 Feb '14, 06:45)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="30766"></span>
<div id="comment-30766" class="comment">
<div id="post-30766-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not particularly tied to iD - if you have the time to share your process with JOSM, I'm sure you'd be helping out a lot of would-be mappers.</p>
</div>
<div id="comment-30766-info" class="comment-info">
<span class="comment-age">(16 Feb '14, 14:31)</span> <span class="comment-user userinfo">JamesChevalier</span>
</div>
</div>
<span id="30842"></span>
<div id="comment-30842" class="comment">
<div id="post-30842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I manually create the boundary relation and set e.g. the attributes, name=xxx; type=boundary; boundary=administrative ; admin_level=9 The members of the relations are way with attributes boundary=administrative; admin_level=9 Note that is is also possible to have admin_level=8 here, it's typically the highest level that wins. All the ways get role outer. see e.g. <a href="https://www.openstreetmap.org/relation/3402541#map=13/51.0137/3.6307">https://www.openstreetmap.org/relation/3402541#map=13/51.0137/3.6307</a></p>
<p>We use add a node with role admin_centre, other communities use the role label</p>
</div>
<div id="comment-30842-info" class="comment-info">
<span class="comment-age">(19 Feb '14, 16:22)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-30758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30758-form-container" class="comment-form-container">
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

<span id="31990"></span>

<div id="answer-container-31990" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31990-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is probably, "Don't edit or create a boundary relation as a beginner." That's not very encouraging though. That short answer is also at odds with the over-arching OpenStreetMap theme that "anybody can improve the map." True enough.<br />
</p>
<p>A boundary relation can be a rather complex object in OpenStreetMap terms. I can't recommend that you struggle with creating that complex object, while simultaneously struggling with a new editor. I don't know of a boundary relation tutorial. But let's try to point you in the right direction.<br />
</p>
<p>Here is a <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">wiki page on multipolygon relations</a>. A boundary relation is a type of multipolygon relation. I wouldn't dive into a complex multipolygon as a first step.<br />
</p>
<p>This is a tutorial on creating a simpler multipolygon relation, for a <a href="http://weait.com/courtyard">building with a courtyard</a>. The courtyard tutorial creates a very simple multipolygon relation. That probably makes a good first step on relations.<br />
</p>
<p>Ideally, there would be another tutorial or two with increasing complexity. I'm not aware of such tutorials at this time. Perhaps I'll write one and add a link here later.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '14, 02:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-31990" class="comments-container">
&#10;</div>
<div id="comment-tools-31990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31990-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30827"></span>

<div id="answer-container-30827" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've been speaking to some people directly about this, as well, and the predominant suggestion is "don't".</p>
<p>Most suggest that only those with a lot of experience with OSM editing (including creating and editing relations) create Administrative Boundaries. Additionally, there is a possibility that someone will import the town boundaries from some other data source. Administrative boundaries are mostly not visible on the ground, so the best source of this data is typically the government GIS department.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '14, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span> </br></br></p>
</div>
</div>
<div id="comments-container-30827" class="comments-container">
&#10;</div>
<div id="comment-tools-30827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30827-form-container" class="comment-form-container">
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

