+++
type = "question"
title = "Compiling Mapnik on Raspberry Pi"
description = '''Hi There I am trying to compile mapnik on a raspberry pi, but ran into an error compiling mapnik_geometry.os.  g++ -o bindings/python/mapnik_geometry.os -c -ansi -Wall -pthread -ftemplate-depth-300 -O3 -fno-strict-aliasing -finline-functions -Wno-inline -Wno-parentheses -Wno-char-subscripts -fPIC -D...'''
date = "2015-03-03T22:39:00Z"
lastmod = "2015-03-04T07:54:00Z"
weight = 41476
keywords = [ "compile", "mapnik" ]
aliases = [ "/questions/41476" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Compiling Mapnik on Raspberry Pi](/questions/41476/compiling-mapnik-on-raspberry-pi)

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
<span id="post-41476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41476-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi There</p>
<p>I am trying to compile mapnik on a raspberry pi, but ran into an error compiling mapnik_geometry.os.</p>
<blockquote>
<p>g++ -o bindings/python/mapnik_geometry.os -c -ansi -Wall -pthread -ftemplate-depth-300 -O3 -fno-strict-aliasing -finline-functions -Wno-inline -Wno-parentheses -Wno-char-subscripts -fPIC -DHAVE_JPEG -DMAPNIK_USE_PROJ4 -DHAVE_PNG -DHAVE_TIFF -DBIGINT -DBOOST_REGEX_HAS_ICU -DLINUX -DMAPNIK_THREADSAFE -DNDEBUG -DHAVE_CAIRO -DHAVE_PYCAIRO -Ideps -Ideps/clipper/include -Ideps/agg/include -I. -Iinclude -I/usr/local/include -I/usr/include -I/usr/include/freetype2 -I/usr/include/libxml2 -I/usr/include/postgresql -I/usr/include/gdal -I/usr/include/python2.7 -I/usr/include/cairo -I/usr/include/glib-2.0 -I/usr/lib/arm-linux-gnueabihf/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/libpng12 -I/usr/include/pycairo bindings/python/mapnik_geometry.cpp g++: internal compiler error: Killed (program cc1plus)</p>
</blockquote>
<p>How did you install mapnik on the Pi? Once I have it up and running I can look into <a href="/questions/38209/rendering-blank-tiles-on-raspberry-pi-setup">this question</a>.</p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '15, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/983e541383fc2dd6b21fe40db33bee21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dickvla&#39;s gravatar image" />
<p><span>dickvla</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dickvla has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '15, 07:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-41476" class="comments-container">
&#10;</div>
<div id="comment-tools-41476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41476-form-container" class="comment-form-container">
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

<span id="41482"></span>

<div id="answer-container-41482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41482-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"internal compiler error: Killed" sounds like you are running out of memory, which is very likely on a Raspberry Pi. Try to stop other processes requiring much memory and maybe add a swap file, note that this might increase your compile time significantly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '15, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '15, 07:54</strong> </span></p>
</div>
</div>
<div id="comments-container-41482" class="comments-container">
&#10;</div>
<div id="comment-tools-41482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41482-form-container" class="comment-form-container">
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

