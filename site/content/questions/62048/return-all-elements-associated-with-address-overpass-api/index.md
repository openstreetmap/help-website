+++
type = "question"
title = "Return all elements associated with address - Overpass API"
description = '''Hi All,  I am quite new to OSM and am looking for help regarding gettting all the elements assoicated with a particular address using the Overpass API. So far I have managed to get the house number, street name and city of a particular area, however when I search a specific address on Nominatim, I s...'''
date = "2018-02-11T11:04:00Z"
lastmod = "2018-02-11T21:02:00Z"
weight = 62048
keywords = [ "overpass", "address" ]
aliases = [ "/questions/62048" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Return all elements associated with address - Overpass API](/questions/62048/return-all-elements-associated-with-address-overpass-api)

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
<span id="post-62048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62048-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I am quite new to OSM and am looking for help regarding gettting all the elements assoicated with a particular address using the Overpass API. So far I have managed to get the house number, street name and city of a particular area, however when I search a specific address on Nominatim, I see other elements associated with the address that are not appearing in my query. Certain elements associated with the address are tagged under place and boundary and I would like them included as a full address as listed under the address table in the following link - <a href="https://nominatim.openstreetmap.org/details.php?place_id=137891179">https://nominatim.openstreetmap.org/details.php?place_id=137891179</a></p>
<p>Any help would be greatly appreciated.</p>
<p>Thank you in advance</p>
<p>EDIT: Current (badly written) query:</p>
<p>[out:csv(::"id","addr:housenumber","addr:street","addr:postcode","addr:city", relation, "boundary:administrative")][timeout:25] [bbox:{{bbox}}]; (</p>
<p>node["addr:housenumber"]; way["addr:housenumber"]; relation["addr:housenumber"];</p>
<p>/ <em>node[name]; way[name]; relation[name];</em>/</p>
<p>node[place]; way[place]; relation[place];</p>
<p>node["boundary:administrative"]; way["boundary = administrative"]; relation["boundary = administrative"]; ); // print results out body;</p>
<blockquote>
<p>;out skel qt;</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '18, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/16a12e32ee0676ade5093f70a39d893e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rThornton93&#39;s gravatar image" />
<p><span>rThornton93</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rThornton93 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '18, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-62048" class="comments-container">
&#10;</div>
<div id="comment-tools-62048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62048-form-container" class="comment-form-container">
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

<span id="62049"></span>

<div id="answer-container-62049" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62049-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim can offer the full address hierarchy because it computes it upon loading the data into the database. Overpass, on the other hand, has to try and resolve your queries ("what admin_level=2 boundary is this location in") at runtime and hence takes vastly more computing resources. Even if you find the query to do this, running it more than once or twice a day would really consider abuse of the Overpass platform given that Nomniatim is so much more efficient in giving you the response you are looking for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '18, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62049" class="comments-container">
<span id="62050"></span>
<div id="comment-62050" class="comment">
<div id="post-62050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik,</p>
<p>Thank you for your prompt response. Based on what you have said, would it be possible for me to get the information I need by querying Nomniatim directly - if this is even possible?</p>
<p>Thank you in advance for your help.</p>
</div>
<div id="comment-62050-info" class="comment-info">
<span class="comment-age">(11 Feb '18, 14:49)</span> <span class="comment-user userinfo">rThornton93</span>
</div>
</div>
</div>
<div id="comment-tools-62049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62049-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62051"></span>

<div id="answer-container-62051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can retrieve boundaries from Overpass-API using the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29">is_in</a> query, but Overpass API does not support annotating the individual addresses with the information. So you'd end up implementing that aspect of Nominatim locally.</p>
<p>Nominatim has an <a href="https://help.openstreetmap.org/questions/62048/return-all-elements-associated-with-address-overpass-api">api for retrieving the address information for a given coordinate</a>. You'd have to call that api for each location you wanted information about. Make sure to follow the <a href="https://operations.osmfoundation.org/policies/nominatim/">use policy</a> if you use the public server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '18, 21:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-62051" class="comments-container">
&#10;</div>
<div id="comment-tools-62051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62051-form-container" class="comment-form-container">
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

