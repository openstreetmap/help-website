+++
type = "question"
title = "Reversible Way for HOVs"
description = '''A motorway near me contains a separate travel corridor specifically for HOV traffic. The corridor is oneway at any given time but reverses to accommodate morning and evening rush hour traffic. The corridor is correctly represented on the map as a separate way but it does not have the proper conditio...'''
date = "2017-08-05T20:20:00Z"
lastmod = "2017-08-07T02:45:00Z"
weight = 57470
keywords = [ "hov", "restrictions", "reversible", "conditional" ]
aliases = [ "/questions/57470" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reversible Way for HOVs](/questions/57470/reversible-way-for-hovs)

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
<span id="post-57470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57470-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A motorway near me contains a separate travel corridor specifically for HOV traffic. The corridor is oneway at any given time but reverses to accommodate morning and evening rush hour traffic. The corridor is correctly represented on the map as a separate way but it does not have the proper conditional tagging to reflect the change in direction and vehicle type restriction. The corridor is open to HOV traffic traveling in the forward (as drawn) direction Mo-Fri 14:00 -05:00 and in the backward direction Mo-Fri 6:00-13:00. For simplicity, all other times the way can be regarded as closed for all traffic in both directions.</p>
<p>Ignoring the lane, layer and name tagging, I'm thinking this way should be tagged as follows.</p>
<p>highway=motorway<br />
access=no<br />
oneway:hov:forward:conditional=yes @ Mo-Fri 14:00-05:00<br />
oneway:hov:backward:conditional=yes @ Mo-Fri 6:00-13:00</p>
<p>Any thoughts or suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hov" rel="tag" title="see questions tagged &#39;hov&#39;">hov</span> <span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span> <span class="post-tag tag-link-reversible" rel="tag" title="see questions tagged &#39;reversible&#39;">reversible</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '17, 20:20</strong></p>
<img src="https://secure.gravatar.com/avatar/37f70927fe27ade9cf8f83cf924554ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="userJeff&#39;s gravatar image" />
<p><span>userJeff</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="userJeff has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-57470" class="comments-container">
<span id="57471"></span>
<div id="comment-57471" class="comment">
<div id="post-57471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are the 1 hour gaps 5:00-6:00 &amp; 13:00-14:00 intended?</p>
</div>
<div id="comment-57471-info" class="comment-info">
<span class="comment-age">(05 Aug '17, 22:28)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="57472"></span>
<div id="comment-57472" class="comment">
<div id="post-57472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes the 1 hr gaps are intended as changeover periods. Also, I plan on assuming no access on weekends. The weekend schedule is less predictable and there is little benefit to routing on this way during the lighter weekend traffic.</p>
</div>
<div id="comment-57472-info" class="comment-info">
<span class="comment-age">(06 Aug '17, 00:09)</span> <span class="comment-user userinfo">userJeff</span>
</div>
</div>
<span id="57482"></span>
<div id="comment-57482" class="comment">
<div id="post-57482-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I find the "oneway:forward" and "oneway:backward" tags a little confusing. Sure, <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions#Tagging">the syntax</a> allows them, but semantically, a oneway attribution applies to both travel directions. Would it be clearer to drop :forward/:backward modifiers and instead set <code>oneway:hov:conditional = yes @ Mo-Fri 14:00-05:00; -1 @ Mo-Fri 6:00-13:00</code> using the <a href="https://wiki.openstreetmap.org/wiki/Key:oneway#List_of_values"><code>oneway=-1</code></a> tag? Or perhaps change "oneway:hov:forward:conditional" to "hov:forward:conditional" so it is a conditional access= <em>rather than a conditional oneway=</em>.</p>
</div>
<div id="comment-57482-info" class="comment-info">
<span class="comment-age">(06 Aug '17, 17:41)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57484"></span>
<div id="comment-57484" class="comment">
<div id="post-57484-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Both of those options are clearer in my head. If I understand, these alternatives tagging schemes are</p>
<p>highway=motorway<br />
access=no<br />
oneway:hov:conditional = yes @ Mo-Fri 14:00-05:00; ; -1 @ Mo-Fri 6:00-13:00</p>
<p>OR</p>
<p>highway=motorway<br />
access=no<br />
hov:forward:conditional = yes @ Mo-Fri 14:00-05:00<br />
hov:backward:conditional = yes @ Mo-Fri 6:00-13:00</p>
<p>Are there any other tags required in either case?</p>
</div>
<div id="comment-57484-info" class="comment-info">
<span class="comment-age">(07 Aug '17, 02:13)</span> <span class="comment-user userinfo">userJeff</span>
</div>
</div>
<span id="57485"></span>
<div id="comment-57485" class="comment">
<div id="post-57485-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, now that I see it spelled out, I think only the second example is valid: in the first example nothing overrides the access=no tag.</p>
<p>Also, "Fri" should be changed to "Fr", since the opening_hours syntax requires 2-letter abbreviations.</p>
</div>
<div id="comment-57485-info" class="comment-info">
<span class="comment-age">(07 Aug '17, 02:45)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-57470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57470-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

