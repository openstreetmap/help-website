+++
type = "question"
title = "Cheap DIY DGPS – experiences? worthwhile? how did you do it?"
description = '''Prompted by this question  Disappointed with GPX track detail - looking for suggestions …  I thought about trying to post process a GPX trace by using an older stationary GPS, parked in a car nearby, and then subtracting the error for each corresponding second in a similar way to a DGPS system. I th...'''
date = "2014-08-18T19:57:00Z"
lastmod = "2014-08-19T16:16:00Z"
weight = 35962
keywords = [ "dgps", "post_process_gpx" ]
aliases = [ "/questions/35962" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cheap DIY DGPS – experiences? worthwhile? how did you do it?](/questions/35962/cheap-diy-dgps-experiences-worthwhile-how-did-you-do-it)

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
<span id="post-35962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35962-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Prompted by this question <a href="/questions/35883/">Disappointed with GPX track detail - looking for suggestions</a> … I thought about trying to post process a GPX trace by using an older stationary GPS, parked in a car nearby, and then subtracting the error for each corresponding second in a similar way to a DGPS system. I think a spreadsheet could do the maths. And hopefully I could get a more accurate, reprocessed GPX back from the spreadsheet.</p>
<p>Here is a bit more information: The process is that the fixed GPS as a known position and some of the error is down to Satellite clock which should be the same for both GPSes so if the fixed GPS is 3 meters north and 2 west these errors are used to adjust the moving reading at that time. Hope you get the idea.</p>
<p><em>The question is:</em> have you tried it, is it worthwhile, and if so, how did you do it.<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dgps" rel="tag" title="see questions tagged &#39;dgps&#39;">dgps</span> <span class="post-tag tag-link-post_process_gpx" rel="tag" title="see questions tagged &#39;post_process_gpx&#39;">post_process_gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '14, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '14, 22:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-35962" class="comments-container">
&#10;</div>
<div id="comment-tools-35962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35962-form-container" class="comment-form-container">
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

<span id="35983"></span>

<div id="answer-container-35983" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35983-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are clearly on the wrong track here. Post fix correction of offsets doesn't work and you are just as likely to make the position worse as better.</p>
<p>Averaging does help (experiments have shown that you need a larger number of samples) to a certain point, but it, naturally, doesn't eliminate errors that are caused by reflections from buildings, coverage etc. which tend to be far larger than those caused by atmospeheric pertubations. Averaging over a large number of tracks may be a bit better because you typically will have different devices mounted in different positions in the vehicle over a very long time with different weather conditions, vegetation etc. However inspection of track bundles where reception is difficult and tracking is difficult (sharp corners) typically shows all devices showing the same errors (over-/underruns etc.).</p>
<p>Building a system that can actually do real DGPS is not that expensive, depending on where you live there may even be a public base station service that you can access for free or for a small amount of money (you will need access to one if you are doing short base line DGPS anyway to locate your base station precisely).</p>
<p>Software: <a href="http://www.rtklib.com/">http://www.rtklib.com/</a> OSM wiki: <a href="http://wiki.openstreetmap.org/wiki/RTKLIB">http://wiki.openstreetmap.org/wiki/RTKLIB</a></p>
<p>There are other non-DGPS approaches to providing higher accuracy GPS positions that are interesting for OSM use see <a href="http://en.wikipedia.org/wiki/Precise_Point_Positioning">http://en.wikipedia.org/wiki/Precise_Point_Positioning</a> and <a href="http://www.u-blox.ch/en/precise-point-positioning-ppp.html">http://www.u-blox.ch/en/precise-point-positioning-ppp.html</a> (an example of a chip that can do it).</p>
<p>Further it should be noted that OSM currently uses a single global coordinate system instead of multiple latched to the continental plates making sub-dezimeter measurements rather pointless.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '14, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '14, 16:21</strong> </span></p>
</div>
</div>
<div id="comments-container-35983" class="comments-container">
<span id="35986"></span>
<div id="comment-35986" class="comment">
<div id="post-35986-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To be clear: the error seen on the stationary GPS is not directly related to the error seen on the mobile one. So you can't simply improve one with the other.</p>
<p>DGPS works because the reference station constantly broadcasts the information, kind of like ahaving an extra GPS satellite on the ground.</p>
</div>
<div id="comment-35986-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 10:24)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="35987"></span>
<div id="comment-35987" class="comment">
<div id="post-35987-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@Vincent</span> you are thinking of the correction information provided by WAAS, EGNOS and similar ground based systems, that is not DGPS. DGPS does work by having a base station nearby (emulated or real) that receives signals from the same satellites with the the same atmospheric disturbances as the device you want the postion from, however this works on the "raw" GPS signal on a satellite per satellite base and not on the already calculated solution.</p>
</div>
<div id="comment-35987-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 10:31)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="35995"></span>
<div id="comment-35995" class="comment">
<div id="post-35995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To summarize: The "raw" is important here, as far as I understand it. So the spreadsheet version will not work whereas the RTKLIB software (this is the same as mentioned in my answer's link) would work because it has available the raw gps data of a fixed and a mobile receiver.</p>
</div>
<div id="comment-35995-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 16:16)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35983" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35983-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35972"></span>

<div id="answer-container-35972" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35972-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><del>Yes, it is a interesting and promising idea!</del>(←no, raw data needed) However, I think it is important to try other, simpler options first: At least WAAS, EGNOS, or similar sat-based correction systems should be switched on. That already helps. And of course there is the great option of averaging (single points or tracks).</p>
<p>At e.g. <span>DE:Genauigkeit von GPS-Daten#Nachträgliche Korrektur durch DGPS</span> (German) there is a description of your idea and a software link (instead of your spreadsheet calculation).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '14, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Aug '14, 16:20</strong> </span></p>
</div>
</div>
<div id="comments-container-35972" class="comments-container">
<span id="35992"></span>
<div id="comment-35992" class="comment">
<div id="post-35992-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you all for extra info, I will spend some time digesting it. I did, and do think that DPGS isn't required for editing OSM in areas of good Bing and with lots of Traces. For a while I have been utilizing all traces to average ways aided by excellent Bing. Other areas may not be so lucky. They may need DGPS.</p>
</div>
<div id="comment-35992-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 14:58)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-35972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35972-form-container" class="comment-form-container">
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

