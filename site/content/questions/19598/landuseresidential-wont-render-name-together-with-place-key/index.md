+++
type = "question"
title = "Landuse=residential won&#x27;t render name together with place key."
description = '''When I map smaller villages I often make a polygon and tag it landuse=residential, place=village/hamlet and name=[name]. For some reason however, this won&#x27;t render the name of the village in any render style available on openstreetmap.org. Example: https://www.openstreetmap.org/?lat=55.59874&amp;amp;lon=...'''
date = "2013-02-05T23:17:00Z"
lastmod = "2013-05-11T07:37:00Z"
weight = 19598
keywords = [ "rendering", "landuse", "place", "mapnik", "residential" ]
aliases = [ "/questions/19598" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Landuse=residential won't render name together with place key.](/questions/19598/landuseresidential-wont-render-name-together-with-place-key)

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
<span id="post-19598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19598-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I map smaller villages I often make a polygon and tag it landuse=residential, place=village/hamlet and name=[name]. For some reason however, this won't render the name of the village in any render style available on openstreetmap.org. Example: <a href="https://www.openstreetmap.org/?lat=55.59874&amp;lon=13.40605&amp;zoom=15&amp;layers=M">https://www.openstreetmap.org/?lat=55.59874&amp;lon=13.40605&amp;zoom=15&amp;layers=M</a> landuse=residential without place tag for reference: <a href="https://www.openstreetmap.org/?lat=55.69905&amp;lon=13.19617&amp;zoom=17&amp;layers=M">https://www.openstreetmap.org/?lat=55.69905&amp;lon=13.19617&amp;zoom=17&amp;layers=M</a></p>
<p>How is this? Is this kind of mapping discouraged? I thought it best if the place name rendered at the center of the polygon, instead of where the mapper may have put the place node. Or is it simply a Mapnik bug?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '13, 23:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0210a545c865c5db5159bb059fe343d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grillo&#39;s gravatar image" />
<p><span>Grillo</span><br />
<span class="score" title="345 reputation points">345</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grillo has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-19598" class="comments-container">
&#10;</div>
<div id="comment-tools-19598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19598-form-container" class="comment-form-container">
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

<span id="19612"></span>

<div id="answer-container-19612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19612-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually the place tags go on nodes. If it's on a closed way, it's usually also tagged with boundary=administrative. See <a href="https://wiki.openstreetmap.org/wiki/Place">https://wiki.openstreetmap.org/wiki/Place</a> (NB: the villages of Veberod and Dalby near your example seem to use the node)</p>
<p>I've put a name on landuse only when it's a specific unified area (ie residential development, trailer park, powerplant, military base, etc) which is generally a smaller subsection of an administrative area.</p>
<p>Also, from the <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dresidential">landuse=residential</a> wiki page:</p>
<p>"The extent of the area should mark the boundary of known residential use, not the extent of the whole town or village, where they are not identical." It would appear in your example that not all of the area is residential?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '13, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-19612" class="comments-container">
<span id="19620"></span>
<div id="comment-19620" class="comment">
<div id="post-19620-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Key:place">place</a> tag is equally valid on areas.</p>
</div>
<div id="comment-19620-info" class="comment-info">
<span class="comment-age">(06 Feb '13, 17:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19635"></span>
<div id="comment-19635" class="comment">
<div id="post-19635-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I've used residential in this way at least the majority of the village is residential (there's some industrial tagged in the north of Genarp, my linked example)</p>
<p>Towns and villages aren't administrative units in Sweden, so it would be misleading to use administrative tags for them.</p>
<p>The main problem still stands though: why won't the name render just because there's a place tag in the area, together with the residential tag?</p>
</div>
<div id="comment-19635-info" class="comment-info">
<span class="comment-age">(06 Feb '13, 20:27)</span> <span class="comment-user userinfo">Grillo</span>
</div>
</div>
<span id="20383"></span>
<div id="comment-20383" class="comment">
<div id="post-20383-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry, but since the above really didn't answer my question (why place and residential won't render name, but only residential will), I voted it down.</p>
</div>
<div id="comment-20383-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 12:44)</span> <span class="comment-user userinfo">Grillo</span>
</div>
</div>
<span id="20390"></span>
<div id="comment-20390" class="comment">
<div id="post-20390-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Fair enough, but the literal answer to that is "because that's how the Mapnik rendering works right now". Use trac to search for or report bugs/wishes: <a href="https://trac.openstreetmap.org/query?component=mapnik&amp;order=id&amp;desc=1">https://trac.openstreetmap.org/query?component=mapnik&amp;order=id&amp;desc=1</a></p>
</div>
<div id="comment-20390-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 15:16)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-19612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19612-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20519"></span>

<div id="answer-container-20519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20519-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If an area is tagged as a place, its name is only rendered if area=yes is set.</p>
<p>But this doesn't make much sense to me. Place the residential area where it is, place an admin border where it is and place a place name node where you want the label to be placed.</p>
<p>/al</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '13, 09:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-20519" class="comments-container">
<span id="22250"></span>
<div id="comment-22250" class="comment">
<div id="post-22250-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, but we don't use admin borders for Swedish towns since they are not administrative units. Also thank you for the area suggestion, but I decided to make the place tag into a node of itself again.</p>
</div>
<div id="comment-22250-info" class="comment-info">
<span class="comment-age">(09 May '13, 22:51)</span> <span class="comment-user userinfo">Grillo</span>
</div>
</div>
<span id="22295"></span>
<div id="comment-22295" class="comment">
<div id="post-22295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>area=yes and place gets rendered? that doesn't work for me unfortunately.</p>
</div>
<div id="comment-22295-info" class="comment-info">
<span class="comment-age">(11 May '13, 07:37)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-20519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20519-form-container" class="comment-form-container">
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

