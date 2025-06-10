+++
type = "question"
title = "How can i exclude &#x27;admin_centre&#x27; from my output?"
description = '''I am working on project where i need the boundaries at admin level 6 in geojson format. I am using the following query. but the output of the query also includes &quot;admin_centre&quot;. I dont want admin_centre in my output. how can i archive this? Query: [out:json][timeout:25]; {{geocodeArea: india}}-&amp;gt;....'''
date = "2020-12-02T11:58:00Z"
lastmod = "2020-12-03T03:53:00Z"
weight = 77831
keywords = [ "exclude", "admin_boundary", "admin_centre" ]
aliases = [ "/questions/77831" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can i exclude 'admin_centre' from my output?](/questions/77831/how-can-i-exclude-admin_centre-from-my-output)

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
<span id="post-77831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77831-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on project where i need the boundaries at admin level 6 in geojson format. I am using the following query. but the output of the query also includes "admin_centre". I dont want admin_centre in my output. how can i archive this?</p>
<p>Query:</p>
<pre><code>[out:json][timeout:25];
{{geocodeArea: india}}-&gt;.searchArea;
(
    relation(area.searchArea)[&quot;type&quot;=&quot;boundary&quot;][admin_level = 6];
);
out geom;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-exclude" rel="tag" title="see questions tagged &#39;exclude&#39;">exclude</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-admin_centre" rel="tag" title="see questions tagged &#39;admin_centre&#39;">admin_centre</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '20, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/203cf23bc7b343ffbec5dbb92c2857f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PramodG&#39;s gravatar image" />
<p><span>PramodG</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PramodG has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '20, 03:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span></p>
</div>
</div>
<div id="comments-container-77831" class="comments-container">
&#10;</div>
<div id="comment-tools-77831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77831-form-container" class="comment-form-container">
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

<span id="77836"></span>

<div id="answer-container-77836" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77836-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Build up the data directly instead of using <code>out geom;</code>:</p>
<pre><code>[out:json][timeout:25];
{{geocodeArea: Indiana}}-&gt;.searchArea;
rel(area.searchArea)[&quot;type&quot;=&quot;boundary&quot;][admin_level = 6];
out;
(
  way(r);
  node(w);
);
out skel;</code></pre>
<p><a href="http://overpass-turbo.eu/s/10NK">http://overpass-turbo.eu/s/10NK</a></p>
<p>The first <code>out;</code> is the boundaries and then the <code>out skel;</code> only includes the parts of the ways and nodes that are needed to construct the geometries.</p>
<p>(Note that I've used "Indiana" to make the example query complete faster)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '20, 03:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '20, 03:56</strong> </span></p>
</div>
</div>
<div id="comments-container-77836" class="comments-container">
&#10;</div>
<div id="comment-tools-77836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77836-form-container" class="comment-form-container">
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

