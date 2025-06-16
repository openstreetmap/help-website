+++
type = "question"
title = "Satellite image accuracy"
description = '''I am new to this and started to make a local minor road in rural France near my home conform more closely to the satellite image. But then when I got to the main road I noticed it was a bit off too - and to correct it would have meant moving some buildings too! Is the satellite image always right? I...'''
date = "2012-06-07T21:51:00Z"
lastmod = "2012-06-16T21:54:00Z"
weight = 13320
keywords = [ "versus", "map", "satellite", "image", "accuracy" ]
aliases = [ "/questions/13320" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Satellite image accuracy](/questions/13320/satellite-image-accuracy)

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
<span id="post-13320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13320-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new to this and started to make a local minor road in rural France near my home conform more closely to the satellite image. But then when I got to the main road I noticed it was a bit off too - and to correct it would have meant moving some buildings too! Is the satellite image always right? If I am going to do more work on my local area I need to know which to trust.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-versus" rel="tag" title="see questions tagged &#39;versus&#39;">versus</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-satellite" rel="tag" title="see questions tagged &#39;satellite&#39;">satellite</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '12, 21:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a9cacd4f59ad17a7859c57fbb9efdbd5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oldnog&#39;s gravatar image" />
<p><span>Oldnog</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oldnog has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13320" class="comments-container">
<span id="13540"></span>
<div id="comment-13540" class="comment">
<div id="post-13540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Similar question: <a href="/questions/1200/which-is-more-reliable-gps-traces-or-aerial-imagery">https://help.openstreetmap.org/questions/1200/which-is-more-reliable-gps-traces-or-aerial-imagery</a></p>
</div>
<div id="comment-13540-info" class="comment-info">
<span class="comment-age">(14 Jun '12, 15:08)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-13320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13320-form-container" class="comment-form-container">
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

<span id="13325"></span>

<div id="answer-container-13325" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13325-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-13325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"Is the satellite image always right?" Defintely no.</p>
<p>Note what we tend to call "satellite imagery" is actually taken from aeroplanes and needs to be georeferenced and corrected for distortions caused by viewing angle of the camera and varying elevation of the ground (hills, mountains etc.).</p>
<p>Depending on well this processing is done, the imagery can have errors around dozens of meters down to a sub-meter range. This can change substantially even over short distances. For example where I live Bing imagery is quite good (sub 1m error), 10km away from here Bing has errors of over 30 meters.</p>
<p>The only way to determine if the imagery has an offset in the immediate area you are working on, is to compare it to other sources. For example:</p>
<ul>
<li>GPX tracks</li>
<li>Objects that have had their coordinates determined with high precision</li>
<li>Objects that have been imported from high accuracy sources (for example French cadastre data)</li>
</ul>
<p>Once you have determined if or if not the imagery has an offset that is large enough to need correction at least Potlatch 2 and JOSM allow you to adjust the position of background imagery.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '12, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '12, 22:15</strong> </span></p>
</div>
</div>
<div id="comments-container-13325" class="comments-container">
<span id="13322"></span>
<div id="comment-13322" class="comment">
<div id="post-13322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No the Satellite image may be a bit out of alignment. The best thing to do is collect some gps traces upload them and also use what is already been uploaded to check alignment you should then have enough to get a good average. Then if you are sure alignment is wrong it is possible to drag the aerial image so that it aligns correctly. In potlach2 just hold space bar and drag. also see this Question alignment of track vs background imagery</p>
</div>
<div id="comment-13322-info" class="comment-info">
<span class="comment-age">(07 Jun '12, 22:00)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="13350"></span>
<div id="comment-13350" class="comment">
<div id="post-13350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks to both. Can I just check then: Many of the buidings are from French cadastre information. It sounds like I can't go wrong with adjusting to conform with that?</p>
</div>
<div id="comment-13350-info" class="comment-info">
<span class="comment-age">(08 Jun '12, 12:17)</span> <span class="comment-user userinfo">Oldnog</span>
</div>
</div>
<span id="13354"></span>
<div id="comment-13354" class="comment">
<div id="post-13354-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I would check with the French community if there are any known issues in your area, but otherwise if it seems to be consistent with other information (GPS tracks mainly in this case): yes.</p>
</div>
<div id="comment-13354-info" class="comment-info">
<span class="comment-age">(08 Jun '12, 13:07)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="13374"></span>
<div id="comment-13374" class="comment">
<div id="post-13374-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I looked at this further, I found that when I matched the cadastre information on one view, all was OK and I could put the roads etc in the right place. But when I moved along a road to a new view, the two slipped out of alignment again. In other words there is no single "right" match.</p>
<p>I dealt with this by re-aligning each time I moved the map, so the new road is always in the right place relative to local buildings. It works, but there is a risk of minor errors or disjunctions along the new way.</p>
<p>My conclusion is that the cadastre information is accurate but that there is not an exact 1:1 relationship to the satellite image, in other words that the latter is slightly warped. Beam me up Scottie.</p>
</div>
<div id="comment-13374-info" class="comment-info">
<span class="comment-age">(09 Jun '12, 13:51)</span> <span class="comment-user userinfo">Oldnog</span>
</div>
</div>
<span id="13566"></span>
<div id="comment-13566" class="comment">
<div id="post-13566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... maybe <a href="https://wiki.openstreetmap.org/wiki/True_Offset_Process">https://wiki.openstreetmap.org/wiki/True_Offset_Process</a> can also help.</p>
</div>
<div id="comment-13566-info" class="comment-info">
<span class="comment-age">(16 Jun '12, 21:54)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-13325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13325-form-container" class="comment-form-container">
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

