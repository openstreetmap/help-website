+++
type = "question"
title = "How can I define the direction of a speed camera"
description = '''Hello, 1) There is a street for both direction. How can I define in which direction the speed camera is active? 2) Is it better to do a point on the street or beside the street? Thanks for helping hand'''
date = "2014-08-12T12:42:00Z"
lastmod = "2014-08-12T16:15:00Z"
weight = 35748
keywords = [ "definition", "direction", "speed_camera", "tagging", "mapping" ]
aliases = [ "/questions/35748" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I define the direction of a speed camera](/questions/35748/how-can-i-define-the-direction-of-a-speed-camera)

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
<span id="post-35748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35748-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>1) There is a street for both direction. How can I define in which direction the speed camera is active? 2) Is it better to do a point on the street or beside the street?</p>
<p>Thanks for helping hand</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-definition" rel="tag" title="see questions tagged &#39;definition&#39;">definition</span> <span class="post-tag tag-link-direction" rel="tag" title="see questions tagged &#39;direction&#39;">direction</span> <span class="post-tag tag-link-speed_camera" rel="tag" title="see questions tagged &#39;speed_camera&#39;">speed_camera</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '14, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/acbecbbb7015b7f8434f879db6f142a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Phipsiii&#39;s gravatar image" />
<p><span>Phipsiii</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Phipsiii has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '14, 13:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35748" class="comments-container">
<span id="35755"></span>
<div id="comment-35755" class="comment">
<div id="post-35755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help.</p>
<p>I'm not sure if I understood the Wiki correct. But please have a look.</p>
<p>I have found a speed_camera inside OSM here, but if I understand it correct, this one is not correct inside OSM: <a href="https://www.openstreetmap.org/edit?way=296449989#map=21/48.18224/16.31885">https://www.openstreetmap.org/edit?way=296449989#map=21/48.18224/16.31885</a></p>
<p>So I added my first own speed_camera here. This is a speed camera like "Example 3c" (Speed camera making pictures from the back). This camera makes pictures from cars, which drives from Buckalgasse to Löwenthalgasse. <a href="https://www.openstreetmap.org/edit?way=289875094#map=20/48.13317/16.27551">https://www.openstreetmap.org/edit?way=289875094#map=20/48.13317/16.27551</a></p>
<p>Is it correct or what do I need to change?</p>
<p>Thanks!</p>
</div>
<div id="comment-35755-info" class="comment-info">
<span class="comment-age">(12 Aug '14, 14:20)</span> <span class="comment-user userinfo">Phipsiii</span>
</div>
</div>
<span id="35756"></span>
<div id="comment-35756" class="comment">
<div id="post-35756-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>You have the relation tags on the camera node. You are using iD as your editor and the relation page doesn't include an example on how to do it using iD, but if you put the camera tags on the point object, then under All Relations beneath the list of tags, click + and create a new relation, set the type to enforcement, add the other tags, then select in turn the from and to nodes in the highway and click + to add them to that relation (set roles next to the list of members). Edit: I tried to make a video <a href="http://www.flickr.com/photos/edloach/14709835920/">http://www.flickr.com/photos/edloach/14709835920/</a></p>
</div>
<div id="comment-35756-info" class="comment-info">
<span class="comment-age">(12 Aug '14, 14:31)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="35762"></span>
<div id="comment-35762" class="comment">
<div id="post-35762-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you, your video was very helpful for me! Now I changed my first speed_camera. Please can you have a look again. <a href="https://www.openstreetmap.org/edit?way=289875094#map=19/48.13333/16.27561">https://www.openstreetmap.org/edit?way=289875094#map=19/48.13333/16.27561</a></p>
</div>
<div id="comment-35762-info" class="comment-info">
<span class="comment-age">(12 Aug '14, 16:15)</span> <span class="comment-user userinfo">Phipsiii</span>
</div>
</div>
</div>
<div id="comment-tools-35748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35748-form-container" class="comment-form-container">
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

<span id="35749"></span>

<div id="answer-container-35749" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35749-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-35749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Phipsiii has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I use OsmAnd and the cameras I have mapped as nodes at the side of the road have not triggered the warning that nodes as part of the way do. However, checking the wiki page for <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dspeed_camera">speed camera</a> suggests that OsmAnd now processes <a href="https://wiki.openstreetmap.org/wiki/Relation:enforcement">enforcement relations</a>, which looks like a more complicated but more accurate way of mapping speed cameras.</p>
<p>If I've read if correctly, you would:</p>
<ol>
<li>add a highway=speed_camera node where the camera is (e.g. side of the road)</li>
<li>position nodes in the way which mark the start and end of the section of way that the camera covers (e.g. the start and end of any markings on the road, perhaps)</li>
<li>create a new relation, set type to enforcement, add the camera node with role "device" and add the way nodes with roles "from" and "to"</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '14, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-35749" class="comments-container">
<span id="35751"></span>
<div id="comment-35751" class="comment">
<div id="post-35751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is not "how to map for OsmAnd" in the question. ;-) Anyway, thanks for the info what this (big) data user understands and what not.</p>
</div>
<div id="comment-35751-info" class="comment-info">
<span class="comment-age">(12 Aug '14, 13:47)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="35752"></span>
<div id="comment-35752" class="comment">
<div id="post-35752-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The enforcement relation hasn't been created for OsmAnd explicity. OsmAnd is just one (very) popular application which is actually able to use it.</p>
</div>
<div id="comment-35752-info" class="comment-info">
<span class="comment-age">(12 Aug '14, 14:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35749-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35750"></span>

<div id="answer-container-35750" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35750-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>1) See the wiki: "Consider using the enforcement relation to provide more information about the speed camera." (<span>Tag:highway=speed_camera</span>) Click through there and read the info. It is what you are searching for. Also see the <span>examples</span> in the original proposal]. However, note that there were quite some opposing votes in this proposal, so not everybody may think this is the best way (I personally know no other way).</p>
<p>2) Both is possible. See 1.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '14, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-35750" class="comments-container">
&#10;</div>
<div id="comment-tools-35750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35750-form-container" class="comment-form-container">
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

