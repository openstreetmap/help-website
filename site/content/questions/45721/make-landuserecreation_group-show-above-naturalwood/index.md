+++
type = "question"
title = "Make landuse=recreation_group show above natural=wood"
description = '''At https://www.openstreetmap.org/#map=14/60.8507/8.5202 I&#x27;m working on a multipolygon (https://www.openstreetmap.org/way/160841891) with lots of &quot;inner&quot;s to define the skiing area. The problem is that the branch to the east is covered by wood instead of being on top of the wood area. How do I fix th...'''
date = "2015-10-05T16:36:00Z"
lastmod = "2015-10-28T22:36:00Z"
weight = 45721
keywords = [ "openlayers", "landuse", "natural", "multipolygon" ]
aliases = [ "/questions/45721" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Make landuse=recreation_group show above natural=wood](/questions/45721/make-landuserecreation_group-show-above-naturalwood)

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
<span id="post-45721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45721-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>At <a href="https://www.openstreetmap.org/#map=14/60.8507/8.5202">https://www.openstreetmap.org/#map=14/60.8507/8.5202</a> I'm working on a multipolygon (<a href="https://www.openstreetmap.org/way/160841891">https://www.openstreetmap.org/way/160841891</a>) with lots of "inner"s to define the skiing area. The problem is that the branch to the east is covered by wood instead of being on top of the wood area. How do I fix that? Do I really need to use the layer tag? Could also split up the wood into two object but I wonder how this should be done correctly.</p>
<p>Interestingly enough, when the skiing area covered the wood on the west (next to Skarsnuten peak) the skiing area was rendered on top (although with "trees" in it). So why difference?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-natural" rel="tag" title="see questions tagged &#39;natural&#39;">natural</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '15, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/f5f518bf2004bb3f7ab129cf07cc8c59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AJensen&#39;s gravatar image" />
<p><span>AJensen</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AJensen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45721" class="comments-container">
<span id="45723"></span>
<div id="comment-45723" class="comment">
<div id="post-45723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What about splitting the area? Sometimes this isn't the worst idea, especially for complex shapes.</p>
</div>
<div id="comment-45723-info" class="comment-info">
<span class="comment-age">(05 Oct '15, 17:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45737"></span>
<div id="comment-45737" class="comment">
<div id="post-45737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You mean splitting the wood area covering the multipolygon? The wood area comes from an bigger import it seems like, so ideally I would like to leave that alone in case they would make future updates - but maybe splitting that area is simply the only and the proper way to deal with it...</p>
</div>
<div id="comment-45737-info" class="comment-info">
<span class="comment-age">(06 Oct '15, 08:53)</span> <span class="comment-user userinfo">AJensen</span>
</div>
</div>
</div>
<div id="comment-tools-45721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45721-form-container" class="comment-form-container">
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

<span id="45741"></span>

<div id="answer-container-45741" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45741-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AJensen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Firstly</strong>, I know it is used in North America, but use of <code>landuse=recreation_ground</code> for a ski area is stretching the use of this tag too far.</p>
<p>It may be unfortunate, but the usual british english term "recreation ground" does not refer to any area used for recreation, but for areas which are predominantly sports field. For me the two absolutely implict properties of a recreation ground are a) that it is covered by grass and b) that it is flat. A quick check on the wiki suggests that this is a widespread view. The problem is that by extending the meaning of recreation_ground it makes it impossible to make any implicit assumptions and hundreds of thousands of already mapped objects will need additional tags. I would suggest that you use <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dwinter_sports"><code>landuse=winter_sports</code></a>, or the alternative <a href="https://wiki.openstreetmap.org/wiki/Tag:site%3Dpiste"><code>site=piste</code></a> relation.</p>
<p><strong>Secondly</strong>, have no fear about breaking up imported polygons. OSM is not a repository for other people's data.</p>
<p><strong>Thirdly</strong>, unless there are stringent prohibitions about skiing through the trees I wouldn't worry about precisely delineating the ski area in such a manner excluding all areas between the pistes. The existing piste:type=downhill can be used on areas too and thus provides additional information about the width of a specific piste, and when taken in toto for a resort shows the area of on-piste skiing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '15, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-45741" class="comments-container">
<span id="46195"></span>
<div id="comment-46195" class="comment">
<div id="post-46195-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just a few comments: 1) landuse=winter_sports isn't rendered by standard mapnik so in that case I won't be able to see it on the map. 2) I understand that, but my reasoning was that we could be shooting ourselves in the foot if we make it difficult for other "providers" to improve on the data they provided down the road (= doing updates). But I can understand if that's not a main priority. 3) I just like to have the visual view of the actual skiing area. If piste:type=downhill is visibly rendered by standard mapnik I guess that could be used instead.</p>
</div>
<div id="comment-46195-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 19:27)</span> <span class="comment-user userinfo">AJensen</span>
</div>
</div>
<span id="46199"></span>
<div id="comment-46199" class="comment">
<div id="post-46199-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11549/ajensen">@AJensen</a> all pistes are shown on opensnowmap, although not absolutely sure how speedily it updates. Perhaps there is scope for a more general leisure=recreation_area tag, which would do what North American mappers expect leisure=recreation_ground to mean.</p>
</div>
<div id="comment-46199-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 22:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45741-form-container" class="comment-form-container">
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

