+++
type = "question"
title = "How to define the name of an area which is not an administrative area nor a village"
description = '''Hi I am contributing to OSM since years but I still have not found proper way to define name of an area. With area I mean an unsettled (or settled) area which is not an administrative object, nor city nor village. It is just an area in the landscape which local people gave a name. There is lot of su...'''
date = "2014-04-05T13:57:00Z"
lastmod = "2014-04-08T11:26:00Z"
weight = 32147
keywords = [ "locality", "place", "area" ]
aliases = [ "/questions/32147" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to define the name of an area which is not an administrative area nor a village](/questions/32147/how-to-define-the-name-of-an-area-which-is-not-an-administrative-area-nor-a-village)

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
<span id="post-32147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32147-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I am contributing to OSM since years but I still have not found proper way to define name of an area. With area I mean an unsettled (or settled) area which is not an administrative object, nor city nor village. It is just an area in the landscape which local people gave a name. There is lot of such places in Switzerland, like Alp da Munt in Val Mustair.</p>
<p>Sometimes I was using place=locality with the name, but this should be used only for single nodes and not for areas. This is important from the rendering point of view.</p>
<p>A possibility would be to set area=yes to place=locality, but this is not a recommended solution.</p>
<p>Any ideas are very welcome.</p>
<p>Milos</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-locality" rel="tag" title="see questions tagged &#39;locality&#39;">locality</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '14, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a0b089f2b6c8a69f354c0581a8810e3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Milos&#39;s gravatar image" />
<p><span>Milos</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Milos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Apr '14, 15:59</strong> </span></p>
</div>
</div>
<div id="comments-container-32147" class="comments-container">
&#10;</div>
<div id="comment-tools-32147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32147-form-container" class="comment-form-container">
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

<span id="32165"></span>

<div id="answer-container-32165" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32165-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-32165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Tag:place=locality">Place=locality</a> is quite correct for this usage, named places on earth that do not necessarily correspond to inhabited areas.</p>
<p>There's also nothing wrong with that tag being used on an area. In fact it's the opposite: although the <a href="http://taginfo.openstreetmap.org/tags/place=locality">current stats</a> show that it is much more frequently used on a node, that kind of data naturally applies to an area, not a node. All those locality nodes are certainly approximations (and often imports). As an example of place=locality usage, that's how <a href="http://www.openstreetmap.org/relation/3011969">townlands are mapped in Ireland</a>.</p>
<p>If your favorite rendering displays locality names for nodes but not for areas, you should probably file a bug with them. <a href="http://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">Don't tag for the renderer</a>. For the default "mapink" style on osm.org, see <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/">osm-carto</a>. Note that lately they did a fair amount of area vs node discrepency fixes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '14, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-32165" class="comments-container">
<span id="32167"></span>
<div id="comment-32167" class="comment">
<div id="post-32167-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding "area=yes" for the renderer is not the solution. But you may add a "landuse=*" tag which may help in your case.</p>
</div>
<div id="comment-32167-info" class="comment-info">
<span class="comment-age">(07 Apr '14, 09:54)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="32168"></span>
<div id="comment-32168" class="comment">
<div id="post-32168-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It depends on the feature of course, but I find it unlikely that the whole place=locality deserves a single landuse=* (I expect multiple landuse=* inside a place=locality).</p>
</div>
<div id="comment-32168-info" class="comment-info">
<span class="comment-age">(07 Apr '14, 10:24)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="32170"></span>
<div id="comment-32170" class="comment">
<div id="post-32170-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think that adding "area=yes" to something that IS an area could be accused of tagging for the renderer, could it?</p>
</div>
<div id="comment-32170-info" class="comment-info">
<span class="comment-age">(07 Apr '14, 11:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32195"></span>
<div id="comment-32195" class="comment">
<div id="post-32195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding area=yes to a closed way that isn't implicitly expected to be linear (such as one with a highway=*) is as harmless (data-wise) as oneway=no or layer=0, but it is not recommended.</p>
<p>If the renderer behaves differently with area=yes on a place=locality closed way, it's a renderer bug. And adding an otherwise useless tag to work around a renderer bug is "tagging for the renderer", even if the tag is harmless.</p>
</div>
<div id="comment-32195-info" class="comment-info">
<span class="comment-age">(08 Apr '14, 11:26)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-32165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32165-form-container" class="comment-form-container">
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

