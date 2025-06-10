+++
type = "question"
title = "Overpass turbo: runtime error: Query timed out in &quot;query&quot; - What to do?"
description = '''I like to download all places(nodes) which are tagged in osm with highway&quot;=&quot;services and which contains &quot;Raststätte&quot; in the name value, which have a maximal distance to a motorway of 100 meter. When I run my query on a smaller area it work fine but with this I get a error message like this: An error...'''
date = "2017-04-12T10:49:00Z"
lastmod = "2017-04-12T11:30:00Z"
weight = 55579
keywords = [ "overpass-turbo", "timeout" ]
aliases = [ "/questions/55579" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass turbo: runtime error: Query timed out in "query" - What to do?](/questions/55579/overpass-turbo-runtime-error-query-timed-out-in-query-what-to-do)

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
<span id="post-55579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55579-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I like to download all places(nodes) which are tagged in osm with highway"="services and which contains "Raststätte" in the name value, which have a maximal distance to a motorway of 100 meter.</p>
<p>When I run my query on a smaller area it work fine but with this I get a error message like this:</p>
<pre><code>An error occured during the execution of the overpass query! This is what overpass API returned:
&#10;runtime error: Query timed out in &quot;query&quot; at line 17 after 199 seconds.</code></pre>
<p>Below is my querry:</p>
<pre><code>[bbox:45.0,4.7,50.2,9.3];
&#10;(
&#10;  node[&quot;name&quot;~&quot;Raststätte&quot;];   (way[&quot;name&quot;~&quot;Raststätte&quot;];&gt;;);   (relation[&quot;name&quot;~&quot;Raststätte&quot;];&gt;;);
     node[&quot;highway&quot;=&quot;services&quot;];   (way[&quot;highway&quot;=&quot;services&quot;];&gt;;);   (relation[&quot;highway&quot;=&quot;services&quot;];&gt;;); )-&gt;.rasten;
&#10;way(around.rasten:100)[&quot;highway&quot;=&quot;motorway&quot;]
-&gt;.motorway;
&#10;( node.rasten(around.motorway:100);   way.rasten(around.motorway:100);   rel.rasten(around.motorway:100);  )-&gt;.matchingRasten;
&#10;(.matchingRasten;); out body; (._;&gt;;); out skel qt;</code></pre>
<p>What possibility I have to solve this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '17, 10:49</strong></p>
<img src="https://secure.gravatar.com/avatar/115ebdce3a1373428dcaca9f66b80fa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ino_oni&#39;s gravatar image" />
<p><span>ino_oni</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ino_oni has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>16 Apr '17, 13:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span></p>
</div>
</div>
<div id="comments-container-55579" class="comments-container">
&#10;</div>
<div id="comment-tools-55579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55579-form-container" class="comment-form-container">
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

<span id="55580"></span>

<div id="answer-container-55580" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55580-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ino_oni has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You get to much hits on your query, this leads to it timing out. The solution is to increase the timeout like so</p>
<p><code>[timeout:50];</code></p>
<p>Have a look <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Simple_usage_examples">here</a> for some examples</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '17, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '17, 11:01</strong> </span></p>
</div>
</div>
<div id="comments-container-55580" class="comments-container">
<span id="55582"></span>
<div id="comment-55582" class="comment">
<div id="post-55582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>perfect. Because of another problem I needed to use <a href="http://overpass-api.de/query_form.html">http://overpass-api.de/query_form.html</a> but its exactly I was looking for</p>
</div>
<div id="comment-55582-info" class="comment-info">
<span class="comment-age">(12 Apr '17, 11:30)</span> <span class="comment-user userinfo">ino_oni</span>
</div>
</div>
</div>
<div id="comment-tools-55580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55580-form-container" class="comment-form-container">
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

