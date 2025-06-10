+++
type = "question"
title = "Best practice for mapping ~5-month road closure with approximate end date?"
description = '''In this part of the map, the westbound lanes of Randolph Road are closed for construction from Parklawn Drive to Nebel Street until 2022-02-07, according to a sign I saw there on 2021-08-20. However, the sign has been removed since then, and I wouldn&#x27;t be surprised if the end date changes by as much...'''
date = "2021-09-06T18:28:00Z"
lastmod = "2021-09-09T06:55:00Z"
weight = 81647
keywords = [ "road_closure", "construction", "conditional" ]
aliases = [ "/questions/81647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best practice for mapping ~5-month road closure with approximate end date?](/questions/81647/best-practice-for-mapping-5-month-road-closure-with-approximate-end-date)

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
<span id="post-81647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81647-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In <a href="https://www.openstreetmap.org/#map=18/39.05292/-77.10858&amp;layers=N">this part of the map</a>, the westbound lanes of Randolph Road are closed for construction from Parklawn Drive to Nebel Street until 2022-02-07, according to a sign I saw there on 2021-08-20. However, the sign has been removed since then, and I wouldn't be surprised if the end date changes by as much as a few weeks based on unpredictable factors affecting the progress of the construction project.</p>
<p>I'd like to map this closure in some form to help routers. I understand that there are two general approaches:</p>
<ol>
<li>Edit the ways (in this case, make them one-way eastbound rather than <code>highway=construction</code>) and edit them back once I confirm the lanes have reopened.</li>
<li>Use time-based restrictions: something like <code>oneway:conditional=yes @ 2021 Sep 06-2022 Feb 07</code>.</li>
</ol>
<p>On <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dconstruction">this wiki page</a>, <a href="https://help.openstreetmap.org/questions/69620/closing-the-road">one question</a>, and <a href="https://help.openstreetmap.org/questions/66384/what-are-the-current-practices-for-road-closures">another question</a>, I see that there are trade-offs and some debate about how to weigh the competing considerations and consequently what the best practice should be. If I'm certain of the end date (as well as the desired state of the map after that date, which I am in this case), then #2 is almost certainly better. But here I'm not completely certain of the end date, and at approximately 5 months, the length of the closure falls near the threshold that several users have said should decide between #1 and #2. Not finding any obvious local precedent, I believe I'm probably allowed the discretion to map the closure either way, but I thought it would be a good opportunity to solicit some more opinions here first. (Let me know if I should take this discussion to another place.)</p>
<p>Re "The original mapper may move or change hobbies by the time construction completes. The road will permanently be marked closed until someone else happens to notice": I hope I've already built some credibility by promptly <a href="https://www.openstreetmap.org/changeset/110811542">reopening</a> one closure for which I used approach #1, though of course, the community has the right not to believe me. The other serious concern with #1 is the concern that clients that use old data could see the road as closed for much longer than it actually is.</p>
<p>But ISTM #2 has problems of its own if the closure continues past the end date I originally enter: clients will start trying to route over the closed road until I have time to re-survey it and update the end date on OSM. If a new end date is not announced, I'm left to guess. In the worst case, ISTM we could end up with the road oscillating between open and closed from OSM's point of view, as I make a series of artificial updates to the guessed end date on OSM to try to keep up.</p>
<p>So I'd like a better sense of what is the least evil here and, if I go with #2, whether there's anything I can do to help manage the potential problem. (Might it make sense to deliberately enter an end date in OSM that is several weeks after the announced date and then update OSM if the road reopens before then?) I get the sense that the community doesn't have great data on how many users are using what update cycle for OSM data and how badly they would be affected by their app showing them a false positive versus a false negative road closure. I'd guess that a false positive (a suboptimal route) is less annoying than a false negative (being routed on a closed road and having to find a detour on the spot, though in this case, signs are posted for an adequate detour, so the impact would effectively just be a suboptimal route by the time the user takes the signed detour). But this is just based on my own experience as a user of OsmAnd with weekly live updates; I can't speak for all OSM clients.</p>
<p><strong>Update 2021-09-08:</strong> Another problem with #2 is that some (most?) popular routers don't support <code>oneway:conditional</code>. OsmAnd does; I tested OSRM and it doesn't; and I think Valhalla doesn't based on a look at the source code. I don't know how heavily this consideration should be weighed. For now, I've <a href="https://www.openstreetmap.org/changeset/110931126">gone ahead</a> and used #2 with the OSM end date set to the originally signed end date of 2022-02-07, since I can't think of any sense in which that could be argued to be worse than the status quo, even if it isn't an ideal solution.</p>
<p>Thanks for your attention!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-road_closure" rel="tag" title="see questions tagged &#39;road_closure&#39;">road_closure</span> <span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '21, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a09c08e1ae93a83e9102b6715fc75b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt%20McCutchen&#39;s gravatar image" />
<p><span>Matt McCutchen</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt McCutchen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '21, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-81647" class="comments-container">
&#10;</div>
<div id="comment-tools-81647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81647-form-container" class="comment-form-container">
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

<span id="81695"></span>

<div id="answer-container-81695" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81695-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>3</strong> There is also a third option. Oneway are mostly because of a oneway traffic_sign. But when other prohibited signs are used, you can get a similar effect.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">https://wiki.openstreetmap.org/wiki/Conditional_restrictions</a></p>
<p>you can use the direction</p>
<p>access:forward:conditional=yes @ (2021 Sep 06-2022 Feb 07) access:backward:conditional=no @ (2021 Sep 06-2022 Feb 07)</p>
<p>oneway:conditional -1 @ 2021 Sep 07-2022 Feb 07<br />
You did not use @ ( )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '21, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/6c5dc0fc3be6786b643d15ec99ba3e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allroads&#39;s gravatar image" />
<p><span>Allroads</span><br />
<span class="score" title="222 reputation points">222</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allroads has one accepted answer">10%</span> </br></p>
</div>
</div>
<div id="comments-container-81695" class="comments-container">
<span id="81697"></span>
<div id="comment-81697" class="comment">
<div id="post-81697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting idea. I can see how <code>access:{forward,backward}:conditional</code> could be philosophically a better way to model the data, but is it actually accepted practice on OSM? Does any router actually support it? I tried loading a custom OSM file into OsmAnd and it doesn't support <code>access:{forward,backward}</code>, let alone <code>access:{forward,backward}:conditional</code>. And the use of all these tags on taginfo is tiny compared to <code>oneway:conditional</code>. So I think <code>oneway:conditional</code> is more practical than <code>access:{forward,backward}:conditional</code> for now. Both approaches present the same issues related to getting the end time right.</p>
<p>Re parentheses around the condition: you are right, that is best practice according to <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions#Condition.">https://wiki.openstreetmap.org/wiki/Conditional_restrictions#Condition.</a> Fixed in <a href="https://www.openstreetmap.org/changeset/110939263.">https://www.openstreetmap.org/changeset/110939263.</a></p>
</div>
<div id="comment-81697-info" class="comment-info">
<span class="comment-age">(08 Sep '21, 22:31)</span> <span class="comment-user userinfo">Matt McCutchen</span>
</div>
</div>
<span id="81699"></span>
<div id="comment-81699" class="comment">
<div id="post-81699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a supported (eg by Graphhopper) practice, not necessary "best practice". Opposing argument in eg <a href="https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/temporary_(conditional)#Why_not_:conditional?">https://wiki.openstreetmap.org/wiki/Talk:Proposed_features/temporary_(conditional)#Why_not_:conditional?</a> .</p>
</div>
<div id="comment-81699-info" class="comment-info">
<span class="comment-age">(09 Sep '21, 06:55)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-81695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81695-form-container" class="comment-form-container">
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

