+++
type = "question"
title = "Problem installing the Nominatim web front-end"
description = '''I am currently trying to set up a OSM Server together with Nominatim to do Reverse Geocoding. OSM works fine (I can render maps with Mapnik etc...) I also set up the tables for Nominatim following this:  https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Set_up_the_website But when I copy the...'''
date = "2011-03-09T15:59:00Z"
lastmod = "2011-03-09T17:28:00Z"
weight = 3651
keywords = [ "nominatim", "installation" ]
aliases = [ "/questions/3651" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem installing the Nominatim web front-end](/questions/3651/problem-installing-the-nominatim-web-front-end)

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
<span id="post-3651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3651-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently trying to set up a OSM Server together with Nominatim to do Reverse Geocoding. OSM works fine (I can render maps with Mapnik etc...)</p>
<p>I also set up the tables for Nominatim following this: <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Set_up_the_website">https://wiki.openstreetmap.org/wiki/Nominatim/Installation#Set_up_the_website</a></p>
<p>But when I copy the website directory to /var/www/ and open the page, it will just show an empty page. (PHP-Parser works fine) I already hunted the problem down to a line in "init.php", where it says "require_once('DB.php');", but there is no DB.php in the website/.htlib/ directory. Is it missing, or where is this usually to be found?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '11, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ba62b0ca95b995e68fc3356510c6bb11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Santhor&#39;s gravatar image" />
<p><span>Santhor</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Santhor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '11, 16:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-3651" class="comments-container">
&#10;</div>
<div id="comment-tools-3651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3651-form-container" class="comment-form-container">
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

<span id="3657"></span>

<div id="answer-container-3657" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3657-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Santhor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would assume that this refers to the PHP's Pear DB module.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '11, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-3657" class="comments-container">
&#10;</div>
<div id="comment-tools-3657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3657-form-container" class="comment-form-container">
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

