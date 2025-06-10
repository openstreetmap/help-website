+++
type = "question"
title = "Modify style file for osm2pgsql"
description = '''Im a beginner and want to modify a style_default file befor import to osm2pgsql, can somebody answer me please? '''
date = "2023-04-29T00:45:00Z"
lastmod = "2023-04-29T12:44:00Z"
weight = 87186
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/87186" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Modify style file for osm2pgsql](/questions/87186/modify-style-file-for-osm2pgsql)

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
<span id="post-87186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87186-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Im a beginner and want to modify a style_default file befor import to osm2pgsql, can somebody answer me please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '23, 00:45</strong></p>
<img src="https://secure.gravatar.com/avatar/eab66f0d7f69924f6b9c931be7c0e9eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rezzzat&#39;s gravatar image" />
<p><span>Rezzzat</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rezzzat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87186" class="comments-container">
<span id="87187"></span>
<div id="comment-87187" class="comment">
<div id="post-87187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello - you might need to provide a bit more information about what you are trying to do. The word "style" is unfortunately used for several different things:</p>
<p>Firstly, it's used for the entire map style, so <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> is the "map style" for the "standard" tiles you see at openstreetmap.org. In there is a "style" directory <a href="https://github.com/gravitystorm/openstreetmap-carto/tree/master/style">https://github.com/gravitystorm/openstreetmap-carto/tree/master/style</a> which contains the actual code for the map style.</p>
<p>There's also <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.style">https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.style</a> , which determines which columns are created in the database by osm2pgsql.</p>
<p>Finally lua processing files such as <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua">https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua</a> are sometimes referred to as "style files".</p>
</div>
<div id="comment-87187-info" class="comment-info">
<span class="comment-age">(29 Apr '23, 12:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87186-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

