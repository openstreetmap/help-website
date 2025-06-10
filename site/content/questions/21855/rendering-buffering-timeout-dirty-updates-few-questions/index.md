+++
type = "question"
title = "Rendering / Buffering / Timeout / Dirty / Updates (few Questions)"
description = '''See: http://forum.openstreetmap.org/viewtopic.php?pid=330395#p330395 Hello. i have a few Questions: I use debug with: tail -f /var/log/syslog |grep renderd At first: If i want to Render Tiles, it throws me an errormessage: The tile is dirty. How can i skip this? Then: It takes long to Render tiles.....'''
date = "2013-04-25T19:19:00Z"
lastmod = "2013-04-26T17:20:00Z"
weight = 21855
keywords = [ "rendering", "buffering", "dirty", "updates", "error" ]
aliases = [ "/questions/21855" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering / Buffering / Timeout / Dirty / Updates (few Questions)](/questions/21855/rendering-buffering-timeout-dirty-updates-few-questions)

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
<span id="post-21855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21855-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>See: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=330395#p330395">http://forum.openstreetmap.org/viewtopic.php?pid=330395#p330395</a></p>
<p>Hello.</p>
<p>i have a few Questions:</p>
<p>I use debug with: tail -f /var/log/syslog |grep renderd</p>
<p>At first:</p>
<p>If i want to Render Tiles, it throws me an errormessage: The tile is dirty. How can i skip this?</p>
<p>Then:</p>
<p>It takes long to Render tiles... After 10 Seconds i get a timeout (if it doesnt throw the errormessage dirty). How can i Change the Timeout to X Seconds?</p>
<p>Buffering:</p>
<p>I want that the renderjob do the rendeing in the background, and dont start it just when it is requested. Is there a method?</p>
<p>Updates:</p>
<p>for example my tiles are old (one Month) is there a method to update the Database? Whats the fasted Method?</p>
<p>Thank you! :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-buffering" rel="tag" title="see questions tagged &#39;buffering&#39;">buffering</span> <span class="post-tag tag-link-dirty" rel="tag" title="see questions tagged &#39;dirty&#39;">dirty</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '13, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/8fd83011d6e87db1c8974cae52e89899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asmardemir&#39;s gravatar image" />
<p><span>asmardemir</span><br />
<span class="score" title="76 reputation points">76</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asmardemir has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21855" class="comments-container">
&#10;</div>
<div id="comment-tools-21855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21855-form-container" class="comment-form-container">
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

<span id="21867"></span>

<div id="answer-container-21867" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21867-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(It is possibly better to ask these as separate questions)</p>
<p>What do you mean that it throws an error message that the tile is dirty? Dirty tiles are a normal process and simply means they need re-rendering, as the content might have changed and are thus outdated. This should not be an error. If you don't use diff files to keep the database up-to-date, then the likely cause for this is that you didn't specify the date of the imported data via the file "planet-import-complete", in which case all tiles older than 3 days are considered as outdated.</p>
<p>You can change the timeout in the apache site configuration (see <a href="https://github.com/openstreetmap/mod_tile/blob/master/debian/tileserver_site#L40">https://github.com/openstreetmap/mod_tile/blob/master/debian/tileserver_site#L40</a> ).</p>
<p>You can use the render_list utility to pre-seed the tile cache. It is usually sensible to do this for at least all of the tiles up to about z12. Lowzoom tiles are usually to slow to render on the fly, whereas it is possible to do so for high zoom tiles.</p>
<p>With regard to updating there is a description of how to do this on <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> . Assuming your db is up-to-date (either via a fresh import or via diff imports), you can use the utility render_old to re-render outdated tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '13, 08:55</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-21867" class="comments-container">
<span id="21896"></span>
<div id="comment-21896" class="comment">
<div id="post-21896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok thank you. Now i changed the Timeout to 5 minutes (300 Seconds) but it takes so long and i get timeouts. How can i upgrade the Performance of the renderer?</p>
<p>Best regards</p>
</div>
<div id="comment-21896-info" class="comment-info">
<span class="comment-age">(26 Apr '13, 17:20)</span> <span class="comment-user userinfo">asmardemir</span>
</div>
</div>
</div>
<div id="comment-tools-21867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21867-form-container" class="comment-form-container">
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

