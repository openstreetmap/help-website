+++
type = "question"
title = "Generates exception in reverse geocoding using nominatim."
description = '''I&#x27;m creating asp.net website and using Nominatim for reverse geocoding to find address in simple text format. My Code: WebClient webClient = new WebClient(); var jsonData = webClient.DownloadData(&quot;http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=23.02951&amp;amp;lon=72.48689&quot;); DataContrac...'''
date = "2013-12-27T07:51:00Z"
lastmod = "2013-12-27T15:43:00Z"
weight = 29357
keywords = [ "asp.net", "nominatim" ]
aliases = [ "/questions/29357" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Generates exception in reverse geocoding using nominatim.](/questions/29357/generates-exception-in-reverse-geocoding-using-nominatim)

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
<span id="post-29357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29357-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm creating asp.net website and using Nominatim for reverse geocoding to find address in simple text format.</p>
<p>My Code:</p>
<pre><code>WebClient webClient = new WebClient();
var jsonData = webClient.DownloadData(&quot;http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=23.02951&amp;lon=72.48689&quot;);
DataContractJsonSerializer ser = new DataContractJsonSerializer(typeof(RootObject));
var rootObject = ser.ReadObject(new MemoryStream(jsonData));</code></pre>
<p>But got exception that</p>
<blockquote>
<p>The remote name could not be resolved: 'nominatim.openstreetmap.org'</p>
</blockquote>
<p>Actually I got null response from the page.</p>
<p>Any suggestion there?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-asp.net" rel="tag" title="see questions tagged &#39;asp.net&#39;">asp.net</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '13, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d6486fb620bab407a8c81f0c54a0551f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="netX&#39;s gravatar image" />
<p><span>netX</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="netX has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '13, 15:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-29357" class="comments-container">
<span id="29378"></span>
<div id="comment-29378" class="comment">
<div id="post-29378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are welcome here anytime and OSM community likes to help :)<br />
But please try to avoid crosspostings, as they consume a lot of ressources of the people that like to help you: <a href="http://stackoverflow.com/questions/20795389/reverse-geocoding-using-nominatim-in-asp-net">http://stackoverflow.com/questions/20795389/reverse-geocoding-using-nominatim-in-asp-net</a></p>
</div>
<div id="comment-29378-info" class="comment-info">
<span class="comment-age">(27 Dec '13, 15:43)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-29357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29357-form-container" class="comment-form-container">
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

<span id="29368"></span>

<div id="answer-container-29368" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29368-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try the URL in a browser on the same machine. It works fine here. If errors persist, must be a network issue on the machine where the code runs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '13, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-29368" class="comments-container">
&#10;</div>
<div id="comment-tools-29368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29368-form-container" class="comment-form-container">
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

