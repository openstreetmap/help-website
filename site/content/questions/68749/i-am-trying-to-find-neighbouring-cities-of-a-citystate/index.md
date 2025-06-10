+++
type = "question"
title = "I am trying to find neighbouring cities of a city/state."
description = '''I am very new to overpass api. I am trying to find a way to get nearby cities.  i,e if I enter a city or a state, I should be able to get cities within that input area. And as an option, I want to filter the results for a specific country.  I have tried several ways. But none of them seems to work. ...'''
date = "2019-04-10T17:08:00Z"
lastmod = "2019-04-10T18:08:00Z"
weight = 68749
keywords = [ "overpassapi", "overpass", "query", "area" ]
aliases = [ "/questions/68749" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I am trying to find neighbouring cities of a city/state.](/questions/68749/i-am-trying-to-find-neighbouring-cities-of-a-citystate)

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
<span id="post-68749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am very new to overpass api. I am trying to find a way to get nearby cities. i,e if I enter a city or a state, I should be able to get cities within that input area. And as an option, I want to filter the results for a specific country. I have tried several ways. But none of them seems to work.</p>
<pre><code>[out:json];area[&quot;name&quot;=&quot;India&quot;][admin_level=2];area[&quot;name&quot;=&quot;Kerala&quot;][&quot;border_type&quot;=&quot;state&quot;];(node[&quot;place&quot;=&quot;city&quot;][&quot;name&quot;=&quot;Cochin&quot;](area);)-&gt;.center;node(around:10000)[&quot;place&quot;];out;</code></pre>
<p>Here India is the country Kerala is a state of the country And Cochin is a city inside that state. So I am trying to find the nearby cities of Cochin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '19, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a151e43c2c6d85c3670efb4a7c6307b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zudheer&#39;s gravatar image" />
<p><span>zudheer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zudheer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68749" class="comments-container">
&#10;</div>
<div id="comment-tools-68749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68749-form-container" class="comment-form-container">
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

<span id="68750"></span>

<div id="answer-container-68750" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68750-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Zudheer, you might want to take a look at overpass-turbo, it has a wizard (see menu-button on the top) which translates easy words to queries, great for experimenting and learning. I'Ve made you a quick example here -&gt;</p>
<p><a href="https://overpass-turbo.eu/s/HSo">https://overpass-turbo.eu/s/HSo</a></p>
<p>On a little side-note, I think it'S safe to say this code:</p>
<pre><code>  node[&quot;place&quot;=&quot;city&quot;](area.searchArea);
  way[&quot;place&quot;=&quot;city&quot;](area.searchArea);
  relation[&quot;place&quot;=&quot;city&quot;](area.searchArea);</code></pre>
<p>can be shortened by:</p>
<pre><code>nwr[&quot;place&quot;=&quot;city&quot;](area.searchArea);</code></pre>
<p>Hope it helped!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '19, 18:08</strong></p>
<img src="https://secure.gravatar.com/avatar/89858e1d0e500ae658bf8cf7fc4964c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tijmenheid&#39;s gravatar image" />
<p><span>tijmenheid</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tijmenheid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68750" class="comments-container">
&#10;</div>
<div id="comment-tools-68750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68750-form-container" class="comment-form-container">
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

