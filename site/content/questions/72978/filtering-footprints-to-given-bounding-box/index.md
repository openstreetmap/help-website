+++
type = "question"
title = "Filtering footprints to given bounding box"
description = '''Hi,  I&#x27;m trying to get footprints with landuse tag within sample bounding box with query below: [out:json][timeout:180]; (  way(poly:&quot;50.859515 18.568600 50.859515 18.580753 50.862946 18.580753 50.862946 18.568600 50.859515 18.568600&quot;)[&quot;landuse&quot;];(._;&amp;gt;;);  relation(poly:&quot;50.859515 18.568600 50.85...'''
date = "2020-02-10T13:19:00Z"
lastmod = "2020-02-11T08:47:00Z"
weight = 72978
keywords = [ "filter", "filtering", "bbox", "bounding-polygon" ]
aliases = [ "/questions/72978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering footprints to given bounding box](/questions/72978/filtering-footprints-to-given-bounding-box)

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
<span id="post-72978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72978-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to get footprints with landuse tag within sample bounding box with query below:</p>
<pre><code>[out:json][timeout:180];
(
  way(poly:&quot;50.859515 18.568600 50.859515 18.580753 50.862946 18.580753 50.862946 18.568600 50.859515 18.568600&quot;)[&quot;landuse&quot;];(._;&gt;;);
  relation(poly:&quot;50.859515 18.568600 50.859515 18.580753 50.862946 18.580753 50.862946 18.568600 50.859515 18.568600&quot;)[&quot;landuse&quot;];(._;&gt;;);
);
out body;</code></pre>
<p>Unfortunately, returned ways are out of my bounding box, as shown on the picture below (bbox is approximately red square) so the question is how to filter results to retrieve data only in my bounding box range?</p>
<p><img src="https://help.openstreetmap.org/upfiles/example1.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '20, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/36ab6acd0d62af564e7cabec38df12da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dnstankiewicz&#39;s gravatar image" />
<p><span>dnstankiewicz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dnstankiewicz has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-72978" class="comments-container">
<span id="72980"></span>
<div id="comment-72980" class="comment">
<div id="post-72980-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Would you actually want area objects that are completely contained in the bounding box only? If you are simply going to do your work within the bounding box, you are supposed to further process this data elsewhere.</p>
</div>
<div id="comment-72980-info" class="comment-info">
<span class="comment-age">(10 Feb '20, 13:35)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="72998"></span>
<div id="comment-72998" class="comment">
<div id="post-72998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I need to do following steps: 1. provide bounding box to my algorithm 2. it downloads data from OSM and filter only landuse in (forest,farmland) 3. union all territory with this tags 4. apply another algorithm to solar panel placement</p>
<p>Any suggestions on how to keep only territories within bounding box and then union it into one shape? Thanks for help!</p>
</div>
<div id="comment-72998-info" class="comment-info">
<span class="comment-age">(11 Feb '20, 08:47)</span> <span class="comment-user userinfo">dnstankiewicz</span>
</div>
</div>
</div>
<div id="comment-tools-72978" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72978-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

