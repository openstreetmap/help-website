+++
type = "question"
title = "How to force mapnik render only not empty tiles?"
description = '''Is there a way to force mapnik not to generate empty tiles? And create instead a symbolic link for that??? Update Sorry for DUMM question. So how to do that generate_tiles.py will not save empty tiles? '''
date = "2011-11-06T07:54:00Z"
lastmod = "2014-07-09T22:45:00Z"
weight = 8849
keywords = [ "tiles", "mapnik" ]
aliases = [ "/questions/8849" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to force mapnik render only not empty tiles?](/questions/8849/how-to-force-mapnik-render-only-not-empty-tiles)

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
<span id="post-8849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8849-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to force mapnik not to generate empty tiles? And create instead a symbolic link for that???</p>
<p>Update</p>
<p>Sorry for DUMM question. So how to do that <a href="http://generate_tiles.py">generate_tiles.py</a> will not save empty tiles?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '11, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>23 Nov '11, 12:49</strong> </span></p>
</div>
</div>
<div id="comments-container-8849" class="comments-container">
&#10;</div>
<div id="comment-tools-8849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8849-form-container" class="comment-form-container">
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

<span id="8855"></span>

<div id="answer-container-8855" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8855-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gevork has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't have a direct answer, but in practice I add a command at the end of the generation for removing these empty tiles: find tiles/ -size 116c | xargs rm</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '11, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-8855" class="comments-container">
<span id="8857"></span>
<div id="comment-8857" class="comment">
<div id="post-8857-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@NicolasDumoulin</span> do you add this line in the end of <a href="http://generate_tiles.py">generate_tiles.py</a> ????</p>
</div>
<div id="comment-8857-info" class="comment-info">
<span class="comment-age">(06 Nov '11, 22:13)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="8860"></span>
<div id="comment-8860" class="comment">
<div id="post-8860-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, no, it is a bash command (linux). But I think you can achieve the same in pure python as follow:</p>
<blockquote>
<p><code>import os,glob;</code></p>
<p><code>for f in glob.glob('tiles/**/*'): if (os.path.getsize(f) == 0): os.remove(f)</code></p>
</blockquote>
</div>
<div id="comment-8860-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 08:15)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="9215"></span>
<div id="comment-9215" class="comment">
<div id="post-9215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@NicolasDumoulin</span> when I make find tiles/ -size 116c | xargs rm I get rm: missing operand</p>
<p>here is the output marmur@marmur-Extensa-5635ZG:~/tiles$ find yerevanMap/ -size 116c | xargs rm rm: missing operand Try `rm --help' for more information. marmur@marmur-Extensa-5635ZG:~/tiles$</p>
<p>Any idea why???</p>
</div>
<div id="comment-9215-info" class="comment-info">
<span class="comment-age">(23 Nov '11, 18:45)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="9216"></span>
<div id="comment-9216" class="comment">
<div id="post-9216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it is because the result of the command find is empty, you can check it by removing "| xargs rm" from the command. Maybe the size value isn't correct. I've found the "116" by looking at the printed size of my empty tiles with the "ls -l" command.</p>
</div>
<div id="comment-9216-info" class="comment-info">
<span class="comment-age">(23 Nov '11, 20:09)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="9217"></span>
<div id="comment-9217" class="comment">
<div id="post-9217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@NicolasDumoulin</span> -rw-rw-r-- 1 marmur marmur 139 2011-11-23 00:51 0.png I get this... so should it be -size 139c???</p>
</div>
<div id="comment-9217-info" class="comment-info">
<span class="comment-age">(23 Nov '11, 22:41)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="9218"></span>
<div id="comment-9218" class="comment not_top_scorer">
<div id="post-9218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@NicolasDumoulin</span> thanks! it worked, found out that empty tiles was not 139 but 103 by me.... deleted like a charm! once again, thank you very much</p>
</div>
<div id="comment-9218-info" class="comment-info">
<span class="comment-age">(23 Nov '11, 22:57)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="34783"></span>
<div id="comment-34783" class="comment not_top_scorer">
<div id="post-34783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>be aware that empty sea tile, empty land tile, or any other "empty" tile that has only one color in it, may all have exactly the same size.</p>
</div>
<div id="comment-34783-info" class="comment-info">
<span class="comment-age">(09 Jul '14, 22:45)</span> <span class="comment-user userinfo">leding</span>
</div>
</div>
</div>
<div id="comment-tools-8855" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-8855-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8850"></span>

<div id="answer-container-8850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8850-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mapnik doesn't generate tiles; Mapnik is a library only. It is the program that calls Mapnik - e.g. <a href="http://generate_tiles.py">generate_tiles.py</a> or renderd or tirex or something else - that generates tiles, or maybe metatiles. Mapnik has no way of signalling to these calling programs that it has just generated an "empty" tile (anyway, in our standard OSM style, only sea tiles are really "empty", everything else has at least a land polygon drawn).</p>
<p>Read the thread <a href="http://lists.openstreetmap.org/pipermail/dev/2011-August/023298.html">Not saving empty Mapnik tiles</a> on the osm-dev mailing list for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '11, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8850" class="comments-container">
&#10;</div>
<div id="comment-tools-8850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8850-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23097"></span>

<div id="answer-container-23097" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23097-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think that "only sea tiles are really empty" - in some cases it depends of network connection when Mapnik receives "empty" blue tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '13, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/b6a0b1f4c2b18dbbed2a999a67c790f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nedol&#39;s gravatar image" />
<p><span>nedol</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nedol has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23097" class="comments-container">
&#10;</div>
<div id="comment-tools-23097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23097-form-container" class="comment-form-container">
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

