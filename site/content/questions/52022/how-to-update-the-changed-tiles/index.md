+++
type = "question"
title = "How to update the changed tiles?"
description = '''I have installed the rails port and tile server, if i make an edit at my local map, and use osmosis command to keep the tile server database consistent with the rails port database, then how can i update the tiles that has been edited? Each time i want to see the changes, i have to clear up the cook...'''
date = "2016-09-13T07:38:00Z"
lastmod = "2016-09-13T11:15:00Z"
weight = 52022
keywords = [ "tiles", "mod_tile", "tileserver" ]
aliases = [ "/questions/52022" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to update the changed tiles?](/questions/52022/how-to-update-the-changed-tiles)

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
<span id="post-52022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52022-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed the rails port and tile server, if i make an edit at my local map, and use osmosis command to keep the tile server database consistent with the rails port database, then how can i update the tiles that has been edited? Each time i want to see the changes, i have to clear up the cookies on the website and remove the /var/lib/mod_tile/default directory in the vm, then re-run the renderd command. But this method can't be the proper solution, so what is the correct way to update the changed tiles?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '16, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-52022" class="comments-container">
&#10;</div>
<div id="comment-tools-52022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52022-form-container" class="comment-form-container">
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

<span id="52026"></span>

<div id="answer-container-52026" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52026-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yuyy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're using <a href="https://github.com/openstreetmap/mod_tile/"><code>mod_tile</code></a> then there's a <a href="https://github.com/openstreetmap/mod_tile/blob/master/openstreetmap-tiles-update-expire">script</a> that comes with that that calls osmosis to update a rendering database based on "minutely diffs" and also expires tiles based on those updates. You'll need to have a look at that to see what needs to be changed so that it expires tiles based on your own changes. The one that comes with <code>mod_tile</code> initialises replication to look <a href="https://github.com/openstreetmap/mod_tile/blob/master/openstreetmap-tiles-update-expire">here</a> by default (the file <code>/var/lib/mod_tile/.osmosis/configuration.txt</code> is created when you initialise replication).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '16, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52026" class="comments-container">
<span id="52029"></span>
<div id="comment-52029" class="comment">
<div id="post-52029-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://github.com/openstreetmap/mod_tile/blob/master/openstreetmap-tiles-update-expire">https://github.com/openstreetmap/mod_tile/blob/master/openstreetmap-tiles-update-expire</a> creates those as it runs</p>
</div>
<div id="comment-52029-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 09:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52035"></span>
<div id="comment-52035" class="comment">
<div id="post-52035-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think the main command that used to updata tiles are "$OSM2PGSQL_BIN -a --slim -e$EXPIRY_METAZOOM:$EXPIRY_METAZOOM $OSM2PGSQL_OPTIONS -o "$EXPIRY_FILE.$$" $CHANGE_FILE" and "render_expired --min-zoom=$EXPIRY_MINZOOM --max-zoom=$EXPIRY_MAXZOOM --touch-from=$EXPIRY_MINZOOM -s /var/run/renderd.sock", am i right?</p>
</div>
<div id="comment-52035-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 11:09)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="52036"></span>
<div id="comment-52036" class="comment">
<div id="post-52036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes - and obviously $CHANGE_FILE is the list of changes that you'll need to create somehow.</p>
</div>
<div id="comment-52036-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 11:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52037"></span>
<div id="comment-52037" class="comment">
<div id="post-52037-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I know that, "osmosis --read-replication-interval workingDirectory=replication --simplify-change --write-xml-change changes.osc.gz" command can create the changes file.</p>
</div>
<div id="comment-52037-info" class="comment-info">
<span class="comment-age">(13 Sep '16, 11:15)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-52026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52026-form-container" class="comment-form-container">
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

