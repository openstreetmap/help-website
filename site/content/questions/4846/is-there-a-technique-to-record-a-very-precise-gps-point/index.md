+++
type = "question"
title = "Is there a technique to record a very precise GPS point?"
description = '''My understanding is that most GPS units (like the one built-in to my iPhone) can only resolve a point to a confidence of roughly 5 metres, even on the clearest of days. Can this be improved upon without splashing out on a pricey Differential GPS unit? I wondered if perhaps I/someone could write an a...'''
date = "2011-04-27T11:18:00Z"
lastmod = "2013-04-06T11:28:00Z"
weight = 4846
keywords = [ "aerial", "gps" ]
aliases = [ "/questions/4846" ]
osqa_answers = 7
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a technique to record a very precise GPS point?](/questions/4846/is-there-a-technique-to-record-a-very-precise-gps-point)

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
<span id="post-4846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4846-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-4846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My understanding is that most GPS units (like the one built-in to my iPhone) can only resolve a point to a confidence of roughly 5 metres, even on the clearest of days.</p>
<p>Can this be improved upon without splashing out on a pricey <a href="http://en.wikipedia.org/wiki/Differential_GPS">Differential GPS</a> unit?</p>
<p>I wondered if perhaps I/someone could write an app that took multiple readings over a given time and then found the statistical mean. Assuming the errors are spread across a <a href="http://en.wikipedia.org/wiki/Normal_distribution">normal distribution</a> around the actual point then this should result in a more accurate position, or am I missing something?</p>
<p>Having very accurately recorded locations for visible landmarks would then hopefully help with aerial image alignment and rectification.</p>
<p>Also any suggestions for how such a point might be tagged?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aerial" rel="tag" title="see questions tagged &#39;aerial&#39;">aerial</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '11, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '11, 11:26</strong> </span></p>
</div>
</div>
<div id="comments-container-4846" class="comments-container">
&#10;</div>
<div id="comment-tools-4846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4846-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="4851"></span>

<div id="answer-container-4851" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4851-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-4851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GrahamS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can reduce the error by taking multiple readings. However to get an error radius of one meter or better you will need hundreds of meassurements taken over the course of days.</p>
<p>DGPS will reduce the error of both a single reading and timeseries but it doesn't do magic.</p>
<p>Survey grade receivers use the other frequencies of GPS (even if they can't decrypt them) and allow a precession in the range of centimeters but are expensive.</p>
<p>In france thousands of survey points from a goverment import exist and are tagged with <code>man_made=survey_point</code>. For your gps reference points I'd suggest <code>man_made=reference_point</code> along with <code>source=gps</code> and a short <code>note</code> how you measured the position.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '11, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-4851" class="comments-container">
<span id="4871"></span>
<div id="comment-4871" class="comment">
<div id="post-4871-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>It depends on the site conditions, I doubt hundreds of measurements will help if you don't have a clear view of sky. Even in cities tracks are sometimes distorted around tall buildings, so every measurement has significant error in one direction.</p>
</div>
<div id="comment-4871-info" class="comment-info">
<span class="comment-age">(28 Apr '11, 06:41)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="4873"></span>
<div id="comment-4873" class="comment">
<div id="post-4873-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Agreed. You should have direct line of sight to at least five satellites and no signals via reflections. The multiple measurements and averaging are to get rid of the uncertainty that comes from the propagation effects up in the ionosphere, not from systematic distrosions due to urban canyon effect and so on.</p>
</div>
<div id="comment-4873-info" class="comment-info">
<span class="comment-age">(28 Apr '11, 07:02)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="4878"></span>
<div id="comment-4878" class="comment">
<div id="post-4878-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>As above, but you could also consider enabling WAAS/EGNOS if your GPS has it, and you are in an area where it improves the accuracy (probably only western Europe and continental USA). Many Garmin units have this, although iPhone does not.</p>
</div>
<div id="comment-4878-info" class="comment-info">
<span class="comment-age">(28 Apr '11, 08:25)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
</div>
<div id="comment-tools-4851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4851-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4967"></span>

<div id="answer-container-4967" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4967-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also improve your results if your device allows to store the raw measurements. You can then later download from the internet correctional data for the given time/date and apply postprocessing to your measurement data (to eliminate/reduce the ionosphere effects).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '11, 17:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-4967" class="comments-container">
&#10;</div>
<div id="comment-tools-4967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4987"></span>

<div id="answer-container-4987" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4987-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just tried an experiment I thought should work. if i walked while sighting along a wall of a building I could align this trace on bing when editing i then turned 90 degrees when my position lined up with another building line. I then drew two straight ways in potlatch two along the mean of these ways to beyond the sides of the buildings observed. I then dragged the bing to agree with these alignments,ok so far but I found that after scrolling the map just 200 meters it was out of alignment.so no better then doing minor adjustments as mis-alignment show up. thought this may give others some ideas.here's the trace <a href="http://www.openstreetmap.org/user/andy%20mackey/traces/1430934">http://www.openstreetmap.org/user/andy%20mackey/traces/1430934</a> the buildings are east wall of catholic church and south wall of changing room building the co-ords of point are 0.17248 W 52.33163 N. this is to big for a comment so its posted in an answer box.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '11, 14:57</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Apr '13, 20:30</strong> </span></p>
</div>
</div>
<div id="comments-container-4987" class="comments-container">
<span id="5363"></span>
<div id="comment-5363" class="comment">
<div id="post-5363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This all assumes that the Bing images have been correctly rectified, which is by no means certain. Never assume an aerial image is any more correct than any other source, especially where the images are mostly intended for consumer use.</p>
</div>
<div id="comment-5363-info" class="comment-info">
<span class="comment-age">(25 May '11, 09:31)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="5366"></span>
<div id="comment-5366" class="comment">
<div id="post-5366-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>yes. some images are, I estimate are up to 30 degrees off vertical (at the edges) judging by the fact I can see the faces of vertical walls.this would suggest that errors could occur.I been helping another mapper by drawing in building foot prints and some adjacent buildings were photographed from opposite directions evidentially (end walls and shadows) but I couldn't see the join. Bing is very good though I think</p>
</div>
<div id="comment-5366-info" class="comment-info">
<span class="comment-age">(25 May '11, 10:10)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-4987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4987-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5348"></span>

<div id="answer-container-5348" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5348-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is one idea for reducing the positioning error. It requires using using two (same type of) receivers that can record raw NMEA data simultaneously. One set on a fixed, known location and the other recording the actual track nearby. Later on, the error could be minimized by subtracting the error of the fixed location from the track data.</p>
<p>This may be a somewhat nice idea, or then close to no help. I have not tested this yet, but I'm going to. The problems are obvious without testing. Firstly, the two receivers probably will not listen to the same set of satellites all the time, so the nominal accuracy will vary on both receivers. Post processing should identify the case and not try to correct, or then the error should be interpolated over the required period of time. This is why you need the raw data, as it contains information about the satellites, which helps evaluating the positioning quality.</p>
<p>Downloading the correctional data, as dieterdreist suggested, could be better way. I just happen to have two bluetooth receivers of the same type, so I could test this out.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '11, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/30bf221646491c37b65224fdeb59c283?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeE&#39;s gravatar image" />
<p><span>SomeE</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeE has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '11, 14:10</strong> </span></p>
</div>
</div>
<div id="comments-container-5348" class="comments-container">
<span id="5349"></span>
<div id="comment-5349" class="comment">
<div id="post-5349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Check out rtklib if you are playing with this.</p>
</div>
<div id="comment-5349-info" class="comment-info">
<span class="comment-age">(24 May '11, 14:26)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-5348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5348-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4963"></span>

<div id="answer-container-4963" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4963-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4963-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4963-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a proposed process (and proposed tagging) and the beginnings of some API implementation for tracking imagery offsets: "<a href="http://wiki.openstreetmap.org/wiki/True_Offset_Process">True Offset Process</a>".</p>
<p>The tagging scheme though is for drawing an area around where an imagery offset applies. Did you want to tag an imagery offset at a particular point? or perhaps you just wanted to record the fact that you've accurately positioned a particular feature so maybe <code>source:location=multiple_gps_readings</code> ...or something (I just made that up, but you get the idea. Maybe someone else has a better suggestion for a good source tag)</p>
<p>Also a <a href="http://wiki.openstreetmap.org/wiki/Talk:True_Offset_Process#Process_of_accurately_determining_offset">discussion on 'Process of accurately determining offset'</a>. I've been doing some experiments with this myself recently, following the approach of "average a large number of tracks collected over several weeks" suggested there</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '11, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-4963" class="comments-container">
&#10;</div>
<div id="comment-tools-4963" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4963-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5350"></span>

<div id="answer-container-5350" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I read somewhere that the GPS satellites belong to the US military. Military units are able to get much more detailed map data, down to approx 1 meter. They do not want to release the codes for higher resolution to civilian use to prevent us from getting better detail. It all has to do with the military's belief that civilians might use the higher definition GPS for "evil purposes."</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '11, 15:18</strong></p>
<img src="https://secure.gravatar.com/avatar/654e2be24ccbe7c088eea3d64d32bbe3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DBlarer&#39;s gravatar image" />
<p><span>DBlarer</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DBlarer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5350" class="comments-container">
<span id="5351"></span>
<div id="comment-5351" class="comment">
<div id="post-5351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>GPS was indeed originally developed for military applications and neither the Y nor the M code have been published. Nevertheless one can try to get the best possible precission out of the received signals.</p>
</div>
<div id="comment-5351-info" class="comment-info">
<span class="comment-age">(24 May '11, 15:44)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="5367"></span>
<div id="comment-5367" class="comment">
<div id="post-5367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've been told by a surveyor that accuracy within inches is possible with there own ground based transmissions that are available to survey instruments.</p>
</div>
<div id="comment-5367-info" class="comment-info">
<span class="comment-age">(25 May '11, 10:20)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-5350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5350-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21268"></span>

<div id="answer-container-21268" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21268-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At the remote sensing conference I was at yesterday a few people mentioned renting a RTK unit for measurements more accurate than conventional GPS units could achieve. It's worth noting that the wikipedia page for RTK has some problems.</p>
<p>My garmin (eTrex 20) can average measurements over multiple days for increased accuracy, and this accuracy is more than enough for OSM's purposes, provided you pick a site with a clear view of the sky and no signal reflections.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '13, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-21268" class="comments-container">
&#10;</div>
<div id="comment-tools-21268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21268-form-container" class="comment-form-container">
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

