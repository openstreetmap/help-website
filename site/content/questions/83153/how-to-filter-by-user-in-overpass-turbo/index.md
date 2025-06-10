+++
type = "question"
title = "How to filter by user in overpass turbo"
description = '''I want to see a particular feature mapped by a given user, and the opposite (mapped by other users different to a given one). However, I see that the user value is in the Meta section, and I cannot write a query to filter by this criterion. This is the original query, to get all monitoring stations ...'''
date = "2022-01-22T19:51:00Z"
lastmod = "2022-01-22T21:23:00Z"
weight = 83153
keywords = [ "filter", "overpass", "overpass-turbo", "user", "query" ]
aliases = [ "/questions/83153" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter by user in overpass turbo](/questions/83153/how-to-filter-by-user-in-overpass-turbo)

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
<span id="post-83153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83153-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to see a particular feature mapped by a given user, and the opposite (mapped by other users different to a given one). However, I see that the user value is in the Meta section, and I cannot write a query to filter by this criterion.</p>
<p>This is the original query, to get all monitoring stations in Colombia:</p>
<pre><code>[out:xml][timeout:25];
area[name=&quot;Colombia&quot;][admin_level=2][boundary=administrative]-&gt;.searchColombia;
(
  nwr[&quot;man_made&quot;=&quot;monitoring_station&quot;](area.searchColombia);
);
out meta;
&gt;;
out meta qt;</code></pre>
<p>However, I know that the user dcruizr has worked a lot on this, and I do not want to see her contributions. I was thinking about something like:</p>
<pre><code>[out:xml][timeout:25];
area[name=&quot;Colombia&quot;][admin_level=2][boundary=administrative]-&gt;.searchColombia;
(
  nwr[&quot;man_made&quot;=&quot;monitoring_station&quot;][user!=&quot;dcruizr&quot;](area.searchColombia);
);
out meta;
&gt;;
out meta qt;</code></pre>
<p>However, this does not do any filter on the data. How can I write a query to filter by user?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '22, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/6998587ec6de0bab814c70777bcdd2ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AngocA&#39;s gravatar image" />
<p><span>AngocA</span><br />
<span class="score" title="281 reputation points">281</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AngocA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83153" class="comments-container">
&#10;</div>
<div id="comment-tools-83153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83153-form-container" class="comment-form-container">
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

<span id="83156"></span>

<div id="answer-container-83156" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83156-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-83156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AngocA has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As an update to DaveF's answer, you now can negatively filter for users:</p>
<pre><code>area[name=Colombia][admin_level=2];
nwr[man_made=monitoring_station](area)(if:user()!=&quot;dcruizr&quot;);
out meta;
&gt;;
out meta qt;</code></pre>
<p>The <code>if</code> conditional allows for free-form boolean operations. The only restriction is that <a href="https://dev.overpass-api.de/overpass-doc/en/criteria/misc_criteria.html#count">it only works in combination</a> with another conditional, because one otherwise could too easily ask accidentally for the whole planet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '22, 21:23</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-83156" class="comments-container">
&#10;</div>
<div id="comment-tools-83156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83156-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83154"></span>

<div id="answer-container-83154" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83154-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-83154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's irritating we can't negate user's input directly in overpass.</p>
<p>The Data variable is used so the search for the user is only performed on the monitoring_stations returned &amp; not the whole of Columbia, speeding it up slightly.</p>
<p>Note <code>user</code> uses a colon, not an equals sign.</p>
<p><a href="https://overpass-turbo.eu/s/1fjq">https://overpass-turbo.eu/s/1fjq</a></p>
<pre><code>area[name=Colombia][admin_level=2];
(
 nwr[man_made=monitoring_station](area)-&gt;.Data;
 -nwr.Data(user:dcruizr);
);
out meta;
&gt;;
out meta qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '22, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '22, 20:45</strong> </span></p>
</div>
</div>
<div id="comments-container-83154" class="comments-container">
<span id="83155"></span>
<div id="comment-83155" class="comment">
<div id="post-83155-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for your answer. I'm just adding an extra answer, because there are more semantics available now.</p>
</div>
<div id="comment-83155-info" class="comment-info">
<span class="comment-age">(22 Jan '22, 21:15)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-83154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83154-form-container" class="comment-form-container">
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

