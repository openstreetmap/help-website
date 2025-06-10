+++
type = "question"
title = "How to implement OpenStreetMap on the website / sharepoint environment"
description = '''Hello All It is first time I have come across the OpenStreetMap of which I am really amazed :) Congratulation to all the developers and participants...  My question is, how would I implement the MAP to show on my website where user can type in the From location and To location and in return the map ...'''
date = "2018-08-08T12:43:00Z"
lastmod = "2018-08-09T09:35:00Z"
weight = 65213
keywords = [ "website", "implementation", "sharepoint" ]
aliases = [ "/questions/65213" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to implement OpenStreetMap on the website / sharepoint environment](/questions/65213/how-to-implement-openstreetmap-on-the-website-sharepoint-environment)

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
<span id="post-65213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65213-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello All</p>
<p>It is first time I have come across the OpenStreetMap of which I am really amazed :)</p>
<p>Congratulation to all the developers and participants...</p>
<p>My question is, how would I implement the MAP to show on my website where user can type in the From location and To location and in return the map shows the route including the costing or miles.</p>
<p>I have come across a taxi company online (****.book.citytaxis.com/new-booking) using this map and their map shows the estimated cost. I assume the cost is calculated based on £x.xx per mile.</p>
<p>Anyway, I am slightly confused what needs to be done :) Ideally, I would wish this working on a SharePoint environment.</p>
<p>I hope it is a matter of downloading the .js files and linking it up?</p>
<p>Please advise in really simple terms for me to follow easily.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-implementation" rel="tag" title="see questions tagged &#39;implementation&#39;">implementation</span> <span class="post-tag tag-link-sharepoint" rel="tag" title="see questions tagged &#39;sharepoint&#39;">sharepoint</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '18, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9d06910537f6649995922e448a3b2e67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bimi82uk&#39;s gravatar image" />
<p><span>Bimi82uk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bimi82uk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '18, 12:45</strong> </span></p>
</div>
</div>
<div id="comments-container-65213" class="comments-container">
<span id="65226"></span>
<div id="comment-65226" class="comment">
<div id="post-65226-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Perhaps you should start reading <a href="https://wiki.openstreetmap.org/wiki/Develop">https://wiki.openstreetmap.org/wiki/Develop</a> which describes how you can use OpenStreetMap data.</p>
</div>
<div id="comment-65226-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 04:17)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="65230"></span>
<div id="comment-65230" class="comment">
<div id="post-65230-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, I did have a look at the WiKi Page and reason why I asked here is in hope SOMEBODY would take his/her time to explain simple term in a way or step by step process. And not like "here read the link" which is not very straight forward.</p>
</div>
<div id="comment-65230-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 08:27)</span> <span class="comment-user userinfo">Bimi82uk</span>
</div>
</div>
<span id="65231"></span>
<div id="comment-65231" class="comment">
<div id="post-65231-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15505/bimi82uk">@bimi82uk</a> I don't think that's likely to happen (especially with regards to how things fit into a Sharepoint environment).</p>
<p>It sounds like you have a number of requirements:</p>
<ul>
<li>Some sort of background map</li>
<li>A UI to request to / from places</li>
<li>A back-end routing API</li>
<li>A way of displaying routes on the background map</li>
<li>How to do all this beneath Sharepoint</li>
</ul>
<p>What I'd suggest is that you look at each of these in turn - break what you want to do into small manageable steps and look at each one in turn. For example, <a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>'s link already contains links to "Showing a Map" and "Routing/navigation", which address two of your requirements.</p>
</div>
<div id="comment-65231-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 08:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65232"></span>
<div id="comment-65232" class="comment">
<div id="post-65232-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a></p>
<p>Indeed, it is far from easy to follow the steps required. I assumed it would be a case of using the leaflet js files etc. but the "showing a map" just provides loads of framework of which I have no clue about ... nor implementing it.</p>
</div>
<div id="comment-65232-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 09:06)</span> <span class="comment-user userinfo">Bimi82uk</span>
</div>
</div>
<span id="65233"></span>
<div id="comment-65233" class="comment not_top_scorer">
<div id="post-65233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Furthermore,</p>
<p>I hoped that I could use a simple test on a blank simple html page. I can test it via html first to get the look and feel ... but I fail to understand what is required step by step.</p>
<p>I am not a coder nor a developer and this may explain why it is so difficult to follow through :/</p>
</div>
<div id="comment-65233-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 09:13)</span> <span class="comment-user userinfo">Bimi82uk</span>
</div>
</div>
<span id="65234"></span>
<div id="comment-65234" class="comment">
<div id="post-65234-score" class="comment-score">
2
</div>
<div class="comment-text">
<blockquote>
<p>I am not a coder nor a developer and this may explain why it is so difficult to follow through :/</p>
</blockquote>
<p>Indeed :)</p>
<p>However, <a href="https://leafletjs.com/examples.html">Leaflet</a> is an excellent place to start from - there are lots of examples there.</p>
</div>
<div id="comment-65234-info" class="comment-info">
<span class="comment-age">(09 Aug '18, 09:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65213" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-65213-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

