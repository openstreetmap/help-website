+++
type = "question"
title = "Displaying and selecting neighborhood areas on the map"
description = '''I would like to add defined neighborhood lines (highlighted) on the open source map on my website. These lines will travel mostly along roads but will also travel along a few rivers. They need to be highlighted as the road name will still need to be read under the line. There are a six spots that th...'''
date = "2014-02-26T20:43:00Z"
lastmod = "2014-02-26T21:27:00Z"
weight = 31062
keywords = [ "selectable", "area" ]
aliases = [ "/questions/31062" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Displaying and selecting neighborhood areas on the map](/questions/31062/displaying-and-selecting-neighborhood-areas-on-the-map)

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
<span id="post-31062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31062-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to add defined neighborhood lines (highlighted) on the open source map on my website. These lines will travel mostly along roads but will also travel along a few rivers. They need to be highlighted as the road name will still need to be read under the line. There are a six spots that the line must travel in a straight line that is not associated with a river or road. I am looking at dividing the city up into 90+- neighborhoods I am a realtor and I want buyers to click on the areas (neighborhoods) they are interested in buying a home. When they click on the defined neighborhood, it will be highlighted. They can be clicked on or off. In turn, the areas they click on will be auto populated into a form below. The form below will also have questions such as price range of the home, # beds, #baths, style of home etc.</p>
<p>The website user will hit submit and the completed form (including the neighbourhoods chosen) will be e mailed to me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-selectable" rel="tag" title="see questions tagged &#39;selectable&#39;">selectable</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '14, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/238c504f907d87f1198d64c1306baf2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Realtorsteve&#39;s gravatar image" />
<p><span>Realtorsteve</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Realtorsteve has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '14, 21:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-31062" class="comments-container">
&#10;</div>
<div id="comment-tools-31062" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31062-form-container" class="comment-form-container">
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

<span id="31063"></span>

<div id="answer-container-31063" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31063-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many different ways to solve this. One typical way would be storing the different neighborhood lines in a separate file, like a KML or GeoJSON file, and then overlay that onto an OpenStreetMap base map with OpenLayers. For that, you would require</p>
<ul>
<li>someone to actually record the neighborhood areas and store them in a suitable file</li>
<li>someone to code the bits for your web frontend that display these areas, and react to mouse clicks by copying an area name into the form</li>
<li>an OpenStreetMap tile server to load the basemap tiles for your web map from</li>
</ul>
<p>The first two bullet points can be done by yourself if you have sufficient GIS/programming skills, or you could hire a professional. The third bullet point can be had for free if your tile usage is small-scale (use OSM tile server) or you could use the free MapQuest tiles; but you can also buy tile serving commercially.</p>
<p>If you are looking for professional support see <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">"Commercial OSM Software and Services"</a> on the Wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '14, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31063" class="comments-container">
&#10;</div>
<div id="comment-tools-31063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31063-form-container" class="comment-form-container">
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

