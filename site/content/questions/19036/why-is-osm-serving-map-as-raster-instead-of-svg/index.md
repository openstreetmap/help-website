+++
type = "question"
title = "Why is OSM serving map as raster instead of SVG?"
description = '''Considering all underlying data is stored as SVG, why does OSM serves maps as raster data? Switching to SVG would:  Remove need of tile rendering (instant map updates, less resources consumed) Reduce server bandwidth consumption - especially good for mobile data Introduce ability to change look&#x27;n&#x27;fe...'''
date = "2013-01-13T22:58:00Z"
lastmod = "2013-01-16T17:04:00Z"
weight = 19036
keywords = [ "openstreetmap", "svg", "map" ]
aliases = [ "/questions/19036" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Why is OSM serving map as raster instead of SVG?](/questions/19036/why-is-osm-serving-map-as-raster-instead-of-svg)

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
<span id="post-19036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19036-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Considering all underlying data is stored as SVG, why does OSM serves maps as raster data? Switching to SVG would:</p>
<ul>
<li>Remove need of tile rendering (instant map updates, less resources consumed)</li>
<li>Reduce server bandwidth consumption - especially good for mobile data</li>
<li>Introduce ability to change look'n'feel (drawing layout) on demant with CSS</li>
<li>Allow to zoom from 0 to oblivion without quality loose</li>
</ul>
<p>So, why? Is it simply because OSM started with raster and changing cost is simply too big?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '13, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/35fc429c14a6b1064cf250b9e6c58ed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Expro&#39;s gravatar image" />
<p><span>Expro</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Expro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19036" class="comments-container">
&#10;</div>
<div id="comment-tools-19036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19036-form-container" class="comment-form-container">
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

<span id="19039"></span>

<div id="answer-container-19039" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19039-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-19039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Expro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A couple of misconceptions:</p>
<ul>
<li>underlying data is not stored in SVG.</li>
<li>serving vector data would not necessarily consume less resources</li>
<li>serving vector data would not necessarily consume less bandwidth (as even now-unrendered things would be served)</li>
</ul>
<p>The most important reason however is lack of browser support. We'd like everyone to see the map, not only those with modern browsers on powerful processors.</p>
<p>I think it is likely that we will switch to vector tiles at some point in the future but I'd guess it's going to be something like 2 years.</p>
<p>You are of course welcome to set up your own vector tile server based on OSM, as others have done, e.g. <a href="http://www.opensciencemap.org/.">http://www.opensciencemap.org/.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '13, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-19039" class="comments-container">
<span id="19046"></span>
<div id="comment-19046" class="comment">
<div id="post-19046-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>About misconceptions 2. and 3. - usually vector data is smaller than raster data, but I cant tell how it would work in this case, thats true.</p>
<p>I guess lack of browser support is the answer I was looking for.</p>
</div>
<div id="comment-19046-info" class="comment-info">
<span class="comment-age">(13 Jan '13, 23:39)</span> <span class="comment-user userinfo">Expro</span>
</div>
</div>
</div>
<div id="comment-tools-19039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19039-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19037"></span>

<div id="answer-container-19037" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19037-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am guessing because not all browsers will display svgs as fast as rasters(IE mobile) also like all big projects it takes some time to change or update things.(Don't break what you already have). I would think that the devs are at the very least testing it out. Remember it has to work almost everywhere at a decent speed otherwise there will be a lot of complaints. With mobile devices it is better a server does the hard work than the device with limited resources and battery. Also there would need to be some work on the theme which also takes work and testing. I also think it needs mapnik2 and don't know if they switched over to mapnik2.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '13, 23:12</strong></p>
<img src="https://secure.gravatar.com/avatar/602a4908e9bea5a3f086bd91654717c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redsteakraw&#39;s gravatar image" />
<p><span>redsteakraw</span><br />
<span class="score" title="1040 reputation points"><span>1.0k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redsteakraw has 2 accepted answers">22%</span> </br></p>
</div>
</div>
<div id="comments-container-19037" class="comments-container">
&#10;</div>
<div id="comment-tools-19037" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19037-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19038"></span>

<div id="answer-container-19038" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19038-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="http://kothic.org/js/">the Kothic JS demo</a>, even though it's fast it's alot slower than pngs, and it seems to takes up more or less the same amount of bandwidth.</p>
<p>So basically it doesn't quite work on osm.org yet, but try kothic out it's pretty amazing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '13, 23:17</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-19038" class="comments-container">
<span id="19040"></span>
<div id="comment-19040" class="comment">
<div id="post-19040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is canvas rendering - so its basicly exacly same thing as rendering SVG data to raster on server side, but it simply happens on client side. What I had in mind was simply serving SVG embaded inside HTML page. Thanks for interesing link though!</p>
</div>
<div id="comment-19040-info" class="comment-info">
<span class="comment-age">(13 Jan '13, 23:21)</span> <span class="comment-user userinfo">Expro</span>
</div>
</div>
<span id="19044"></span>
<div id="comment-19044" class="comment">
<div id="post-19044-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, unless you want to view the raw xml, it eventually has to be rendered into pixel based images, if it is SVG or some other vector format. The tiles that are served for KothicJS are simple vector data, so you can do other things with it than render it to a bitmap.</p>
<p>What are you trying to achieve with "SVG embedded inside HTML" other than what KothicJS does? But as Frederik said, the underlying OSM data is not stored as SVG, so one would need to "render" it to SVG to start with.</p>
</div>
<div id="comment-19044-info" class="comment-info">
<span class="comment-age">(13 Jan '13, 23:36)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="19047"></span>
<div id="comment-19047" class="comment">
<div id="post-19047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Currently, browsers are able to render embedded SVG on their own - no need to write (client side) renderer engine, as KothicJS did with use of canvas. But need of casting internal data format to SVH still remains as was pointed.</p>
</div>
<div id="comment-19047-info" class="comment-info">
<span class="comment-age">(13 Jan '13, 23:44)</span> <span class="comment-user userinfo">Expro</span>
</div>
</div>
<span id="19087"></span>
<div id="comment-19087" class="comment">
<div id="post-19087-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><span>@Expro</span>:</p>
<p>Also have a look at <a href="http://www.flosm.de/html/POI-Karte.html">http://www.flosm.de/html/POI-Karte.html</a></p>
</div>
<div id="comment-19087-info" class="comment-info">
<span class="comment-age">(14 Jan '13, 20:16)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="19088"></span>
<div id="comment-19088" class="comment">
<div id="post-19088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@stephan75</span> Yeah, its esentially what I had in mind. And its really fast at desktop machine.</p>
</div>
<div id="comment-19088-info" class="comment-info">
<span class="comment-age">(14 Jan '13, 20:21)</span> <span class="comment-user userinfo">Expro</span>
</div>
</div>
<span id="19141"></span>
<div id="comment-19141" class="comment not_top_scorer">
<div id="post-19141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But they aren't using SVG either, are they?</p>
</div>
<div id="comment-19141-info" class="comment-info">
<span class="comment-age">(16 Jan '13, 13:40)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="19144"></span>
<div id="comment-19144" class="comment not_top_scorer">
<div id="post-19144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also try using their public transport map on a nettop/netbook. Slow, zoom stops working after a while,...</p>
</div>
<div id="comment-19144-info" class="comment-info">
<span class="comment-age">(16 Jan '13, 17:04)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-19038" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-19038-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19041"></span>

<div id="answer-container-19041" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19041-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM isn't one map - it's the <a href="http://planet.openstreetmap.org/">data</a>. There are <a href="https://wiki.openstreetmap.org/wiki/Maps">lots of OSM-based maps</a>, some vector-based.<br />
</p>
<p>The way that progress happens (e.g. the recent move to Leaflet) is that someone goes away and makes a variant that is an improvement, and it gets incorporated. The way that it doesn't happen is with people say "the volunteers who develop and run OSM services ought to do X".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '13, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-19041" class="comments-container">
<span id="19043"></span>
<div id="comment-19043" class="comment">
<div id="post-19043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As software developer im quite aware of how open source projects usually develops. I was simply asking what is a reason of current state of OSM - not even remotly suggesting that this state should be different.</p>
</div>
<div id="comment-19043-info" class="comment-info">
<span class="comment-age">(13 Jan '13, 23:36)</span> <span class="comment-user userinfo">Expro</span>
</div>
</div>
</div>
<div id="comment-tools-19041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19041-form-container" class="comment-form-container">
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

