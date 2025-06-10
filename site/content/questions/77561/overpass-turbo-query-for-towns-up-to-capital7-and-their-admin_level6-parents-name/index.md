+++
type = "question"
title = "Overpass-turbo query for towns up to capital=7 and their admin_level=6 parents name"
description = '''I&#x27;m trying to output a file in Overpass Turbo, let&#x27;s assume CSV (because it seems easier to accomplish this with CSV), with:  All nodes in Portugal where the tag capital=yes or capital=1 or (...) or capital=7 For all those nodes, output the following information: name (tag), capital (tag) and coordi...'''
date = "2020-11-15T23:59:00Z"
lastmod = "2020-11-17T19:57:00Z"
weight = 77561
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/77561" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass-turbo query for towns up to capital=7 and their admin_level=6 parents name](/questions/77561/overpass-turbo-query-for-towns-up-to-capital7-and-their-admin_level6-parents-name)

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
<span id="post-77561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77561-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to output a file in Overpass Turbo, let's assume CSV (because it seems easier to accomplish this with CSV), with:</p>
<ul>
<li>All nodes in Portugal where the tag capital=yes <em>or</em> capital=1 <em>or</em> <strong>(...)</strong> <em>or</em> capital=7</li>
<li>For all those nodes, output the following information: name (tag), capital (tag) and coordinates <strong>and</strong> find the rel with the tag border_type=distrito (or admin_level=6) they belong to, and output it's <em>name</em> as well.</li>
</ul>
<p>Example output:</p>
<table>
<tbody>
<tr>
<th>name</th>
<th>capital</th>
<th>lat</th>
<th>lng</th>
<th>parent</th>
</tr>
&#10;<tr>
<td>City_1</td>
<td>7</td>
<td>38.123</td>
<td>-9.123</td>
<td>County_1</td>
</tr>
<tr>
<td>City_2</td>
<td>2</td>
<td>38.123</td>
<td>-9.123</td>
<td>County_1</td>
</tr>
<tr>
<td>City_3</td>
<td>4</td>
<td>38.123</td>
<td>-9.123</td>
<td>County_2</td>
</tr>
<tr>
<td>City_4</td>
<td>4</td>
<td>38.123</td>
<td>-9.123</td>
<td>County_3</td>
</tr>
<tr>
<td>City_5</td>
<td>4</td>
<td>38.123</td>
<td>-9.123</td>
<td>County_2</td>
</tr>
</tbody>
</table>
<p><br />
</p>
<p>I've managed to output all info correctly except for the parent information, with this Overpass Turbo query:</p>
<pre><code>[out:csv(name,capital,::lat,::lon;true;&quot;;&quot;)][timeout:250];
{{geocodeArea:Portugal}}-&gt;.searchArea;
&#10;(
  node[&quot;capital&quot;=&quot;yes&quot;](area.searchArea);
  node[&quot;capital&quot;=&quot;1&quot;](area.searchArea);
  node[&quot;capital&quot;=&quot;2&quot;](area.searchArea);
  node[&quot;capital&quot;=&quot;3&quot;](area.searchArea);
  node[&quot;capital&quot;=&quot;4&quot;](area.searchArea);
  node[&quot;capital&quot;=&quot;5&quot;](area.searchArea);
  node[&quot;capital&quot;=&quot;6&quot;](area.searchArea);
  node[&quot;capital&quot;=&quot;7&quot;](area.searchArea);
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>However, I'm having a hard time figuring out how to get which admin_level=6 each place belongs to. Any help would be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '20, 23:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a9c6d8a55e23491c53237acfefe6abe5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FSeixasPT&#39;s gravatar image" />
<p><span>FSeixasPT</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FSeixasPT has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-77561" class="comments-container">
&#10;</div>
<div id="comment-tools-77561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77561-form-container" class="comment-form-container">
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

<span id="77581"></span>

<div id="answer-container-77581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77581-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Unsure if it's possible, but try looking at recursion (to get the relation on the way) &amp; the 'for' block command in the wiki &amp; here: <a href="https://dev.overpass-api.de/blog/index.html">https://dev.overpass-api.de/blog/index.html</a> (unfortunately it's isn't searchable. you'll have to go through each page individually)</p>
<p>Compacted version of your routine using RegEx:</p>
<pre><code>[out:csv(name,capital,::lat,::lon;true;&quot;;&quot;)];
{{geocodeArea:Portugal}};
node[capital~&quot;yes|[1-7]&quot;](area);
out meta;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '20, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '20, 20:02</strong> </span></p>
</div>
</div>
<div id="comments-container-77581" class="comments-container">
&#10;</div>
<div id="comment-tools-77581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77581-form-container" class="comment-form-container">
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

