+++
type = "question"
title = "Get a list of street names for zip"
description = '''Hello! As mentionned here (https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#List_of_streets) one can use [out:csv(&quot;name&quot;;false)]; area[name=&quot;Passau&quot;]; way(area)[highway][name]; out; to get all streets for a given city. However, A lot of streets are missing (for example in Pas...'''
date = "2020-03-03T14:03:00Z"
lastmod = "2020-03-03T23:18:00Z"
weight = 73332
keywords = [ "openstreetmap", "overpass-turbo" ]
aliases = [ "/questions/73332" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get a list of street names for zip](/questions/73332/get-a-list-of-street-names-for-zip)

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
<span id="post-73332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>As mentionned here (<a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#List_of_streets)">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#List_of_streets)</a> one can use</p>
<p><code>[out:csv("name";false)]; area[name="Passau"]; way(area)[highway][name]; out;</code></p>
<p>to get all streets for a given city.</p>
<p>However, A lot of streets are missing (for example in Passau, Germany). However, on openstreetmap.org on the official map the street can be found.</p>
<p>Am I missing something?</p>
<p>Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '20, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/4a1005d44d537160f06ec9789ac121f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vielhuber&#39;s gravatar image" />
<p><span>vielhuber</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vielhuber has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '20, 15:57</strong> </span></p>
</div>
</div>
<div id="comments-container-73332" class="comments-container">
&#10;</div>
<div id="comment-tools-73332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73332-form-container" class="comment-form-container">
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

<span id="73334"></span>

<div id="answer-container-73334" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had the wrong API endpoint URL.</p>
<p>Had to use: <a href="https://lz4.overpass-api.de/api/interpreter">https://lz4.overpass-api.de/api/interpreter</a> instead of <a href="https://overpass-api.de/api/interpreter.">https://overpass-api.de/api/interpreter.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '20, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/4a1005d44d537160f06ec9789ac121f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vielhuber&#39;s gravatar image" />
<p><span>vielhuber</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vielhuber has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73334" class="comments-container">
<span id="73336"></span>
<div id="comment-73336" class="comment">
<div id="post-73336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's weird, I got 9117 (non-uniq) results in either cases. Actually on the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances">wiki</a> I find that one URL is a redirection to the other (with a round-robin to another one).</p>
<p>Maybe a temporary problem on the server ?</p>
<p>Do you have missing streets examples ?</p>
<p>Regards</p>
</div>
<div id="comment-73336-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 20:55)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73339"></span>
<div id="comment-73339" class="comment">
<div id="post-73339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just try out:</p>
<p>[out:csv("name";false)]; area[name="Passau"]; way(area)[highway][name]; out;</p>
<p>On <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a> I don't find "Baumannstraße", on <a href="https://lz4.overpass-api.de/api/interpreter">https://lz4.overpass-api.de/api/interpreter</a> (via a direct request) I receive "Baumannstraße".</p>
</div>
<div id="comment-73339-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 21:05)</span> <span class="comment-user userinfo">vielhuber</span>
</div>
</div>
<span id="73347"></span>
<div id="comment-73347" class="comment">
<div id="post-73347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's really weird, as said before there's a 50-50 chance that it's the same server ! When I use lz4 through turbo, I get the same result, without Baumannstraße. But when I look specifically for it, it comes :</p>
<pre><code>[out:csv(&quot;name&quot;;false)]; area[name=&quot;Passau&quot;]; way(area)[highway][name=&quot;Baumannstraße&quot;]; out;</code></pre>
<p>And when I display the results of your query, the Baumannstraße is highlighted. But my browser can't find it in the data. :-( <a href="https://overpass-turbo.eu/s/Rh4">https://overpass-turbo.eu/s/Rh4</a></p>
</div>
<div id="comment-73347-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 22:40)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73348"></span>
<div id="comment-73348" class="comment">
<div id="post-73348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But when I download the data (either as OSM from the linked query, or as CSV from your query : <a href="https://overpass-api.de/api/interpreter?data=%5Bout%3Acsv%28%22name%22%3Bfalse%29%5D%3B%20area%5Bname%3D%22Passau%22%5D%3B%20way%28area%29%5Bhighway%5D%5Bname%5D%3B%20out%3B">https://overpass-api.de/api/interpreter?data=%5Bout%3Acsv%28%22name%22%3Bfalse%29%5D%3B%20area%5Bname%3D%22Passau%22%5D%3B%20way%28area%29%5Bhighway%5D%5Bname%5D%3B%20out%3B</a> ) I can find it in the downloaded file !</p>
<p>Well and it works again when I copy from the data tab to a file, so I guess the problem is with my browser search engine...</p>
<p>My browser is Firefox 68.5.0esr. Can you confirm it's only a browser problem ?</p>
</div>
<div id="comment-73348-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 22:50)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73350"></span>
<div id="comment-73350" class="comment">
<div id="post-73350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I can confirm that. When I do a GET request via console or Postman, I get both for <a href="https://lz4.overpass-api.de/api/interpreter">https://lz4.overpass-api.de/api/interpreter</a> and for <a href="https://overpass-api.de/api/interpreter">https://overpass-api.de/api/interpreter</a> "Baumannstraße". But not in the webinterface <a href="https://overpass-turbo.eu/.">https://overpass-turbo.eu/.</a></p>
</div>
<div id="comment-73350-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 23:18)</span> <span class="comment-user userinfo">vielhuber</span>
</div>
</div>
</div>
<div id="comment-tools-73334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73334-form-container" class="comment-form-container">
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

