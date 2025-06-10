+++
type = "question"
title = "Error on Snowonia National Park Polygon"
description = '''When I try to download this polygon I get this error; Error while generating polygon. You could check the geometry through an analyser: analyser using an internal database.  analyser using OSM API (slower).  Message from postgresql server: NOTICE: missing connexion at point -3.9528684f 52.9621599f -...'''
date = "2014-10-19T20:01:00Z"
lastmod = "2014-10-20T15:02:00Z"
weight = 37751
keywords = [ "error" ]
aliases = [ "/questions/37751" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error on Snowonia National Park Polygon](/questions/37751/error-on-snowonia-national-park-polygon)

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
<span id="post-37751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37751-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I try to download this polygon I get this error;</p>
<p>Error while generating polygon. You could check the geometry through an analyser:</p>
<p>analyser using an internal database. analyser using OSM API (slower). Message from postgresql server: NOTICE: missing connexion at point -3.9528684f 52.9621599f - ways: 4685489 NOTICE: missing connexion at point -3.9471549f 52.9622537f - ways: 4685491 NOTICE: missing connexion at point -3.8930782f 53.2573835f - ways: 50894166 208237990 98747616 50894167</p>
<p>I'm new to OSM does anyone know how to fix it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '14, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/e30e97ec03de3795e7d89d3a55e0074b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Malpas%20wanderer&#39;s gravatar image" />
<p><span>Malpas wanderer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Malpas wanderer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37751" class="comments-container">
<span id="37752"></span>
<div id="comment-37752" class="comment">
<div id="post-37752-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What software is it that is giving you the "Error while generating polygon"?</p>
</div>
<div id="comment-37752-info" class="comment-info">
<span class="comment-age">(19 Oct '14, 20:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37751-form-container" class="comment-form-container">
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

<span id="37754"></span>

<div id="answer-container-37754" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37754-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Obviously you're getting these error messages from <a href="http://polygons.openstreetmap.fr/?id=287245">http://polygons.openstreetmap.fr/?id=287245</a> :</p>
<p><img src="http://help.openstreetmap.org/upfiles/fr.png" alt="alt text" /></p>
<p>Strange enough that the analysis tool on this page fails to provide a useful error message: <a href="http://analyser.openstreetmap.fr/cgi-bin/index.py?relation=287245">http://analyser.openstreetmap.fr/cgi-bin/index.py?relation=287245</a></p>
<p>As this is a server maintained by the French OSM community, I'd recommend to create a ticket on the issue tracker <a href="https://trac.openstreetmap.fr/">https://trac.openstreetmap.fr/</a> - However, I'm not quite sure which area is the right one. Maybe you want to check on a French list/forum?</p>
<p>In any case, if you're using this page to download some GeoJSON/etc. format, you might as well consider Overpass Turbo: <a href="http://overpass-turbo.eu/s/5wP">http://overpass-turbo.eu/s/5wP</a> - Just hit the "Run" + "Export" buttons for various output formats.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '14, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '14, 22:10</strong> </span></p>
</div>
</div>
<div id="comments-container-37754" class="comments-container">
<span id="37759"></span>
<div id="comment-37759" class="comment">
<div id="post-37759-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Many thanks for that. After some experimentation exporting as a KML file seems to have been imported to my application satisfactorily.</p>
</div>
<div id="comment-37759-info" class="comment-info">
<span class="comment-age">(20 Oct '14, 00:15)</span> <span class="comment-user userinfo">Malpas wanderer</span>
</div>
</div>
</div>
<div id="comment-tools-37754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37754-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37757"></span>

<div id="answer-container-37757" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37757-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Snowdonia NP relation appears to be fine according to Relation Analyser (see <a href="http://ra.osmsurround.org/analyzeRelation?relationId=287245&amp;_noCache=on).">http://ra.osmsurround.org/analyzeRelation?relationId=287245&amp;_noCache=on).</a></p>
<p>In general its worth checking with <a href="http://tools.geofabrik.de/osmi/?view=multipolygon&amp;lon=-3.81879&amp;lat=52.89141&amp;zoom=9&amp;overlays=ring_not_closed_hull,ring_not_closed,unconnected_end_nodes,role_mismatch_hull,role_mismatch,ways,role_markers,way_end_nodes,way_nodes">OSM Inspector</a> for the state of large polygons &amp; relations before trying to download them. OSM Inspector reports and error but I couldn't find the break in the ring.</p>
<p>If something is broken then it's usually best to badger someone with experience of fixing them rather than trying to get to grips both with multipolygons and finding the tools which are most useful in the situation. Normally I would pull down the relation into JOSM and use JOSM to find and fix the issues.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '14, 23:39</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-37757" class="comments-container">
<span id="37761"></span>
<div id="comment-37761" class="comment">
<div id="post-37761-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The solution in the previous post has seemed to work for me so I'm happy.</p>
<p>many thanks for offering your advice too though.</p>
</div>
<div id="comment-37761-info" class="comment-info">
<span class="comment-age">(20 Oct '14, 00:18)</span> <span class="comment-user userinfo">Malpas wanderer</span>
</div>
</div>
<span id="37772"></span>
<div id="comment-37772" class="comment">
<div id="post-37772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but the ideas of these Q&amp;As is to offer advice which might be helpful to others too.</p>
</div>
<div id="comment-37772-info" class="comment-info">
<span class="comment-age">(20 Oct '14, 15:02)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37757-form-container" class="comment-form-container">
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

