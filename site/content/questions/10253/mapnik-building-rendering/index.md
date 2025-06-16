+++
type = "question"
title = "Mapnik building rendering"
description = '''If a building is tagged buildng=yes it rendrers in darker colour and with outline, if it is something else (building=appartments/building=garage...) it renderes in a lighter colour and without outline.  building=school is rendered (almost?) same as building=yes. Is this intentional? If it is, why? E...'''
date = "2012-01-26T23:12:00Z"
lastmod = "2012-01-28T19:53:00Z"
weight = 10253
keywords = [ "building", "rendering", "mapnik" ]
aliases = [ "/questions/10253" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Mapnik building rendering](/questions/10253/mapnik-building-rendering)

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
<span id="post-10253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10253-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If a building is tagged buildng=yes it rendrers in darker colour and with outline, if it is something else (building=appartments/building=garage...) it renderes in a lighter colour and without outline. building=school is rendered (almost?) same as building=yes.</p>
<p>Is this intentional? If it is, why?</p>
<p>Example can be seen <a href="https://www.openstreetmap.org/?lat=49.204433&amp;lon=16.593089&amp;zoom=18&amp;layers=M">here</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '12, 23:12</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '12, 23:17</strong> </span></p>
</div>
</div>
<div id="comments-container-10253" class="comments-container">
&#10;</div>
<div id="comment-tools-10253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10253-form-container" class="comment-form-container">
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

<span id="10259"></span>

<div id="answer-container-10259" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10259-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LM_1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you use building=house, etc for residential properties then non-residences stand out more, which I think looks quite good.</p>
<p>I am guessing it is intentional as the rule is in the style file; <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/inc/layer-buildings.xml.inc">'residential','house','garage','garages','detached','terrace','apartments'</a> are rendered without the line around them, and other buildings with the line (there seem to be special rules for stations, supermarkets, places of worship and airport terminals).</p>
<p>See for example <a href="http://osm.org/go/0EHmTf5k">here</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '12, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jan '12, 09:47</strong> </span></p>
</div>
</div>
<div id="comments-container-10259" class="comments-container">
<span id="10265"></span>
<div id="comment-10265" class="comment">
<div id="post-10265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Makes sense, it just looks weird if only one building in the area is tagged specifically.</p>
</div>
<div id="comment-10265-info" class="comment-info">
<span class="comment-age">(27 Jan '12, 10:16)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="10286"></span>
<div id="comment-10286" class="comment">
<div id="post-10286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This rendering decision confuses a lot of mappers (including local mappers I discussed it with) mostly because it does not match current tagging at all. Unremarkable buildings are usually building=yes, at <a href="http://taginfo.openstreetmap.org:8001/keys/building#values">96%</a> of buildings.</p>
<p>The fundamental problem with this style is, imo, that you need to map things as "not remarkable", when it should preferably be the other way round. I understand why it's done this way (it is easier to compile a list of values for "non-special" buildings), but I wonder if it will ever work really well.</p>
</div>
<div id="comment-10286-info" class="comment-info">
<span class="comment-age">(28 Jan '12, 04:30)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="10300"></span>
<div id="comment-10300" class="comment">
<div id="post-10300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would really make more sense if defaultly tagged buildings were considered insignificant and the important ones (usually tagged more precisely) according to this.</p>
</div>
<div id="comment-10300-info" class="comment-info">
<span class="comment-age">(28 Jan '12, 19:53)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-10259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10259-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10262"></span>

<div id="answer-container-10262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10262-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it is intentional. You can see the details directly in the <a href="http://trac.openstreetmap.org/browser/applications/rendering/mapnik/inc/layer-buildings.xml.inc">stylesheet</a>.</p>
<p>Why? It is a choice for better buildings distinction, see these tickets <a href="http://trac.openstreetmap.org/ticket/3463">#3463</a> <a href="http://trac.openstreetmap.org/ticket/3594">#3594</a> <a href="http://trac.openstreetmap.org/ticket/3610">#3610</a></p>
<p>If you have better proposition, I think that you can suggest them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '12, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-10262" class="comments-container">
&#10;</div>
<div id="comment-tools-10262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10262-form-container" class="comment-form-container">
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

