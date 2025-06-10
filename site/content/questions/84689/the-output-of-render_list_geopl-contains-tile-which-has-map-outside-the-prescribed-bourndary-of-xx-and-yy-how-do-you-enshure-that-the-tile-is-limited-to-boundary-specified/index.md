+++
type = "question"
title = "The output of render_list_geo.pl contains tile which has map outside the prescribed bourndary of x,X and y,Y How do you enshure that the tile is limited to boundary specified?"
description = '''Any advice on how to understand exact gps co-ordinates on tile boundaries that are rendered. I want to limit the boundary of tile rendered upto a certain box, whoes co-ordinates are specified by GPS co-ordinates'''
date = "2022-06-03T11:43:00Z"
lastmod = "2022-06-03T12:20:00Z"
weight = 84689
keywords = [ "openstreetmap", "render_list", "mod_tile" ]
aliases = [ "/questions/84689" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The output of render_list_geo.pl contains tile which has map outside the prescribed bourndary of x,X and y,Y How do you enshure that the tile is limited to boundary specified?](/questions/84689/the-output-of-render_list_geopl-contains-tile-which-has-map-outside-the-prescribed-bourndary-of-xx-and-yy-how-do-you-enshure-that-the-tile-is-limited-to-boundary-specified)

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
<span id="post-84689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84689-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Any advice on how to understand exact gps co-ordinates on tile boundaries that are rendered. I want to limit the boundary of tile rendered upto a certain box, whoes co-ordinates are specified by GPS co-ordinates</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '22, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d561310552086ae83097f8a3b8394be7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="royrod&#39;s gravatar image" />
<p><span>royrod</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="royrod has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84689" class="comments-container">
<span id="84690"></span>
<div id="comment-84690" class="comment">
<div id="post-84690-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you give details of the parameters you used (with what version) and what tile got rendered in error?</p>
</div>
<div id="comment-84690-info" class="comment-info">
<span class="comment-age">(03 Jun '22, 11:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84691"></span>
<div id="comment-84691" class="comment">
<div id="post-84691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>render_list_geo.pl -n 1 -z 20 -Z 20 -Y -35.3126827027 -y -35.3133302143 -X 149.095972244 -x 149.096765757 -m ajt</p>
<p>I used this as the parameters. I was expecting the tile to be limited by:</p>
<p><a href="https://www.google.com/maps/place/35%C2%B018&#39;45.7%22S+149%C2%B005&#39;45.5%22E/@-35.3126827,149.0937835,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0xa14acd77fb345e63!8m2!3d-35.3126827!4d149.0959722">https://www.google.com/maps/place/35%C2%B018'45.7%22S+149%C2%B005'45.5%22E/@-35.3126827,149.0937835,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0xa14acd77fb345e63!8m2!3d-35.3126827!4d149.0959722</a></p>
<p><a href="https://www.google.com/maps/place/35%C2%B018&#39;48.0%22S+149%C2%B005&#39;48.4%22E/@-35.3133302,149.0945771,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0xf50720905cbbd220!8m2!3d-35.3133302!4d149.0967658">https://www.google.com/maps/place/35%C2%B018'48.0%22S+149%C2%B005'48.4%22E/@-35.3133302,149.0945771,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0xf50720905cbbd220!8m2!3d-35.3133302!4d149.0967658</a></p>
<p>But what I got instead was a shifted version of the tile and not limited by the boundaries I specified.</p>
</div>
<div id="comment-84691-info" class="comment-info">
<span class="comment-age">(03 Jun '22, 12:11)</span> <span class="comment-user userinfo">royrod</span>
</div>
</div>
<span id="84692"></span>
<div id="comment-84692" class="comment">
<div id="post-84692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><img src="https://help.openstreetmap.org/upfiles/ig.JPG" alt="alt text" /></p>
<p>This is what got rendered, different from what I expected</p>
</div>
<div id="comment-84692-info" class="comment-info">
<span class="comment-age">(03 Jun '22, 12:20)</span> <span class="comment-user userinfo">royrod</span>
</div>
</div>
</div>
<div id="comment-tools-84689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84689-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

