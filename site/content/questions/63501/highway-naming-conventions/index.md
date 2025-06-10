+++
type = "question"
title = "Highway Naming Conventions"
description = '''Greetings,  At this location you&#x27;ll see a few buildings with addresses located on, &quot;East US Highway 24&quot;. One of these addresses belongs to the Swiss Chalet. The Swiss Chalet lists an address on its own website as, &quot;19263 E. US Hwy 24&quot;. In OSM, the highway has no name. The ref is US 24.  https://www....'''
date = "2018-05-16T10:27:00Z"
lastmod = "2018-05-16T20:29:00Z"
weight = 63501
keywords = [ "tag", "ref", "alt_name", "highway", "name" ]
aliases = [ "/questions/63501" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Highway Naming Conventions](/questions/63501/highway-naming-conventions)

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
<span id="post-63501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings,</p>
<p>At this location you'll see a few buildings with addresses located on, "East US Highway 24". One of these addresses belongs to the Swiss Chalet. The Swiss Chalet lists an address on its own website as, "19263 E. US Hwy 24". In OSM, the highway has no name. The ref is US 24.</p>
<p><a href="https://www.openstreetmap.org/edit?way=95607441#map=18/38.97935/-105.04084">https://www.openstreetmap.org/edit?way=95607441#map=18/38.97935/-105.04084</a></p>
<p>1) What is the correct convention? Should I add, "East US 24" or "US 24" to the name field of the highway? Then link all these buildings to the name I've entered in the highway name field?</p>
<p>2) What if this highway already had a name such as, "Blue Mountain Highway", for example, but the highway ref was still US 24? I've seen many examples where businesses on a highway such as this list their addresses as the highway number of US 24 and ignore the name of the highway. In this scenario, if I add US 24 as an alt_name, will the business address link properly to a highway using an alt_name?</p>
<p>3) Does OSM prefer users avoid using a dash in highway names? Such as, US-24 or CO-37?</p>
<p>Cheers :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-ref" rel="tag" title="see questions tagged &#39;ref&#39;">ref</span> <span class="post-tag tag-link-alt_name" rel="tag" title="see questions tagged &#39;alt_name&#39;">alt_name</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '18, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/97e2f141b910d9a08dabfc0865382491?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chachafish&#39;s gravatar image" />
<p><span>chachafish</span><br />
<span class="score" title="411 reputation points">411</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chachafish has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-63501" class="comments-container">
&#10;</div>
<div id="comment-tools-63501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63501-form-container" class="comment-form-container">
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

<span id="63523"></span>

<div id="answer-container-63523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63523-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ran into the same issue when I was trying to clean up an old address import in San Diego county. Various addresses along some highways had things like "Hwy 79", "CA 79", etc. The highway itself did not have a name, only a ref tag.</p>
<p>The convention in OSM is to use the name that is on the signs on the ground. If you can survey the route or if you can see the signs captured from street cameras with suitable licensing (Mapillary or OpenStreetCam) then you know what to put for the name. But if all you have to go on is the addr:street value and it is varying all over the place then you really don't know what to put into the name field. In my case, I left the name field blank and have a mental note to drive out that way someday to so some sightseeing and mapping.</p>
<p>Conversely, if you have identified the official name I think it is a good idea to correct the addr:street values to match the name on the highway. Even if the official (signed) name on the highway does not match the name found in the businesses' advertising.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '18, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-63523" class="comments-container">
&#10;</div>
<div id="comment-tools-63523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63519"></span>

<div id="answer-container-63519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63519-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would say there isn't much of a consensus about what to do with names that are mostly based on the highway number. Something that looks just like the ref probably isn't worth it, so I would not put just "US 24" in the name tag. After that it starts to depend on how much the name is used. If lots of people call something "East US Highway 24" then it is probably a name. If 10 different businesses use 10 different versions of the name then I would say that the OSM highway shouldn't get any of them as a name.</p>
<p>The same sort of logic would apply to when to set an alt_name.</p>
<p>The majority of existing refs use a space instead of a dash, so there's no real reason to switch those. For names the best thing is probably to go with the local usage, if people write "East US-24" then use a dash, if they write "East US 24" then use a space.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '18, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63519" class="comments-container">
&#10;</div>
<div id="comment-tools-63519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63519-form-container" class="comment-form-container">
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

