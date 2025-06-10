+++
type = "question"
title = "All places in the world with the same name... search?"
description = '''Hello community, I wondered if anyone could tell me if it is possible to find a list of all the places in the world that are named after a specific person? The person in question is Italian, so there are various &#x27;corso&#x27;, &#x27;piazza&#x27;, &#x27;via&#x27; + name in Italy but I would like to search globally and export ...'''
date = "2016-10-31T18:38:00Z"
lastmod = "2016-10-31T22:35:00Z"
weight = 52764
keywords = [ "streetnames", "names" ]
aliases = [ "/questions/52764" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [All places in the world with the same name... search?](/questions/52764/all-places-in-the-world-with-the-same-name-search)

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
<span id="post-52764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52764-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello community,</p>
<p>I wondered if anyone could tell me if it is possible to find a list of all the places in the world that are named after a specific person? The person in question is Italian, so there are various 'corso', 'piazza', 'via' + name in Italy but I would like to search globally and export that data. I feel like it should be easy but I'm new to the world of mapping...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '16, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/7d696979fe885cb97b9fe1b7b5ec6576?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amy%20K&#39;s gravatar image" />
<p><span>Amy K</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amy K has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52764" class="comments-container">
&#10;</div>
<div id="comment-tools-52764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52764-form-container" class="comment-form-container">
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

<span id="52768"></span>

<div id="answer-container-52768" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52768-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many ways to achieve this. You could download the OSM data for the whole world - the so-called "planet file" - and then use a search program on that (for example <code>osmgrp</code>) or load the data into a database and search there. That would give you the maximum flexibility but take a lot of time and resources.</p>
<p>Another option is the "overpass turbo" database which lets you make certain queries directly to a server without having to load the data yourself. A query for "anything where the name contains 'Botticelli'" would look like this:</p>
<pre><code>[out:json][timeout:25];
(
  node[&quot;name&quot;~&quot;Botticelli&quot;];
  way[&quot;name&quot;~&quot;Botticelli&quot;];
  relation[&quot;name&quot;~&quot;Botticelli&quot;];
);
out body;
&gt;;
out skel qt;</code></pre>
<p><a href="http://overpass-turbo.eu/s/jKW">Try it out!</a></p>
<p>If you read up a bit on Overpass Turbo you will be able to refine your query to, for example, query only for buildings or only for streets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '16, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52768" class="comments-container">
&#10;</div>
<div id="comment-tools-52768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52768-form-container" class="comment-form-container">
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

