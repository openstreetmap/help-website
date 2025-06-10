+++
type = "question"
title = "Getting all maxspeed tags"
description = '''I&#x27;m Using http://www.overpass-api.de/api/xapi?[maxspeed=][bbox=42.378275,-71.089182,42.378475,-71.089382] URL to get max speed but its not work. Can any buddy suggest me the right way. From where i can create api for the same?'''
date = "2014-10-01T08:35:00Z"
lastmod = "2014-10-06T15:19:00Z"
weight = 37172
keywords = [ "maxspeed", "overpass", "api" ]
aliases = [ "/questions/37172" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting all maxspeed tags](/questions/37172/getting-all-maxspeed-tags)

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
<span id="post-37172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37172-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm Using <a href="http://www.overpass-api.de/api/xapi?">http://www.overpass-api.de/api/xapi?</a><em>[maxspeed=</em>][bbox=42.378275,-71.089182,42.378475,-71.089382] URL to get max speed but its not work. Can any buddy suggest me the right way.</p>
<p>From where i can create api for the same?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Oct '14, 08:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a85348500bd1961aaf51907b736e9c77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Omkar%20Bodke&#39;s gravatar image" />
<p><span>Omkar Bodke</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Omkar Bodke has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Oct '14, 18:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-37172" class="comments-container">
<span id="37193"></span>
<div id="comment-37193" class="comment">
<div id="post-37193-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please tell us in detail WHAT does not work!</p>
<p>Do you think that a mechanic can help you if you tell him just: "my car does not drive" ??</p>
<p>Have you tried already <a href="http://wiki.openstreetmap.org/wiki/Overpass_Turbo">http://wiki.openstreetmap.org/wiki/Overpass_Turbo</a> ? Read about all its features in the OSM wiki and built-in help pages.</p>
</div>
<div id="comment-37193-info" class="comment-info">
<span class="comment-age">(01 Oct '14, 16:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="37327"></span>
<div id="comment-37327" class="comment not_top_scorer">
<div id="post-37327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using this link to get maxspeed limit of road but is gives error like The data is made available under ODbL.</p>
<p>Error: line 4: static error: The value of attribute "n" of the element "bbox-query" must always be greater or equal than the value of attribute "s".</p>
<p>Error: line 10: static error: The value of attribute "n" of the element "bbox-query" must always be greater or equal than the value of attribute "s".</p>
<p>Error: line 17: static error: The value of attribute "n" of the element "bbox-query" must always be greater or equal than the value of attribute "s".</p>
</div>
<div id="comment-37327-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 07:29)</span> <span class="comment-user userinfo">Omkar Bodke</span>
</div>
</div>
<span id="37329"></span>
<div id="comment-37329" class="comment">
<div id="post-37329-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Your bounding box is wrong. The numbers must be left,bottom,right,top.</p>
</div>
<div id="comment-37329-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 08:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="37337"></span>
<div id="comment-37337" class="comment">
<div id="post-37337-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The correct URL would be <a href="http://www.overpass-api.de/api/xapi?*%5Bbbox=42.378275,-71.089382,42.378475,-71.089182%5D%5Bmaxspeed=*%5D"><code>http://www.overpass-api.de/api/xapi?*[bbox=42.378275,-71.089382,42.378475,-71.089182][maxspeed=*]</code></a> (second and forth number switched) but it doesn't return any elements because the bounding box you chose doesn't contain elements with a maxspeed tag. In fact, the bbox is somewhere in Antarctica. Did you mix lat and lon, too? In that case try this URL instead which returns data from Boston: <a href="http://www.overpass-api.de/api/xapi?*%5Bbbox=-71.089382,42.378275,-71.089182,42.378475%5D%5Bmaxspeed=*%5D"><code>http://www.overpass-api.de/api/xapi?*[bbox=-71.089382,42.378275,-71.089182,42.378475][maxspeed=*]</code></a></p>
</div>
<div id="comment-37337-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 12:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="37341"></span>
<div id="comment-37341" class="comment not_top_scorer">
<div id="post-37341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ohhh. This issue not allow me to go forward. <a href="http://www.overpass-api.de/api/xapi?">http://www.overpass-api.de/api/xapi?</a><em>[bbox=-77.015412,38.889732,-77.015212,38.889932][maxspeed=</em>] why this not return any maxspeed?</p>
</div>
<div id="comment-37341-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 14:22)</span> <span class="comment-user userinfo">Omkar Bodke</span>
</div>
</div>
<span id="37342"></span>
<div id="comment-37342" class="comment not_top_scorer">
<div id="post-37342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because your version is missing two "*" characters when compared to scai's version? Or is that just a "copy and paste issue" and you're actually worried that no matching data is being returned?</p>
</div>
<div id="comment-37342-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 14:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37343"></span>
<div id="comment-37343" class="comment not_top_scorer">
<div id="post-37343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually its not working even if we placed "*" character. And not return any maxspeed.</p>
</div>
<div id="comment-37343-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 15:08)</span> <span class="comment-user userinfo">Omkar Bodke</span>
</div>
</div>
<span id="37344"></span>
<div id="comment-37344" class="comment">
<div id="post-37344-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Your bounding box (which is different to the one in scai's example above) is a tiny area:</p>
<p><a href="http://owl.apis.dev.openstreetmap.org/?box=yes&amp;bbox=-77.015412%2C38.889932%2C-77.015212%2C38.889732#map=19/38.88982/-77.01594&amp;layers=N">http://owl.apis.dev.openstreetmap.org/?box=yes&amp;bbox=-77.015412%2C38.889932%2C-77.015212%2C38.889732#map=19/38.88982/-77.01594&amp;layers=N</a></p>
<p>The ways in it have no maxspeed tags:</p>
<p><a href="http://www.openstreetmap.org/way/6055099">http://www.openstreetmap.org/way/6055099</a></p>
<p><a href="http://www.openstreetmap.org/way/6062971">http://www.openstreetmap.org/way/6062971</a></p>
<p>EDIT: Clarified that the bbox used differs from the suggestion in the previous comment (just to make it absolutely clear!).</p>
</div>
<div id="comment-37344-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 15:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="37345"></span>
<div id="comment-37345" class="comment">
<div id="post-37345-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9742/omkar-bodke"></a><a href="http://help.openstreetmap.org/users/9742/omkar-bodke">@Omkar</a> The second URL in my previous comment returns two ways with maxspeed tags (<a href="http://www.openstreetmap.org/way/9429794">http://www.openstreetmap.org/way/9429794</a> and <a href="http://www.openstreetmap.org/way/257681343">http://www.openstreetmap.org/way/257681343</a> ).</p>
</div>
<div id="comment-37345-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 15:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37172" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-37172-form-container" class="comment-form-container">
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

<span id="37204"></span>

<div id="answer-container-37204" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37204-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Omkar Bodke has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer">http://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer</a></p>
<p>Check the link above ... it even has an example for maxspeed and bbox. Change way to * if you also want nodes and relations.</p>
<p>Btw: this page is horrible to use on a mobile device!!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '14, 18:30</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-37204" class="comments-container">
<span id="37332"></span>
<div id="comment-37332" class="comment">
<div id="post-37332-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. This is helpful for me.</p>
</div>
<div id="comment-37332-info" class="comment-info">
<span class="comment-age">(06 Oct '14, 11:04)</span> <span class="comment-user userinfo">Omkar Bodke</span>
</div>
</div>
</div>
<div id="comment-tools-37204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37204-form-container" class="comment-form-container">
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

