+++
type = "question"
title = "How do I tag a juice bar?"
description = '''In Morroco, there are very different places depending of what you want to drink:  coffee or tea beer juice  How should I tag them?  coffee or tea: amenity = drink beer: amenity = amenity juice: amenity = drink  How to make a difference between a coffee bar and a juice bar? Should I add shop:drinks o...'''
date = "2016-06-04T12:18:00Z"
lastmod = "2019-11-15T10:12:00Z"
weight = 50014
keywords = [ "juice", "bar", "tagging", "drinks" ]
aliases = [ "/questions/50014" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I tag a juice bar?](/questions/50014/how-do-i-tag-a-juice-bar)

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
<span id="post-50014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50014-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Morroco, there are very different places depending of what you want to drink:</p>
<ul>
<li>coffee or tea</li>
<li>beer</li>
<li>juice</li>
</ul>
<p>How should I tag them?</p>
<ul>
<li>coffee or tea: amenity = drink</li>
<li>beer: amenity = amenity</li>
<li>juice: amenity = drink</li>
</ul>
<p>How to make a difference between a coffee bar and a juice bar?</p>
<p>Should I add shop:drinks or drink:juice for the juice bar?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-juice" rel="tag" title="see questions tagged &#39;juice&#39;">juice</span> <span class="post-tag tag-link-bar" rel="tag" title="see questions tagged &#39;bar&#39;">bar</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-drinks" rel="tag" title="see questions tagged &#39;drinks&#39;">drinks</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '16, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/47b14cbe3e92cf59763de21f144570b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Toub&#39;s gravatar image" />
<p><span>Toub</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Toub has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '16, 15:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-50014" class="comments-container">
&#10;</div>
<div id="comment-tools-50014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50014-form-container" class="comment-form-container">
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

<span id="50017"></span>

<div id="answer-container-50017" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50017-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Toub has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would go for this: <span><code>amenity=bar</code></span> + <span><code>drink</code></span><code>:juice=served</code> (or =yes) (see the current usage in the <span>taginfo keys overview</span>). The drink: namespace is somewhat popular. Just choose the amenity tag to many the kind of place (see the "similar tags" section on the amenity=bar wiki page). Could be that another <code>amenity</code> tag is more suitable instead of <code>bar</code>.</p>
<p>As always if there could be a misunderstanding of tags it is wise to add a <span><code>description</code></span> tag too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '16, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '16, 20:36</strong> </span></p>
</div>
</div>
<div id="comments-container-50017" class="comments-container">
<span id="50041"></span>
<div id="comment-50041" class="comment">
<div id="post-50041-score" class="comment-score">
6
</div>
<div class="comment-text">
<p>Thanks for your answer.</p>
<p>However, amenity=bar is related to an "establishment that sells alcoholic drinks".</p>
<p>So probably that amenity=cafe, related to a "generally informal place with sit-down facilities selling beverages", is more adapted. Especially in Morocco where alcohol is never available in a "café".</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcafe">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcafe</a> <a href="http://taginfo.openstreetmap.org/search?q=cafe#values">http://taginfo.openstreetmap.org/search?q=cafe#values</a></p>
<p>So is "amenity=cafe" + "drink:juice=served" better?</p>
</div>
<div id="comment-50041-info" class="comment-info">
<span class="comment-age">(06 Jun '16, 11:27)</span> <span class="comment-user userinfo">Toub</span>
</div>
</div>
<span id="50043"></span>
<div id="comment-50043" class="comment">
<div id="post-50043-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/12387/toub"></a><a href="http://help.openstreetmap.org/users/12387/toub">@Toub</a>: yes, that sounds fine to me. Maybe add also <code>drink:coffee=no</code> to make it clear that there is no coffee available (if that is the case). Do not forget a <code>description</code> tag, then everybody (also end users) know what is meant here. If I remember correctly e.g. OsmAnd shows a <code>description</code> tag in object's details.</p>
</div>
<div id="comment-50043-info" class="comment-info">
<span class="comment-age">(06 Jun '16, 19:03)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="50465"></span>
<div id="comment-50465" class="comment">
<div id="post-50465-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> could you please update your answer, so I can mark it as accepted.</p>
<p>So the recommendation is:</p>
<ul>
<li>"amenity=cafe"</li>
<li>"drink:juice=served"</li>
<li>"coffee=no"</li>
<li>"description=juice bar"</li>
</ul>
<p>Also, should we update the wiki? <a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcafe">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcafe</a></p>
</div>
<div id="comment-50465-info" class="comment-info">
<span class="comment-age">(26 Jun '16, 15:02)</span> <span class="comment-user userinfo">Toub</span>
</div>
</div>
<span id="50466"></span>
<div id="comment-50466" class="comment">
<div id="post-50466-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/12387/toub">@Toub</a>: Depending on the country you are in, a bar is not a place where you get alcoholic drinks (only/mainly). Since from these countries there are only little mappers in OSM, this fact isn't widely known &amp; spread here…</p>
<p>For aseerel4c26's answer I'd enhance only slightly: use <em>drink:juice=only</em>, when only juice is served.</p>
</div>
<div id="comment-50466-info" class="comment-info">
<span class="comment-age">(26 Jun '16, 15:41)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="50469"></span>
<div id="comment-50469" class="comment">
<div id="post-50469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/583/malenki">@malenki</a>: from where did you get the "only"? Not in use currently for this prefix, is it?</p>
</div>
<div id="comment-50469-info" class="comment-info">
<span class="comment-age">(26 Jun '16, 20:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="50471"></span>
<div id="comment-50471" class="comment not_top_scorer">
<div id="post-50471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>: from common sense. :)<br />
I didn't check all possible subkeys of drink:* for all possible values. <a href="https://wiki.openstreetmap.org/wiki/Key:organic">Organic</a> e.g. knows "only" as value.</p>
</div>
<div id="comment-50471-info" class="comment-info">
<span class="comment-age">(26 Jun '16, 20:55)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="50472"></span>
<div id="comment-50472" class="comment not_top_scorer">
<div id="post-50472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/583/malenki">@malenki</a>: I am not sure if "only" makes sense here and if it is useful to have that many values, but I remember that I have seen "only" in documentation of some tag...</p>
</div>
<div id="comment-50472-info" class="comment-info">
<span class="comment-age">(26 Jun '16, 22:07)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50017" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50017-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71645"></span>

<div id="answer-container-71645" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71645-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a new tagging proposal now: <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Juice_bar">https://wiki.openstreetmap.org/wiki/Proposed_features/Juice_bar</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '19, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a28e06c92c1203085990d63059952e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="takje&#39;s gravatar image" />
<p><span>takje</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="takje has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-71645" class="comments-container">
&#10;</div>
<div id="comment-tools-71645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71645-form-container" class="comment-form-container">
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

