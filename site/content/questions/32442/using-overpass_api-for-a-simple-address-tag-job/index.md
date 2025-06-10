+++
type = "question"
title = "using overpass_API for a simple address-tag-job"
description = '''hello - i wanted to run a osmconvert &amp;amp; filter with the following goal - to get the following tags out of the datas: addr:street addr:housenumber addr:city so i decided to do the following command ./osmconvert hamburg-latest.osm.pbf --all-to-nodes -o=hamburgrestaurants_2.o5m ./osmfilter hamburgre...'''
date = "2014-04-19T10:46:00Z"
lastmod = "2014-06-13T09:44:00Z"
weight = 32442
keywords = [ "overpass", "osmconvert", "api", "address" ]
aliases = [ "/questions/32442" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using overpass_API for a simple address-tag-job](/questions/32442/using-overpass_api-for-a-simple-address-tag-job)

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
<span id="post-32442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32442-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello - i wanted to run a osmconvert &amp; filter with the following goal - to get the following tags out of the datas:</p>
<p>addr:street addr:housenumber addr:city</p>
<p>so i decided to do the following command</p>
<pre><code>./osmconvert hamburg-latest.osm.pbf --all-to-nodes -o=hamburgrestaurants_2.o5m
./osmfilter hamburgrestaurants_2.o5m --keep=&quot;amenity=restaurant&quot; -o=restaurant_2.o5m
./osmconvert restaurant_2.o5m --csv=&quot;@id @lon @lat shop name  addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=restaurant_2.csv</code></pre>
<p>but i failed - there were no streets no housenumbers and cities. Now i decidet to use overpass-API which seems to be less complicated. Can someone advice me here to go the first step.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '14, 10:46</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '14, 16:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span></p>
</div>
</div>
<div id="comments-container-32442" class="comments-container">
&#10;</div>
<div id="comment-tools-32442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32442-form-container" class="comment-form-container">
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

<span id="32478"></span>

<div id="answer-container-32478" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32478-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmconvert is a bit picky when is comes to specifying csv field names. Especially extra whitespace characters seem to cause some issue. In your case you'll have to remove the superfluous space character between name and addr:street to get some results according to your csv string (of course only where this data exists in OSM in the first place).</p>
<pre><code>./osmconvert restaurant_2.o5m --csv=&quot;@id @lon @lat shop name addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=restaurant_2.csv</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '14, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-32478" class="comments-container">
<span id="33946"></span>
<div id="comment-33946" class="comment">
<div id="post-33946-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you for the help. It helps alot - and gives new starting points. Greetings</p>
</div>
<div id="comment-33946-info" class="comment-info">
<span class="comment-age">(13 Jun '14, 09:44)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-32478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32478-form-container" class="comment-form-container">
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

