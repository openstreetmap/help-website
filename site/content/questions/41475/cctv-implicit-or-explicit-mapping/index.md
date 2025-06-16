+++
type = "question"
title = "CCTV - implicit or explicit mapping?"
description = '''Hi there, I&#x27;m confused about mapping CCTV / surveilance cameras: Here in Germany most of fuel stations, banks, train- or subway stations are monitored using cameras. The wiki notices that it should be used to explicitly tag the cams for this kind of objects. But isn t that redundant and &quot;implicit&quot; b...'''
date = "2015-03-03T21:48:00Z"
lastmod = "2015-03-05T21:46:00Z"
weight = 41475
keywords = [ "implicit", "tagging", "surveillance" ]
aliases = [ "/questions/41475" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [CCTV - implicit or explicit mapping?](/questions/41475/cctv-implicit-or-explicit-mapping)

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
<span id="post-41475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41475-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I'm confused about mapping CCTV / surveilance cameras: Here in Germany most of fuel stations, banks, train- or subway stations are monitored using cameras.<br />
The wiki notices that it should be used to explicitly tag the cams for this kind of objects. But isn t that redundant and "implicit" by this object categories?</p>
<p>Do you map cams at such places?</p>
<p>P.S. There doesn't seem to be a general discussion / consensus on this genereal topic <a href="https://wiki.osm.org/wiki/Category:Tagging_guidelines">at the wiki</a>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-implicit" rel="tag" title="see questions tagged &#39;implicit&#39;">implicit</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-surveillance" rel="tag" title="see questions tagged &#39;surveillance&#39;">surveillance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '15, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-41475" class="comments-container">
<span id="41483"></span>
<div id="comment-41483" class="comment">
<div id="post-41483-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Most buildings have entrances and most cities have streets, so why are we mapping them at all? ;)</p>
</div>
<div id="comment-41483-info" class="comment-info">
<span class="comment-age">(04 Mar '15, 07:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41475-form-container" class="comment-form-container">
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

<span id="41478"></span>

<div id="answer-container-41478" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41478-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="iii has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To indicate the location of a surveillance camera, you need to explicitly tag a node with <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dsurveillance">man_made=surveillance</a>. I don't see how you can implicitly mark the locations of discrete objects. For example, how would one render "there's probably a camera somewhere around here, but we're not really sure where"? That wouldn't seem very useful. :)</p>
<p>As for whether to map them, that seems like something that would be better discussed in the <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">Mailing lists</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '15, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-41478" class="comments-container">
<span id="41479"></span>
<div id="comment-41479" class="comment">
<div id="post-41479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, an implicit detection would be e.g. <a href="http://osmcamera.tk">http://osmcamera.tk</a> highlightning such objects as "under surveillance" and don't tag them as such?</p>
</div>
<div id="comment-41479-info" class="comment-info">
<span class="comment-age">(04 Mar '15, 06:11)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-41478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41478-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41480"></span>

<div id="answer-container-41480" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41480-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>as you write "most fuel stations", it means not all. So assuming that they all have camera's would be wrong, not ? And perhaps in other countries maybe only a few have camera's. And maybe in other countries all jewelries have camera's. I would go explicit mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '15, 06:29</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-41480" class="comments-container">
&#10;</div>
<div id="comment-tools-41480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41480-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41516"></span>

<div id="answer-container-41516" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41516-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The intention is to map a node of the location for each camera. <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dsurveillance">Additional tags</a> are also encouraged that describe elements such as the operating organisation of the camera (e.g. the business or the local authority) and the zone of interest.</p>
<p>Remember that OpenStreetMap data is not just used to render map images, some potential uses of CCTV data might be...</p>
<ul>
<li>How many cameras are within 10 metres of me.</li>
<li>How many cameras are in my city, state, or country.</li>
<li>In such an area, what is the number/percentage of each type of camera.</li>
<li>I saw where a camera was positioned, but who is the operator so I can get the recordings.</li>
<li>Have the cameras in an area increased or decreased over time.</li>
</ul>
<p>Some of those uses might need OpenStreetMap to be complete, others may be okay if the camera of interest happens to be mapped or an acceptable sample are mapped. However, the community likes to think about possibilities and then strives to reach the required completeness. You can help if you choose to start mapping CCTV cameras.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '15, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f846f21cfbcf60a35e1f69c2cc74df77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LivingWithDragons&#39;s gravatar image" />
<p><span>LivingWithDr...</span><br />
<span class="score" title="524 reputation points">524</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LivingWithDragons has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-41516" class="comments-container">
&#10;</div>
<div id="comment-tools-41516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41516-form-container" class="comment-form-container">
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

