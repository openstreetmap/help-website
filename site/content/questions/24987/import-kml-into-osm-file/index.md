+++
type = "question"
title = "Import .kml into .osm file"
description = '''I have a pretty big, custom .kml file (it is the property of my company, and I can legally use it), what I want to import into an .osm file, downloaded from here: download.geofabrik.de. I can open this .osm map in softwares, for completely offline usage, such as Marble. My question is: can I somehow...'''
date = "2013-08-06T14:49:00Z"
lastmod = "2013-08-07T11:59:00Z"
weight = 24987
keywords = [ "openstreetmap", "merge", "kml", "osm" ]
aliases = [ "/questions/24987" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import .kml into .osm file](/questions/24987/import-kml-into-osm-file)

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
<span id="post-24987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24987-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a pretty big, custom .kml file (it is the property of my company, and I can legally use it), what I want to import into an .osm file, downloaded from here: <a href="http://download.geofabrik.de/">download.geofabrik.de</a>. I can open this .osm map in softwares, for completely offline usage, such as Marble.</p>
<p>My question is: can I somehow merge this kml and osm file, so when I open the merged file in Marble, the routes described by the kml are also visible? So basically, I want to merge a.kml with b.osm, resulting in c.osm, what I can use offline.</p>
<p>Is it possible? If yes, can you direct me in the right direction?</p>
<p>Any help is appreciated, thanks!</p>
<p>EDIT: with "custom .kml" I meant standard kml file format, and it contains routes only, no idea why I wrote that :)</p>
<p>EDIT2: I have tried GPSBabel, it indicates that it can convert .kml to .osm. It generates a 65MB .osm file from my 12MB .kml, but when I open it in Marble, it does not show any routes, so it looks like a dead end. :/</p>
<p>EDIT3: Well, GPSBabel produced an input what QGIS could open. I merged the two .osm file with osmosis, but the problem is, the output is invalid, nothing can open it. Any idea?</p>
<p>EDIT4: I guess this will be the last edit, sort of a "bump", since I'm still stuck on the issue, and maybe someone will notice, who has a solution, which I would be very happy to hear. :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '13, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/f67d6264f52e07ad3b93596873c5af9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hundeva&#39;s gravatar image" />
<p><span>hundeva</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hundeva has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '13, 13:49</strong> </span></p>
</div>
</div>
<div id="comments-container-24987" class="comments-container">
<span id="24989"></span>
<div id="comment-24989" class="comment">
<div id="post-24989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I just discovered, ogr2ogr can read OSM files but apparently not write them. So it seems not to be possible using ogr2ogr.</p>
</div>
<div id="comment-24989-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 15:24)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-24987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24987-form-container" class="comment-form-container">
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

<span id="25024"></span>

<div id="answer-container-25024" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25024-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can open KML and OSM files using <a href="http://www.qgis.org/">QGIS</a>.</p>
<p>Here is a <a href="http://maps.cga.harvard.edu/qgis/wkshop/import_kml.php">basic tutorial</a> on importing KML files into QGIS.</p>
<p>Here is a <a href="https://wiki.openstreetmap.org/wiki/QGIS">wiki page</a> and <a href="https://wiki.openstreetmap.org/wiki/QGIS_OSM_Plugin">another wiki page</a> on using OSM data in QGIS.</p>
<p>You will probably then be able to save the various files into formats that can be manipulated by other software if needed. Alternatively, you may be able to meet your needs using QGIS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Aug '13, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/e466cf295ae880686a4b809362f931b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rovingmedic&#39;s gravatar image" />
<p><span>rovingmedic</span><br />
<span class="score" title="1060 reputation points"><span>1.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rovingmedic has one accepted answer">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Aug '13, 08:06</strong> </span></p>
</div>
</div>
<div id="comments-container-25024" class="comments-container">
<span id="25025"></span>
<div id="comment-25025" class="comment">
<div id="post-25025-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, I will take a look at this!</p>
</div>
<div id="comment-25025-info" class="comment-info">
<span class="comment-age">(07 Aug '13, 08:24)</span> <span class="comment-user userinfo">hundeva</span>
</div>
</div>
<span id="25032"></span>
<div id="comment-25032" class="comment">
<div id="post-25032-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unfortunately, this does not seem to work. After opening the kml, and trying to save as osm, I get the following error: "No OSM data are loaded/downloaded or no OSM layer is selected in Layers panel. Please change this situation first, because OSM Plugin doesn't know what to save." The layers are selected, so it does not seem to recognize it.</p>
</div>
<div id="comment-25032-info" class="comment-info">
<span class="comment-age">(07 Aug '13, 11:59)</span> <span class="comment-user userinfo">hundeva</span>
</div>
</div>
</div>
<div id="comment-tools-25024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25024-form-container" class="comment-form-container">
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

