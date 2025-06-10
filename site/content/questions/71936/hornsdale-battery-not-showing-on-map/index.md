+++
type = "question"
title = "Hornsdale battery not showing on map"
description = '''I saw on openinframap that the Hornsdale battery (in South Australia built by Neoen/Tesla 100 MW, 129 MWh) was missing: https://openinframap.org/#17.82/-33.085953/138.519478 Same thing on openstreetmap: https://www.openstreetmap.org/#map=18/-33.08559/138.51884 But in edit mode it appears: https://ww...'''
date = "2019-12-02T15:38:00Z"
lastmod = "2019-12-03T10:04:00Z"
weight = 71936
keywords = [ "invisible", "map" ]
aliases = [ "/questions/71936" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Hornsdale battery not showing on map](/questions/71936/hornsdale-battery-not-showing-on-map)

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
<span id="post-71936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71936-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I saw on openinframap that the Hornsdale battery (in South Australia built by Neoen/Tesla 100 MW, 129 MWh) was missing: <a href="https://openinframap.org/#17.82/-33.085953/138.519478">https://openinframap.org/#17.82/-33.085953/138.519478</a></p>
<p>Same thing on openstreetmap: <a href="https://www.openstreetmap.org/#map=18/-33.08559/138.51884">https://www.openstreetmap.org/#map=18/-33.08559/138.51884</a></p>
<p>But in edit mode it appears: <a href="https://www.openstreetmap.org/edit?editor=id#map=18/-33.08559/138.51884">https://www.openstreetmap.org/edit?editor=id#map=18/-33.08559/138.51884</a> Same thing if you follow the link directly: <a href="https://www.openstreetmap.org/way/544861272#map=19/-33.08612/138.51949">https://www.openstreetmap.org/way/544861272#map=19/-33.08612/138.51949</a></p>
<p>How do I make it appear in both the openstreetmap and openinframap views please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-invisible" rel="tag" title="see questions tagged &#39;invisible&#39;">invisible</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '19, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/688a8eb05930e8c8cd2606aa27ff8888?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TFJamMan&#39;s gravatar image" />
<p><span>TFJamMan</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TFJamMan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '19, 15:39</strong> </span></p>
</div>
</div>
<div id="comments-container-71936" class="comments-container">
&#10;</div>
<div id="comment-tools-71936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71936-form-container" class="comment-form-container">
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

<span id="71941"></span>

<div id="answer-container-71941" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71941-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TFJamMan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not appearing on either OpenStreetMap or OpenInfraMap because it's not tagged with any recognised area tags. "power=battery" is not a documented tag anywhere.</p>
<p>I would tag this as:</p>
<pre><code>landuse=industrial
power=plant
plant:source=battery
plant:output:electricity=100 MW</code></pre>
<p>With these tags it will appear correctly on both OpenStreetMap and OpenInfraMap.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '19, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/8b3bb7691f5081b29e318ab4e84479e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="russss&#39;s gravatar image" />
<p><span>russss</span><br />
<span class="score" title="110 reputation points">110</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="russss has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-71941" class="comments-container">
<span id="71946"></span>
<div id="comment-71946" class="comment">
<div id="post-71946-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>russss, the <a href="https://www.openstreetmap.org/relation/8403778">windfarm</a> is already tagged as power=plant. Here we are talking merely about one element within, a battery and not a plant. I would consider your proposal tagging for the renderer, i.e. using inappropriate tags just to make something show up on the map.</p>
<p>The relation I linked to could be extended to include the substation and the battery. Still it would probably not be rendered by this means.</p>
</div>
<div id="comment-71946-info" class="comment-info">
<span class="comment-age">(02 Dec '19, 19:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="71948"></span>
<div id="comment-71948" class="comment">
<div id="post-71948-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ah OK, I wasn't aware it was a part of a wind farm.</p>
<p>In that case the wind farm should have plant:source=wind;battery and the plant:output:electricity should be the combined peak output of the wind farm and the battery storage.</p>
<p>The battery storage should be tagged as power=generator, and generator:source=battery. This will not render on OpenInfraMap currently although I'm planning to add it.</p>
<p>If you just add the landuse=industrial tag (which I think is appropriate), it will render on the main OSM map.</p>
</div>
<div id="comment-71948-info" class="comment-info">
<span class="comment-age">(02 Dec '19, 19:29)</span> <span class="comment-user userinfo">russss</span>
</div>
</div>
<span id="71949"></span>
<div id="comment-71949" class="comment">
<div id="post-71949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Having said that, I think there is also a reasonable argument to tag the wind farm and the battery storage as separate plants.</p>
<p>Co-located storage is relatively new so I don't think we've come to a reasonable consensus on how to tag these yet.</p>
</div>
<div id="comment-71949-info" class="comment-info">
<span class="comment-age">(02 Dec '19, 19:33)</span> <span class="comment-user userinfo">russss</span>
</div>
</div>
<span id="71961"></span>
<div id="comment-71961" class="comment">
<div id="post-71961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Russss, isn’t the battery part of an industrial complex, a power plant ? Are you tagging every part of an industrial complex or just the borders and buildings ? Just not the functions, from gate-house up to works ? Or did you add the basements of the standing windmills (generators) as well, since they are based on these concrete buildings and connected by several bolts. <a href="https://www.openstreetmap.org/#map=19/52.01731/5.12144">https://www.openstreetmap.org/#map=19/52.01731/5.12144</a> But feel free to tag what you like and change the Wiki if it has a lacune. Ps and what about the connecting lines over or underground ?</p>
</div>
<div id="comment-71961-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 09:49)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="71962"></span>
<div id="comment-71962" class="comment">
<div id="post-71962-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The wind farm is (correctly, IMO) tagged as a relation rather than an area, because the landuse in the area between the wind turbines is not (normally) changed. This is described on the wiki here: <a href="https://wiki.openstreetmap.org/wiki/Tag:power%3Dplant#Dispersed_facilities_power_plants">https://wiki.openstreetmap.org/wiki/Tag:power%3Dplant#Dispersed_facilities_power_plants</a></p>
<p>The battery storage and substation are separate, fenced compounds, so I think they are industrial landuse by themselves.</p>
<p>I don't think this is inconsistent with what is currently on the wiki (although the power tagging pages could still do with some cleanup, which I am slowly working on).</p>
<p>As I mentioned before, whether the battery storage is part of the wind farm or separate is arguable in my opinion.</p>
</div>
<div id="comment-71962-info" class="comment-info">
<span class="comment-age">(03 Dec '19, 10:04)</span> <span class="comment-user userinfo">russss</span>
</div>
</div>
</div>
<div id="comment-tools-71941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71941-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71938"></span>

<div id="answer-container-71938" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71938-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The maps on www.openstreetmap.org, openinframap.org and many others are created by different organizations or people. They each decide what they want to show on the map and what not. They need to make selections to not render the map unreadable by cluttering the map with overlaying objects.</p>
<p>If you want to see the battery you can either produce a map by yourself if you have the means to do so or ask the maintainer of these maps to add support for the feature. I guess you have the best chance to achieve the latter with a dedicated map like openinframap. I suggest you click on the about link in the top left hand corner and contact the author directly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '19, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-71938" class="comments-container">
<span id="71947"></span>
<div id="comment-71947" class="comment">
<div id="post-71947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is the battery in a building or a building by itself? You could add building=yes to the object.</p>
</div>
<div id="comment-71947-info" class="comment-info">
<span class="comment-age">(02 Dec '19, 19:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71938-form-container" class="comment-form-container">
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

