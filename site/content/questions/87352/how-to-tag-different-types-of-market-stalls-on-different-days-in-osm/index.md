+++
type = "question"
title = "How to Tag Different Types of Market Stalls on Different Days in OSM?"
description = '''Hello OpenStreetMap community, I&#x27;m seeking advice on how to tag a weekly market which has different types of goods offered on different days. On Tuesdays, the market sells food and on Wednesdays, it sells clothes and various smaller items. I am familiar with the opening_hours tag, but as I understan...'''
date = "2023-06-06T16:58:00Z"
lastmod = "2023-06-13T17:10:00Z"
weight = 87352
keywords = [ "opening_hours", "market", "tagging" ]
aliases = [ "/questions/87352" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to Tag Different Types of Market Stalls on Different Days in OSM?](/questions/87352/how-to-tag-different-types-of-market-stalls-on-different-days-in-osm)

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
<span id="post-87352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87352-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OpenStreetMap community,</p>
<p>I'm seeking advice on how to tag a weekly market which has different types of goods offered on different days.</p>
<p>On Tuesdays, the market sells food and on Wednesdays, it sells clothes and various smaller items. I am familiar with the opening_hours tag, but as I understand, it doesn't support differentiating between the types of goods sold on different days.</p>
<p>Is there a more specific, machine-readable way to tag this in OSM, so it can accurately reflect the different products offered on different days?</p>
<p>Any guidance on this matter would be greatly appreciated. Thank you.</p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span> <span class="post-tag tag-link-market" rel="tag" title="see questions tagged &#39;market&#39;">market</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '23, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/07ada7feacac48b9534331b30ef3c453?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Copymaster86&#39;s gravatar image" />
<p><span>Copymaster86</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Copymaster86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87352" class="comments-container">
&#10;</div>
<div id="comment-tools-87352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87352-form-container" class="comment-form-container">
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

<span id="87353"></span>

<div id="answer-container-87353" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87353-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours#Summary_syntax">opening_hours</a> syntax supports comment field, so you can do something like:</p>
<p>Tue 08:00-12:00 "food market"; Wed 08:00-16:00 "clothes &amp; flea market"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '23, 23:43</strong></p>
<img src="https://secure.gravatar.com/avatar/666391973130e371bf8092f70c43df28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matija%20Nalis&#39;s gravatar image" />
<p><span>Matija Nalis</span><br />
<span class="score" title="750 reputation points">750</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matija Nalis has 2 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '23, 23:44</strong> </span></p>
</div>
</div>
<div id="comments-container-87353" class="comments-container">
<span id="87355"></span>
<div id="comment-87355" class="comment">
<div id="post-87355-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this the preferred way to tag this? Is this supported when one searches for "food" or "clothes" in a mobile app like OSMAnd? Would be reasonable to add two separate POI one: shop=greengrocer and the other shop=clothes, each one with the given opening_hours and maybe liking both to the closed way representing the market.</p>
</div>
<div id="comment-87355-info" class="comment-info">
<span class="comment-age">(07 Jun '23, 09:38)</span> <span class="comment-user userinfo">ernsterwinwg</span>
</div>
</div>
<span id="87358"></span>
<div id="comment-87358" class="comment">
<div id="post-87358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Is this supported when one searches for "food" or "clothes" in a mobile app like OSMAnd</p>
</blockquote>
<p>That would depend on the app, but is not really related to this question. E.g. would such an app find "regular" (i.e. same opening hours, always mixed selection of goods) <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=marketplace">amenity=marketplace</a> when searching for "food" or "clothes"? It might, or it might need to be enhanced with <a href="https://wiki.openstreetmap.org/wiki/Key:description">description=*</a> key or <a href="https://wiki.openstreetmap.org/wiki/Key:clothes">clothes=*</a> or <a href="https://taginfo.openstreetmap.org/search?q=sells%3A#keys">sells:*</a> prefix etc.</p>
</div>
<div id="comment-87358-info" class="comment-info">
<span class="comment-age">(07 Jun '23, 14:29)</span> <span class="comment-user userinfo">Matija Nalis</span>
</div>
</div>
<span id="87359"></span>
<div id="comment-87359" class="comment">
<div id="post-87359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Would be reasonable to add two separate POI one: shop=greengrocer and the other shop=clothes, each one with the given opening_hours</p>
</blockquote>
<p>That too would depend. If they were separate kiosks on the marketplace that only get used for one purpose and are closed rest of the time, then that would be correct option. If on the other hand there is <code>amenity=marketplace</code> with lots of empty stalls which get rented to different users on different days (i.e. how I understood the question), then one <a href="https://wiki.openstreetmap.org/wiki/Good_practice#Don&#39;t_map_temporary_events_and_temporary_features">should not be mapping those temporary features</a> due to lack of <a href="https://wiki.openstreetmap.org/wiki/Verifiability">verifiability</a>.</p>
</div>
<div id="comment-87359-info" class="comment-info">
<span class="comment-age">(07 Jun '23, 14:38)</span> <span class="comment-user userinfo">Matija Nalis</span>
</div>
</div>
<span id="87360"></span>
<div id="comment-87360" class="comment">
<div id="post-87360-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello Matija,</p>
<p>Thank you for your response. To provide more context, the marketplace in question does not have any kiosks that get rented out. Instead, it's a common space where vendors bring their goods and set up for the day.</p>
<p>On Tuesdays, the vendors sell food items, and on Wednesdays, the vendors sell clothes and various smaller items. There are no permanent structures that could be tagged individually.</p>
<p>Given this situation, how would it be best to represent this in OSM? Since the type of goods sold changes depending on the day, is there a way to make this clear while maintaining verifiability?</p>
<p>Thank you for your continued help on this matter.</p>
</div>
<div id="comment-87360-info" class="comment-info">
<span class="comment-age">(07 Jun '23, 20:59)</span> <span class="comment-user userinfo">Copymaster86</span>
</div>
</div>
<span id="87362"></span>
<div id="comment-87362" class="comment">
<div id="post-87362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In that case I'd suggest as I originally wrote, just tag the whole amenity=marketplace area with:</p>
<p>opening_hours=Tue 08:00-12:00 "food market"; Wed 08:00-16:00 "clothes &amp; flea market"</p>
<p>You can use overpass query like this: <a href="https://overpass-turbo.eu/s/1vVB">https://overpass-turbo.eu/s/1vVB</a> to find similarly tagged locations (with at least two time-based with comments), and try it out how they work in your location and app. It works for me in OsmAnd nicely, displaying both the time and the comment that time range relates to.</p>
</div>
<div id="comment-87362-info" class="comment-info">
<span class="comment-age">(10 Jun '23, 23:05)</span> <span class="comment-user userinfo">Matija Nalis</span>
</div>
</div>
<span id="87370"></span>
<div id="comment-87370" class="comment not_top_scorer">
<div id="post-87370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much, I'll try it out</p>
</div>
<div id="comment-87370-info" class="comment-info">
<span class="comment-age">(13 Jun '23, 17:10)</span> <span class="comment-user userinfo">Copymaster86</span>
</div>
</div>
</div>
<div id="comment-tools-87353" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-87353-form-container" class="comment-form-container">
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

