+++
type = "question"
title = "Get all ways of a specific tag with Overpass Turbo (geocode)"
description = '''How do I get all ways in a US state (e.g. Oklahoma) which have the &quot;tiger:cfcc&quot; tag? I&#x27;ve tried to query for it here: https://overpass-turbo.eu/s/wLz: [out:json][timeout:300];  {{geocodeArea:Oklahoma}}-&amp;gt;.searchArea; way[&quot;tiger:cfcc&quot;]  (area.searchArea);  out body;  &amp;gt;; out skel qt;  May you ple...'''
date = "2018-03-06T20:09:00Z"
lastmod = "2018-03-07T12:41:00Z"
weight = 62536
keywords = [ "overpass" ]
aliases = [ "/questions/62536" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get all ways of a specific tag with Overpass Turbo (geocode)](/questions/62536/get-all-ways-of-a-specific-tag-with-overpass-turbo-geocode)

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
<span id="post-62536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62536-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I get all ways in a US state (e.g. Oklahoma) which have the "tiger:cfcc" tag?</p>
<p>I've tried to query for it here: <a href="https://overpass-turbo.eu/s/wLz">https://overpass-turbo.eu/s/wLz</a>:</p>
<pre><code>[out:json][timeout:300];
&#10;{{geocodeArea:Oklahoma}}-&gt;.searchArea;
way[&quot;tiger:cfcc&quot;]
  (area.searchArea);
&#10;out body;
&#10;&gt;;
out skel qt;</code></pre>
<p>May you please help me bringing it to work?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '18, 20:09</strong></p>
<img src="https://secure.gravatar.com/avatar/8e0867aa963fc989a200f2f35144d3c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="landuse&#39;s gravatar image" />
<p><span>landuse</span><br />
<span class="score" title="116 reputation points">116</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="landuse has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62536" class="comments-container">
&#10;</div>
<div id="comment-tools-62536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62536-form-container" class="comment-form-container">
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

<span id="62539"></span>

<div id="answer-container-62539" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62539-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you won't be able to get it to work. Even a small area has many ways and will be a large query:</p>
<p><a href="https://overpass-turbo.eu/s/wLH">https://overpass-turbo.eu/s/wLH</a></p>
<p>(I've used <code>out center</code> there, so it isn't returning all the nodes, but it gets the point across)</p>
<p>Your best bet is to grab an extract from <a href="https://download.geofabrik.de/north-america/us/oklahoma.html">https://download.geofabrik.de/north-america/us/oklahoma.html</a> and process that locally using <a href="https://wiki.openstreetmap.org/wiki/Osmium">osmium</a> or <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '18, 22:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-62539" class="comments-container">
<span id="62548"></span>
<div id="comment-62548" class="comment">
<div id="post-62548-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As ever I'd recommend the osmconvert/osmfilter combination for simple filtering problems like this. These can be downloaded and run as is, which is not true of osmium, and not always true for osmosis.</p>
</div>
<div id="comment-62548-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 12:41)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62539-form-container" class="comment-form-container">
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

