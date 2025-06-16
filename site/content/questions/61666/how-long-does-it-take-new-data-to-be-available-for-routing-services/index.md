+++
type = "question"
title = "How long does it take new data to be available for routing services?"
description = '''I&#x27;ve started to map new features, mainly paths, by using JOSM. It is possible to immediately access them for the edition by using iD or Potlatch 2, even though they are not present in all the tiles, at all scales, when accessing OpenStreetMap web site. But it takes longer to be available to make rou...'''
date = "2018-01-16T20:27:00Z"
lastmod = "2018-02-20T17:11:00Z"
weight = 61666
keywords = [ "routing" ]
aliases = [ "/questions/61666" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How long does it take new data to be available for routing services?](/questions/61666/how-long-does-it-take-new-data-to-be-available-for-routing-services)

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
<span id="post-61666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61666-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've started to map new features, mainly paths, by using JOSM. It is possible to immediately access them for the edition by using iD or Potlatch 2, even though they are not present in all the tiles, at all scales, when accessing OpenStreetMap web site. But it takes longer to be available to make routes calculations. I've tried by using Locus Map relaying on online GraphHopper and offline BRouter, BRouter web client and Orux Maps (to the best of my knowledge, using also GraphHopper ad BRouter), but it takes days to have new data available for routing.</p>
<p>Please, is it possible to get new data for routing calculation immediately upon edition?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '18, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1c367fd463bbeb37fc5257c03f8618fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rrodrigueznt&#39;s gravatar image" />
<p><span>rrodrigueznt</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rrodrigueznt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61666" class="comments-container">
&#10;</div>
<div id="comment-tools-61666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61666-form-container" class="comment-form-container">
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

<span id="61679"></span>

<div id="answer-container-61679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61679-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-61679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most (all?) routing providers will need to pre-process the OSM data, so while your edits will be available to them as soon as you save it may take some time before it becomes available from their APIs. Examples you mention are GraphHopper who <a href="https://graphhopper.com/api/1/docs/FAQ/#how-long-does-it-take-after-i-updated-the-data-on-openstreetmaporg">have in their FAQ</a></p>
<blockquote>
<p>"A change of the data at openstreetmap.org will be considered in our APIs roughly after 1 to 2 days. Except for the Geocoding API: the default provider can take up to 7 weeks and the nominatim provider should be updated within one week."</p>
</blockquote>
<p>BRouter <a href="http://brouter.de/brouter/">mentions</a> they do weekly updates</p>
<blockquote>
<p>"Routing data is available worldwide with automatic weekly updates"</p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '18, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-61679" class="comments-container">
<span id="61803"></span>
<div id="comment-61803" class="comment">
<div id="post-61803-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, <a href="https://help.openstreetmap.org/users/339/edloach">@EdLoach</a>! I should have been able to find those references myself, but I'm still strungling to understand what I should ask! And where! I to need more testing to confirm the delays they announce for their product! I'm report back when done!</p>
</div>
<div id="comment-61803-info" class="comment-info">
<span class="comment-age">(24 Jan '18, 23:27)</span> <span class="comment-user userinfo">rrodrigueznt</span>
</div>
</div>
</div>
<div id="comment-tools-61679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61679-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61667"></span>

<div id="answer-container-61667" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61667-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM has a <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Routing">routing plugin</a> option:<br />
I have not used but it seems that you can use this on the data you have loaded in to JOSM.<br />
I noticed this query that related to the plugin:<br />
<a href="/questions/30832/how-do-i-use-the-josm-routing-plugin">https://help.openstreetmap.org/questions/30832/how-do-i-use-the-josm-routing-plugin</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '18, 23:44</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '18, 01:30</strong> </span></p>
</div>
</div>
<div id="comments-container-61667" class="comments-container">
<span id="61802"></span>
<div id="comment-61802" class="comment">
<div id="post-61802-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, <a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a>, I've installed the plugin and get it working but, as stated in the related query you pointed out, it is by no means an obvious task to deal with this piece of software! I'm sure the work behind deserves attention and I would like to look deep into it to be able to contribute, but this is far from my capabilities right now! I should find a way to use new paths in routing or, at least, to be able to predict/know the time they take to be able for a freely available routing tool. Thanks!</p>
</div>
<div id="comment-61802-info" class="comment-info">
<span class="comment-age">(24 Jan '18, 23:05)</span> <span class="comment-user userinfo">rrodrigueznt</span>
</div>
</div>
</div>
<div id="comment-tools-61667" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61667-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61676"></span>

<div id="answer-container-61676" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61676-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you need the data in a navigation app, (and not only in JOSM as in nevw's answer), the fastest solution I am aware of the live update functionality of OsmAnd. It updates every hour or so. Note that this is not a free service.</p>
<p>Edit: I was told the the live update is free in the f-droid version of OsmAnd</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '18, 04:15</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Feb '18, 04:12</strong> </span></p>
</div>
</div>
<div id="comments-container-61676" class="comments-container">
<span id="61804"></span>
<div id="comment-61804" class="comment">
<div id="post-61804-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, <a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>! I arrive in OsmAnd+ far before than arriving to Locus Map and, but moved to Locus Map's Router planning as soon as I discovered it. It is a pity have not a service offering Locus Map's Router planning together with OsmAnd Live. To the best of my understanding, OsmAnd has not a similar planning tool oriented to walk routes. Please, could you point me to any suitable alternative to Locus Map's Router planning running on OsmAnd? Thanks!</p>
</div>
<div id="comment-61804-info" class="comment-info">
<span class="comment-age">(24 Jan '18, 23:58)</span> <span class="comment-user userinfo">rrodrigueznt</span>
</div>
</div>
<span id="61805"></span>
<div id="comment-61805" class="comment">
<div id="post-61805-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As I don't know why you prefer the Local Map Router above OsmAnd's, it's hard to help out. Bart Eisenberg made a number of videos on using OsmAnd, with a focus on planning hiking trips. He has a <a href="https://www.youtube.com/user/barteisenberg">video channel</a> on Youtube.</p>
</div>
<div id="comment-61805-info" class="comment-info">
<span class="comment-age">(25 Jan '18, 04:16)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="62216"></span>
<div id="comment-62216" class="comment">
<div id="post-62216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, <a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>. Sorry for taking so long to follow this thread. I've been busy with other issues and thinking about the answer to your comment. I realized that the main reason why I do prefer Locus over OsmAnd to plan routes is the fact of having Locus a Function's menu entry called Router planner. To the best of my understanding to get a similar feature while working with OsmAnd I must enter through the option Measure distance, which is, to my poor understanding, at least, not clear at all. In my case, the main issue is not my own access to the feature, but to identify a workflow clear enough as for being proposed to ther users. Thanks!</p>
</div>
<div id="comment-62216-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 21:02)</span> <span class="comment-user userinfo">rrodrigueznt</span>
</div>
</div>
<span id="62218"></span>
<div id="comment-62218" class="comment">
<div id="post-62218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not familiar with the Router planner of Locus, but you can create a route in OsmAnd by adding multiple waypoints (see video <a href="https://www.youtube.com/watch?v=o84C0z3Kydc),">https://www.youtube.com/watch?v=o84C0z3Kydc),</a> or by creating a route between previously created favorites (see <a href="http://osmand.net/features?id=trip-planning).">http://osmand.net/features?id=trip-planning).</a></p>
</div>
<div id="comment-62218-info" class="comment-info">
<span class="comment-age">(20 Feb '18, 04:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="62223"></span>
<div id="comment-62223" class="comment">
<div id="post-62223-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSMand live will <em>not</em> route over the newly added paths by default, unless you turn that (experimental) feature on in settings.</p>
<p>Also note that the rendering on osm.org is broken at the moment, so new edits don't show up in the tiles (although they are saved and propagated to the third parties)</p>
</div>
<div id="comment-62223-info" class="comment-info">
<span class="comment-age">(20 Feb '18, 17:11)</span> <span class="comment-user userinfo">Pieter Vande...</span>
</div>
</div>
</div>
<div id="comment-tools-61676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61676-form-container" class="comment-form-container">
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

