+++
type = "question"
title = "Does overpass handle request&#x27;s sequentially?"
description = '''I have this local setup of overpass in a 32core 16Gb-ram server. My requests are not processing parallel, when i trigger multiple threads of the same request, the total time taken is = (time taken to complete one request * no of threads). Can someone point me towards what am missing here!! So i woul...'''
date = "2016-05-20T10:13:00Z"
lastmod = "2020-06-15T15:06:00Z"
weight = 49754
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/49754" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does overpass handle request's sequentially?](/questions/49754/does-overpass-handle-requests-sequentially)

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
<span id="post-49754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49754-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have this local setup of overpass in a 32core 16Gb-ram server. My requests are not processing parallel, when i trigger multiple threads of the same request, the total time taken is = (time taken to complete one request * no of threads). Can someone point me towards what am missing here!! So i would like to know if overpass handle's requests parallel or sequential ?</p>
<p>Tnx in advance - AG</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '16, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcf9d391ca68ff816e8f9f8ec9f3fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20Gowtham&#39;s gravatar image" />
<p><span>Arun Gowtham</span><br />
<span class="score" title="0 reputation points">0</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun Gowtham has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '16, 11:15</strong> </span></p>
</div>
</div>
<div id="comments-container-49754" class="comments-container">
&#10;</div>
<div id="comment-tools-49754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49754-form-container" class="comment-form-container">
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

<span id="49755"></span>

<div id="answer-container-49755" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49755-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you can see in the <a href="https://overpass-api.de/munin/localdomain/localhost.localdomain/osm_db_request_count.html">munin stats for the official server</a>, the server handles about 400-700 requests/minute. That for sure wouldn't be possible by processing a single request at a time. Also, the CPU utilization clearaly shows that all 8 cores all completely used up.</p>
<p>Conclusion: processing is parallel by default, each request is handled by a different Apache CGI process up to a certain limit.</p>
<p>Note that there's a limit of one request per IP at the same time on the official instance. That most likely doesn't apply if you're running your own instance, unless you set it up explicitly.</p>
<p>Unless you're adding more detail on your setup and your query, it's impossible to tell what kind of issues your might see on your local instance. It might also be that you're hitting some I/O limit or experiencing CPU saturation, too many parallel requests for your machine, internal scalability issues in the dispatcher, wrong/insufficient configuration of your web server, your load driver may not work properly. There are literally dozens of different influencing factors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '16, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '16, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-49755" class="comments-container">
<span id="49756"></span>
<div id="comment-49756" class="comment">
<div id="post-49756-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanx for the info <a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a> I'll debug my web server configuration's and look for issues anywhere else.</p>
</div>
<div id="comment-49756-info" class="comment-info">
<span class="comment-age">(20 May '16, 12:03)</span> <span class="comment-user userinfo">Arun Gowtham</span>
</div>
</div>
<span id="49757"></span>
<div id="comment-49757" class="comment">
<div id="post-49757-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi <a href="http://help.openstreetmap.org/users/8708/mmd"></a><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a></p>
<p>Here's the case am trying to solve:</p>
<p>My query: [out:json];area[name='Tamil Nadu'];node(area)[amenity='atm'];out count;</p>
<p>The time taken for this single request is :</p>
<p>1 new Thread started</p>
<p>Time taken for req :1 : 1936 (ms)</p>
<p>Whereas when i trigger 10 threads of the same request i get such result,</p>
<p>10 new Threads started</p>
<p>Time taken for req :1 : 1870 (ms)</p>
<p>Time taken for req :7 : 1869 (ms)</p>
<p>Time taken for req :2 : 1870 (ms)</p>
<p>Time taken for req :3 : 1870 (ms)</p>
<p>Time taken for req :8 : 1868 (ms)</p>
<p>Time taken for req :6 : 1869 (ms)</p>
<p>Time taken for req :5 : 1947 (ms)</p>
<p>Time taken for req :10 : 3588 (ms)</p>
<p>Time taken for req :4 : 3590 (ms)</p>
<p>Time taken for req :9 : 3950 (ms)</p>
<p>Is this normal, what i am expecting is all those 10 requests should have completed approximately around 1870 (ms), but it took additional time.</p>
<p>When i increase the thread count, say to 50, the total time taken goes upto 14 seconds.</p>
<p>When increased ever further to 500, i start to get 504 error's for nearly 370 of the requests and the time taken for entire set including the errors is 35 seconds</p>
<p>Please help me sort out this issue, is this functionality normal or have i configured wrong?! :(</p>
<p>Thanks-AG</p>
</div>
<div id="comment-49757-info" class="comment-info">
<span class="comment-age">(20 May '16, 12:39)</span> <span class="comment-user userinfo">Arun Gowtham</span>
</div>
</div>
<span id="49760"></span>
<div id="comment-49760" class="comment">
<div id="post-49760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it seems to scale fine up to 7 requests in parallel. Your system has 8 cores and surely has some other minor stuff to do while processing your requests. The remaining 3 requests take twice as long since they have to wait for the other requests to finish. Sounds fine to me. However I don't know any internals about Overpass. But just bumping up the allowed number of threads will usually have a negative impact on the system since they will also introduce additional overhead and will lead to processing more quests in parallel than the system can handle, slowing down each individual request.</p>
</div>
<div id="comment-49760-info" class="comment-info">
<span class="comment-age">(20 May '16, 14:21)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49761"></span>
<div id="comment-49761" class="comment">
<div id="post-49761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> actually my machine is 32 core cpu...</p>
</div>
<div id="comment-49761-info" class="comment-info">
<span class="comment-age">(20 May '16, 14:25)</span> <span class="comment-user userinfo">Arun Gowtham</span>
</div>
</div>
<span id="49762"></span>
<div id="comment-49762" class="comment">
<div id="post-49762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, sorry. I've taken the 8 cores mentioned in mmd's answer for your system. Anyway, as already explained by mmd there can be multiple other reasons like limited I/O. You can for example check your wa (=wait) in <code>top</code>.</p>
</div>
<div id="comment-49762-info" class="comment-info">
<span class="comment-age">(20 May '16, 14:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49763"></span>
<div id="comment-49763" class="comment not_top_scorer">
<div id="post-49763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yeah,i get you, i just wanted to know if what i stated above is not normal in overpass, so that i would start to debug elsewhere..</p>
</div>
<div id="comment-49763-info" class="comment-info">
<span class="comment-age">(20 May '16, 14:35)</span> <span class="comment-user userinfo">Arun Gowtham</span>
</div>
</div>
</div>
<div id="comment-tools-49755" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-49755-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75335"></span>

<div id="answer-container-75335" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75335-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We were facing the same problem, using an unofficial Docker image. It probably had a bug in its Nginx configuration. Updating this image solved it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '20, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/6ddb3ffa68da77e22f967daac3e2ea40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flogoe&#39;s gravatar image" />
<p><span>flogoe</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flogoe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75335" class="comments-container">
&#10;</div>
<div id="comment-tools-75335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75335-form-container" class="comment-form-container">
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

