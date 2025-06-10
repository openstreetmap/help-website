+++
type = "question"
title = "How to tag traffic lights on pedestrian crossing?"
description = '''It seems to me that traffic lights are valuable orientation points and having them visible on the map would be desired. Wiki recommendation for traffic lights on pedestrian crossing (without road crossing): Traffic signals at crossings for pedestrians redirects to: Key:crossing which tells to use hi...'''
date = "2010-11-08T16:01:00Z"
lastmod = "2013-09-15T17:48:00Z"
weight = 1489
keywords = [ "crossing", "pedestrian", "traffic_signals" ]
aliases = [ "/questions/1489" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag traffic lights on pedestrian crossing?](/questions/1489/how-to-tag-traffic-lights-on-pedestrian-crossing)

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
<span id="post-1489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1489-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It seems to me that traffic lights are valuable orientation points and having them visible on the map would be desired.</p>
<p>Wiki recommendation for traffic lights on pedestrian crossing (without road crossing):<br />
<a href="http://wiki.openstreetmap.org/wiki/Traffic_lights#Traffic_signals_at_crossings_for_pedestrians">Traffic signals at crossings for pedestrians</a> redirects to: <a href="http://wiki.openstreetmap.org/wiki/Key:crossing">Key:crossing</a> which tells to use <strong>highway=crossing</strong> &amp; <strong>crossing=traffic_signals</strong></p>
<p>I've tried that but this was not rendered as any visible symbol (?)</p>
<p>I've look how it's done in other places and traffic lights on pedestrian crossings are tagged as <strong>highway=traffic_signals</strong> Which defies Wiki, but yields a nice icon on the map...</p>
<p>What is the right tag to follow?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-traffic_signals" rel="tag" title="see questions tagged &#39;traffic_signals&#39;">traffic_signals</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '10, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/25e5605a7f3f6f93ba7596380dfae6b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PawelJ&#39;s gravatar image" />
<p><span>PawelJ</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PawelJ has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-1489" class="comments-container">
&#10;</div>
<div id="comment-tools-1489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1489-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="1492"></span>

<div id="answer-container-1492" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1492-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-1492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You've already answered your question: It's tagged as <strong>highway=crossing + crossing=traffic_signals</strong>.</p>
<p>The fact that this doesn't show up in a particular map doesn't indicate that it isn't correctly tagged - no map displays all features that are in the database, neither the maps on <a href="http://openstreetmap.org">openstreetmap.org</a>, nor any other map made from OpenStreetMap data.</p>
<p>Instead, that map apparently chooses to display traffic signals at vehicle junctions (highway=traffic_signals), but doesn't display pedestrian crossings with traffic signals. That's why an icon will show up if you incorrectly tag this node as vehicle junction, rather than pedestrian crossing, with traffic signals.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '10, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '10, 17:04</strong> </span></p>
</div>
</div>
<div id="comments-container-1492" class="comments-container">
<span id="1493"></span>
<div id="comment-1493" class="comment">
<div id="post-1493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! That confirms my understanding of Wiki, but still leaves me uneasy about the lack of any indication on the map. I fully agree that pedestrian crossings are much less important that road crossings, and displaying too much icons would 'pollute' the map. But they are not visible even in the highest zoom level, when they cannot obscure anything because the size of the icon is about the same as the width of the road... And surely to know that you need to "turn after the lights" would be helpful?</p>
</div>
<div id="comment-1493-info" class="comment-info">
<span class="comment-age">(08 Nov '10, 17:25)</span> <span class="comment-user userinfo">PawelJ</span>
</div>
</div>
<span id="1494"></span>
<div id="comment-1494" class="comment">
<div id="post-1494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I personally agree with you, but ... well, I'm not a style sheet dev. This seems like another instance of <a href="http://help.openstreetmap.org/questions/1107/can-i-influence-what-gets-rendered-in-the-main-mapnik-layer">"Can I influence what gets rendered in the main Mapnik layer"</a> (assuming that the Mapnik layer on <a href="http://osm.org">osm.org</a> is the map that you are referring to).</p>
</div>
<div id="comment-1494-info" class="comment-info">
<span class="comment-age">(08 Nov '10, 18:21)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-1492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1492-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2126"></span>

<div id="answer-container-2126" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2126-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have also seen that this is tagged as highway=traffic_signals and crossing=traffic_signals. Actually I do not quite understand why there should be any differentiation between highway=traffic_signals and crossing=traffic_signals. All should be tagged as highway=traffic_signals because the do always regulate the flow of vehicle traffic. Sometimes because there is a crossing of roads, sometimes because there is a pedestrian crossing. So highway=traffic_signals and crossing=traffic_signals seems to me a good solution which could still be improved in some why.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '11, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-2126" class="comments-container">
<span id="2134"></span>
<div id="comment-2134" class="comment">
<div id="post-2134-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>One tag applies to how the highway is controlled, the other applies to how the crossing is controlled.</p>
</div>
<div id="comment-2134-info" class="comment-info">
<span class="comment-age">(09 Jan '11, 20:04)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="2228"></span>
<div id="comment-2228" class="comment">
<div id="post-2228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I still do not see why we need two different tags for the same issue. If the crossing is controlled by traffic lights then consequently also the highway that is crossed. So highway=traffic_signals for both cases should be sufficient IMHO.</p>
</div>
<div id="comment-2228-info" class="comment-info">
<span class="comment-age">(16 Jan '11, 15:45)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
<span id="2230"></span>
<div id="comment-2230" class="comment">
<div id="post-2230-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There are traffic signals where pedestrians can cross the road, and traffic signals where they cannot do so. From a pedestrian's perspective, these two cases are fundamentally different. Therefore, we cannot use the same tag for both.</p>
</div>
<div id="comment-2230-info" class="comment-info">
<span class="comment-age">(16 Jan '11, 16:02)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-2126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2126-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26366"></span>

<div id="answer-container-26366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26366-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't want to frustrate anyone by re-asking this question, but I too don't quite follow the logics here, or on the wikis. I'd welcome advice on tagging the following common - but it not totally clear -scenarios, expecting to use any or all of the following tags: highway=traffic_signals highway=crossing crossing=traffic signals crossing_ref=pelican</p>
<p>1) A street with a zebra crossing midway along 2) A street with a pelican crossing midway along 3) A single intersection-node of two streets a)controlled by traffic signals b) with pelican crossings present on each junction.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '13, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/bc748fa13130629dfec3d6469f4c6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rogerstb&#39;s gravatar image" />
<p><span>rogerstb</span><br />
<span class="score" title="235 reputation points">235</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rogerstb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26366" class="comments-container">
<span id="26367"></span>
<div id="comment-26367" class="comment">
<div id="post-26367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are not alone: <a href="http://help.openstreetmap.org/questions/5410/what-is-best-practice-for-mapping-signal-controlled-pedestrian-crossings-at-road-junctions.">http://help.openstreetmap.org/questions/5410/what-is-best-practice-for-mapping-signal-controlled-pedestrian-crossings-at-road-junctions.</a> I find Tordanik's comment above is the best answer, but I still find it unsatisfactory for things like former roundabouts which are traffic-light controlled. The existing tagging is fine for pedestrians, but imposes costs for other applications, such as routers which must apply cost penalties for traffic lights (&amp; different ones your cases 2) &amp; 3).</p>
</div>
<div id="comment-26367-info" class="comment-info">
<span class="comment-age">(15 Sep '13, 17:48)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26366-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2075"></span>

<div id="answer-container-2075" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2075-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-2075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is the complete instruction to tag pedestrian crossings:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Key:crossing">http://wiki.openstreetmap.org/wiki/Key:crossing</a></p>
<p>Blindmap renders pedestrian crossings with sound.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/cb9e3487765b1e13e3fd6ebb00fdcac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartograefin&#39;s gravatar image" />
<p><span>Kartograefin</span><br />
<span class="score" title="592 reputation points">592</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartograefin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2075" class="comments-container">
&#10;</div>
<div id="comment-tools-2075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2075-form-container" class="comment-form-container">
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

