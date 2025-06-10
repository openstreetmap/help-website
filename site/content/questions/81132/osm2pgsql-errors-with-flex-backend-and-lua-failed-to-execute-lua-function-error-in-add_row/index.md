+++
type = "question"
title = "Osm2pgsql errors with flex backend and Lua. Failed to execute Lua function [...] Error in &#x27;add_row&#x27;"
description = '''I am currently running a postgres DB in a docker container. I want to upload a small pbf file usinf osm2pgsql using the new flex-backend. However i&#x27;m runing into problems with Lua. My osm command: osm2pgsql -d osm -U osm2pgsql -H XXX.XX.XX.XXX -P 5432 -c pbf_files/district-of-columbia-latest.osm.pbf...'''
date = "2021-07-30T18:49:00Z"
lastmod = "2021-07-31T07:40:00Z"
weight = 81132
keywords = [ "lua", "osm2pgsql" ]
aliases = [ "/questions/81132" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osm2pgsql errors with flex backend and Lua. Failed to execute Lua function \[...\] Error in 'add_row'](/questions/81132/osm2pgsql-errors-with-flex-backend-and-lua-failed-to-execute-lua-function-error-in-add_row)

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
<span id="post-81132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81132-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently running a postgres DB in a docker container. I want to upload a small pbf file usinf osm2pgsql using the new flex-backend. However i'm runing into problems with Lua.</p>
<p>My osm command:</p>
<p>osm2pgsql -d osm -U osm2pgsql -H XXX.XX.XX.XXX -P 5432 -c pbf_files/district-of-columbia-latest.osm.pbf -W -O flex -S flex-config/unitable.lua --flat-nodes flat-nodes --keep-coastlines --cache 30000 --hstore --hstore-add-index --tablespace-index pg_default --number-processes 8 --cache-strategy dense --extra-attributes --slim</p>
<p>The error message: 2021-07-30 17:30:52 node cache: stored: 3(100.00%), storage efficiency: 0.02% (dense blocks: 2, sparse nodes: 0), hit rate: 0.00% 2021-07-30 17:30:52 ERROR: Failed to execute Lua function 'osm2pgsql.process_node': flex-config/unitable.lua:42: Error in 'add_row': Invalid type 'table' for text column.</p>
<p>stack traceback: [C]: in method 'add_row' flex-config/unitable.lua:42: in function 'process' flex-config/unitable.lua:53: in function &lt;flex-config unitable.lua:52=""&gt;.</p>
<p>I can run the upload with the default backend and I've tried all default templates provided by osm2pgsql but know of them work, they all return the same error.</p>
<p>Would greatly appreciate some help. Chris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '21, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a552a23b3f38276d0a5fff44687838b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrisvreug&#39;s gravatar image" />
<p><span>chrisvreug</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrisvreug has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81132" class="comments-container">
&#10;</div>
<div id="comment-tools-81132" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81132-form-container" class="comment-form-container">
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

<span id="81135"></span>

<div id="answer-container-81135" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81135-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are using an older version of osm2pgsql (before 1.5.0) with a config file (unitable.lua) that is made for osm2pgsql 1.5.0 or greater. Update your osm2pgsql to 1.5.1 or use an older version of the unitable.lua file.</p>
<p>Also: Check your command line. Many of the options you are using don't do anything when the <code>flex</code> output is used, so you should probably get rid of them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '21, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-81135" class="comments-container">
&#10;</div>
<div id="comment-tools-81135" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81135-form-container" class="comment-form-container">
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

