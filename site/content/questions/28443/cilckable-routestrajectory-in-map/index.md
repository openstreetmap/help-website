+++
type = "question"
title = "Cilckable Routes/Trajectory in Map"
description = '''Hi, In my application I am using OSM Map. I am displaying different trajectories/routes in different layer. Now my requirement is like, If I click any of displayed trajectory, it should create a popup to display information regarding that trajectory/route.  Can you suggest different approach to go t...'''
date = "2013-11-25T10:50:00Z"
lastmod = "2013-11-26T12:50:00Z"
weight = 28443
keywords = [ "map", "export", "osm", "web" ]
aliases = [ "/questions/28443" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cilckable Routes/Trajectory in Map](/questions/28443/cilckable-routestrajectory-in-map)

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
<span id="post-28443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28443-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>In my application I am using OSM Map. I am displaying different trajectories/routes in different layer. Now my requirement is like,</p>
<p>If I click any of displayed trajectory, it should create a popup to display information regarding that trajectory/route.</p>
<p>Can you suggest different approach to go through with this requirement?]</p>
<p>I've gone through following link but not succeeded with this.</p>
<p><a href="https://help.openstreetmap.org/questions/9823/how-can-i-select-a-linestring-with-openlayers-selectfeture-at-any-position-of-the-line">https://help.openstreetmap.org/questions/9823/how-can-i-select-a-linestring-with-openlayers-selectfeture-at-any-position-of-the-line</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-web" rel="tag" title="see questions tagged &#39;web&#39;">web</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '13, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/013d1ceebe32a620c4031eed8d9e7236?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nismeh&#39;s gravatar image" />
<p><span>nismeh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nismeh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '13, 12:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-28443" class="comments-container">
<span id="28444"></span>
<div id="comment-28444" class="comment">
<div id="post-28444-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How is "create a popup to display information regarding that trajectory/route" related to OSM? What kind of information do you imagine?</p>
</div>
<div id="comment-28444-info" class="comment-info">
<span class="comment-age">(25 Nov '13, 11:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="28445"></span>
<div id="comment-28445" class="comment">
<div id="post-28445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also have some problems to understand your request.<br />
So you talk about #OpenLayers and popups. But where is the exact problem in your case? <a href="http://wiki.openstreetmap.org/wiki/Openlayers#Examples">http://wiki.openstreetmap.org/wiki/Openlayers#Examples</a></p>
</div>
<div id="comment-28445-info" class="comment-info">
<span class="comment-age">(25 Nov '13, 12:25)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="28448"></span>
<div id="comment-28448" class="comment">
<div id="post-28448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Let me again try to describe my requirement.</p>
<p>I am displaying route of two different coordinates. Now on my map I am with multiple routes for multiple locations. Now if I am clicking on any of the route, it should show me route information in popup window. for an example my route it from location A to location B is shown in map. Now if I am clicking on this route than it should display information like</p>
<p>Route A- B</p>
<p>Distance X miles</p>
<p>Similar feature is available there on Google Earth. If we are with multiple KMLs and that displays us multiple routes. Now if I am clicking on any of them, than it will display a popup providing differen information about selected route.</p>
</div>
<div id="comment-28448-info" class="comment-info">
<span class="comment-age">(25 Nov '13, 12:45)</span> <span class="comment-user userinfo">nismeh</span>
</div>
</div>
<span id="28449"></span>
<div id="comment-28449" class="comment">
<div id="post-28449-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You'd be better off asking this question at the support site of whichever web framework you're using to display the data. You've linked to an OpenLayers question - does that mean you're using OpenLayers? If so, you're probably best off starting here:</p>
<p><a href="http://openlayers.org/dev/examples/">http://openlayers.org/dev/examples/</a></p>
</div>
<div id="comment-28449-info" class="comment-info">
<span class="comment-age">(25 Nov '13, 13:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28443-form-container" class="comment-form-container">
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

<span id="28471"></span>

<div id="answer-container-28471" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28471-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As the other comments, I recommand to you to post your question on specific forum about OpenLayers or Leaflet. For your information, umap may answer your request: <a href="http://umap.openstreetmap.fr/fr/">http://umap.openstreetmap.fr/fr/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '13, 09:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-28471" class="comments-container">
<span id="28473"></span>
<div id="comment-28473" class="comment">
<div id="post-28473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Thank You for your suggestion. I want exact thing as follwing link showing.</p>
<p><a href="http://umap.openstreetmap.fr/en/map/gebiete-mit-fehlenden-adressen-in-chemnitz_828#12/50.8301/12.9299">http://umap.openstreetmap.fr/en/map/gebiete-mit-fehlenden-adressen-in-chemnitz_828#12/50.8301/12.9299</a></p>
<p>Can you suggest me an approach?</p>
</div>
<div id="comment-28473-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 10:46)</span> <span class="comment-user userinfo">nismeh</span>
</div>
</div>
<span id="28481"></span>
<div id="comment-28481" class="comment">
<div id="post-28481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It depends on the source of you trajectories/routes! In umap, you can import your data as gpx/geojson/kml/osm. So you have to save your trajectories/routes in a file (the format will depend on your source and your tool), and then add them in your umap creation.</p>
</div>
<div id="comment-28481-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 12:50)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-28471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28471-form-container" class="comment-form-container">
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

