+++
type = "question"
title = "merging street segments of the same name as one"
description = '''Hi here, Thank you always. Your responses on this platform have been of an immeasurable value to me. In my python project, I want to combine street segments having the same name as one. Merging them is not a problem for me, but how do I do it such that the nodes of each street segment is combined wi...'''
date = "2022-09-01T21:38:00Z"
lastmod = "2022-09-02T20:28:00Z"
weight = 85523
keywords = [ "merge", "segements", "street" ]
aliases = [ "/questions/85523" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [merging street segments of the same name as one](/questions/85523/merging-street-segments-of-the-same-name-as-one)

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
<span id="post-85523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85523-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi here, Thank you always. Your responses on this platform have been of an immeasurable value to me. In my python project, I want to combine street segments having the same name as one. Merging them is not a problem for me, but how do I do it such that the nodes of each street segment is combined with others, and such that they are arranged in an orderly pattern, to form a single straight street?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-segements" rel="tag" title="see questions tagged &#39;segements&#39;">segements</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '22, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '22, 21:39</strong> </span></p>
</div>
</div>
<div id="comments-container-85523" class="comments-container">
<span id="85526"></span>
<div id="comment-85526" class="comment">
<div id="post-85526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What editor are you using?</p>
</div>
<div id="comment-85526-info" class="comment-info">
<span class="comment-age">(02 Sep '22, 07:26)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
<span id="85527"></span>
<div id="comment-85527" class="comment">
<div id="post-85527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this for a downstream application? Do you want to upload the result to OSM?</p>
</div>
<div id="comment-85527-info" class="comment-info">
<span class="comment-age">(02 Sep '22, 07:53)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="85530"></span>
<div id="comment-85530" class="comment">
<div id="post-85530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is like a student project on extracting streets within a specified region in OSM and identifying points of intersection . So let's say street "Rue" starts from A and runs through point B to C, and another street "Avenue" starts from X through point B to Y. Then what I want to achieve in my python code now is having on Rue, the street segments AB and BC merged together as one street still under the name Rue, then also street segments for Avenue is merged as one (XB +BY) , with both Rue and Avenue intersecting at B. I'm also particular about the order of street segments merging so that the combined nodes are so arranged as they are in reality on the OSM map.</p>
</div>
<div id="comment-85530-info" class="comment-info">
<span class="comment-age">(02 Sep '22, 10:12)</span> <span class="comment-user userinfo">Segunlakata</span>
</div>
</div>
<span id="85531"></span>
<div id="comment-85531" class="comment">
<div id="post-85531-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How are you <strong>merging</strong>?<br />
<a href="https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.unary_union.html#geopandas.GeoSeries.unary_union">unary_union</a>? <a href="https://geopandas.org/en/stable/docs/user_guide/aggregation_with_dissolve.html">dissolve</a>?</p>
<p>Have you asked on <a href="https://gis.stackexchange.com/">GIS Stackexchange</a>?<br />
If you do; don't forget a code-snippet and leave a trail-of-breadcrumbs (a link) please.</p>
</div>
<div id="comment-85531-info" class="comment-info">
<span class="comment-age">(02 Sep '22, 20:28)</span> <span class="comment-user userinfo">arkriger</span>
</div>
</div>
</div>
<div id="comment-tools-85523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

