+++
type = "question"
title = "How can I indicate different categories of parking for an institution?"
description = '''My problem: I have been mapping the parking lots on the University of Louisville campus (see: https://www.openstreetmap.org/?lat=38.216213285923&amp;amp;lon=-85.760897397995&amp;amp;zoom=18). The university divides lots into colors - red/purple/blue, etc. The parking pass you buy determines which lots you ca...'''
date = "2012-09-22T05:18:00Z"
lastmod = "2012-09-24T13:58:00Z"
weight = 16333
keywords = [ "relations", "tagging", "categories", "parking" ]
aliases = [ "/questions/16333" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I indicate different categories of parking for an institution?](/questions/16333/how-can-i-indicate-different-categories-of-parking-for-an-institution)

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
<span id="post-16333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16333-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My problem: I have been mapping the parking lots on the University of Louisville campus (see: <a href="https://www.openstreetmap.org/?lat=38.216213285923&amp;lon=-85.760897397995&amp;zoom=18).">https://www.openstreetmap.org/?lat=38.216213285923&amp;lon=-85.760897397995&amp;zoom=18).</a> The university divides lots into colors - red/purple/blue, etc. The parking pass you buy determines which lots you can park in. I would like to indicate somehow which category each lot belongs to.</p>
<p>I have not found a way to tag parking lots in this way, and I'm not sure how to or if I should start adding this info. Would it be best to use a relation somehow?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-categories" rel="tag" title="see questions tagged &#39;categories&#39;">categories</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '12, 05:18</strong></p>
<img src="https://secure.gravatar.com/avatar/c4bef549649e73792906075419fac952?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dneelyep&#39;s gravatar image" />
<p><span>dneelyep</span><br />
<span class="score" title="125 reputation points">125</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dneelyep has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16333" class="comments-container">
&#10;</div>
<div id="comment-tools-16333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16333-form-container" class="comment-form-container">
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

<span id="16413"></span>

<div id="answer-container-16413" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16413-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dneelyep has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are those parkings reserved for specific groups of people ? If so, one to do this might be access=students/staff/etc. The set of access values actually distinguished by renderers is small, but if parking access matches something commonly seen in <a href="http://taginfo.openstreetmap.org/keys/access#values">taginfo</a>, there's no reason not to tag it.</p>
<p>The second/complementary option is to simply tag "name=Blue car park". It makes semantic sense, and most renderers will use that.</p>
<p>Lastly, there's the obvious-sounding "colour=" tag (the "color" spelling variant is less used in osm). No existing renderer (that I know of) uses that for car parks (it's more commonly used for route relations), but you could set up <a href="https://wiki.openstreetmap.org/wiki/Tilemill">your own renderer config</a> to display color-coded car parks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '12, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-16413" class="comments-container">
<span id="16420"></span>
<div id="comment-16420" class="comment">
<div id="post-16420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A couple additional ideas: access=blue_pass/red_pass/purple_pass, or access=private and a note about which pass is valid.</p>
</div>
<div id="comment-16420-info" class="comment-info">
<span class="comment-age">(24 Sep '12, 13:58)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-16413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16413-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16340"></span>

<div id="answer-container-16340" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16340-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-16340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, what do you want to see or show on the map, or do you need just a tag. If so consider amenity = parking with area = red or anything else for each separate lot. Or if the areas are separated by a longer way to the entrances, ad a distance instead of the color. But its only visible reading the map and the area doesnt colorize. Greetz Hendrik</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '12, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-16340" class="comments-container">
<span id="16347"></span>
<div id="comment-16347" class="comment">
<div id="post-16347-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><em>area=red</em> is not a good suggestion here, the <a href="https://wiki.openstreetmap.org/wiki/Key:area">area</a> tag is already used for different things. Better use the <a href="https://wiki.openstreetmap.org/wiki/Key:ref">ref</a> tag instead.</p>
</div>
<div id="comment-16347-info" class="comment-info">
<span class="comment-age">(22 Sep '12, 12:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16340-form-container" class="comment-form-container">
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

