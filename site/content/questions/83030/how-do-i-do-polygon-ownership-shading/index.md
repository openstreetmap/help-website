+++
type = "question"
title = "How do I do polygon ownership shading?"
description = '''I&#x27;d like to upload ownership polygons. E.g. parks, conservation areas and distinguish the different agencies with color shading. I have shp files for the areas which I pulled from the county tax parcel data.  Is this possible without manually tracing the outlines?  example: '''
date = "2022-01-10T02:53:00Z"
lastmod = "2022-01-11T03:55:00Z"
weight = 83030
keywords = [ "shapefiles", "polygons", "ownership" ]
aliases = [ "/questions/83030" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I do polygon ownership shading?](/questions/83030/how-do-i-do-polygon-ownership-shading)

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
<span id="post-83030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83030-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to upload ownership polygons. E.g. parks, conservation areas and distinguish the different agencies with color shading. I have shp files for the areas which I pulled from the county tax parcel data.</p>
<p>Is this possible without manually tracing the outlines?</p>
<p>example:</p>
<p><img src="http://www.interisland.net/watershed/mike/Trails/2022-01-08%20-002308.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefiles" rel="tag" title="see questions tagged &#39;shapefiles&#39;">shapefiles</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-ownership" rel="tag" title="see questions tagged &#39;ownership&#39;">ownership</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '22, 02:53</strong></p>
<img src="https://secure.gravatar.com/avatar/74a43781cd2c13bbb2dd6a8c0e12b79f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PacNWMike&#39;s gravatar image" />
<p><span>PacNWMike</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PacNWMike has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-83030" class="comments-container">
&#10;</div>
<div id="comment-tools-83030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83030-form-container" class="comment-form-container">
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

<span id="83031"></span>

<div id="answer-container-83031" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83031-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a number of issues with your request.</p>
<ol>
<li>In general, OSM is not interested in ownership or parcel data, especially when this information is not visible on the ground. (If there's a fence with a sign "XYZ property" then that's a different matter.) OSM might, however, be interested in areas that have a certain protection status or other characteristics that we do record.</li>
<li>If such data is retrieved from a third-party source, the license situation must be checked. Probably not an issue in the US but best be safe, ensure that the source doesn't claim a copyright on the data.</li>
<li>Simply uploading polygons leads to low-quality data, where the boundaries of neighboring areas (say, a state park and an Indian Reservation) overlap or leave little gaps when in reality one starts exactly where the other ends. Or, a state park ends exactly at the river, but because the river was traced from imagery and the state park imported, they don't line up or overlap in OSM. In the worst case, you'd be uploading an object that already exists in some form and you'd duplicate that. You would be expected to fix all these issues before uploading.</li>
<li>Even if the data <em>were</em> in OSM, you wouldn't get to color-code it in OSM; you'd have to run your own renderer to define which kinds of areas to use which color for. And if you do (run your own renderer) then you might not have to get the data into OSM in the first place, you could just configure your renderer to read it from a shape file on disk. (Another option of drawing stuff on top of OSM, including ready-made third-party GeoJSON files, is the "umap" service on umap.openstreetmap.fr.)</li>
</ol>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a> for more on importing third-party data to OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '22, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '22, 09:12</strong> </span></p>
</div>
</div>
<div id="comments-container-83031" class="comments-container">
<span id="83050"></span>
<div id="comment-83050" class="comment">
<div id="post-83050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the response. It's all public domain so there shouldn't be any copyright issues. Very little of the public land has been added in our county. Exceptions being the State parks and National Park (example above). I would like to add several different ownerships. There are many. National Monument, National Wilderness, National Wildlife Refuge, BLM, State Natural Resources, Nature Conservancy, County Land Bank, Preservation Trust, etc. Quite a mish-mash. I could call them all PARKS but they would all show green and many share a common boundary. I can create the boundaries from GPX tracks derived from the tax parcel data and copy the area.</p>
<p>However I have all of the shp files from the various agencies which I thought would be easier. Not only the boundaries but also the roads and trails too.</p>
</div>
<div id="comment-83050-info" class="comment-info">
<span class="comment-age">(11 Jan '22, 03:55)</span> <span class="comment-user userinfo">PacNWMike</span>
</div>
</div>
</div>
<div id="comment-tools-83031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83031-form-container" class="comment-form-container">
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

