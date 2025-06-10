+++
type = "question"
title = "How to exclude a &quot;user:&quot; in an Overpass Wizard query"
description = '''This overpass-turbo wizard query works, but I want the negation user:&quot;MassGIS Import&quot; and type:way and highway=* in &quot;Boylston,Massachusetts&quot; I&#x27;ve tried  -user:&quot;MassGIS Import&quot; user:!&quot;MassGIS Import&quot; user:!=&quot;MassGIS Import&quot;'''
date = "2016-08-27T13:57:00Z"
lastmod = "2016-08-27T14:33:00Z"
weight = 51749
keywords = [ "overpass", "negation", "query" ]
aliases = [ "/questions/51749" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to exclude a "user:" in an Overpass Wizard query](/questions/51749/how-to-exclude-a-user-in-an-overpass-wizard-query)

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
<span id="post-51749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51749-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This overpass-turbo wizard query works, but I want the negation</p>
<p><strong>user:"MassGIS Import" and type:way and highway=* in "Boylston,Massachusetts"</strong></p>
<p>I've tried</p>
<p>-user:"MassGIS Import"</p>
<p>user:!"MassGIS Import"</p>
<p>user:!="MassGIS Import"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-negation" rel="tag" title="see questions tagged &#39;negation&#39;">negation</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '16, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/75cc9956f060892f585352e9011cd26e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan01730&#39;s gravatar image" />
<p><span>Alan01730</span><br />
<span class="score" title="464 reputation points">464</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan01730 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51749" class="comments-container">
&#10;</div>
<div id="comment-tools-51749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51749-form-container" class="comment-form-container">
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

<span id="51750"></span>

<div id="answer-container-51750" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51750-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass turbo wizard does not support negative user queries. You need to manually set up your query using the <em>difference</em> statement:</p>
<pre><code>[out:json][timeout:25];
{{geocodeArea:Boylston,Massachusetts}}-&gt;.searchArea;
(
  way[&quot;highway&quot;](area.searchArea); - 
  way(user:&quot;MassGIS Import&quot;)[&quot;highway&quot;](area.searchArea);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>Try it in overpass turbo: <a href="http://overpass-turbo.eu/s/i3c">http://overpass-turbo.eu/s/i3c</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '16, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-51750" class="comments-container">
<span id="51751"></span>
<div id="comment-51751" class="comment">
<div id="post-51751-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Great answer, works like a charm. You've nudged me just enough that I'll be digging deeper into overpass. I was trying to avoid that!!!</p>
</div>
<div id="comment-51751-info" class="comment-info">
<span class="comment-age">(27 Aug '16, 14:33)</span> <span class="comment-user userinfo">Alan01730</span>
</div>
</div>
</div>
<div id="comment-tools-51750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51750-form-container" class="comment-form-container">
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

