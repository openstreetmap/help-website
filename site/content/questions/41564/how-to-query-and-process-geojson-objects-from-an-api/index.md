+++
type = "question"
title = "How to query and process GeoJSON objects from an API?"
description = '''For my master&#x27;s thesis, I need to geocode many postal addresses (my dataset provides zip code, city and street) that are all located in Germany. However, this was not successful for a subset of around 70,000 observations. Apparently, the geocoder failed to convert the addresses due to minor mistakes...'''
date = "2015-03-08T22:06:00Z"
lastmod = "2015-03-13T08:38:00Z"
weight = 41564
keywords = [ "auto-correct", "autocomplete", "api", "geocoding" ]
aliases = [ "/questions/41564" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to query and process GeoJSON objects from an API?](/questions/41564/how-to-query-and-process-geojson-objects-from-an-api)

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
<span id="post-41564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41564-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For my master's thesis, I need to geocode many postal addresses (my dataset provides zip code, city and street) that are all located in Germany. However, this was not successful for a subset of around 70,000 observations. Apparently, the geocoder failed to convert the addresses due to minor mistakes in the data. Eyeballing led me to the impression that the most prevalent reasons are the following</p>
<ul>
<li>minor spelling mistakes in terms of the city name. Example: "Neunburg v. Wald" instead of "Neunburg vorm Wald" or "Hessheim" instead of "Heßheim"</li>
<li>missing part of the name. Example: "Pohlheim" instead of "Pohlheim-Watzenborn"</li>
<li>the string in the city column refers to village that belongs to the city of interest</li>
<li>wrong match between zip code and city name (maybe because the address was recorded before a change in the zip code occured, e.g. two zip codes were merged)</li>
</ul>
<p><a href="http://photon.komoot.de/">Photon</a> appears to be able to identify many of the addresses which is why I would like to use their API to auto-correct my addresses. I would like to run a Java code on my local machine that queries a GeoJSON object for each of my addresses stored in a csv file using the Photon API and then save the answer in the very same file. This seems to be a standard problem but unfortunately I could not find a straight forward tutorial (I have little to no knowledge of Java). Is there available code which I can build upon? Thank you for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-auto-correct" rel="tag" title="see questions tagged &#39;auto-correct&#39;">auto-correct</span> <span class="post-tag tag-link-autocomplete" rel="tag" title="see questions tagged &#39;autocomplete&#39;">autocomplete</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '15, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/f1ac39ece091aedaeb2d8b0a48351daf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scoopert&#39;s gravatar image" />
<p><span>scoopert</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scoopert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '16, 11:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41564" class="comments-container">
&#10;</div>
<div id="comment-tools-41564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41564-form-container" class="comment-form-container">
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

<span id="41575"></span>

<div id="answer-container-41575" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41575-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While I don't quite see what significant hurdle learning enough Java to query an API and write the results to a file could be, you can obviously use any other language to access the API.</p>
<p>A further note: while we, obviously, can't speak for Komoot here, I suspect you should plan on running a local install of Photon for your project.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '15, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-41575" class="comments-container">
<span id="41576"></span>
<div id="comment-41576" class="comment">
<div id="post-41576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> thanks for your reply. Would you bother to give me a link that sets me up with sufficient material to tackle this problem? The problem is that I do not know what specifically I need to work through and with regards to my deadline I would like to avoid a lengthy search.</p>
</div>
<div id="comment-41576-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 14:20)</span> <span class="comment-user userinfo">scoopert</span>
</div>
</div>
<span id="41592"></span>
<div id="comment-41592" class="comment">
<div id="post-41592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You haven't indicated at all what level of (computer/programming) knowledge you have, further is java is a hard requirement or if there is a language you are comfortable with, that you would prefer etc.</p>
</div>
<div id="comment-41592-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 19:59)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="41593"></span>
<div id="comment-41593" class="comment">
<div id="post-41593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a very basic knowledge of programming: I started with PHP, continued with C (completed half an online course) and at some point took an introductory course in Java at university. I think that I know most basic concepts of programming but lack experience.</p>
</div>
<div id="comment-41593-info" class="comment-info">
<span class="comment-age">(09 Mar '15, 21:42)</span> <span class="comment-user userinfo">scoopert</span>
</div>
</div>
<span id="41630"></span>
<div id="comment-41630" class="comment">
<div id="post-41630-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I beleive any beginners JAVA textbook plus a google search for JAVA API JSON (turns up literally dozens of suitable examples) will be suficient.</p>
<p>Simply read the original addrss file, query photon, write the original address and the best match from Photon to the output file.</p>
</div>
<div id="comment-41630-info" class="comment-info">
<span class="comment-age">(11 Mar '15, 08:13)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="41670"></span>
<div id="comment-41670" class="comment">
<div id="post-41670-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2053/simonpoole"></a><a href="http://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a> As you claimed, it turned out not to be a major problem. Though it took me a whole day, now I have my code compiling and running using a csv file. However, I am not sure yet what logic I should implement to pick "the best match" from Photon to avoid that the coordinates refer to a completely different point in the country. One possibility I can imagine is that I exploit the fact that the postal address additionally provides the state. Thus, I can check whether Photon's response and my original data match. But this is a pretty poor check as states are big. Do you have a suggestion?</p>
</div>
<div id="comment-41670-info" class="comment-info">
<span class="comment-age">(13 Mar '15, 08:36)</span> <span class="comment-user userinfo">scoopert</span>
</div>
</div>
<span id="41671"></span>
<div id="comment-41671" class="comment not_top_scorer">
<div id="post-41671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a response to your note in your original post: I have checked with Komoot to ensure that I stay within their usage policy, so there's no problem in this regard.</p>
</div>
<div id="comment-41671-info" class="comment-info">
<span class="comment-age">(13 Mar '15, 08:38)</span> <span class="comment-user userinfo">scoopert</span>
</div>
</div>
</div>
<div id="comment-tools-41575" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-41575-form-container" class="comment-form-container">
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

