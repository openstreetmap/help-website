+++
type = "question"
title = "Separate lines, polygons and points"
description = '''I have managed to extract some highway types out of an .osm file and when I display it in Quantum GIS it splits it into lines, points and polygons. Being roads I only need lines, but with points checked, I get thousands of points across the map. I have had a look and Quantum GIS reads type=polygon o...'''
date = "2012-06-20T11:29:00Z"
lastmod = "2015-10-07T02:25:00Z"
weight = 13656
keywords = [ "qgis", "type", "osmosis" ]
aliases = [ "/questions/13656" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Separate lines, polygons and points](/questions/13656/separate-lines-polygons-and-points)

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
<span id="post-13656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13656-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have managed to extract some highway types out of an .osm file and when I display it in Quantum GIS it splits it into lines, points and polygons. Being roads I only need lines, but with points checked, I get thousands of points across the map.</p>
<p>I have had a look and Quantum GIS reads type=polygon or type=line etc. Is there anyway to only include type=line when extracting data through osmosis?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '12, 11:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0dc847b1bc00d07449e18feb3772c0ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stuart576&#39;s gravatar image" />
<p><span>stuart576</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stuart576 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13656" class="comments-container">
&#10;</div>
<div id="comment-tools-13656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13656-form-container" class="comment-form-container">
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

<span id="13659"></span>

<div id="answer-container-13659" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13659-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not an osmosis expert but checking quickly the <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage">detailed usage on the wiki</a> says that you can filter ways on a tag list ("--tag-filter") with the option 'accept-ways'.</p>
<p>Example from the wiki:</p>
<pre><code>osmosis \
  --read-xml input.osm \
  --tf accept-ways highway=* \ 
  --tf reject-ways highway=motorway,motorway_link \
  --tf reject-relations \
  --used-node \
  --write-xml output.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '12, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-13659" class="comments-container">
<span id="13660"></span>
<div id="comment-13660" class="comment">
<div id="post-13660-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>have tried adding --tf reject-ways type=point,polygon to my script but it makes no difference</p>
</div>
<div id="comment-13660-info" class="comment-info">
<span class="comment-age">(20 Jun '12, 13:26)</span> <span class="comment-user userinfo">stuart576</span>
</div>
</div>
<span id="13661"></span>
<div id="comment-13661" class="comment">
<div id="post-13661-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Right I have solved this, after reading up on nodes and ways.</p>
<p>"...a node will normally have at least one tag to define it's purpose or be part of a Relation and may have multiple tags."</p>
<p>From this I realised that the points were only relations to highway tags. So I added "--tf reject-relations" and voila!</p>
<p>Thanks for the guidance Pieren.</p>
</div>
<div id="comment-13661-info" class="comment-info">
<span class="comment-age">(20 Jun '12, 13:35)</span> <span class="comment-user userinfo">stuart576</span>
</div>
</div>
<span id="45771"></span>
<div id="comment-45771" class="comment">
<div id="post-45771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/3876/stuart576">@stuart576</a>, I'm having trouble with this. Can you update with the complete solution that worked for you?</p>
</div>
<div id="comment-45771-info" class="comment-info">
<span class="comment-age">(07 Oct '15, 02:25)</span> <span class="comment-user userinfo">mkirk</span>
</div>
</div>
</div>
<div id="comment-tools-13659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13659-form-container" class="comment-form-container">
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

