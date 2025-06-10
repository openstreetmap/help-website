+++
type = "question"
title = "Nomintaim is returning HTML when asking for JSON in PHP"
description = '''The same URL through webbrowser returns JSON perfectly defined. When trying to acess through a PHP script (file_get_content or curl) I get the response in HTML when using &quot;format=json&quot; in the URL. I am working with Spanish data and response is correct but not in the format I am requesting it. This h...'''
date = "2015-10-23T09:03:00Z"
lastmod = "2015-10-28T11:47:00Z"
weight = 46064
keywords = [ "json", "nominatim", "html", "php" ]
aliases = [ "/questions/46064" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nomintaim is returning HTML when asking for JSON in PHP](/questions/46064/nomintaim-is-returning-html-when-asking-for-json-in-php)

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
<span id="post-46064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46064-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The same URL through webbrowser returns JSON perfectly defined. When trying to acess through a PHP script (file_get_content or curl) I get the response in HTML when using "format=json" in the URL. I am working with Spanish data and response is correct but not in the format I am requesting it.</p>
<p>This happens both, with a nominatim installed locally and with the public server from nominatim.openstreetmap.org. I tried this one to check if it was a problem of my installation. The response with the same parameters are identical in both servers.</p>
<p>I reviewed the documentation and it mentioned in wiki that the public webservice is open but that it is necessary to define correctly the referer or the agent so that it answers correctly. I make sure of copying agent header from the webbrowser request headers but it goes the same. I got a warning before that about not being able to find agent header in log.php from Nominatim, but after adding it no error is present anymore. However I still get not JSON response from scruipts. Anyway, I am not sure if headers could be the problem.</p>
<p>Anyone knows which is the correct header configuration to get the json response from PHP? Or do I have to change any configuration in my server to get json responses from scripts?</p>
<p><strong>Web Browser headers (firebug)</strong></p>
<p>Request:</p>
<ul>
<li>GET /nominatim/search.php?q=CALLE+POZO+SANTA+CATALINA+3+Ciudad+Real&amp;format=json&amp;addressdetails=1</li>
<li>HTTP/1.1 Host: local.ip</li>
<li>User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0</li>
<li>Accept: text/html,application/xhtml+xml,application/xml;q=0.9,<em>/</em>;q=0.8</li>
<li>Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3</li>
<li>Accept-Encoding: gzip, deflate</li>
<li>Cookie: PHPSESSID=guebk1lc2vu0ihaoedflmjhof1</li>
<li>Connection: keep-alive</li>
</ul>
<p>Also tried with nominatim.openstreetmap.org as host and same behaviour.</p>
<p>Response:</p>
<ul>
<li>HTTP/1.1 200 OK Date: Wed, 28 Oct 2015 09:01:40 GMT</li>
<li>Server: Apache/2.2.22 (Debian)</li>
<li>X-Powered-By: PHP/5.4.4-14+deb7u14</li>
<li>Access-Control-Allow-Origin: *</li>
<li>access-control-allow-methods: OPTIONS,GET</li>
<li>Vary: Accept-Encoding</li>
<li>Content-Encoding: gzip</li>
<li>Content-Length: 369 Keep-Alive: timeout=5, max=100</li>
<li>Connection: Keep-Alive</li>
<li>Content-Type: application/json; charset=UTF-8</li>
</ul>
<p><strong>Eclipse headers (debugging)</strong></p>
<p>Request:</p>
<ul>
<li>GET /nominatim/search.php?q=CALLE+POZO+SANTA+CATALINA+3+Ciudad Real&amp;format=json&amp;addressdetails=1 HTTP/1.1</li>
<li>User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0</li>
<li>Host: local.ip</li>
<li>Accept: */*</li>
</ul>
<p>User-Agent is copied and manually set from the original HTTP request in the PHP script. If not done, Eclipse it is not sending any user-agent header. This is the reason I thought it could be due to headers when reading OSM wiki about service.</p>
<p>Response:</p>
<ul>
<li>HTTP/1.1 200 OK Date: Wed, 28 Oct 2015 09:17:56 GMT</li>
<li>Server: Apache/2.2.22 (Debian)</li>
<li>X-Powered-By: PHP/5.4.4-14+deb7u14</li>
<li>Access-Control-Allow-Origin: *</li>
<li>Access-Control-Allow-Methods: OPTIONS,GET</li>
<li>Vary: Accept-Encoding</li>
<li>Connection: close</li>
<li>Content-Type: text/html; charset=UTF-8</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '15, 09:03</strong></p>
<img src="https://secure.gravatar.com/avatar/8ff71fc907067296fbfac86e637faa50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juanma%20MR&#39;s gravatar image" />
<p><span>Juanma MR</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juanma MR has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '15, 09:41</strong> </span></p>
</div>
</div>
<div id="comments-container-46064" class="comments-container">
<span id="46070"></span>
<div id="comment-46070" class="comment">
<div id="post-46070-score" class="comment-score">
4
</div>
<div class="comment-text">
<p><em>I make sure of copying agent header from the webbrowser request headers</em> -&gt; That's wrong. You should NOT fake a user agent, instead specify YOUR program. But that shouldn't be the problem. Can you post the complete HTTP request you are sending? Or compare it on your own with the request your browser sends. You can capture it by using wireshark or tcpdump.</p>
</div>
<div id="comment-46070-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 09:44)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46160"></span>
<div id="comment-46160" class="comment">
<div id="post-46160-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your response. I added the headers of both requests. Eclipse is not adding almost any header. This iis why I thought it could be due to headers but I am not sure which are the ones necessary if this is the problem.</p>
<p>It works the same in local or using nominatim.openstreetmap.org service.</p>
</div>
<div id="comment-46160-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 09:40)</span> <span class="comment-user userinfo">Juanma MR</span>
</div>
</div>
<span id="46161"></span>
<div id="comment-46161" class="comment">
<div id="post-46161-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One difference is that your browser offers <code>gzip</code> encoding in its request. This is then also chosen by Nominatim for its response. Your Eclipse doesn't offer this encoding. Maybe Nominatim needs gzip encoding for returning json? Try to add the header <code>Content-Encoding: gzip</code> to your request. Just a guess, I don't know anything about Nominatim's internals.</p>
</div>
<div id="comment-46161-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 09:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46172"></span>
<div id="comment-46172" class="comment">
<div id="post-46172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I got it. It was accept-encoding as you pointed out. Just wrote the answer. Thanks again.</p>
</div>
<div id="comment-46172-info" class="comment-info">
<span class="comment-age">(28 Oct '15, 11:47)</span> <span class="comment-user userinfo">Juanma MR</span>
</div>
</div>
</div>
<div id="comment-tools-46064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46064-form-container" class="comment-form-container">
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

<span id="46171"></span>

<div id="answer-container-46171" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46171-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks to <a href="https://help.openstreetmap.org/users/158/scai">scai</a> commnets I got the solution.</p>
<p>According to documentation it is necessary to send correctly referer or user-agent headers. However it is not true. It works without them, at least in my tests with the headers shown above without user-agent header.</p>
<p>However the accept-encoding in the request is compulsory as if Nominatim does not find it, will always response in HTML.</p>
<p>I have used curl for the tests and added this header with the following php function (just copied the string from the working web browser header):</p>
<blockquote>
<p>curl_setopt($curl, CURLOPT_ENCODING ,"gzip, deflate");</p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '15, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/8ff71fc907067296fbfac86e637faa50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juanma%20MR&#39;s gravatar image" />
<p><span>Juanma MR</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juanma MR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46171" class="comments-container">
&#10;</div>
<div id="comment-tools-46171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46171-form-container" class="comment-form-container">
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

