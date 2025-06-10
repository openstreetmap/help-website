+++
type = "question"
title = "Overpass Api, wrong order of nodes??"
description = '''Hi, I want to extract a route with the Overpass API which works great. But I have some problemns getting the order of the nodes inside the relation right. Check this relation: http://overpass-turbo.eu/s/hao It looks good on the map. But when you look at the data tab and you scroll a little down you ...'''
date = "2016-07-06T16:00:00Z"
lastmod = "2016-07-07T02:09:00Z"
weight = 50685
keywords = [ "overpass", "api", "order", "relations" ]
aliases = [ "/questions/50685" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Api, wrong order of nodes??](/questions/50685/overpass-api-wrong-order-of-nodes)

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
<span id="post-50685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50685-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to extract a route with the Overpass API which works great. But I have some problemns getting the order of the nodes inside the relation right.</p>
<p>Check this relation: <a href="http://overpass-turbo.eu/s/hao">http://overpass-turbo.eu/s/hao</a></p>
<p>It looks good on the map. But when you look at the data tab and you scroll a little down you see the coordinates jump from</p>
<ul>
<li>13.8223610, 100.5474506</li>
<li>To</li>
<li>15.1323097, 100.4504222</li>
</ul>
<p>which is in the middle of the route. At the bottom there are the parts which are in between. (14.xxx)</p>
<p>So when I extract the route, process all the coordinates in the order the api returns them and convert it to a Google Polyline path, the route is messed up.</p>
<p>Paste this path into Google maps example (<a href="https://developers.google.com/maps/documentation/utilities/polylineutility">https://developers.google.com/maps/documentation/utilities/polylineutility</a> and click decode polyline)</p>
<pre><code>kfrsAefydRprJztDc|bGdiP}qQvlPiqV~fHofUzrYk|@r[snUaWeoTneDsnAadA_xAepGgC{hBwoB{{DgkN{rEelCuEicZmlKs`EitC}_NcyE_b`@awB}|I~|BatOvyB{wFrdDu|@xuBclKjtAanBdcAsjNp{E{~GIweKt|Bsd\}Q{wf@daO}dQz`MwsFtqEclJ{sAiuRdjBicGccCm}FyP}~Do`AmlFpD_dCpt@q}L~f@sgFedAgSqhBskMia@e}Rr}MjjIygJxyDo}B~vBtG{bSvhN{xB|Scmc@l{V}HkmB`sByoAd_BuvD~{Bg`Lb|Ciy@rs@r_@|kFat@|}BzhC|tFeTog}@j{`@|hFj}Bjy@}E`dGwoEyu@gcF|{GvZqqXxxHcu|@hmtBffJsM`_Dx`@feE}vAts@gaAs|Ag_CfpA}aD|rCwpCzwKigV`fOsiK_{B_~FybDmlBmuB_gF~f@wfFeFs|DqbAg}@iTgwKmt@c|D_qAg{@anAk_D`ZosB`}BiKr|AmdBbzGnE``B|f@_yx@vmuBbaA~@eiCraHe]gbGfeBk`@qiAphHmiD|v_@jcFky@rrJtd@cuAebFjVedEopDqpJe_BowAokGjg[eqFr_DlaCs_CvnB__@ycHjoDinXkmBrxAae@hyIdD~sHbrCgb`@nShyHweCxn_YojhIoh@oVkiS`^m`LePe{KdkDy_Qx`Oqji@rdHwb@lRijV~uUlyhCq`l@pmEhbLr|BjeDzyC~RvvMuWboFr[dj}AxxKicMcxD{ySmnJgq@sIyfPxbAalKpbAcsOl|@wmJgj@zq_BrcL</code></pre>
<p>How do I get overpass to give the nodes inside the relation in the correct order??</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '16, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/cbcec43f8f6c9d5b869aa5bdc56eb673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NLAnaconda&#39;s gravatar image" />
<p><span>NLAnaconda</span><br />
<span class="score" title="166 reputation points">166</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NLAnaconda has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50685" class="comments-container">
&#10;</div>
<div id="comment-tools-50685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50685-form-container" class="comment-form-container">
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

<span id="50686"></span>

<div id="answer-container-50686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50686-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your conversion routine does not seem to work correctly. Ways in relations don't need to follow the exact sequence of a route. As Overpass API delivers the data in the exact same sequence as they are in the main OSM database, it's your responsibility to bring them in the right sequence in a post-processing step.</p>
<p>As additional hint, please see this answer by scai: <a href="http://stackoverflow.com/questions/27403202/how-to-convert-an-osmar-object-osm-relation-containing-several-ways-to-a-close">link</a></p>
<p>Furthermore, you might want to check the result of <code>(relation(1820650);&gt;;);out meta;</code> to get all node ids as well. <code>out geom;</code> only provides lat/lon values of nodes, but omits all node ids.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '16, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '16, 17:08</strong> </span></p>
</div>
</div>
<div id="comments-container-50686" class="comments-container">
<span id="50694"></span>
<div id="comment-50694" class="comment">
<div id="post-50694-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, Got it working: <a href="http://bl.ocks.org/d/982ee618ffc16fbc82f463026ebcb7b5">http://bl.ocks.org/d/982ee618ffc16fbc82f463026ebcb7b5</a></p>
</div>
<div id="comment-50694-info" class="comment-info">
<span class="comment-age">(07 Jul '16, 02:09)</span> <span class="comment-user userinfo">NLAnaconda</span>
</div>
</div>
</div>
<div id="comment-tools-50686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50686-form-container" class="comment-form-container">
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

