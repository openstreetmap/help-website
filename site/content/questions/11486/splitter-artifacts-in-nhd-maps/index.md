+++
type = "question"
title = "Splitter artifacts in NHD maps"
description = '''OSM experts, Thanks for your time. I&#x27;m experimenting with building maps from US NHD data and have encountered a problem that only comes up when I split my osm files with splitter. I&#x27;m using the latest svn version of it and mkgmap. Here&#x27;s the short version: (1) Use ogr2osm with a suitable translation...'''
date = "2012-03-24T04:40:00Z"
lastmod = "2012-03-24T04:40:00Z"
weight = 11486
keywords = [ "splitter", "problem", "nhd" ]
aliases = [ "/questions/11486" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Splitter artifacts in NHD maps](/questions/11486/splitter-artifacts-in-nhd-maps)

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
<span id="post-11486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11486-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OSM experts,</p>
<p>Thanks for your time. I'm experimenting with building maps from US NHD data and have encountered a problem that only comes up when I split my osm files with splitter. I'm using the latest svn version of it and mkgmap. Here's the short version:</p>
<p>(1) Use ogr2osm with a suitable translation file to convert NHDFlowline.shp -&gt; NHDFlowline.osm and NHDWaterbody.shp -&gt; NHDWaterbody.osm</p>
<p>(2) Use sed to add dummy database fields so that these osm files are acceptable to osmosis.</p>
<p>(3) Use osmosis to delete nodes that aren't used by ways in these files, eg</p>
<pre><code>osmosis --rx NHDWaterbody.osm --tf accept-way natural=water,natural=wetland,landuse=reservoir,man_made=reservoir,leisure=swimming_pool --used-node  --wx NHDWaterbody.filtered.osm</code></pre>
<p>(4) Run splitter:</p>
<pre><code>splitter --split-file=areas.list --mapid=20000000 --max-nodes=2400000  NHDFlowline.filtered.osm NHDWaterbody.filtered.osm</code></pre>
<p>(5) Run mkgmap (with loads of options that aren't relevant, experimentation shows).</p>
<p>In the case of the subbassin I'm experimenting with, two of the three tiles have large, spurious, angular lakes. I've put a screenshot from from qlandkartegt at <a href="http://www.math.sjsu.edu/~stanley/Screenshot.png">link text</a> for the time being.</p>
<p>If it helps any, one large angular water area is given the name that belongs to a lake near, but not touching the edge of the tile containing that spurious lake. Another clue, perhaps, is that between the actual lake of that name and the spurious region in the adjoining tile is a lake the straddles the two tiles, but appears in neither.</p>
<p>Further possible hints:</p>
<p>(1) mkgmap can actually handle this modest amount of data without splitting. Just using mkgmap, I don't get the spurious water area when building a map from the two filtered osm files.</p>
<p>(2) I can split either NHDFlowline.filtered.osm or the NHDWaterbody.filtered.osm file using the areas.list file generated when splitting them together, and the mkgmap results are good.</p>
<p>Thanks for any pointers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-splitter" rel="tag" title="see questions tagged &#39;splitter&#39;">splitter</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-nhd" rel="tag" title="see questions tagged &#39;nhd&#39;">nhd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '12, 04:40</strong></p>
<img src="https://secure.gravatar.com/avatar/3a1ff01c0aea36852c07f21c2c416de2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Utea&#39;s gravatar image" />
<p><span>Utea</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Utea has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11486" class="comments-container">
&#10;</div>
<div id="comment-tools-11486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11486-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

