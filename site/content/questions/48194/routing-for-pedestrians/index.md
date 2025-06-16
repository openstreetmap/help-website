+++
type = "question"
title = "Routing for pedestrians"
description = '''I want to work in pedestrian routing. I&#x27;m kinda new with osm so i would like that someone tell me the route that i have to follow. I want to do it offline first, to don&#x27;t be a &quot;problem&quot; for other people, and when my work is finished uploading to osm server in case it can help someone. I want that th...'''
date = "2016-02-17T22:02:00Z"
lastmod = "2016-03-01T20:00:00Z"
weight = 48194
keywords = [ "pedestrian", "routing" ]
aliases = [ "/questions/48194" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Routing for pedestrians](/questions/48194/routing-for-pedestrians)

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
<span id="post-48194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48194-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to work in pedestrian routing. I'm kinda new with osm so i would like that someone tell me the route that i have to follow. I want to do it offline first, to don't be a "problem" for other people, and when my work is finished uploading to osm server in case it can help someone. I want that the routing engine lead you by the sidewalk. Always the routing engines, even for pedestrians, leads people by the road. Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '16, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/5894dcb145d23eb16eec38c71ca3c716?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iTheNoob&#39;s gravatar image" />
<p><span>iTheNoob</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iTheNoob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48194" class="comments-container">
&#10;</div>
<div id="comment-tools-48194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48194-form-container" class="comment-form-container">
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

<span id="48195"></span>

<div id="answer-container-48195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48195-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-48195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <em>bad</em> way of solving this problem is generating or drawing footways for every pavement and uploading them to OSM. Don't do that!</p>
<p>The <em>good</em> way is writing a routing algorithm that will automatically create a routing graph with edges for each pavement on either side of the street, even if those are not explicitly mapped in OSM. Some work in this area has been done in the context of this project <a href="https://github.com/Nathanael-L/pedro">https://github.com/Nathanael-L/pedro</a> (a student's bachelor thesis), and their final software version is due to be committed this week. Nathanael, the author, is likely very busy these days finishing his thesis but if you contact him next week about his software, I'm sure he'll be more than happy to help. Perhaps you can even continue his work where he left off!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '16, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48195" class="comments-container">
<span id="48207"></span>
<div id="comment-48207" class="comment">
<div id="post-48207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would like to see and improve Nathanael's work, but maybe in a fute. I need to do the pedestrian routing kinda soon, so I don't have much time. The "bad way" can be made offline?</p>
</div>
<div id="comment-48207-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 17:56)</span> <span class="comment-user userinfo">iTheNoob</span>
</div>
</div>
<span id="48209"></span>
<div id="comment-48209" class="comment">
<div id="post-48209-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess so; you'll however be limited in area to something that you can still process with an offline editor e.g. JOSM or Merkaator. Then save the modified data and run a routing algorithm on it.</p>
</div>
<div id="comment-48209-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 19:58)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="48210"></span>
<div id="comment-48210" class="comment">
<div id="post-48210-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, i have already made my map on JOSM, but the question is: How can i run my map made in JOSM in an offline routing algorithm? Thank you so much, you're helping me a lot!!</p>
</div>
<div id="comment-48210-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 20:10)</span> <span class="comment-user userinfo">iTheNoob</span>
</div>
</div>
<span id="48212"></span>
<div id="comment-48212" class="comment">
<div id="post-48212-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Save your file in JOSM, then run the importer of whatever routing engine you wish to use (OSRM, GraphHopper, osm2pgrouting...). Not all of them will work out of the box with JOSM's negative IDs but nothing that a little search-and-replace on the XML cannot fix!</p>
</div>
<div id="comment-48212-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 21:42)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48446"></span>

<div id="answer-container-48446" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48446-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>look at:-</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:footway%3Dsidewalk">https://wiki.openstreetmap.org/wiki/Tag:footway%3Dsidewalk</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Sidewalk_as_separate_way">https://wiki.openstreetmap.org/wiki/Proposed_features/Sidewalk_as_separate_way</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Area/The_Future_of_Areas">https://wiki.openstreetmap.org/wiki/Area/The_Future_of_Areas</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Street_area">https://wiki.openstreetmap.org/wiki/Proposed_features/Street_area</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway">https://wiki.openstreetmap.org/wiki/Proposed_features/area:highway</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Proposed_features/area_highway/mapping_guidelines">https://wiki.openstreetmap.org/wiki/Proposed_features/area_highway/mapping_guidelines</a></p>
<p>these should help you get started with pedestrian level maps and routing if you follow all the links on those pages you can learn a lot on the subject. Some of it still feels new to older contributers and input so far is patchy but expanding steadily.</p>
<p>when it comes to going into buildings there are moves to use a combination of highway and special indoor tagging to discrbe things like malls, station, shops, lots of public buildings etc. They also handle multi-floored buildings with level or elevation sperated tagging though some older contributers have big problems with stacked nodes they aren't technicaly not allowed are needed in cirtain places with these new schemes such as entrance doors to flats in highrise blocks for instance...</p>
<p>some infomation can be found on wiki searches on indoor mapping such as:-</p>
<p><a href="https://wiki.openstreetmap.org/w/index.php?title=Special%3ASearch&amp;profile=default&amp;search=indoor&amp;fulltext=Search">https://wiki.openstreetmap.org/w/index.php?title=Special%3ASearch&amp;profile=default&amp;search=indoor&amp;fulltext=Search</a> <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging</a> <a href="https://wiki.openstreetmap.org/wiki/Indoor_Mapping">https://wiki.openstreetmap.org/wiki/Indoor_Mapping</a></p>
<p>by resurching through the above you can a lean a lot about how others have been doing what you are trying to map.</p>
<p>incedentaly its a area I also try to focus on in my contributions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '16, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Mar '16, 20:03</strong> </span></p>
</div>
</div>
<div id="comments-container-48446" class="comments-container">
&#10;</div>
<div id="comment-tools-48446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48446-form-container" class="comment-form-container">
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

