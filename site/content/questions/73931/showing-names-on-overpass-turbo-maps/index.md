+++
type = "question"
title = "Showing names on overpass turbo maps"
description = '''This works great, but I would also like to get the name of each object (milestone) found shown next to the object. [out:json][timeout:25]; // gather results (  // query part for: “highway=milestone”  node[&quot;highway&quot;=&quot;milestone&quot;]({{bbox}});  way[&quot;highway&quot;=&quot;milestone&quot;]({{bbox}});  relation[&quot;highway&quot;=&quot;m...'''
date = "2020-04-01T19:34:00Z"
lastmod = "2020-04-02T15:38:00Z"
weight = 73931
keywords = [ "overpass-turbo", "name" ]
aliases = [ "/questions/73931" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Showing names on overpass turbo maps](/questions/73931/showing-names-on-overpass-turbo-maps)

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
<span id="post-73931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This works great, but I would also like to get the <strong>name</strong> of each object (milestone) found shown next to the object.</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // query part for: “highway=milestone”
  node[&quot;highway&quot;=&quot;milestone&quot;]({{bbox}});
  way[&quot;highway&quot;=&quot;milestone&quot;]({{bbox}});
  relation[&quot;highway&quot;=&quot;milestone&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '20, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/47edd1ee4d973c50bbe7991bb063d09d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jidanni&#39;s gravatar image" />
<p><span>jidanni</span><br />
<span class="score" title="339 reputation points">339</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jidanni has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73931" class="comments-container">
<span id="73955"></span>
<div id="comment-73955" class="comment">
<div id="post-73955-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Isn't it weird for a milestone to have a name? It is not mentioned as a useful combination on the <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmilestone">wiki page</a>.</p>
</div>
<div id="comment-73955-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 14:08)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="73963"></span>
<div id="comment-73963" class="comment">
<div id="post-73963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, got it: {text: distance;}</p>
</div>
<div id="comment-73963-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 15:38)</span> <span class="comment-user userinfo">jidanni</span>
</div>
</div>
</div>
<div id="comment-tools-73931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73931-form-container" class="comment-form-container">
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

<span id="73952"></span>

<div id="answer-container-73952" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73952-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jidanni has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As documented on the <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/MapCSS#Markers_with_Text">wiki</a>, you can use MapCSS for that. Here is an <a href="https://overpass-turbo.eu/s/Sdh">example</a>.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '20, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73952" class="comments-container">
&#10;</div>
<div id="comment-tools-73952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73952-form-container" class="comment-form-container">
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

