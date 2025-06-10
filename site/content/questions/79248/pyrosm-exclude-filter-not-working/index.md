+++
type = "question"
title = "pyrosm exclude filter not working"
description = '''hi I&#x27;m trying to use pyrosm to read a pbf file and filter it to get &#x27;major&#x27; driving edges i.e. which are not parking/parking aisle etc. I tried using the &quot;exclude&quot; filter type to get edges that don&#x27;t have specific tags, but I still get such edges. Any idea what am I doing wrong? thanks My code is: f...'''
date = "2021-03-14T15:45:00Z"
lastmod = "2021-03-14T15:45:00Z"
weight = 79248
keywords = [ "filter", "pyrosm" ]
aliases = [ "/questions/79248" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pyrosm exclude filter not working](/questions/79248/pyrosm-exclude-filter-not-working)

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
<span id="post-79248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79248-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi</p>
<p>I'm trying to use pyrosm to read a pbf file and filter it to get 'major' driving edges i.e. which are not parking/parking aisle etc. I tried using the "exclude" filter type to get edges that don't have specific tags, but I still get such edges. Any idea what am I doing wrong?</p>
<p>thanks</p>
<p>My code is:</p>
<pre><code>from pyrosm import OSM, get_data
drive_filter = dict(
    area=[&#39;yes&#39;],
    service=[&#39;parking&#39;, &#39;parking_aisle&#39;, &#39;private&#39;, &#39;emergency_access&#39;,&#39;parking_aisle&#39;],
    highway=[&#39;cycleway&#39;, &#39;footway&#39;, &#39;path&#39;, &#39;pedestrian&#39;, &#39;steps&#39;, &#39;track&#39;,
             &#39;corridor&#39;, &#39;elevator&#39;, &#39;escalator&#39;, &#39;proposed&#39;, &#39;construction&#39;,
             &#39;bridleway&#39;, &#39;abandoned&#39;, &#39;platform&#39;, &#39;raceway&#39;],
    motor_vehicle=[&#39;no&#39;],
    motorcar=[&#39;no&#39;]
)
osm = OSM(get_data(&quot;test_pbf&quot;))
driving = osm.get_data_by_custom_criteria(custom_filter=drive_filter,
                                          osm_keys_to_keep=&quot;highway&quot;,
                                          filter_type=&quot;exclude&quot;)
print(driving[&#39;service&#39;].unique())</code></pre>
<p>Output is:</p>
<pre><code>[None &#39;driveway&#39; &#39;parking_aisle&#39;]</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-pyrosm" rel="tag" title="see questions tagged &#39;pyrosm&#39;">pyrosm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '21, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/32a6051739552d8a3ffd4e8f91998a5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anatrk&#39;s gravatar image" />
<p><span>anatrk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anatrk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '21, 07:07</strong> </span></p>
</div>
</div>
<div id="comments-container-79248" class="comments-container">
&#10;</div>
<div id="comment-tools-79248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79248-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

