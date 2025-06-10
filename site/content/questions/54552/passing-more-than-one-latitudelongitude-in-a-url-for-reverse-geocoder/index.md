+++
type = "question"
title = "Passing more than one latitude,longitude in a url for reverse geocoder"
description = '''Hi all I&#x27;m a newbie in GIS, so don&#x27;t know much about it One of the first things I&#x27;m trying to accomplish is this: I have a a list of latitude,longitude and I need to validated them I found this url (webservice) http://nominatim.openstreetmap.org/reverse?format=xml&amp;amp;lat=52.5487429714954&amp;amp;lon=-1...'''
date = "2017-02-08T15:07:00Z"
lastmod = "2017-02-13T19:58:00Z"
weight = 54552
keywords = [ "url", "latitude", "webservices", "longitude", "batch" ]
aliases = [ "/questions/54552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Passing more than one latitude,longitude in a url for reverse geocoder](/questions/54552/passing-more-than-one-latitudelongitude-in-a-url-for-reverse-geocoder)

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
<span id="post-54552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I'm a newbie in GIS, so don't know much about it One of the first things I'm trying to accomplish is this:</p>
<p>I have a a list of latitude,longitude and I need to validated them I found this url (webservice) <a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=1&amp;addressdetails=-1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=52.5487429714954&amp;lon=-1.81602098644987&amp;zoom=1&amp;addressdetails=-1</a></p>
<p>As you can see I can pass only one latitude,longitude. It is possible to pass a list of latitude,longitude to process them all at once? is there any procedure that I can use to do this? probably CURL</p>
<p>I really appreciate any guidance on this one.</p>
<p>Thanks in advance</p>
<p>Julio Leiva</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-webservices" rel="tag" title="see questions tagged &#39;webservices&#39;">webservices</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '17, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/30e1526867a53d05ee4e48f82bfd1346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Julio%20Leiva&#39;s gravatar image" />
<p><span>Julio Leiva</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Julio Leiva has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54552" class="comments-container">
&#10;</div>
<div id="comment-tools-54552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54552-form-container" class="comment-form-container">
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

<span id="54623"></span>

<div id="answer-container-54623" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54623-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure, but on <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a> we have some services beside Nominatim, maybe some are able to do reverse geocoding and that task in a batch? Please try to do some investigations yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '17, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-54623" class="comments-container">
&#10;</div>
<div id="comment-tools-54623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54623-form-container" class="comment-form-container">
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

