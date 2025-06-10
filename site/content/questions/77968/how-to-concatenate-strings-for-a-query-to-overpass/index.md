+++
type = "question"
title = "How to concatenate strings for a query to overpass"
description = '''I would like to write a query that takes the lateral and longitudinal gps coordinates as variables. I have tried it as followed : lat = 30.74797 long = 53.81236 import overpy api = overpy.Overpass()  result = api.query(&quot;&quot;&quot; way(around:5,&quot;&quot;&quot; + lat + &quot;&quot;&quot; , &quot;&quot;&quot; + long + &quot;&quot;&quot;)  [&#x27;highway&#x27;]  [&#x27;highway&#x27; !~ ...'''
date = "2020-12-17T14:32:00Z"
lastmod = "2020-12-17T17:52:00Z"
weight = 77968
keywords = [ "pyhton", "overpass", "jupyter" ]
aliases = [ "/questions/77968" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to concatenate strings for a query to overpass](/questions/77968/how-to-concatenate-strings-for-a-query-to-overpass)

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
<span id="post-77968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77968-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to write a query that takes the <em>lateral</em> and <em>longitudinal</em> gps coordinates as variables. I have tried it as followed :</p>
<pre><code>lat = 30.74797
long = 53.81236
import overpy
api = overpy.Overpass()
&#10;result = api.query(&quot;&quot;&quot;
way(around:5,&quot;&quot;&quot; + lat + &quot;&quot;&quot; , &quot;&quot;&quot; + long + &quot;&quot;&quot;)
  [&#39;highway&#39;]
  [&#39;highway&#39; !~ &#39;path&#39;]
  [&#39;highway&#39; !~ &#39;steps&#39;];
(
  ._;
  &gt;;
);
out;&quot;&quot;&quot;)</code></pre>
<p>Unfortunately it does not work as expected.</p>
<p>How could I manage that ? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pyhton" rel="tag" title="see questions tagged &#39;pyhton&#39;">pyhton</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-jupyter" rel="tag" title="see questions tagged &#39;jupyter&#39;">jupyter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '20, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/68b001d382235f9caa18384183210af0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dykay&#39;s gravatar image" />
<p><span>Dykay</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dykay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '20, 14:34</strong> </span></p>
</div>
</div>
<div id="comments-container-77968" class="comments-container">
&#10;</div>
<div id="comment-tools-77968" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77968-form-container" class="comment-form-container">
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

<span id="77973"></span>

<div id="answer-container-77973" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77973-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dykay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Format strings are a nice way to solve this problem:</p>
<p><a href="https://docs.python.org/3.4/library/string.html#format-string-syntax">https://docs.python.org/3.4/library/string.html#format-string-syntax</a></p>
<p>I'd suggest using keywords so that you don't have to remember what order to pass in the values, so</p>
<pre><code>&quot;&quot;&quot;way(around:5, {lat}, {long})...&quot;&quot;&quot;.format(lat=lat,long=long)</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '20, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-77973" class="comments-container">
<span id="77975"></span>
<div id="comment-77975" class="comment">
<div id="post-77975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a></p>
</div>
<div id="comment-77975-info" class="comment-info">
<span class="comment-age">(17 Dec '20, 17:52)</span> <span class="comment-user userinfo">Dykay</span>
</div>
</div>
</div>
<div id="comment-tools-77973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77973-form-container" class="comment-form-container">
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

