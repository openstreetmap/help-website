+++
type = "question"
title = "Import relation with no geometry using flex"
description = '''Is there a way to import a relation using the flex style when that relation doesn&#x27;t have any related geometry data? I&#x27;m trying to import a list of ski resorts in Scotland but one is not being imported correctly. I&#x27;ve done some digging and found that there is a relation which has a lot of ways as mem...'''
date = "2022-08-24T15:15:00Z"
lastmod = "2022-08-26T14:34:00Z"
weight = 85433
keywords = [ "flex", "osm2pgsql", "lua" ]
aliases = [ "/questions/85433" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Import relation with no geometry using flex](/questions/85433/import-relation-with-no-geometry-using-flex)

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
<span id="post-85433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85433-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to import a relation using the flex style when that relation doesn't have any related geometry data?</p>
<p>I'm trying to import a list of ski resorts in Scotland but one is not being imported correctly. I've done some digging and found that there is a relation which has a lot of ways as members, allowing me to group all those ways, but as there is no geometry field associated with that relation it doesn't appear in the database after I call add_row.</p>
<p>In a reduced test case I've found that if I remove the geometry field from the relevant database table, the relation is added correctly.</p>
<p>inspect = require('inspect')</p>
<p>local tables = {}</p>
<p>tables.relations_test = osm2pgsql.define_table({ name = 'relations_test', ids = { type = 'area', id_column = "id"}, columns = { { column = 'name', type = 'text' }, --{ column = 'geom', type = 'geometry' }, } })</p>
<p>function osm2pgsql.process_relation(object) if object:grab_tag('type') == "site" then</p>
<pre><code>    print(&quot;Matched rel &quot;, object.id, object.tags.name)
&#10;    tables.relations_test:add_row({
        name = object.tags.name,
      --  geom = { create = &#39;area&#39; },
    })
&#10;end</code></pre>
<p>end If I remove the commented out lines in the above, my relation is not imported into the table. This suggests to me that each row requires a geometry.</p>
<p>If there any way to maintain the geometry field in the row (it's populated for other relations and ways) but allow it to be NULL?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-flex" rel="tag" title="see questions tagged &#39;flex&#39;">flex</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '22, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0d0a44946fe28018053741f5a225e569?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarkSnow&#39;s gravatar image" />
<p><span>DarkSnow</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarkSnow has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85433" class="comments-container">
&#10;</div>
<div id="comment-tools-85433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85433-form-container" class="comment-form-container">
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

<span id="85437"></span>

<div id="answer-container-85437" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85437-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-85437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DarkSnow has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not possible to have an empty geometry column with the <code>add_row()</code> function, it will be filtered out as you noticed. Luckily we have just recently released version 1.7.0 which has a new <code>import()</code> function which does basically the same as <code>add_row()</code>, but has "less magic" built in. If you don't have a geometry, it will happily add a NULL into that column (unless you declare the column as <code>NOT NULL</code>). See the <a href="https://osm2pgsql.org/doc/manual.html#the-insert-function">osm2pgsql manual for details</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '22, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-85437" class="comments-container">
&#10;</div>
<div id="comment-tools-85437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85437-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85448"></span>

<div id="answer-container-85448" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85448-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's perfect Jochen, I've compiled the new version of osm2pgsql and I can now get the relation with a NULL geometry.</p>
<p>Perfect timing on the new version.</p>
<p>Thanks for the help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '22, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0d0a44946fe28018053741f5a225e569?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarkSnow&#39;s gravatar image" />
<p><span>DarkSnow</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarkSnow has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85448" class="comments-container">
&#10;</div>
<div id="comment-tools-85448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85448-form-container" class="comment-form-container">
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

