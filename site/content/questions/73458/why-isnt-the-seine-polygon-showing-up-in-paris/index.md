+++
type = "question"
title = "Why isn&#x27;t The Seine polygon showing up in Paris?"
description = '''I&#x27;m querying water in a 5 km radius of Paris city centre and was expecting the Seine to show up in its entirety; however, it&#x27;s only showing in part as a polygon? What am I doing wrong, please? Query: [out:json]; nwr[&quot;natural&quot;~&quot;water&quot;] (around:5000, 48.8693488, 2.319511);  out meta; &amp;gt;; out skel qt...'''
date = "2020-03-10T14:18:00Z"
lastmod = "2020-03-10T19:06:00Z"
weight = 73458
keywords = [ "water", "paris", "river" ]
aliases = [ "/questions/73458" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why isn't The Seine polygon showing up in Paris?](/questions/73458/why-isnt-the-seine-polygon-showing-up-in-paris)

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
<span id="post-73458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73458-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm querying water in a 5 km radius of Paris city centre and was expecting the Seine to show up in its entirety; however, it's only showing in part as a polygon?</p>
<p>What am I doing wrong, please?</p>
<p>Query:</p>
<pre><code>[out:json];
nwr[&quot;natural&quot;~&quot;water&quot;] (around:5000, 48.8693488, 2.319511); 
out meta;
&gt;; out skel qt;</code></pre>
<p>I do query the using 'river' separately but I really want the polygon and not the line!</p>
<p><img src="https://help.openstreetmap.org/upfiles/laseine.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-paris" rel="tag" title="see questions tagged &#39;paris&#39;">paris</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '20, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/09f53b06dcac1cb83c71c601571cf449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jusdespommes&#39;s gravatar image" />
<p><span>jusdespommes</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jusdespommes has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-73458" class="comments-container">
&#10;</div>
<div id="comment-tools-73458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73458-form-container" class="comment-form-container">
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

<span id="73460"></span>

<div id="answer-container-73460" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73460-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please have a look at the wiki on <a href="https://wiki.openstreetmap.org/wiki/Rivers">different ways to tag rivers</a>. The <a href="https://www.openstreetmap.org/way/22972062">Seine to the East of your selection</a> is tagged as waterway=riverbank.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '20, 14:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-73460" class="comments-container">
<span id="73461"></span>
<div id="comment-73461" class="comment">
<div id="post-73461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
<p>I have that in my separate river query - however, I only get a polyline back in my output. Is there no way to get a multi-polygon instead, please?</p>
<p><img src="https://help.openstreetmap.org/upfiles/Capture_zNxkJU4.PNG" alt="alt text" /></p>
</div>
<div id="comment-73461-info" class="comment-info">
<span class="comment-age">(10 Mar '20, 15:38)</span> <span class="comment-user userinfo">jusdespommes</span>
</div>
</div>
<span id="73462"></span>
<div id="comment-73462" class="comment">
<div id="post-73462-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Replied below to add a pic!</p>
</div>
<div id="comment-73462-info" class="comment-info">
<span class="comment-age">(10 Mar '20, 15:38)</span> <span class="comment-user userinfo">jusdespommes</span>
</div>
</div>
<span id="73464"></span>
<div id="comment-73464" class="comment">
<div id="post-73464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well you get the objects back that are in the database. If you want to join them or whatever it is you hope to get out of a multi-polygon you have to do some post-processing afterwards.</p>
<p>Maybe you describe a bit better what it is you try to achieve if I missed something.</p>
</div>
<div id="comment-73464-info" class="comment-info">
<span class="comment-age">(10 Mar '20, 19:06)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-73460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73460-form-container" class="comment-form-container">
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

