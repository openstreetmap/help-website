+++
type = "question"
title = "Evaluating type of road for a certain path given GPS coordonates"
description = '''Hello, Here is what i&#x27;m trying to achieve: I have a lot of GPS coordinates (long/lat) that represents an itinerary. I would like to be able to evaluate the types of road (highway tag of a way) for all these locations to be able to have statistics like this.  Your Itinerary :  - 40% Secondary  - 30% ...'''
date = "2018-03-09T09:44:00Z"
lastmod = "2018-03-09T10:12:00Z"
weight = 62601
keywords = [ "higway", "type", "road", "gps" ]
aliases = [ "/questions/62601" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Evaluating type of road for a certain path given GPS coordonates](/questions/62601/evaluating-type-of-road-for-a-certain-path-given-gps-coordonates)

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
<span id="post-62601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62601-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Here is what i'm trying to achieve: I have a lot of GPS coordinates (long/lat) that represents an itinerary. I would like to be able to evaluate the types of road (highway tag of a way) for all these locations to be able to have statistics like this.</p>
<p>Your Itinerary : - 40% Secondary - 30% Track - 30% Residential</p>
<p>What i tried : I tried to use the Overpass Turbo to get the ways around my gps coordonates with this kind of script</p>
<pre><code>    (
  way(around:1.0,45.645431, 1.812229);
  way(around:1.0,45.645381, 1.812486);
  way(around:1.0,45.645248, 1.812958);...); 
out tags;</code></pre>
<p>I do get some results, like that :</p>
<pre><code> &lt;way id=&quot;159143665&quot;&gt;
    &lt;tag k=&quot;highway&quot; v=&quot;tertiary&quot;/&gt;
    &lt;tag k=&quot;ref&quot; v=&quot;D 132E1&quot;/&gt;
  &lt;/way&gt;
  &lt;way id=&quot;159143666&quot;&gt;
    &lt;tag k=&quot;highway&quot; v=&quot;tertiary&quot;/&gt;
    &lt;tag k=&quot;ref&quot; v=&quot;D 132E2&quot;/&gt;
  &lt;/way&gt;</code></pre>
<p>But i don't retrieve a result for <strong>each</strong> gps coordinate so i cannot do statistics on that... I am not sure if my approach is good. Any advice/ solution?</p>
<p>Thanks for reading. Cheers.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-higway" rel="tag" title="see questions tagged &#39;higway&#39;">higway</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '18, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/0f07328454c89945ddcee32cbfd1d842?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hydeo&#39;s gravatar image" />
<p><span>Hydeo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hydeo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62601" class="comments-container">
&#10;</div>
<div id="comment-tools-62601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62601-form-container" class="comment-form-container">
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

<span id="62602"></span>

<div id="answer-container-62602" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62602-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you want to do is called "track matching". It requires a routing engine. The routing engine will compute the most likely, valid path through the OSM street network that corresponds to your GPS track. Then, once you know exactly which roads have (likely) been traveled, you can compute your statistics. Many existing routing engines offer track matching (e.g. Graphhopper, OSRM), but I don't know off the top of my head whether their results will contain all the road type information you want, or whether you'll need to modify the software.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '18, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62602" class="comments-container">
&#10;</div>
<div id="comment-tools-62602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62602-form-container" class="comment-form-container">
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

