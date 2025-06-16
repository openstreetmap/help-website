+++
type = "question"
title = "Help me understand warning messages for relation id=2871705"
description = '''Using JOSM I have just added a high school having two open atria, areas that have no roof and are surrounded by building. I used a multi-polygon with role &quot;outer&quot; to describe the outer building and two multi-polygons with roles &quot;inner&quot; to describe the enclosed open areas. When I upload the data to O...'''
date = "2013-04-10T21:59:00Z"
lastmod = "2013-04-11T15:17:00Z"
weight = 21377
keywords = [ "josm", "multipolygon", "relations", "warnings" ]
aliases = [ "/questions/21377" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Help me understand warning messages for relation id=2871705](/questions/21377/help-me-understand-warning-messages-for-relation-id2871705)

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
<span id="post-21377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21377-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using JOSM I have just added a high school having two open atria, areas that have no roof and are surrounded by building. I used a multi-polygon with role "outer" to describe the outer building and two multi-polygons with roles "inner" to describe the enclosed open areas.</p>
<p>When I upload the data to OSM I get assorted warnings about the multipolygons. It is <a href="https://www.openstreetmap.org/browse/relation/2871705">relation id 2871705</a>. Can anyone help explain what's going on?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-warnings" rel="tag" title="see questions tagged &#39;warnings&#39;">warnings</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '13, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '13, 09:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span></p>
</div>
</div>
<div id="comments-container-21377" class="comments-container">
&#10;</div>
<div id="comment-tools-21377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21377-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="21381"></span>

<div id="answer-container-21381" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21381-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure what warnings you are getting, but you might want to move all the tags from the outer way to the relation. Think of the relation as describing the area you are mapping, so have the tags for what you are mapping on the relation. Think of the members of the relation with roles outer as describing the extent of the area and those with roles inner as describing any holes - those members don't need their own tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '13, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-21381" class="comments-container">
&#10;</div>
<div id="comment-tools-21381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21381-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21382"></span>

<div id="answer-container-21382" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21382-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main problem seems to be you have added an extra multipolygon relation in the same changeset, see <a href="https://www.openstreetmap.org/browse/relation/2871704">relation 2871704</a></p>
<p>This only has a single inner member, so it doesn't make much sense, which is why JOSM has a warning. The other multipolygon (2871705) seems to be fine. So just delete relation 2871704, and it should fix the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '13, 01:36</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-21382" class="comments-container">
<span id="21383"></span>
<div id="comment-21383" class="comment">
<div id="post-21383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I could see the "extra" relation in Potlatch2 easily but in JOSM it's obscured to the point that it's practically invisible, at least to me. How it got there I'll never know. I fiddled with the 3 multi-polygons in JOSM for 15 minutes, eventually completely redoing everything with no luck. Then I undid everything to return to initial conditions.</p>
<p>Finally, somehow, I did manage to delete 2871704 and after telling JOSM to Ignore the obviously incorrect error messages (empty relation, etc.) referring to 2871704 after it was deleted, the upload proceeded okay. I rearranged the members of the High School polygon so the "children" or inner polygons were below the "parent" or outer polygon. Maybe that did the trick, who knows?</p>
<p>No disrespect to the developers who are IMO pretty fantastic, but I must say the relation editor is one of the most difficult and opaque extensions I've ever used. Also, there seems to be no way to copy the error messages from the Validation window to include with my message.</p>
<p>It want to be able to use JOSM for my OSM work even though its difficult to learn but the sort of things that happened today are very frustrating.</p>
<p>Thanks for the help.</p>
</div>
<div id="comment-21383-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 04:10)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="21403"></span>
<div id="comment-21403" class="comment">
<div id="post-21403-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In JOSM, its probably easiest to switch on the Relations panel (Alt+Shift+R). That should list all of the relations in the area, and you can delete it from there.</p>
<p>Also, for the validation window, you can right-click on one of the warnings, and choose "Zoom to problem", then it should highlight the objects with the problem.</p>
</div>
<div id="comment-21403-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 12:34)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="21407"></span>
<div id="comment-21407" class="comment">
<div id="post-21407-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Vclaw - I was using the Relations Editor (see my complaint above) and I know about the Zoom to Error feature but how would one copy the actual text of the arcane error messages to for inclusion in a plea for help?</p>
</div>
<div id="comment-21407-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 14:34)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-21382" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21382-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21387"></span>

<div id="answer-container-21387" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21387-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, in JOSM I use the Create Multipolygon plugin. It even supports deep nesting, that's holes in holes in holes in holes, (if needed). There's not yet a help file in JOSM for the multipolygon plugin. What you do is construct all your areas, in this case the school and the two holes, tag them as you see fit, or leave the inners as untagged. Select/highlight all the areas to be included in the multipolygon, click Create Multipolygon, tags are correctly placed. When there are nested areas the inners and outers sometimes get mixed up so you have to open the relation editor rearrange/rename the inner and outer areas as necessary. I've found this method greatly reduces the number of problems I get when making multipolygons. Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '13, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '13, 08:18</strong> </span></p>
</div>
</div>
<div id="comments-container-21387" class="comments-container">
<span id="21408"></span>
<div id="comment-21408" class="comment">
<div id="post-21408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll try the Create Multipolygon extension. I did manage to map another school having two holes with the Relation Editor but this time I did it step by step, adding each inner polygon after creating the outer one and then putting the inners below the containing outer. I'm good for now - thanks again.</p>
</div>
<div id="comment-21408-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 15:17)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-21387" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21387-form-container" class="comment-form-container">
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

