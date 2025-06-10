+++
type = "question"
title = "Error: Missing attribute &#x27;version&#x27; on OSM primitive with ID 16604. (at line 3, column 78)"
description = '''I have a custom road network in shapefile format that contains two columns &quot;source&quot; and &quot;target&quot;. These columns contain an id number referring to the start and end points of the lines. Using ogr2osm I converted this shapefile succesfully to .osm format. In order to make sure that the node id&#x27;s in th...'''
date = "2021-03-02T12:14:00Z"
lastmod = "2021-03-02T14:08:00Z"
weight = 79100
keywords = [ "josm", "nodes", "osm" ]
aliases = [ "/questions/79100" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error: Missing attribute 'version' on OSM primitive with ID 16604. (at line 3, column 78)](/questions/79100/error-missing-attribute-version-on-osm-primitive-with-id-16604-at-line-3-column-78)

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
<span id="post-79100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79100-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a custom road network in shapefile format that contains two columns "source" and "target". These columns contain an id number referring to the start and end points of the lines. Using ogr2osm I converted this shapefile succesfully to .osm format. In order to make sure that the node id's in this .osm file correspond to the id's in the source and target columns from the shapefile, I used a translation.py file to accomplish this. However, opening the file in JOSM returns the following error:</p>
<p><code>Could not read file 'output.osm'. Error is: Missing attribute 'version' on OSM primitive with ID 16604. (at line 3, column 78). 157 bytes have been read</code></p>
<p>Does anyone have an idea how to prevent this from happening so that I can open and inspect the file in JOSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '21, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/152906fc74217eeefa79ad3b652b3380?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="winecity&#39;s gravatar image" />
<p><span>winecity</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="winecity has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '21, 13:17</strong> </span></p>
</div>
</div>
<div id="comments-container-79100" class="comments-container">
<span id="79101"></span>
<div id="comment-79101" class="comment">
<div id="post-79101-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It would help to know where your file came from.</p>
</div>
<div id="comment-79101-info" class="comment-info">
<span class="comment-age">(02 Mar '21, 12:42)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="79102"></span>
<div id="comment-79102" class="comment">
<div id="post-79102-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I updated my question, please have a look</p>
</div>
<div id="comment-79102-info" class="comment-info">
<span class="comment-age">(02 Mar '21, 13:18)</span> <span class="comment-user userinfo">winecity</span>
</div>
</div>
</div>
<div id="comment-tools-79100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79100-form-container" class="comment-form-container">
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

<span id="79103"></span>

<div id="answer-container-79103" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79103-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Any OSM primitive (node, way, relation) needs to have these attributes:</p>
<ul>
<li>id</li>
<li>uid</li>
<li>changeset</li>
<li>version</li>
<li>timestamp</li>
<li>user</li>
</ul>
<p>If all you want is to open the file in JOSM, you can set uid, changeset, version, and user all to "1", and for timestamp you can put "2000-01-01T00:00:00Z". Maybe you can add that to one of the scripts you're massaging the data with anyway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '21, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '21, 14:09</strong> </span></p>
</div>
</div>
<div id="comments-container-79103" class="comments-container">
&#10;</div>
<div id="comment-tools-79103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79103-form-container" class="comment-form-container">
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

