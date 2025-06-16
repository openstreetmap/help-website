+++
type = "question"
title = "Residential and Industrial areas defined on OSM..."
description = '''Canton, Ohio (US) has huge polygons (the type created with the area tool) covering many square miles which are denoting both residential and industrial areas. They, however, do not seem to depict anything very close to reality; by that I mean that some obviously industrial areas are defined as resid...'''
date = "2013-07-25T05:03:00Z"
lastmod = "2013-07-25T19:26:00Z"
weight = 24549
keywords = [ "residential", "industrial", "polygon" ]
aliases = [ "/questions/24549" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Residential and Industrial areas defined on OSM...](/questions/24549/residential-and-industrial-areas-defined-on-osm)

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
<span id="post-24549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Canton, Ohio (US) has huge polygons (the type created with the area tool) covering many square miles which are denoting both residential and industrial areas. They, however, do not seem to depict anything very close to reality; by that I mean that some obviously industrial areas are defined as residential and vice-verse, and yet other physical areas are encompassed by BOTH residential and industrial polygons. Does anyone know if these are city zoning areas? Would it be permissible for me to consider deleting this giant polygons? Not too many other cities in my area have these polygons, with the exceptions of Kent, Ohio which is almost covered by one, and I found some in Cleveland, Ohio and a few other towns in my vicinity. The reason I'm interested in their possible deletion, is that they make editing the map more difficult in that it is hard to see through their shading, and it seems that objects within the polygons can be very difficult to select at times.</p>
<p>Any advice would be appreciated. I would never delete ANYTHING unless I was first absolutely certain that it was proper to do so.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-industrial" rel="tag" title="see questions tagged &#39;industrial&#39;">industrial</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '13, 05:03</strong></p>
<img src="https://secure.gravatar.com/avatar/f644da470dd54a21e08f5cf7e888099a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Evan%20Edwards&#39;s gravatar image" />
<p><span>Evan Edwards</span><br />
<span class="score" title="145 reputation points">145</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Evan Edwards has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24549" class="comments-container">
&#10;</div>
<div id="comment-tools-24549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24549-form-container" class="comment-form-container">
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

<span id="24565"></span>

<div id="answer-container-24565" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24565-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OSM, landuse areas should map what the land is actually used for, ie what is actually there on the ground. So if it is housing, map it as landuse=residential. If it is factories, map it as landuse=industrial etc.</p>
<p>Official planning designations (ie zoning) is not usually mapped in OSM.</p>
<p>If the current landuse mapping is inaccurate, then it is helpful to improve this. You can do this by editing and moving the existing areas. Or if areas are really inaccurate, it may be easiest to delete them, and draw new areas in their place. eg if a landuse area is mapped as covering a large part of the city which has a mixture of uses within, it may be best to replace this with smaller more specific areas.</p>
<p>Also, if an object in OSM appears to be inaccurate, you can check its history, and any source tags. This may tell you who added it originally, and what source it is from. This can give you an idea of whether it should be improved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '13, 13:08</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-24565" class="comments-container">
<span id="24579"></span>
<div id="comment-24579" class="comment">
<div id="post-24579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Vclaw, your comment and those of Gormo and Richard above have definitely helped. I now feel confident that I can edit rather than delete these polygons and that I can do the job incrementally as I find the time. I truly appreciate the advice and the philosophy behind the advice is actually quite useful too.</p>
</div>
<div id="comment-24579-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 19:26)</span> <span class="comment-user userinfo">Evan Edwards</span>
</div>
</div>
</div>
<div id="comment-tools-24565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24565-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24555"></span>

<div id="answer-container-24555" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24555-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>The reason I&#39;m interested in their possible deletion, is that they make editing the map more difficult in that it is hard to see through their shading, and it seems that objects within the polygons can be very difficult to select at times.</code></pre>
<p>That is a very bad reason for wanting to delete something. We do not delete stuff because it makes peoples life easier. With the proper tools (e.g. JOSM) you can filter out the objects you are not interested in.</p>
<p>On the other hand, if you say that these polygons do not convey the reality on the ground, then you should correct them.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dresidential">https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dresidential</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '13, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jul '13, 09:03</strong> </span></p>
</div>
</div>
<div id="comments-container-24555" class="comments-container">
<span id="24558"></span>
<div id="comment-24558" class="comment">
<div id="post-24558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the advice, I appreciate it very much. The main reason I was inquiring about their possible deletion was because they seem so wildly inaccurate, the editing considerations were secondary, I should have made that much clearer than I did.</p>
<p>I'm just going to leave them as they are. I'm afraid to correct them because I don't know if they may be actual city-of-Canton zoning boundaries and there are so many nodes and so much area that it would literally take me weeks if not months to accomplish the job. I will look into JOSM, it would be nice to be able to filter some things.</p>
</div>
<div id="comment-24558-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 10:17)</span> <span class="comment-user userinfo">Evan Edwards</span>
</div>
</div>
<span id="24568"></span>
<div id="comment-24568" class="comment">
<div id="post-24568-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"We do not delete stuff because it makes peoples life easier" - that's an over-simplification. OSM's most precious resource is the mapper, therefore we should optimise for ease of mapping. If the value of the information to the map is outweighed by the difficulty it causes to subsequent editors, then it arguably shouldn't be added in the first place.</p>
</div>
<div id="comment-24568-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 13:14)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="24571"></span>
<div id="comment-24571" class="comment">
<div id="post-24571-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>We should definately optimize for ease of mapping. We should also refrain from deleting stuff that is at least partly correct. It's the old (wikipedia) argument on "correct this very bad article" vs. "delete and start from scratch again". So yes, I oversimplified, I admit it. On the other hand, I would delete a polygon covering half of europe with <code>natural=wood</code>.</p>
</div>
<div id="comment-24571-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 14:50)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="24577"></span>
<div id="comment-24577" class="comment">
<div id="post-24577-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you again, Gormo, and Richard too. I really do appreciate the input from both of you and I do have a much clearer idea of how to proceed now as you will see in my reply to Vclaw below.</p>
</div>
<div id="comment-24577-info" class="comment-info">
<span class="comment-age">(25 Jul '13, 19:20)</span> <span class="comment-user userinfo">Evan Edwards</span>
</div>
</div>
</div>
<div id="comment-tools-24555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24555-form-container" class="comment-form-container">
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

