+++
type = "question"
title = "Why no map base south of East India Docks when exporting an Osmarender Image"
description = '''Hi there, When I export an Osmarender Image (format:PNG zoom:16) of anything south of East India Dock Road (including parts of the Thames), the labels show up (e.g. bus stops), but the actual map base does not. Anyone know why or what I need to do to export this geographical area?'''
date = "2010-09-06T11:09:00Z"
lastmod = "2010-09-08T03:01:00Z"
weight = 741
keywords = [ "thames", "east", "london", "osmarender", "base" ]
aliases = [ "/questions/741" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Why no map base south of East India Docks when exporting an Osmarender Image](/questions/741/why-no-map-base-south-of-east-india-docks-when-exporting-an-osmarender-image)

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
<span id="post-741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-741-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>When I export an Osmarender Image (format:PNG zoom:16) of anything south of East India Dock Road (including parts of the Thames), the labels show up (e.g. bus stops), but the actual map base does not.</p>
<p>Anyone know why or what I need to do to export this geographical area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-thames" rel="tag" title="see questions tagged &#39;thames&#39;">thames</span> <span class="post-tag tag-link-east" rel="tag" title="see questions tagged &#39;east&#39;">east</span> <span class="post-tag tag-link-london" rel="tag" title="see questions tagged &#39;london&#39;">london</span> <span class="post-tag tag-link-osmarender" rel="tag" title="see questions tagged &#39;osmarender&#39;">osmarender</span> <span class="post-tag tag-link-base" rel="tag" title="see questions tagged &#39;base&#39;">base</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '10, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/694e1ac7af189938fcb69122911b8677?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AdeA&#39;s gravatar image" />
<p><span>AdeA</span><br />
<span class="score" title="44 reputation points">44</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AdeA has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '10, 14:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-741" class="comments-container">
&#10;</div>
<div id="comment-tools-741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-741-form-container" class="comment-form-container">
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

<span id="743"></span>

<div id="answer-container-743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-743-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The osmarender layer on the front page of <a href="http://www.openstreetmap.org">www.openstreetmap.org</a> is created by the Tiles At Home (T@H) project. It is made by many different computers rendering different areas of the map. It appears that one of the T@H clients has uploaded a broken image, and hasn't drawn the map properly. This is then causing problems with your map export.</p>
<p>You may wish to request that area is re-rendered by the T@H project, see the <a href="https://wiki.openstreetmap.org/wiki/Tiles@Home#Requesting_a_re-render">wiki for instructions</a>. Alternatively, try the mapnik tile export for a slightly different, but working correctly, map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '10, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '10, 15:40</strong> </span></p>
</div>
</div>
<div id="comments-container-743" class="comments-container">
&#10;</div>
<div id="comment-tools-743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-743-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="744"></span>

<div id="answer-container-744" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-744-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There has been an error in the rendering of the area you're trying to export. This is a temporary problem, since the map can be re-rendered, but it's difficult to say how long it will take to get fixed.</p>
<p>Until then, you can either use the Mapnik rendering, or try rendering the area on your own computer using the standalone version of <a href="https://wiki.openstreetmap.org/wiki/Osmarender">Osmarender</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '10, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-744" class="comments-container">
&#10;</div>
<div id="comment-tools-744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-744-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="750"></span>

<div id="answer-container-750" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-750-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Jonathan and Andy,</p>
<p>Many thanks for your answers! It saved me a lot of time.</p>
<p>I decided to go for the mapnik tile exports. A different look, but I'm pleased with the results. Andy, I'll follow the instructions on wiki to ask for the area to be re-rendered.</p>
<p>Thanks again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '10, 03:01</strong></p>
<img src="https://secure.gravatar.com/avatar/694e1ac7af189938fcb69122911b8677?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AdeA&#39;s gravatar image" />
<p><span>AdeA</span><br />
<span class="score" title="44 reputation points">44</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AdeA has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-750" class="comments-container">
&#10;</div>
<div id="comment-tools-750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-750-form-container" class="comment-form-container">
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

