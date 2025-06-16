+++
type = "question"
title = "Add reverse geocoding information to the overpass resulting set."
description = '''I have a overpass query which returns lot of nodes. I would like to know whether there is a way to add reverse geocoding information to the resulting data set. Details of my case are not that important, but just for completness: area[name=&quot;Česko&quot;];(node[information=&quot;guidepost&quot;](area););out;  in fact...'''
date = "2014-08-19T01:55:00Z"
lastmod = "2022-07-23T23:21:00Z"
weight = 35976
keywords = [ "overpass", "reversegeocoding", "reverse" ]
aliases = [ "/questions/35976" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Add reverse geocoding information to the overpass resulting set.](/questions/35976/add-reverse-geocoding-information-to-the-overpass-resulting-set)

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
<span id="post-35976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35976-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a overpass query which returns lot of nodes. I would like to know whether there is a way to add reverse geocoding information to the resulting data set. Details of my case are not that important, but just for completness:</p>
<pre><code>area[name=&quot;Česko&quot;];(node[information=&quot;guidepost&quot;](area););out;</code></pre>
<p>in fact i do not need full reverse geocoding info for nodes, I only need relation of certain administrative level, so if this is possible to add into the result set, it would be great.</p>
<p>PS: I know that I can read the result set and then reverse geocode each individual node, but it seems very inefficient to me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '14, 01:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e6dd88ec54643689069f97f0d52398ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gorn&#39;s gravatar image" />
<p><span>gorn</span><br />
<span class="score" title="542 reputation points">542</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gorn has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '14, 10:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-35976" class="comments-container">
&#10;</div>
<div id="comment-tools-35976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35976-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="36014"></span>

<div id="answer-container-36014" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36014-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-36014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gorn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please have a look at <a href="http://overpass-turbo.eu/s/4EF">http://overpass-turbo.eu/s/4EF</a></p>
<p>The foreach loop enables you to get the areas a node lies in right after each node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '14, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '14, 18:16</strong> </span></p>
</div>
</div>
<div id="comments-container-36014" class="comments-container">
<span id="36035"></span>
<div id="comment-36035" class="comment">
<div id="post-36035-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To avoid retrieving the same area details many times, you could just return the area id in a first API call and retrieve the missing area details in a second query call for each distinct area id returned by the first query.</p>
<p>After the signpost node, you would just get the following detail from the first query:</p>
<p>&lt;area id="3600435511"/&gt; &lt;area id="3600442466"/&gt;</p>
<p>In a second query you could fetch the more details for those area ids: (area(3600435511);area(3600442466););out;</p>
<p>This could save some bandwidth on your end.</p>
<p><a href="http://overpass-turbo.eu/s/4Fo">http://overpass-turbo.eu/s/4Fo</a></p>
</div>
<div id="comment-36035-info" class="comment-info">
<span class="comment-age">(20 Aug '14, 23:16)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="36036"></span>
<div id="comment-36036" class="comment">
<div id="post-36036-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Execllent idea!</p>
<p>On top of this, you could even avoid to ask for a list of ids:</p>
<p><a href="http://overpass-turbo.eu/s/4FJ">http://overpass-turbo.eu/s/4FJ</a></p>
</div>
<div id="comment-36036-info" class="comment-info">
<span class="comment-age">(21 Aug '14, 05:03)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-36014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36014-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35994"></span>

<div id="answer-container-35994" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35994-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look for "batch geocoding" or "batch reverse geocoder" or similar on this FAQ site.</p>
<p>Or have a closer look at the OSM wiki about <a href="https://wiki.openstreetmap.org/wiki/Search_engines">Search engines</a> ... maybe there is a solution for your aim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '14, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-35994" class="comments-container">
&#10;</div>
<div id="comment-tools-35994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35994-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85206"></span>

<div id="answer-container-85206" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For anyone arriving from a Google search:</p>
<pre><code>area[name=&quot;Česko&quot;];
node[information=guidepost][ele~&quot;^1..$&quot;](area)-&gt;.Posts;
.Posts is_in;
rel(pivot)[admin_level=&quot;6&quot;];
out geom;
.Posts out center;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '22, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-85206" class="comments-container">
&#10;</div>
<div id="comment-tools-85206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85206-form-container" class="comment-form-container">
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

