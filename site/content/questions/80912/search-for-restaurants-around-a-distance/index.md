+++
type = "question"
title = "Search for restaurants around a distance"
description = '''Hi, I need the following: I&#x27;m searching for restaurants around &quot;95448 Bayreuth&quot; (Germany) 1000 meters. This is what I got so far, it works nearly, but it shows also restaurants outside the 1000 meters radius: [out:json][timeout:25]; // fetch area &quot;Bonn&quot; to search in {{geocodeArea:95448 Bayreuth}}-&amp;g...'''
date = "2021-07-10T16:28:00Z"
lastmod = "2021-07-10T20:15:00Z"
weight = 80912
keywords = [ "overpass", "overpass-turbo", "around" ]
aliases = [ "/questions/80912" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Search for restaurants around a distance](/questions/80912/search-for-restaurants-around-a-distance)

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
<span id="post-80912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80912-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need the following: I'm searching for restaurants around "95448 Bayreuth" (Germany) 1000 meters.</p>
<p>This is what I got so far, it works nearly, but it shows also restaurants outside the 1000 meters radius:</p>
<pre><code>[out:json][timeout:25];
// fetch area &quot;Bonn&quot; to search in
{{geocodeArea:95448 Bayreuth}}-&gt;.searchArea;
// gather results
(
  // query part for: &quot;restaurant&quot;
  node(around:1000)[&quot;amenity&quot;=&quot;restaurant&quot;](area.searchArea);
  way[&quot;amenity&quot;=&quot;restaurant&quot;](area.searchArea);
  relation[&quot;amenity&quot;=&quot;restaurant&quot;](area.searchArea);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>May you help me with that, please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '21, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d69ef280e0dcf73b27ef022acb0ef864?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alpham8&#39;s gravatar image" />
<p><span>alpham8</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alpham8 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '21, 16:37</strong> </span></p>
</div>
</div>
<div id="comments-container-80912" class="comments-container">
<span id="80917"></span>
<div id="comment-80917" class="comment">
<div id="post-80917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please clarify what you mean by 95448 Bayreuth as that is a boundary. {{geocodeArea:95448 Bayreuth}}; rel(pivot); out geom;</p>
</div>
<div id="comment-80917-info" class="comment-info">
<span class="comment-age">(10 Jul '21, 19:59)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-80912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80912-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="80916"></span>

<div id="answer-container-80916" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80916-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alpham8 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a number of issues with your search:</p>
<ol>
<li>You are searching for all restaurants mapped as a node which are in the entire Gemeinde of Bayreuth + those 1000 m outside that boundary. You need to find the node representing the centre of Bayreuth not the area.</li>
<li>Additionally you are finding any Restaurants mapped as areas within (but not outside) Bayreuth (the around constraint is not applied to ways &amp; areas.</li>
</ol>
<p>This appears to be closer to what you want:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query part for: “name=Bayreuth”
  node[&quot;name&quot;=&quot;Bayreuth&quot;][place]-&gt;.a;
  nwr(around.a:1000)[amenity=restaurant];
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>The place node for Bayreuth is places in a result set &amp; that set is searched for restaurants within 1000 m. If there is more than one place with the name other approaches may be needed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '21, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-80916" class="comments-container">
&#10;</div>
<div id="comment-tools-80916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80916-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80918"></span>

<div id="answer-container-80918" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80918-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want all restaurants within the boundary of Bayreuth:</p>
<pre><code>{{geocodeArea:95448 Bayreuth}}-&gt;.Bayreuth;
rel(pivot.Bayreuth);
out geom;
nwr[amenity=restaurant](area.Bayreuth); 
out center;</code></pre>
<p>If you want all restaurants around the node of the town.</p>
<pre><code>node[place][name=Bayreuth];
nwr(around:1000)[amenity=restaurant];
out center;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '21, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80918" class="comments-container">
&#10;</div>
<div id="comment-tools-80918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80918-form-container" class="comment-form-container">
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

