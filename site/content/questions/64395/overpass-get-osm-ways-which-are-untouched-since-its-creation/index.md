+++
type = "question"
title = "Overpass: Get OSM ways which are untouched since it&#x27;s creation"
description = '''Hi, I&#x27;m looking for an Overpass Turbo query to get all ways with &quot;source&quot;=&quot;PGS&quot; which were NOT TOUCHED since it&#x27;s creation. I&#x27;ve heard that Overpass can do this and would be glad about any help.'''
date = "2018-06-26T19:50:00Z"
lastmod = "2018-06-27T04:07:00Z"
weight = 64395
keywords = [ "overpass", "version" ]
aliases = [ "/questions/64395" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Get OSM ways which are untouched since it's creation](/questions/64395/overpass-get-osm-ways-which-are-untouched-since-its-creation)

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
<span id="post-64395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64395-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm looking for an Overpass Turbo query to get all ways with "source"="PGS" which were NOT TOUCHED since it's creation.</p>
<p>I've heard that Overpass can do this and would be glad about any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '18, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/b081ac1f1126c32011d2c9cf57c2b430?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nehaj&#39;s gravatar image" />
<p><span>Nehaj</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nehaj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64395" class="comments-container">
&#10;</div>
<div id="comment-tools-64395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64395-form-container" class="comment-form-container">
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

<span id="64398"></span>

<div id="answer-container-64398" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64398-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nehaj has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Something like this:</p>
<pre><code>way[source=PGS](if:version()==1);
out;</code></pre>
<p>It takes a long time to complete and won't really work with Overpass Turbo, it returns too much data.</p>
<p><a href="http://overpass-turbo.eu/s/zS5">Here's a similar script</a> finding version 1 nodes, which are more common and easier to find, just to demonstrate the version test:</p>
<pre><code>node[source=PGS]({{bbox}})(if:version()==1);
out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '18, 02:14</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-64398" class="comments-container">
<span id="64400"></span>
<div id="comment-64400" class="comment">
<div id="post-64400-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Please note that the version of a way is not increased when one of its points is moved. It only changes when the tags on the way are changed or when nodes are added/deleted</p>
</div>
<div id="comment-64400-info" class="comment-info">
<span class="comment-age">(27 Jun '18, 04:07)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-64398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64398-form-container" class="comment-form-container">
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

