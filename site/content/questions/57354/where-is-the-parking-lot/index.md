+++
type = "question"
title = "Where is the parking lot?"
description = '''I am trying to make a parking area for buses and the closest thing I see is Car Parking. is there anyway to specify something that is not for just cars? Like trucks and buses?'''
date = "2017-07-30T18:45:00Z"
lastmod = "2017-08-01T22:55:00Z"
weight = 57354
keywords = [ "car", "parking_lot", "truck", "bus", "parking" ]
aliases = [ "/questions/57354" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Where is the parking lot?](/questions/57354/where-is-the-parking-lot)

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
<span id="post-57354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57354-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to make a parking area for buses and the closest thing I see is Car Parking. is there anyway to specify something that is not for just cars? Like trucks and buses?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-car" rel="tag" title="see questions tagged &#39;car&#39;">car</span> <span class="post-tag tag-link-parking_lot" rel="tag" title="see questions tagged &#39;parking_lot&#39;">parking_lot</span> <span class="post-tag tag-link-truck" rel="tag" title="see questions tagged &#39;truck&#39;">truck</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '17, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/bb3aee93ed1e4ac06ab7226e37adc5ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RichManSCTV0&#39;s gravatar image" />
<p><span>RichManSCTV0</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RichManSCTV0 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57354" class="comments-container">
&#10;</div>
<div id="comment-tools-57354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57354-form-container" class="comment-form-container">
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

<span id="57358"></span>

<div id="answer-container-57358" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57358-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-57358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RichManSCTV0 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like you are using the iD editor (this is the default, in browser editor).</p>
<p>The iD editor displays the actual tags used, but not prominently. Instead, it displays a iD specific descriptive name prominently. This is the box with a "P" icon, and "Car Parking" at the top of the left panel when a parking lot is selected.</p>
<p>In general this behaviour of iD is good, as it simplifies some of the complexity of the tagging schemas, and makes editing more accessible. In this case, though, it's misleading. The tag being used is not car specific, but rather (<a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking">as per the OSM Wiki</a>), is for "motor vehicles, such as cars and trucks". Buses would also be fine.</p>
<p>It wouldn't be wrong to just use what iD calls "Car Parking", so start by doing that. It is possible to do better though, so let's improve it a bit (if you're willing to put a bit more work in).</p>
<p>In iD, scroll the left panel down to the bottom, and look in the section called "All Tags". If it's the lot you just added it'll just have one tag <code>amenity=parking</code> (displayed in two table cells), click the plus icon, and add another line: <code>access=no</code>, and another line <code>bus=yes</code>. This means that the parking lot is not accessible for use in general, and that it is accessible for buses. (I think this is what you're going for, please correct me if I'm wrong)</p>
<p>Feel free to let us know if there's something about my answer that is unclear, or if I've made some incorrect assumptions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '17, 22:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '17, 15:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span></p>
</div>
</div>
<div id="comments-container-57358" class="comments-container">
<span id="57359"></span>
<div id="comment-57359" class="comment">
<div id="post-57359-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>One minor clarification: <code>bus=yes</code> means the parking is specifically for public service buses. If privately-owned buses are allowed as well, add the tag <code>tourist_bus=yes</code> instead.</p>
</div>
<div id="comment-57359-info" class="comment-info">
<span class="comment-age">(31 Jul '17, 03:18)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57361"></span>
<div id="comment-57361" class="comment">
<div id="post-57361-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/13665/dsh4">@dsh4</a>, I didn't know about that <code>tourist_bus</code> tag.</p>
</div>
<div id="comment-57361-info" class="comment-info">
<span class="comment-age">(31 Jul '17, 07:39)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="57380"></span>
<div id="comment-57380" class="comment">
<div id="post-57380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That sounds about right. It is a private lot for school buses so I set it access=no and bus=yes and it worked out right, there is even a spot to put the lot operator and I put the name of the bus co/school district.</p>
</div>
<div id="comment-57380-info" class="comment-info">
<span class="comment-age">(31 Jul '17, 14:57)</span> <span class="comment-user userinfo">RichManSCTV0</span>
</div>
</div>
<span id="57383"></span>
<div id="comment-57383" class="comment">
<div id="post-57383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a> Reference: <a href="https://wiki.openstreetmap.org/wiki/Key:access#Land-based_transportation">https://wiki.openstreetmap.org/wiki/Key:access#Land-based_transportation</a></p>
<p><a href="https://help.openstreetmap.org/users/14001/richmansctv0">@RichManSCTV0</a> Excellent.</p>
</div>
<div id="comment-57383-info" class="comment-info">
<span class="comment-age">(31 Jul '17, 16:37)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="57422"></span>
<div id="comment-57422" class="comment">
<div id="post-57422-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14001/richmansctv0">@richmansctv0</a>, that's great iD gives you a spot for the operator. There's no need to add more info than you already have, but I would like to point out there is <em>lots</em> of potential tags that could be added in the "All Tags" section. This allows any tag to be entered. The advantage of this is you can enter uncommon tags on subjects you take an interest in. The disadvantage is that it will accept non-standard tags, like mistakes or typos, and that it can be confusing, because of the huge numbers of OSM tags.</p>
<p>All that said it's worth being aware of the tags, and their potential.</p>
</div>
<div id="comment-57422-info" class="comment-info">
<span class="comment-age">(01 Aug '17, 22:55)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-57358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57358-form-container" class="comment-form-container">
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

