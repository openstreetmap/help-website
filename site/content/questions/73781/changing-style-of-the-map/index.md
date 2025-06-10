+++
type = "question"
title = "Changing style of the map"
description = '''Hey everyone, I have set up a tile server following this guide https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/. What is the best way to change the style of the map?'''
date = "2020-03-26T20:17:00Z"
lastmod = "2020-03-31T12:49:00Z"
weight = 73781
keywords = [ "style", "switch2osm", "mapnik" ]
aliases = [ "/questions/73781" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Changing style of the map](/questions/73781/changing-style-of-the-map)

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
<span id="post-73781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73781-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everyone,</p>
<p>I have set up a tile server following this guide <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/.">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/.</a> What is the best way to change the style of the map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '20, 20:17</strong></p>
<img src="https://secure.gravatar.com/avatar/8861beaab9476d8232a2db4ff00e0bbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JonasPonas&#39;s gravatar image" />
<p><span>JonasPonas</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JonasPonas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73781" class="comments-container">
<span id="73800"></span>
<div id="comment-73800" class="comment">
<div id="post-73800-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi. Do you want to switch to another style ? In this case I guess you should check that style's doc. Or customize the default one ? In this case you could start with this page : <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/CONTRIBUTING.md">https://github.com/gravitystorm/openstreetmap-carto/blob/master/CONTRIBUTING.md</a></p>
</div>
<div id="comment-73800-info" class="comment-info">
<span class="comment-age">(27 Mar '20, 19:10)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73814"></span>
<div id="comment-73814" class="comment">
<div id="post-73814-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, thanks for the reply. Yes i would like to change the default style and also create my own styles. As I understand I can use Kosmtik to create Mapnik ready map styles? I tried TileMill, but i could not figure out how to apply Mapnik xml format file, i imported said file and when running renderd it had a lot of errors. If I would fix those errors it should work? Nonetheless, i will try Kosmtik.</p>
</div>
<div id="comment-73814-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 15:58)</span> <span class="comment-user userinfo">JonasPonas</span>
</div>
</div>
<span id="73831"></span>
<div id="comment-73831" class="comment">
<div id="post-73831-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Editing pure Mapnik .xml is not to be recommended. Most people use CartoCSS and compile it with carto (the command-line utility).</p>
</div>
<div id="comment-73831-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 12:01)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="73839"></span>
<div id="comment-73839" class="comment">
<div id="post-73839-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A quick note about Tilemill - as I understand it, it was designed originally to handle the editing of CartoCSS map styles. Unfortunately, OSM's "standard" tile layer has a lot of layers and it was always a bit cumbersome to edit so many layers with Tilemill (they literally didn't all fit on screen). Tilemill's had some recent redevelopment, so things may have got better, but I'd still suggest working from the command line so that you can see all the moving parts and carefully do one thing at once.</p>
</div>
<div id="comment-73839-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 13:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73781-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="73838"></span>

<div id="answer-container-73838" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73838-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JonasPonas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends a bit on what sort of style change you're planning - if you want to perform minor changes to an existing style (and I'll assume that we're talking about <a href="https://github.com/gravitystorm/openstreetmap-carto">this one</a> for now), then start with that style, make minor changes to the source files (for example, try changing the colours at the top of <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/style/landcover.mss">this file</a>), then:</p>
<ul>
<li>rerun "carto project.mml &gt; mapnik.xml" in the <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">switch2osm guide</a>,</li>
<li>restart renderd,</li>
<li>restart apache,</li>
<li>and (probably) remove previously rendered metatiles.</li>
</ul>
<p>See the last few lines of <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_carto.sh">this script</a> for what I do when testing style changes.</p>
<p>Important - "carto" won't often flag up errors in the style file when run, so you'll need to keep an eye on your system's logfile to see errors like "... which failed to load" (against a map layer).</p>
<p>If you're changing something in the "lua" script that gets run at data load then you'll need to reload data as well. I use <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh">this script</a> for that - you won't want the stuff in there that's specific to the map style I use but the "get a small test area from Geofabrik only when I need a new one" part might be useful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '20, 13:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-73838" class="comments-container">
<span id="73840"></span>
<div id="comment-73840" class="comment not_top_scorer">
<div id="post-73840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, thanks for the reply. Could you explain if Kosmtik would make changing styles easier or I dont fully understand <a href="https://github.com/kosmtik/kosmtik?">https://github.com/kosmtik/kosmtik?</a></p>
</div>
<div id="comment-73840-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 15:10)</span> <span class="comment-user userinfo">JonasPonas</span>
</div>
</div>
<span id="73843"></span>
<div id="comment-73843" class="comment">
<div id="post-73843-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If I understand correctly the Kosmtik doc, it would replace renderd in your setup. The good point seems to be that changes in the style are rendered quickly. Bad point is that it doesn't support MapCSS, on which the main "openstreetmap-carto" style is based.</p>
<p>Hope this helps, I'm no specialist of these things.</p>
</div>
<div id="comment-73843-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 16:14)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73849"></span>
<div id="comment-73849" class="comment not_top_scorer">
<div id="post-73849-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, thanks for replying, correct if I am wrong but here it is written that: <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a></p>
<p>These stylesheets can be used in your own cartography projects, and are designed to be easily customised. They work with Kosmtik and also with the command-line CartoCSS processor.</p>
</div>
<div id="comment-73849-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 08:13)</span> <span class="comment-user userinfo">JonasPonas</span>
</div>
</div>
<span id="73862"></span>
<div id="comment-73862" class="comment">
<div id="post-73862-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a> No, osm-carto is based on CartoCSS, not MapCSS.</p>
</div>
<div id="comment-73862-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 14:30)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="73864"></span>
<div id="comment-73864" class="comment">
<div id="post-73864-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18040/jonasponas">@JonasPonas</a> I've never used Kosmtik, but would actually suggest editing everything manually to start with, because if something goes wrong you need people with two sets of knowledge (Kosmtik and CartoCSS) not just one.</p>
</div>
<div id="comment-73864-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 15:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="73868"></span>
<div id="comment-73868" class="comment">
<div id="post-73868-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5/richard">@Richard</a> Oups, sorry for the confusion. I guess I'm out of my league here.</p>
<p>Is the rest of my remark valid ? That kosmtik is a renderer, like renderd, but more for desktop use ?</p>
</div>
<div id="comment-73868-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 16:57)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73887"></span>
<div id="comment-73887" class="comment">
<div id="post-73887-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You're half right! Neither renderd nor Kosmtik are renderers: Mapnik is the renderer. Both Kosmtik and renderd are effectively glue code for Mapnik; they receive requests, fire them off to Mapnik, and then return the result. As you say, Kosmtik is intended for desktop use (and therefore includes a full UI), renderd for server use (no UI, but more performant).</p>
</div>
<div id="comment-73887-info" class="comment-info">
<span class="comment-age">(31 Mar '20, 12:49)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73838" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-73838-form-container" class="comment-form-container">
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

