+++
type = "question"
title = "How to render imported extract only with render_list"
description = '''Hi all, I want to render area, only where I have imported extracts. I already rendered meta info for levels 0-9 with render_list --all -n 2 --socket=/var/run/renderd/renderd.sock --min-zoom=0 --max-zoom=9  and now I am having troubles rendering tiles for a specified lat/long. I am running this comma...'''
date = "2012-07-11T12:32:00Z"
lastmod = "2017-03-21T03:19:00Z"
weight = 14172
keywords = [ "rendering", "mapnik" ]
aliases = [ "/questions/14172" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to render imported extract only with render_list](/questions/14172/how-to-render-imported-extract-only-with-render_list)

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
<span id="post-14172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14172-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I want to render area, only where I have imported extracts. I already rendered meta info for levels 0-9 with</p>
<pre><code>render_list --all -n 2 --socket=/var/run/renderd/renderd.sock --min-zoom=0 --max-zoom=9</code></pre>
<p>and now I am having troubles rendering tiles for a specified lat/long. I am running this command</p>
<pre><code>render_list -x 159 -X 179 -y 160 -Y 410 -n 2 --socket=/var/run/renderd/renderd.sock --min-zoom=10 --max-zoom=10</code></pre>
<p>but it stays for long time and showing "Starting 2 rendering threads" message without a sign it is rendering. Do I have mistaken the command options? Any help is appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '12, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/efd8cb26d5bdb6ae7d463500cf7a9bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kodex&#39;s gravatar image" />
<p><span>kodex</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kodex has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14172" class="comments-container">
<span id="19301"></span>
<div id="comment-19301" class="comment">
<div id="post-19301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey! I am having same problem. Did you find the solution for that problem ?</p>
</div>
<div id="comment-19301-info" class="comment-info">
<span class="comment-age">(24 Jan '13, 06:21)</span> <span class="comment-user userinfo">asfer mohamed</span>
</div>
</div>
</div>
<div id="comment-tools-14172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14172-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="19307"></span>

<div id="answer-container-19307" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19307-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Render_list does not currently offer this useful feature afaik.</p>
<p>I have a patch to add this functionality, but I have not yet committed it. I will try and clean up the patch and commit it soon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '13, 08:41</strong></p>
<img src="https://secure.gravatar.com/avatar/32c974c4ca8b246698c2b82c64924da5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apmon&#39;s gravatar image" />
<p><span>apmon</span><br />
<span class="score" title="6527 reputation points"><span>6.5k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apmon has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-19307" class="comments-container">
&#10;</div>
<div id="comment-tools-19307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19307-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19308"></span>

<div id="answer-container-19308" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19308-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What I have done is using this command: render_list --all -x 622 -X 755 -y 1515 -Y 1659 -n 2 --socket=/var/run/renderd/renderd.sock --min-zoom=12 --max-zoom=12</p>
<p>to render level 12 for California and the given coordinates, which do the job for me. It prerenders all tiles for the area specified. You can check the coordiantes at <a href="http://tools.geofabrik.de/map/">http://tools.geofabrik.de/map/</a>, just make sure you selected the "Tile coordinates" overlay.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '13, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/efd8cb26d5bdb6ae7d463500cf7a9bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kodex&#39;s gravatar image" />
<p><span>kodex</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kodex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '17, 14:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-19308" class="comments-container">
<span id="55202"></span>
<div id="comment-55202" class="comment">
<div id="post-55202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Took me a minute to find the tile coordinates overlay -- it is in the little plus sign in the top right of the map.</p>
</div>
<div id="comment-55202-info" class="comment-info">
<span class="comment-age">(21 Mar '17, 03:19)</span> <span class="comment-user userinfo">joe_mo</span>
</div>
</div>
</div>
<div id="comment-tools-19308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19308-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44400"></span>

<div id="answer-container-44400" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44400-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try this <a href="https://github.com/alx77/render_list_geo.pl">script</a>. It uses <em>render_list</em> utility in proper way and converts geo coordinates (WGS-84) to tile coordinates on several zoom levels and generates many tiles in one round.</p>
<p>For example:</p>
<pre><code>./render_list_geo.pl -n 2 -z 6 -Z 15 -x 21.8 -X 40.7 -y 44.03 -Y 52.6</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/92b8723cc2887ccb3ad53b57e597ed44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a-furmanov&#39;s gravatar image" />
<p><span>a-furmanov</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a-furmanov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44400" class="comments-container">
&#10;</div>
<div id="comment-tools-44400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44400-form-container" class="comment-form-container">
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

