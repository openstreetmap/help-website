+++
type = "question"
title = "Automatic generation of longitude and latitude by giving the address in the backend?"
description = '''I want to generate the longitude and latitude values by giving address in the back-end. For example, If I inserted my address like area,city,state,country in the back-end then it should generate the longitude and latitude values and it should show the marker to that location.   This I have done in t...'''
date = "2011-02-22T10:44:00Z"
lastmod = "2013-07-29T06:55:00Z"
weight = 3259
keywords = [ "geocoding", "addresses" ]
aliases = [ "/questions/3259" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Automatic generation of longitude and latitude by giving the address in the backend?](/questions/3259/automatic-generation-of-longitude-and-latitude-by-giving-the-address-in-the-backend)

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
<span id="post-3259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3259-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to generate the longitude and latitude values by giving address in the back-end. For example, If I inserted my address like area,city,state,country in the back-end then it should generate the longitude and latitude values and it should show the marker to that location.<br />
</p>
<p>This I have done in the googlemap now I want to use it in the openstreetmap. Please help me with a sample code.</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '11, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/2d3396aea1746c845e5a0456df56322f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psn&#39;s gravatar image" />
<p><span>psn</span><br />
<span class="score" title="54 reputation points">54</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psn has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '11, 12:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-3259" class="comments-container">
<span id="3266"></span>
<div id="comment-3266" class="comment">
<div id="post-3266-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to try to guess what this means.</p>
<p>Guess number 1: You want a javascript map interface, and search box (on the interface) which does a call to a search service, and then places a marker at the location of the first match.</p>
<p>Guess number 2: You want server-side code (which language are you using?) to call a search service and generate a link of the form <a href="http://%22http://www.openstreetmap.org">"http://www.openstreetmap.org</a>/?lat=[Returned latitude]&amp;lon=[Returned logitude]&amp;zoom=14" spitting out the results to file e.g. for bulk geocoding spreadsheet data.</p>
<p>So which is it? Can you re-write you question more clearly.</p>
</div>
<div id="comment-3266-info" class="comment-info">
<span class="comment-age">(22 Feb '11, 13:31)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
<span id="3293"></span>
<div id="comment-3293" class="comment">
<div id="post-3293-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply, Your 2nd Guess matches to my question. I just give my input as city,state,country,etc. The output should show the marker to the given address. what i mean is the code should generate the longitude and latitude values and also have to generate the pointer to that location(based on the generated longitude and latitude values). Iam using PHP scripting.</p>
</div>
<div id="comment-3293-info" class="comment-info">
<span class="comment-age">(23 Feb '11, 06:04)</span> <span class="comment-user userinfo">psn</span>
</div>
</div>
</div>
<div id="comment-tools-3259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3259-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="3261"></span>

<div id="answer-container-3261" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3261-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take a look at the <a href="http://wiki.openstreetmap.org/wiki/Nominatim#Examples">Nominatim Examples</a> in the OpenStreetMap Wiki!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '11, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-3261" class="comments-container">
<span id="3264"></span>
<div id="comment-3264" class="comment">
<div id="post-3264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply, Not getting map. What i need is, i should have a choice to enter the address or by static like area,city,state,etc. After that the openstreetmap should display with the pointer with the given address.</p>
<p>once again thanks for your reply.</p>
</div>
<div id="comment-3264-info" class="comment-info">
<span class="comment-age">(22 Feb '11, 11:43)</span> <span class="comment-user userinfo">psn</span>
</div>
</div>
</div>
<div id="comment-tools-3261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3261-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3267"></span>

<div id="answer-container-3267" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3267-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a javascript search interface you might like to take a look at <a href="http://wiki.openstreetmap.org/wiki/FacilMap">FacilMap</a>, which bundles OpenLayers and add various bits. This includes an interface for searching, which calls the Nominatim search service, shows result matches, and places a marker (or markers) on the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '11, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-3267" class="comments-container">
&#10;</div>
<div id="comment-tools-3267" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3267-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24669"></span>

<div id="answer-container-24669" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24669-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you ever find a way to do this. I am trying to do the same using Python or objective c type code..</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '13, 06:55</strong></p>
<img src="https://secure.gravatar.com/avatar/dfc1979a08853053e1e0a89565d673a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abolfasl&#39;s gravatar image" />
<p><span>abolfasl</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abolfasl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24669" class="comments-container">
&#10;</div>
<div id="comment-tools-24669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24669-form-container" class="comment-form-container">
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

