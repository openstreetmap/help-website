+++
type = "question"
title = "Available address in OSM fails in lookup"
description = '''Hi, I recognized a strange behavior regarding address lookup. The address &quot;Rheinstraße 33, Munich&quot; is available in OSM and correctly defined by a point. Unfortunately, searching for that address fails and returns available streets in different cities except of Munich, irrespective of the housenumber...'''
date = "2011-07-31T16:34:00Z"
lastmod = "2011-08-04T10:31:00Z"
weight = 6742
keywords = [ "lookup", "searching", "address" ]
aliases = [ "/questions/6742" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Available address in OSM fails in lookup](/questions/6742/available-address-in-osm-fails-in-lookup)

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
<span id="post-6742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6742-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I recognized a strange behavior regarding address lookup. The address "Rheinstraße 33, Munich" is available in OSM and correctly defined by a point. Unfortunately, searching for that address fails and returns available streets in different cities except of Munich, irrespective of the housenumber. What is wrong in the looking up for the address database?</p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lookup" rel="tag" title="see questions tagged &#39;lookup&#39;">lookup</span> <span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '11, 16:34</strong></p>
<img src="https://secure.gravatar.com/avatar/2f379e02a6e3c82ac534660f98d5780b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robiston&#39;s gravatar image" />
<p><span>Robiston</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robiston has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '11, 18:22</strong> </span></p>
</div>
</div>
<div id="comments-container-6742" class="comments-container">
&#10;</div>
<div id="comment-tools-6742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6742-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="6859"></span>

<div id="answer-container-6859" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6859-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Robiston has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This might be yet another case of Nominatim not updating with data from the main map database.</p>
<p>Nominatim has its own database, which is updated from the main OSM database. Sometimes, this update may lag - in that case Nominatim will search an older version of the OSM data, and may not find things that are visible on the slippy map and in the DB.</p>
<p>In this case, looking at the history shows that the house number for Rheinstraße 33 was only added on 26 Jul 2011. Searching for e.g. "Rheinstraße 27" works correctly, and this number as added in 2009. So maybe you just need to wait for the update.</p>
<p><em>Update:</em> Now (March 2012) Nominatim correctly finds "Rheinstraße 33, Munich". So it was probably just an updating problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '11, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '12, 15:50</strong> </span></p>
</div>
</div>
<div id="comments-container-6859" class="comments-container">
&#10;</div>
<div id="comment-tools-6859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6859-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6744"></span>

<div id="answer-container-6744" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6744-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that you have entered that address in the search field of the main site of <a href="http://osm.org">osm.org</a></p>
<p>The search engine behind that is called <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>. You can have a look at all related pages in the OSM wiki to find possible cases where search result is similar to your one.</p>
<p>Sometimes it seems that the Nominatim methods to find a place are a little bit weird. But then we can only collect test cases to find out where the error can be located.</p>
<p>So try to find more hints in the wiki, or here at <a href="http://help.osm.org">help.osm.org</a> by searchimg for text or tags "nominatim".</p>
<p>Or have a look at the detailed search result of Nominatim when you go to its <a href="http://nominatim.openstreetmap.org/">website</a></p>
<p>PS: I assume that your address data is already present in the raw OSM data for a longer time, because you always have to pay attention of the date when the Nominatim search base has been generated from.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '11, 19:28</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '11, 15:56</strong> </span></p>
</div>
</div>
<div id="comments-container-6744" class="comments-container">
&#10;</div>
<div id="comment-tools-6744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6744-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6790"></span>

<div id="answer-container-6790" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6790-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This seems to be similar to <a href="/questions/5819/added-street-doesnt-show-up-on-search">this question</a>.</p>
<p>Currently there seems to be a problem with nominatim not importing updates for some weeks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '11, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '11, 16:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/b95e1b5cb818be577b5561688a50368c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="banoffee&#39;s gravatar image" />
<p><span>banoffee</span><br />
<span class="score" title="884 reputation points">884</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span></p>
</div>
</div>
<div id="comments-container-6790" class="comments-container">
<span id="6792"></span>
<div id="comment-6792" class="comment">
<div id="post-6792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you copy-pasted the wrong link... I've updated it to something appropriate with my newly-available "edit" link. Hope that's ok?</p>
</div>
<div id="comment-6792-info" class="comment-info">
<span class="comment-age">(02 Aug '11, 16:35)</span> <span class="comment-user userinfo">banoffee</span>
</div>
</div>
</div>
<div id="comment-tools-6790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6790-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6858"></span>

<div id="answer-container-6858" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6858-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="/questions/642/issues-with-httpnominatimopenstreetmaporg">this question</a>. Quote: "This is probably not the correct place to report bugs in services. For errors in Nominatim (and most other Open Street Map software) you are best off using the <a href="http://trac.openstreetmap.org/newticket?component=nominatim">Open Street Map bug tracker</a>".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '11, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a1156d45a55699715b80fc3cadd0c8d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmehl&#39;s gravatar image" />
<p><span>mmehl</span><br />
<span class="score" title="565 reputation points">565</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmehl has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-6858" class="comments-container">
<span id="6867"></span>
<div id="comment-6867" class="comment">
<div id="post-6867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, this was obviously not really a bug report but a question about the updating procedure itself. I was wondering, what is influencing the lag between OSM update and Nominatim update. Anyway, the bug tracker is bookmarked for any potential upcoming bugs. Thank you!</p>
</div>
<div id="comment-6867-info" class="comment-info">
<span class="comment-age">(04 Aug '11, 10:31)</span> <span class="comment-user userinfo">Robiston</span>
</div>
</div>
</div>
<div id="comment-tools-6858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6858-form-container" class="comment-form-container">
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

