+++
type = "question"
title = "Address-tags in a very simple osmconvert &amp; filter task"
description = '''hello - i wanted to run a osmconvert &amp;amp; filter with the following goal - to get the following tags out of the datas:  addr:street  addr:housenumber  addr:city so i decided to do the following command ./osmconvert hamburg-latest.osm.pbf --all-to-nodes -o=hamburgrestaurants_2.o5m ./osmfilter hambur...'''
date = "2014-04-18T16:36:00Z"
lastmod = "2014-04-23T21:22:00Z"
weight = 32434
keywords = [ "osmconvert", "osm", "linux" ]
aliases = [ "/questions/32434" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Address-tags in a very simple osmconvert & filter task](/questions/32434/address-tags-in-a-very-simple-osmconvert-filter-task)

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
<span id="post-32434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32434-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
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
<p>but i failed - there were no streets no housenumbers and cities</p>
<p>what is wrong with this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '14, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '14, 16:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span></p>
</div>
</div>
<div id="comments-container-32434" class="comments-container">
&#10;</div>
<div id="comment-tools-32434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32434-form-container" class="comment-form-container">
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

<span id="32479"></span>

<div id="answer-container-32479" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32479-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is basically the same question as in <a href="/questions/32442/using-overpass_api-for-a-simple-adress-tag-job">your other post</a>. Issue: there's an extra space between "name" and "addr:street" in your osmconvert csv string. Remove it and you're all set.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '14, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-32479" class="comments-container">
<span id="32588"></span>
<div id="comment-32588" class="comment">
<div id="post-32588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear mmd - many many thanks - i will try it out and come back and report all my findings. Thx alot. your are great!</p>
</div>
<div id="comment-32588-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 21:22)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-32479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32479-form-container" class="comment-form-container">
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

