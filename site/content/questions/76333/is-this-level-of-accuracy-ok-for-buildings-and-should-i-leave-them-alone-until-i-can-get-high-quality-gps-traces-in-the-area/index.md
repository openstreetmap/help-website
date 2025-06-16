+++
type = "question"
title = "Is this level of accuracy &quot;OK&quot; for buildings, and should I leave them alone until I can get high quality GPS traces in the area?"
description = '''I&#x27;m new to OSM and my town has barely any coverage. What little it does have has clearly been placed using different sources for alignment. Some buildings line up with different imagery, some don&#x27;t line up with any of them (I&#x27;m guessing they&#x27;re older). There are no good GPS traces in my area that I ...'''
date = "2020-08-28T06:05:00Z"
lastmod = "2020-09-02T16:28:00Z"
weight = 76333
keywords = [ "question", "newbie", "alignment" ]
aliases = [ "/questions/76333" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is this level of accuracy "OK" for buildings, and should I leave them alone until I can get high quality GPS traces in the area?](/questions/76333/is-this-level-of-accuracy-ok-for-buildings-and-should-i-leave-them-alone-until-i-can-get-high-quality-gps-traces-in-the-area)

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
<span id="post-76333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76333-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM and my town has barely any coverage. What little it does have has clearly been placed using different sources for alignment. Some buildings line up with different imagery, some don't line up with any of them (I'm guessing they're older). There are no good GPS traces in my area that I can use.</p>
<p>Here is one of the worst examples. <img src="/upfiles/osmexample1.png" alt="Example" /> This is using Bing imagery with no offset. It's slightly better using Indiana's 2018 imagery (This is in southern Indiana), but not entirely accurate. Most buildings and roads are only a little bit off, maybe 5-10 feet maximum.</p>
<p>I'm not currently in a position to get high quality GPS traces for my area. I've tried using the Strava heatmap but it only seems to help up to a certain level of accuracy and both Bing and the Indiana 2018 imagery is accurate enough to seem aligned with the heatmap, but they're both still slightly different from each other.</p>
<p>My question is is this too much to be acceptable? Should I hold off on adding anything to the town in case everything ends up 5-10 feet off from where it should be by the time I get good GPS traces to use for more accurate alignment? It doesn't help things that almost every road in town is off by a little, in seemingly random ways. They aren't all too far east or north, they're just off in random ways that make it even harder to tell what alignment is correct.</p>
<p>Here's an example of the difference between the alignment of Bing and IndianaMap 2018 <img src="/upfiles/osmexample2.png" alt="Example 2" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-alignment" rel="tag" title="see questions tagged &#39;alignment&#39;">alignment</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '20, 06:05</strong></p>
<img src="https://secure.gravatar.com/avatar/703955337dab05cec6f447fc6868f1bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Veltoss&#39;s gravatar image" />
<p><span>Veltoss</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Veltoss has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-76333" class="comments-container">
&#10;</div>
<div id="comment-tools-76333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76333-form-container" class="comment-form-container">
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

<span id="76418"></span>

<div id="answer-container-76418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76418-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first thing to check is the alignment of the background aerial images. <a href="https://learnosm.org/en/beginner/id-editor/#configuring-the-background-layer">https://learnosm.org/en/beginner/id-editor/#configuring-the-background-layer</a></p>
<p>To align choose items that have been amended a few times as these tend to be the most accurate &amp; ones that are at ground level. This is important otherwise you maybe liable to parallax errors. I use major roads, especially at junctions or roundabouts. Avoid using tall buildings.</p>
<p>Map however you wish. if you feel amending the building examples you provided would improve the quality of the OSM database then go ahead &amp; tweak them. Over time you'll probably find certain types of entities you prefer to map &amp; buildings a few feet off may not seem that important.</p>
<p>As well as GPS I've found taking photos are a good resource for mapping more accurately.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '20, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-76418" class="comments-container">
&#10;</div>
<div id="comment-tools-76418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76418-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76335"></span>

<div id="answer-container-76335" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76335-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd say the majority of GPS traces uploaded to OSM originate from customer grade devices. It's perfectly acceptable to use them and to rely on them. If there are no usable traces in your vicinity maybe you could go out and create some references on your own. Try to find some crossing roads with minimal buildings and trees around to minimize reflections. Walk - not drive - to ensure free signal to the satellites and possibly use different devices and switch hands. Record a couple of traces and use their average to calibrate the imagery.</p>
<p>The examples you show are off but I have seen much worse. In my opinion it's always better to have something on the map that can be detailed and corrected later than to have nothing. Give it a shot, start mapping, even correct some of the existing objects if you like. Try to stay consistent within an area, if 5 houses are mapped on the one image, move the other house that has been mapped based on the other image.</p>
<p>Are you aware that you can shift/align the background images in the editor? Useful if the newer imagery is off.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '20, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-76335" class="comments-container">
&#10;</div>
<div id="comment-tools-76335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76335-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76336"></span>

<div id="answer-container-76336" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76336-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One other thought - to add to TZorn's suggestions - how about concentrating on adding detail in the sense of point of interest information rather than just tracing roads etc.? You can add shops, office and other amenities as nodes and the detail that you add to those (opening hours, that sort of thing) will still be useful even if better imagery comes along later, whereas redrawing a building with better imagery takes just as much effort as if you hadn't originally added it in the first place.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '20, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-76336" class="comments-container">
&#10;</div>
<div id="comment-tools-76336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76336-form-container" class="comment-form-container">
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

