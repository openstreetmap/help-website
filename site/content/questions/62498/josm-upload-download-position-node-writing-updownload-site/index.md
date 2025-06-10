+++
type = "question"
title = "JOSM upload download, position node, writing up/download site."
description = '''Situation, the problem: When I have a shape file, open in a layer (JOSM), copy/paste a polygon line to the .osm layer. Upload to OSM. Then a new layer, download the data in this area, then compare to just uploaded polygon in the shape file layer, then I see that a node is on a slightly different pos...'''
date = "2018-03-02T19:07:00Z"
lastmod = "2018-03-03T12:46:00Z"
weight = 62498
keywords = [ "download", "josm", "upload", "coordinates" ]
aliases = [ "/questions/62498" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM upload download, position node, writing up/download site.](/questions/62498/josm-upload-download-position-node-writing-updownload-site)

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
<span id="post-62498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Situation, the problem: When I have a shape file, open in a layer (JOSM), copy/paste a polygon line to the .osm layer. Upload to OSM.</p>
<p>Then a new layer, download the data in this area, then compare to just uploaded polygon in the shape file layer, then I see that a node is on a slightly different position. Now copy/paste the abutting polygon, I do not have a validation warning, that both nodes are on the same place, and could connect(double node) them with "fix" button. Before upload. If this is not possible it give a lot of handwork by merging nodes.</p>
<p>It have to do with the other lat/lon coordination numbers after download from OSM.</p>
<p>From this shapefile, i take out a few polygons I want copy into a new layer, this layer is the layer I want to merge with osmlayer, nodes have a slightly different coordination numbers "ready to use before layer".osm</p>
<p>Now to the question: I want to upload this "ready to use before layer".osm to a site and get back a file "ready for osm.osm" with <strong>the right coordinates</strong>, so that after JOSM upload, there is <strong>no</strong> slightly change of the node anymore.</p>
<p>Then it is possible the next day to take a other set of polygons, that is directly on it's place. And can I use the fix validation button to connect these nodes. And then upload to OSM.</p>
<p>Is this possible?</p>
<p>Is there such site?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '18, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-62498" class="comments-container">
<span id="62504"></span>
<div id="comment-62504" class="comment">
<div id="post-62504-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to provide an example pair of coordinates before and after, without that a response is just guessing (for example the differences could simply due to rounding).</p>
<p>Note: if you are importing data, you need to follow <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">https://wiki.openstreetmap.org/wiki/Import/Guidelines</a> which will typically include a technical discussion of the data and how it best should be transformed for use in OSM.</p>
</div>
<div id="comment-62504-info" class="comment-info">
<span class="comment-age">(03 Mar '18, 10:14)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="62506"></span>
<div id="comment-62506" class="comment">
<div id="post-62506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am fully aware of the import guidelines. That is why, I search for solutions to make a import easier and so that others with same data can work connectively.(later)</p>
<p>&lt; (for example the differences could simply due to rounding).&gt; That is exactly the point. In JOSM, new polygon (import, basedata), node, it have a number, after upload to OSM and download again it is a rounded number. Before I make a upload, I want to make this node number a rounded number, the same as I get back from a OSM download.</p>
<p>I need a tool to get the rounded OSM numbers correctly.</p>
<p>I believe when you have a node number lat/lon, and you should upload it in OSM a 1000 times, you get the same rounded number back again and again from download. Is this true?</p>
<p>Maybe there should be a option in JOSM, to set a layer (importdata) to a "before importlayer".osm with the right rounded numbers that never gonna change in OSM.</p>
<p>I was looking/asking if there is such tool. (srcipt)?</p>
<p>So we can make files with the best starting point.</p>
</div>
<div id="comment-62506-info" class="comment-info">
<span class="comment-age">(03 Mar '18, 12:18)</span> <span class="comment-user userinfo">Allroads</span>
</div>
</div>
</div>
<div id="comment-tools-62498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62498-form-container" class="comment-form-container">
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

<span id="62507"></span>

<div id="answer-container-62507" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62507-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Internally in the OSM database coordinates are represented by signed 32bit integers, see <a href="https://wiki.openstreetmap.org/wiki/Node#Structure">https://wiki.openstreetmap.org/wiki/Node#Structure</a> for a discussion of how this works.</p>
<p>To round a coordinate value in a third party source so that it should pass through the API unchanged, you would need to apply the same rules (note this fraught with a number things that could go wrong depending largely on all the intermediate steps doing things the same way). So you need to either add a plugin to JOSM that does this or preprocess the shapefiles before importing them to JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '18, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62507" class="comments-container">
&#10;</div>
<div id="comment-tools-62507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62507-form-container" class="comment-form-container">
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

