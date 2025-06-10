+++
type = "question"
title = "how to use zh-hant via manually building a tile server?"
description = '''map didn&#x27;t show zh-hant, how do i fix？ thanks a lot. '''
date = "2022-07-17T17:58:00Z"
lastmod = "2022-07-19T18:17:00Z"
weight = 85120
keywords = [ "building_server", "zh-hant" ]
aliases = [ "/questions/85120" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to use zh-hant via manually building a tile server?](/questions/85120/how-to-use-zh-hant-via-manually-building-a-tile-server)

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
<span id="post-85120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85120-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>map didn't show zh-hant, how do i fix？ thanks a lot. <img src="https://help.openstreetmap.org/upfiles/1658076890663.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building_server" rel="tag" title="see questions tagged &#39;building_server&#39;">building_server</span> <span class="post-tag tag-link-zh-hant" rel="tag" title="see questions tagged &#39;zh-hant&#39;">zh-hant</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '22, 17:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c66ad6c704973c88fe030ad570ef36a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="weiyilai&#39;s gravatar image" />
<p><span>weiyilai</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="weiyilai has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-85120" class="comments-container">
<span id="85127"></span>
<div id="comment-85127" class="comment">
<div id="post-85127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The previous part of this story is in <a href="https://help.openstreetmap.org/questions/85089/manually-building-a-tile-server-ubuntu-2204-lts-an-error-has-occured">https://help.openstreetmap.org/questions/85089/manually-building-a-tile-server-ubuntu-2204-lts-an-error-has-occured</a> .</p>
</div>
<div id="comment-85127-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 18:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85167"></span>
<div id="comment-85167" class="comment">
<div id="post-85167-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>tile it's not found. <a href="https://imgur.com/zfduAxU">https://imgur.com/zfduAxU</a></p>
</div>
<div id="comment-85167-info" class="comment-info">
<span class="comment-age">(19 Jul '22, 18:11)</span> <span class="comment-user userinfo">weiyilai</span>
</div>
</div>
</div>
<div id="comment-tools-85120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85120-form-container" class="comment-form-container">
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

<span id="85163"></span>

<div id="answer-container-85163" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85163-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="weiyilai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At the time of writing (to be fixed shortly) the "fonts" suggested by the switch2osm guide <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">here</a> are wrong - they are missing some fallback fonts needed for Taiwan.</p>
<p>The <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#installation-on-ubuntudebian">Carto instructions</a> are nearly correct - the missing ones are "fonts-hanazono", although "ttf-unifont" has been replaced by "fonts-unifont".</p>
<p>If you do this:</p>
<pre><code>sudo apt install fonts-hanazono</code></pre>
<p>it should at least not display "little square boxes".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '22, 17:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-85163" class="comments-container">
<span id="85164"></span>
<div id="comment-85164" class="comment">
<div id="post-85164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>installed fonts-hanazano and it still doesn't work Am I missing something?</p>
<p>Thanks a lot</p>
</div>
<div id="comment-85164-info" class="comment-info">
<span class="comment-age">(19 Jul '22, 17:57)</span> <span class="comment-user userinfo">weiyilai</span>
</div>
</div>
<span id="85165"></span>
<div id="comment-85165" class="comment">
<div id="post-85165-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://map.atownsend.org.uk/tmp/Screenshot%202022-07-19%20175957.png">Works for me</a>.</p>
<p>You will need to restart renderd and apache2 after installing new fonts - I also cleared down all old tile directories "/var/cache/renderd/tiles/s2o/?" and "/var/cache/renderd/tiles/s2o/??" to make sure that I was looking at new tiles.</p>
</div>
<div id="comment-85165-info" class="comment-info">
<span class="comment-age">(19 Jul '22, 18:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85168"></span>
<div id="comment-85168" class="comment">
<div id="post-85168-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't understand why I execute carto project.mml &gt; mapnik.xml and then reload renderd and apache Traditional Chinese is now displayed properly</p>
<p>thanks a lot</p>
</div>
<div id="comment-85168-info" class="comment-info">
<span class="comment-age">(19 Jul '22, 18:17)</span> <span class="comment-user userinfo">weiyilai</span>
</div>
</div>
</div>
<div id="comment-tools-85163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85163-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85131"></span>

<div id="answer-container-85131" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85131-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you restart "renderd" you'll get some font loading messages (and errors).</p>
<p>When you set the server up, you will have installed some fonts via "sudo apt install". Which fonts did you install? Are any not listed at <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a> that are listed at <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#fonts">https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#fonts</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '22, 18:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-85131" class="comments-container">
<span id="85136"></span>
<div id="comment-85136" class="comment">
<div id="post-85136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>installed fonts-noto-cjk fonts-noto-hinted fonts-noto-unhinted fonts-unifont</p>
</div>
<div id="comment-85136-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 18:42)</span> <span class="comment-user userinfo">weiyilai</span>
</div>
</div>
<span id="85137"></span>
<div id="comment-85137" class="comment">
<div id="post-85137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure if this can be solved <a href="https://www.openstreetmap.org/user/demonshreder/diary/43956">https://www.openstreetmap.org/user/demonshreder/diary/43956</a></p>
</div>
<div id="comment-85137-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 18:58)</span> <span class="comment-user userinfo">weiyilai</span>
</div>
</div>
<span id="85138"></span>
<div id="comment-85138" class="comment">
<div id="post-85138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect that that is a solution to a different problem. You have a font issue (square boxes instead of characters), they want to display a different language insteaf of "name"?</p>
</div>
<div id="comment-85138-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 19:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85161"></span>
<div id="comment-85161" class="comment">
<div id="post-85161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I still can't solve it. I have installed traditional Chinese fonts, it's not working</p>
</div>
<div id="comment-85161-info" class="comment-info">
<span class="comment-age">(19 Jul '22, 16:50)</span> <span class="comment-user userinfo">weiyilai</span>
</div>
</div>
</div>
<div id="comment-tools-85131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85131-form-container" class="comment-form-container">
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

