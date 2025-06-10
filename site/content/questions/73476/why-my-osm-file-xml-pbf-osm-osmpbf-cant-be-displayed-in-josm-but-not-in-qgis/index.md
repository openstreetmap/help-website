+++
type = "question"
title = "Why my osm file (.xml .pbf, .osm, .osm.pbf) can&#x27;t be displayed in JOSM but not in QGIS?"
description = '''Hi everyone,  I am trying to generate Isochrones from the Open Trip Planner package in R, I have followed all steps from Marcus Yung OTP tutorial, but the answer when I request to the OTP API is: &quot;org.opentripplanner.routing.error.VertexNotFoundException: vertices not found: [from] vertices not foun...'''
date = "2020-03-11T14:56:00Z"
lastmod = "2020-03-11T17:12:00Z"
weight = 73476
keywords = [ "openstreetmap", "qgis", "pbf", "josm", "xml" ]
aliases = [ "/questions/73476" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why my osm file (.xml .pbf, .osm, .osm.pbf) can't be displayed in JOSM but not in QGIS?](/questions/73476/why-my-osm-file-xml-pbf-osm-osmpbf-cant-be-displayed-in-josm-but-not-in-qgis)

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
<span id="post-73476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73476-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I am trying to generate Isochrones from the <a href="https://github.com/marcusyoung/otpr">Open Trip Planner package in R</a>, I have followed all steps from <a href="https://github.com/marcusyoung/otpr#travel-time-isochrones">Marcus Yung OTP tutorial</a>, but the answer when I request to the OTP API is:</p>
<p><em>"org.opentripplanner.routing.error.VertexNotFoundException: vertices not found: [from] vertices not found: [from]"</em></p>
<ul>
<li>I verified that coords were long/lat (as suggest the Young tutorial) and lat/long (as suggest the OTP doc)</li>
</ul>
<p>I suppouse that above error it's caused because my route .pbf is wrong. In other <a href="https://github.com/marcusyoung/otp-tutorial">tutorial of Marcus Young about this same theme</a> the <a href="https://github.com/marcusyoung/otp-tutorial/blob/master/materials/data/greater-manchester-osm.pbf">.pbf route that he uses</a> can be opened and displayed on QGIS and JOSM, instead my .pbf file can be opened but not displayed on QGIS but yes can JOSM. When I opened my .pbf file on QGIS, how it isn't displayed, the geographical coords have very low values i.e: (-0.31, -1,123).</p>
<p>To get my .pbf file I transformed a shapefile to a xml file with ogr2osm, then I converted this xml file to .pbf with osmconverter. I tried too converting xml file to osm.pbf with JOSM, but the results were as I explicited above.</p>
<p>I need this specific routes because I am trying to get Isochrones with OTP and this API use Shortest Path Tree, so if I add a new route that has shortest paths the results could be wrong.</p>
<p>So, my question is:</p>
<p>-<strong>How can I get a .pbf file that I can to display in QGIS and that could works fine in OTP?</strong></p>
<p>and</p>
<p>-<strong>Why my osm file (.xml .pbf, .osm, .osm.pbf) can't be displayed in JOSM but not in QGIS?</strong></p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '20, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/045e09b66b1ea96e44a081f371137789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bryan&#39;s gravatar image" />
<p><span>Bryan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bryan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '20, 15:22</strong> </span></p>
</div>
</div>
<div id="comments-container-73476" class="comments-container">
<span id="73477"></span>
<div id="comment-73477" class="comment">
<div id="post-73477-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Without samples this is going to be rather difficult, with probably trivial.</p>
</div>
<div id="comment-73477-info" class="comment-info">
<span class="comment-age">(11 Mar '20, 17:12)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73476-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

