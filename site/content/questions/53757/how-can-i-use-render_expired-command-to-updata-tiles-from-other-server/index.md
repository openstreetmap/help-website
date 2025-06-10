+++
type = "question"
title = "How can i use render_expired command to updata tiles from other server?"
description = '''If my rails port and tile server built on two different hosts, called s1 and s2. Now i make an edit at the openstreetmap database on s1, can i use the render_expired command on the s1 host to updata tiles on the s2 host? If it is feasible, how to set the config to make render_expired command renderd...'''
date = "2016-12-30T13:36:00Z"
lastmod = "2017-01-03T13:03:00Z"
weight = 53757
keywords = [ "render_list", "renderd", "mod_tile" ]
aliases = [ "/questions/53757" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can i use render_expired command to updata tiles from other server?](/questions/53757/how-can-i-use-render_expired-command-to-updata-tiles-from-other-server)

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
<span id="post-53757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53757-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If my rails port and tile server built on two different hosts, called s1 and s2. Now i make an edit at the openstreetmap database on s1, can i use the render_expired command on the s1 host to updata tiles on the s2 host? If it is feasible, how to set the config to make render_expired command renderd the specifiled host and database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '16, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '17, 02:42</strong> </span></p>
</div>
</div>
<div id="comments-container-53757" class="comments-container">
&#10;</div>
<div id="comment-tools-53757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53757-form-container" class="comment-form-container">
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

<span id="53760"></span>

<div id="answer-container-53760" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53760-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'd need to write some code to do that, I think. The usual mechanism (with a rendering server consuming diffs from OSM.org) is:</p>
<ol>
<li>You change some data on osm.org</li>
<li>That change is written to a diff</li>
<li>Your rendering server periodically runs "openstreetmap-tiles-update-expire"</li>
<li>That consumes pending diffs, generates a list of changed tiles and calls render_expired</li>
</ol>
<p>That process means that data that has changed on the rails port is used to update the rendering server database <em>and</em> the rendering server can choose to expire (or rerender) the affected tiles.</p>
<p>Given that the rails port and rendering server are separate databases anyway, and you'll need to do something to get changed data from one into the other (such as processing diffs) why not just use those diffs to drive rerendering? I'm sure it would be technically possible to link rerendering to <em>editing</em> instead, but it doesn't actually achieve anything different in the long run.</p>
<p>If it helps, I have variations on tile expiry scripts <a href="https://github.com/SomeoneElseOSM/mod_tile/blob/master/openstreetmap-tiles-update-expire#L165">here</a> and <a href="https://github.com/SomeoneElseOSM/mod_tile/blob/master/openstreetmap-tiles-update-rerender#L165">here</a> that have a few more comments explaining tile expiry usage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '16, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53760" class="comments-container">
<span id="53774"></span>
<div id="comment-53774" class="comment">
<div id="post-53774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, i didn't express well. The rails port and rendering server are separate databases, they also built on separate host, the rails port on the s1 host, and rendering server on the s2 host, can i use the render_expired command on the s1 host to updata tiles on the s2 host?</p>
</div>
<div id="comment-53774-info" class="comment-info">
<span class="comment-age">(31 Dec '16, 12:08)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="53829"></span>
<div id="comment-53829" class="comment">
<div id="post-53829-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not easily - it communicates with the renderer via a socket. Easier to get the list of tiles from s1 to s2 and run render_expired on s2.</p>
</div>
<div id="comment-53829-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 13:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53760-form-container" class="comment-form-container">
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

