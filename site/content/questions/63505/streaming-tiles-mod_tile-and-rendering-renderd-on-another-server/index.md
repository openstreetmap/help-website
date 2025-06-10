+++
type = "question"
title = "Streaming tiles (mod_tile) and rendering (renderd) on another server"
description = '''Hello everyone, I have a rather technical question but I&#x27;m sure I can find someone who knows the answer here :) We put https://tile.openstreetmap.be/ online. The goal is to provide baselayers for Belgium and surroundings with default name tag but also with name:fr and name:nl only. So here are my qu...'''
date = "2018-05-16T13:42:00Z"
lastmod = "2018-05-16T16:31:00Z"
weight = 63505
keywords = [ "rendering", "renderd", "osmbe", "mod_tile" ]
aliases = [ "/questions/63505" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Streaming tiles (mod_tile) and rendering (renderd) on another server](/questions/63505/streaming-tiles-mod_tile-and-rendering-renderd-on-another-server)

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
<span id="post-63505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63505-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I have a rather technical question but I'm sure I can find someone who knows the answer here :)</p>
<p>We put <a href="https://tile.openstreetmap.be/">https://tile.openstreetmap.be/</a> online. The goal is to provide baselayers for Belgium and surroundings with default <code>name</code> tag but also with <code>name:fr</code> and <code>name:nl</code> only.</p>
<p>So here are my questions :<br />
I want to render the tiles on a powerful server and only "stream" the tiles on the "tile.openstreetmap.be" (no rendering).<br />
It works rather well <strong>but</strong> how can I make sure my tiles <strong>never</strong> expire ?<br />
How can I "disable" the <code>/dirty</code> option ?<br />
I see, using munin that all the tiles are "Old tile, attempted render". How can I disabled the "attempted render" ?</p>
<p>If needed, everything is documented here : <a href="https://github.com/jbelien/openstreetmap-carto-be/wiki">https://github.com/jbelien/openstreetmap-carto-be/wiki</a></p>
<p>Thanks a lot :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osmbe" rel="tag" title="see questions tagged &#39;osmbe&#39;">osmbe</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '18, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/08e299a7143fc92767e9c66bff9481bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbelien&#39;s gravatar image" />
<p><span>jbelien</span><br />
<span class="score" title="146 reputation points">146</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbelien has one accepted answer">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '18, 13:44</strong> </span></p>
</div>
</div>
<div id="comments-container-63505" class="comments-container">
&#10;</div>
<div id="comment-tools-63505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63505-form-container" class="comment-form-container">
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

<span id="63513"></span>

<div id="answer-container-63513" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63513-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jbelien has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without looking too closely at your setup:</p>
<ul>
<li>You can disable /dirty in your Apache config through a rewrite rule that rewrites everything that ends in "dirty" to some other page, or returns a "forbidden" error, e.g. <code>RewriteRule ^/.*/dirty$ / [F]</code></li>
<li>You can keep mod_tile from issuing low-priority "attempted render" requests by telling it that your database is 10 years old (or so): <code>touch -d '10 years ago' /var/lib/mod_tile/planet-import-complete</code></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '18, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-63513" class="comments-container">
<span id="63516"></span>
<div id="comment-63516" class="comment">
<div id="post-63516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik, I'll try that.</p>
<p>About <code>/dirty</code> what append if someone makes that query but <code>renderd</code> can't render it (because the database is not there). Is the tile deleted or does it "stay" ?</p>
<p>Thanks :)</p>
</div>
<div id="comment-63516-info" class="comment-info">
<span class="comment-age">(16 May '18, 16:23)</span> <span class="comment-user userinfo">jbelien</span>
</div>
</div>
<span id="63517"></span>
<div id="comment-63517" class="comment">
<div id="post-63517-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It stays. If you don't have renderd running, you could also just ignore everything since all render requests will fizzle out anyway, just make sure to set ModTileRequestTimeout to 0.</p>
</div>
<div id="comment-63517-info" class="comment-info">
<span class="comment-age">(16 May '18, 16:26)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63518"></span>
<div id="comment-63518" class="comment">
<div id="post-63518-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just checked, <code>ModTileRequestTimeout</code> is already set to 0.</p>
<p>Should I also set <code>ModTileMissingRequestTimeout</code> to 0, I guess so right ?</p>
</div>
<div id="comment-63518-info" class="comment-info">
<span class="comment-age">(16 May '18, 16:31)</span> <span class="comment-user userinfo">jbelien</span>
</div>
</div>
</div>
<div id="comment-tools-63513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63513-form-container" class="comment-form-container">
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

