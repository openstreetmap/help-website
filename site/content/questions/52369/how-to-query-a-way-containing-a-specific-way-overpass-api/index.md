+++
type = "question"
title = "how to query a way containing a specific way overpass api?"
description = '''I have this query to get hot_water_tanks: [out:json][timeout:85];  (   node[&quot;man_made&quot;=&quot;hot_water_tank&quot;]({{bbox}});  way[&quot;man_made&quot;=&quot;hot_water_tank&quot;]({{bbox}});  );  out body; &amp;gt;; out skel qt;  and here to get industrial building or landuse. [out:json][timeout:85];  (  node[&quot;landuse&quot;=&quot;industrial&quot;]...'''
date = "2016-10-04T14:56:00Z"
lastmod = "2016-10-06T09:36:00Z"
weight = 52369
keywords = [ "overpass", "overpass-turbo", "overpass-api", "overpass-ql" ]
aliases = [ "/questions/52369" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to query a way containing a specific way overpass api?](/questions/52369/how-to-query-a-way-containing-a-specific-way-overpass-api)

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
<span id="post-52369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52369-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have this query to get hot_water_tanks:</p>
<pre><code>[out:json][timeout:85];
&#10;(
&#10;  node[&quot;man_made&quot;=&quot;hot_water_tank&quot;]({{bbox}});
  way[&quot;man_made&quot;=&quot;hot_water_tank&quot;]({{bbox}});
&#10;);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>and here to get industrial building or landuse.</p>
<pre><code>[out:json][timeout:85];
&#10;(
&#10;node[&quot;landuse&quot;=&quot;industrial&quot;]({{bbox}});
  way[&quot;landuse&quot;=&quot;industrial&quot;]({{bbox}});
rel[&quot;landuse&quot;=&quot;industrial&quot;]({{bbox}});
&#10;
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>How can i get only landuse=industrial where there is a hot_water_tank?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '16, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/fdd97ceec9f9544f1c9d7c57b1ee9707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JsonKh&#39;s gravatar image" />
<p><span>JsonKh</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JsonKh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '16, 15:48</strong> </span></p>
</div>
</div>
<div id="comments-container-52369" class="comments-container">
<span id="52377"></span>
<div id="comment-52377" class="comment">
<div id="post-52377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure how to do this in overpass, but you could easily do this within a GIS tool like QGIS.</p>
</div>
<div id="comment-52377-info" class="comment-info">
<span class="comment-age">(06 Oct '16, 09:08)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="52378"></span>
<div id="comment-52378" class="comment">
<div id="post-52378-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>cross-posted: <a href="https://stackoverflow.com/questions/39870997/how-can-i-find-a-tag-way-in-another-way-area-overpass">https://stackoverflow.com/questions/39870997/how-can-i-find-a-tag-way-in-another-way-area-overpass</a></p>
</div>
<div id="comment-52378-info" class="comment-info">
<span class="comment-age">(06 Oct '16, 09:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52369-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

