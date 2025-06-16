+++
type = "question"
title = "Needleleaved inner forest polygon not rendered: rendering or modelling problem?"
description = '''Hello, there. I modeled here a needle-leaved forest parcel in a bigger broad-leaved forest as an inner multipolygon, but this inner parcel is not rendered, as if there was nothing here, a big hole, full of nothing, in the middle of the forest. I&#x27;m wondering: did I messed up the modelling, or is the ...'''
date = "2016-09-27T08:58:00Z"
lastmod = "2018-04-05T18:55:00Z"
weight = 52242
keywords = [ "rendering", "forest", "multipolygon" ]
aliases = [ "/questions/52242" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Needleleaved inner forest polygon not rendered: rendering or modelling problem?](/questions/52242/needleleaved-inner-forest-polygon-not-rendered-rendering-or-modelling-problem)

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
<span id="post-52242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52242-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I modeled <a href="https://www.openstreetmap.org/#map=18/48.24100/6.17774" title="Problem map">here</a> a <a href="https://www.openstreetmap.org/way/444365950" title="inner parcel">needle-leaved forest parcel</a> in a bigger broad-leaved forest as an inner multipolygon, but this inner parcel is not rendered, as if there was nothing here, a big hole, full of nothing, in the middle of the forest. I'm wondering: did I messed up the modelling, or is the area misrendered?</p>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Sep '16, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52242" class="comments-container">
<span id="62920"></span>
<div id="comment-62920" class="comment">
<div id="post-62920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This issue has been fixed, and such inner polygons are now rendered correctly.</p>
</div>
<div id="comment-62920-info" class="comment-info">
<span class="comment-age">(05 Apr '18, 18:55)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
</div>
<div id="comment-tools-52242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52242-form-container" class="comment-form-container">
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

<span id="52371"></span>

<div id="answer-container-52371" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52371-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hard to believe but: "Not a bug, it's a feature"<br />
Assume that also means, it's not going to be "fixed" anytime soon.<br />
At least there are workarounds possible, more or less complicated.</p>
<p>As I've learned only recently too, after years of struggling and wasting endless time with this and other "mysterious forest bugs", those empty forest-in-forest inners are not a bug at all. This behavior is fully intentional!</p>
<p>The reason is that otherwise the old legacy style to create multipolygons would not work anymore. Way back when MPs were first invented, things worked completely different: the forest tag HAD to be given on all outers AND all inners too, not in the relation itself. Therefore it was decided, when the "new" method was introduced years later, that if inners contain the same tags as the relation itself, renderers SHALL keep ignoring such "duplicate" tags on inners. To keep compatibility with that legacy method.<br />
And of course that creates all sorts of rendering probs now, especially when people mix up old and new styles in the same relation (like tagging outer ways directly instead of tagging the relation)</p>
<p>Can't remember anymore where exactly this was explained by one of the osm history experts... Have read it on some discussion page, perhaps in a forum or the Talk mailing list. And the wiki contains a giant quotes collection of multipolygon discussions, some 30 pages filled with MP discussions going back some 10 years! Perhaps it was in that huge heap somewhere:<br />
<a href="https://wiki.openstreetmap.org/wiki/Talk:Relation:multipolygon">https://wiki.openstreetmap.org/wiki/Talk:Relation:multipolygon</a></p>
<p>The recommanded workaround for this non-bug with different leaftypes was to either<br />
- create a new MP relation for each forest-in-forest inner, just 1 member, and move the forest tag from the way into the new relation<br />
- or else to create duplicate ways for such inners: way-1 to stamp the hole into the big forest, and way-2 (NOT in any relation) to fill that hole with the smaller forest again. This also seems to be what those Corine-landcover monsters do.</p>
<p>The prob is, hardly anyone is aware of that issue, myself included until only recently, and therefore have occasionally "fixed" such "nonsense 1-member-relations" or "nonsense duplicate ways" :-(</p>
<p>Anyway, the example in the first post above contains 2 mini-forest inners.<br />
Have fixed the 2nd by using the first method, and left the first as is for comparison.</p>
<p>PS: of course this affects not only forests but all sorts of MULTIPOLYGONs, incl. meadows, water etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '16, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/1d0a9b10a28fd4ae36b38b5fbcc534d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wycbtma&#39;s gravatar image" />
<p><span>wycbtma</span><br />
<span class="score" title="116 reputation points">116</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wycbtma has one accepted answer">33%</span> </br></br></p>
</div>
</div>
<div id="comments-container-52371" class="comments-container">
&#10;</div>
<div id="comment-tools-52371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52371-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52270"></span>

<div id="answer-container-52270" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52270-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I dont expect to see much difference. Forest areas have a minor casing and the rendering does not distinguish between areas with different leaf_type tags (at least in part because this depends on a major refactoring of the osm2pgsql database schema). At best one might expect However I think you would expect to see narrow green lines outlining the parcels.</p>
<p>SomeoneElse has mapped an area of mixed woodland in Nottinghamshire in detail: <a href="https://www.openstreetmap.org/#map=16/53.1443/-1.0733&amp;layers=C">https://www.openstreetmap.org/#map=16/53.1443/-1.0733&amp;layers=C</a>. You can also view the area in Overpass-turbo <a href="http://overpass-turbo.eu/s/iCL">here</a>. This area is a useful testbed for creating a reasonably sized data set for extending the cartography, but perhaps more importantly understanding what is involved in mapping such places. You can make out the thin lines separating the different compartments, which should also be there in your case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '16, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-52270" class="comments-container">
<span id="52272"></span>
<div id="comment-52272" class="comment">
<div id="post-52272-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My vague recollection is that there's a known issue (possibly historical, possibly with osm2pgsql) with a multipolygon inner having the same area tag as an outer which causes the inner tag to "disappear".</p>
<p>If someone can find the same situation (inner forest or wood polygon within an outer) in the UK or Ireland I can investigate further.</p>
</div>
<div id="comment-52272-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 11:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52276"></span>
<div id="comment-52276" class="comment">
<div id="post-52276-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info I've reproduced the issue here, with a "mixed" inner in a "broadleaved" outer:</p>
<p><a href="https://www.openstreetmap.org/#map=19/53.18662/-1.34311">https://www.openstreetmap.org/#map=19/53.18662/-1.34311</a></p>
<p>My own rendering, which treats broadleaved wood as different to mixed wood doesn't show the hole (it renders a mixed area inside a broadleaved area) but OSM-Carto does.</p>
<p>Issues have been raised at <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/973">https://github.com/gravitystorm/openstreetmap-carto/issues/973</a> and <a href="https://github.com/openstreetmap/osm2pgsql/issues/185">https://github.com/openstreetmap/osm2pgsql/issues/185</a> . That osm2pgsql issue seems to have been closed because it was an "old-style" multipolygon, which isn't the case in my example. It probably needs raising again at osm2pgsql's github (I can't see a current issue describing it).</p>
<p>A workaround would be to avoid the use of multipolygons where possible (which makes sense from an "ease of mapping" perspective if your dealing with multipolygons that are "most of Thailand" or "most of Quebec") but in a simple example like yours a multipolygon should be a sensible way to map it.</p>
</div>
<div id="comment-52276-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 13:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52281"></span>
<div id="comment-52281" class="comment">
<div id="post-52281-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I didn't expect to see a difference either: I knew that different rendering for broad-leaved and needle-leaved wasn't effective because of some database issue, but I mapped it anyway for the day it will be rendered. Besides, I expected the inner polygon to be rendered, even if it is rendered the same way than the outer one; its disappearance is unexpected, and a bug IMO, as the underlying data is, AFAIK, valid, unless one can explain me why the data is malformed, or unoptimized, and why it causes the rendering bug.</p>
<p>I opened an issue on Github for that: <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/2381">https://github.com/gravitystorm/openstreetmap-carto/issues/2381</a></p>
</div>
<div id="comment-52281-info" class="comment-info">
<span class="comment-age">(28 Sep '16, 15:38)</span> <span class="comment-user userinfo">Penegal</span>
</div>
</div>
</div>
<div id="comment-tools-52270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52270-form-container" class="comment-form-container">
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

