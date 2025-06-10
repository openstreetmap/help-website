+++
type = "question"
title = "How to convert .pbf into .osm using osmosis"
description = '''Hello, I have downloaded osm.pbf file. Now I want to convert this pbg file into .osm inorder to import into psql. So I downloaded OSMOSIS and extracted. And now I don&#x27;t have a clear idea how can I convert this? Please help me. Thanks'''
date = "2018-01-09T02:48:00Z"
lastmod = "2018-01-10T11:27:00Z"
weight = 61539
keywords = [ "pbf", ".osm", "osmosis" ]
aliases = [ "/questions/61539" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to convert .pbf into .osm using osmosis](/questions/61539/how-to-convert-pbf-into-osm-using-osmosis)

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
<span id="post-61539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61539-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have downloaded osm.pbf file. Now I want to convert this pbg file into .osm inorder to import into psql. So I downloaded OSMOSIS and extracted. And now I don't have a clear idea how can I convert this? Please help me. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '18, 02:48</strong></p>
<img src="https://secure.gravatar.com/avatar/2f44e9d00f417d4cdd1d58c594804d92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swiftDroid&#39;s gravatar image" />
<p><span>swiftDroid</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swiftDroid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '18, 19:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-61539" class="comments-container">
&#10;</div>
<div id="comment-tools-61539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61539-form-container" class="comment-form-container">
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

<span id="61540"></span>

<div id="answer-container-61540" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61540-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="swiftDroid has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a number of different ways to import OSM data into a postgres database, depending on what you want to do with the data (rendering? routing? some sort of data analysis?). Generally speaking, you won't need to expand a .osm.pbf file into a .osm file to import it though - most tools I'd expect would understand pbf files.</p>
<p>If you're creating a rendering server, I'd suggest <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">these</a> instructions, and you won't need to unpack a PBF file to use them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '18, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-61540" class="comments-container">
<span id="61558"></span>
<div id="comment-61558" class="comment">
<div id="post-61558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer. I want to do routing and now I am getting an error when try to import .osm data into PostgreSQL. This is what I get</p>
<p>Error opening /usr/share/osm2pgrouting/mapconfig.xml:No such file or directoryFailed to open / parse config file /usr/share/osm2pgrouting/mapconfig.xml Why is that?</p>
</div>
<div id="comment-61558-info" class="comment-info">
<span class="comment-age">(10 Jan '18, 03:36)</span> <span class="comment-user userinfo">swiftDroid</span>
</div>
</div>
<span id="61567"></span>
<div id="comment-61567" class="comment">
<div id="post-61567-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In order that someone who's familiar with osm2pgrouting (which wouldn't include me) could comment on your error I'd expect that you'd need to post details somewhere of how you got to that stage, not just that a particular file is missing. We don't know what versions of what software you've installed, or even what operating system you're running.</p>
</div>
<div id="comment-61567-info" class="comment-info">
<span class="comment-age">(10 Jan '18, 11:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61540" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61540-form-container" class="comment-form-container">
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

