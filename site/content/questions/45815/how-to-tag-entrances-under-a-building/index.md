+++
type = "question"
title = "How to tag entrances under a building"
description = '''I am trying to correctly tag the following location:  It&#x27;s a block of apartments with a passage through the building. The block of flats is divided into several units, each with its own house number. The entrances to two house numbers (115 and 117, in this case) are located in the passage.  The pass...'''
date = "2015-10-09T12:15:00Z"
lastmod = "2015-10-22T12:45:00Z"
weight = 45815
keywords = [ "building_passage", "entrance", "tagging" ]
aliases = [ "/questions/45815" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag entrances under a building](/questions/45815/how-to-tag-entrances-under-a-building)

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
<span id="post-45815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45815-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to correctly tag the following location: <img src="/upfiles/IMG_7423_(3).jpg" alt="house entrances under passage" /></p>
<p>It's a block of apartments with a passage <em>through</em> the building. The block of flats is divided into several units, each with its own house number. The entrances to two house numbers (115 and 117, in this case) are located in the passage.</p>
<p>The passage through the building is easy - <code>highway=footway</code> and <code>tunnel=building_passage</code>. The two entrances are nodes with <code>entrance=yes</code> and <code>addr:housenumber=115</code> (or 117, respectively).</p>
<p>I would like to know how I should place the nodes for the entrances. Technically they are both on the path through the building - but then I would be placing them on top of each other, which doesn't seem to make sense (example: <span>way 339290816</span>). What I've done is I've added a "phantom" section of <code>highway=footway</code> connecting the main footway to the two entrances, in order to break them up, but still signify (to routing software) that the way to reach these entrances is to go into the passage:</p>
<p><img src="/upfiles/09-10-2015_12-54-25.png" alt="JOSM" /></p>
<p>Is this correct? In case someone wants to look it up in the database, it's <span>way 282416438</span>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building_passage" rel="tag" title="see questions tagged &#39;building_passage&#39;">building_passage</span> <span class="post-tag tag-link-entrance" rel="tag" title="see questions tagged &#39;entrance&#39;">entrance</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '15, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/390c3a1e9ea7b1f10deea61828ad66eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lightsider&#39;s gravatar image" />
<p><span>Lightsider</span><br />
<span class="score" title="1540 reputation points"><span>1.5k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lightsider has 9 accepted answers">42%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '15, 21:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</img>
</div>
</div>
<div id="comments-container-45815" class="comments-container">
<span id="45816"></span>
<div id="comment-45816" class="comment">
<div id="post-45816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I assume motor traffic cannot use this road, I don't think it is a service road, more like a track or footpath. but how are these wide paved paths normally mapped in your area do what they normally do in your town/country.</p>
</div>
<div id="comment-45816-info" class="comment-info">
<span class="comment-age">(09 Oct '15, 13:36)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="45817"></span>
<div id="comment-45817" class="comment">
<div id="post-45817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried out osrm router for car and it seems to use this sevice road.. is that correct</p>
</div>
<div id="comment-45817-info" class="comment-info">
<span class="comment-age">(09 Oct '15, 13:50)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="45859"></span>
<div id="comment-45859" class="comment">
<div id="post-45859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the road is designed for motor vehicles, although only for emergency services and the occasional delivery truck (the access roads are blocked off by bollards - I have to add them to the map).</p>
</div>
<div id="comment-45859-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 07:13)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
</div>
<div id="comment-tools-45815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45815-form-container" class="comment-form-container">
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

<span id="45822"></span>

<div id="answer-container-45822" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45822-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lightsider has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would change the service road to a footpath, unless cars are allowed. The short links should also be footpaths like the ones to the other entrances which I think is the best solution. If part of sevice road does allow cars and delivery vans then that section should stay as they are, but foot only section should be mapped as footpath. I had hoped that someone familiar with Hamberg may have offered advice by now. They now have the chance to vote up or down. Happy mapping</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '15, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '15, 09:56</strong> </span></p>
</div>
</div>
<div id="comments-container-45822" class="comments-container">
<span id="45860"></span>
<div id="comment-45860" class="comment">
<div id="post-45860-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Emergency vehicles and the occasional delivery truck (although I haven't confirmed the latter yet) are allowed, so I'll leave it as a service road.</p>
</div>
<div id="comment-45860-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 07:25)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
<span id="45867"></span>
<div id="comment-45867" class="comment">
<div id="post-45867-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5070/lightsider">@Lightsider</a>: I'd tend to map the main usage of this way, and that clearly is a footway rather than a service road. Many broader footpaths can be used by vehicles, but I think we should be mapping the primary role. If width is specifically designed to allow emergency access then I think you can tag this explicitly whilst still retaining the footway tag.</p>
</div>
<div id="comment-45867-info" class="comment-info">
<span class="comment-age">(13 Oct '15, 12:19)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="46051"></span>
<div id="comment-46051" class="comment">
<div id="post-46051-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In my opinion, the small connections to the actual entrances don't exist as such in reality and should therefore not be mapped. Routers will still be able to use the data if you omit them. If you do want an explicit connection between the way and the entrances, it would be better to use better use an area:highway=* area in addition to the way.</p>
</div>
<div id="comment-46051-info" class="comment-info">
<span class="comment-age">(22 Oct '15, 12:45)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-45822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45822-form-container" class="comment-form-container">
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

