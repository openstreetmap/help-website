+++
type = "question"
title = "Parish boundaries in Tandridge (Surrey, UK)"
description = '''The simple question is, how do I &#x27;make&#x27; parish boundaries for the parishes in Tandridge, UK? E.g. Oxted, Limpsfield, Titsey, and so on? And furthermore, what if part of one parish borders another, and another part, borders yet another? For example, the top half of the left side of Oxted borders Tits...'''
date = "2012-11-06T20:24:00Z"
lastmod = "2012-11-06T21:13:00Z"
weight = 17526
keywords = [ "surrey", "parish", "boundaries", "civil", "tandridge" ]
aliases = [ "/questions/17526" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Parish boundaries in Tandridge (Surrey, UK)](/questions/17526/parish-boundaries-in-tandridge-surrey-uk)

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
<span id="post-17526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17526-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The simple question is, how do I 'make' parish boundaries for the parishes in Tandridge, UK? E.g. Oxted, Limpsfield, Titsey, and so on? And furthermore, what if part of one parish borders another, and another part, borders yet another? For example, the top half of the left side of Oxted borders Titsey, but then, Limpsfield borders the bottom of Titsey, and the left of Oxted as well. Basically, it's like this:</p>
<p>Oxted|Titsey</p>
<p>Oxted|------<br />
</p>
<p>Oxted|Limpsfield</p>
<p>And does anyone know where to find out the exact boundaries of the parishes? All I know is that the parishes in Tandridge (district), are Bletchingley, Burstow, Caterham on the Hill, Caterham Valley, Chaldon, Chelsham and Farleigh, Crowhurst, Dormansland, Felbridge, Godstone, Horne, Limpsfield, Lingfield, Nutfield, Outwood, Oxted, Tandridge, Tatsfield, Titsey, Warlingham, Whyteleafe, and Woldingham... but as I said are there any sites or maps that show the detailed boundaries, to street level? And not just the shapes? E.g. exactly at what point on the A25 is the Oxted/Limpsfield parish boundary?</p>
<p>And should I name parish boundaries with CP at the end? E.g. Tandridge CP, to distinguish it from the district?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-surrey" rel="tag" title="see questions tagged &#39;surrey&#39;">surrey</span> <span class="post-tag tag-link-parish" rel="tag" title="see questions tagged &#39;parish&#39;">parish</span> <span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-civil" rel="tag" title="see questions tagged &#39;civil&#39;">civil</span> <span class="post-tag tag-link-tandridge" rel="tag" title="see questions tagged &#39;tandridge&#39;">tandridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '12, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/6035647123b433de9d9aaa4259d07e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheUltimateKoopa&#39;s gravatar image" />
<p><span>TheUltimateK...</span><br />
<span class="score" title="161 reputation points">161</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheUltimateKoopa has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-17526" class="comments-container">
&#10;</div>
<div id="comment-tools-17526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17526-form-container" class="comment-form-container">
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

<span id="17529"></span>

<div id="answer-container-17529" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17529-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Boundaries like parish boundaries are set up using a relation. Each section of the boundary is a single way which is then shared between the relations either side without duplicating the way. So each parish boundary ends up being made of a multiple ways each shared with neighbouring parishes. The relation can be a boundary relation or a multipolygon relation (views are split). A boundary relation can include the node for the village name in the boundary relation with a role of admin_centre. The admin_level for a UK parish is 10. Due to the way Mapnik renders boundaries it has become normal to add admin_level=10 to both the way and the relation.</p>
<p>The consensus is to not keep the CP at the end of the name, mostly because the real name does not have CP on the end.</p>
<p>I added the parish boundaries in the East Riding of Yorkshire which might serve as an example. There is a <a href="http://wiki.openstreetmap.org/wiki/Using_OS_Shapefiles">wiki page</a> about using OS OpenData which includes the boundary data which we are free to use, though there may be better ways to use the data now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Nov '12, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17529" class="comments-container">
&#10;</div>
<div id="comment-tools-17529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17529-form-container" class="comment-form-container">
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

