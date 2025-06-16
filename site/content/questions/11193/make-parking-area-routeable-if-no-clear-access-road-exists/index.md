+++
type = "question"
title = "Make parking area routeable if no clear access road exists"
description = '''When mapping parking areas, the wiki page cautions to &quot;create a routeable network&quot;. I assume this normally means linking the parking area to some access road (usually highway=service), which is in turn linked to the regular road network. Now I just mapped two small parking areas which have no clear ...'''
date = "2012-03-14T15:34:00Z"
lastmod = "2012-03-21T07:59:00Z"
weight = 11193
keywords = [ "mapping", "routing", "parking" ]
aliases = [ "/questions/11193" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Make parking area routeable if no clear access road exists](/questions/11193/make-parking-area-routeable-if-no-clear-access-road-exists)

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
<span id="post-11193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11193-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When mapping parking areas, the <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking">wiki page</a> cautions to "create a routeable network". I assume this normally means linking the parking area to some access road (usually <code>highway=service</code>), which is in turn linked to the regular road network.</p>
<p>Now I just mapped two small parking areas which have no clear access road. They are right next to the regular road, and can be entered along the whole lenght of the road which they touch:</p>
<p>See <a href="https://www.openstreetmap.org/?lat=50.942285&amp;lon=7.075751&amp;zoom=18&amp;layers=M">the area in OSM</a> and also <a href="http://maps.google.de/maps?q=br%C3%BCcker+sportpark&amp;hl=de&amp;ie=UTF8&amp;ll=50.942303,7.075335&amp;spn=0.001697,0.00339&amp;fb=1&amp;gl=de&amp;hq=br%C3%BCcker+sportpark&amp;hnear=br%C3%BCcker+sportpark&amp;cid=0,0,2981598483906891945&amp;t=h&amp;z=18">Google sat images</a></p>
<p>How should I map those to make sure they are routeable? I simply reused the nodes of the touching road when defining the parking area - is this the right way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '12, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-11193" class="comments-container">
&#10;</div>
<div id="comment-tools-11193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11193-form-container" class="comment-form-container">
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

<span id="11196"></span>

<div id="answer-container-11196" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11196-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sleske has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally, a routing engine will lead you to the nearest point on the nearest road when asked to go to an "off-road" place. This would work perfectly for your parking lots, even if you had not connected them to the road, so this is all fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '12, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11196" class="comments-container">
&#10;</div>
<div id="comment-tools-11196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11196-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11195"></span>

<div id="answer-container-11195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11195-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the Bing imagery were as good as the Google imagery, or if you took GPS traces, you could perhaps add the highway=service service=parking_aisle ways between the marked parking bays.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '12, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-11195" class="comments-container">
<span id="11375"></span>
<div id="comment-11375" class="comment">
<div id="post-11375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's an interesting suggestion, but at least for one of the parking areas (the northern one) this does not help, as it does not have any discernible markings - it's just a graveled area.</p>
</div>
<div id="comment-11375-info" class="comment-info">
<span class="comment-age">(21 Mar '12, 07:59)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-11195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11195-form-container" class="comment-form-container">
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

