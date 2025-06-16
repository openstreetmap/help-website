+++
type = "question"
title = "Inner members of some multipolygon relation object are not rendered by some renderers"
description = '''I have an issue on how some multipolygons are processed by imposm or osm2pqsql. The problem arises for rendering mixed leaf type forests mapped with a MP. Let&#x27;s consider such a MP as:  relation: landuse=forest, leaf_type=broadleaved, leaf_cycle=deciduous, type=multipolygon outer: no tags inner1: lan...'''
date = "2018-10-04T11:16:00Z"
lastmod = "2018-11-03T14:09:00Z"
weight = 66159
keywords = [ "rendering", "imposm", "osm2pgsql", "relations", "multipolygon" ]
aliases = [ "/questions/66159" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Inner members of some multipolygon relation object are not rendered by some renderers](/questions/66159/inner-members-of-some-multipolygon-relation-object-are-not-rendered-by-some-renderers)

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
<span id="post-66159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66159-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an issue on how some multipolygons are processed by imposm or osm2pqsql.</p>
<p>The problem arises for rendering mixed leaf type forests mapped with a MP. Let's consider such a MP as:</p>
<ul>
<li>relation: landuse=forest, leaf_type=broadleaved, leaf_cycle=deciduous, type=multipolygon</li>
<li>outer: no tags</li>
<li>inner1: landuse=forest, leaf_type=needleleaved, leaf_cycle=evergreen</li>
<li>inner2: landuse=meadow</li>
<li>inner3: natural=water, water=pond</li>
</ul>
<p>Examples of this kind of MP live in OSM <a href="https://www.openstreetmap.org/relation/1653686">here</a> and <a href="https://www.openstreetmap.org/relation/1652966">here</a>.</p>
<p>I'm using imposm2 for importing OSM data to make some <a href="https://github.com/nobohan/OpenArdenneMap">paper maps</a> using a custom mapping aimed at rendering the leaf_type. However, with this kind of MP, I got blank holes in the forest for inner rings of type "inner1" that specify a different leaf_type than the relation. Inners like inner2 or inner3 are well rendered. This is not really a Mapnik problem since actually the inners of type "inner1" are not imported in my PostGIS DB using imposm2.</p>
<p>Actually, I'm not the only one to face problem with these kind of MP, since the Transport, the <a href="https://www.openstreetmap.org/way/364040915#map=14/49.7378/5.5572&amp;layers=H">Humanitarian</a> and the OpenCycleMap renderings also show these holes in the MP. I though of a limitation of imposm2 but the Humanitarian rendering is supposed to use osm2pgsql. I didn't check for OpenCycleMap nor the Transport Map.</p>
<p>The questions:</p>
<ul>
<li><p>Is it a limitation of both imposm2 and (a old version) of osm2pgsql? Can it be circumvented by a pre-processing of the raw osm data*?</p></li>
<li><p>Is there a better mapping practice for these MP (that does not trigger JOSM warning)?</p></li>
</ul>
<p>Thanks for the support,</p>
<p>EDIT: <a href="/questions/52242/needleleaved-inner-forest-polygon-not-rendered-rendering-or-modelling-problem">https://help.openstreetmap.org/questions/52242/needleleaved-inner-forest-polygon-not-rendered-rendering-or-modelling-problem</a> is a related question</p>
<p>juminet</p>
<p>* Actually if I manually delete the inners of type "inner1" from the relation, it works, but I'd like to find a automatic and better solution!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-imposm" rel="tag" title="see questions tagged &#39;imposm&#39;">imposm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '18, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7841360034567cd045edd29245f4d5e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juminet&#39;s gravatar image" />
<p><span>juminet</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juminet has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '18, 08:36</strong> </span></p>
</div>
</div>
<div id="comments-container-66159" class="comments-container">
&#10;</div>
<div id="comment-tools-66159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66159-form-container" class="comment-form-container">
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

<span id="66162"></span>

<div id="answer-container-66162" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66162-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a bit difficult to answer here. If you think that some software isn't doing the right thing, you should open tickets with those pieces of software.</p>
<p>There was a big change recently moving away from "old-style" multipolygons. The problems you are seeing might be related to that. Either people are using old versions of the software or haven't reimported the data or something like it. But that can not be answered in a general fashion, you have to ask the people developing or running this software.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '18, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-66162" class="comments-container">
<span id="66642"></span>
<div id="comment-66642" class="comment">
<div id="post-66642-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, there are some link about this <em>"... big change recently moving away from 'old-style' multipolygons"</em>? It is only a osm2pgsql news or a general OSM community decision?</p>
</div>
<div id="comment-66642-info" class="comment-info">
<span class="comment-age">(03 Nov '18, 12:17)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="66644"></span>
<div id="comment-66644" class="comment">
<div id="post-66644-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is a general thing, not osm2pgsql specific. You can read about this here: <a href="http://area.jochentopf.com/">http://area.jochentopf.com/</a></p>
</div>
<div id="comment-66644-info" class="comment-info">
<span class="comment-age">(03 Nov '18, 14:09)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-66162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66162-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66163"></span>

<div id="answer-container-66163" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66163-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The fact that the Standard rendering does render these inners, but as you wrote Humanitarian / Cycle Map / Transport not, does make it likely this is an issue of older versions of osm2pgsql being used.</p>
<p>Contacting the developers is probably only really sensible if you know the exact versions of the software being used by the renderings that fail.</p>
<p>I would definitely not change your tagging / mapping practice to suite a specific renderer or (older) version of an import tool, unless the MP are simply broken and invalid in JOSM, in which case you need to fix them. That doesn't seem likely here though, considering they do render fine in Standard style.</p>
<p><strong>The solution in your case seems to upgrade your own software stack.</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '18, 22:10</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '18, 22:15</strong> </span></p>
</div>
</div>
<div id="comments-container-66163" class="comments-container">
<span id="66164"></span>
<div id="comment-66164" class="comment">
<div id="post-66164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Side note: using a totally different import and rendering software stack based on ArcGIS, I don't see any issue with holes in these multipolygons, this is another indication that the MPs are sound.</p>
</div>
<div id="comment-66164-info" class="comment-info">
<span class="comment-age">(04 Oct '18, 22:15)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
</div>
<div id="comment-tools-66163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66163-form-container" class="comment-form-container">
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

