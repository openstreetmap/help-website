+++
type = "question"
title = "To join or not join ways"
description = '''Hi  I am unsure how the section between two roads should be mapped. I initially mapped it as two separate road endings, but another mapper joined the two ends at this changeset with &quot;Connecting motorable roads using #to-fix https://github.com/mapbox/mapping/issues/105&quot; comment, so I then disconnecte...'''
date = "2016-12-01T03:01:00Z"
lastmod = "2017-01-21T03:27:00Z"
weight = 53186
keywords = [ "editing", "barrier" ]
aliases = [ "/questions/53186" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [To join or not join ways](/questions/53186/to-join-or-not-join-ways)

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
<span id="post-53186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53186-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi<br />
I am unsure how <a href="https://www.openstreetmap.org/#map=19/-27.22085/153.03156">the section between two roads</a> should be mapped. I initially mapped it as two separate road endings, but another mapper joined the two ends at this <a href="https://www.openstreetmap.org/changeset/44014136">changeset</a> with "Connecting motorable roads using #to-fix <a href="https://github.com/mapbox/mapping/issues/105">https://github.com/mapbox/mapping/issues/105"</a> comment, so I then disconnected the way and put a row of bollards between. But another experienced mapper has rejoined the ends with this <a href="https://www.openstreetmap.org/changeset/44045421">changeset</a> and comment "Ways need to join to allow for no-vehicle traffic pass. Converted bollard to node."</p>
<p>I don't think this is correctly mapped and the individual ways should not be joined as there is no join in reality on the ground.</p>
<p>There is a short cement driveway at the very end the each way end, which I am not in the habit of mapping very often as all new residential developments have too many of them. This problem has come up and two experienced editors have felt that the two ends need to be joined.<br />
Should I now edit the map to recreate the gap between the road endings but also spit the roads to add the short driveway sections?<br />
If I had ended each way before the cement driveways begin, would the problem arise?<br />
Where there is a small physical gap would it be best practice to add the tag noexit=yes to the end node.</p>
<p><img src="http://help.openstreetmap.org/upfiles/bollards_5o0LZbG.JPG" alt="alt text" /></p>
<p><img src="http://help.openstreetmap.org/upfiles/block.png" alt="Mapbox" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '16, 03:01</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</img>
</div>
</div>
<div id="comments-container-53186" class="comments-container">
<span id="53203"></span>
<div id="comment-53203" class="comment">
<div id="post-53203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have remapped the site to include the concrete surface sections as driveways instead of highway=residential, split the section where the row of bollards are located, and the footway adjacent the split driveways has bicycle=yes tag added. I decided not to add noexit=yes to the last node of the driveways as this would seem to be self evident on a driveway. Thanks to everyone for the advice.</p>
</div>
<div id="comment-53203-info" class="comment-info">
<span class="comment-age">(02 Dec '16, 02:09)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="53205"></span>
<div id="comment-53205" class="comment">
<div id="post-53205-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One of the reasons for adding the noexit tag is to indicate to other OSM mappers that you have investigated the way and found it to have no outlet to another way. I use it mostly for that purpose. I don't think most routers pay attention to it because that last node has no connecting way so it leads nowhere. However, I was surprised to observe that OSMand does have a unique icon for such nodes.</p>
</div>
<div id="comment-53205-info" class="comment-info">
<span class="comment-age">(02 Dec '16, 05:58)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="53209"></span>
<div id="comment-53209" class="comment">
<div id="post-53209-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>After re-reading the Wiki, I have reconsidered and added the noexit=yes tags to make it clear to other mappers.</p>
</div>
<div id="comment-53209-info" class="comment-info">
<span class="comment-age">(02 Dec '16, 08:03)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-53186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53186-form-container" class="comment-form-container">
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

<span id="53188"></span>

<div id="answer-container-53188" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53188-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Clearly, the roads are not connected in a way that vehicles can use them. I think your initial approach was valid. I don't know why the other user would have said "Connecting motorable roads" when it seems so obviously not the case. Not only are those ways not "motorable", there isn't even a footway connecting them. I would put a noexit=yes tag on each of those driveway end nodes or simply not map them at all.</p>
<p>Plus, I suppose you should contact those other mappers to try to understand why they did what they did.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '16, 05:10</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span> </br></br></p>
</img>
</div>
</div>
<div id="comments-container-53188" class="comments-container">
<span id="53192"></span>
<div id="comment-53192" class="comment">
<div id="post-53192-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>@AlakaDave "Connecting motorable roads" is a task from to-fix which is mainly used by Mapbox employees.</p>
<p><a href="http://help.openstreetmap.org/users/7380/nevw">@nevw</a> you can complain directly to Mapbox if necessary, their employees tend to be overzealous now and then.</p>
</div>
<div id="comment-53192-info" class="comment-info">
<span class="comment-age">(01 Dec '16, 09:11)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="54220"></span>
<div id="comment-54220" class="comment">
<div id="post-54220-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well I don't know why the first user made their edit (whack-a-mole perhaps?). But my edit was intended to indicate that non-vehicle (note typo) traffic can pass through. At the time the footpath was not tagged bicycle=yes so there was no way for them to get through. I had forgotten that riding on footpaths is legal in QLD so I would have retagged the path if I had.</p>
</div>
<div id="comment-54220-info" class="comment-info">
<span class="comment-age">(21 Jan '17, 03:27)</span> <span class="comment-user userinfo">TheSwavu</span>
</div>
</div>
</div>
<div id="comment-tools-53188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53188-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53189"></span>

<div id="answer-container-53189" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53189-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Can pedestrians go from one side to the other ? I think so from your pictures, so I would add a highway=footpath between the 2 ends. This footpath will have represent the concrete path in front and part of the driveway.</p>
<p>Another solution is to map the footpath completely as a separate line. In this case you could map all connections to the street via the driveways or not bother with the street connections at all.</p>
<p>I would not map the noexit=yes tag when pedestrians (and probably cyclist) can move from one end to the other.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '16, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-53189" class="comments-container">
<span id="53191"></span>
<div id="comment-53191" class="comment">
<div id="post-53191-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have mapped the footway as separate from the road as the only connections to the roads are as mapped and it is expected that pedestrians only use the footways where provided in that vicinity. I think this is preferred over the sidewalk tag here because there is a gap between the road/driveways. Cyclists are permitted to ride on footways in this state. I will add the bicycle=yes to this footway too.<br />
<a href="https://www.openstreetmap.org/#map=19/-27.22085/153.03156">https://www.openstreetmap.org/#map=19/-27.22085/153.03156</a><br />
I think adding noexit=yes tags to the end node of the roads over-complicates the mapping here, but reading the wiki on the tag does indicate that this is an instance where it may be useful. <a href="http://wiki.openstreetmap.org/wiki/Key:noexit">http://wiki.openstreetmap.org/wiki/Key:noexit</a></p>
</div>
<div id="comment-53191-info" class="comment-info">
<span class="comment-age">(01 Dec '16, 08:52)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="53193"></span>
<div id="comment-53193" class="comment">
<div id="post-53193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi nevw, there sturdy fences on both ends and bollards in the middle are there just to prevent motor_vehicles passing from one road to the other. And they even build a zone with buches as an accent, filled with bollards. Even the footway with bicycle=yes has a cycle barrier on both ends just to slow down speeding bicycles onto the main road.</p>
</div>
<div id="comment-53193-info" class="comment-info">
<span class="comment-age">(01 Dec '16, 10:38)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-53189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53189-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53341"></span>

<div id="answer-container-53341" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53341-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that there are no ways for anything to pass through. Just map it as noexit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-53341" class="comments-container">
<span id="53347"></span>
<div id="comment-53347" class="comment">
<div id="post-53347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did, :) see earlier comment and the link to the map. The no_exit does not render on the standard layers offered at openstreetmap.org but serves it's design purpose well.</p>
</div>
<div id="comment-53347-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 09:04)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-53341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53341-form-container" class="comment-form-container">
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

