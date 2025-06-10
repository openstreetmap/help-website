+++
type = "question"
title = "Get the bounds of areas in overpass (states)"
description = '''I want to get the coordinates that limit a state using overpass (OSM) like this: {  &quot;type&quot;: &quot;way&quot;,  &quot;id&quot;: 24157062,  &quot;bounds&quot;: {  &quot;minlat&quot;: 24.4535230,  &quot;minlon&quot;: 54.3770477,  &quot;maxlat&quot;: 24.4541602,  &quot;maxlon&quot;: 54.3777469  } }  the problem is when I query an area, it does not return the arguments I ne...'''
date = "2021-12-28T22:57:00Z"
lastmod = "2021-12-31T16:17:00Z"
weight = 82907
keywords = [ "bounding_box" ]
aliases = [ "/questions/82907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get the bounds of areas in overpass (states)](/questions/82907/get-the-bounds-of-areas-in-overpass-states)

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
<span id="post-82907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82907-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get the coordinates that limit a state using overpass (OSM) like this:</p>
<pre><code>{
  &quot;type&quot;: &quot;way&quot;,
  &quot;id&quot;: 24157062,
  &quot;bounds&quot;: {
    &quot;minlat&quot;: 24.4535230,
    &quot;minlon&quot;: 54.3770477,
    &quot;maxlat&quot;: 24.4541602,
    &quot;maxlon&quot;: 54.3777469
  }
}</code></pre>
<p>the problem is when I query an area, it does not return the arguments I need, and it returns this:</p>
<pre><code>{
  &quot;type&quot;: &quot;area&quot;,
  &quot;id&quot;: 3600307763,
  &quot;tags&quot;: {
    &quot;ISO3166-1&quot;: &quot;AE&quot;,
    &quot;ISO3166-1:alpha2&quot;: &quot;AE&quot;,
    &quot;ISO3166-1:alpha3&quot;: &quot;ARE&quot;,
    &quot;ISO3166-1:numeric&quot;: &quot;784&quot;,
    &quot;admin_level&quot;: &quot;2&quot;,
    &quot;alt_name:ar&quot;: &quot;الإمارات العربيّة المتّحدة&quot;,
    &quot;alt_name:la&quot;: &quot;Emiratus Arabici Uniti&quot;,
    ...
    }
}</code></pre>
<p>is it possible to consult the bounding boxes of an area? and if so, could you help me with the structure of the query</p>
<p>i'm trying to do it this way:</p>
<pre><code>[out:json];
 area[&#39;ISO3166-2&#39;=&#39;EC-L&#39;][admin_level=4];
 out bb;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding_box" rel="tag" title="see questions tagged &#39;bounding_box&#39;">bounding_box</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '21, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/516aedeace620064dadd49fa48e40c0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chjuca&#39;s gravatar image" />
<p><span>chjuca</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chjuca has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82907" class="comments-container">
&#10;</div>
<div id="comment-tools-82907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82907-form-container" class="comment-form-container">
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

<span id="82926"></span>

<div id="answer-container-82926" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>area[&#39;ISO3166-2&#39;=&#39;EC-L&#39;];
rel(pivot);
out bb;</code></pre>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Area_pivot_.28pivot.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Area_pivot_.28pivot.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '21, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82926" class="comments-container">
&#10;</div>
<div id="comment-tools-82926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82926-form-container" class="comment-form-container">
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

