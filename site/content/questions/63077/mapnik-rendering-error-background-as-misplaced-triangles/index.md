+++
type = "question"
title = "Mapnik rendering error - background as misplaced triangles"
description = '''Please be as kind as to have a look at the attached image and say what is your first thought of the probable reasons for such malfunction. The setup is Tilestache/Mapnik/Nginx. PostgreSQL database contains OSM data and works just fine with the &quot;standard&quot; setup of Apache/mod_tile/Mapnik. '''
date = "2018-04-22T18:06:00Z"
lastmod = "2018-04-24T20:43:00Z"
weight = 63077
keywords = [ "rendering", "tilestache", "postgresql", "mapnik", "error" ]
aliases = [ "/questions/63077" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik rendering error - background as misplaced triangles](/questions/63077/mapnik-rendering-error-background-as-misplaced-triangles)

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
<span id="post-63077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63077-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please be as kind as to have a look at the attached image and say what is your first thought of the probable reasons for such malfunction.</p>
<p>The setup is Tilestache/Mapnik/Nginx. PostgreSQL database contains OSM data and works just fine with the "standard" setup of Apache/mod_tile/Mapnik.</p>
<p><img src="https://help.openstreetmap.org/upfiles/mapnik-error.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tilestache" rel="tag" title="see questions tagged &#39;tilestache&#39;">tilestache</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '18, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/05223f63dcaf7b43f1eab94ca71cccff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mixroc&#39;s gravatar image" />
<p><span>Mixroc</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mixroc has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '18, 18:07</strong> </span></p>
</div>
</div>
<div id="comments-container-63077" class="comments-container">
<span id="63078"></span>
<div id="comment-63078" class="comment">
<div id="post-63078-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What happens if you zoom in - do the triangles get bigger?</p>
</div>
<div id="comment-63078-info" class="comment-info">
<span class="comment-age">(22 Apr '18, 19:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63079"></span>
<div id="comment-63079" class="comment">
<div id="post-63079-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a></p>
<p>Hi! Thanks for the reply.</p>
<p>If I zoom in, it, basically, remains in essence the same - a matrix of tiles of the same size with the background shifted in the same triangle manner, only at a larger scale.</p>
<p><img src="https://help.openstreetmap.org/upfiles/zoom-in_FIPJVon.png" alt="alt text" /></p>
<p>If I zoom out, though, it becomes even more strange, as the map is almost normal, but there are defects in the background, with similar regular displaced light/dark triangles at the top of the screen, next to the Polar Circle, and, in addition to that, with long but narrow irregular diagonal triangles stretched out from three (in this particular case) locations in Europe with their top vertices converging somewhere above Iceland.</p>
<p><img src="https://help.openstreetmap.org/upfiles/zoom-out.png" alt="alt text" /></p>
</div>
<div id="comment-63079-info" class="comment-info">
<span class="comment-age">(22 Apr '18, 20:07)</span> <span class="comment-user userinfo">Mixroc</span>
</div>
</div>
<span id="63080"></span>
<div id="comment-63080" class="comment">
<div id="post-63080-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Another view at about mid-zoom: <img src="https://help.openstreetmap.org/upfiles/zoom-mid_T4GicAv.png" alt="alt text" /></p>
</div>
<div id="comment-63080-info" class="comment-info">
<span class="comment-age">(22 Apr '18, 20:16)</span> <span class="comment-user userinfo">Mixroc</span>
</div>
</div>
<span id="63081"></span>
<div id="comment-63081" class="comment">
<div id="post-63081-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One of the views of the world:</p>
<p><img src="https://help.openstreetmap.org/upfiles/zoom-world.png" alt="alt text" /></p>
</div>
<div id="comment-63081-info" class="comment-info">
<span class="comment-age">(22 Apr '18, 20:21)</span> <span class="comment-user userinfo">Mixroc</span>
</div>
</div>
</div>
<div id="comment-tools-63077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63077-form-container" class="comment-form-container">
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

<span id="63083"></span>

<div id="answer-container-63083" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63083-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is that I don't know - the land / sea boundaries aren't "consistently wrong" across zoom levels (and as you say it works OK with Apache/mod_tile/Mapnik). Things to check might include:</p>
<ul>
<li>Processes getting killed while generating tiles</li>
<li>What "OSM data" (as opposed to just boundaries) looks like when you zoom right in</li>
<li>Trying to ask somewhere that TileStache users might hang out (github, I'm guessing?)</li>
<li>Any lingering 32bit vs 64bit issues (I'm guessing that everything is 64bit throughout, but just checking)</li>
<li>Any potential endian issues if the environment where it doesn't work is different to where it does</li>
</ul>
<p>... but as you can probably tell I'm mostly guessing here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '18, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-63083" class="comments-container">
&#10;</div>
<div id="comment-tools-63083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63083-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63112"></span>

<div id="answer-container-63112" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63112-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a></p>
<p>Hey! Thanks anyway. After wasting a whole day fiddling with various ways to install mapnik and the rest of the toolchain, fighting new non-compliances and errors where there were none before, I finally managed to get it working in a virtual machine with no problems at all, using - TADA! - exactly the same software I used before, but obviously different releases of it. The glithcy system was running bunsenlabs, the current successfull one is running ubuntu 16.04. The devil must have been in details, who knows where.</p>
<p>Cheers!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '18, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/05223f63dcaf7b43f1eab94ca71cccff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mixroc&#39;s gravatar image" />
<p><span>Mixroc</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mixroc has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-63112" class="comments-container">
&#10;</div>
<div id="comment-tools-63112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63112-form-container" class="comment-form-container">
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

