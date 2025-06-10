+++
type = "question"
title = "How to split up osm 8x8 meta file into 64 single tiles"
description = '''I use tirex/renderd together with mapnik to generate a custom styled OSM map. This results in meta files like /var/lib/tirex/tiles/mapnik/4/0/0/0/0/128.meta consisting of 8x8 single tiles. These files are normally delivered by apache&#x27;s mod_tile. My problem is that I do not have mod_tile available on...'''
date = "2015-03-10T10:56:00Z"
lastmod = "2016-06-03T15:14:00Z"
weight = 41600
keywords = [ "tileserver", "tirex", "mapnik", "mod_tile" ]
aliases = [ "/questions/41600" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to split up osm 8x8 meta file into 64 single tiles](/questions/41600/how-to-split-up-osm-8x8-meta-file-into-64-single-tiles)

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
<span id="post-41600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41600-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use <code>tirex</code>/<code>renderd</code> together with <code>mapnik</code> to generate a custom styled OSM map. This results in meta files like <code>/var/lib/tirex/tiles/mapnik/4/0/0/0/0/128.meta</code> consisting of 8x8 single tiles. These files are normally delivered by apache's <code>mod_tile</code>. My problem is that I do not have <code>mod_tile</code> available on the production server.</p>
<p>I there a way to generate the normal single <code>/z/x/y.png</code> files from these meta files, so that the OSM map can be delivered by just any normal http server? Say, either as part of tirex or mapnik, or as a post rendering script or similar?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '15, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/42c22f7724a32aa2d2e19609d8e7f1b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jnachtigall&#39;s gravatar image" />
<p><span>jnachtigall</span><br />
<span class="score" title="101 reputation points">101</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jnachtigall has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41600" class="comments-container">
&#10;</div>
<div id="comment-tools-41600" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41600-form-container" class="comment-form-container">
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

<span id="41608"></span>

<div id="answer-container-41608" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41608-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jnachtigall has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not having mod_tile available means that you will have to generate all tiles beforehand. You could do that by running mod_tile on a different server and then using a tile downloader to download PNG tiles from your server, or you could make metatiles and then use <a href="https://github.com/openstreetmap/mod_tile/tree/master/extra">meta2tile</a> to convert to PNG. Be careful with the huge numbers of files this may create though - on file systems with a large block size having so many files can easily fill up your disk.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '15, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-41608" class="comments-container">
<span id="49993"></span>
<div id="comment-49993" class="comment">
<div id="post-49993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... and many numbers of small tiles can also exhaust the available inodes too (depending on the filesystem you're using).</p>
</div>
<div id="comment-49993-info" class="comment-info">
<span class="comment-age">(03 Jun '16, 15:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41608-form-container" class="comment-form-container">
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

