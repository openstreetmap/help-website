+++
type = "question"
title = "Loading different styles in custom openstreemap server"
description = '''hello, i have setup an openstreetmap server and everything works perfectly..however there are somethings that i do not fully understand... regarding alternative styles --when you load the osm file with osm2psql into postgresql you need to pass the style.xml as a parameter.. Than implies that postgre...'''
date = "2017-07-28T09:27:00Z"
lastmod = "2017-07-28T11:40:00Z"
weight = 57323
keywords = [ "sytle", "tilemmil", "mapnik" ]
aliases = [ "/questions/57323" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Loading different styles in custom openstreemap server](/questions/57323/loading-different-styles-in-custom-openstreemap-server)

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
<span id="post-57323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello, i have setup an openstreetmap server and everything works perfectly..however there are somethings that i do not fully understand...</p>
<p>regarding alternative styles --when you load the osm file with osm2psql into postgresql you need to pass the style.xml as a parameter.. Than implies that postgresql holds representation data (for example, colors) into the tables? I have seen the tables loaded but i did not find anything related to style... --that leads to my main confusion..for example i want to load either the humanitarial style or the osm-bright? how do i do that? do i have to run the osm2psql with a different another_style.xml into the <strong>same</strong> database? i do not quite understand how to serve different layers ? another style means another database ? some explanations would be great...</p>
<p>also, lets say that i want to remove all the restaurants from the tiles and add them with javascript as points with leafletjs...as far as i understand, i need to create a style with tilemill, generate the mms file, convert it with mapnik and reload the data (and then it goes to my first question)..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sytle" rel="tag" title="see questions tagged &#39;sytle&#39;">sytle</span> <span class="post-tag tag-link-tilemmil" rel="tag" title="see questions tagged &#39;tilemmil&#39;">tilemmil</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '17, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f0aa2d242d42c70426e0916f304c1f1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmtrs&#39;s gravatar image" />
<p><span>dmtrs</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmtrs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57323" class="comments-container">
&#10;</div>
<div id="comment-tools-57323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57323-form-container" class="comment-form-container">
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

<span id="57324"></span>

<div id="answer-container-57324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57324-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't pass any <code>style.xml</code> file to osm2pgsql. Instead you pass a <code>.style</code> file, which describes to osm2pgsql what columns (attributes) should be added to the database. For example, <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.style">here</a> is the <code>.style</code> file for openstreetmap-carto.</p>
<p>You can often run multiple styles from the same osm2pgsql database, so long as they have been either written to work with the same columns, or use the same <code>.style</code> (and <code>.lua</code> rules, if used) files. If you are creating your own styles it's straightforward. If you are using other people's styles, sometimes they work, and sometimes they need small changes to their SQL queries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '17, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-57324" class="comments-container">
&#10;</div>
<div id="comment-tools-57324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57324-form-container" class="comment-form-container">
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

