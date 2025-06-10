+++
type = "question"
title = "Missouri River Boundary Anomaly Near Jefferson City, Missouri"
description = '''I&#x27;m new to OSM. I&#x27;m using garmin.openstreetmap.nl for routable roads on my Garmin Dakota 20 GPS, and I have found this anomaly for the Missouri River near the town of Jefferson City, Missouri--where I live. I&#x27;ve taken some screenshots from Base Camp (Garmin&#x27;s map management software), to illustrate ...'''
date = "2012-05-29T10:51:00Z"
lastmod = "2012-06-06T16:37:00Z"
weight = 13057
keywords = [ "osm", "routable", "river", "garmin", "riverbank" ]
aliases = [ "/questions/13057" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Missouri River Boundary Anomaly Near Jefferson City, Missouri](/questions/13057/missouri-river-boundary-anomaly-near-jefferson-city-missouri)

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
<span id="post-13057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13057-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM. I'm using garmin.openstreetmap.nl for routable roads on my Garmin Dakota 20 GPS, and I have found this anomaly for the Missouri River near the town of Jefferson City, Missouri--where I live.</p>
<p>I've taken some screenshots from Base Camp (Garmin's map management software), to illustrate the anomaly:</p>
<p><a href="http://www.panoramio.com/photo_explorer#view=photo&amp;position=0&amp;with_photo_id=72790355&amp;order=date_desc&amp;user=6944431">Detail-1</a></p>
<p><a href="http://www.panoramio.com/photo_explorer#view=photo&amp;position=1&amp;with_photo_id=72790350&amp;order=date_desc&amp;user=6944431">Detail-2</a></p>
<p>If anyone can help me with this, I'd appreciate it.</p>
<p>--Stephen</p>
<p>P.S. Please see the following screenshot, taken of OSM Inspector, for: Error: Invalid Geometry relation #933167 -- This looks like it might have something to do with it:</p>
<p><a href="http://www.panoramio.com/photo_explorer#view=photo&amp;position=0&amp;with_photo_id=72867196&amp;order=date_desc&amp;user=6944431">OSM Inspector Screenshot</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routable" rel="tag" title="see questions tagged &#39;routable&#39;">routable</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 May '12, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0259291440feb20492c5df693dc8612e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishe&#39;s gravatar image" />
<p><span>Firefishe</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '12, 11:13</strong> </span></p>
</div>
</div>
<div id="comments-container-13057" class="comments-container">
&#10;</div>
<div id="comment-tools-13057" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13057-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="13074"></span>

<div id="answer-container-13074" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13074-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had to look at OSM Inspector for a bit, but I eventually found some red Xs that indicated a self-intersecting way (28996041) that is part of that relation. I've fixed that, so hopefully it'll render correctly in the future. You can check OSMI tomorrow and the error for that relation should be gone, unless there's another error with it!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '12, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-13074" class="comments-container">
<span id="13109"></span>
<div id="comment-13109" class="comment">
<div id="post-13109-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>neuhausr,</p>
<p>Thank you for correcting the data. I appreciate you taking the time and applying your experience to my issue.</p>
<p>As soon as garmin.openstreetmap.nl is updated, I will be able to see if the problem is resolved.</p>
<p>Thank you for your assistance, neuhausr. I appreciate it! Oh, and as an aside: Points Given :-)</p>
<p>Best Regards, Stephen Brown/Firefishe</p>
</div>
<div id="comment-13109-info" class="comment-info">
<span class="comment-age">(30 May '12, 02:00)</span> <span class="comment-user userinfo">Firefishe</span>
</div>
</div>
</div>
<div id="comment-tools-13074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13074-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13086"></span>

<div id="answer-container-13086" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13086-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you happen to have the Kansas River loaded up in your existing data? If so, could you look and see if there is any of this flooding along it? This is the relation that represents it:</p>
<p><a href="http://www.openstreetmap.org/browse/relation/1061544">http://www.openstreetmap.org/browse/relation/1061544</a></p>
<p>I'm trying to see if the garmin rendering has problems with the way some rivers are mapped.</p>
<p>Also, keep in mind that the data from garmin.openstreetmap.nl is not kept constantly up to date. It is refreshed periodically and hasn't been updated since April 1st so any fixes that people have made to the river won't show up until an update is run.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '12, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/43ae79d3345e19f30ea5f2ea64a9f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToeBee&#39;s gravatar image" />
<p><span>ToeBee</span><br />
<span class="score" title="976 reputation points">976</span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToeBee has 6 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-13086" class="comments-container">
<span id="13111"></span>
<div id="comment-13111" class="comment">
<div id="post-13111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ToeBee,</p>
<p>Thank you for the validation of the update issue with garmin.openstreetmap.nl. This helps me to understand what I needed to know, relative to that portion of my inquiry.</p>
<p>Now, relative to your query regarding the Kansas River. I downloaded the proper portion from garmin.openstreetmap.nl, and installed it to BaseCamp.</p>
<p>I started from the western terminus, and went all the way across to the eastern terminus, then back the other way, at two different detail levels. I detected no trace of rendering the type of "flooding" I experienced near Jefferson City, or in any other way.</p>
</div>
<div id="comment-13111-info" class="comment-info">
<span class="comment-age">(30 May '12, 02:18)</span> <span class="comment-user userinfo">Firefishe</span>
</div>
</div>
<span id="13112"></span>
<div id="comment-13112" class="comment">
<div id="post-13112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In short, the entirety of the Kansas River, relative to garmin.openstreetmap.nl and BaseCamp, indicates that it is properly rendered. (This, of course, reflects current data on garmin.openstreetmap.nl. If OSM/OSMI is showing something more current, then any "flooding," if present as of today (5/29/2012), will not show up, of course, until the data is updated on garmin.openstreetmap.nl.</p>
<p>I would trust, however, that since I am not finding any flooding or rendering problems with the Kansas River, as indicated, that there will be no problems in the future. One can hope, anyway ;-).</p>
</div>
<div id="comment-13112-info" class="comment-info">
<span class="comment-age">(30 May '12, 02:19)</span> <span class="comment-user userinfo">Firefishe</span>
</div>
</div>
<span id="13113"></span>
<div id="comment-13113" class="comment">
<div id="post-13113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hope this helps you. Please feel free to drop me an email directly at firefishe AT gmail DOT com if you'd like; I'd be happy to answer any questions you have, as well as doing any experimentation with my Dakota 20 and BaseCamp, as needed.</p>
<p>Oh, and as an aside: Points Given :-) Thanks again!</p>
<p>Best Regards, Stephen Brown/Firefishe</p>
</div>
<div id="comment-13113-info" class="comment-info">
<span class="comment-age">(30 May '12, 02:20)</span> <span class="comment-user userinfo">Firefishe</span>
</div>
</div>
<span id="13279"></span>
<div id="comment-13279" class="comment">
<div id="post-13279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for looking. That would seem to indicate that the garmin translation/rendering stack does indeed handle large riverbank relations correctly so hopefully it was just the self-intersecting ways that were causing the problems for you. Guess We'll just have to wait for an update and see if it goes away. Or if you're looking for a challenge you can try your hand at using mkgmap to make your own garmin maps from OSM data :)</p>
</div>
<div id="comment-13279-info" class="comment-info">
<span class="comment-age">(06 Jun '12, 16:37)</span> <span class="comment-user userinfo">ToeBee</span>
</div>
</div>
</div>
<div id="comment-tools-13086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13086-form-container" class="comment-form-container">
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

