+++
type = "question"
title = "How to get the address from coordinates with Open Street Maps API?"
description = '''I developed an open-source APP in Cordova (it uses Javascript) and I&#x27;m using the Google Maps API, though as the APP is becoming popular my bill is increasing (not nice for a free, ad-free APP). Thus I&#x27;d like to move to Open Street Maps.  I&#x27;ve been reading the docs about the Overpass API but I see no...'''
date = "2021-03-06T14:23:00Z"
lastmod = "2023-01-05T16:47:00Z"
weight = 79139
keywords = [ "overpassapi", "reversegeocoding", "nominatim", "reverse" ]
aliases = [ "/questions/79139" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get the address from coordinates with Open Street Maps API?](/questions/79139/how-to-get-the-address-from-coordinates-with-open-street-maps-api)

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
<span id="post-79139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79139-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I developed an open-source APP in Cordova (it uses Javascript) and I'm using the Google Maps API, though as the APP is becoming popular my bill is increasing (not nice for a free, ad-free APP). Thus I'd like to move to Open Street Maps.</p>
<p>I've been reading the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">docs</a> about the Overpass API but I see no simple clear examples of code implementation. I know the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances">sever</a> to use, that I should use HTTP GET requests and use their special XML syntax. But it's not clear how do I pass that XML to the GET request. Furthermore the examples regarding coordinates provides as input a boundary box, not a point (or a point is considered as a square whose corners are the same?).</p>
<p>Could you kindly provide a simple example in Javascript (for example with <a href="https://api.jquery.com/jquery.ajax/"><code>$.ajax</code></a>) on how to get the address of a certain location by providing the geo-coordinates to the API?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '21, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/af81b55e4f9bd063e59e2a4e54bb5496?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jo%C3%A3o&#39;s gravatar image" />
<p><span>João</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="João has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '21, 16:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-79139" class="comments-container">
&#10;</div>
<div id="comment-tools-79139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79139-form-container" class="comment-form-container">
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

<span id="79141"></span>

<div id="answer-container-79141" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79141-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="João has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are looking for is reverse geocoding. This is rather a job for Nominatim - see <a href="https://nominatim.org">https://nominatim.org</a> for documentation. And there you can use json responses that are much easier for you to use. Please respect the nominatim usage policy - to be found here: <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> . It's maybe not a good idea to hardcode the nominatim endpoint operated by osm into an app. So maybe you would have to install your own nominatim instance or use one of the providers listed here: <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers">https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '21, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '21, 16:42</strong> </span></p>
</div>
</div>
<div id="comments-container-79141" class="comments-container">
<span id="79143"></span>
<div id="comment-79143" class="comment">
<div id="post-79143-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot, what do you think about my solution? <a href="https://github.com/jfoclpf/form-for-parking-violation/issues/85">https://github.com/jfoclpf/form-for-parking-violation/issues/85</a> and yes, I will respect the usage policy, surely much less than 1 request per second. Right now my APP has something like 2000 requests per month</p>
</div>
<div id="comment-79143-info" class="comment-info">
<span class="comment-age">(06 Mar '21, 19:06)</span> <span class="comment-user userinfo">João</span>
</div>
</div>
<span id="79145"></span>
<div id="comment-79145" class="comment">
<div id="post-79145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks good. I would add a version number to your User-Agent string, e.g.</p>
<p>xhr.setRequestHeader('User-Agent', 'com.form.parking.violation v0.1');</p>
<p>And 2000 a month does not sound like too much. But then versioning helps if the app gets more users and you have to change sth if v0.1 gets to many requests.</p>
<p>Please don't don't forget to accept the answer with the nominatim hint above if that helped.</p>
</div>
<div id="comment-79145-info" class="comment-info">
<span class="comment-age">(06 Mar '21, 19:37)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="79153"></span>
<div id="comment-79153" class="comment">
<div id="post-79153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again, I also shared the result in Stackoverflow: <a href="https://stackoverflow.com/a/66509433/1243247">https://stackoverflow.com/a/66509433/1243247</a></p>
</div>
<div id="comment-79153-info" class="comment-info">
<span class="comment-age">(07 Mar '21, 13:11)</span> <span class="comment-user userinfo">João</span>
</div>
</div>
<span id="79159"></span>
<div id="comment-79159" class="comment">
<div id="post-79159-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw, I realized now I can't change the http request headers (browsers won't allow it). May I use instead other means of ID, for example the email address such as seen <a href="https://nominatim.org/release-docs/develop/api/Reverse/#other">here</a>?</p>
</div>
<div id="comment-79159-info" class="comment-info">
<span class="comment-age">(07 Mar '21, 14:11)</span> <span class="comment-user userinfo">João</span>
</div>
</div>
<span id="86434"></span>
<div id="comment-86434" class="comment">
<div id="post-86434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Based on the answers above I am able to get the information I need. But I want to do this the right way, within the guidelines. What do I need to do for my app, should I apply for permission, request a special kind of commercial account, pay for it, how? Thanks in advance :)</p>
</div>
<div id="comment-86434-info" class="comment-info">
<span class="comment-age">(05 Jan '23, 16:42)</span> <span class="comment-user userinfo">freestyle212</span>
</div>
</div>
<span id="86435"></span>
<div id="comment-86435" class="comment not_top_scorer">
<div id="post-86435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/22590/freestyle212">@freestyle212</a>: for internal testing or if you have a really small usage footprint, you may follow the guidelines as described in the Nominatim usage policy. If you do want to use it for a business use case or commercial application, you should either run your own nominatim instance or use one of the third party providers listed here: <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers">https://wiki.openstreetmap.org/wiki/Nominatim#Alternatives_.2F_Third-party_providers</a></p>
</div>
<div id="comment-86435-info" class="comment-info">
<span class="comment-age">(05 Jan '23, 16:47)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-79141" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-79141-form-container" class="comment-form-container">
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

