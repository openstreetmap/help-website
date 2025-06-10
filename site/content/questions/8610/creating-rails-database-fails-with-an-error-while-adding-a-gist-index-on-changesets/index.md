+++
type = "question"
title = "Creating rails database fails with an error while adding a GIST index on changesets?"
description = '''I&#x27;m trying to install the rail port.  THis is the command i received an error.  env RAILS_ENV=production rake db:migrate  This is my error: -- add_index(&quot;changesets&quot;, [&quot;min_lat&quot;, &quot;max_lat&quot;, &quot;min_lon&quot;, &quot;max_lon&quot;], {:method=&amp;gt;&quot;GIST&quot;, :name=&amp;gt;&quot;changesets_bbox_idx&quot;}) rake aborted! An error has occur...'''
date = "2011-10-24T09:15:00Z"
lastmod = "2011-10-25T08:19:00Z"
weight = 8610
keywords = [ "gist", "rails" ]
aliases = [ "/questions/8610" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Creating rails database fails with an error while adding a GIST index on changesets?](/questions/8610/creating-rails-database-fails-with-an-error-while-adding-a-gist-index-on-changesets)

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
<span id="post-8610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8610-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-8610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to install the rail port. THis is the command i received an error.<br />
<code>env RAILS_ENV=production rake db:migrate</code></p>
<p>This is my error:<br />
</p>
<pre><code>-- add_index(&quot;changesets&quot;, [&quot;min_lat&quot;, &quot;max_lat&quot;, &quot;min_lon&quot;, &quot;max_lon&quot;], {:method=&gt;&quot;GIST&quot;, :name=&gt;&quot;changesets_bbox_idx&quot;})
rake aborted!
An error has occurred, this and all later migrations canceled:
PGError: ERROR:  data type integer has no default operator class for access method &quot;gist&quot;
HINT:  You must specify an operator class for the index or define a default operator class for the data type.
: CREATE  INDEX &quot;changesets_bbox_idx&quot; ON &quot;changesets&quot; USING GIST (&quot;min_lat&quot;, &quot;max_lat&quot;, &quot;min_lon&quot;, &quot;max_lon&quot;)
Tasks: TOP =&gt; db:migrate
(See full trace by running task with --trace)</code></pre>
<p>I tried deleting the databases and create them all over again but i still get this error. I'm 100% sure i didn't missed the <code>psql -d openstreetmap &lt; /usr/share/postgresql/8.4/contrib/btree_gist.sql</code> part.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gist" rel="tag" title="see questions tagged &#39;gist&#39;">gist</span> <span class="post-tag tag-link-rails" rel="tag" title="see questions tagged &#39;rails&#39;">rails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '11, 09:15</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '11, 14:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-8610" class="comments-container">
&#10;</div>
<div id="comment-tools-8610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8610-form-container" class="comment-form-container">
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

<span id="8617"></span>

<div id="answer-container-8617" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8617-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well I'm 100% sure that you did miss that step, as that is exactly the error you will get if you haven't added that contrib module.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '11, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-8617" class="comments-container">
<span id="8618"></span>
<div id="comment-8618" class="comment">
<div id="post-8618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@Tomh</span>, thanks for your input! I tried it once more to configure my db, beginning with table creation. This is my full copy-paste result from the terminal to demonstrate that the error still persists. <a href="http://pastebin.com/VMvsNk9S">http://pastebin.com/VMvsNk9S</a></p>
</div>
<div id="comment-8618-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 15:06)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8620"></span>
<div id="comment-8620" class="comment">
<div id="post-8620-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So you have created three databases, but have only installed the btree_gist code in one of them. Presumably a different one to the one you are migrating, but I would need to see your database.yml to be sure.</p>
</div>
<div id="comment-8620-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 15:08)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
<span id="8631"></span>
<div id="comment-8631" class="comment">
<div id="post-8631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! That worked. I didn't realise i had to execute that command for every db. But i have an error with osmosis now. If you are competent with it and want to help out, please see this post <a href="http://help.openstreetmap.org/questions/8630/osmosis-stops-with-error-insert-or-update-on-table-current_way_nodes-violates-foreign-key-constraint-current_way_nodes_node_id_fkey">http://help.openstreetmap.org/questions/8630/osmosis-stops-with-error-insert-or-update-on-table-current_way_nodes-violates-foreign-key-constraint-current_way_nodes_node_id_fkey</a></p>
</div>
<div id="comment-8631-info" class="comment-info">
<span class="comment-age">(25 Oct '11, 08:19)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8617-form-container" class="comment-form-container">
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

