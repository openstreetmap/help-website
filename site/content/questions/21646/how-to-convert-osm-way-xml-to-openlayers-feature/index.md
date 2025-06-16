+++
type = "question"
title = "How to convert osm way xml to openlayers feature?"
description = '''I am displaying the osm data through a popup with openlayers. For now i am using the overpass api to get data.  But my app needs to reflect the rapidly changing data i.e. one changes the data then uses my app, then they need to see the new data. The one minute lag of overpass api is not acceptable, ...'''
date = "2013-04-18T12:57:00Z"
lastmod = "2013-04-18T12:57:00Z"
weight = 21646
keywords = [ "xml", "overpass", "vector", "openlayers" ]
aliases = [ "/questions/21646" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert osm way xml to openlayers feature?](/questions/21646/how-to-convert-osm-way-xml-to-openlayers-feature)

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
<span id="post-21646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21646-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am displaying the osm data through a popup with openlayers. For now i am using the overpass api to get data.</p>
<p>But my app needs to reflect the rapidly changing data i.e. one changes the data then uses my app, then they need to see the new data.</p>
<p>The one minute lag of overpass api is not acceptable, so i have decided to use the</p>
<ol>
<li>skel mode of overpass api to display feature,</li>
<li>Get id and geometry</li>
<li>query the feature from osm database</li>
</ol>
<p>this way i can limit the data usage also.</p>
<p>Now i have an Openlayers Vector Layer using OpenLayers.Format.OSM. i can add features to it.</p>
<p>i need to convert an xml data in <a href="https://www.openstreetmap.org/api/0.6/way/191189605">this format</a> to an OpenLayers.Feature.Vector.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '13, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-21646" class="comments-container">
&#10;</div>
<div id="comment-tools-21646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21646-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

