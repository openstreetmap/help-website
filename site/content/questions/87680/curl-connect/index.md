+++
type = "question"
title = "Curl Connect"
description = '''Hello, We are facing a problem in using Openstreet map when I choose Openstreet Api in Geocoder API (primary) in the settings of openstreet map it shows an error on all devices &#x27;CURLE_COULDNT_CONNECT&#x27; It seems like openstreet map has blocked our server IP. Can you please let us know how to unblock t...'''
date = "2023-08-16T13:54:00Z"
lastmod = "2023-08-16T14:01:00Z"
weight = 87680
keywords = [ "openstreetmap" ]
aliases = [ "/questions/87680" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Curl Connect](/questions/87680/curl-connect)

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
<span id="post-87680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87680-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>We are facing a problem in using Openstreet map when I choose Openstreet Api in Geocoder API (primary) in the settings of openstreet map it shows an error on all devices 'CURLE_COULDNT_CONNECT' It seems like openstreet map has blocked our server IP. Can you please let us know how to unblock the IP of our server. Here is the detailed error:</p>
<p>CURLE_COULDNT_CONNECT: Failed to connect to nominatim.openstreetmap.... Connection refused.</p>
<p>Please help to resolve this issue.</p>
<p>Thankyou</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '23, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/31d3ce204f94bb90a0a62ddd192bf2e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rehan%20Butt&#39;s gravatar image" />
<p><span>Rehan Butt</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rehan Butt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87680" class="comments-container">
&#10;</div>
<div id="comment-tools-87680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87680-form-container" class="comment-form-container">
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

<span id="87681"></span>

<div id="answer-container-87681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87681-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are limitations on the use of the free Nominatim service. You have likely vilated one or more of the requirements in <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> - perhaps you have not identified yourselves properly, or made more than one request per second.</p>
<p>For heavy use, it is suggested to set up your own Nominatim server - that way you are bearing the cost of server operations, rather than using donation-sponsored OSM resources for your project. The data and the software are free to use - go to nominatim.org to learn how to install your own server.</p>
<p>There also commercial providers of Nominatim services in case you'd prefer someone else to do the work for you, see <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a> for a selection of providers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '23, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87681" class="comments-container">
&#10;</div>
<div id="comment-tools-87681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87681-form-container" class="comment-form-container">
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

