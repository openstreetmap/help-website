+++
type = "question"
title = "Overpass: Retrieve ways that are member of more than one multipolygon"
description = '''I&#x27;d like to find ways that are members of more than one type=multipolygon relation with role &quot;outer&quot; with Overpass API as this often indicates errors/problems. I&#x27;m not sure how to approach this correctly. This is how far I got: relation({{bbox}})  [type=multipolygon]; way(r:&quot;outer&quot;); rel(bw:&quot;outer&quot;)...'''
date = "2017-03-12T21:35:00Z"
lastmod = "2017-03-13T21:39:00Z"
weight = 55027
keywords = [ "member", "overpass", "relations", "multipolygon" ]
aliases = [ "/questions/55027" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Retrieve ways that are member of more than one multipolygon](/questions/55027/overpass-retrieve-ways-that-are-member-of-more-than-one-multipolygon)

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
<span id="post-55027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55027-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to find ways that are members of more than one type=multipolygon relation with role "outer" with Overpass API as this often indicates errors/problems. I'm not sure how to approach this correctly. This is how far I got:</p>
<pre><code>relation({{bbox}})
  [type=multipolygon];
way(r:&quot;outer&quot;);
rel(bw:&quot;outer&quot;)(if:count(relations) &gt; 1);
(._;&gt;;);
&#10;out;</code></pre>
<p>I start with multipolygon relations, look for their outer ways and try to find those ways parent relations where they have the role outer and look if there are more than one.</p>
<p>Alternatively I could also start with ways, but I thought it might be good to restrict the input set more:</p>
<pre><code>way({{bbox}});
rel(bw:&quot;outer&quot;)(if:count(relations) &gt; 1);
(._;&gt;;);
&#10;out;</code></pre>
<p>I was not able to find any results and once I got an out of memory error. Is this somehow correct what I'm trying to do? Is this even possible with Overpass API?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-member" rel="tag" title="see questions tagged &#39;member&#39;">member</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '17, 21:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9be9845ba172a0e4fab182ecf03c51e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nebulon42&#39;s gravatar image" />
<p><span>nebulon42</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nebulon42 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '17, 21:36</strong> </span></p>
</div>
</div>
<div id="comments-container-55027" class="comments-container">
<span id="55039"></span>
<div id="comment-55039" class="comment">
<div id="post-55039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If a way is on the shared boundary between adjoining multipolygons, wouldn't it correctly be an "outer" for both? It seems to me that this would be a common and very much correct situation, so I wouldn't say that it would "often indicate errors/problems".</p>
</div>
<div id="comment-55039-info" class="comment-info">
<span class="comment-age">(13 Mar '17, 17:09)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="55041"></span>
<div id="comment-55041" class="comment">
<div id="post-55041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point. I missed that. What I meant is that a <em>closed</em> way that is in more than one multipolygon with role outer would indicate a potential problem. For a non-closed way this would indeed be a valid and maybe common situation.</p>
</div>
<div id="comment-55041-info" class="comment-info">
<span class="comment-age">(13 Mar '17, 21:22)</span> <span class="comment-user userinfo">nebulon42</span>
</div>
</div>
</div>
<div id="comment-tools-55027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55027-form-container" class="comment-form-container">
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

<span id="55038"></span>

<div id="answer-container-55038" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55038-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nebulon42 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure it is the best way to do it, but one way to find them is to use a foreach statement to look through the relations one by one:</p>
<pre><code>relation({{bbox}})[type=multipolygon]-&gt;.multis;
foreach.multis-&gt;.multi(
  // calculate outer ways of other multipolygons
  (.multis - .multi)-&gt;.others;
  way(r.others:&quot;outer&quot;)-&gt;.otherways;
  // outer ways of current multi
  way(r.multi:&quot;outer&quot;)-&gt;.multiways;
  // output ways in both sets
  way.multiways.otherways;
  out geom;
  );</code></pre>
<p><a href="http://overpass-turbo.eu/s/nsO">http://overpass-turbo.eu/s/nsO</a></p>
<p>A slightly adjusted query eliminates the duplicates by collecting the found ways together in a set before outputting them:</p>
<pre><code>relation({{bbox}})[type=multipolygon]-&gt;.multis;
foreach.multis-&gt;.multi(
  // calculate outer ways of other multipolygons
  (.multis - .multi)-&gt;.others;
  way(r.others:&quot;outer&quot;)-&gt;.otherways;
  // outer ways of current multi
  way(r.multi:&quot;outer&quot;)-&gt;.multiways;
  // collect found ways for output
  (way.multiways.otherways;.all;)-&gt;.all;
);
.all out geom;</code></pre>
<p><a href="http://overpass-turbo.eu/s/nsW">http://overpass-turbo.eu/s/nsW</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '17, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55038" class="comments-container">
<span id="55043"></span>
<div id="comment-55043" class="comment">
<div id="post-55043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, it clearly works, so I accepted it as answer. But as alester has pointed out above I haven't formulated the problem well.</p>
</div>
<div id="comment-55043-info" class="comment-info">
<span class="comment-age">(13 Mar '17, 21:39)</span> <span class="comment-user userinfo">nebulon42</span>
</div>
</div>
</div>
<div id="comment-tools-55038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55038-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55033"></span>

<div id="answer-container-55033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55033-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not good with Overpass, but could write a little program to extract them from a planet file, if you are not getting any answers here. Just open an issue on <a href="https://github.com/osmlab/fixing-polygons-in-osm">https://github.com/osmlab/fixing-polygons-in-osm</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '17, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-55033" class="comments-container">
<span id="55042"></span>
<div id="comment-55042" class="comment">
<div id="post-55042-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the offer! This would be a possibility, but Overpass API has the advantage of minutely diffs that I can't easily setup for myself. This allows for some agile clean-up.</p>
</div>
<div id="comment-55042-info" class="comment-info">
<span class="comment-age">(13 Mar '17, 21:25)</span> <span class="comment-user userinfo">nebulon42</span>
</div>
</div>
</div>
<div id="comment-tools-55033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55033-form-container" class="comment-form-container">
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

