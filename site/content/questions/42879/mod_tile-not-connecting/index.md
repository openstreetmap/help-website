+++
type = "question"
title = "mod_tile not connecting"
description = '''Hi all, I&#x27;m working on setting up a tile server and I&#x27;ve gotten everything to work except mod_tile. renderd works fine, I&#x27;m able to pre-render with render_all and I can see the queries in the query logs in the database. I was also able to use the generate_img.py in mapnik and the image was good. The...'''
date = "2015-05-04T21:26:00Z"
lastmod = "2015-05-05T21:34:00Z"
weight = 42879
keywords = [ "centos", "mod_tile" ]
aliases = [ "/questions/42879" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [mod_tile not connecting](/questions/42879/mod_tile-not-connecting)

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
<span id="post-42879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I'm working on setting up a tile server and I've gotten everything to work except mod_tile. renderd works fine, I'm able to pre-render with render_all and I can see the queries in the query logs in the database. I was also able to use the generate_img.py in mapnik and the image was good. The one part I havent been able to get to work is being able to view through apache. When I go to <a href="http://url/mod_tile/">http://url/mod_tile/</a> I get what is expected, but if i do something like /mod_url/0/0/0.png it says the image cant be displayed because it contains a error. When I setup slippymap.html it shows pink tiles and I see nothing in the database query log. Any pointers to what the issue is would be greatly appreciated. I'm running CentOS7.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '15, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/437be9dd9e835ce600eb3f720b077550?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Root&#39;s gravatar image" />
<p><span>Root</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Root has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42879" class="comments-container">
&#10;</div>
<div id="comment-tools-42879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42879-form-container" class="comment-form-container">
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

<span id="42880"></span>

<div id="answer-container-42880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42880-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Monitor rendering activity while accessing tiles. If there is activity then mod_tile gets the request through to renderd but the finished tile is somehow not saved or the return message does not reach mod_tile in time. If there is no rendering activity (perhaps also error messages in Apache's error log) then mod_tile cannot access the renderd socket. This can be a side effect of SELinux and perhaps the quick fix is as easy as "disable SELinux" (even though more fine grained approaches exist).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '15, 21:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42880" class="comments-container">
<span id="42881"></span>
<div id="comment-42881" class="comment">
<div id="post-42881-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your quick reply! I dont see anything when running renderd in the foreground and then accessing slippymap.html or trying to access /mod_tile/0/0/0.png. SELinux is disabled. The apache logs dont show anything I see as useful when accessing either url....</p>
</div>
<div id="comment-42881-info" class="comment-info">
<span class="comment-age">(04 May '15, 21:56)</span> <span class="comment-user userinfo">Root</span>
</div>
</div>
</div>
<div id="comment-tools-42880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42880-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42907"></span>

<div id="answer-container-42907" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42907-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem ended up being that you cant use /mod_tile in renderd.conf for the URI. /mod_tile is already taken by the mod_tile stats and it ended up creating a conflict. I found this out by changing the tile.conf line "ModTileEnableStats On" to off and then went to /mod_tile/0/0/0.png. A error in the logs said the stats were off and I figured it out from there. Thanks to Andy Allan for kinda pointing me in that direction.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '15, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/437be9dd9e835ce600eb3f720b077550?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Root&#39;s gravatar image" />
<p><span>Root</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Root has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42907" class="comments-container">
&#10;</div>
<div id="comment-tools-42907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42907-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42882"></span>

<div id="answer-container-42882" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42882-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure that your URLs are correct? Check that the url matches whatever is set in renderd.conf for your style, for example, <a href="http://url/openstreetmap/0/0/0.png">http://url/openstreetmap/0/0/0.png</a> - it's normally the name of the stylesheet, rather than "mod_tile", when requesting images.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '15, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-42882" class="comments-container">
<span id="42899"></span>
<div id="comment-42899" class="comment">
<div id="post-42899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure what you mean here? My renderd.conf is fairly simple but maybe I'm doing something wrong?</p>
<p>[renderd] socketname=/var/run/renderd/renderd.sock num_threads=4 tile_dir=/var/lib/mod_tile stats_file=/var/run/renderd/renderd.stats</p>
<p>[default] URI=/mod_tile/ TILEDIR=/data/tiles XML=/root/install/mapnik-v2.2.0/src/mapnik-style/osm.xml TILESIZE=256 HOST=localhost</p>
<p>[mapnik] plugins_dir=/usr/local/lib/mapnik/input font_dir=/usr/local/lib/mapnik/fonts font_dir_recurse=1</p>
</div>
<div id="comment-42899-info" class="comment-info">
<span class="comment-age">(05 May '15, 15:21)</span> <span class="comment-user userinfo">Root</span>
</div>
</div>
</div>
<div id="comment-tools-42882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42882-form-container" class="comment-form-container">
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

