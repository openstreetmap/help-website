+++
type = "question"
title = "Fail to connect my tiles server"
description = '''Hi  I am creating an Android app that displays an OpenStreetMap using osmdroid.  On the tile server I am using: Mod_tile, renderd, mapnik, osm2pgsql and a  postgresql/postgis database.  I tried to connect this server using a firefox navigator from the same machine as the server and i succeed, but wh...'''
date = "2013-02-22T14:02:00Z"
lastmod = "2013-02-24T22:02:00Z"
weight = 20159
keywords = [ "renderd", "osmdroid", "osm2pgsql", "mapnik", "mod_tile" ]
aliases = [ "/questions/20159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fail to connect my tiles server](/questions/20159/fail-to-connect-my-tiles-server)

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
<span id="post-20159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20159-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I am creating an Android app that displays an OpenStreetMap using osmdroid. On the tile server I am using: Mod_tile, renderd, mapnik, osm2pgsql and a postgresql/postgis database. I tried to connect this server using a firefox navigator from the same machine as the server and i succeed, but when I try to contact this server from other machine I fail. Can you give me the issue of this problème? Do you tried to connect such server with osmdroid? Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '13, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/67d0bc74b15335eb039e36c3c58b9d55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yahya_Romdhane&#39;s gravatar image" />
<p><span>Yahya_Romdhane</span><br />
<span class="score" title="25 reputation points">25</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yahya_Romdhane has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20159" class="comments-container">
<span id="20186"></span>
<div id="comment-20186" class="comment">
<div id="post-20186-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Could you provide any clues, such as any actual error that you're getting?</p>
</div>
<div id="comment-20186-info" class="comment-info">
<span class="comment-age">(24 Feb '13, 00:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20159-form-container" class="comment-form-container">
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

<span id="20230"></span>

<div id="answer-container-20230" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20230-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your Apache is probably configured to only accept connections from localhost. Check for "Allow from" and "Deny from" and "Order Allow,Deny" or "Order Deny,Allow" in your httpd config files /.htaccess files.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '13, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '13, 22:02</strong> </span></p>
</div>
</div>
<div id="comments-container-20230" class="comments-container">
&#10;</div>
<div id="comment-tools-20230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20230-form-container" class="comment-form-container">
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

