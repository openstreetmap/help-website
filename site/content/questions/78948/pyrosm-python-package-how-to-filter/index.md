+++
type = "question"
title = "Pyrosm python package: how to filter?"
description = '''Hello,  I&#x27;m using the pyrosm package in python and I read with it a bdf file for Bristol city. I want to filter and query all the shops and couple of amenities. However, every time I filter only for all shops I&#x27;ve 3,367 records. When I filter for all shops and some amenities, instead of having more ...'''
date = "2021-02-19T15:21:00Z"
lastmod = "2021-02-19T15:21:00Z"
weight = 78948
keywords = [ "python", "filter", "osm", "pyrosm" ]
aliases = [ "/questions/78948" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Pyrosm python package: how to filter?](/questions/78948/pyrosm-python-package-how-to-filter)

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
<span id="post-78948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78948-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm using the pyrosm package in python and I read with it a bdf file for Bristol city. I want to filter and query all the shops and couple of amenities. However, every time I filter only for all shops I've 3,367 records. When I filter for all shops and some amenities, instead of having more records I have less (2,059). It seems in the data that I miss some of the shops. Below my code.</p>
<pre><code>from pyrosm import OSM
osm_path =&#39;bristol-latest.osm.pbf&#39; # downloaded from geofabrik
osm = OSM(osm_path)
custom_filter = {&quot;shop&quot;:True, &quot;amenity&quot;:[&quot;bar&quot;, &quot;cafe&quot;, &quot;fast_food&quot;, &quot;ice_cream&quot;, &quot;pub&quot;, &quot;cinema&quot;]}
pois = osm.get_pois(custom_filter=custom_filter)</code></pre>
<p>Any idea what's wrong please?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-pyrosm" rel="tag" title="see questions tagged &#39;pyrosm&#39;">pyrosm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '21, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/78ca4faede71449fd93c1790b87d816d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Katerina_Kourou&#39;s gravatar image" />
<p><span>Katerina_Kourou</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Katerina_Kourou has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '21, 15:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span></p>
</div>
</div>
<div id="comments-container-78948" class="comments-container">
&#10;</div>
<div id="comment-tools-78948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78948-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

