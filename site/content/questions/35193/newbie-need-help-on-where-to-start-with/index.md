+++
type = "question"
title = "Newbie-need help on where to start with"
description = '''I&#x27;m just discovering this world of OSM. Here&#x27;s my ultimate goal. To create a small website for a small group of craft beers fans to use. I want to create an interact map of the US with lots of little points of interest everywhere. For example I want to list all the US breweries &amp;amp; bottle shops &amp;a...'''
date = "2014-07-25T19:34:00Z"
lastmod = "2014-07-26T21:53:00Z"
weight = 35193
keywords = [ "newbie" ]
aliases = [ "/questions/35193" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie-need help on where to start with](/questions/35193/newbie-need-help-on-where-to-start-with)

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
<span id="post-35193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35193-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm just discovering this world of OSM. Here's my ultimate goal. To create a small website for a small group of craft beers fans to use. I want to create an interact map of the US with lots of little points of interest everywhere. For example I want to list all the US breweries &amp; bottle shops &amp; beer traders I can. All diff color flags. So you click on one &amp; up pops the store, brewery, etc &amp; you get more detailed info. I know OSM is for the map portion. What works with that side for the interactive elements &amp; screen pop up info? Please explain the diff in Javascript API vs ARCgis? Once I understand what all I need I'd like to get a book on Amazon but I'm not sure which one I need yet. I'm not a JAVA programmer although I do understand HTML &amp; can do light program script work if necc. Please point me in the right direction &amp; let me know what terminology I need to be researching further. I'm a quick learner (just started 2 days ago), but learn quickly. Thanks everyone!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '14, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/08d138ab3b5198d778e0ac350b67a504?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matrix64015&#39;s gravatar image" />
<p><span>matrix64015</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matrix64015 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35193" class="comments-container">
&#10;</div>
<div id="comment-tools-35193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35193-form-container" class="comment-form-container">
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

<span id="35200"></span>

<div id="answer-container-35200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35200-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What I'd imagine that you'd want to do is to display some points of interest (breweries etc.) over the top of some existing map tiles.</p>
<p><a href="http://brewmap.maps3.org.uk/client/brewmap.html">Here's a site</a> that's similar to what you're describing, but for the UK. It uses <a href="http://leafletjs.com/">Leaflet</a> as a Javascript library to display map tiles and the overlays on top of them. There are lots of leaflet examples <a href="http://leafletjs.com/examples.html">here</a>, and there are some worked examples at the <a href="http://switch2osm.org/using-tiles/getting-started-with-leaflet/">switch2osm</a> site that may be helpful.</p>
<p>What also might be helpful is a <a href="http://help.openstreetmap.org/questions/32760/looking-for-a-description-of-how-the-map-is-shown-on-a-pc-rendering-process-but-no-technical-details/33010">previous answer</a> attempting to give a "soup to nuts" explanation of OpenStreetMap, and the <a href="http://wiki.openstreetmap.org/wiki/Beginners_Guide">Beginners' Guide</a> in the OSM wiki.</p>
<p>I'd actually start with the "getting started with Leaflet" example at the switch2osm site, to just display a simple slippy map using existing tiles. Then try adding simple hardcoded overlay markers, then try getting those overlays from a server that are loaded based on map position, etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '14, 23:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-35200" class="comments-container">
<span id="35226"></span>
<div id="comment-35226" class="comment">
<div id="post-35226-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you very much for pointing me in the right direction! Much appreciated!</p>
</div>
<div id="comment-35226-info" class="comment-info">
<span class="comment-age">(26 Jul '14, 21:53)</span> <span class="comment-user userinfo">matrix64015</span>
</div>
</div>
</div>
<div id="comment-tools-35200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35200-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35196"></span>

<div id="answer-container-35196" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35196-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi please read this thoroughly and you ll find some answers, <a href="http://wiki.openstreetmap.org/wiki/Using_OSM">http://wiki.openstreetmap.org/wiki/Using_OSM</a> and <a href="http://wiki.openstreetmap.org/wiki/Web_front_end">http://wiki.openstreetmap.org/wiki/Web_front_end</a> and don’t ask multiple questions inside one question. These links carry a lot of other ones how to build and use a site with OSM material. Feel free to ask for specific answers after reading.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '14, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-35196" class="comments-container">
&#10;</div>
<div id="comment-tools-35196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35196-form-container" class="comment-form-container">
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

