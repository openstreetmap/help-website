+++
type = "question"
title = "Mapnik not rendering Changes"
description = '''Greetings... I have setup my own OSM website from the rails port and also installed mapnik to render tiles using the OSM database. Everything works well. However, when i try to edit something, the changes are not reflected. Basically i got to the OSM rails application, then edit using Potlatch2 and ...'''
date = "2014-10-09T20:32:00Z"
lastmod = "2014-10-11T14:42:00Z"
weight = 37471
keywords = [ "renderd", "mapnik" ]
aliases = [ "/questions/37471" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapnik not rendering Changes](/questions/37471/mapnik-not-rendering-changes)

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
<span id="post-37471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37471-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings... I have setup my own OSM website from the rails port and also installed mapnik to render tiles using the OSM database. Everything works well. However, when i try to edit something, the changes are not reflected. Basically i got to the OSM rails application, then edit using Potlatch2 and save. Afterwards, i delete all the cached tiles and restart renderd. When i do this, the tiles are rendered without the changes. I have tried to change the road name, added a hotel, etc but none of those works. Kindly help point me in the right direction.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '14, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0de1b5d71fb7c74799148889048261?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20SSali&#39;s gravatar image" />
<p><span>David SSali</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David SSali has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37471" class="comments-container">
&#10;</div>
<div id="comment-tools-37471" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37471-form-container" class="comment-form-container">
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

<span id="37474"></span>

<div id="answer-container-37474" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37474-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="David SSali has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume you have set up two different databases, one for rendering and one for the API database.</p>
<p>There is no automatic linkage between these databases (on OSM's own infrastructure, these databases are on different machines).</p>
<p>You need to dump API database changes to a file using Osmosis, and then import these change files into your rendering database using osm2pgsql.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '14, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-37474" class="comments-container">
<span id="37484"></span>
<div id="comment-37484" class="comment">
<div id="post-37484-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik...However i am using the same database for both. Matter of fact when i make changes to v/etc/mapnik-osm-data/inc/datasource-settings.xml.inc and put the wrong database, there are no tiles rendered at all.</p>
</div>
<div id="comment-37484-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 10:56)</span> <span class="comment-user userinfo">David SSali</span>
</div>
</div>
<span id="37496"></span>
<div id="comment-37496" class="comment">
<div id="post-37496-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The Rails port and the rendering engine require databases that have a different setup. The rails port database uses the "APIDB" data schema, and the rendering uses the schema created by the osm2pgsql import. They are completely different, e.g. the APIDB database contains no geometry columns but does have a history of all edits, whereas the rendering database has geometries but discards history. It might be possible to run both services off the same database in the senses of PostgreSQL but then one service will use one set of tables and the other service another - they'll never share tables.</p>
</div>
<div id="comment-37496-info" class="comment-info">
<span class="comment-age">(10 Oct '14, 15:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="37532"></span>
<div id="comment-37532" class="comment">
<div id="post-37532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik...You have indeed enlightened me. This is indeed true. Is there an automated way to keep the rendering tables upto date? I see that in OSM when you make changes, they seem to take effect without human intervention. For now am doing this manually using osmosis</p>
</div>
<div id="comment-37532-info" class="comment-info">
<span class="comment-age">(11 Oct '14, 14:42)</span> <span class="comment-user userinfo">David SSali</span>
</div>
</div>
</div>
<div id="comment-tools-37474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37474-form-container" class="comment-form-container">
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

