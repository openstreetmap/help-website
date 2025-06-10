+++
type = "question"
title = "osm2pgsql: processing diff files"
description = '''Hi, When processing diff files (*.osc) how are changes sent to postgres? I assume it&#x27;s via a delete and an insert, because when splitting long lines and multipolygons you don&#x27;t have an unique id. If I make my tables have a primary key (osm_id) and not splitting long lines and multipolygons are the c...'''
date = "2021-06-15T13:33:00Z"
lastmod = "2021-06-16T08:18:00Z"
weight = 80582
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/80582" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql: processing diff files](/questions/80582/osm2pgsql-processing-diff-files)

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
<span id="post-80582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80582-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>When processing diff files (*.osc) how are changes sent to postgres? I assume it's via a delete and an insert, because when splitting long lines and multipolygons you don't have an unique id.</p>
<p>If I make my tables have a primary key (osm_id) and not splitting long lines and multipolygons are the changes then sent to postgres as an update statement?</p>
<p>Paul</p>
<p>Edit: to clarify, I want to add some filtering (current way I'm exploring is through triggers on the postgres tables) so I can expire tiles only when relevant changes appear. If the changes are done through delete and insert I can't compare them to see if anything interesting changed. If this isn't going to work, is it possible then in a lua script (flex-output)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '21, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/31d950f81ca152c66d5ed83bb7c53950?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paulosm2016&#39;s gravatar image" />
<p><span>Paulosm2016</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paulosm2016 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jun '21, 14:55</strong> </span></p>
</div>
</div>
<div id="comments-container-80582" class="comments-container">
&#10;</div>
<div id="comment-tools-80582" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80582-form-container" class="comment-form-container">
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

<span id="80587"></span>

<div id="answer-container-80587" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80587-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osm2pgsql currently always uses DELETE to remove the old versions of objects and then COPY to insert the new versions, so you can use ON DELETE and ON INSERT triggers. (But note that this behaviour might change in the future.) This is independent of whether ids are unique or not (even without line /multipolygon splitting).</p>
<p>It is a bit complicated but you could probably use the ON DELETE trigger to copy the data about to be deleted to an extra table and then use the ON INSERT trigger to do the comparison with the old data. I can't think of any other way to do what you want. The Lua script can't see the old version of the data, so it can't do any comparison.</p>
<p>The developers are aware that the expire functionality isn't as good as it could be and making expiry better and more flexible is on the todo list, but it could take a while to get that done. I suggest you start a <a href="https://github.com/openstreetmap/osm2pgsql/discussions">discussion</a>, though so that your use case is considered when working on this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '21, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-80587" class="comments-container">
<span id="80594"></span>
<div id="comment-80594" class="comment">
<div id="post-80594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a variant of this you can also just not do the DELETE (ie. the trigger can signal the database it should not do it, I believe by returning NULL from the BEFORE DELETE trigger function). Then do the DELETE yourself in the BEFORE INSERT function after doing the comparison with the original data.</p>
</div>
<div id="comment-80594-info" class="comment-info">
<span class="comment-age">(16 Jun '21, 08:18)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-80587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80587-form-container" class="comment-form-container">
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

