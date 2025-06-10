+++
type = "question"
title = "Possibilities to remove company-names (Places) from card"
description = '''Hi there, another question for today ;-), I successfully installed my osm tile server with this tutorial: https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/ and everything looks fine, except the fact, that I need to remove company names (Places). I´ve read that there´s a...'''
date = "2021-10-19T10:20:00Z"
lastmod = "2021-10-19T15:59:00Z"
weight = 82242
keywords = [ "stylesheet", "tileserver" ]
aliases = [ "/questions/82242" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Possibilities to remove company-names (Places) from card](/questions/82242/possibilities-to-remove-company-names-places-from-card)

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
<span id="post-82242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82242-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, another question for today ;-), I successfully installed my osm tile server with this tutorial: <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> and everything looks fine, except the fact, that I need to remove company names (Places). I´ve read that there´s a need for changing the Stylesheet of the map. Can anybody give me a hint, how to manipulate the stylesheet of the tutorial for achieving that?</p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '21, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/2ee56dffff70eb5c464e336817ac08a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dom771013&#39;s gravatar image" />
<p><span>Dom771013</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dom771013 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82242" class="comments-container">
&#10;</div>
<div id="comment-tools-82242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82242-form-container" class="comment-form-container">
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

<span id="82250"></span>

<div id="answer-container-82250" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I solved this, by editing the stylesheets in ~/src/openstreetmap-carto/style/*.mss. I just set the unwanted elements on transparent. For sure this is a little bit hacky, but it works. After that you need to do the following:</p>
<pre><code>carto project.mml &gt; mapnik.xml
then remove the folder /var/lib/mod_tile/ajt
then restart via sudo /etc/init.d/renderd restart</code></pre>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '21, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/2ee56dffff70eb5c464e336817ac08a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dom771013&#39;s gravatar image" />
<p><span>Dom771013</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dom771013 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82250" class="comments-container">
&#10;</div>
<div id="comment-tools-82250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82250-form-container" class="comment-form-container">
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

