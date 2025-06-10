+++
type = "question"
title = "Should I tag a park using landcover=grass or surface=grass?"
description = '''Using taginfo, it seems that surface=grass is much more popular (590k vs 19k), but it doesn&#x27;t differentiate between ways that form polygons and those that don&#x27;t, so I&#x27;m not sure which tag is more appropriate for areas.'''
date = "2020-01-02T08:50:00Z"
lastmod = "2020-01-03T07:09:00Z"
weight = 72324
keywords = [ "landcover", "grass", "park", "surface" ]
aliases = [ "/questions/72324" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should I tag a park using landcover=grass or surface=grass?](/questions/72324/should-i-tag-a-park-using-landcovergrass-or-surfacegrass)

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
<span id="post-72324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72324-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using taginfo, it seems that <code>surface=grass</code> is much more popular (590k vs 19k), but it doesn't differentiate between ways that form polygons and those that don't, so I'm not sure which tag is more appropriate for areas.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landcover" rel="tag" title="see questions tagged &#39;landcover&#39;">landcover</span> <span class="post-tag tag-link-grass" rel="tag" title="see questions tagged &#39;grass&#39;">grass</span> <span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-surface" rel="tag" title="see questions tagged &#39;surface&#39;">surface</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '20, 08:50</strong></p>
<img src="https://secure.gravatar.com/avatar/318c1da3c99b1d25f9834cbb24648736?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zismac&#39;s gravatar image" />
<p><span>Zismac</span><br />
<span class="score" title="136 reputation points">136</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zismac has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72324" class="comments-container">
<span id="72339"></span>
<div id="comment-72339" class="comment">
<div id="post-72339-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/Key:area"><code>area=yes</code></a> and <code>area=no</code> are accepted in combination with many tags that can be either an area or a loop.</p>
</div>
<div id="comment-72339-info" class="comment-info">
<span class="comment-age">(02 Jan '20, 17:36)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-72324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72324-form-container" class="comment-form-container">
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

<span id="72341"></span>

<div id="answer-container-72341" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72341-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Zismac has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What is typical for a park will vary according to cultural norms and climate. In Britain parks tend to be predominantly grass, but in Spain a park may contain limited areas of grass and many more hard surfaces and gravel paths. Therefore although leisure=park is conventionally rendered in green including on the Carto-CSS style this may reflect specific cultural expectations. Adding a surface tag can clarify that a park is indeed predominantly grass.</p>
<p>Landuse grass is used for many different things, but most usually for grassy places which have not, or cannot be easily, categorised as something else (parks, farmland etc). It is also often used to make areas appear green on CartoCSS (mapping for the renderer). Although it is possible to map grassy areas within a park as landuse=grass it's something I'd recommend avoiding. If the park is predominantly grass then put surface=grass on the main park, and ensure that surface is tagged on other park features (paths etc). If it is a wide mix of surfaces then it gets more complicated, and I don't believe there is a single good solution. One example might be the <a href="https://www.openstreetmap.org/relation/2200771">Queen Elizabeth Olympic Park</a> in East London which has been mapped in some detail.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '20, 23:02</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-72341" class="comments-container">
<span id="72345"></span>
<div id="comment-72345" class="comment">
<div id="post-72345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why do you recommend to avoid to map the grassy areas as landuse=grass? Personally, I want to know whether there are a lot of trees in a park that offer shade during hot days, but likewise, there might be people that want to know whether there are grassy areas (e.g. for relaxing in the sun). So I like it when people map a park in more detail and I try to do it myself too (eg. <a href="https://www.openstreetmap.org/way/27841723">Park Sorghvliedt</a> )</p>
</div>
<div id="comment-72345-info" class="comment-info">
<span class="comment-age">(03 Jan '20, 05:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="72346"></span>
<div id="comment-72346" class="comment">
<div id="post-72346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because landuse grass has way too many meanings. This is probably one situation where I think using a land over=grass would be OK (generally I don't think a land over tag solves any of the problems which it is supposed to it just moved them somewhere else, and creates new ones). The fundamental issues here are: we don't have a good tag vocabulary for different grassy places &amp; other than buildings we don't have a technique for mapping parts of elements).</p>
</div>
<div id="comment-72346-info" class="comment-info">
<span class="comment-age">(03 Jan '20, 07:09)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72341-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72334"></span>

<div id="answer-container-72334" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72334-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is also landuse=grass.</p>
<p>There is quite some discussion within the community whether that should actually be landcover=grass. The reasoning is that it is not really "use of the land", but rather "the land is covered by". But on the other hand, we should not take the keys of the tags too literally.</p>
<p>The wiki page for <a href="https://wiki.openstreetmap.org/wiki/Tag:leisure=pitch">leisure=pitch</a> also lists surface as a useful combination. I use surface typically for line features (e.g highways). I would use both landcover and landuse for grass areas inside a park. Typically there will be other surfaces in the park as well (bushes, trees, sand in playground, fine gravel for paths, etc)</p>
<p>So, in conclusion, I think that when there is already a "main"-tag such as highway or leisure, one can use surface. If you only want to map a grass area, use landuse/landcover.</p>
<p>p.s. only landuse=grass gets rendered on the default style</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '20, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '20, 13:56</strong> </span></p>
</div>
</div>
<div id="comments-container-72334" class="comments-container">
&#10;</div>
<div id="comment-tools-72334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72334-form-container" class="comment-form-container">
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

