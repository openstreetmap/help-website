+++
type = "question"
title = "How can I dissolve intersecting polygons with Overpass?"
description = '''I want to create one polygon of these 3: [out:json]; (  area[&quot;name:nl&quot;=&quot;Antwerpen&quot;][&quot;admin_level&quot;=6];  area[&quot;name:nl&quot;=&quot;Limburg&quot;][&quot;admin_level&quot;=6];  area[&quot;name:nl&quot;=&quot;Vlaams-Brabant&quot;][&quot;admin_level&quot;=6]; ) -&amp;gt;.a; rel(area.a)[&quot;admin_level&quot;=6]; out meta; way(r); out geom;  So the ways that are shared sho...'''
date = "2015-05-19T14:44:00Z"
lastmod = "2016-05-03T16:22:00Z"
weight = 43114
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/43114" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I dissolve intersecting polygons with Overpass?](/questions/43114/how-can-i-dissolve-intersecting-polygons-with-overpass)

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
<span id="post-43114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43114-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create one polygon of these 3:</p>
<pre><code>[out:json];
(
  area[&quot;name:nl&quot;=&quot;Antwerpen&quot;][&quot;admin_level&quot;=6];
  area[&quot;name:nl&quot;=&quot;Limburg&quot;][&quot;admin_level&quot;=6];
  area[&quot;name:nl&quot;=&quot;Vlaams-Brabant&quot;][&quot;admin_level&quot;=6];
) -&gt;.a;
rel(area.a)[&quot;admin_level&quot;=6];
out meta;
way(r);
out geom;</code></pre>
<p>So the ways that are shared should be removed so it would be one area. Any way I could do this with Overpass?</p>
<p>Thanks, Frans</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '15, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/251358054457c39262ea6e368e8122d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Frans_&#39;s gravatar image" />
<p><span>_Frans_</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Frans_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43114" class="comments-container">
&#10;</div>
<div id="comment-tools-43114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43114-form-container" class="comment-form-container">
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

<span id="43115"></span>

<div id="answer-container-43115" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43115-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-43115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="_Frans_ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API can't to this for you, but you could run the following Overpass API query in QGIS via QuickOSM plugin and merge the resulting polygons according to the description below.</p>
<pre><code>[out:json];
(
  area[&quot;name:nl&quot;=&quot;Antwerpen&quot;][&quot;admin_level&quot;=6];
  area[&quot;name:nl&quot;=&quot;Limburg&quot;][&quot;admin_level&quot;=6];
  area[&quot;name:nl&quot;=&quot;Vlaams-Brabant&quot;][&quot;admin_level&quot;=6];
) -&gt;.a;
(rel(area.a)[&quot;admin_level&quot;=6];&gt;;);out meta;</code></pre>
<p>To merge intersecting polygons in QGIS, first select all polygons, then choose "Vector-&gt;Geoprocessing Tools-&gt;Dissolve" and dissolve by field "osm_type". Save the result in a new shape file and the result to your map. A new layer with a new multilinestring should appear like in the screenshot below.</p>
<p>Please see <a href="http://gis.stackexchange.com/questions/65256/qgis-merge-intersecting-polygons-into-one-which-are-part-of-the-same-feature">the following link for details</a>. Here's how the result could look like with a bit of shapeburst styling:</p>
<p><img src="/upfiles/res2.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '15, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 May '15, 20:48</strong> </span></p>
</div>
</div>
<div id="comments-container-43115" class="comments-container">
<span id="43148"></span>
<div id="comment-43148" class="comment">
<div id="post-43148-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, this solved my problem!</p>
</div>
<div id="comment-43148-info" class="comment-info">
<span class="comment-age">(21 May '15, 13:58)</span> <span class="comment-user userinfo">_Frans_</span>
</div>
</div>
<span id="49559"></span>
<div id="comment-49559" class="comment">
<div id="post-49559-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for answer, this helped me very much.</p>
</div>
<div id="comment-49559-info" class="comment-info">
<span class="comment-age">(03 May '16, 16:22)</span> <span class="comment-user userinfo">Chriss85</span>
</div>
</div>
</div>
<div id="comment-tools-43115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43115-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43178"></span>

<div id="answer-container-43178" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43178-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try the webservice from OSM user Wambacher:</p>
<p><a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a></p>
<p>and try the "Union" feature at the bottom of the screen after selecting some boundary elements from the tree structure on the left. Then try to export in the format you need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '15, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '17, 08:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-43178" class="comments-container">
&#10;</div>
<div id="comment-tools-43178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43178-form-container" class="comment-form-container">
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

