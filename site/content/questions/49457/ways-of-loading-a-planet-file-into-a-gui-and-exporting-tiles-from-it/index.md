+++
type = "question"
title = "Ways of loading a planet file into a GUI and exporting tiles from it"
description = '''Ok, ultimately I am trying to do the following:  Take a full planet file and change all the colours/style sheet Load the now altered planet data into a program that can handle it Export raster tiles from it  I have tried loading the whole planet file into Maperitive but even with loads of RAM and sp...'''
date = "2016-04-27T13:57:00Z"
lastmod = "2016-04-27T14:23:00Z"
weight = 49457
keywords = [ "planet", "styles", "generate_tiles" ]
aliases = [ "/questions/49457" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ways of loading a planet file into a GUI and exporting tiles from it](/questions/49457/ways-of-loading-a-planet-file-into-a-gui-and-exporting-tiles-from-it)

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
<span id="post-49457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49457-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ok, ultimately I am trying to do the following:</p>
<ul>
<li>Take a full planet file and change all the colours/style sheet</li>
<li>Load the now altered planet data into a program that can handle it</li>
<li>Export raster tiles from it</li>
</ul>
<p>I have tried loading the whole planet file into Maperitive but even with loads of RAM and space it can't seem to handle a full planet file.</p>
<p>I have tried using osm2pgsql and PostgreSQL with PostGIS to take the data from the file into a database but (without boring you) it doesn't work for me.</p>
<p>I've tried to get to the bottom of these issues to no avail so now I am just looking for suggestions of different ways to approach this. Does anyone have any alternative ways of achieving the above tasks?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-styles" rel="tag" title="see questions tagged &#39;styles&#39;">styles</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '16, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/b75302f1065a5eca0c63dcb6f3b51ea7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elea%20J&#39;s gravatar image" />
<p><span>Elea J</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elea J has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '16, 14:24</strong> </span></p>
</div>
</div>
<div id="comments-container-49457" class="comments-container">
<span id="49459"></span>
<div id="comment-49459" class="comment">
<div id="post-49459-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think that it's fair to say that "... using osm2pgsql and PostgreSQL with PostGIS to take the data from the file into a database" does work for at least some people. See also <a href="/questions/49178/osm2pgsql-appears-to-have-stopped-with-no-errors">https://help.openstreetmap.org/questions/49178/osm2pgsql-appears-to-have-stopped-with-no-errors</a></p>
</div>
<div id="comment-49459-info" class="comment-info">
<span class="comment-age">(27 Apr '16, 14:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49461"></span>
<div id="comment-49461" class="comment">
<div id="post-49461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey SomeoneElse, the question you reference is my question and I still haven't been able to get it working. I have now raised a bug on osm2pgsql's GitHub page in the hopes that someone can help me there. :)</p>
</div>
<div id="comment-49461-info" class="comment-info">
<span class="comment-age">(27 Apr '16, 14:13)</span> <span class="comment-user userinfo">Elea J</span>
</div>
</div>
<span id="49463"></span>
<div id="comment-49463" class="comment">
<div id="post-49463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd be surprised if it was an osm2pgsql bug; I've replied to your other help question.</p>
</div>
<div id="comment-49463-info" class="comment-info">
<span class="comment-age">(27 Apr '16, 14:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49466"></span>
<div id="comment-49466" class="comment">
<div id="post-49466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I just saw it.</p>
</div>
<div id="comment-49466-info" class="comment-info">
<span class="comment-age">(27 Apr '16, 14:23)</span> <span class="comment-user userinfo">Elea J</span>
</div>
</div>
</div>
<div id="comment-tools-49457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49457-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

