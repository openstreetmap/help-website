+++
type = "question"
title = "Editing/moving clusters of objects"
description = '''Hello. I&#x27;m trying to update areas around Nuuk in Greenland (the Quinngorput area).  There, the area is offset from its true location by about 30-50 meters. This is due to the underlying satellite imagery being offset as well. So when roads, buildings and so have been drawn in, the error has been inh...'''
date = "2020-01-27T08:30:00Z"
lastmod = "2020-01-27T16:25:00Z"
weight = 72708
keywords = [ "editing", "moving", "bulk_editing" ]
aliases = [ "/questions/72708" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Editing/moving clusters of objects](/questions/72708/editingmoving-clusters-of-objects)

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
<span id="post-72708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72708-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. I'm trying to update areas around Nuuk in Greenland (the Quinngorput area).</p>
<p>There, the area is offset from its true location by about 30-50 meters. This is due to the underlying satellite imagery being offset as well. So when roads, buildings and so have been drawn in, the error has been inherited. However, the placement of everything related to eachother in that area is right.</p>
<p>The error starts to appear along the way from the west to the east side of fjord there. It would be easy to cut off the road in the middle, properly align the satellite imagery, and then move all the objects on the east side to the right place. As there are several roads with roundaabouts and bicycle roads too, it's near impossible to mark every little segment by individually clicking it. Instead, I would need an area markup, as in "mark everything up in the area I've selected". The road could then be manuallt stiched together.</p>
<p>The other way is to manually move every object manually, which will take hours of work.</p>
<p>However, I can't find a way to do that "area markup mass move" in the editor I'm using. Is there one?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-moving" rel="tag" title="see questions tagged &#39;moving&#39;">moving</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '20, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/06e58c824cbd2c78c3365b31ea790695?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAA71&#39;s gravatar image" />
<p><span>JAA71</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAA71 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '20, 10:23</strong> </span></p>
</div>
</div>
<div id="comments-container-72708" class="comments-container">
<span id="72709"></span>
<div id="comment-72709" class="comment">
<div id="post-72709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which editor are you using? What are you using as the basis for the 'true' location?</p>
</div>
<div id="comment-72709-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 08:45)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="72711"></span>
<div id="comment-72711" class="comment">
<div id="post-72711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's the ID editor. I use three playgrounds as calibration spots.</p>
<p>Today, when I checked the area up, the sat imagery seem to have been rectified. I moved a bit of the area, just to see if it aligns properly with the true locations. The first one should be located at 64.172372, -51.672523.</p>
</div>
<div id="comment-72711-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 09:44)</span> <span class="comment-user userinfo">JAA71</span>
</div>
</div>
<span id="72715"></span>
<div id="comment-72715" class="comment">
<div id="post-72715-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The other two are placed at 64.169821, -51.670944 and 64.169501, -51.669784. One of the background images is still off. The two differing are Bing and Mapbox. The move I made was to match the Bing image (Taqissorfik area). When the online map updates, I'll see if it matches better.</p>
</div>
<div id="comment-72715-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 11:27)</span> <span class="comment-user userinfo">JAA71</span>
</div>
</div>
<span id="72719"></span>
<div id="comment-72719" class="comment">
<div id="post-72719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sadly, is seems that both are off. The only data I've found is the Google satellite pics, but they can't be used in OSM as they are copyrighted. Is there a way to insert calibration points into OSM using exact coordinates, so I can move the Bing/Mapbox pics instead?</p>
</div>
<div id="comment-72719-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 16:25)</span> <span class="comment-user userinfo">JAA71</span>
</div>
</div>
</div>
<div id="comment-tools-72708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72708-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

