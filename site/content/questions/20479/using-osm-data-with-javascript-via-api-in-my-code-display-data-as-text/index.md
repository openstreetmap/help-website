+++
type = "question"
title = "Using OSM data with javascript via API (in my code, display data as text)"
description = '''Hi, Is the only way to use OSM Data by downloading them? There&#x27;s anyway to use the data with javascript via API without the need to download Data? if yes can you provide me with any example please. Thank you'''
date = "2013-03-04T12:53:00Z"
lastmod = "2013-03-05T14:58:00Z"
weight = 20479
keywords = [ "data", "use", "api", "osm", "javascript" ]
aliases = [ "/questions/20479" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using OSM data with javascript via API (in my code, display data as text)](/questions/20479/using-osm-data-with-javascript-via-api-in-my-code-display-data-as-text)

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
<span id="post-20479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20479-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Is the only way to use OSM Data by downloading them? There's anyway to use the data with javascript via API without the need to download Data? if yes can you provide me with any example please. Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-use" rel="tag" title="see questions tagged &#39;use&#39;">use</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '13, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e8897e88098c249a19794d0ecf25b206?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Berjawi&#39;s gravatar image" />
<p><span>Berjawi</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Berjawi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '13, 20:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-20479" class="comments-container">
&#10;</div>
<div id="comment-tools-20479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20479-form-container" class="comment-form-container">
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

<span id="20482"></span>

<div id="answer-container-20482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20482-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-20482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also use for example the overpass API to get all restaurants in a given geographic area as a JSON-formatted object, and then process this object using JavaScript. Is that what you want to do?</p>
<p>You would need to know the key-Value-combination(s) of your objects of interest and the lat/lon coordinates of the bounding box in which to search.</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];node[amenity=restaurant](50.7,7.1,50.8,7.25);out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '13, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '13, 14:56</strong> </span></p>
</div>
</div>
<div id="comments-container-20482" class="comments-container">
<span id="20487"></span>
<div id="comment-20487" class="comment">
<div id="post-20487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. Actually I tried this using javascript but its fail. check this code please: $(document).ready(function() { var url='http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];node<a href="50.7,7.1,50.8,7.25">amenity=restaurant</a>;out;'; $('#myBtn').click(function(){ $.getJSON(url, function(data) { alert('success');}).success(function(){alert('second success');}).error(function(){alert('error');}); }); });</p>
<p>I dont know why the result is always error !!</p>
</div>
<div id="comment-20487-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 15:48)</span> <span class="comment-user userinfo">Berjawi</span>
</div>
</div>
<span id="20488"></span>
<div id="comment-20488" class="comment">
<div id="post-20488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you are missing square brackets [ ] around amenity=restaurant</p>
</div>
<div id="comment-20488-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 16:10)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="20496"></span>
<div id="comment-20496" class="comment">
<div id="post-20496-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@gormo</span>: they were eaten by MarkDown. The code should have been written in a new line and indented by a space to display it as it is.</p>
</div>
<div id="comment-20496-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 20:30)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="20502"></span>
<div id="comment-20502" class="comment">
<div id="post-20502-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>$.getJSON(..) needs the success function in its third argument: <a href="http://api.jquery.com/jQuery.getJSON/">http://api.jquery.com/jQuery.getJSON/</a></p>
<p>The call itself and standalone returns JSON.</p>
</div>
<div id="comment-20502-info" class="comment-info">
<span class="comment-age">(05 Mar '13, 08:18)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="20510"></span>
<div id="comment-20510" class="comment">
<div id="post-20510-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here is an Example that works for me: <a href="http://pastebin.com/rfQgCPtZ">http://pastebin.com/rfQgCPtZ</a> . It's using JSONP, cause I could not get pure JSON running consistently because of the same origin policies(probably).</p>
</div>
<div id="comment-20510-info" class="comment-info">
<span class="comment-age">(05 Mar '13, 14:58)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20482-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20480"></span>

<div id="answer-container-20480" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20480-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Dear Berjawi, What do you mean by using OSM data ? There some protocols at the Wiki for commercial or any other use, but youre question needs some extra data to made clear whats behind your question. Take for instance a look here <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services.">http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '13, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-20480" class="comments-container">
<span id="20481"></span>
<div id="comment-20481" class="comment">
<div id="post-20481-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Hi, thank you for you answer. Here's a sample example : I want to search all restaurant near a given location, but I'll not display the data on a map, I just want to use the data on my code, lets tell display data as text.</p>
<p>What I understand from the wiki , that I can use API to search and download Data to my local, then put the data into a database and finally use data in the code from my database. there's any other way?</p>
</div>
<div id="comment-20481-info" class="comment-info">
<span class="comment-age">(04 Mar '13, 13:51)</span> <span class="comment-user userinfo">Berjawi</span>
</div>
</div>
</div>
<div id="comment-tools-20480" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20480-form-container" class="comment-form-container">
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

